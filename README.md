# The Week in Seed — weekly VC digest automation

Every week: research the latest **seed / pre-seed** rounds from top firms (YC & alike),
analyse them **by investment theme** with a per-startup framework (Problem · Product ·
Customer · Stage · TAM · Moat), render a header chart, and drop a **draft** into
Substack for one-click review-and-publish.

Two ways to run it. **Option A (recommended): a Claude Code Routine** — no servers,
runs on Anthropic's cloud on a weekly schedule. **Option B: self-hosted** on GCP
Cloud Run + Scheduler.

---

## Status — 2026-07-09

**Option A is live.** Decisions and current state:

- ✅ Repo pushed to `github.com/bogdanripa/week-in-seed`.
- ✅ **Remote routine created** via the claude.ai triggers API:
  trigger `trig_0169n318LEV5fgxuGrvjYAqB`, cron `0 5 * * 1` (**UTC** — the API does
  not track timezones, so this is 08:00 Bucharest in summer, 07:00 in winter).
  First run: Monday 2026-07-13. Manage it at `claude.ai/code/routines`.
- ✅ Routine clones this repo as its source and commits its output to the
  **`claude/weekly-digest`** branch — so if Substack publishing fails, the finished
  article + chart still land in `sample_output/` / `assets/` on that branch.
- ✅ A local desktop-app scheduled task (`weekly-vc-digest`) was created first, then
  **disabled** in favour of the remote routine — it only ran while the app was open.
- ⚠️ **Substack auth is pending.** `substack_cookies.json` is scaffolded locally
  (gitignored) but the auth cookie value is still a placeholder, and
  `SUBSTACK_PUBLICATION_URL` in `.env` is unset. Until the routine's environment
  gets the env vars + `substack.com` on the allowed-domains list, runs will fall
  back to committing the article to the outcome branch instead of drafting.
- 📌 Correction discovered during setup: the auth cookie is **`substack.sid`** (not
  `connect.sid`), and `python-substack` expects the cookies file as a **flat JSON
  dict** `{"name": "value"}`, not a browser-export array. The "Substack auth"
  section below is updated accordingly.

---

## Option A — run it as a Claude Code Routine  ★ recommended

A routine is a saved Claude Code config (prompt + repo + connectors + trigger) that
runs on Anthropic-managed cloud infrastructure — it fires weekly whether your laptop
is open or not. The routine session does the research itself (built-in web search),
follows `SKILL.md`, runs the two Python scripts, and creates the Substack draft.

### One-time setup

1. **Push this repo** to GitHub (the routine clones it each run).
2. **Create the routine** at `claude.ai/code/routines` → *New routine* → *Remote*
   (or `/schedule` in the Claude Code CLI). Attach this repository.
3. **Trigger:** Scheduled → Weekly → Monday 08:00 (Europe/Bucharest).
4. **Prompt** (paste this):
   > Run the weekly VC digest exactly as described in `SKILL.md`. Research the last
   > 7 days of seed/pre-seed rounds, write the themed analysis with the per-startup
   > framework, render the header chart, and create the Substack draft. Do not
   > auto-publish. When done, report the draft URL.
5. **Network:** the default routine environment uses *Trusted* network access, which
   does **not** include `substack.com`. Either:
   - **a)** In the routine's environment, add `substack.com` (and `*.substack.com`)
     to **Allowed domains**, and set env vars `SUBSTACK_PUBLICATION_URL` +
     `SUBSTACK_COOKIES_PATH` (mount the cookie file as an env secret); **or**
   - **b)** Attach a **Substack MCP connector** instead — MCP traffic routes through
     Anthropic's servers and bypasses the allowlist. Then swap step 4 of `SKILL.md`
     to publish via the connector rather than `publish_substack.py`.
6. **Setup script** (routine environment → runs before each session):
   ```bash
   pip install -r requirements.txt
   ```

### Daily-limit note
Routines draw down your plan's usage and have a per-day cap (Pro 5 / Max 15 /
Team-Enterprise 25 routines per day). One weekly run is comfortably within any plan.

### Why this beats the GCP path
No Dockerfile, no Cloud Run, no separate Anthropic API key, no scheduler to wire —
the routine's own agent session is the researcher *and* the writer. You maintain a
repo and a prompt, nothing else.

---

## Option B — self-hosted on GCP (Cloud Run + Scheduler)

Use this if you want full control, custom data sources, or to keep it off your Claude
plan. Here the research is a single Anthropic API call with the `web_search` server tool.

```bash
pip install -r requirements.txt
cp .env.example .env && set -a && . ./.env && set +a
python src/main.py --dry-run     # research + chart + markdown, no Substack
python src/main.py               # full run → Substack draft
```

Deploy:
```bash
gcloud run deploy week-in-seed --source . --region europe-west1 --no-allow-unauthenticated \
  --set-env-vars SUBSTACK_PUBLICATION_URL=https://yourname.substack.com,AUTO_PUBLISH=false \
  --set-secrets ANTHROPIC_API_KEY=anthropic-key:latest,SUBSTACK_COOKIES_PATH=/secrets/substack_cookies.json

gcloud scheduler jobs create http week-in-seed-weekly \
  --schedule "0 8 * * 1" --time-zone "Europe/Bucharest" \
  --uri "$(gcloud run services describe week-in-seed --region europe-west1 --format='value(status.url)')" \
  --http-method POST --oidc-service-account-email SCHEDULER_SA@PROJECT.iam.gserviceaccount.com
```

---

## The article format (both options)

Structured **by investment theme**, not a flat list. Each featured startup gets:

| Field | What it answers |
|-------|-----------------|
| Problem | the pain, for whom, why now |
| Product | what they actually built |
| Customer | who buys (named logos if disclosed) |
| Stage | round + total raised + traction caveats |
| TAM | size + source, as a labelled analyst range |
| Moat | the real defensible asset — data, distribution, IP, timing |

See `sample_output/2026-07-08-weekly-digest.md` for a real generated edition.

## Files

| File | Role |
|------|------|
| `SKILL.md` | Routine instructions: research method + framework + publish flow |
| `render_chart.py` | CLI: `deals.json` → header PNG (routine calls this) |
| `publish_substack.py` | CLI: markdown → Substack draft (routine calls this) |
| `src/research.py` | Option B only: Anthropic call + `web_search` server tool |
| `src/images.py` | Chart renderer (shared) |
| `src/publish.py` | Markdown → Substack blocks; draft creation |
| `src/main.py` | Option B orchestrator + Cloud Run handler |
| `sample_output/` | This week's real generated edition |

## Substack auth (both options)

No official publishing API. Export your session cookie once:
1. Log into **substack.com** (the root site, not just your publication's subdomain)
   → DevTools → Application → Cookies → `https://substack.com` → copy the value of
   **`substack.sid`** (HttpOnly, sorts near the bottom of the list).
2. Save `substack_cookies.json` as a **flat dict** (what `python-substack` loads):
   `{"substack.sid": "<value>"}`
3. Point `SUBSTACK_COOKIES_PATH` at it. Valid for months, MFA-safe.
   Analytics cookies (`_ga`, `__cf_bm`, `AWSALBTG`, …) are not needed and don't authenticate.

## Honest limits
- **Substack is unofficial** (`python-substack` on internal endpoints) — pin the version.
- **Early-stage reporting lags** — web search alone under-covers pure seed/pre-seed.
  Phase 2: add a paid feed (Crunchbase News / Harmonic / Fundup) as a repo tool.
- **Draft mode by default** until you trust it.
- **TAM figures are analyst estimates** with wide, scope-dependent ranges — the skill
  forces a labelled range, not a single fake-precise number.

## Phase 2 ideas
- Add a structured deal feed for coverage completeness.
- Drop a `voice-guide.md` in the repo (or your `bogdan-voice` skill) so it writes as you.
- Telegram "draft ready" ping (connector already supported in `SKILL.md` step 5).
- Track week-over-week theme trends in a small store so the piece can say "physical AI up 3 weeks running".
