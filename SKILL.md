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
  git ls-tree -r --name-only "$b" sample_output/; done | sort -u
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
- Cover the geography honestly. Run at least a couple of searches explicitly
  targeting US / Silicon Valley deal flow, not just whatever surfaces first.
  If the final selection ends up with no Bay Area startup, double-check that
  this reflects the week rather than a search blind spot — and if it holds,
  say so in the article as a deliberate observation, not by omission.
- Target 3–5 featured companies. It's fine to include one just-past-seed round
  (e.g. an early Series A) if it anchors a theme — label the stage honestly.

## 2. Structure the article: TRENDS FIRST, deals as evidence

Do **not** write a flat list of rounds, and do **not** save the analysis for the
end. The trends are the story; the deals are the evidence supporting them.

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

Abstract art, **not** a chart or graph. Write `header.json`:

```json
{"concept": "<one evocative sentence distilling the week's themes>",
 "mood": "ember|deep|dawn|moss|solar|mist"}
```

`concept` seeds the generative art (it is not drawn as text) — make it specific
to this week so the image differs from past issues. `mood` is optional; pick
one that fits the week's tone or omit it to let the seed decide.

Then run: `python render_header.py header.json assets/header.png`

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
  `assets/<YYYY-MM-DD>-header.png`, then fold the issue into the dedupe summary:
  `python update_coverage.py sample_output/<YYYY-MM-DD>-weekly-digest.md`
  Commit all three (article, chart, `coverage.json`) and **push straight to
  `main`**: `git push origin HEAD:main`. The platform's per-run outcome branch
  has an auto-generated name future runs can't predict, so `main` is the
  archive of record; the outcome branch is only the fallback if that push is
  rejected (flag it in the report if so).

## 5. Notify

If a Telegram or Slack connector is available, send a one-line "draft ready" note
with the Substack draft link. Otherwise just print the draft URL.

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
- **Never** flip `AUTO_PUBLISH`/auto-publish behaviour — drafts only, always.
- **Never** weaken editorial rules (accuracy, sourcing, dedupe, framework).
- **Never** commit secrets (cookies, tokens, `.env`) or print their values.
- Environment problems you cannot fix from inside (network allowlist, missing
  env vars) get reported, not worked around.

## Guardrails
- Accuracy over completeness. A short, correct digest beats a padded one.
- Every number traces to a source you actually read this run.
- TAM figures are directional; always show the range and the caveat.
