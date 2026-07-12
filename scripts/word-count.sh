#!/usr/bin/env bash
# Report word counts per part in src/ (and optional writings/ subtree).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TOTAL=0

count_path() {
  local label="$1" path="$2"
  if [[ ! -e "$path" ]]; then
    return
  fi
  local words=0
  if [[ -d "$path" ]]; then
    words="$(find "$path" -maxdepth 1 -name '*.md' -print0 | xargs -0 wc -w 2>/dev/null | tail -1 | awk '{print $1}')"
  else
    words="$(wc -w < "$path" | tr -d ' ')"
  fi
  words="${words:-0}"
  printf "%-42s %6s words\n" "$label" "$words"
  TOTAL=$((TOTAL + words))
}

echo "CompMechBook word counts (src/)"
echo "----------------------------------------"
count_path "Preface" "$ROOT/src/preface.md"
count_path "Prologue" "$ROOT/src/prologue"
count_path "Part I — Linear algebra" "$ROOT/src/part01-linear-algebra"
count_path "Part II — Functional analysis" "$ROOT/src/part02-functional-analysis"
count_path "Part III — PDEs" "$ROOT/src/part03-pdes"
count_path "Part IV — FEM" "$ROOT/src/part04-fem"
count_path "Part V — FVM" "$ROOT/src/part05-fvm"
count_path "Part VI — Continuum" "$ROOT/src/part06-continuum"
count_path "Part VII — Defects" "$ROOT/src/part07-defects"
count_path "Part VIII — MD" "$ROOT/src/part08-md"
count_path "Part IX — DFT" "$ROOT/src/part09-dft"
count_path "Epilogue" "$ROOT/src/epilogue"
count_path "Appendix" "$ROOT/src/appendix"
echo "----------------------------------------"
printf "%-42s %6s words\n" "Total (excluding SUMMARY.md)" "$TOTAL"
