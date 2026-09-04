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

    # python-substack's add_tag_to_post matches existing tags case-sensitively,
    # so "Venture Capital" doesn't match a stored "venture capital" and it
    # tries (and fails) to create a duplicate. Resolve case-insensitively
    # against what's already on the publication before adding.
    existing_by_lower = {t["name"].lower(): t["name"] for t in (api.get_publication_post_tags() or [])}

    applied_tags = []
    for tag in tags or []:
        resolved = existing_by_lower.get(tag.lower(), tag)
        try:  # never let a tag failure block publishing
            api.add_tag_to_post(post_id, resolved)
            applied_tags.append(resolved)
        except Exception as e:
            print(f"[warn] tag {tag!r} failed: {e}")

    if CONFIG.get("auto_publish"):
        api.prepublish_draft(post_id)
        api.publish_draft(post_id)  # send=True — emails subscribers
        # publish_draft's response doesn't reliably carry the slug, so look
        # the post back up by id to build its canonical URL for the report.
        post_url = None
        try:
            for p in api.get_published_posts(limit=5).get("posts", []):
                if p.get("id") == post_id:
                    post_url = f"{CONFIG['substack_publication_url']}/p/{p['slug']}"
                    break
        except Exception as e:
            print(f"[warn] could not resolve post URL: {e}")
        print(f"[ok] PUBLISHED post {post_id} ({post_url or 'url unknown'}) "
              f"(tags: {', '.join(applied_tags) or 'none'})")
        return {"post_id": post_id, "url": post_url, "published": True, "tags": applied_tags}

    print(f"[ok] DRAFT {post_id} created (AUTO_PUBLISH=false) — review at "
          f"{CONFIG['substack_publication_url']}/publish/posts")
    return {"post_id": post_id, "published": False, "tags": applied_tags}
