#!/usr/bin/env bash
# Verify narrative intermission hinges at Part III.4, V.4, and VI.4 (continuous-book device).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

MISSING=0

check_intermission() {
  local file="$1" anchor="$2"
  if ! grep -q "^## Intermission:" "$file"; then
    echo "MISSING ## Intermission: $file"
    MISSING=1
  fi
  if ! grep -q "{#${anchor}}" "$file"; then
    echo "MISSING anchor {#${anchor}}: $file"
    MISSING=1
  fi
}

check_intermission src/part03-pdes/04-energy-methods.md intermission-analysis-complete-assembly-begins
check_intermission src/part05-fvm/04-navier-stokes-cfd.md intermission-discretization-complete-continuum-begins
check_intermission src/part06-continuum/04-nonlinear-plasticity-preview.md intermission-ascent-ends-descent-begins

if [[ $MISSING -ne 0 ]]; then
  echo "FAIL: narrative intermission hinges incomplete (III.4, V.4, and VI.4 required)"
  exit 1
fi

echo "OK: narrative intermission hinges present (III.4 analysis→assembly, V.4 discretization→continuum, VI.4 ascent→descent)"
