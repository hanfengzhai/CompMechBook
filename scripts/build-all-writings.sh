#!/usr/bin/env bash
# Build every standalone mdBook under writings/.
set -euo pipefail

export PATH="${HOME}/.local/bin:${PATH}"

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PARTS=(
  linear-algebra
  functional-analysis
  pde
  fem
  fvm
  continuum
  defects
  md
  dft
)

for part in "${PARTS[@]}"; do
  dir="$ROOT/writings/$part"
  if [[ -f "$dir/book.toml" ]]; then
    echo "==> mdbook build: writings/$part"
    (cd "$dir" && mdbook build)
  else
    echo "skip (no book.toml): writings/$part"
  fi
done

echo "All standalone Writings mdBooks built."
