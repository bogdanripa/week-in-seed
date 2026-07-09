#!/usr/bin/env python3
"""render_header.py — CLI the routine calls: renders the abstract header image.

Usage: python render_header.py header.json assets/header.png
header.json: {"concept": "<one evocative sentence distilling the week's themes>",
              "mood": "ember|deep|dawn|moss|solar|mist"}   # mood optional

The art is generative (flow fields + glowing forms), seeded by the concept —
same concept, same image; new week, new image. Not a chart, no text drawn.
"""
import json
import os
import sys

sys.path.insert(0, "src")
from images import abstract_header, PALETTES


def main():
    spec_path = sys.argv[1] if len(sys.argv) > 1 else "header.json"
    out_path = sys.argv[2] if len(sys.argv) > 2 else "assets/header.png"
    spec = json.load(open(spec_path))
    if not spec.get("concept"):
        raise SystemExit("header.json needs a non-empty \"concept\".")
    mood = spec.get("mood")
    if mood is not None and mood not in PALETTES:
        raise SystemExit(f"unknown mood {mood!r}; pick one of {', '.join(PALETTES)} or omit it.")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)  # assets/ may be absent in a fresh clone
    abstract_header(spec["concept"], out_path, mood=mood)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
