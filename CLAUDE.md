# Working in this repo

- **Always work on `main`. No feature branches.** Commit directly to `main`
  and push with `git push origin HEAD:main` — even if the session suggests a
  designated `claude/*` branch. Delete any stray `claude/*` branches after
  their work lands on `main`.
- `main` is also the archive of record for published issues (see SKILL.md
  step 4): each run's article, header image, and `coverage.json` update are
  committed and pushed straight to `main`.
- Never flip `AUTO_PUBLISH` — Substack drafts only.
- Article format and editorial rules live in `SKILL.md` (routine flow) and
  `src/research.py` (API flow). Keep the two in sync when changing either.
