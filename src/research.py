"""
research.py — one Anthropic API call that researches the week's early-stage
funding and returns a finished article as structured JSON.

Uses the server-side web_search tool, so no scraping infra is needed: Claude
does the retrieval and the drafting in a single call.
"""
from __future__ import annotations
import json
import os
import datetime as dt
from anthropic import Anthropic

from config import CONFIG
import coverage


def _week_window(today: dt.date | None = None) -> tuple[str, str]:
    today = today or dt.date.today()
    start = today - dt.timedelta(days=today.weekday() + 7)  # previous Mon
    end = start + dt.timedelta(days=6)                       # previous Sun
    return start.isoformat(), end.isoformat()


SYSTEM = """You are the research desk and lead writer for a weekly newsletter
called "{name}" that covers SEED and PRE-SEED venture funding.

Your job each week:
1. Use web_search to find the seed / pre-seed / pre-Series-A rounds ANNOUNCED
   in the target window, prioritising rounds led by or involving top firms
   ({firms}) plus notable accelerators (YC, Techstars, a16z Speedrun).
2. Verify each round against a primary or reputable secondary source. Never
   invent a round, a firm, an amount, or a quote. If you cannot confirm a
   detail, omit it. Search broadly across geographies (US / Silicon Valley,
   Europe, elsewhere) so no region is a blind spot, but select purely on deal
   merit — never favor Bay Area startups or add one to balance geography. If
   the week skews notably (e.g. zero Bay Area rounds), a one-line observation
   is enough.
3. Write a punchy, opinionated "state of early-stage investing" article.
   Structure: LEAD with the 2-3 trends tying the week together, then use the
   individual deals as evidence supporting each trend — analysis first, deal
   details second. No trailing "the pattern" recap. Lead with the answer, no
   throat-clearing. {voice}
4. Link each featured company's name to its homepage on first mention, and link
   the round's announcement (press release or the most credible coverage)
   inline where the round is described. Only link URLs your searches actually
   surfaced — never guess a URL.
5. When describing who a company sells to, give the IDEAL customer profile
   (role, company type, buying trigger) rather than a list of current customer
   names; put traction (paying customers, pilots, logos) with the round details.

Return ONLY a JSON object, no markdown fences, matching exactly:
{{
  "title": "string, <= 70 chars, format 'The Week in Seed: <this week's specific thesis>' — never the bare newsletter name; if it could headline any other week, rewrite it",
  "subtitle": "string, one line, the concrete particulars of this week (what was funded, what changed) — not a generic tagline",
  "header_photo_query": "string, 2-5 concrete words naming a real photographable scene matching the week's dominant theme (e.g. 'robotic arm factory floor') — never an abstraction",
  "body_markdown": "string, the full article in Markdown (no H1 title; start at ## sections)",
  "chart": {{
     "caption": "string",
     "deals": [{{"label": "Company (stage)", "amount_musd": number}}]  // 3-6 confirmed rounds for the header chart
  }},
  "sources": [{{"title": "string", "url": "string"}}]
}}
Amounts in the chart are in US$ millions; convert other currencies at a
reasonable rate and note it in the body if material."""


def research_and_write(today: dt.date | None = None) -> dict:
    client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    start, end = _week_window(today)

    voice = CONFIG.get("voice_instruction", "").strip()
    system = SYSTEM.format(
        name=CONFIG["newsletter_name"],
        firms=", ".join(CONFIG["tracked_firms"]),
        voice=voice or "Write in a clean, confident newsletter voice.",
    )

    user = (
        f"Target window: {start} to {end} (inclusive). "
        "Find and write up this week's seed and pre-seed activity. "
        "Do enough searches to cover the major early-stage rounds; a single "
        "search is not enough. Then return the JSON object."
    )
    dedupe = coverage.summary_for_prompt(CONFIG["coverage_path"])
    if dedupe:
        user += "\n\n" + dedupe

    resp = client.messages.create(
        model=CONFIG["model"],
        max_tokens=4096,
        system=system,
        tools=[{"type": "web_search_20250305", "name": "web_search", "max_uses": CONFIG["max_searches"]}],
        messages=[{"role": "user", "content": user}],
    )

    # The final text block holds the JSON; tool_use / tool_result blocks precede it.
    text = "".join(b.text for b in resp.content if b.type == "text").strip()
    text = text.removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    try:
        article = json.loads(text)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Model did not return valid JSON: {e}\n---\n{text[:2000]}")

    article["_window"] = {"start": start, "end": end}
    return article


if __name__ == "__main__":
    art = research_and_write()
    print(json.dumps(art, indent=2)[:3000])
