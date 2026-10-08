#!/usr/bin/env python3
"""Fix row 156 lift artifacts, sources table row, memory baby picture, and prologue labels."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFACE = ROOT / "writings/preface/chapters/preface.md"
PROLOGUE = ROOT / "writings/prologue/chapters/00-many-scales.md"
EPILOGUE = ROOT / "writings/epilogue/chapters/multiscale.md"
SOURCES = ROOT / "writings/appendix/chapters/sources.md"
MEMORY = ROOT / "writings/appendix/chapters/memory-sheet.md"


def tx(s: str, pairs: list[tuple[str, str]]) -> str:
    for a, b in pairs:
        s = s.replace(a, b)
    return s


def bump136_to_156(s: str) -> str:
    """Lift opening-hinge row 136 checkpoint to capstone row 156 (+20 meta bump)."""
    p = [
        ("skill-navigation-row-136", "skill-navigation-row-156"),
        ("### Row 136 skill checkpoint", "### Row 156 skill checkpoint"),
        ("Row 136 does not replace", "Row 156 does not replace"),
        ("Row 136 three-way audit", "Row 156 three-way audit"),
        ("row-136-closing-stitch", "row-156-closing-stitch"),
        ("prologue-preview-row-136", "prologue-preview-row-156"),
        ("Row 136 preview", "Row 156 preview"),
        ("memory sheet row 136", "memory sheet row 156"),
        (
            "Row 68 → Row 116 Row 68 → Row 56 Born–Oppenheimer meta capstone",
            "Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone",
        ),
        (
            "row68-row116-born-oppenheimer-meta-capstone-reunion-index-row-136",
            "row68-row136-born-oppenheimer-meta-prelude-capstone-reunion-index-row-156",
        ),
        (
            "row-136-baby-picture-row68-row116-born-oppenheimer-meta-capstone-reunion",
            "row-156-baby-picture-row68-row136-born-oppenheimer-meta-prelude-capstone-reunion",
        ),
        ("Born–Oppenheimer meta capstone reunion", "Born–Oppenheimer meta prelude capstone reunion"),
        ("Born–Oppenheimer meta capstone boundary", "Born–Oppenheimer meta prelude capstone boundary"),
        ("before Born–Oppenheimer meta capstone", "before Born–Oppenheimer meta prelude capstone"),
        ("[row 137]", "__R157__"),
        ("[row 135]", "[row 155]"),
        ("row 135", "row 155"),
        ("Row 135", "Row 155"),
        ("__R157__", "[row 157]"),
        ("row 134", "row 154"),
        ("Row 134", "Row 154"),
        (
            "verified electronic audit meta prelude capstone closure with the full-book IX.0 → IX.1 Born–Oppenheimer meta capstone reunion",
            "verified electronic audit meta prelude capstone closure (row 155) with the full-book IX.0 → IX.1 Born–Oppenheimer meta prelude capstone reunion",
        ),
        ("when row 135 closed but row 56", "when row 155 closed but row 56"),
        ("when row 135 and row 56", "when row 155 and row 56"),
        (
            "rear-view mirror of row 135's foundation SCF → BO vocabulary turn at the Born–Oppenheimer meta capstone boundary",
            "rear-view mirror of row 155's foundation SCF → BO vocabulary turn at the Born–Oppenheimer meta prelude capstone boundary",
        ),
        (
            "when opening [row 117](preface.md#skill-navigation-row-117) before row 57 closes on the capstone path",
            "when opening [row 157](preface.md#skill-navigation-row-157) before row 57 closes on the capstone path",
        ),
        (
            "When row 136 is complete, proceed to [row 137]",
            "When row 156 is complete, proceed to [row 157]",
        ),
        (
            "When row 136 is complete, proceed to [row 137](preface.md#skill-navigation-row-137) when Born–Oppenheimer meta capstone is clean but Kohn–Sham meta capstone still lags after verified Murnaghan archive on the capstone path, to [row 117](preface.md#skill-navigation-row-117) when Born–Oppenheimer meta capstone is clean but Kohn–Sham meta capstone still lags on the opening-hinge path, to [row 97](preface.md#skill-navigation-row-117) for the Row 68 ↔ Row 57 Kohn–Sham opening prelude audit alone, to [row 136](preface.md#skill-navigation-row-136) when electronic audit meta prelude capstone still lags after verified foundation SCF on the capstone path, to [row 57](preface.md#skill-navigation-row-57) when only IX.1 → IX.2 stalls, or extend prose only under `writings/` then sync.",
            "When row 156 is complete, proceed to [row 157](preface.md#skill-navigation-row-157) when Born–Oppenheimer meta prelude capstone is clean but Kohn–Sham meta prelude capstone still lags after verified Murnaghan archive on the capstone path, to [row 137](preface.md#skill-navigation-row-137) when Born–Oppenheimer meta prelude capstone is clean but Kohn–Sham meta prelude capstone still lags on the opening-hinge path, to [row 117](preface.md#skill-navigation-row-117) for the Row 68 ↔ Row 57 Kohn–Sham opening prelude audit alone, to [row 155](preface.md#skill-navigation-row-155) when export meta prelude capstone still lags after verified pedigree checklist on the capstone path, to [row 57](preface.md#skill-navigation-row-57) when only IX.1 → IX.2 stalls, or extend prose only under `writings/` then sync.",
        ),
        ("[row 116](preface.md#skill-navigation-row-96)", "[row 136](preface.md#skill-navigation-row-136)"),
        (
            "Row 68 → Row 116 Born–Oppenheimer meta capstone reunion index (row 116)",
            "Row 68 → Row 136 Born–Oppenheimer meta prelude capstone reunion index (row 136)",
        ),
        (
            "row68-row96-born-oppenheimer-meta-capstone-reunion-index-row-116",
            "row68-row136-born-oppenheimer-meta-prelude-capstone-reunion-index-row-136",
        ),
        ("row 135 or row 116", "row 155 or row 136"),
        ("row 116", "row 136"),
        ("Row 116", "Row 136"),
        ("row 96", "row 116"),
        ("row 76", "row 96"),
        ("row 37", "row 57"),
        ("before the Murnaghan Lab act", "before the Kohn–Sham meta prelude capstone reunion"),
        ("[preface row 136 closing loop]", "[epilogue row 156 closing loop]"),
        ("epilogue row 136 closing loop", "epilogue row 156 closing loop"),
        ("row-136-closing-loop", "row-156-closing-loop"),
        ("prologue row 136 closing stitch", "prologue row 156 closing stitch"),
        ("prologue row 136 preview", "prologue row 156 preview"),
        ("[row 136](prologue/00-many-scales.md#prologue-preview-row-156)", "[row 156](prologue/00-many-scales.md#prologue-preview-row-156)"),
        (
            "[row 155](preface.md#skill-navigation-row-135)",
            "[row 155](preface.md#skill-navigation-row-155)",
        ),
        (
            "VIII.3 Bridge → IX.0 SCF recited",
            "IX.0 Bridge → IX.1 BO/HK recited on the capstone path",
        ),
        (
            "beside [electronic audit export manifest](part09-dft/00-opening.md#electronic-audit-export-manifest-handoff-to-ix1) at \\(T_w\\), one dft arc under `writings/dft` chapters 00–01)",
            "beside [electronic audit export manifest](part09-dft/00-opening.md#electronic-audit-export-manifest-handoff-to-ix1) at \\(T_w\\), one SCF → BO arc under `writings/dft` chapters 00–01 on the capstone path)",
        ),
    ]
    return tx(s, p)


def fix_preface() -> None:
    text = PREFACE.read_text()
    m136 = re.search(
        r"(### Row 136 skill checkpoint.*?)(?=\n### Row 137 skill checkpoint)",
        text,
        re.S,
    )
    if not m136:
        raise SystemExit("row 136 checkpoint missing")
    good156 = bump136_to_156(m136.group(1))
    text = re.sub(
        r"### Row 156 skill checkpoint.*?(?=\n## The copper wire through the book)",
        good156.rstrip() + "\n",
        text,
        count=1,
        flags=re.S,
    )
    row155_proceed_old = (
        "When row 136 is complete, proceed to [row 137](preface.md#skill-navigation-row-137) when Born–Oppenheimer meta capstone is clean but Kohn–Sham meta capstone still lags after verified Murnaghan archive on the capstone path, to [row 117](preface.md#skill-navigation-row-117) when Born–Oppenheimer meta capstone is clean but Kohn–Sham meta capstone still lags on the opening-hinge path, to [row 97](preface.md#skill-navigation-row-117) for the Row 68 ↔ Row 57 Kohn–Sham opening prelude audit alone, to [row 136](preface.md#skill-navigation-row-136) when electronic audit meta prelude capstone still lags after verified foundation SCF on the capstone path, to [row 57](preface.md#skill-navigation-row-57) when only IX.1 → IX.2 stalls, or extend prose only under `writings/` then sync."
    )
    row155_proceed_new = (
        "When row 155 is complete, proceed to [row 156](preface.md#skill-navigation-row-156) when electronic audit meta prelude capstone is clean but Born–Oppenheimer meta prelude capstone still lags after verified foundation SCF archive on the capstone path, to [row 136](preface.md#skill-navigation-row-136) when electronic audit meta capstone is clean but Born–Oppenheimer meta capstone still lags on the opening-hinge path, to [row 116](preface.md#skill-navigation-row-116) for the Row 68 ↔ Row 56 Born–Oppenheimer opening prelude audit alone, to [row 155](preface.md#skill-navigation-row-155) when export meta prelude capstone still lags after verified pedigree checklist on the capstone path, to [row 56](preface.md#skill-navigation-row-56) when only IX.0 → IX.1 stalls, or extend prose only under `writings/` then sync."
    )
    text = text.replace(row155_proceed_old, row155_proceed_new)
    PREFACE.write_text(text)
    print("preface: fixed row 156")


def fix_prologue_compass() -> None:
    text = PROLOGUE.read_text()
    text = text.replace(
        "Born–Oppenheimer meta prelude capstone reunion (row 136) | [Preface: row 136 skill checkpoint]",
        "Born–Oppenheimer meta prelude capstone reunion (row 156) | [Preface: row 156 skill checkpoint]",
    )
    text = text.replace(
        "../preface.md#skill-navigation-row-156) · [Row 68 → Row 116 Born–Oppenheimer meta prelude capstone reunion index",
        "../preface.md#skill-navigation-row-156) · [Row 68 → Row 136 Born–Oppenheimer meta prelude capstone reunion index",
    )
    text = text.replace("prologue row 136 preview row", "prologue row 156 preview row", 1)
    text = text.replace("prologue row 136 closing stitch", "prologue row 156 closing stitch", 1)
    text = text.replace("epilogue row 136 closing loop", "epilogue row 156 closing loop", 1)
    text = text.replace("row 155 or row 116 electronic", "row 155 or row 136 electronic")
    PROLOGUE.write_text(text)
    print("prologue: fixed row 156 compass labels")


def fix_epilogue_loop() -> None:
    text = EPILOGUE.read_text()
    m136 = re.search(
        r"(### Row 136 closing loop \(Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta capstone reunion\) \{[^}]+\}.*?)(?=\n### Row 135 closing loop)",
        text,
        re.S,
    )
    if not m136:
        raise SystemExit("row 136 epilogue loop missing")
    good = bump136_to_156(m136.group(1))
    good = good.replace("Row 136 closing loop", "Row 156 closing loop", 1)
    good = good.replace("row-136-closing-loop", "row-156-closing-loop", 1)
    text = re.sub(
        r"### Row 156 closing loop.*?(\n### Row 155 closing loop)",
        good.rstrip() + r"\1",
        text,
        count=1,
        flags=re.S,
    )
    EPILOGUE.write_text(text)
    print("epilogue: fixed row 156 loop")


def add_sources_table_row() -> None:
    text = SOURCES.read_text()
    if "row68-row136-born-oppenheimer-meta-prelude-capstone-reunion-index-row-156" in text:
        print("sources: row 156 already in table")
        return
    row = (
        "| 156 | Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone (midpoint prelude gate ↔ electronic audit meta prelude capstone ↔ row 56 meta) | "
        "[Row 68 → Row 136 Born–Oppenheimer meta prelude capstone reunion index](#row68-row136-born-oppenheimer-meta-prelude-capstone-reunion-index-row-156) · "
        "[preface row 156](../preface.md#skill-navigation-row-156) · "
        "[prologue row 156 preview](../prologue/00-many-scales.md#prologue-preview-row-156) · "
        "[prologue row 156 closing stitch](../prologue/00-many-scales.md#row-156-closing-stitch) · "
        "[epilogue row 156 closing loop](../epilogue/multiscale.md#row-156-closing-loop) · "
        "[memory sheet row 156 baby picture](memory-sheet.md#row-156-baby-picture-row68-row136-born-oppenheimer-meta-prelude-capstone-reunion) | "
        "Row 68 closed but **row 56 IX.0 → IX.1 opening hinge still feels disconnected from verified electronic audit meta prelude capstone on the capstone path** — "
        "read row 68 + row 155 or row 136 gate + IX.0 Bridge → opening hinge → IX.1 BO/HK + row 56; "
        "[preface row 56](../preface.md#skill-navigation-row-56) |\n"
    )
    text = text.replace(
        "| 155 | Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone",
        row + "| 155 | Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone",
    )
    idx116 = text.find(
        "## Row 68 → Row 96 Row 68 → Row 56 Born–Oppenheimer meta capstone reunion index (row 116)"
    )
    idx117 = text.find(
        "## Row 68 → Row 97 Row 68 → Row 57 Kohn–Sham meta capstone reunion index (row 117)"
    )
    if idx116 < 0 or idx117 < 0:
        raise SystemExit("sources row 116/117 section missing")
    block = bump136_to_156(text[idx116:idx117])
    block = block.replace(
        "## Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion index (row 136)",
        "## Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion index (row 156) {#row68-row136-born-oppenheimer-meta-prelude-capstone-reunion-index-row-156}",
        1,
    )
    block = block.replace(
        "{#row68-row96-born-oppenheimer-meta-capstone-reunion-index-row-116}",
        "",
        1,
    )
    text = text.replace(
        "## Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 155)",
        block + "## Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 155)",
    ) if "## Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 155)" in text else text
    if "row68-row136-born-oppenheimer-meta-prelude-capstone-reunion-index-row-156" not in text:
        text = text.replace(
            "| 155 | Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone",
            row + "| 155 | Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone",
        )
    SOURCES.write_text(text)
    print("sources: added row 156")


def add_memory() -> None:
    text = MEMORY.read_text()
    if "row-156-baby-picture" in text:
        print("memory: row 156 already present")
        return
    start = text.find("### Row 136 baby picture")
    end = text.find("### Row 155 baby picture", start)
    if start < 0 or end < 0:
        raise SystemExit("memory row 136/155 baby picture missing")
    baby = bump136_to_156(text[start:end])
    baby = baby.replace("### Row 136 baby picture", "### Row 156 baby picture", 1)
    text = text.replace("### Row 155 baby picture", baby + "### Row 155 baby picture", 1)
    mem_table = (
        "| 156 | Meta | Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion | "
        "[Row 68 → Row 136 Born–Oppenheimer meta prelude capstone reunion index](sources.md#row68-row136-born-oppenheimer-meta-prelude-capstone-reunion-index-row-156) · "
        "[preface row 156 skill checkpoint](../preface.md#skill-navigation-row-156) · "
        "[prologue row 156 preview](../prologue/00-many-scales.md#prologue-preview-row-156) · "
        "[prologue row 156 closing stitch](../prologue/00-many-scales.md#row-156-closing-stitch) · "
        "[epilogue row 156 closing loop](../epilogue/multiscale.md#row-156-closing-loop) | "
        "Row 68 closed but row 56 IX.0 → IX.1 opening hinge feels disconnected from verified electronic audit meta prelude capstone on the capstone path — "
        "read row 68 + row 155 or row 136 gate + IX.0 Bridge → opening hinge → IX.1 BO/HK + row 56; "
        "[row 156 baby picture](#row-156-baby-picture-row68-row136-born-oppenheimer-meta-prelude-capstone-reunion) |\n"
    )
    text = text.replace(
        "| 155 | Meta | Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone reunion |",
        mem_table + "| 155 | Meta | Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone reunion |",
    )
    if "When row 155 closed but Born–Oppenheimer meta prelude capstone reunion still lags" not in text:
        text = text.replace(
            "When row 154 closed but electronic audit meta reunion still lags on the capstone path, switch to [row 155](#row-155-baby-picture-row68-row135-electronic-audit-meta-prelude-capstone-reunion).",
            "When row 154 closed but electronic audit meta reunion still lags on the capstone path, switch to [row 155](#row-155-baby-picture-row68-row135-electronic-audit-meta-prelude-capstone-reunion). "
            "When row 155 closed but Born–Oppenheimer meta prelude capstone reunion still lags on the capstone path, switch to [row 156](#row-156-baby-picture-row68-row136-born-oppenheimer-meta-prelude-capstone-reunion).",
        )
    MEMORY.write_text(text)
    print("memory: added row 156")


def main() -> None:
    fix_preface()
    fix_prologue_compass()
    fix_epilogue_loop()
    add_sources_table_row()
    add_memory()


if __name__ == "__main__":
    main()
