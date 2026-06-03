#!/usr/bin/env bash
# Install mdBook into DEST (default: /usr/local/bin) if not already on PATH.
set -euo pipefail

VERSION="${MDBOOK_VERSION:-0.4.40}"
DEST="${MDBOOK_DEST:-${HOME}/.local/bin}"

if command -v mdbook >/dev/null 2>&1; then
  echo "mdbook already installed: $(mdbook --version)"
  exit 0
fi

tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

archive="mdbook-v${VERSION}-x86_64-unknown-linux-gnu.tar.gz"
curl -sSL "https://github.com/rust-lang/mdBook/releases/download/v${VERSION}/${archive}" \
  | tar -xz -C "$tmp"

mkdir -p "$DEST"
install -m 0755 "$tmp/mdbook" "$DEST/mdbook"
export PATH="$DEST:$PATH"
echo "Installed mdbook to $DEST/mdbook ($(mdbook --version))"
echo "Add to your shell profile if needed: export PATH=\"$DEST:\$PATH\""
