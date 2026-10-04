#!/usr/bin/env python3
"""Add row 172 (Row 68 → Row 151 ↔ Row 52 atomistic meta prelude capstone on capstone path)."""
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


LIFT_152_TO_172_PAIRS: list[tuple[str, str]] = [
    ("Row 153 closing loop", "__PH153_LOOP__"),
    ("Row 152 closing loop", "Row 172 closing loop"),
    ("row-153-closing-loop", "__PH153_LOOP_ANCHOR__"),
    ("row-152-closing-loop", "row-172-closing-loop"),
    ("Row 153 closing stitch", "__PH153_STITCH__"),
    ("Row 152 closing stitch", "Row 172 closing stitch"),
    ("row-153-closing-stitch", "__PH153_STITCH_ANCHOR__"),
    ("row-152-closing-stitch", "row-172-closing-stitch"),
    ("prologue-preview-row-153", "__PH153_PREVIEW__"),
    ("prologue-preview-row-152", "prologue-preview-row-172"),
    ("Row 153 preview", "__PH153_PREVIEW_TEXT__"),
    ("Row 152 preview", "Row 172 preview"),
    ("Row 153 skill checkpoint", "__PH153_SKILL__"),
    ("Row 152 skill checkpoint", "Row 172 skill checkpoint"),
    ("skill-navigation-row-153", "__PH153_SKILL_NAV__"),
    ("skill-navigation-row-152", "skill-navigation-row-172"),
    ("memory sheet row 153", "__PH153_MEM__"),
    ("memory sheet row 152", "memory sheet row 172"),
    ("Row 153 baby picture", "__PH153_BABY__"),
    ("Row 152 baby picture", "Row 172 baby picture"),
    ("Row 153 three-way audit", "__PH153_AUDIT__"),
    ("Row 152 three-way audit", "Row 172 three-way audit"),
    (
        "Row 68 → Row 132 Row 68 → Row 52 atomistic meta prelude capstone",
        "Row 68 → Row 151 Row 68 → Row 52 atomistic meta prelude capstone",
    ),
    (
        "row68-row132-atomistic-meta-prelude-capstone-reunion-index-row-152",
        "row68-row151-atomistic-meta-prelude-capstone-reunion-index-row-172",
    ),
    (
        "row-152-baby-picture-row68-row132-atomistic-meta-prelude-capstone-reunion",
        "row-172-baby-picture-row68-row151-atomistic-meta-prelude-capstone-reunion",
    ),
    ("[row 153]", "__ROW153_REF__"),
    ("[row 132]", "[row 152]"),
    ("row 132", "row 152"),
    ("Row 132", "Row 152"),
    ("__ROW153_REF__", "[row 153]"),
    ("[row 151]", "__ROW171_GATE__"),
    ("row 151", "__row171_gate__"),
    ("Row 151", "__ROW171_GATE_CAP__"),
    (
        "Row 68 → Row 112 atomistic meta prelude capstone reunion index (row 132)",
        "Row 68 → Row 132 atomistic meta prelude capstone reunion index (row 152)",
    ),
    (
        "row68-row112-atomistic-meta-prelude-capstone-reunion-index-row-132",
        "row68-row151-atomistic-meta-prelude-capstone-reunion-index-row-172",
    ),
    (
        "verified homogenization meta prelude capstone closure (row 151)",
        "verified homogenization meta prelude capstone closure (row 171)",
    ),
    ("when row 151 closed but row 52", "when row 171 closed but row 52"),
    ("after row 151.", "after row 171."),
    ("when row 151 and row 52", "when row 171 and row 52"),
    (
        "rear-view mirror of row 151's polycrystal → atomic ink turn",
        "rear-view mirror of row 171's polycrystal → atomic ink turn",
    ),
    (
        "when opening [row 153](preface.md#skill-navigation-row-153) before row 54 closes on the capstone path",
        "when opening [row 172](preface.md#skill-navigation-row-172) before row 54 closes on the capstone path",
    ),
    (
        "When row 152 is complete, proceed to [row 153]",
        "When row 172 is complete, proceed to [row 153]",
    ),
    (
        "Proceed to [row 153](#row-153-closing-loop) when row 68 closed but dynamics meta prelude capstone still lags after row 152 on the capstone path",
        "Proceed to [row 172](#row-172-closing-loop) when row 68 closed but atomistic meta prelude capstone still lags after row 171 on the capstone path, "
        "to [row 152](#row-152-closing-loop) when row 68 closed but atomistic meta prelude capstone still lags after verified homogenization meta prelude capstone on the opening-hinge path",
    ),
    (
        "When row 52 feels like LAMMPS homework after row 151 alone on the capstone path",
        "When row 52 feels like LAMMPS homework after row 171 alone on the capstone path",
    ),
    (
        "row 152 (row 68 ↔ row 52 reunion on the capstone path) with row 132",
        "row 172 (row 68 ↔ row 52 reunion on the capstone path) with row 152",
    ),
    (
        "row 152 names **why that reunion must follow verified homogenization meta prelude capstone (row 151)",
        "row 172 names **why that reunion must follow verified homogenization meta prelude capstone (row 171)",
    ),
    ("Row 68 → Row 52 meta (row 132)", "Row 68 → Row 52 meta (row 152)"),
    (
        "Row 68 → Row 132 atomistic meta prelude capstone reunion index (row 152)",
        "Row 68 → Row 151 atomistic meta prelude capstone reunion index (row 172)",
    ),
    ("Row 68 → Row 132 reunion index", "Row 68 → Row 151 reunion index"),
    ("(row 152)", "(row 172)"),
    ("Row 152 closes the", "Row 172 closes the"),
    ("Row 152 does not conflate", "Row 172 does not conflate"),
    ("Row 152 does not replace", "Row 172 does not replace"),
    ("__PH153_LOOP__", "Row 153 closing loop"),
    ("__PH153_LOOP_ANCHOR__", "row-153-closing-loop"),
    ("__PH153_STITCH__", "Row 153 closing stitch"),
    ("__PH153_STITCH_ANCHOR__", "row-153-closing-stitch"),
    ("__PH153_PREVIEW__", "prologue-preview-row-153"),
    ("__PH153_PREVIEW_TEXT__", "Row 153 preview"),
    ("__PH153_SKILL__", "Row 153 skill checkpoint"),
    ("__PH153_SKILL_NAV__", "skill-navigation-row-153"),
    ("__PH153_MEM__", "memory sheet row 153"),
    ("__PH153_BABY__", "Row 153 baby picture"),
    ("__PH153_AUDIT__", "Row 153 three-way audit"),
    ("__ROW171_GATE__", "[row 171]"),
    ("__row171_gate__", "row 171"),
    ("__ROW171_GATE_CAP__", "Row 171"),
]


def lift_152_to_172(s: str) -> str:
    out = tx(s, LIFT_152_TO_172_PAIRS)
    out = out.replace(
        "[row 171](preface.md#skill-navigation-row-151)",
        "[row 171](preface.md#skill-navigation-row-171)",
    )
    out = out.replace(
        "[row 152](preface.md#skill-navigation-row-132)",
        "[row 152](preface.md#skill-navigation-row-152)",
    )
    out = re.sub(
        r"(### Row 172 skill checkpoint[^\n]*)\{#skill-navigation-row-152\}",
        r"\1{#skill-navigation-row-172}",
        out,
        count=1,
    )
    return out


def insert_preface_row() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    if "### Row 172 skill checkpoint" in text:
        print("preface: row 172 already present")
        return
    m = re.search(
        r"(### Row 152 skill checkpoint.*?)(?=\n### Row 153 skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 152 checkpoint missing")
    block = lift_152_to_172(m.group(1))
    anchor = "\n## The copper wire through the book"
    idx = text.find(anchor)
    if idx < 0:
        raise SystemExit("copper wire anchor missing")
    text = text[:idx] + "\n" + block + text[idx:]
    path.write_text(text)
    print("preface: added row 172")


def insert_epilogue_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "### Row 172 closing loop" in text:
        print("epilogue: row 172 loop already present")
        return
    block = lift_152_to_172(
        extract_between(
            text,
            "### Row 152 closing loop",
            "### Row 151 closing loop",
        )
    )
    needle = "### Row 171 closing loop"
    text = text.replace(needle, block + needle, 1)
    path.write_text(text)
    print("epilogue: added row 172 loop")


def add_prologue_compass() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    compass = "| Row 68 → Row 151 Row 68 → Row 52 atomistic meta prelude capstone reunion (row 172) |"
    if compass in text:
        print("prologue: row 172 compass already present")
    else:
        after = "| Row 68 → Row 151 Row 68 → Row 51 homogenization meta prelude capstone reunion (row 171) |"
        idx = text.find(after)
        if idx < 0:
            raise SystemExit("prologue row 171 compass missing")
        line_end = text.find("\n", idx)
        src = "| Row 68 → Row 132 Row 68 → Row 52 atomistic meta prelude capstone reunion (row 152) |"
        sidx = text.find(src)
        if sidx < 0:
            raise SystemExit("prologue row 152 compass missing")
        new_line = lift_152_to_172(text[sidx : text.find("\n", sidx)]) + "\n"
        text = text[: line_end + 1] + new_line + text[line_end + 1 :]
    preview_src = '| <span id="prologue-preview-row-152"></span>'
    preview_dst = '| <span id="prologue-preview-row-172"></span>'
    if preview_src in text and preview_dst not in text:
        i = text.find(preview_src)
        j = text.find("\n|", i + 1)
        preview_block = lift_152_to_172(text[i:j]) + "\n"
        text = text.replace(preview_src, preview_block + preview_src, 1)
    if "**Row 172 closing stitch" not in text:
        stitch = (
            "**Row 172 closing stitch (Row 68 → Row 151 Row 68 → Row 52 atomistic meta prelude capstone reunion).** {#row-172-closing-stitch} "
            "When row 171 closed — homogenization meta prelude capstone verified, row 170 or row 151 recited on the capstone path, and VII.2 Bridge → VII.3 polycrystal recited with handoff Lab act archived `mobility.yaml` — "
            "but **row 52 VII.3 → VIII.1 opening hinge still opens like standalone LAMMPS homework after the handoff Lab act on the capstone path** — "
            "the [preface row 172 When-to-pause opening sentence](../preface.md#skill-navigation-row-172) names the dual reunion before the dynamics meta reunion; "
            "read [preface row 172](../preface.md#skill-navigation-row-172), then the "
            "[Row 68 → Row 151 atomistic reunion index](../appendix/sources.md#row68-row151-atomistic-meta-prelude-capstone-reunion-index-row-172), then "
            "[epilogue row 172 closing loop](../epilogue/multiscale.md#row-172-closing-loop) before row 53 dynamics meta prelude opens on the capstone path.\n\n"
        )
        text = text.replace("**Row 171 closing stitch", stitch + "**Row 171 closing stitch", 1)
    path.write_text(text)
    print("prologue: row 172 compass/preview/stitch")


def add_sources_row() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    idx_key = "row68-row151-atomistic-meta-prelude-capstone-reunion-index-row-172"
    if idx_key in text:
        print("sources: row 172 already present")
        return
    start = "## Row 68 → Row 132 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 152)"
    i = text.find(start)
    if i < 0:
        raise SystemExit("sources row 152 index missing")
    end171 = "## Row 68 → Row 151 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 171)"
    j171 = text.find(end171, i)
    if j171 < 0:
        raise SystemExit("sources row 171 index missing")
    block = lift_152_to_172(text[i:j171])
    block = block.replace(
        "## Row 68 → Row 151 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 172)",
        f"## Row 68 → Row 151 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 172) {{#{idx_key}}}",
        1,
    )
    table_row = (
        "| 172 | Row 68 → Row 151 Row 68 → Row 52 atomistic meta prelude capstone (midpoint prelude gate ↔ homogenization meta prelude capstone ↔ row 52 meta) | "
        f"[Row 68 → Row 151 atomistic meta prelude capstone reunion index](#{idx_key}) · "
        "[preface row 172](../preface.md#skill-navigation-row-172) · "
        "[prologue row 172 preview](../prologue/00-many-scales.md#prologue-preview-row-172) · "
        "[prologue row 172 closing stitch](../prologue/00-many-scales.md#row-172-closing-stitch) · "
        "[epilogue row 172 closing loop](../epilogue/multiscale.md#row-172-closing-loop) · "
        "[memory sheet row 172 baby picture](memory-sheet.md#row-172-baby-picture-row68-row151-atomistic-meta-prelude-capstone-reunion) | "
        "Row 68 closed but **row 52 VII.3 → VIII.1 opening hinge still feels disconnected from verified homogenization meta prelude capstone on the capstone path** — "
        "read row 68 + row 171 or row 152 gate + VII.3 Bridge → opening hinge → VIII.1 phase space + row 52; "
        "[preface row 52](../preface.md#skill-navigation-row-52) |\n"
    )
    text = text.replace(
        "| 171 | Row 68 → Row 151 Row 68 → Row 51 homogenization meta prelude capstone",
        table_row + "| 171 | Row 68 → Row 151 Row 68 → Row 51 homogenization meta prelude capstone",
    )
    text = text.replace(
        start,
        block + start,
        1,
    )
    extra = (
        f"[row 172](#{idx_key}) reunites **homogenization meta prelude capstone with the atomistic meta prelude capstone boundary** "
        "when row 171 closed homogenization meta prelude capstone at verified polycrystal closure on the capstone path but VII.3 Bridge and row 52 still read like separate courses after verified atomistic meta prelude meta;"
    )
    if extra not in text:
        needle = (
            "[row 171](#row68-row151-homogenization-meta-prelude-capstone-reunion-index-row-171) reunites **homogenization meta prelude capstone with the atomistic meta prelude capstone boundary** "
        )
        if needle in text:
            text = text.replace(needle, needle + " " + extra)
    path.write_text(text)
    print("sources: added row 172")


def add_memory_row() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    if "row-172-baby-picture-row68-row151-atomistic-meta-prelude-capstone-reunion" in text:
        print("memory-sheet: row 172 already present")
        return
    baby = lift_152_to_172(
        extract_between(
            text,
            "### Row 152 baby picture",
            "### Row 153 baby picture",
        )
    )
    anchor = "### Row 152 baby picture"
    text = text.replace(anchor, baby + anchor, 1)
    mem_table = (
        "| 172 | Meta | Row 68 → Row 151 Row 68 → Row 52 atomistic meta prelude capstone reunion | "
        "[Row 68 → Row 151 atomistic meta prelude capstone reunion index](sources.md#row68-row151-atomistic-meta-prelude-capstone-reunion-index-row-172) · "
        "[preface row 172 skill checkpoint](../preface.md#skill-navigation-row-172) · "
        "[prologue row 172 preview](../prologue/00-many-scales.md#prologue-preview-row-172) · "
        "[prologue row 172 closing stitch](../prologue/00-many-scales.md#row-172-closing-stitch) · "
        "[epilogue row 172 closing loop](../epilogue/multiscale.md#row-172-closing-loop) | "
        "Row 68 closed but row 52 VII.3 → VIII.1 opening hinge feels disconnected from verified homogenization meta prelude capstone on the capstone path — "
        "read row 68 + row 171 or row 152 gate + VII.3 Bridge → opening hinge → VIII.1 phase space + row 52; "
        "[row 172 baby picture](#row-172-baby-picture-row68-row151-atomistic-meta-prelude-capstone-reunion) |\n"
    )
    text = text.replace(
        "| 171 | Meta | Row 68 → Row 151 Row 68 → Row 51 homogenization meta prelude capstone reunion |",
        mem_table + "| 171 | Meta | Row 68 → Row 151 Row 68 → Row 51 homogenization meta prelude capstone reunion |",
    )
    if "When row 171 closed but atomistic meta reunion still lags" not in text:
        text = text.replace(
            "When row 170 closed but homogenization meta reunion still lags on the capstone path, switch to [row 171](#row-171-baby-picture-row68-row151-homogenization-meta-prelude-capstone-reunion).",
            "When row 170 closed but homogenization meta reunion still lags on the capstone path, switch to [row 171](#row-171-baby-picture-row68-row151-homogenization-meta-prelude-capstone-reunion). "
            "When row 171 closed but atomistic meta reunion still lags on the capstone path, switch to [row 172](#row-172-baby-picture-row68-row151-atomistic-meta-prelude-capstone-reunion).",
        )
    path.write_text(text)
    print("memory-sheet: added row 172")


def patch_row_171_proceed_links() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    text = text.replace(
        "proceed to [row 172](preface.md#skill-navigation-row-152)",
        "proceed to [row 172](preface.md#skill-navigation-row-172)",
    )
    path.write_text(text)
    ep = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep_text = ep.read_text()
    ep_text = ep_text.replace(
        "proceed to [row 172](preface.md#skill-navigation-row-152)",
        "proceed to [row 172](preface.md#skill-navigation-row-172)",
    )
    ep.write_text(ep_text)
    print("preface/epilogue: patched row 171 → row 172 proceed links")


def main() -> None:
    insert_preface_row()
    insert_epilogue_loop()
    add_prologue_compass()
    add_sources_row()
    add_memory_row()
    patch_row_171_proceed_links()


if __name__ == "__main__":
    main()
