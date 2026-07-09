"""
coverage.py — rolling summary of the last N published issues, kept in
coverage.json at the repo root and committed to GitHub.

Purpose: dedupe. Each run reads the summary before researching (so a round we
already featured is never presented as a fresh discovery) and appends its own
issue after writing.

The file stays small on purpose — themes + featured companies per issue, last
N issues only — so it can be injected straight into a research prompt.
"""
from __future__ import annotations
import json
import os
import re

_THEME_RE = re.compile(r"^## +(.+?)\s*$")
_COMPANY_RE = re.compile(r"^### +(.+?)\s*$")
_MD_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]*\)")  # [text](url) -> text
# ## sections that are article furniture, not investment themes
_NON_THEME = re.compile(r"^(the pattern|what to watch|this week's trends)", re.IGNORECASE)


def parse_article_md(md_text: str) -> dict:
    """Extract title, themes and featured companies from a digest markdown file.

    Relies on the article shape SKILL.md mandates: `# title`, `## <theme>`
    sections, `### <Company> — <amount> <stage> (led by <firm>)` entries.
    """
    title, themes, companies = "", [], []
    current_theme = None
    for line in md_text.splitlines():
        if line.startswith("# ") and not title:
            title = line[2:].strip()
            continue
        m = _THEME_RE.match(line)
        if m:
            heading = m.group(1).strip()
            if _NON_THEME.match(heading):
                current_theme = None
            else:
                current_theme = heading
                themes.append(heading)
            continue
        m = _COMPANY_RE.match(line)
        if m and current_theme is not None:
            # "[Hive](https://...) — $15M seed (led by SuperSeed)" -> name + details
            entry = _MD_LINK_RE.sub(r"\1", m.group(1).strip())
            name, _, details = (p.strip() for p in entry.partition("—"))
            companies.append({
                "name": name or entry,
                "round": details,
                "theme": current_theme,
            })
    return {"title": title, "themes": themes, "companies": companies}


def load(path: str = "coverage.json") -> dict:
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return {"max_issues": 12, "issues": []}


def update(md_path: str, date: str, path: str = "coverage.json") -> dict:
    """Parse one finished article and fold it into the rolling summary."""
    with open(md_path) as f:
        parsed = parse_article_md(f.read())
    cov = load(path)
    cov["issues"] = [i for i in cov["issues"] if i["date"] != date]  # idempotent re-runs
    cov["issues"].append({"date": date, **parsed})
    cov["issues"].sort(key=lambda i: i["date"])
    cov["issues"] = cov["issues"][-cov.get("max_issues", 12):]
    with open(path, "w") as f:
        json.dump(cov, f, indent=2, ensure_ascii=False)
        f.write("\n")
    return cov


def summary_for_prompt(path: str = "coverage.json") -> str:
    """Human-readable dedupe block to inject into the research prompt."""
    cov = load(path)
    if not cov["issues"]:
        return ""
    lines = ["Previously covered (do NOT re-feature these companies as fresh "
             "discoveries; only mention them again on genuinely new, material "
             "news, clearly labelled as an update):"]
    for issue in cov["issues"]:
        names = ", ".join(c["name"] for c in issue["companies"]) or "-"
        themes = "; ".join(issue["themes"]) or "-"
        lines.append(f"- {issue['date']} — themes: {themes} — companies: {names}")
    return "\n".join(lines)
