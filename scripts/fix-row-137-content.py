#!/usr/bin/env python3
"""Fix row 136/137 lift artifacts and insert sources row 137 index."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WRITINGS = ROOT / "writings"


def patch_all(text: str) -> str:
    text = text.replace(r"V_{	ext{BO}}", r"V_{\text{BO}}")
    text = text.replace("Row 68 → Row 137 Row 68 → Row 57", "Row 68 → Row 117 Row 68 → Row 57")
    text = text.replace(
        "## Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta capstone reunion index (row 136)",
        "## Row 68 → Row 116 Row 68 → Row 56 Born–Oppenheimer meta capstone reunion index (row 136)",
    )
    fixes = [
        ("#skill-navigation-row-116)", "#skill-navigation-row-136)"),
        ("#skill-navigation-row-97)", "#skill-navigation-row-117)"),
        ("[preface row 136](../preface.md#skill-navigation-row-116)", "[preface row 136](../preface.md#skill-navigation-row-136)"),
        ("[preface row 117](../preface.md#skill-navigation-row-97)", "[preface row 117](../preface.md#skill-navigation-row-117)"),
        ("[row 136](preface.md#skill-navigation-row-116)", "[row 136](preface.md#skill-navigation-row-136)"),
        ("[row 117](preface.md#skill-navigation-row-97)", "[row 117](preface.md#skill-navigation-row-117)"),
    ]
    for a, b in fixes:
        text = text.replace(a, b)
    return text


def insert_sources_137(src: str) -> str:
    if "## Row 68 → Row 117 Row 68 → Row 57 Kohn–Sham meta capstone reunion index (row 137)" in src:
        return src
    idx117 = src.find(
        "## Row 68 → Row 97 Row 68 → Row 57 Kohn–Sham meta capstone reunion index (row 117)"
    )
    idx118 = src.find(
        "## Row 68 → Row 98 Row 68 → Row 58 DFT workflows meta capstone reunion index (row 118)"
    )
    if idx117 < 0 or idx118 < 0:
        raise SystemExit("row 117/118 sources anchors missing")
    block117 = src[idx117:idx118]

    def cap(s: str) -> str:
        p = [
            ("Row 117 closing loop", "Row 137 closing loop"),
            ("row-117-closing-loop", "row-137-closing-loop"),
            ("Row 117 skill checkpoint", "Row 137 skill checkpoint"),
            ("skill-navigation-row-117", "skill-navigation-row-137"),
            ("memory sheet row 117", "memory sheet row 137"),
            ("Row 117 baby picture", "Row 137 baby picture"),
            (
                "Row 68 → Row 97 Row 68 → Row 57 Kohn–Sham meta capstone reunion index (row 117)",
                "Row 68 → Row 117 Row 68 → Row 57 Kohn–Sham meta capstone reunion index (row 137) {#row68-row117-kohn-sham-meta-capstone-reunion-index-row-137}",
            ),
            (
                "row68-row97-kohn-sham-meta-capstone-reunion-index-row-117",
                "row68-row117-kohn-sham-meta-capstone-reunion-index-row-137",
            ),
            (
                "row-117-baby-picture-row68-row97-kohn-sham-meta-capstone-reunion",
                "row-137-baby-picture-row68-row117-kohn-sham-meta-capstone-reunion",
            ),
            ("row 117", "row 137"),
            ("Row 117", "Row 137"),
            ("[row 116]", "[row 136]"),
            ("row 116", "row 136"),
            ("Row 116", "Row 136"),
            ("[row 97]", "[row 117]"),
            ("row 97", "row 117"),
            ("Row 97", "Row 117"),
            ("inside Part IX", "inside the coupling gate on the capstone path"),
            ("Row 68 → Row 57 move |", "Row 68 → Row 57 move (capstone path) |"),
            (
                "before row 118 DFT workflows meta capstone opens",
                "before row 58 DFT workflows meta prelude opens on the capstone path",
            ),
            (
                "row 116 closed Born–Oppenheimer meta capstone",
                "row 136 closed Born–Oppenheimer meta capstone",
            ),
            (
                "verified Born–Oppenheimer meta capstone closure (row 116)",
                "verified Born–Oppenheimer meta capstone closure (row 136)",
            ),
            ("on the capstone path on the capstone path", "on the capstone path"),
        ]
        for a, b in p:
            s = s.replace(a, b)
        s = s.replace(
            "{#row68-row117-kohn-sham-meta-capstone-reunion-index-row-137} {#row68-row97-kohn-sham-meta-capstone-reunion-index-row-117}",
            "{#row68-row117-kohn-sham-meta-capstone-reunion-index-row-137}",
        )
        return s

    block137 = cap(block117)
    table = (
        "| 137 | Row 68 → Row 117 Row 68 → Row 57 Kohn–Sham meta capstone (midpoint prelude gate ↔ Born–Oppenheimer meta capstone ↔ row 57 meta) | "
        "[Row 68 → Row 117 Kohn–Sham meta capstone reunion index](#row68-row117-kohn-sham-meta-capstone-reunion-index-row-137) · "
        "[preface row 137](../preface.md#skill-navigation-row-137) · "
        "[prologue row 137 preview](../prologue/00-many-scales.md#prologue-preview-row-137) · "
        "[prologue row 137 closing stitch](../prologue/00-many-scales.md#row-137-closing-stitch) · "
        "[epilogue row 137 closing loop](../epilogue/multiscale.md#row-137-closing-loop) · "
        "[memory sheet row 137 baby picture](memory-sheet.md#row-137-baby-picture-row68-row117-kohn-sham-meta-capstone-reunion) | "
        "Row 68 closed but **row 57 IX.1 → IX.2 opening hinge still feels disconnected from verified Born–Oppenheimer meta capstone on the capstone path** — "
        "read row 68 + row 136 or row 117 gate + IX.1 Bridge → opening hinge → IX.2 Kohn–Sham SCF + row 57; "
        "[preface row 57](../preface.md#skill-navigation-row-57) |\n"
    )
    src = src.replace(
        "| 136 | Row 68 → Row 116 Row 68 → Row 56 Born–Oppenheimer meta capstone",
        table + "| 136 | Row 68 → Row 116 Row 68 → Row 56 Born–Oppenheimer meta capstone",
    )
    src = src.replace(
        "## Row 68 → Row 97 Row 68 → Row 57 Kohn–Sham meta capstone reunion index (row 117)",
        block137 + "## Row 68 → Row 97 Row 68 → Row 57 Kohn–Sham meta capstone reunion index (row 117)",
    )
    return src


def rebuild_row137_baby(mem: str) -> str:
    start = mem.find("### Row 117 baby picture")
    end = mem.find("### Row 118 baby picture", start)
    if start < 0 or end < 0:
        raise SystemExit("row 117 baby picture block missing")
    baby117 = mem[start:end]
    baby137 = baby117
    reps = [
        ("Row 117 baby picture", "Row 137 baby picture"),
        ("row-117-baby-picture-row68-row97-kohn-sham-meta-capstone-reunion", "row-137-baby-picture-row68-row117-kohn-sham-meta-capstone-reunion"),
        ("Row 68 → Row 97 Row 68 → Row 57", "Row 68 → Row 117 Row 68 → Row 57"),
        ("row68-row97-kohn-sham-meta-capstone-reunion-index-row-117", "row68-row117-kohn-sham-meta-capstone-reunion-index-row-137"),
        ("row 117", "row 137"),
        ("Row 117", "Row 137"),
        ("[row 116]", "[row 136]"),
        ("skill-navigation-row-116", "skill-navigation-row-136"),
        ("[row 97]", "[row 117]"),
        ("skill-navigation-row-97", "skill-navigation-row-117"),
        ("row 116 when", "row 136 when"),
        ("row 117 when", "row 137 when"),
        ("before row 118 DFT workflows meta capstone or row 98 prelude opens", "before row 138 DFT workflows meta capstone or row 58 workflow reunion opens on the capstone path"),
        ("on the capstone path", "on the capstone path"),
    ]
    for a, b in reps:
        baby137 = baby137.replace(a, b)
    if "### Row 137 baby picture" in mem:
        s0 = mem.find("### Row 137 baby picture")
        s1 = mem.find("### Act VI baby picture", s0)
        if s0 >= 0 and s1 >= 0:
            mem = mem[:s0] + baby137 + mem[s1:]
    return mem


def main() -> None:
    for rel in [
        "preface/chapters/preface.md",
        "prologue/chapters/00-many-scales.md",
        "epilogue/chapters/multiscale.md",
        "appendix/chapters/memory-sheet.md",
        "appendix/chapters/sources.md",
    ]:
        path = WRITINGS / rel
        text = patch_all(path.read_text())
        if rel.endswith("sources.md"):
            text = insert_sources_137(text)
        if rel.endswith("memory-sheet.md"):
            text = rebuild_row137_baby(text)
        path.write_text(text)
    print("fix-row-137-content: OK")


if __name__ == "__main__":
    main()
