#!/usr/bin/env bash
# WakeelBano — push helper.
# Token .secrets/gh_token mein rakhein (gitignored).
# Usage: ./scripts/push.sh "commit message"
set -euo pipefail
cd "$(dirname "$0")/.."

MSG="${1:-update}"
USER_NAME="${GH_USER:-Sarmads050}"
REPO="${GH_REPO:-wakeelbano}"
TOKEN="$(cat .secrets/gh_token 2>/dev/null | tr -d '\r\n' || true)"

if [ -z "$TOKEN" ]; then
  echo "❌ .secrets/gh_token nahi mila."
  echo "   Banayein:  printf '%s' 'github_pat_xxx' > .secrets/gh_token"
  exit 1
fi

# git identity (the sandbox does not keep ~/.gitconfig between sessions)
git config user.email >/dev/null 2>&1 || git config user.email "agent@wakeelbano.com"
git config user.name  >/dev/null 2>&1 || git config user.name  "WakeelBano Agent"

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
