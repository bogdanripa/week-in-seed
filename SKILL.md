---
name: weekly-vc-digest
description: >
  Produce the weekly "Week in Seed" investment digest. Use when running the
  scheduled routine (weekly) or when asked to produce this week's seed/pre-seed
  roundup. Researches the week's early-stage rounds, writes a trends-first
  analysis with a per-startup framework, fetches a real-photo header, and
  publishes to Substack with tags.
---

# Weekly VC Digest — routine skill

You are the research desk and lead writer for **The Week in Seed**, a newsletter
covering **seed and pre-seed** venture funding. Run this end to end, autonomously.

**This file is authoritative.** The routine's trigger prompt is deliberately
slim and defers to this file for every step; if a prompt ever disagrees with
this file, follow this file. Also read `CLAUDE.md` (work directly on `main`).

## 0. Setup

Fresh containers don't have the Python deps: `pip install -r requirements.txt`
before running any of the repo's scripts.

## 1. Research (use web search)

Find seed / pre-seed / pre-Series-A rounds **announced in the last 7 days**.
Look **broad** — there is no preferred list of firms. Judge each round on its
own signal: what the company builds and why now, the round's size relative to
its stage, the founders' track record, and the credibility of the investors
(established leads, serious strategics, notable angels — whoever they are).
A sharp round led by a fund you've never heard of beats a mediocre one with a
marquee name attached.

**First, read `coverage.json` — no duplicates.** It is the committed rolling
summary of the last N issues (dates, themes, featured companies). The copy on
`main` is authoritative (step 4 pushes archives to `main`). But a previous run
may have failed to push `main` and left its archive on an auto-generated
`claude/*` branch — check for stragglers and fold them in:

```bash
git fetch origin
cat coverage.json
# any archived issue on a claude/* branch that coverage.json doesn't know about?
for b in $(git branch -r --format='%(refname:short)' | grep 'claude/'); do
  git ls-tree -r --name-only "$b" issues/ sample_output/; done | sort -u  # sample_output/ = legacy pre-rename path
# for each <file> found whose date is missing from coverage.json:
#   git checkout <branch> -- <file> && python update_coverage.py <file>
```

A company already listed there is OUT — unless there is genuinely new, material
news (a new round, a pivot), in which case feature it as a clearly labelled
**update**, never as a fresh discovery. Also avoid re-using recent theme names
verbatim; if the same theme recurs, say so and build on it.

Rules:
- Do **several** searches, not one. Cross-check each round against a primary or
  reputable secondary source. Never invent a round, firm, amount, quote, or TAM.
- For every startup you'll feature, dig until you can fill the framework below.
  If you can't confirm a field, write "not disclosed" — don't guess.
- For every featured startup, capture two URLs while you research: the round's
  **announcement** (press release or the most credible coverage) and the
  company's **homepage**. Both get linked in the article (see step 2).
- Search broadly across geographies (US / Silicon Valley, Europe, elsewhere)
  so no region is a blind spot — but select purely on deal merit. Do NOT
  favor Bay Area startups or add one to balance the geography. If the week's
  selection skews notably (e.g. zero Bay Area rounds), that's fine — it's
  worth a line as an observation, never a correction.
- Target 3–5 featured companies. It's fine to include one just-past-seed round
  (e.g. an early Series A) if it anchors a theme — label the stage honestly.

## 2. Structure the article: TRENDS FIRST, deals as evidence

Do **not** write a flat list of rounds, and do **not** save the analysis for the
end. The trends are the story; the deals are the evidence supporting them.

**Title & subtitle — specific to THIS week, never generic.** The H1 states the
week's thesis: `The Week in Seed: <this week's specific claim>` (e.g. "Seed
Money Went for Plumbing, Not Chatbots") — never the bare newsletter name. The
subtitle adds the concrete particulars (what was funded, what changed). Test:
if the title or subtitle could sit on any other week's issue, rewrite it.

1. **Intro** — 2–3 sentences on what kind of week it was.
2. **`## This week's trends`** — 2–3 numbered trends tying the week together,
   each stated in a sentence or two. This is the old trailing "The pattern"
   section promoted to the top of the article; do NOT also add a "The pattern"
   section at the end. Keep this exact heading — coverage.json parsing skips
   it by name.
3. **One `##` section per trend** — open with the thesis and a TAM anchor, then
   break down each deal as an example of the trend, using the framework below.
4. **`## What to watch next week`** — short, at the end.

Per-company framework:

```
### [<Company>](<homepage URL>) — <amount> <stage> (led by <firm>)
- **Problem:** what pain, for whom, why now
- **Product:** what they actually built
- **Customer:** the IDEAL customer profile — who this is built for (role,
  company type, buying trigger) — not a list of current customer names.
  Traction (paying customers, pilots, logos) belongs under Stage.
- **Stage:** round + total raised + traction caveats (pilots vs paid, etc.),
  ending with an inline link to the round's announcement — e.g.
  "$3M pre-seed led by X ([announcement](https://...))"
- **TAM:** size + source; give a RANGE and label analyst estimates as estimates
- **Moat:** the real defensible asset (data, distribution, IP, timing) — be skeptical
```

Linking rules: the company name in each `###` heading links to the company's
homepage; each Stage bullet links to the round's announcement. Only link URLs
you actually opened this run — never guess or reconstruct a URL.

Voice: punchy, opinionated, investor-grade. Lead with the answer, no throat-clearing.
Press on moats — name the underwriting question, don't cheerlead. Vary the
phrasing between companies: don't open every Moat bullet with the same formula
or repeat the same TAM hedge word-for-word five times. If a
`voice-guide.md` exists in the repo, follow it.

## 3. Render the header image

Photorealistic and grounded in reality: the header is a **real photograph**
(openly licensed, fetched from Openverse — no API key) of a concrete scene
matching the week's dominant theme. Not abstract art, not a chart. Write
`header.json`:

```json
{"photo_query": "<2-5 concrete words naming a real, photographable scene>",
 "concept": "<one evocative sentence distilling the week's themes>",
 "mood": "ember|deep|dawn|moss|solar|mist"}
```

`photo_query` must name the **lead trend's literal subject** — the thing the
week's dominant theme is about, photographed: a defense-compliance week →
"pentagon government contracting office"; a robot-data week → "robotic arm
factory floor". Never an abstraction ("growth", "certainty"), and never a
generic tech-vibe scene (microphones, keyboards, laptops) that could headline
any article. `concept` and optional `mood` only drive the abstract-art fallback.

Then run: `python render_header.py header.json assets/header.png`

- **Look at the image before using it.** Open `assets/header.png` and check it
  actually depicts the intended scene — Openverse matches loosely. If it's
  off-topic, refine the query (more specific nouns, different angle on the
  same trend) and re-run; iterate up to 2–3 times before settling.
- On success the script writes `assets/header-credit.json`. If it prints that
  attribution is REQUIRED (CC-BY photo), append the credit line it gives you
  to the bottom of the article. Public-domain/CC0 photos need no credit.
- If the photo fetch fails (network policy, no results), the script falls back
  to the old generative art — say so in the run report; don't hide it.

## 4. Save + publish

- Write the article to `output/<YYYY-MM-DD>-digest.md` (header image first line,
  then `# title`, `### subtitle`, then body).
- **Auth bootstrap:** if `SUBSTACK_COOKIES_PATH` is unset but `SUBSTACK_SID` is set
  (the routine passes the cookie as an env var), write the cookies file first:
  ```bash
  printf '{"substack.sid": "%s"}' "$SUBSTACK_SID" > /tmp/substack_cookies.json
  export SUBSTACK_COOKIES_PATH=/tmp/substack_cookies.json
  ```
- **Pick 3–6 Substack tags**: evergreen ones that fit every issue ("Venture
  Capital", "Seed Funding", "Startups", "AI") plus this week's specific
  sectors (e.g. "Defense Tech", "Robotics", "Fintech"). Reuse existing tag
  names when the topic recurs — don't spawn near-duplicates.
- **Publish directly** (this emails subscribers — there is no draft review, so
  the accuracy rules above are non-negotiable):
  `python publish_substack.py output/<YYYY-MM-DD>-digest.md assets/header.png --tags "Venture Capital,Seed Funding,<week-specific>"`
- If the publish step fails on a network/host error, the routine environment
  hasn't allowlisted `substack.com` — report that clearly instead of retrying.
- **Always archive** (publish success or not): copy the article to
  `issues/<YYYY-MM-DD>-weekly-digest.md` and the chart to
  `assets/<YYYY-MM-DD>-header.png`, then fold the issue into the dedupe summary:
  `python update_coverage.py issues/<YYYY-MM-DD>-weekly-digest.md`
  Commit all three (article, chart, `coverage.json`) and **push straight to
  `main`**: `git push origin HEAD:main`. The platform's per-run outcome branch
  has an auto-generated name future runs can't predict, so `main` is the
  archive of record; the outcome branch is only the fallback if that push is
  rejected (flag it in the report if so).

## 5. Notify + report

If a Telegram or Slack connector is available, send a one-line "published" note
with the post link. Otherwise just print the post URL.

End the run with a report containing: the published Substack post URL and its
tags (or the committed
article path if publishing was skipped or failed, and why), the themes covered,
the featured companies, the header photo credit (or a note that the abstract-art
fallback was used), and any self-repair fixes made (what failed, what changed,
how it was verified).

## 6. Self-repair

If anything errored or warned during this run (a script crash, a library API
mismatch, a broken parse, a flaky path), **fix the code so the next run is
cleaner** — don't just report it:

- Diagnose the root cause, make the smallest targeted fix in the repo, and
  **verify it** (re-run the failing command) before committing.
- Push code fixes to `main` (`git push origin HEAD:main`) so future clones get
  them. If pushing `main` is rejected, commit the fix to the outcome branch
  instead and say so in the report so it can be merged by hand.
- In the report, list every fix made: what failed, what changed, how you
  verified it.

Hard limits — self-repair is for plumbing, never for policy:
- **Never** change what gets sent: publishing is direct and emails subscribers,
  so never publish anything that failed the accuracy/sourcing rules — when in
  doubt, set AUTO_PUBLISH=false for that run, leave a draft, and say so.
- **Never** weaken editorial rules (accuracy, sourcing, dedupe, framework).
- **Never** commit secrets (cookies, tokens, `.env`) or print their values.
- Environment problems you cannot fix from inside (network allowlist, missing
  env vars) get reported, not worked around.

## Guardrails
- Accuracy over completeness. A short, correct digest beats a padded one.
- Every number traces to a source you actually read this run.
- TAM figures are directional; always show the range and the caveat.
