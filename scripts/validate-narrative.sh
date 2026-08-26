#!/usr/bin/env bash
# Verify numbered chapters carry Scene, Bridge, and Lab act sections (ME 412 narrative template).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

MISSING=0

check_section() {
  local file="$1" section="$2"
  if ! grep -q "^## ${section}" "$file"; then
    echo "MISSING ## ${section}: $file"
    MISSING=1
  fi
}

for f in src/part*/[0-9][0-9]-*.md; do
  [[ "$f" == *"/00-"* ]] && continue
  check_section "$f" "Scene"
  check_section "$f" "Bridge"
  check_section "$f" "Lab act"
done

if [[ $MISSING -ne 0 ]]; then
  echo "FAIL: narrative template incomplete (expected Scene, Bridge, Lab act on every numbered chapter)"
  exit 1
fi

echo "OK: all numbered chapters have Scene, Bridge, and Lab act sections"
