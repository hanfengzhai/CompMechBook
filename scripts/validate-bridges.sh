#!/usr/bin/env bash
# Verify every numbered chapter and part opening ends with a Bridge section
# (continuous-book narrative hinge; ME 412 layout).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

MISSING=0

check_bridge() {
  local file="$1"
  if ! grep -qE '^## Bridge' "$file"; then
    echo "MISSING ## Bridge: $file"
    MISSING=1
  fi
}

for f in src/part*/[0-9][0-9]-*.md; do
  [[ "$f" == *"/00-"* ]] && continue
  check_bridge "$f"
done

for f in src/part*/00-opening.md; do
  check_bridge "$f"
done

check_bridge src/preface.md
check_bridge src/prologue/00-many-scales.md
check_bridge src/epilogue/multiscale.md

if [[ $MISSING -ne 0 ]]; then
  echo "FAIL: Bridge section missing (continuous-book handoff required)"
  exit 1
fi

echo "OK: all chapters and part openings have Bridge sections"
