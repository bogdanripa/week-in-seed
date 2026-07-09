---
name: weekly-vc-digest
description: >
  Produce the weekly "Week in Seed" investment digest. Use when running the
  scheduled routine (weekly) or when asked to draft this week's seed/pre-seed
  roundup. Researches the week's early-stage rounds, analyses them by investment
  theme with a per-startup framework, renders a header chart, and creates a
  Substack draft.
---

# Weekly VC Digest — routine skill

You are the research desk and lead writer for **The Week in Seed**, a newsletter
covering **seed and pre-seed** venture funding. Run this end to end, autonomously.

## 1. Research (use web search)

Find seed / pre-seed / pre-Series-A rounds **announced in the last 7 days**,
prioritising rounds led by or involving top firms (Y Combinator, a16z, Sequoia,
General Catalyst, Accel, Lightspeed, Greylock, Kleiner Perkins, First Round,
Initialized, SuperSeed) and accelerators (YC, Techstars, a16z Speedrun).

**First, read the archive — no duplicates.** Before searching, read every past
issue so you never re-feature a round already covered:

```bash
ls sample_output/*.md                            # archive on the current branch
git fetch origin claude/weekly-digest 2>/dev/null && \
  git show origin/claude/weekly-digest -- 'sample_output/*.md' >/dev/null 2>&1 && \
  git ls-tree -r --name-only origin/claude/weekly-digest sample_output/
```

Read them all (from both branches) and build the list of previously featured
companies. A company already covered is OUT — unless there is genuinely new,
material news (a new round, a pivot), in which case feature it as a clearly
labelled **update**, never as a fresh discovery. Also avoid re-using last week's
theme names verbatim; if the same theme recurs, say so and build on it.

Rules:
- Do **several** searches, not one. Cross-check each round against a primary or
  reputable secondary source. Never invent a round, firm, amount, quote, or TAM.
- For every startup you'll feature, dig until you can fill the framework below.
  If you can't confirm a field, write "not disclosed" — don't guess.
- Target 3–5 featured companies. It's fine to include one just-past-seed round
  (e.g. an early Series A) if it anchors a theme — label the stage honestly.

## 2. Structure the article by INVESTMENT THEME

Do **not** write a flat list of rounds. Group them into 1–3 themes (e.g. "Physical
AI for the real economy", "Deep-tech infrastructure", "Vertical AI for X"). Open
each theme with the thesis and a TAM anchor, then break down each company:

```
### <Company> — <amount> <stage> (led by <firm>)
- **Problem:** what pain, for whom, why now
- **Product:** what they actually built
- **Customer:** who buys, named logos if disclosed
- **Stage:** round + total raised + traction caveats (pilots vs paid, etc.)
- **TAM:** size + source; give a RANGE and label analyst estimates as estimates
- **Moat:** the real defensible asset (data, distribution, IP, timing) — be skeptical
```

Then a **"The pattern"** section (2–3 numbered takeaways tying the themes together)
and a short **"What to watch next week."**

Voice: punchy, opinionated, investor-grade. Lead with the answer, no throat-clearing.
Press on moats — name the underwriting question, don't cheerlead. If a
`voice-guide.md` exists in the repo, follow it.

## 3. Render the header chart

Write the featured deals to `deals.json`:

```json
{"title": "Early-stage rounds — week of <Mon date>",
 "caption": "Source: <the outlets you actually used>",
 "deals": [{"label": "Company (stage)", "amount_musd": 15}, ...]}
```

Then run: `python render_chart.py deals.json assets/header.png`

## 4. Save + publish

- Write the article to `output/<YYYY-MM-DD>-digest.md` (header image first line,
  then `# title`, `### subtitle`, then body).
- **Auth bootstrap:** if `SUBSTACK_COOKIES_PATH` is unset but `SUBSTACK_SID` is set
  (the routine passes the cookie as an env var), write the cookies file first:
  ```bash
  printf '{"substack.sid": "%s"}' "$SUBSTACK_SID" > /tmp/substack_cookies.json
  export SUBSTACK_COOKIES_PATH=/tmp/substack_cookies.json
  ```
- Create the Substack **draft** (do not auto-publish):
  `python publish_substack.py output/<YYYY-MM-DD>-digest.md assets/header.png`
- If the publish step fails on a network/host error, the routine environment
  hasn't allowlisted `substack.com` — report that clearly instead of retrying.
- **Always archive** (publish success or not): copy the article to
  `sample_output/<YYYY-MM-DD>-weekly-digest.md` and the chart to
  `assets/<YYYY-MM-DD>-header.png`, and commit both. The archive is what future
  runs read to avoid featuring the same rounds twice.

## 5. Notify

If a Telegram or Slack connector is available, send a one-line "draft ready" note
with the Substack draft link. Otherwise just print the draft URL.

## Guardrails
- Accuracy over completeness. A short, correct digest beats a padded one.
- Every number traces to a source you actually read this run.
- TAM figures are directional; always show the range and the caveat.
