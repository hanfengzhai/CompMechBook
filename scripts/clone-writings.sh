#!/usr/bin/env bash
# Clone or update the external Writings repository into writings/.
# Requires access to https://github.com/hanfengzhai/Writings (private for many clones).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WRITINGS_URL="${WRITINGS_URL:-https://github.com/hanfengzhai/Writings.git}"
TARGET="$ROOT/writings"

if [[ -f "$TARGET/.git" ]] || [[ -d "$TARGET/.git" ]]; then
  echo "Updating existing Writings checkout in $TARGET"
  git -C "$TARGET" pull --ff-only
elif [[ -f "$ROOT/.gitmodules" ]] && grep -E '^[[:space:]]*path[[:space:]]*=' "$ROOT/.gitmodules" 2>/dev/null | grep -qv '^#' | grep -q 'writings'; then
  echo "Initializing writings submodule"
  git submodule update --init --recursive writings
else
  echo "Cloning $WRITINGS_URL into temporary directory"
  tmp="$(mktemp -d)"
  if git clone --depth 1 "$WRITINGS_URL" "$tmp/Writings" 2>/dev/null; then
    echo ""
    echo "Writings cloned. Merge upstream subtrees into $TARGET manually, then run:"
    echo "  ./scripts/sync-writings.sh && mdbook build"
    echo ""
    echo "Suggested layout (Functional Analysis Notes style):"
    ls -1 "$tmp/Writings" 2>/dev/null || true
  else
    echo "Writings remote not available. Use vendored content under $TARGET."
    echo "Edit chapters there, then: ./scripts/sync-writings.sh"
  fi
  rm -rf "$tmp"
fi
