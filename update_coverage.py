#!/usr/bin/env python3
"""update_coverage.py — CLI the routine calls after writing an article.

Folds the finished digest into coverage.json (rolling last-N summary used for
dedupe) and prints the updated dedupe block.

Usage: python update_coverage.py sample_output/2026-07-13-weekly-digest.md [YYYY-MM-DD]
The date defaults to the YYYY-MM-DD prefix of the markdown filename.
"""
import os
import re
import sys

sys.path.insert(0, "src")
import coverage


def main():
    md_path = sys.argv[1]
    if len(sys.argv) > 2:
        date = sys.argv[2]
    else:
        m = re.match(r"(\d{4}-\d{2}-\d{2})", os.path.basename(md_path))
        if not m:
            raise SystemExit("Filename has no YYYY-MM-DD prefix; pass the date as 2nd arg.")
        date = m.group(1)
    cov = coverage.update(md_path, date)
    print(f"[ok] coverage.json updated — {len(cov['issues'])} issue(s) tracked "
          f"(max {cov.get('max_issues', 12)})")
    print(coverage.summary_for_prompt())


if __name__ == "__main__":
    main()
