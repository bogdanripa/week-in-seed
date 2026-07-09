"""photos.py — fetches a real, openly-licensed photograph for the issue header.

Photorealistic by construction: the header is an actual photo of a real-world
scene, found on Openverse (no API key needed) with a concrete search query
distilled from the week's dominant theme. Public-domain/CC0 images are
preferred, CC-BY accepted; the caller gets attribution metadata back and must
credit the photographer in the article when the license requires it.

The image is center-cropped to the header aspect ratio and resized. Any
failure (network policy, no usable results) raises PhotoError so the caller
can fall back to the generative art in images.py.
"""
from __future__ import annotations
import io
import json
import urllib.error
import urllib.parse
import urllib.request

from PIL import Image

API = "https://api.openverse.org/v1/images/"
USER_AGENT = "week-in-seed/1.0 (weekly newsletter header; contact: repo owner)"
# public domain first, then CC0, then CC-BY (needs a credit line)
_LICENSE_RANK = {"pdm": 0, "cc0": 1, "by": 2}


class PhotoError(RuntimeError):
    """No photo could be fetched — caller should fall back to abstract art."""


def _get(url: str, timeout: int = 30) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def search_photo(query: str, min_width: int = 1100) -> dict:
    """Return the best Openverse result for `query` (a concrete, photographable
    real-world scene — 'container ship port cranes', not 'innovation')."""
    params = urllib.parse.urlencode({
        "q": query,
        "license": "pdm,cc0,by",
        "category": "photograph",
        "aspect_ratio": "wide",
        "size": "large",
        "page_size": "20",
    })
    try:
        data = json.loads(_get(f"{API}?{params}"))
    except (urllib.error.URLError, OSError, ValueError) as e:
        raise PhotoError(f"Openverse search failed: {e}") from e

    candidates = [
        r for r in data.get("results", [])
        if (r.get("width") or 0) >= min_width and r.get("url")
        and r.get("license") in _LICENSE_RANK
    ]
    if not candidates:
        raise PhotoError(f"no usable Openverse results for query {query!r}")
    # freest license first; within a license, highest resolution
    candidates.sort(key=lambda r: (_LICENSE_RANK[r["license"]], -(r.get("width") or 0)))
    return candidates[0]


def _crop_resize(img: Image.Image, width_px: int, height_px: int) -> Image.Image:
    """Center-crop to the target aspect ratio, then resize."""
    target = width_px / height_px
    w, h = img.size
    if w / h > target:  # too wide — crop the sides
        new_w = round(h * target)
        left = (w - new_w) // 2
        img = img.crop((left, 0, left + new_w, h))
    else:  # too tall — crop top/bottom
        new_h = round(w / target)
        top = (h - new_h) // 2
        img = img.crop((0, top, w, top + new_h))
    return img.resize((width_px, height_px), Image.LANCZOS)


def photo_header(query: str, out_path: str,
                 width_px: int = 1456, height_px: int = 819) -> dict:
    """Fetch a real photo for `query`, write it to out_path, return attribution.

    Returns {"title", "creator", "license", "license_url", "source_url",
    "attribution_required"} — when attribution_required is True the article
    must carry a photo credit line.
    """
    meta = search_photo(query)
    try:
        raw = _get(meta["url"], timeout=60)
        img = Image.open(io.BytesIO(raw))
        img.load()
    except (urllib.error.URLError, OSError) as e:
        raise PhotoError(f"photo download failed: {e}") from e
    img = _crop_resize(img.convert("RGB"), width_px, height_px)
    img.save(out_path)
    lic = meta["license"]
    return {
        "title": meta.get("title") or "Untitled",
        "creator": meta.get("creator") or "unknown",
        "license": ("Public Domain" if lic == "pdm" else lic.upper().replace("BY", "CC BY")),
        "license_url": meta.get("license_url") or "",
        "source_url": meta.get("foreign_landing_url") or meta.get("url"),
        "attribution_required": lic == "by",
    }
