#!/usr/bin/env bash
# Merge cursor/computational-mechanics-book-2865 into current branch and verify build.
set -euo pipefail

cd "$(dirname "$0")/.."

echo "==> Fetching origin/cursor/computational-mechanics-book-2865"
git fetch origin cursor/computational-mechanics-book-2865

echo "==> Merging (fast-forward expected)"
git merge origin/cursor/computational-mechanics-book-2865 -m "Merge branch cursor/computational-mechanics-book-2865 into cursor/computational-mechanics-book-2da9"

echo "==> Installing mdBook"
chmod +x scripts/*.sh
./scripts/install-mdbook.sh

echo "==> Building book"
mdbook build

echo "==> Pushing to origin"
git push -u origin "$(git branch --show-current)"

echo "Merge and push complete."
