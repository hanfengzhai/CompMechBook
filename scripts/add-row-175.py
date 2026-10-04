#!/usr/bin/env python3
"""Add row 175 (Row 68 → Row 151 ↔ Row 55 electronic audit meta prelude capstone on capstone path)."""
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


LIFT_155_TO_175_PAIRS: list[tuple[str, str]] = [
    ("Row 156 closing loop", "__PH156_LOOP__"),
    ("Row 155 closing loop", "Row 175 closing loop"),
    ("row-156-closing-loop", "__PH156_LOOP_ANCHOR__"),
    ("row-155-closing-loop", "row-175-closing-loop"),
    ("Row 156 closing stitch", "__PH156_STITCH__"),
    ("Row 155 closing stitch", "Row 175 closing stitch"),
    ("row-156-closing-stitch", "__PH156_STITCH_ANCHOR__"),
    ("row-155-closing-stitch", "row-175-closing-stitch"),
    ("prologue-preview-row-156", "__PH156_PREVIEW__"),
    ("prologue-preview-row-155", "prologue-preview-row-175"),
    ("Row 156 preview", "__PH156_PREVIEW_TEXT__"),
    ("Row 155 preview", "Row 175 preview"),
    ("Row 156 skill checkpoint", "__PH156_SKILL__"),
    ("Row 155 skill checkpoint", "Row 175 skill checkpoint"),
    ("skill-navigation-row-156", "__PH156_SKILL_NAV__"),
    ("skill-navigation-row-155", "skill-navigation-row-175"),
    ("memory sheet row 156", "__PH156_MEM__"),
    ("memory sheet row 155", "memory sheet row 175"),
    ("Row 156 baby picture", "__PH156_BABY__"),
    ("Row 155 baby picture", "Row 175 baby picture"),
    ("Row 156 three-way audit", "__PH156_AUDIT__"),
    ("Row 155 three-way audit", "Row 175 three-way audit"),
    (
        "Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone",
        "Row 68 → Row 151 Row 68 → Row 55 electronic audit meta prelude capstone",
    ),
    (
        "row68-row135-electronic-audit-meta-prelude-capstone-reunion-index-row-155",
        "row68-row151-electronic-audit-meta-prelude-capstone-reunion-index-row-175",
    ),
    (
        "row-155-baby-picture-row68-row135-electronic-audit-meta-prelude-capstone-reunion",
        "row-175-baby-picture-row68-row151-electronic-audit-meta-prelude-capstone-reunion",
    ),
    ("[row 156]", "__ROW156_REF__"),
    ("[row 135]", "[row 155]"),
    ("row 135", "row 155"),
    ("Row 135", "Row 155"),
    ("__ROW156_REF__", "[row 156]"),
    ("[row 154]", "__ROW174_GATE__"),
    ("row 154", "__row174_gate__"),
    ("Row 154", "__ROW174_GATE_CAP__"),
    (
        "Row 68 → Row 135 electronic audit meta prelude capstone reunion index (row 155)",
        "Row 68 → Row 151 electronic audit meta prelude capstone reunion index (row 175)",
    ),
    (
        "row68-row115-electronic-audit-meta-prelude-capstone-reunion-index-row-135",
        "row68-row151-electronic-audit-meta-prelude-capstone-reunion-index-row-175",
    ),
    (
        "verified export meta prelude capstone closure (row 154)",
        "verified export meta prelude capstone closure (row 174)",
    ),
    ("when row 154 closed but row 55", "when row 174 closed but row 55"),
    ("after row 154.", "after row 174."),
    ("when row 154 and row 55", "when row 174 and row 55"),
    (
        "rear-view mirror of row 154's pedigree checklist → IX.0 SCF audit turn",
        "rear-view mirror of row 174's pedigree checklist → IX.0 SCF audit turn",
    ),
    (
        "when opening [row 156](preface.md#skill-navigation-row-156) before row 56 closes on the capstone path",
        "when opening [row 175](preface.md#skill-navigation-row-175) before row 56 closes on the capstone path",
    ),
    (
        "When row 155 is complete, proceed to [row 156]",
        "When row 175 is complete, proceed to [row 156]",
    ),
    (
        "Proceed to [row 156](#row-156-closing-loop) when row 68 closed but Born–Oppenheimer meta prelude capstone still lags after row 155 on the capstone path",
        "Proceed to [row 175](#row-175-closing-loop) when row 68 closed but electronic audit meta prelude capstone still lags after row 174 on the capstone path, "
        "to [row 155](#row-155-closing-loop) when row 68 closed but electronic audit meta prelude still lags on the opening-hinge path",
    ),
    (
        "When row 55 feels like DFT homework after row 154 alone on the capstone path",
        "When row 55 feels like DFT homework after row 174 alone on the capstone path",
    ),
    (
        "row 155 (row 68 ↔ row 55 reunion on the capstone path) with row 135",
        "row 175 (row 68 ↔ row 55 reunion on the capstone path) with row 155",
    ),
    (
        "row 155 names **why that reunion must follow verified export meta prelude capstone (row 154)",
        "row 175 names **why that reunion must follow verified export meta prelude capstone (row 174)",
    ),
    ("Row 68 → Row 55 meta (row 135)", "Row 68 → Row 55 meta (row 155)"),
    (
        "Row 68 → Row 135 electronic audit meta prelude capstone reunion index (row 155)",
        "Row 68 → Row 151 electronic audit meta prelude capstone reunion index (row 175)",
    ),
    ("Row 68 → Row 135 reunion index", "Row 68 → Row 151 reunion index"),
    ("(row 155)", "(row 175)"),
    ("Row 155 closes the", "Row 175 closes the"),
    ("Row 155 does not conflate", "Row 175 does not conflate"),
    ("Row 155 does not replace", "Row 175 does not replace"),
    ("__PH156_LOOP__", "Row 156 closing loop"),
    ("__PH156_LOOP_ANCHOR__", "row-156-closing-loop"),
    ("__PH156_STITCH__", "Row 156 closing stitch"),
    ("__PH156_STITCH_ANCHOR__", "row-156-closing-stitch"),
    ("__PH156_PREVIEW__", "prologue-preview-row-156"),
    ("__PH156_PREVIEW_TEXT__", "Row 156 preview"),
    ("__PH156_SKILL__", "Row 156 skill checkpoint"),
    ("__PH156_SKILL_NAV__", "skill-navigation-row-156"),
    ("__PH156_MEM__", "memory sheet row 156"),
    ("__PH156_BABY__", "Row 156 baby picture"),
    ("__PH156_AUDIT__", "Row 156 three-way audit"),
    ("__ROW174_GATE__", "[row 174]"),
    ("__row174_gate__", "row 174"),
    ("__ROW174_GATE_CAP__", "Row 174"),
]


def lift_155_to_175(s: str) -> str:
    out = tx(s, LIFT_155_TO_175_PAIRS)
    out = out.replace(
        "[row 174](preface.md#skill-navigation-row-154)",
        "[row 174](preface.md#skill-navigation-row-174)",
    )
    out = out.replace(
        "[row 155](preface.md#skill-navigation-row-135)",
        "[row 155](preface.md#skill-navigation-row-155)",
    )
    out = re.sub(
        r"(### Row 175 skill checkpoint[^\n]*)\{#skill-navigation-row-155\}",
        r"\1{#skill-navigation-row-175}",
        out,
        count=1,
    )
    return out


def export_index_to_electronic_audit_175(block: str) -> str:
    """Turn a lifted export capstone index (174-shaped) into electronic audit capstone 175."""
    pairs = [
        (
            "export meta prelude capstone reunion index (row 174)",
            "electronic audit meta prelude capstone reunion index (row 175)",
        ),
        (
            "export meta prelude capstone reunion index (row 175)",
            "electronic audit meta prelude capstone reunion index (row 175)",
        ),
        ("Row 68 → Row 54", "Row 68 → Row 55"),
        ("row 54", "row 55"),
        ("dynamics meta prelude capstone", "export meta prelude capstone"),
        ("row 173", "row 174"),
        (
            "row68-row151-dynamics-meta-prelude-capstone-reunion-index-row-173",
            "row68-row151-export-meta-prelude-capstone-reunion-index-row-174",
        ),
        ("VIII.2 Bridge", "VIII.3 Bridge to Part IX"),
        (
            "VIII.3 opening hinge from VIII.2",
            "IX.0 opening hinge from VIII.3",
        ),
        ("VIII.3 pedigree checklist", "IX.0 foundation SCF audit"),
        (
            "viii2-viii3-opening-hinge-reunion-index-row-54",
            "viii3-ix0-opening-hinge-reunion-index-row-55",
        ),
        ("NPT Lab act steps 1–7", "EAM-fit audit Lab act steps 1–6"),
        ("`cu.elastic/`", "`pedigree_checklist.yaml`"),
        ("export homework", "DFT homework"),
        ("NPT → pedigree", "pedigree → foundation SCF"),
        ("export meta prelude capstone reunion", "electronic audit meta prelude capstone reunion"),
        ("skill-navigation-row-174", "skill-navigation-row-175"),
        ("row-174-baby-picture", "row-175-baby-picture"),
        ("Row 174", "Row 175"),
        ("row 174", "row 175"),
        ("row 54 export meta prelude", "row 56 Born–Oppenheimer meta prelude"),
        ("row 55 electronic audit meta prelude", "row 56 Born–Oppenheimer meta prelude"),
    ]
    return tx(block, pairs)


def insert_preface_row() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    if "### Row 175 skill checkpoint" in text:
        print("preface: row 175 already present")
        return
    m = re.search(
        r"(### Row 155 skill checkpoint.*?)(?=\n### Row 156 skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 155 checkpoint missing")
    block = lift_155_to_175(m.group(1))
    anchor = "\n## The copper wire through the book"
    idx = text.find(anchor)
    if idx < 0:
        raise SystemExit("copper wire anchor missing")
    text = text[:idx] + "\n" + block + text[idx:]
    path.write_text(text)
    print("preface: added row 175")


def insert_epilogue_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "### Row 175 closing loop" in text:
        print("epilogue: row 175 loop already present")
        return
    block = lift_155_to_175(
        extract_between(
            text,
            "### Row 155 closing loop",
            "### Row 154 closing loop",
        )
    )
    needle = "### Row 174 closing loop"
    text = text.replace(needle, block + needle, 1)
    path.write_text(text)
    print("epilogue: added row 175 loop")


def add_prologue_compass() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    compass = "| Row 68 → Row 151 Row 68 → Row 55 electronic audit meta prelude capstone reunion (row 175) |"
    if compass in text:
        print("prologue: row 175 compass already present")
    else:
        after = "| Row 68 → Row 151 Row 68 → Row 54 export meta prelude capstone reunion (row 174) |"
        idx = text.find(after)
        if idx < 0:
            raise SystemExit("prologue row 174 compass missing")
        line_end = text.find("\n", idx)
        src = "| Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone reunion (row 155) |"
        sidx = text.find(src)
        if sidx < 0:
            raise SystemExit("prologue row 155 compass missing")
        new_line = lift_155_to_175(text[sidx : text.find("\n", sidx)]) + "\n"
        text = text[: line_end + 1] + new_line + text[line_end + 1 :]
    preview_src = '| <span id="prologue-preview-row-155"></span>'
    preview_dst = '| <span id="prologue-preview-row-175"></span>'
    if preview_src in text and preview_dst not in text:
        i = text.find(preview_src)
        j = text.find("\n|", i + 1)
        preview_block = lift_155_to_175(text[i:j]) + "\n"
        text = text.replace(preview_src, preview_block + preview_src, 1)
    if "**Row 175 closing stitch" not in text:
        stitch = (
            "**Row 175 closing stitch (Row 68 → Row 151 Row 68 → Row 55 electronic audit meta prelude capstone reunion).** {#row-175-closing-stitch} "
            "When row 174 closed — export meta prelude capstone verified, row 174 or row 154 recited on the capstone path, and VIII.3 Bridge → IX.0 SCF recited with "
            "[EAM-fit audit Lab act](../part08-md/03-ab-initio-and-coarse-graining.md#lab-act-eam-fit-audit-before-the-notch-md-run-act-v--notch) archived `pedigree_checklist.yaml` — but **row 55 VIII.3 → IX.0 opening hinge still opens like standalone DFT homework after the export Scene on the capstone path** — "
            "the [preface row 175 When-to-pause opening sentence](../preface.md#skill-navigation-row-175) names the dual reunion before the Born–Oppenheimer meta prelude capstone reunion; "
            "read [preface row 175](../preface.md#skill-navigation-row-175), then the "
            "[Row 68 → Row 151 electronic audit reunion index](../appendix/sources.md#row68-row151-electronic-audit-meta-prelude-capstone-reunion-index-row-175), then "
            "[epilogue row 175 closing loop](../epilogue/multiscale.md#row-175-closing-loop) before row 56 Born–Oppenheimer meta prelude opens on the capstone path.\n\n"
        )
        text = text.replace("**Row 174 closing stitch", stitch + "**Row 174 closing stitch", 1)
    path.write_text(text)
    print("prologue: row 175 compass/preview/stitch")


def add_sources_row() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    idx_key = "row68-row151-electronic-audit-meta-prelude-capstone-reunion-index-row-175"
    if idx_key in text:
        print("sources: row 175 already present")
        return
    start174 = "## Row 68 → Row 151 Row 68 → Row 54 export meta prelude capstone reunion index (row 174)"
    i = text.find(start174)
    if i < 0:
        raise SystemExit("sources row 174 index missing")
    end173 = "## Row 68 → Row 151 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 173)"
    j173 = text.find(end173, i)
    if j173 < 0:
        j173 = text.find("\n## Row 68 → Row 132", i)
    if j173 < 0:
        raise SystemExit("sources row 173 index missing after 174")
    block = export_index_to_electronic_audit_175(lift_155_to_175(text[i:j173]))
    block = block.replace(
        "## Row 68 → Row 151 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 175)",
        f"## Row 68 → Row 151 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 175) {{#{idx_key}}}",
        1,
    )
    table_row = (
        "| 175 | Row 68 → Row 151 Row 68 → Row 55 electronic audit meta prelude capstone (midpoint prelude gate ↔ export meta prelude capstone ↔ row 55 meta) | "
        f"[Row 68 → Row 151 electronic audit meta prelude capstone reunion index](#{idx_key}) · "
        "[preface row 175](../preface.md#skill-navigation-row-175) · "
        "[prologue row 175 preview](../prologue/00-many-scales.md#prologue-preview-row-175) · "
        "[prologue row 175 closing stitch](../prologue/00-many-scales.md#row-175-closing-stitch) · "
        "[epilogue row 175 closing loop](../epilogue/multiscale.md#row-175-closing-loop) · "
        "[memory sheet row 175 baby picture](memory-sheet.md#row-175-baby-picture-row68-row151-electronic-audit-meta-prelude-capstone-reunion) | "
        "Row 68 closed but **row 55 VIII.3 → IX.0 opening hinge still feels disconnected from verified export meta prelude capstone on the capstone path** — "
        "read row 68 + row 174 or row 155 gate + VIII.3 Bridge → opening hinge → IX.0 SCF audit + row 55; "
        "[preface row 55](../preface.md#skill-navigation-row-55) |\n"
    )
    text = text.replace(
        "| 174 | Row 68 → Row 151 Row 68 → Row 54 export meta prelude capstone",
        table_row + "| 174 | Row 68 → Row 151 Row 68 → Row 54 export meta prelude capstone",
    )
    text = text.replace(start174, block + start174, 1)
    extra = (
        f"[row 175](#{idx_key}) reunites **export meta prelude capstone with the electronic audit meta prelude capstone boundary** "
        "when row 174 closed export meta prelude capstone at verified VIII.2 → VIII.3 closure on the capstone path but VIII.3 Bridge to Part IX and row 55 still read like separate courses;"
    )
    needle = (
        "[row 174](#row68-row151-export-meta-prelude-capstone-reunion-index-row-174) reunites **dynamics meta prelude capstone with the export meta prelude capstone boundary** "
    )
    if extra not in text and needle in text:
        text = text.replace(needle, needle + " " + extra)
    path.write_text(text)
    print("sources: added row 175")


def add_memory_row() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    if "row-175-baby-picture-row68-row151-electronic-audit-meta-prelude-capstone-reunion" in text:
        print("memory-sheet: row 175 already present")
        return
    baby = lift_155_to_175(
        extract_between(
            text,
            "### Row 155 baby picture",
            "### Row 156 baby picture",
        )
    )
    anchor = "### Row 155 baby picture"
    text = text.replace(anchor, baby + anchor, 1)
    mem_table = (
        "| 175 | Meta | Row 68 → Row 151 Row 68 → Row 55 electronic audit meta prelude capstone reunion | "
        "[Row 68 → Row 151 electronic audit meta prelude capstone reunion index](sources.md#row68-row151-electronic-audit-meta-prelude-capstone-reunion-index-row-175) · "
        "[preface row 175 skill checkpoint](../preface.md#skill-navigation-row-175) · "
        "[prologue row 175 preview](../prologue/00-many-scales.md#prologue-preview-row-175) · "
        "[prologue row 175 closing stitch](../prologue/00-many-scales.md#row-175-closing-stitch) · "
        "[epilogue row 175 closing loop](../epilogue/multiscale.md#row-175-closing-loop) | "
        "Row 68 closed but row 55 VIII.3 → IX.0 opening hinge feels disconnected from verified export meta prelude capstone on the capstone path — "
        "read row 68 + row 174 or row 155 gate + VIII.3 Bridge → opening hinge → IX.0 SCF audit + row 55; "
        "[row 175 baby picture](#row-175-baby-picture-row68-row151-electronic-audit-meta-prelude-capstone-reunion) |\n"
    )
    text = text.replace(
        "| 174 | Meta | Row 68 → Row 151 Row 68 → Row 54 export meta prelude capstone reunion |",
        mem_table + "| 174 | Meta | Row 68 → Row 151 Row 68 → Row 54 export meta prelude capstone reunion |",
    )
    if "When row 174 closed but electronic audit meta reunion still lags" not in text:
        text = text.replace(
            "When row 173 closed but export meta reunion still lags on the capstone path, switch to [row 174](#row-174-baby-picture-row68-row151-export-meta-prelude-capstone-reunion).",
            "When row 173 closed but export meta reunion still lags on the capstone path, switch to [row 174](#row-174-baby-picture-row68-row151-export-meta-prelude-capstone-reunion). "
            "When row 174 closed but electronic audit meta reunion still lags on the capstone path, switch to [row 175](#row-175-baby-picture-row68-row151-electronic-audit-meta-prelude-capstone-reunion).",
        )
    path.write_text(text)
    print("memory-sheet: added row 175")


def patch_row_174_proceed_links() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    text = text.replace(
        "proceed to [row 175](preface.md#skill-navigation-row-155)",
        "proceed to [row 175](preface.md#skill-navigation-row-175)",
    )
    path.write_text(text)
    ep = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep_text = ep.read_text()
    ep_text = ep_text.replace(
        "proceed to [row 175](preface.md#skill-navigation-row-155)",
        "proceed to [row 175](preface.md#skill-navigation-row-175)",
    )
    ep.write_text(ep_text)
    print("preface/epilogue: patched row 174 → row 175 proceed links")


def main() -> None:
    insert_preface_row()
    insert_epilogue_loop()
    add_prologue_compass()
    add_sources_row()
    add_memory_row()
    patch_row_174_proceed_links()


if __name__ == "__main__":
    main()
