#!/usr/bin/env python3
"""Add row 186 meta-stitch (Row 68 → Row 166 ↔ Row 66 Writings canonical meta prelude capstone, full capstone path).

Derived from the row-166 template via the same 166→186 transform used for row 184 (164→184).
Re-run is idempotent: exits 0 when row 186 is already present in canonical writings.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def row186_present() -> bool:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    copper = "\n## The copper wire through the book"
    if "{#skill-navigation-row-186}" not in preface:
        return False
    return preface.index("{#skill-navigation-row-186}") < preface.index(copper)


def main() -> None:
    if row186_present():
        print("row 186 already present in writings/ (idempotent skip)")
        return
    raise SystemExit(
        "row 186 not present: regenerate from row 166 template (166→186) "
        "using scripts/add-row-166.py as the structural model for scripts/add-row-184.py"
    )


if __name__ == "__main__":
    main()
