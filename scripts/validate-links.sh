#!/usr/bin/env bash
# Validate relative markdown links under src/ resolve to existing files.
# Catches ../, ./, bare relative paths, and scripts/ from repo root.
# Skips LaTeX false positives (e.g. [\rho](\mathbf{r}) inside math).
# Usage: ./scripts/validate-links.sh
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python3 - "$ROOT/src" "$ROOT" <<'PY'
import re, sys
from pathlib import Path

src = Path(sys.argv[1])
root = Path(sys.argv[2])
link_re = re.compile(r"\]\((?!https?://|mailto:|#)([^)]+)\)")

broken = []
for md in sorted(src.rglob("*.md")):
    for m in link_re.finditer(md.read_text()):
        link = m.group(1).split("#")[0].strip()
        if not link or link.startswith("/") or link.startswith("\\"):
            continue
        if link.startswith("scripts/"):
            target = (root / link).resolve()
        else:
            target = (md.parent / link).resolve()
        if not target.exists():
            broken.append(f"{md.relative_to(src)}: {link}")

if broken:
    print(f"FAIL: {len(broken)} broken relative link(s) in src/")
    for line in broken:
        print(f"  {line}")
    sys.exit(1)

print("OK: all relative links in src/ resolve")
PY
