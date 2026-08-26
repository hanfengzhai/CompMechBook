#!/usr/bin/env bash
# Verify numbered chapters and part openings carry Scene, Bridge, and Lab act
# sections (ME 412 narrative template). Preface/prologue/epilogue require Scene
# and Bridge; part openings also require Lab act.
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

check_sections() {
  local file="$1"
  shift
  for section in "$@"; do
    check_section "$file" "$section"
  done
}

# Numbered chapters (01–NN): Scene, Bridge, Lab act
for f in src/part*/[0-9][0-9]-*.md; do
  [[ "$f" == *"/00-"* ]] && continue
  check_sections "$f" Scene Bridge "Lab act"
done

# Part openings (00-opening.md): Scene, Bridge, Lab act
for f in src/part*/00-opening.md; do
  check_sections "$f" Scene Bridge "Lab act"
done

# Bookends: Scene + Bridge (Lab act optional on preface)
check_sections src/preface.md Scene Bridge
check_sections src/prologue/00-many-scales.md Scene Bridge
check_sections src/epilogue/multiscale.md Scene Bridge

if [[ $MISSING -ne 0 ]]; then
  echo "FAIL: narrative template incomplete (Scene/Bridge/Lab act per ME 412 layout)"
  exit 1
fi

echo "OK: narrative template complete (chapters, part openings, bookends)"
