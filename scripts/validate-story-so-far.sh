#!/usr/bin/env bash
# Verify part openings and epilogue include Story so far recaps (continuous-book device).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

MISSING=0

check_story_so_far() {
  local file="$1"
  if ! grep -q "^## Story so far" "$file"; then
    echo "MISSING ## Story so far: $file"
    MISSING=1
  fi
}

for f in src/part*/00-opening.md; do
  check_story_so_far "$f"
done

check_story_so_far src/epilogue/multiscale.md

if [[ $MISSING -ne 0 ]]; then
  echo "FAIL: Story so far recap missing (part openings and epilogue required)"
  exit 1
fi

echo "OK: all part openings and epilogue have Story so far recaps"
