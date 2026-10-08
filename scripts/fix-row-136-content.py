#!/usr/bin/env python3
"""Repair row 136 preface after naive tx from row 135 (capstone lift from row 116 template)."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
preface_path = ROOT / "writings/preface/chapters/preface.md"


def extract_row(n: int, text: str) -> str | None:
    pat = rf"(### Row {n} skill checkpoint.*?)(?=\n### Row {n+1} skill checkpoint|\n## The copper wire)"
    m = re.search(pat, text, re.S)
    return m.group(1) if m else None


def main():
    text = preface_path.read_text()
    r116 = extract_row(116, text)
    if not r116:
        raise SystemExit("row 116 checkpoint missing")
    P = [
        ("Row 116 skill checkpoint", "Row 136 skill checkpoint"),
        ("skill-navigation-row-116", "skill-navigation-row-136"),
        (
            "Row 68 → Row 96 Row 68 → Row 56 Born–Oppenheimer meta capstone reunion",
            "Row 68 → Row 116 Row 68 → Row 56 Born–Oppenheimer meta capstone reunion",
        ),
        (
            "row68-row96-born-oppenheimer-meta-capstone-reunion-index-row-116",
            "row68-row116-born-oppenheimer-meta-capstone-reunion-index-row-136",
        ),
        (
            "row-116-baby-picture-row68-row96-born-oppenheimer-meta-capstone-reunion",
            "row-136-baby-picture-row68-row116-born-oppenheimer-meta-capstone-reunion",
        ),
        ("Row 116 three-way audit", "Row 136 three-way audit"),
        ("([row 116]", "([row 136]"),
        ("prologue-preview-row-116", "prologue-preview-row-136"),
        ("row-116-closing-stitch", "row-136-closing-stitch"),
        ("row-116-closing-loop", "row-136-closing-loop"),
        ("memory sheet row 116 baby picture", "memory sheet row 136 baby picture"),
        ("Row 68 ↔ Row 56 reunion |", "Row 68 ↔ Row 56 reunion (capstone path) |"),
        (
            "electronic audit meta capstone / Born–Oppenheimer opening prelude hinge",
            "electronic audit meta prelude capstone / Born–Oppenheimer opening prelude hinge on the capstone path",
        ),
        (
            "[row 115](preface.md#skill-navigation-row-115) or [row 96]",
            "[row 135](preface.md#skill-navigation-row-135) or [row 116]",
        ),
        (
            "[Row 68 → Row 76 Born–Oppenheimer meta prelude reunion index (row 96)](appendix/sources.md#row68-row76-born-oppenheimer-meta-prelude-reunion-index-row-96)",
            "[Row 68 → Row 96 Born–Oppenheimer meta capstone reunion index (row 116)](appendix/sources.md#row68-row96-born-oppenheimer-meta-capstone-reunion-index-row-116)",
        ),
        ("electronic audit meta capstone", "electronic audit meta prelude capstone"),
        (
            "after IX.0's foundation SCF audit Lab act**",
            "after IX.0's foundation SCF audit Lab act on the capstone path**",
        ),
        (
            "row 115's foundation SCF → BO vocabulary turn at the IX.0 → IX.1 chapter boundary inside Part IX",
            "row 135's foundation SCF → BO vocabulary turn at the Born–Oppenheimer meta capstone boundary inside the coupling gate on the capstone path",
        ),
        (
            "Row 116 does not replace row 68, row 56, row 115, row 96, row 76, row 95, or row 37",
            "Row 136 does not replace row 68, row 56, row 135, row 116, row 96, row 76, or row 37",
        ),
        (
            "before IX.2 opens at \\(T_w\\)",
            "before row 57 Kohn–Sham meta prelude opens on the capstone path at \\(T_w\\)",
        ),
        ("Row 68 → Row 96 Born–Oppenheimer meta capstone reunion index", "Row 68 → Row 116 Born–Oppenheimer meta capstone reunion index"),
        ("Row 68 → Row 96 reunion index", "Row 68 → Row 116 reunion index"),
        ("row 115 closed but row 56", "row 135 closed but row 56"),
        ("when `cu.relax.out` exists but", "when `cu.relax.out` exists on the capstone path but"),
        ("after row 115.", "after row 135."),
        ("when row 115 and row 56", "when row 135 and row 56"),
        ("before row 56 closes", "before row 57 closes on the capstone path"),
        ("prologue row 116 closing stitch", "prologue row 136 closing stitch"),
        ("prologue row 116 preview", "prologue row 136 preview"),
        ("epilogue row 116 closing loop", "epilogue row 136 closing loop"),
    ]
    r136 = r116
    for a, b in P:
        r136 = r136.replace(a, b)
    tail = (
        "**When to pause.** Read the [prologue row 136 closing stitch](prologue/00-many-scales.md#row-136-closing-stitch) first when row 135 closed but row 56 IX.0 → IX.1 reunion still feels like quantum chemistry homework disconnected from verified electronic audit meta prelude capstone on the capstone path — it names the dual reunion before the Murnaghan Lab act. Then read the [prologue row 136 preview](prologue/00-many-scales.md#prologue-preview-row-136) when `cu.relax.out` exists on the capstone path but \\(V_{\\text{BO}}\\) is unnamed after row 135. Return to the [Row 68 → Row 116 reunion index](appendix/sources.md#row68-row116-born-oppenheimer-meta-capstone-reunion-index-row-136) when row 135 and row 56 both verify individually but **electronic audit meta prelude capstone and IX.0 → IX.1 opening hinge still feel like separate stories** — the break is usually skipping [IX.0's Bridge](part09-dft/00-opening.md#bridge), not missing Murnaghan algebra. Read the [memory sheet row 136 baby picture](appendix/memory-sheet.md#row-136-baby-picture-row68-row116-born-oppenheimer-meta-capstone-reunion) when opening [row 117](preface.md#skill-navigation-row-117) before row 57 closes on the capstone path; read the [epilogue row 136 closing loop](epilogue/multiscale.md#row-136-closing-loop) when the competence loop closes. When row 135 is complete, proceed to [row 136](preface.md#skill-navigation-row-136) when electronic audit meta prelude capstone is clean but Born–Oppenheimer meta capstone still lags after verified foundation SCF archive on the capstone path, to [row 116](preface.md#skill-navigation-row-116) when electronic audit meta capstone is clean but Born–Oppenheimer meta capstone still lags on the opening-hinge path, to [row 96](preface.md#skill-navigation-row-96) for the Row 68 ↔ Row 56 Born–Oppenheimer opening prelude audit alone, to [row 135](preface.md#skill-navigation-row-135) when export meta prelude capstone still lags after verified pedigree checklist on the capstone path, to [row 56](preface.md#skill-navigation-row-56) when only IX.0 → IX.1 stalls, or extend prose only under `writings/` then sync.\n"
    )
    r136 = re.sub(r"\*\*When to pause\.\*\*.*", tail.rstrip(), r136, count=1, flags=re.S)
    old = extract_row(136, text)
    if not old:
        raise SystemExit("row 136 checkpoint missing")
    text = text.replace(old, r136)
    preface_path.write_text(text)
    print("fix-row-136-content: preface OK")


if __name__ == "__main__":
    main()
