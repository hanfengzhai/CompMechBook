#!/usr/bin/env python3
"""Repair row 156 preface checkpoint after lift from row 136."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
preface_path = ROOT / "writings/preface/chapters/preface.md"


def extract_row(n: int, text: str) -> str | None:
    pat = rf"(### Row {n} skill checkpoint.*?)(?=\n### Row {n + 1} skill checkpoint|\n## The copper wire)"
    m = re.search(pat, text, re.S)
    return m.group(1) if m else None


def main() -> None:
    text = preface_path.read_text()
    r136 = extract_row(136, text)
    if not r136:
        raise SystemExit("row 136 checkpoint missing")
    r156 = extract_row(156, text)
    if not r156:
        raise SystemExit("row 156 checkpoint missing — run add-row-156.py first")

    P = [
        ("[row 115](preface.md#skill-navigation-row-115)", "[row 155](preface.md#skill-navigation-row-155)"),
        (
            "[Row 68 → Row 116 Born–Oppenheimer meta prelude capstone reunion index (row 116)]",
            "[Row 68 → Row 136 Born–Oppenheimer meta prelude capstone reunion index (row 136)](appendix/sources.md#row68-row116-born-oppenheimer-meta-capstone-reunion-index-row-136)",
        ),
        (
            "Row 156 does not replace row 68, row 56, row 135, row 116, row 96, row 76, or row 37",
            "Row 156 does not replace row 68, row 56, row 155, row 136, row 116, row 96, row 76, or row 37",
        ),
        (
            "([row 136](prologue/00-many-scales.md#prologue-preview-row-156))",
            "([row 156](prologue/00-many-scales.md#prologue-preview-row-156))",
        ),
        ("Born–Oppenheimer meta prelude capstone reunion audit audit", "Born–Oppenheimer meta prelude capstone reunion audit"),
    ]
    for a, b in P:
        r156 = r156.replace(a, b)

    tail = (
        "**When to pause.** Read the [prologue row 156 closing stitch](prologue/00-many-scales.md#row-156-closing-stitch) first when row 155 closed but row 56 IX.0 → IX.1 reunion still feels like quantum chemistry homework disconnected from verified electronic audit meta prelude capstone on the capstone path — it names the dual reunion before the Kohn–Sham meta prelude capstone reunion. Then read the [prologue row 156 preview](prologue/00-many-scales.md#prologue-preview-row-156) when `cu.relax.out` exists on the capstone path but \\(V_{\\text{BO}}\\) is unnamed after row 155. Return to the [Row 68 → Row 136 reunion index](appendix/sources.md#row68-row136-born-oppenheimer-meta-prelude-capstone-reunion-index-row-156) when row 155 and row 56 both verify individually but **electronic audit meta prelude capstone and IX.0 → IX.1 opening hinge still feel like separate stories** — the break is usually skipping [IX.0's Bridge](part09-dft/00-opening.md#bridge), not missing Murnaghan algebra. Read the [memory sheet row 156 baby picture](appendix/memory-sheet.md#row-156-baby-picture-row68-row136-born-oppenheimer-meta-prelude-capstone-reunion) when opening [row 157](preface.md#skill-navigation-row-157) before row 57 closes on the capstone path; read the [epilogue row 156 closing loop](epilogue/multiscale.md#row-156-closing-loop) when the competence loop closes. When row 156 is complete, proceed to [row 157](preface.md#skill-navigation-row-157) when Born–Oppenheimer meta prelude capstone is clean but Kohn–Sham meta prelude capstone still lags after verified Murnaghan archive on the capstone path, to [row 137](preface.md#skill-navigation-row-137) when Born–Oppenheimer meta capstone is clean but Kohn–Sham meta capstone still lags on the opening-hinge path, to [row 97](preface.md#skill-navigation-row-117) for the Row 68 ↔ Row 57 Kohn–Sham opening prelude audit alone, to [row 156](preface.md#skill-navigation-row-156) when electronic audit meta prelude capstone still lags after verified foundation SCF on the capstone path, to [row 57](preface.md#skill-navigation-row-57) when only IX.1 → IX.2 stalls, or extend prose only under `writings/` then sync.\n"
    )
    r156 = re.sub(r"\*\*When to pause\.\*\*.*", tail.rstrip(), r156, count=1, flags=re.S)
    old156 = extract_row(156, text)
    if not old156:
        raise SystemExit("row 156 block not found after edit")
    text = text.replace(old156, r156)
    preface_path.write_text(text)
    print("fix-row-156-content: preface OK")


if __name__ == "__main__":
    main()
