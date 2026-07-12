#!/usr/bin/env bash
# Sync canonical Writings markdown into CompMechBook src/ chapters.
# Usage: ./scripts/sync-writings.sh [--dry-run|--check]
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DRY_RUN=false
CHECK_ONLY=false
for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN=true ;;
    --check) CHECK_ONLY=true ;;
  esac
done

DRIFT=0

rewrite_links() {
  # Normalize cross-part links for unified mdBook layout (src/).
  sed -e 's|](../../prologue/|](../prologue/|g' \
      -e 's|](../../epilogue/|](../epilogue/|g' \
      -e 's|(../../prologue/|(../prologue/|g' \
      -e 's|(../../epilogue/|(../epilogue/|g'
}

sync_file() {
  local src="$1" dst="$2"
  if [[ ! -f "$src" ]]; then
    echo "skip (missing): $src"
    return
  fi
  if $DRY_RUN; then
    echo "would sync: $src -> $dst"
  elif $CHECK_ONLY; then
    if [[ ! -f "$dst" ]]; then
      echo "DRIFT (missing dst): $dst"
      DRIFT=1
    elif ! cmp -s <(rewrite_links < "$src") "$dst"; then
      echo "DRIFT: $src != $dst"
      DRIFT=1
    fi
  else
    rewrite_links < "$src" > "$dst"
    echo "synced: $dst"
  fi
}

sync_opening() {
  local src_dir="$1" dst_dir="$2"
  sync_file "$src_dir/00-opening.md" "$dst_dir/00-opening.md"
}

sync_part() {
  local src_dir="$1" dst_dir="$2"
  shift 2
  local numbers=("$@")
  sync_opening "$src_dir" "$dst_dir"
  for n in "${numbers[@]}"; do
    local src_file
    src_file="$(ls "$src_dir"/${n}-*.md 2>/dev/null | head -1 || true)"
    local dst_file
    dst_file="$(ls "$dst_dir"/${n}-*.md 2>/dev/null | head -1 || true)"
    if [[ -n "$src_file" && -n "$dst_file" ]]; then
      sync_file "$src_file" "$dst_file"
    elif [[ -n "$src_file" ]]; then
      dst_file="$dst_dir/$(basename "$src_file")"
      sync_file "$src_file" "$dst_file"
    fi
  done
}

# Front matter
sync_file "$ROOT/writings/preface/chapters/preface.md" "$ROOT/src/preface.md"
sync_file "$ROOT/writings/prologue/chapters/00-many-scales.md" "$ROOT/src/prologue/00-many-scales.md"
sync_file "$ROOT/writings/epilogue/chapters/multiscale.md" "$ROOT/src/epilogue/multiscale.md"

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

# Part VI: Continuum Mechanics Notes (01–04)
sync_part "$ROOT/writings/continuum/chapters" "$ROOT/src/part06-continuum" 01 02 03 04

# Part VII: Defects Notes (01–03)
sync_part "$ROOT/writings/defects/chapters" "$ROOT/src/part07-defects" 01 02 03

# Part VIII: MD Notes (01–03)
sync_part "$ROOT/writings/md/chapters" "$ROOT/src/part08-md" 01 02 03

# Part IX: DFT Notes (01–03)
sync_part "$ROOT/writings/dft/chapters" "$ROOT/src/part09-dft" 01 02 03

# Appendix: glossary, sources, memory sheet
sync_file "$ROOT/writings/appendix/chapters/glossary.md" "$ROOT/src/appendix/glossary.md"
sync_file "$ROOT/writings/appendix/chapters/sources.md" "$ROOT/src/appendix/sources.md"
sync_file "$ROOT/writings/appendix/chapters/memory-sheet.md" "$ROOT/src/appendix/memory-sheet.md"

if $CHECK_ONLY; then
  if [[ $DRIFT -ne 0 ]]; then
    echo "FAIL: src/ is out of sync with writings/. Run ./scripts/sync-writings.sh"
    exit 1
  fi
  echo "OK: src/ matches writings/"
  exit 0
fi

echo "Done. Run 'mdbook build' from repo root to verify."
