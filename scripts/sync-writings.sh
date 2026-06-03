#!/usr/bin/env bash
# Sync canonical Writings markdown into CompMechBook src/ chapters.
# Usage: ./scripts/sync-writings.sh [--dry-run]
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DRY_RUN=false
[[ "${1:-}" == "--dry-run" ]] && DRY_RUN=true

sync_file() {
  local src="$1" dst="$2"
  if [[ ! -f "$src" ]]; then
    echo "skip (missing): $src"
    return
  fi
  if $DRY_RUN; then
    echo "would sync: $src -> $dst"
  else
    cp "$src" "$dst"
    echo "synced: $dst"
  fi
}

sync_part() {
  local src_dir="$1" dst_dir="$2"
  shift 2
  local numbers=("$@")
  for n in "${numbers[@]}"; do
    local src_file
    src_file="$(ls "$src_dir"/${n}-*.md 2>/dev/null | head -1 || true)"
    local dst_file
    dst_file="$(ls "$dst_dir"/${n}-*.md 2>/dev/null | head -1 || true)"
    if [[ -n "$src_file" && -n "$dst_file" ]]; then
      sync_file "$src_file" "$dst_file"
    elif [[ -n "$src_file" ]]; then
      local basename
      basename="$(basename "$src_file")"
      sync_file "$src_file" "$dst_dir/$basename"
    fi
  done
}

# Part I: Linear Algebra Notes (01–04)
sync_part "$ROOT/writings/linear-algebra/chapters" "$ROOT/src/part01-linear-algebra" 01 02 03 04

# Part II: Functional Analysis Notes (01–05)
sync_part "$ROOT/writings/functional-analysis/chapters" "$ROOT/src/part02-functional-analysis" 01 02 03 04 05

# Part III: PDE Notes (01–04)
sync_part "$ROOT/writings/pde/chapters" "$ROOT/src/part03-pdes" 01 02 03 04

# Part IV: FEM Notes (01–05)
sync_part "$ROOT/writings/fem/chapters" "$ROOT/src/part04-fem" 01 02 03 04 05

# Part V: FVM Notes (01–04)
sync_part "$ROOT/writings/fvm/chapters" "$ROOT/src/part05-fvm" 01 02 03 04

# Part VI: Continuum Mechanics Notes (01–03)
sync_part "$ROOT/writings/continuum/chapters" "$ROOT/src/part06-continuum" 01 02 03

# Part VII: Defects Notes (01–02)
sync_part "$ROOT/writings/defects/chapters" "$ROOT/src/part07-defects" 01 02

# Part VIII: MD Notes (01–02)
sync_part "$ROOT/writings/md/chapters" "$ROOT/src/part08-md" 01 02

# Part IX: DFT Notes (01–03)
sync_part "$ROOT/writings/dft/chapters" "$ROOT/src/part09-dft" 01 02 03

echo "Done. Run 'mdbook build' from repo root to verify."
