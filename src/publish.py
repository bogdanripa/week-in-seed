"""
publish.py — pushes the article to Substack as a DRAFT via `python-substack`
(the unofficial client; Substack has no official publishing API).

Design choice: we create a draft and STOP. You review in the Substack editor and
hit publish. Flip AUTO_PUBLISH=True in config only once you trust the pipeline.

Auth: prefer a cookies file (connect.sid stays valid for months, best for headless
Cloud Run). Falls back to email/password. Put secrets in GCP Secret Manager.

    pip install python-substack   # import name is `substack`
"""
from __future__ import annotations
import os
import re
from substack import Api
from substack.post import Post

from config import CONFIG


# ---------- minimal Markdown -> Substack (ProseMirror) node converter ----------

_BOLD = re.compile(r"\*\*(.+?)\*\*")
_ITALIC = re.compile(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)")


def _inline(text: str) -> list[dict]:
    """Convert a line with **bold**/*italic* into text nodes with marks."""
    nodes, idx = [], 0
    # Handle bold first, then italics inside the leftovers (simple, good-enough).
    for m in _BOLD.finditer(text):
        if m.start() > idx:
            nodes += _italicize(text[idx:m.start()])
        nodes.append({"type": "text", "text": m.group(1), "marks": [{"type": "strong"}]})
        idx = m.end()
    if idx < len(text):
        nodes += _italicize(text[idx:])
    return nodes or [{"type": "text", "text": text}]


def _italicize(text: str) -> list[dict]:
    nodes, idx = [], 0
    for m in _ITALIC.finditer(text):
        if m.start() > idx:
            nodes.append({"type": "text", "text": text[idx:m.start()]})
        nodes.append({"type": "text", "text": m.group(1), "marks": [{"type": "em"}]})
        idx = m.end()
    if idx < len(text):
        nodes.append({"type": "text", "text": text[idx:]})
    return nodes


def markdown_to_nodes(md: str) -> list[dict]:
    nodes, bullets = [], []

    def flush_bullets():
        nonlocal bullets
        if bullets:
            nodes.append({"type": "bullet_list", "content": [
                {"type": "list_item", "content": [
                    {"type": "paragraph", "content": _inline(b)}]} for b in bullets]})
            bullets = []

    for raw in md.splitlines():
        line = raw.rstrip()
        if not line.strip():
            flush_bullets(); continue
        if line.startswith("### "):
            flush_bullets(); nodes.append({"type": "heading", "attrs": {"level": 3},
                                           "content": _inline(line[4:])})
        elif line.startswith("## "):
            flush_bullets(); nodes.append({"type": "heading", "attrs": {"level": 2},
                                           "content": _inline(line[3:])})
        elif re.match(r"^\s*[-*]\s+", line):
            bullets.append(re.sub(r"^\s*[-*]\s+", "", line))
        elif re.match(r"^\s*\d+\.\s+", line):
            bullets.append(re.sub(r"^\s*\d+\.\s+", "", line))
        else:
            flush_bullets(); nodes.append({"type": "paragraph", "content": _inline(line)})
    flush_bullets()
    return nodes


# ------------------------------- publishing ------------------------------------

def _make_api() -> Api:
    cookies = CONFIG.get("substack_cookies_path") or os.environ.get("SUBSTACK_COOKIES_PATH")
    pub = CONFIG["substack_publication_url"]
    if cookies:
        return Api(cookies_path=cookies, publication_url=pub)
    return Api(email=os.environ["SUBSTACK_EMAIL"],
               password=os.environ["SUBSTACK_PASSWORD"],
               publication_url=pub)


def create_draft(article: dict, header_image_path: str | None = None) -> dict:
    api = _make_api()
    user_id = api.get_user_id()

    post = Post(title=article["title"], subtitle=article.get("subtitle", ""), user_id=user_id)

    # Header image first (uploaded to Substack, then embedded).
    if header_image_path:
        try:
            image = api.get_image(header_image_path)  # uploads, returns {"url": ...}
            # python-substack's Post.add() unpacks this dict into captioned_image(**kwargs)
            post.add({"type": "captionedImage", "src": image["url"], "alt": article["title"]})
        except Exception as e:  # never let an image failure block the draft
            print(f"[warn] header image upload failed, continuing without it: {e}")

    for node in markdown_to_nodes(article["body_markdown"]):
        post.add(node)

    draft = api.post_draft(post.get_draft())
    draft_id = draft.get("id")

    if CONFIG.get("auto_publish"):
        api.prepublish_draft(draft_id)
        api.publish_draft(draft_id)
        print(f"[ok] PUBLISHED draft {draft_id}")
    else:
        print(f"[ok] DRAFT {draft_id} created — review at {CONFIG['substack_publication_url']}/publish/posts")
    return {"draft_id": draft_id, "auto_published": bool(CONFIG.get("auto_publish"))}
