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
      echo "skip (no dst for $n): $src_file"
    fi
  done
}

# Part I: Linear Algebra Notes (01–04 numbering preserved)
sync_part "$ROOT/writings/linear-algebra/chapters" "$ROOT/src/part01-linear-algebra" 01 02 03 04

# Part II: Functional Analysis Notes (01–05 numbering preserved)
sync_part "$ROOT/writings/functional-analysis/chapters" "$ROOT/src/part02-functional-analysis" 01 02 03 04 05

echo "Done. Run 'mdbook build' from repo root to verify."
