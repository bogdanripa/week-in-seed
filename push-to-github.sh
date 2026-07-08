#!/usr/bin/env bash
# Creates the GitHub repo and pushes this folder. Run from inside the repo.
set -euo pipefail
REPO_NAME="${1:-week-in-seed}"
VISIBILITY="${2:-private}"   # private | public

if command -v gh >/dev/null 2>&1 && gh auth status >/dev/null 2>&1; then
  echo "→ Using gh CLI (authenticated)."
  gh repo create "$REPO_NAME" --"$VISIBILITY" --source=. --remote=origin --push
  echo "✓ Done. Repo created and pushed under your account."
else
  echo "gh CLI not found or not authenticated."
  echo "Create the repo at https://github.com/new (name: $REPO_NAME), then run:"
  echo "  git remote add origin git@github.com:<your-username>/$REPO_NAME.git"
  echo "  git push -u origin main"
fi
