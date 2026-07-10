#!/usr/bin/env python3
"""render_header.py — CLI the routine calls: renders the issue header image.

Usage: python render_header.py header.json assets/header.png
header.json:
  {"photo_query": "<2-5 concrete words naming a real, photographable scene>",
   "concept": "<one evocative sentence distilling the week's themes>",
   "mood": "ember|deep|dawn|moss|solar|mist"}   # mood optional

Preferred path: a REAL photograph (photorealistic, grounded in reality) found
on Openverse via photo_query — public-domain/CC0 preferred, CC-BY accepted.
On success a header-credit.json is written next to the image with attribution;
add the credit line to the article when the license requires it.

Fallback: if the photo fetch fails (network policy, no results), the old
generative abstract art is rendered from `concept` — flag the fallback in the
run report.
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))
from images import abstract_header, PALETTES
from photos import photo_header, PhotoError


def main():
    spec_path = sys.argv[1] if len(sys.argv) > 1 else "header.json"
    out_path = sys.argv[2] if len(sys.argv) > 2 else "assets/header.png"
    spec = json.load(open(spec_path))
    query = (spec.get("photo_query") or "").strip()
    concept = (spec.get("concept") or "").strip()
    if not query and not concept:
        raise SystemExit('header.json needs "photo_query" (preferred) and/or "concept" (fallback).')
    mood = spec.get("mood")
    if mood is not None and mood not in PALETTES:
        raise SystemExit(f"unknown mood {mood!r}; pick one of {', '.join(PALETTES)} or omit it.")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)  # assets/ may be absent in a fresh clone

    if query:
        try:
            credit = photo_header(query, out_path)
        except PhotoError as e:
            print(f"[warn] photo fetch failed ({e}) — falling back to abstract art", file=sys.stderr)
        else:
            credit_path = os.path.join(out_dir or ".", "header-credit.json")
            with open(credit_path, "w") as f:
                json.dump(credit, f, indent=2)
            print(f"wrote {out_path} (photo: \"{credit['title']}\" by {credit['creator']}, "
                  f"{credit['license']}) + {credit_path}")
            if credit["attribution_required"]:
                print("attribution REQUIRED — add to the article footer:\n"
                      f"*Header photo: \"{credit['title']}\" by {credit['creator']}, "
                      f"[{credit['license']}]({credit['license_url']}), via [Openverse]({credit['source_url']}).*")
            return

    if not concept:
        raise SystemExit("photo fetch failed and header.json has no \"concept\" to fall back on.")
    abstract_header(concept, out_path, mood=mood)
    print(f"wrote {out_path} (abstract-art fallback)")


if __name__ == "__main__":
    main()
