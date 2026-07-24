# The Week in Seed — weekly VC digest automation

A Claude Code routine that, every Monday, researches the last 7 days of
**seed / pre-seed** rounds, writes a trends-first analysis with a per-startup
framework, fetches a real photographic header, and **publishes it to Substack**
with topic tags. Every issue is archived to `main`.

## How it runs

- **Routine** `trig_0169n318LEV5fgxuGrvjYAqB`, cron `0 5 * * 1` (UTC — 08:00
  Bucharest in summer). Manage it at `claude.ai/code/routines`.
- The trigger prompt is deliberately slim: it points at **`SKILL.md`**, the
  single source of truth for every step (setup, dedupe, research, writing,
  header, publish, archive, self-repair, report). Editing the repo is how the
  routine's behaviour changes — never the prompt.
- The routine's environment provides `SUBSTACK_SID` + `SUBSTACK_PUBLICATION_URL`
  and full network access.
- All work lands directly on **`main`** (see `CLAUDE.md`): the article in
  `issues/`, the header in `assets/`, the dedupe memory in `coverage.json`.
- Publishing is **direct** — the run tags the post and sends it to subscribers.
  Set `AUTO_PUBLISH=false` in the environment for draft-only test runs.

## The article format

**A high-level trends essay, deals only as examples** — each trend gets a
section of industry-level analysis (the shift, why now, who wins, a TAM
anchor); the week's deals appear only as compact example blocks inside the
trend they exemplify. Everything is said exactly once: no trend list up top,
no recap at the end, deal facts only in the example blocks. Each featured
startup gets:

| Field | What it answers |
|-------|-----------------|
| Problem | the pain, for whom, why now |
| Product | what they actually built |
| Customer | the ideal customer profile (role, company type, buying trigger) |
| Stage | round + total raised + traction caveats, linked to the announcement |
| TAM | size + source, as a labelled analyst range |
| Moat | the real defensible asset — data, distribution, IP, timing |

Every company name links to its homepage and every round to its announcement —
only URLs the research actually opened, never guessed. The header is a real,
openly licensed photograph (Openverse, no API key) of a concrete scene from the
week's dominant theme; CC-BY photos get a credit line in the article.

See the latest edition in `issues/` for a real generated example.

## Files

| File | Role |
|------|------|
| `SKILL.md` | The routine's instructions — research method, framework, publish flow |
| `CLAUDE.md` | Repo working rules (work on `main`, direct publish, keep flows in sync) |
| `render_header.py` | CLI: `header.json` (photo_query + concept) → real-photo header PNG, abstract-art fallback |
| `publish_substack.py` | CLI: markdown (+ `--tags`) → published Substack post |
| `update_coverage.py` | CLI: folds a finished issue into `coverage.json` |
| `coverage.json` | Rolling last-12-issues summary (themes + companies) — the dedupe memory |
| `issues/` | Archive of record: every published edition |
| `src/photos.py` | Openverse photo fetcher: query → CC-licensed photo + attribution |
| `src/images.py` | Generative abstract-art renderer (header fallback) |
| `src/coverage.py` | Parser + summary logic behind `update_coverage.py` |
| `src/publish.py` | Markdown → Substack blocks; tagging + publishing |
| `src/research.py`, `src/main.py` | API flow: same pipeline as one Anthropic `web_search` call (see below) |

## Substack auth

No official publishing API; `python-substack` (pinned 0.1.25) drives internal
endpoints with a session cookie. Export it once: log into **substack.com** (the
root site) → DevTools → Cookies → copy **`substack.sid`**. The routine passes it
as the `SUBSTACK_SID` env var and `SKILL.md` writes the flat-dict cookies file
`{"substack.sid": "<value>"}` at runtime. Valid for months, MFA-safe.

## API flow (self-hosted fallback)

The same pipeline can run off-plan as a single Anthropic API call with the
`web_search` server tool — useful for Cloud Run or local testing:

```bash
pip install -r requirements-gcp.txt
cp .env.example .env && set -a && . ./.env && set +a
python src/main.py --dry-run     # research + header + markdown, no Substack
python src/main.py               # full run → published Substack post
```

`Dockerfile` builds the Cloud Run image. Keep `src/research.py` in sync with
`SKILL.md` when editorial rules change (`CLAUDE.md` rule).

## Known limits

- Substack publishing is unofficial — keep `python-substack` pinned.
- Web search under-covers pure seed/pre-seed; a paid deal feed (Crunchbase
  News, Harmonic) would improve completeness.
- TAM figures are analyst estimates — the format forces a labelled range, not
  a single fake-precise number.
