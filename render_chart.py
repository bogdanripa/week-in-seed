#!/usr/bin/env python3
"""render_chart.py — CLI wrapper the routine calls: reads deals.json, writes a PNG.
Usage: python render_chart.py deals.json assets/header.png
"""
import json, sys
sys.path.insert(0, "src")
from images import header_chart

def main():
    deals_path = sys.argv[1] if len(sys.argv) > 1 else "deals.json"
    out_path = sys.argv[2] if len(sys.argv) > 2 else "assets/header.png"
    spec = json.load(open(deals_path))
    header_chart(
        deals=spec["deals"],
        caption=spec.get("caption", "Source: public funding announcements"),
        out_path=out_path,
        title=spec.get("title", "Early-stage rounds this week"),
    )
    print(f"wrote {out_path}")

if __name__ == "__main__":
    main()
