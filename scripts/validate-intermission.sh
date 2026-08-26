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

check_intermission src/prologue/00-many-scales.md intermission-panorama-complete-grammar-begins
check_intermission src/part03-pdes/04-energy-methods.md intermission-analysis-complete-assembly-begins
check_intermission src/part05-fvm/04-navier-stokes-cfd.md intermission-discretization-complete-continuum-begins
check_intermission src/part06-continuum/04-nonlinear-plasticity-preview.md intermission-ascent-ends-descent-begins
check_intermission src/part07-defects/03-polycrystal-and-fem-handoff.md intermission-mesoscale-complete-atomistic-begins
check_intermission src/part08-md/03-ab-initio-and-coarse-graining.md intermission-atomistic-complete-electronic-audit-begins
check_intermission src/part09-dft/03-dft-workflows.md intermission-descent-complete-coupling-begins
check_intermission src/epilogue/multiscale.md intermission-coupling-begins-loop-closes

if [[ $MISSING -ne 0 ]]; then
  echo "FAIL: narrative intermission hinges incomplete (prologue, III.4, V.4, VI.4, VII.3, VIII.3, IX.3, epilogue required)"
  exit 1
fi

echo "OK: narrative intermission hinges present (prologue panorama→grammar, III.4 analysis→assembly, V.4 discretization→continuum, VI.4 ascent→descent, VII.3 mesoscale→atomistic, VIII.3 atomistic→electronic, IX.3 descent→coupling, epilogue coupling→loop)"
