#!/usr/bin/env python3
"""publish_substack.py — CLI wrapper the routine calls to create a Substack draft.
Usage: python publish_substack.py output/2026-07-08-digest.md assets/header.png
Parses the markdown file back into title/subtitle/body and calls src/publish.py.
"""
import sys, re, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))
from publish import create_draft

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
    md_path = sys.argv[1]
    img = sys.argv[2] if len(sys.argv) > 2 else None
    article = parse_md(md_path)
    if not article["title"]:
        raise SystemExit("Could not find an H1 title in the markdown.")
    result = create_draft(article, header_image_path=img)
    print(result)

if __name__ == "__main__":
    main()
