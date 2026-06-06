#!/usr/bin/env bash
# Install mdBook to /usr/local/bin (or $MDOOK_INSTALL_DIR).
set -euo pipefail

VERSION="${MDBOOK_VERSION:-0.4.40}"
INSTALL_DIR="${MDBOOK_INSTALL_DIR:-/usr/local/bin}"
ARCH="$(uname -m)"
OS="$(uname -s | tr '[:upper:]' '[:lower:]')"

case "${ARCH}" in
  x86_64) ARCH_TAG="x86_64" ;;
  aarch64|arm64) ARCH_TAG="aarch64" ;;
  *)
    echo "Unsupported architecture: ${ARCH}" >&2
    exit 1
    ;;
esac

TARBALL="mdbook-v${VERSION}-${ARCH_TAG}-unknown-${OS}-gnu.tar.gz"
URL="https://github.com/rust-lang/mdBook/releases/download/v${VERSION}/${TARBALL}"

tmpdir="$(mktemp -d)"
trap 'rm -rf "$tmpdir"' EXIT

echo "Downloading ${URL}"
curl -sSL "$URL" | tar -xz -C "$tmpdir"
install -m 755 "$tmpdir/mdbook" "$INSTALL_DIR/mdbook"
echo "Installed $(mdbook --version) to ${INSTALL_DIR}/mdbook"
