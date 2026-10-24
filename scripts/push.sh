#!/usr/bin/env bash
# Sanad — repo ko GitHub par push karne ka helper.
# Token .secrets/gh_token mein rakhein (gitignored). Usage: ./scripts/push.sh "commit message"
set -euo pipefail
cd "$(dirname "$0")/.."

MSG="${1:-update}"
USER_NAME="${GH_USER:?GH_USER env var set karein (GitHub username)}"
REPO="${GH_REPO:-sanad}"
TOKEN="$(cat .secrets/gh_token 2>/dev/null || true)"

if [ -z "$TOKEN" ]; then
  echo "❌ .secrets/gh_token nahi mila. Token file banayein:  printf '%s' 'ghp_xxx' > .secrets/gh_token"
  exit 1
fi

git add -A
if git diff --cached --quiet; then
  echo "ℹ️  Koi change nahi — commit skip."
else
  git commit -q -m "$MSG"
fi

git remote remove origin 2>/dev/null || true
git remote add origin "https://x-access-token:${TOKEN}@github.com/${USER_NAME}/${REPO}.git"
git branch -M main
git push -u origin main
git remote set-url origin "https://github.com/${USER_NAME}/${REPO}.git"
echo "✅ Pushed: https://github.com/${USER_NAME}/${REPO}"
