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

# Part II: Functional Analysis Notes (01–05 numbering preserved)
FA_SRC="$ROOT/writings/functional-analysis/chapters"
FA_DST="$ROOT/src/part02-functional-analysis"
for n in 01 02 03 04 05; do
  src_file="$(ls "$FA_SRC"/${n}-*.md 2>/dev/null | head -1 || true)"
  dst_file="$(ls "$FA_DST"/${n}-*.md 2>/dev/null | head -1 || true)"
  if [[ -n "$src_file" && -n "$dst_file" ]]; then
    sync_file "$src_file" "$dst_file"
  fi
done

echo "Done. Run 'mdbook build' from repo root to verify."
