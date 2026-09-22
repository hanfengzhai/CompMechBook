#!/usr/bin/env bash
# Remove accidental mdBook stub files (paths that included "#anchor" in SUMMARY links).
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
find "$ROOT/src" "$ROOT/writings" -name '*#*' -type f -print -delete 2>/dev/null || true
rm -f "$ROOT/writings/SUMMARY.html"
