#!/usr/bin/env python3
"""Add row 156 (Row 68 → Row 136 ↔ Row 56 Born–Oppenheimer meta prelude capstone reunion)."""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def tx(s: str, pairs: list[tuple[str, str]]) -> str:
    for a, b in pairs:
        s = s.replace(a, b)
    return s


def extract_between(text: str, start: str, end: str) -> str:
    i = text.find(start)
    if i < 0:
        raise SystemExit(f"start marker not found: {start[:80]}")
    j = text.find(end, i + len(start))
    if j < 0:
        raise SystemExit(f"end marker not found after {start[:40]}")
    return text[i:j]


def lift_136_to_156(s: str) -> str:
    p = [
        ("__R137__", "[row 137]"),
        ("__R157__", "[row 157]"),
        ("[row 137]", "__R137__"),
        ("[row 157]", "__R157__"),
        ("skill-navigation-row-136", "skill-navigation-row-156"),
        ("### Row 136 skill checkpoint", "### Row 156 skill checkpoint"),
        ("Row 136 does not replace", "Row 156 does not replace"),
        ("Row 136 three-way audit", "Row 156 three-way audit"),
        ("Row 136 closing loop", "Row 156 closing loop"),
        ("row-136-closing-loop", "row-156-closing-loop"),
        ("Row 136 closing stitch", "Row 156 closing stitch"),
        ("row-136-closing-stitch", "row-156-closing-stitch"),
        ("prologue-preview-row-136", "prologue-preview-row-156"),
        ("Row 136 preview", "Row 156 preview"),
        ("Row 136 skill checkpoint", "Row 156 skill checkpoint"),
        ("memory sheet row 136", "memory sheet row 156"),
        ("Row 136 baby picture", "Row 156 baby picture"),
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
        ("Born–Oppenheimer meta capstone", "Born–Oppenheimer meta prelude capstone"),
        ("before Born–Oppenheimer meta capstone", "before Born–Oppenheimer meta prelude capstone"),
        ("before the Murnaghan Lab act", "before the Kohn–Sham meta prelude capstone reunion"),
        ("before the Kohn–Sham meta reunion", "before the Kohn–Sham meta prelude capstone reunion"),
        ("[row 116]", "__R116__"),
        ("[row 136]", "__R136OLD__"),
        ("[row 135]", "[row 155]"),
        ("row 135", "row 155"),
        ("Row 135", "Row 155"),
        ("__R116__", "[row 136]"),
        ("__R136OLD__", "[row 136]"),
        (
            "Row 68 → Row 116 Born–Oppenheimer meta capstone reunion index (row 136)",
            "Row 68 → Row 136 Born–Oppenheimer meta prelude capstone reunion index (row 156)",
        ),
        (
            "Row 68 → Row 116 Born–Oppenheimer meta prelude capstone reunion index",
            "Row 68 → Row 136 Born–Oppenheimer meta prelude capstone reunion index",
        ),
        (
            "verified electronic audit meta prelude capstone closure (row 135)",
            "verified electronic audit meta prelude capstone closure (row 155)",
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
            "When row 56 feels like quantum chemistry homework after row 135 alone on the capstone path",
            "When row 56 feels like quantum chemistry homework after row 155 alone on the capstone path",
        ),
        (
            "row 136 (row 68 ↔ row 56 reunion on the capstone path) with row 116",
            "row 156 (row 68 ↔ row 56 reunion on the capstone path) with row 136",
        ),
        (
            "Row 68 → Row 116 reunion index",
            "Row 68 → Row 136 reunion index",
        ),
        (
            "Proceed to [row 137](#row-136-closing-loop) when row 68 closed but Kohn–Sham meta capstone still lags after row 136 on the capstone path",
            "Proceed to [row 157](#row-156-closing-loop) when row 68 closed but Kohn–Sham meta prelude capstone still lags after row 156 on the capstone path, "
            "to [row 137](#row-137-closing-loop) when row 68 closed but Kohn–Sham meta capstone still lags on the opening-hinge path",
        ),
        ("Recite [preface row 135]", "Recite [preface row 155]"),
        ("[row 115](preface.md#skill-navigation-row-115)", "[row 155](preface.md#skill-navigation-row-155)"),
        (
            "[Row 68 → Row 96 Born–Oppenheimer meta capstone reunion index (row 116)](appendix/sources.md#row68-row96-born-oppenheimer-meta-capstone-reunion-index-row-116)",
            "[Row 68 → Row 116 Born–Oppenheimer meta capstone reunion index (row 136)](appendix/sources.md#row68-row116-born-oppenheimer-meta-capstone-reunion-index-row-136)",
        ),
        ("Born–Oppenheimer meta capstone reunion audit", "Born–Oppenheimer meta prelude capstone reunion audit"),
        ("__R137__", "[row 137]"),
        ("__R157__", "[row 157]"),
    ]
    return tx(s, p)


def insert_preface_row() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    if "skill-navigation-row-156" in text and "### Row 156 skill checkpoint" in text:
        print("preface: row 156 already present")
        return
    m = re.search(
        r"(### Row 136 skill checkpoint.*?)(?=\n### Row 137 skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 136 checkpoint missing")
    block = lift_136_to_156(m.group(1))
    anchor = "\n## The copper wire through the book"
    idx = text.find(anchor)
    if idx < 0:
        raise SystemExit("copper wire anchor missing")
    text = text[:idx] + "\n" + block + text[idx:]
    path.write_text(text)
    print("preface: added row 156")


def insert_epilogue_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "row-156-closing-loop" in text:
        print("epilogue: row 156 loop already present")
        return
    block = lift_136_to_156(
        extract_between(text, "### Row 136 closing loop", "### Row 155 closing loop")
    )
    text = text.replace("### Row 155 closing loop", block + "### Row 155 closing loop", 1)
    path.write_text(text)
    print("epilogue: added row 156 loop")


def add_prologue() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    line155 = (
        "| Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone reunion (row 155) |"
    )
    compass156 = (
        "| Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion (row 156) |"
        " [Preface: row 156 skill checkpoint](../preface.md#skill-navigation-row-156) · "
        "[Row 68 → Row 136 Born–Oppenheimer meta prelude capstone reunion index]"
        "(../appendix/sources.md#row68-row136-born-oppenheimer-meta-prelude-capstone-reunion-index-row-156) · "
        "[memory sheet row 156 baby picture](../appendix/memory-sheet.md#row-156-baby-picture-row68-row136-born-oppenheimer-meta-prelude-capstone-reunion) · "
        "[prologue row 156 preview row](#prologue-preview-row-156); [prologue row 156 closing stitch](#row-156-closing-stitch); "
        "[epilogue row 156 closing loop](../epilogue/multiscale.md#row-156-closing-loop) — "
        "read row 68 gate + row 155 or row 136 electronic audit meta prelude capstone / Born–Oppenheimer opening gate + "
        "IX.0 Bridge → opening hinge → IX.1 BO/HK + row 56 meta aloud when foundation SCF logs are clean on the capstone path "
        "but Born–Oppenheimer still feels like standalone quantum chemistry after verified electronic audit meta prelude capstone |"
    )
    if "row 156)" not in text:
        idx = text.find(line155)
        if idx < 0:
            raise SystemExit("prologue compass row 155 not found")
        line_end = text.find("\n", idx)
        src_line = text[idx:line_end]
        new_line = lift_136_to_156(src_line.replace("Row 135", "Row 156").replace("row 155", "row 156").replace("Row 55", "Row 56").replace("row 55", "row 56").replace("electronic audit", "Born–Oppenheimer meta prelude").replace("export meta prelude capstone / electronic audit meta prelude gate + VIII.3 Bridge → opening hinge → IX.0 SCF audit", "electronic audit meta prelude capstone / Born–Oppenheimer opening gate + IX.0 Bridge → opening hinge → IX.1 BO/HK"))
        if "Born–Oppenheimer meta prelude capstone reunion (row 156)" not in text:
            text = text[: line_end + 1] + new_line + "\n" + text[line_end + 1 :]
        print("prologue: compass row 156")
    preview_src = '| <span id="prologue-preview-row-136"></span>'
    preview_dst = '| <span id="prologue-preview-row-156"></span>'
    if preview_dst not in text and preview_src in text:
        i = text.find(preview_src)
        j = text.find("\n|", i + 1)
        preview_block = lift_136_to_156(text[i:j])
        text = text.replace(preview_src, preview_block + preview_src, 1)
        print("prologue: preview row 156")
    if "row-156-closing-stitch" not in text:
        stitch = (
            "**Row 155 closing stitch (Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone reunion).** {#row-156-closing-stitch} "
            "When row 155 closed — electronic audit meta prelude capstone verified, row 154 or row 135 recited on the capstone path, and VIII.3 Bridge → IX.0 SCF recited with "
            "[foundation SCF audit Lab act](../part09-dft/00-opening.md#lab-act-foundation-scf-audit-before-born-oppenheimer-act-vi--foundation) archived `cu.relax.out` — but **row 56 IX.0 → IX.1 opening hinge still opens like standalone quantum chemistry homework after the electronic audit Scene on the capstone path** — "
            "the [preface row 156 When-to-pause opening sentence](../preface.md#skill-navigation-row-156) names the dual reunion before Kohn–Sham meta prelude capstone reunion; "
            "read [preface row 156](../preface.md#skill-navigation-row-156), then the "
            "[Row 68 → Row 136 reunion index](../appendix/sources.md#row68-row136-born-oppenheimer-meta-prelude-capstone-reunion-index-row-156), then "
            "[epilogue row 156 closing loop](../epilogue/multiscale.md#row-156-closing-loop) before row 57 Kohn–Sham meta prelude opens on the capstone path.\n\n"
        )
        text = text.replace("**Row 155 closing stitch", stitch + "**Row 155 closing stitch", 1)
        print("prologue: stitch row 156")
    path.write_text(text)


def add_sources_table() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    idx_key = "row68-row136-born-oppenheimer-meta-prelude-capstone-reunion-index-row-156"
    if idx_key in text:
        print("sources: row 156 already present")
        return
    table_row = (
        "| 156 | Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone "
        "(midpoint prelude gate ↔ electronic audit meta prelude capstone ↔ row 56 meta) | "
        f"[Row 68 → Row 136 Born–Oppenheimer meta prelude capstone reunion index](#{idx_key}) · "
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
        table_row + "| 155 | Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone",
    )
    path.write_text(text)
    print("sources: added row 156 table")


def add_memory_row() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    if "row-156-baby-picture" in text:
        print("memory-sheet: row 156 already present")
        return
    baby = lift_136_to_156(
        extract_between(text, "### Row 136 baby picture", "### Row 137 baby picture")
    )
    needle = "### Row 136 baby picture"
    text = text.replace(needle, baby + needle, 1)
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
    if "When row 155 closed but Born–Oppenheimer meta reunion still lags" not in text:
        text = text.replace(
            "When row 154 closed but electronic audit meta reunion still lags on the capstone path, switch to [row 155](#row-155-baby-picture-row68-row135-electronic-audit-meta-prelude-capstone-reunion).",
            "When row 154 closed but electronic audit meta reunion still lags on the capstone path, switch to [row 155](#row-155-baby-picture-row68-row135-electronic-audit-meta-prelude-capstone-reunion). "
            "When row 155 closed but Born–Oppenheimer meta reunion still lags on the capstone path, switch to [row 156](#row-156-baby-picture-row68-row136-born-oppenheimer-meta-prelude-capstone-reunion).",
        )
    path.write_text(text)
    print("memory-sheet: added row 156")


def patch_row_155_proceed() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    bad = (
        "When row 136 is complete, proceed to [row 137](preface.md#skill-navigation-row-137) when Born–Oppenheimer meta capstone is clean but Kohn–Sham meta capstone still lags after verified Murnaghan archive on the capstone path, to [row 117](preface.md#skill-navigation-row-117) when Born–Oppenheimer meta capstone is clean but Kohn–Sham meta capstone still lags on the opening-hinge path, to [row 97](preface.md#skill-navigation-row-117) for the Row 68 ↔ Row 57 Kohn–Sham opening prelude audit alone, to [row 136](preface.md#skill-navigation-row-136) when electronic audit meta prelude capstone still lags after verified foundation SCF on the capstone path, to [row 57](preface.md#skill-navigation-row-57) when only IX.1 → IX.2 stalls, or extend prose only under `writings/` then sync."
    )
    good = (
        "When row 155 is complete, proceed to [row 156](preface.md#skill-navigation-row-156) when electronic audit meta prelude capstone is clean but Born–Oppenheimer meta prelude capstone still lags after verified foundation SCF archive on the capstone path, to [row 136](preface.md#skill-navigation-row-136) when electronic audit meta capstone is clean but Born–Oppenheimer meta capstone still lags on the opening-hinge path, to [row 96](preface.md#skill-navigation-row-96) for the Row 68 ↔ Row 56 Born–Oppenheimer opening prelude audit alone, to [row 155](preface.md#skill-navigation-row-155) when export meta prelude capstone still lags after verified pedigree checklist on the capstone path, to [row 56](preface.md#skill-navigation-row-56) when only IX.0 → IX.1 stalls, or extend prose only under `writings/` then sync."
    )
    if bad in text:
        text = text.replace(bad, good)
        path.write_text(text)
        print("preface: patched row 155 proceed links")


def main() -> None:
    insert_preface_row()
    insert_epilogue_loop()
    add_prologue()
    add_sources_table()
    add_memory_row()
    patch_row_155_proceed()
    fix = ROOT / "scripts/fix-row-156-content.py"
    if fix.is_file():
        subprocess.check_call([sys.executable, str(fix)])


if __name__ == "__main__":
    main()
