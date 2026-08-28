#!/usr/bin/env bash
# Validate relative markdown links under src/ (default) or writings/ (--writings).
# Catches ../, ./, bare relative paths, and scripts/ from repo root.
# Skips LaTeX false positives (e.g. [\rho](\mathbf{r}) inside math).
# Usage:
#   ./scripts/validate-links.sh            # src/
#   ./scripts/validate-links.sh --writings # writings/ resolved via src/ mirror
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MODE="src"
for arg in "$@"; do
  case "$arg" in
    --writings) MODE="writings" ;;
  esac
done

python3 - "$ROOT" "$MODE" <<'PY'
import re, sys
from pathlib import Path

root = Path(sys.argv[1])
mode = sys.argv[2]
link_re = re.compile(r"\]\((?!https?://|mailto:|#)([^)]+)\)")

PART_MAP = {
    "linear-algebra": "part01-linear-algebra",
    "functional-analysis": "part02-functional-analysis",
    "pde": "part03-pdes",
    "fem": "part04-fem",
    "fvm": "part05-fvm",
    "continuum": "part06-continuum",
    "defects": "part07-defects",
    "md": "part08-md",
    "dft": "part09-dft",
}


def strip_anchor(link: str) -> str:
    return link.split("#")[0].strip()


def skip_link(link: str) -> bool:
    path_part = strip_anchor(link)
    return not path_part or path_part.startswith("/") or path_part.startswith("\\")


def resolve_src(md: Path, link: str) -> Path | None:
    if skip_link(link):
        return Path("/dev/null")
    path_part = strip_anchor(link)
    if path_part.startswith("scripts/") or path_part.startswith("fixtures/"):
        target = (root / path_part).resolve()
    else:
        target = (md.parent / path_part).resolve()
    return target if target.exists() else None


def writings_to_src_md(wmd: Path) -> Path | None:
    try:
        rel = wmd.relative_to(root / "writings")
    except ValueError:
        return None
    parts = rel.parts
    if not parts:
        return None
    if parts[0] == "preface" and rel.name == "preface.md":
        return root / "src" / "preface.md"
    if parts[0] == "prologue" and len(parts) >= 2:
        return root / "src" / "prologue" / rel.name
    if parts[0] == "epilogue" and len(parts) >= 2:
        return root / "src" / "epilogue" / rel.name
    if parts[0] == "appendix" and len(parts) >= 2:
        return root / "src" / "appendix" / rel.name
    if parts[0] in PART_MAP and len(parts) >= 2 and parts[1] == "chapters":
        return root / "src" / PART_MAP[parts[0]] / rel.name
    return None


def resolve_writings(md: Path, link: str) -> Path | None:
    if skip_link(link):
        return Path("/dev/null")
    src_md = writings_to_src_md(md)
    if src_md is not None:
        return resolve_src(src_md, link)
    local = (md.parent / strip_anchor(link)).resolve()
    return local if local.exists() else None


if mode == "writings":
    scan_dir = root / "writings"
    label = "writings/"
    resolver = resolve_writings
else:
    scan_dir = root / "src"
    label = "src/"
    resolver = resolve_src

broken = []
for md in sorted(scan_dir.rglob("*.md")):
    for m in link_re.finditer(md.read_text()):
        link = m.group(1)
        if resolver(md, link) is None:
            broken.append(f"{md.relative_to(root)}: {link}")

if broken:
    print(f"FAIL: {len(broken)} broken relative link(s) in {label}")
    for line in broken[:50]:
        print(f"  {line}")
    if len(broken) > 50:
        print(f"  ... and {len(broken) - 50} more")
    sys.exit(1)

print(f"OK: all relative links in {label} resolve")
PY
