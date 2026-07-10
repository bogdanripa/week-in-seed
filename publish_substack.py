#!/usr/bin/env python3
"""publish_substack.py — CLI wrapper the routine calls to publish to Substack.
Usage: python publish_substack.py output/2026-07-08-digest.md assets/header.png --tags "AI,Venture Capital,Seed Funding"
Parses the markdown file back into title/subtitle/body and calls src/publish.py.
Publishes directly (emails subscribers) unless AUTO_PUBLISH=false in the env.
"""
import sys, re, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))
from publish import publish_article

def parse_md(path):
    lines = open(path).read().splitlines()
    title = subtitle = ""
    body = []
    for i, ln in enumerate(lines):
        if ln.startswith("# ") and not title:
            title = ln[2:].strip()
        elif ln.startswith("### ") and title and not subtitle:
            subtitle = ln[4:].strip()
        elif title:  # everything after the H1 (minus the first ### subtitle) is body
            if ln.startswith("### ") and ln[4:].strip() == subtitle:
                continue
            body.append(ln)
    return {"title": title, "subtitle": subtitle, "body_markdown": "\n".join(body).strip()}

def main():
    args = sys.argv[1:]
    tags = []
    if "--tags" in args:
        i = args.index("--tags")
        tags = [t.strip() for t in args[i + 1].split(",") if t.strip()]
        del args[i:i + 2]
    md_path = args[0]
    img = args[1] if len(args) > 1 else None
    article = parse_md(md_path)
    if not article["title"]:
        raise SystemExit("Could not find an H1 title in the markdown.")
    result = publish_article(article, header_image_path=img, tags=tags)
    print(result)

if __name__ == "__main__":
    main()
