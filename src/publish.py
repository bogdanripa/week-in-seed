"""
publish.py — publishes the article to Substack via `python-substack`
(the unofficial client; Substack has no official publishing API).

The post goes out DIRECTLY: draft created, tagged, then published (send=True
emails subscribers). Set AUTO_PUBLISH=false in the environment to fall back
to draft-only mode for testing.

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


def publish_article(article: dict, header_image_path: str | None = None,
                    tags: list[str] | None = None) -> dict:
    api = _make_api()
    user_id = api.get_user_id()

    post = Post(title=article["title"], subtitle=article.get("subtitle", ""), user_id=user_id)

    # Header image first (uploaded to Substack, then embedded).
    if header_image_path:
        try:
            image = api.get_image(header_image_path)  # uploads, returns {"url": ...}
            # must go through Post.add: captioned_image() alone indexes
            # draft_body["content"][-1], which IndexErrors on an empty draft
            post.add({"type": "captionedImage", "src": image["url"], "alt": article["title"]})
        except Exception as e:  # never let an image failure block the post
            print(f"[warn] header image upload failed, continuing without it: {e}")

    # api= lets the renderer upload any local images referenced in the markdown
    post.from_markdown(article["body_markdown"], api=api)

    draft = api.post_draft(post.get_draft())
    post_id = draft.get("id")

    applied_tags = []
    for tag in tags or []:
        try:  # never let a tag failure block publishing
            api.add_tag_to_post(post_id, tag)
            applied_tags.append(tag)
        except Exception as e:
            print(f"[warn] tag {tag!r} failed: {e}")

    if CONFIG.get("auto_publish"):
        api.prepublish_draft(post_id)
        api.publish_draft(post_id)  # send=True — emails subscribers
        print(f"[ok] PUBLISHED post {post_id} (tags: {', '.join(applied_tags) or 'none'})")
        return {"post_id": post_id, "published": True, "tags": applied_tags}

    print(f"[ok] DRAFT {post_id} created (AUTO_PUBLISH=false) — review at "
          f"{CONFIG['substack_publication_url']}/publish/posts")
    return {"post_id": post_id, "published": False, "tags": applied_tags}
