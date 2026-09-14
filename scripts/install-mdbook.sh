#!/usr/bin/env bash
# Install mdBook v0.4.40 to /usr/local/bin (or ~/.local/bin without sudo).
set -euo pipefail

VERSION="${MDBOOK_VERSION:-0.4.40}"
ARCH="x86_64-unknown-linux-gnu"
URL="https://github.com/rust-lang/mdBook/releases/download/v${VERSION}/mdbook-v${VERSION}-${ARCH}.tar.gz"

tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

curl -sSL "$URL" | tar -xz -C "$tmp"
bin="$tmp/mdbook"

if command -v sudo >/dev/null 2>&1 && [[ -w /usr/local/bin ]]; then
  install -m 0755 "$bin" /usr/local/bin/mdbook
  echo "Installed mdbook to /usr/local/bin/mdbook"
elif mkdir -p "${HOME}/.local/bin" 2>/dev/null; then
  install -m 0755 "$bin" "${HOME}/.local/bin/mdbook"
  echo "Installed mdbook to ${HOME}/.local/bin/mdbook"
  export PATH="${HOME}/.local/bin:${PATH}"
else
  echo "Could not install mdbook; copy manually from $bin"
  exit 1
fi

mdbook --version
