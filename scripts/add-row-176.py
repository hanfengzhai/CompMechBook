#!/usr/bin/env python3
"""Add row 176 (Row 68 → Row 151 ↔ Row 56 Born–Oppenheimer meta prelude capstone on capstone path)."""
from __future__ import annotations

import re
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


LIFT_156_TO_176_PAIRS: list[tuple[str, str]] = [
    ("Row 157 closing loop", "__PH157_LOOP__"),
    ("Row 156 closing loop", "Row 176 closing loop"),
    ("row-157-closing-loop", "__PH157_LOOP_ANCHOR__"),
    ("row-156-closing-loop", "row-176-closing-loop"),
    ("Row 157 closing stitch", "__PH157_STITCH__"),
    ("Row 156 closing stitch", "Row 176 closing stitch"),
    ("row-157-closing-stitch", "__PH157_STITCH_ANCHOR__"),
    ("row-156-closing-stitch", "row-176-closing-stitch"),
    ("prologue-preview-row-157", "__PH157_PREVIEW__"),
    ("prologue-preview-row-156", "prologue-preview-row-176"),
    ("Row 157 preview", "__PH157_PREVIEW_TEXT__"),
    ("Row 156 preview", "Row 176 preview"),
    ("Row 157 skill checkpoint", "__PH157_SKILL__"),
    ("Row 156 skill checkpoint", "Row 176 skill checkpoint"),
    ("skill-navigation-row-157", "__PH157_SKILL_NAV__"),
    ("skill-navigation-row-156", "skill-navigation-row-176"),
    ("memory sheet row 157", "__PH157_MEM__"),
    ("memory sheet row 156", "memory sheet row 176"),
    ("Row 157 baby picture", "__PH157_BABY__"),
    ("Row 156 baby picture", "Row 176 baby picture"),
    ("Row 157 three-way audit", "__PH157_AUDIT__"),
    ("Row 156 three-way audit", "Row 176 three-way audit"),
    (
        "Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone",
        "Row 68 → Row 151 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone",
    ),
    (
        "row68-row136-born-oppenheimer-meta-prelude-capstone-reunion-index-row-156",
        "row68-row151-born-oppenheimer-meta-prelude-capstone-reunion-index-row-176",
    ),
    (
        "row-156-baby-picture-row68-row136-born-oppenheimer-meta-prelude-capstone-reunion",
        "row-176-baby-picture-row68-row151-born-oppenheimer-meta-prelude-capstone-reunion",
    ),
    ("[row 157]", "__ROW157_REF__"),
    ("[row 136]", "[row 156]"),
    ("row 136", "row 156"),
    ("Row 136", "Row 156"),
    ("__ROW157_REF__", "[row 157]"),
    ("[row 155]", "__ROW175_GATE__"),
    ("row 155", "__row175_gate__"),
    ("Row 155", "__ROW175_GATE_CAP__"),
    (
        "Row 68 → Row 136 Born–Oppenheimer meta prelude capstone reunion index (row 156)",
        "Row 68 → Row 151 Born–Oppenheimer meta prelude capstone reunion index (row 176)",
    ),
    (
        "row68-row116-born-oppenheimer-meta-capstone-reunion-index-row-136",
        "row68-row151-born-oppenheimer-meta-prelude-capstone-reunion-index-row-176",
    ),
    (
        "verified electronic audit meta prelude capstone closure (row 155)",
        "verified electronic audit meta prelude capstone closure (row 175)",
    ),
    ("when row 155 closed but row 56", "when row 175 closed but row 56"),
    ("after row 155.", "after row 175."),
    ("when row 155 and row 56", "when row 175 and row 56"),
    (
        "rear-view mirror of row 155's foundation SCF → BO vocabulary turn",
        "rear-view mirror of row 175's foundation SCF → BO vocabulary turn",
    ),
    (
        "when opening [row 157](preface.md#skill-navigation-row-157) before row 57 closes on the capstone path",
        "when opening [row 176](preface.md#skill-navigation-row-176) before row 57 closes on the capstone path",
    ),
    (
        "When row 156 is complete, proceed to [row 157]",
        "When row 176 is complete, proceed to [row 157]",
    ),
    (
        "Proceed to [row 157](#row-157-closing-loop) when row 68 closed but Kohn–Sham meta prelude capstone still lags after row 156 on the capstone path",
        "Proceed to [row 176](#row-176-closing-loop) when row 68 closed but Born–Oppenheimer meta prelude capstone still lags after row 175 on the capstone path, "
        "to [row 156](#row-156-closing-loop) when row 68 closed but Born–Oppenheimer meta prelude still lags on the opening-hinge path",
    ),
    (
        "When row 56 feels like quantum chemistry homework after row 155 alone on the capstone path",
        "When row 56 feels like quantum chemistry homework after row 175 alone on the capstone path",
    ),
    (
        "row 156 (row 68 ↔ row 56 reunion on the capstone path) with row 136",
        "row 176 (row 68 ↔ row 56 reunion on the capstone path) with row 156",
    ),
    (
        "row 156 names **why that reunion must follow verified electronic audit meta prelude capstone (row 155)",
        "row 176 names **why that reunion must follow verified electronic audit meta prelude capstone (row 175)",
    ),
    ("Row 68 → Row 56 meta (row 136)", "Row 68 → Row 56 meta (row 156)"),
    (
        "Row 68 → Row 136 Born–Oppenheimer meta prelude capstone reunion index (row 156)",
        "Row 68 → Row 151 Born–Oppenheimer meta prelude capstone reunion index (row 176)",
    ),
    ("Row 68 → Row 136 reunion index", "Row 68 → Row 151 reunion index"),
    ("(row 156)", "(row 176)"),
    ("Row 156 closes the", "Row 176 closes the"),
    ("Row 156 does not conflate", "Row 176 does not conflate"),
    ("Row 156 does not replace", "Row 176 does not replace"),
    ("__PH157_LOOP__", "Row 157 closing loop"),
    ("__PH157_LOOP_ANCHOR__", "row-157-closing-loop"),
    ("__PH157_STITCH__", "Row 157 closing stitch"),
    ("__PH157_STITCH_ANCHOR__", "row-157-closing-stitch"),
    ("__PH157_PREVIEW__", "prologue-preview-row-157"),
    ("__PH157_PREVIEW_TEXT__", "Row 157 preview"),
    ("__PH157_SKILL__", "Row 157 skill checkpoint"),
    ("__PH157_SKILL_NAV__", "skill-navigation-row-157"),
    ("__PH157_MEM__", "memory sheet row 157"),
    ("__PH157_BABY__", "Row 157 baby picture"),
    ("__PH157_AUDIT__", "Row 157 three-way audit"),
    ("__ROW175_GATE__", "[row 175]"),
    ("__row175_gate__", "row 175"),
    ("__ROW175_GATE_CAP__", "Row 175"),
]


def lift_156_to_176(s: str) -> str:
    out = tx(s, LIFT_156_TO_176_PAIRS)
    out = out.replace(
        "[row 175](preface.md#skill-navigation-row-155)",
        "[row 175](preface.md#skill-navigation-row-175)",
    )
    out = out.replace(
        "[row 156](preface.md#skill-navigation-row-136)",
        "[row 156](preface.md#skill-navigation-row-156)",
    )
    out = re.sub(
        r"(### Row 176 skill checkpoint[^\n]*)\{#skill-navigation-row-156\}",
        r"\1{#skill-navigation-row-176}",
        out,
        count=1,
    )
    return out


def export_index_to_born_oppenheimer_176(block: str) -> str:
    """Turn a lifted electronic-audit capstone index (175-shaped) into Born–Oppenheimer capstone 176."""
    pairs = [
        (
            "electronic audit meta prelude capstone reunion index (row 175)",
            "Born–Oppenheimer meta prelude capstone reunion index (row 176)",
        ),
        (
            "electronic audit meta prelude capstone reunion index (row 176)",
            "Born–Oppenheimer meta prelude capstone reunion index (row 176)",
        ),
        ("Row 68 → Row 55", "Row 68 → Row 56"),
        ("row 55", "row 56"),
        ("export meta prelude capstone", "electronic audit meta prelude capstone"),
        ("row 174", "row 175"),
        (
            "row68-row151-export-meta-prelude-capstone-reunion-index-row-174",
            "row68-row151-electronic-audit-meta-prelude-capstone-reunion-index-row-175",
        ),
        ("VIII.3 Bridge to Part IX", "IX.0 Bridge"),
        (
            "IX.0 opening hinge from VIII.3",
            "IX.1 opening hinge from IX.0",
        ),
        ("IX.0 foundation SCF audit", "IX.1 BO/HK vocabulary audit"),
        (
            "viii3-ix0-opening-hinge-reunion-index-row-55",
            "ix0-ix1-opening-hinge-reunion-index-row-56",
        ),
        ("EAM-fit audit Lab act steps 1–6", "foundation SCF audit Lab act steps 1–6"),
        ("`pedigree_checklist.yaml`", "`cu.relax.out`"),
        ("DFT homework", "quantum chemistry homework"),
        ("pedigree → foundation SCF", "foundation SCF → BO/HK"),
        (
            "electronic audit meta prelude capstone reunion",
            "Born–Oppenheimer meta prelude capstone reunion",
        ),
        ("skill-navigation-row-175", "skill-navigation-row-176"),
        ("row-175-baby-picture", "row-176-baby-picture"),
        ("Row 175", "Row 176"),
        ("row 175", "row 176"),
        ("row 55 electronic audit meta prelude", "row 56 Born–Oppenheimer meta prelude"),
        ("row 56 Born–Oppenheimer meta prelude", "row 57 Kohn–Sham meta prelude"),
        ("electronic audit meta prelude capstone", "Born–Oppenheimer meta prelude capstone"),
        ("VIII.3 → IX.0", "IX.0 → IX.1"),
        ("export meta prelude capstone boundary", "electronic audit meta prelude capstone boundary"),
    ]
    return tx(block, pairs)


def insert_preface_row() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    if "### Row 176 skill checkpoint" in text:
        print("preface: row 176 already present")
        return
    m = re.search(
        r"(### Row 156 skill checkpoint.*?)(?=\n### Row 157 skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 156 checkpoint missing")
    block = lift_156_to_176(m.group(1))
    anchor = "\n## The copper wire through the book"
    idx = text.find(anchor)
    if idx < 0:
        raise SystemExit("copper wire anchor missing")
    text = text[:idx] + "\n" + block + text[idx:]
    path.write_text(text)
    print("preface: added row 176")


def insert_epilogue_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "### Row 176 closing loop" in text:
        print("epilogue: row 176 loop already present")
        return
    block = lift_156_to_176(
        extract_between(
            text,
            "### Row 156 closing loop",
            "### Row 155 closing loop",
        )
    )
    needle = "### Row 175 closing loop"
    text = text.replace(needle, block + needle, 1)
    path.write_text(text)
    print("epilogue: added row 176 loop")


def add_prologue_compass() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    compass = "| Row 68 → Row 151 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion (row 176) |"
    if compass in text:
        print("prologue: row 176 compass already present")
    else:
        after = "| Row 68 → Row 151 Row 68 → Row 55 electronic audit meta prelude capstone reunion (row 175) |"
        idx = text.find(after)
        if idx < 0:
            raise SystemExit("prologue row 175 compass missing")
        line_end = text.find("\n", idx)
        src = "| Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion (row 156) |"
        sidx = text.find(src)
        if sidx < 0:
            raise SystemExit("prologue row 156 compass missing")
        new_line = lift_156_to_176(text[sidx : text.find("\n", sidx)]) + "\n"
        text = text[: line_end + 1] + new_line + text[line_end + 1 :]
    preview_src = '| <span id="prologue-preview-row-156"></span>'
    preview_dst = '| <span id="prologue-preview-row-176"></span>'
    if preview_src in text and preview_dst not in text:
        i = text.find(preview_src)
        j = text.find("\n|", i + 1)
        preview_block = lift_156_to_176(text[i:j]) + "\n"
        text = text.replace(preview_src, preview_block + preview_src, 1)
    if "**Row 176 closing stitch" not in text:
        stitch = (
            "**Row 176 closing stitch (Row 68 → Row 151 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion).** {#row-176-closing-stitch} "
            "When row 175 closed — electronic audit meta prelude capstone verified, row 175 or row 155 recited on the capstone path, and IX.0 Bridge → IX.1 BO/HK recited with "
            "[foundation SCF audit Lab act](../part09-dft/00-opening.md#lab-act-foundation-scf-audit-before-born-oppenheimer-act-vi--foundation) archived `cu.relax.out` — but **row 56 IX.0 → IX.1 opening hinge still opens like standalone quantum chemistry homework after the electronic audit Scene on the capstone path** — "
            "the [preface row 176 When-to-pause opening sentence](../preface.md#skill-navigation-row-176) names the dual reunion before the Kohn–Sham meta prelude capstone reunion; "
            "read [preface row 176](../preface.md#skill-navigation-row-176), then the "
            "[Row 68 → Row 151 Born–Oppenheimer reunion index](../appendix/sources.md#row68-row151-born-oppenheimer-meta-prelude-capstone-reunion-index-row-176), then "
            "[epilogue row 176 closing loop](../epilogue/multiscale.md#row-176-closing-loop) before row 57 Kohn–Sham meta prelude opens on the capstone path.\n\n"
        )
        text = text.replace("**Row 175 closing stitch", stitch + "**Row 175 closing stitch", 1)
    path.write_text(text)
    print("prologue: row 176 compass/preview/stitch")


def add_sources_row() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    idx_key = "row68-row151-born-oppenheimer-meta-prelude-capstone-reunion-index-row-176"
    if idx_key in text:
        print("sources: row 176 already present")
        return
    start175 = "## Row 68 → Row 151 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 175)"
    i = text.find(start175)
    if i < 0:
        raise SystemExit("sources row 175 index missing")
    end174 = "## Row 68 → Row 151 Row 68 → Row 54 export meta prelude capstone reunion index (row 174)"
    j174 = text.find(end174, i)
    if j174 < 0:
        j174 = text.find("\n## Row 68 → Row 132", i)
    if j174 < 0:
        raise SystemExit("sources row 174 index missing after 175")
    block = export_index_to_born_oppenheimer_176(lift_156_to_176(text[i:j174]))
    block = block.replace(
        "## Row 68 → Row 151 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion index (row 176)",
        f"## Row 68 → Row 151 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion index (row 176) {{#{idx_key}}}",
        1,
    )
    table_row = (
        "| 176 | Row 68 → Row 151 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone (midpoint prelude gate ↔ electronic audit meta prelude capstone ↔ row 56 meta) | "
        f"[Row 68 → Row 151 Born–Oppenheimer meta prelude capstone reunion index](#{idx_key}) · "
        "[preface row 176](../preface.md#skill-navigation-row-176) · "
        "[prologue row 176 preview](../prologue/00-many-scales.md#prologue-preview-row-176) · "
        "[prologue row 176 closing stitch](../prologue/00-many-scales.md#row-176-closing-stitch) · "
        "[epilogue row 176 closing loop](../epilogue/multiscale.md#row-176-closing-loop) · "
        "[memory sheet row 176 baby picture](memory-sheet.md#row-176-baby-picture-row68-row151-born-oppenheimer-meta-prelude-capstone-reunion) | "
        "Row 68 closed but **row 56 IX.0 → IX.1 opening hinge still feels disconnected from verified electronic audit meta prelude capstone on the capstone path** — "
        "read row 68 + row 175 or row 156 gate + IX.0 Bridge → opening hinge → IX.1 BO/HK + row 56; "
        "[preface row 56](../preface.md#skill-navigation-row-56) |\n"
    )
    text = text.replace(
        "| 175 | Row 68 → Row 151 Row 68 → Row 55 electronic audit meta prelude capstone",
        table_row + "| 175 | Row 68 → Row 151 Row 68 → Row 55 electronic audit meta prelude capstone",
    )
    text = text.replace(start175, block + start175, 1)
    extra = (
        f"[row 176](#{idx_key}) reunites **electronic audit meta prelude capstone with the Born–Oppenheimer meta prelude capstone boundary** "
        "when row 175 closed electronic audit meta prelude capstone at verified VIII.3 → IX.0 closure on the capstone path but IX.0 Bridge and row 56 still read like separate courses;"
    )
    needle = (
        "[row 175](#row68-row151-electronic-audit-meta-prelude-capstone-reunion-index-row-175) reunites **export meta prelude capstone with the electronic audit meta prelude capstone boundary** "
    )
    if extra not in text and needle in text:
        text = text.replace(needle, needle + " " + extra)
    path.write_text(text)
    print("sources: added row 176")


def add_memory_row() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    if "row-176-baby-picture-row68-row151-born-oppenheimer-meta-prelude-capstone-reunion" in text:
        print("memory-sheet: row 176 already present")
        return
    baby = lift_156_to_176(
        extract_between(
            text,
            "### Row 156 baby picture",
            "### Row 137 baby picture",
        )
    )
    anchor = "### Row 156 baby picture"
    text = text.replace(anchor, baby + anchor, 1)
    mem_table = (
        "| 176 | Meta | Row 68 → Row 151 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion | "
        "[Row 68 → Row 151 Born–Oppenheimer meta prelude capstone reunion index](sources.md#row68-row151-born-oppenheimer-meta-prelude-capstone-reunion-index-row-176) · "
        "[preface row 176 skill checkpoint](../preface.md#skill-navigation-row-176) · "
        "[prologue row 176 preview](../prologue/00-many-scales.md#prologue-preview-row-176) · "
        "[prologue row 176 closing stitch](../prologue/00-many-scales.md#row-176-closing-stitch) · "
        "[epilogue row 176 closing loop](../epilogue/multiscale.md#row-176-closing-loop) | "
        "Row 68 closed but row 56 IX.0 → IX.1 opening hinge feels disconnected from verified electronic audit meta prelude capstone on the capstone path — "
        "read row 68 + row 175 or row 156 gate + IX.0 Bridge → opening hinge → IX.1 BO/HK + row 56; "
        "[row 176 baby picture](#row-176-baby-picture-row68-row151-born-oppenheimer-meta-prelude-capstone-reunion) |\n"
    )
    text = text.replace(
        "| 175 | Meta | Row 68 → Row 151 Row 68 → Row 55 electronic audit meta prelude capstone reunion |",
        mem_table + "| 175 | Meta | Row 68 → Row 151 Row 68 → Row 55 electronic audit meta prelude capstone reunion |",
    )
    if "When row 175 closed but Born–Oppenheimer meta reunion still lags" not in text:
        text = text.replace(
            "When row 174 closed but electronic audit meta reunion still lags on the capstone path, switch to [row 175](#row-175-baby-picture-row68-row151-electronic-audit-meta-prelude-capstone-reunion).",
            "When row 174 closed but electronic audit meta reunion still lags on the capstone path, switch to [row 175](#row-175-baby-picture-row68-row151-electronic-audit-meta-prelude-capstone-reunion). "
            "When row 175 closed but Born–Oppenheimer meta reunion still lags on the capstone path, switch to [row 176](#row-176-baby-picture-row68-row151-born-oppenheimer-meta-prelude-capstone-reunion).",
        )
    path.write_text(text)
    print("memory-sheet: added row 176")


def patch_row_175_proceed_links() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    text = text.replace(
        "proceed to [row 176](preface.md#skill-navigation-row-156)",
        "proceed to [row 176](preface.md#skill-navigation-row-176)",
    )
    path.write_text(text)
    ep = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep_text = ep.read_text()
    ep_text = ep_text.replace(
        "proceed to [row 176](preface.md#skill-navigation-row-156)",
        "proceed to [row 176](preface.md#skill-navigation-row-176)",
    )
    ep.write_text(ep_text)
    print("preface/epilogue: patched row 175 → row 176 proceed links")


def main() -> None:
    insert_preface_row()
    insert_epilogue_loop()
    add_prologue_compass()
    add_sources_row()
    add_memory_row()
    patch_row_175_proceed_links()


if __name__ == "__main__":
    main()
