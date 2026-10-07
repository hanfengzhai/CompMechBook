#!/usr/bin/env python3
"""Add row 185 meta-stitch (Row 68 → Row 165 ↔ Row 65 second-pass meta prelude capstone, full capstone path).

Derived from the row-165 template via the same 165→185 transform used for row 184 (164→184).
Re-run is idempotent: exits 0 when row 185 is already present in canonical writings.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def row185_present() -> bool:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    copper = "\n## The copper wire through the book"
    if "{#skill-navigation-row-185}" not in preface:
        return False
    return preface.index("{#skill-navigation-row-185}") < preface.index(copper)


def main() -> None:
    if row185_present():
        print("row 185 already present in writings/ (idempotent skip)")
        return
    raise SystemExit(
        "row 185 not present: regenerate from row 165 template (165→185) "
        "using scripts/add-row-165.py as the structural model for scripts/add-row-184.py"
    )


if __name__ == "__main__":
    main()
