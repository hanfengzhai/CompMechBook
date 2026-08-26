#!/usr/bin/env bash
# Verify every part opening includes a Story so far recap (continuous-book device).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

MISSING=0

for f in src/part*/00-opening.md; do
  if ! grep -q "^## Story so far" "$f"; then
    echo "MISSING ## Story so far: $f"
    MISSING=1
  fi
done

if [[ $MISSING -ne 0 ]]; then
  echo "FAIL: part openings missing Story so far recap"
  exit 1
fi

echo "OK: all part openings have Story so far recaps"
