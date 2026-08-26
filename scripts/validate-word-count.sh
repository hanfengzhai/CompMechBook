#!/usr/bin/env bash
# Fail CI if src/ word count drops below minimum (guards against accidental deletion).
# Usage: ./scripts/validate-word-count.sh [MIN_WORDS]
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MIN="${1:-180000}"

TOTAL=0
while IFS= read -r -d '' f; do
  TOTAL=$((TOTAL + $(wc -w < "$f")))
done < <(find "$ROOT/src" -name '*.md' ! -name 'SUMMARY.md' -print0)

if [[ "$TOTAL" -lt "$MIN" ]]; then
  echo "FAIL: src/ word count $TOTAL below minimum $MIN"
  exit 1
fi

echo "OK: src/ word count $TOTAL (minimum $MIN)"
