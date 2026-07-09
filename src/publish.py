"""
publish.py — pushes the article to Substack as a DRAFT via `python-substack`
(the unofficial client; Substack has no official publishing API).

Design choice: we create a draft and STOP. You review in the Substack editor and
hit publish. Flip AUTO_PUBLISH=True in config only once you trust the pipeline.

Auth: prefer a cookies file (the `substack.sid` cookie stays valid for months,
best for headless runs). Falls back to email/password.

Markdown conversion is delegated to the library's own `Post.from_markdown`
(substack.mdrender) — it produces ProseMirror JSON that Substack's tiptap
editor actually accepts. Do NOT hand-roll nodes and feed them to `Post.add`:
its text-chunk format ({"content": ..., "marks": ...}) silently mangles
{"type": "text", "text": ...} nodes into null-text garbage that makes the
draft unopenable in the editor ("Invalid JSON content", seen 2026-07-09).

    pip install python-substack   # import name is `substack`
"""
from __future__ import annotations
import os

from substack import Api
from substack.post import Post

from config import CONFIG


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
            post.captioned_image(src=image["url"], alt=article["title"])
        except Exception as e:  # never let an image failure block the draft
            print(f"[warn] header image upload failed, continuing without it: {e}")

    # api= lets the renderer upload any local images referenced in the markdown
    post.from_markdown(article["body_markdown"], api=api)

    draft = api.post_draft(post.get_draft())
    draft_id = draft.get("id")

    if CONFIG.get("auto_publish"):
        api.prepublish_draft(draft_id)
        api.publish_draft(draft_id)
        print(f"[ok] PUBLISHED draft {draft_id}")
    else:
        print(f"[ok] DRAFT {draft_id} created — review at {CONFIG['substack_publication_url']}/publish/posts")
    return {"draft_id": draft_id, "auto_published": bool(CONFIG.get("auto_publish"))}
