"""
main.py — orchestrates the weekly run:
    research -> header chart -> save markdown -> create Substack draft

Run locally:
    python src/main.py                 # full run (creates a Substack draft)
    python src/main.py --dry-run       # research + chart + save, NO Substack call

Cloud Run: the module also exposes `handler(request)` for an HTTP trigger fired
weekly by Cloud Scheduler.
"""
from __future__ import annotations
import argparse
import datetime as dt
import json
import os
import sys

from config import CONFIG
from research import research_and_write
from images import abstract_header


def run(dry_run: bool = False) -> dict:
    out_dir = CONFIG["output_dir"]
    os.makedirs(out_dir, exist_ok=True)
    stamp = dt.date.today().isoformat()

    print("[1/4] researching + writing…")
    article = research_and_write()

    print("[2/4] rendering abstract header…")
    img_path = os.path.join(out_dir, f"{stamp}-header.png")
    concept = f"{article['title']} — {article.get('subtitle', '')}"
    abstract_header(concept, img_path)

    print("[3/4] saving markdown…")
    md_path = os.path.join(out_dir, f"{stamp}-digest.md")
    with open(md_path, "w") as f:
        if img_path:
            f.write(f"![header]({os.path.basename(img_path)})\n\n")
        f.write(f"# {article['title']}\n\n### {article.get('subtitle','')}\n\n")
        f.write(article["body_markdown"])
        if article.get("sources"):
            f.write("\n\n---\n**Sources:** " + " · ".join(
                f"[{s['title']}]({s['url']})" for s in article["sources"]))
    with open(os.path.join(out_dir, f"{stamp}-article.json"), "w") as f:
        json.dump(article, f, indent=2)

    print("      updating coverage.json (dedupe summary)…")
    import coverage
    coverage.update(md_path, stamp, CONFIG["coverage_path"])

    if dry_run:
        print(f"[4/4] dry-run: skipped Substack. Output in {out_dir}")
        return {"status": "dry_run", "markdown": md_path, "image": img_path}

    print("[4/4] creating Substack draft…")
    from publish import create_draft  # imported late so dry-runs need no substack lib
    result = create_draft(article, header_image_path=img_path)
    return {"status": "ok", "markdown": md_path, "image": img_path, **result}


def handler(request):
    """Cloud Run / Functions HTTP entrypoint."""
    dry = False
    try:
        dry = bool((request.get_json(silent=True) or {}).get("dry_run"))
    except Exception:
        pass
    return json.dumps(run(dry_run=dry))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    print(json.dumps(run(dry_run=args.dry_run), indent=2))
    sys.exit(0)
