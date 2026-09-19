#!/usr/bin/env bash
# Validate relative markdown links under src/ resolve to existing files.
# Usage: ./scripts/validate-links.sh
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python3 - "$ROOT/src" <<'PY'
import re, sys
from pathlib import Path

src = Path(sys.argv[1])
broken = []
for md in sorted(src.rglob("*.md")):
    for m in re.finditer(r"\]\((\.\./[^)]+)\)", md.read_text()):
        link = m.group(1).split("#")[0]
        if not link or link.startswith("http"):
            continue
        if not (md.parent / link).resolve().exists():
            broken.append(f"{md.relative_to(src)}: {link}")

if broken:
    print(f"FAIL: {len(broken)} broken relative link(s) in src/")
    for line in broken:
        print(f"  {line}")
    sys.exit(1)

print("OK: all relative links in src/ resolve")
PY
