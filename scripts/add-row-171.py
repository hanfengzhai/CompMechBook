#!/usr/bin/env python3
"""Add row 171 (Row 68 → Row 151 ↔ Row 51 homogenization meta prelude capstone on capstone path)."""
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


LIFT_151_TO_171_PAIRS: list[tuple[str, str]] = [
    ("Row 152 closing loop", "__PH152_LOOP__"),
    ("Row 151 closing loop", "Row 171 closing loop"),
    ("row-152-closing-loop", "__PH152_LOOP_ANCHOR__"),
    ("row-151-closing-loop", "row-171-closing-loop"),
    ("Row 152 closing stitch", "__PH152_STITCH__"),
    ("Row 151 closing stitch", "Row 171 closing stitch"),
    ("row-152-closing-stitch", "__PH152_STITCH_ANCHOR__"),
    ("row-151-closing-stitch", "row-171-closing-stitch"),
    ("prologue-preview-row-152", "__PH152_PREVIEW__"),
    ("prologue-preview-row-151", "prologue-preview-row-171"),
    ("Row 152 preview", "__PH152_PREVIEW_TEXT__"),
    ("Row 151 preview", "Row 171 preview"),
    ("Row 152 skill checkpoint", "__PH152_SKILL__"),
    ("Row 151 skill checkpoint", "Row 171 skill checkpoint"),
    ("skill-navigation-row-152", "__PH152_SKILL_NAV__"),
    ("skill-navigation-row-151", "skill-navigation-row-171"),
    ("memory sheet row 152", "__PH152_MEM__"),
    ("memory sheet row 151", "memory sheet row 171"),
    ("Row 152 baby picture", "__PH152_BABY__"),
    ("Row 151 baby picture", "Row 171 baby picture"),
    ("Row 152 three-way audit", "__PH152_AUDIT__"),
    ("Row 151 three-way audit", "Row 171 three-way audit"),
    (
        "Row 68 → Row 131 Row 68 → Row 51 homogenization meta prelude capstone",
        "Row 68 → Row 151 Row 68 → Row 51 homogenization meta prelude capstone",
    ),
    (
        "row68-row131-homogenization-meta-prelude-capstone-reunion-index-row-151",
        "row68-row151-homogenization-meta-prelude-capstone-reunion-index-row-171",
    ),
    (
        "row-151-baby-picture-row68-row131-homogenization-meta-prelude-capstone-reunion",
        "row-171-baby-picture-row68-row151-homogenization-meta-prelude-capstone-reunion",
    ),
    ("[row 152]", "__ROW152_REF__"),
    ("[row 131]", "[row 151]"),
    ("row 131", "row 151"),
    ("Row 131", "Row 151"),
    ("__ROW152_REF__", "[row 152]"),
    ("[row 150]", "[row 170]"),
    ("row 150", "row 170"),
    ("Row 150", "Row 170"),
    (
        "Row 68 → Row 111 homogenization meta prelude capstone reunion index (row 131)",
        "Row 68 → Row 131 homogenization meta prelude capstone reunion index (row 151)",
    ),
    (
        "row68-row111-homogenization-meta-prelude-capstone-reunion-index-row-131",
        "row68-row151-homogenization-meta-prelude-capstone-reunion-index-row-171",
    ),
    (
        "verified DDD meta prelude capstone closure (row 150)",
        "verified DDD meta prelude capstone closure (row 170)",
    ),
    ("when row 150 closed but row 51", "when row 170 closed but row 51"),
    ("after row 150.", "after row 170."),
    ("when row 150 and row 51", "when row 170 and row 51"),
    (
        "rear-view mirror of row 150's Peach–Köhler → spool turn",
        "rear-view mirror of row 170's Peach–Köhler → spool turn",
    ),
    (
        "when opening [row 152](preface.md#skill-navigation-row-152) before row 52 closes on the capstone path",
        "when opening [row 171](preface.md#skill-navigation-row-171) before row 52 closes on the capstone path",
    ),
    (
        "When row 151 is complete, proceed to [row 152]",
        "When row 171 is complete, proceed to [row 152]",
    ),
    (
        "Proceed to [row 152](#row-152-closing-loop) when row 68 closed but atomistic meta capstone still lags after row 151 on the capstone path",
        "Proceed to [row 171](#row-171-closing-loop) when row 68 closed but homogenization meta prelude capstone still lags after row 170 on the capstone path, "
        "to [row 151](#row-151-closing-loop) when row 68 closed but homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the opening-hinge path",
    ),
    (
        "When row 51 feels like DAMASK homework after row 150 alone on the capstone path",
        "When row 51 feels like DAMASK homework after row 170 alone on the capstone path",
    ),
    (
        "row 151 (row 68 ↔ row 51 reunion on the capstone path) with row 131",
        "row 171 (row 68 ↔ row 51 reunion on the capstone path) with row 151",
    ),
    (
        "row 151 names **why that reunion must follow verified DDD meta prelude capstone (row 150)",
        "row 171 names **why that reunion must follow verified DDD meta prelude capstone (row 170)",
    ),
    ("Row 68 → Row 51 meta (row 131)", "Row 68 → Row 51 meta (row 151)"),
    (
        "Row 68 → Row 131 homogenization meta prelude capstone reunion index (row 151)",
        "Row 68 → Row 151 homogenization meta prelude capstone reunion index (row 171)",
    ),
    ("Row 68 → Row 131 reunion index", "Row 68 → Row 151 reunion index"),
    ("(row 151)", "(row 171)"),
    ("Row 151 closes the", "Row 171 closes the"),
    ("Row 151 does not conflate", "Row 171 does not conflate"),
    ("Row 151 does not replace", "Row 171 does not replace"),
    ("__PH152_LOOP__", "Row 152 closing loop"),
    ("__PH152_LOOP_ANCHOR__", "row-152-closing-loop"),
    ("__PH152_STITCH__", "Row 152 closing stitch"),
    ("__PH152_STITCH_ANCHOR__", "row-152-closing-stitch"),
    ("__PH152_PREVIEW__", "prologue-preview-row-152"),
    ("__PH152_PREVIEW_TEXT__", "Row 152 preview"),
    ("__PH152_SKILL__", "Row 152 skill checkpoint"),
    ("__PH152_SKILL_NAV__", "skill-navigation-row-152"),
    ("__PH152_MEM__", "memory sheet row 152"),
    ("__PH152_BABY__", "Row 152 baby picture"),
    ("__PH152_AUDIT__", "Row 152 three-way audit"),
]


def lift_151_to_171(s: str) -> str:
    out = tx(s, LIFT_151_TO_171_PAIRS)
    out = out.replace(
        "[row 170](preface.md#skill-navigation-row-130)",
        "[row 170](preface.md#skill-navigation-row-170)",
    )
    out = out.replace(
        "[row 151](preface.md#skill-navigation-row-111)",
        "[row 151](preface.md#skill-navigation-row-151)",
    )
    out = re.sub(
        r"(### Row 171 skill checkpoint[^\n]*)\{#skill-navigation-row-151\}",
        r"\1{#skill-navigation-row-171}",
        out,
        count=1,
    )
    return out


def insert_preface_row() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    if "### Row 171 skill checkpoint" in text:
        print("preface: row 171 already present")
        return
    m = re.search(
        r"(### Row 151 skill checkpoint.*?)(?=\n### Row 152 skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 151 checkpoint missing")
    block = lift_151_to_171(m.group(1))
    anchor = "\n## The copper wire through the book"
    idx = text.find(anchor)
    if idx < 0:
        raise SystemExit("copper wire anchor missing")
    text = text[:idx] + "\n" + block + text[idx:]
    path.write_text(text)
    print("preface: added row 171")


def insert_epilogue_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "### Row 171 closing loop" in text:
        print("epilogue: row 171 loop already present")
        return
    block = lift_151_to_171(
        extract_between(
            text,
            "### Row 151 closing loop",
            "### Row 132 closing loop",
        )
    )
    needle = "### Row 170 closing loop"
    text = text.replace(needle, block + needle, 1)
    path.write_text(text)
    print("epilogue: added row 171 loop")


def add_prologue_compass() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    compass = "| Row 68 → Row 151 Row 68 → Row 51 homogenization meta prelude capstone reunion (row 171) |"
    if compass in text:
        print("prologue: row 171 compass already present")
    else:
        after = "| Row 68 → Row 150 Row 68 → Row 50 DDD meta prelude capstone reunion (row 170) |"
        idx = text.find(after)
        if idx < 0:
            raise SystemExit("prologue row 170 compass missing")
        line_end = text.find("\n", idx)
        src = "| Row 68 → Row 131 Row 68 → Row 51 homogenization meta prelude capstone reunion (row 151) |"
        sidx = text.find(src)
        if sidx < 0:
            raise SystemExit("prologue row 151 compass missing")
        new_line = lift_151_to_171(text[sidx : text.find("\n", sidx)]) + "\n"
        text = text[: line_end + 1] + new_line + text[line_end + 1 :]
    preview_src = '| <span id="prologue-preview-row-151"></span>'
    preview_dst = '| <span id="prologue-preview-row-171"></span>'
    if preview_src in text and preview_dst not in text:
        i = text.find(preview_src)
        j = text.find("\n|", i + 1)
        preview_block = lift_151_to_171(text[i:j]) + "\n"
        text = text.replace(preview_src, preview_block + preview_src, 1)
    if "**Row 171 closing stitch" not in text:
        stitch = (
            "**Row 171 closing stitch (Row 68 → Row 151 Row 68 → Row 51 homogenization meta prelude capstone reunion).** {#row-171-closing-stitch} "
            "When row 170 closed — DDD meta prelude capstone verified, row 169 or row 150 recited on the capstone path, and VII.1 Bridge → VII.2 Peach–Köhler recited with forest-density Lab act linked \\(\\tau(\\gamma)\\) to Taylor hardening — "
            "but **row 51 VII.2 → VII.3 opening hinge still opens like standalone DAMASK homework after the post-yield forest Scene on the capstone path** — "
            "the [preface row 171 When-to-pause opening sentence](../preface.md#skill-navigation-row-171) names the dual reunion before the atomistic meta reunion; "
            "read [preface row 171](../preface.md#skill-navigation-row-171), then the "
            "[Row 68 → Row 151 reunion index](../appendix/sources.md#row68-row151-homogenization-meta-prelude-capstone-reunion-index-row-171), then "
            "[epilogue row 171 closing loop](../epilogue/multiscale.md#row-171-closing-loop) before row 52 atomistic meta prelude opens on the capstone path.\n\n"
        )
        text = text.replace("**Row 170 closing stitch", stitch + "**Row 170 closing stitch", 1)
    path.write_text(text)
    print("prologue: row 171 compass/preview/stitch")


def add_sources_row() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    idx_key = "row68-row151-homogenization-meta-prelude-capstone-reunion-index-row-171"
    if idx_key in text:
        print("sources: row 171 already present")
        return
    start = "## Row 68 → Row 131 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 151)"
    i = text.find(start)
    if i < 0:
        raise SystemExit("sources row 151 index missing")
    block = lift_151_to_171(text[i:])
    block = block.split("## Row 68 → Row 112")[0]
    block = block.replace(
        "## Row 68 → Row 151 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 171)",
        f"## Row 68 → Row 151 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 171) {{#{idx_key}}}",
        1,
    )
    table_row = (
        "| 171 | Row 68 → Row 151 Row 68 → Row 51 homogenization meta prelude capstone (midpoint prelude gate ↔ DDD meta prelude capstone ↔ row 51 meta) | "
        f"[Row 68 → Row 151 homogenization meta prelude capstone reunion index](#{idx_key}) · "
        "[preface row 171](../preface.md#skill-navigation-row-171) · "
        "[prologue row 171 preview](../prologue/00-many-scales.md#prologue-preview-row-171) · "
        "[prologue row 171 closing stitch](../prologue/00-many-scales.md#row-171-closing-stitch) · "
        "[epilogue row 171 closing loop](../epilogue/multiscale.md#row-171-closing-loop) · "
        "[memory sheet row 171 baby picture](memory-sheet.md#row-171-baby-picture-row68-row151-homogenization-meta-prelude-capstone-reunion) | "
        "Row 68 closed but **row 51 VII.2 → VII.3 opening hinge still feels disconnected from verified DDD meta prelude capstone on the capstone path** — "
        "read row 68 + row 170 or row 151 gate + VII.2 Bridge → opening hinge → VII.3 homogenization + row 51; "
        "[preface row 51](../preface.md#skill-navigation-row-51) |\n"
    )
    text = text.replace(
        "| 170 | Row 68 → Row 150 Row 68 → Row 50 DDD meta prelude capstone",
        table_row + "| 170 | Row 68 → Row 150 Row 68 → Row 50 DDD meta prelude capstone",
    )
    text = text.replace(
        start,
        block + start,
        1,
    )
    extra = (
        f"[row 170](#{idx_key}) reunites **DDD meta prelude capstone with the homogenization meta prelude capstone boundary** "
        "when row 170 closed DDD meta prelude capstone at verified Peach–Köhler closure on the capstone path but VII.2 Bridge and row 51 still read like separate courses after verified homogenization meta prelude meta;"
    )
    if extra not in text:
        needle = (
            "[row 169](#row68-row150-ddd-meta-prelude-capstone-reunion-index-row-170) reunites **taxonomy meta prelude capstone with the DDD meta prelude capstone boundary** "
        )
        if needle in text:
            text = text.replace(needle, needle + " " + extra)
    path.write_text(text)
    print("sources: added row 171")


def add_memory_row() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    if "row-171-baby-picture-row68-row151-homogenization-meta-prelude-capstone-reunion" in text:
        print("memory-sheet: row 171 already present")
        return
    baby = lift_151_to_171(
        extract_between(
            text,
            "### Row 151 baby picture",
            "### Row 152 baby picture",
        )
    )
    anchor = "### Row 151 baby picture"
    text = text.replace(anchor, baby + anchor, 1)
    mem_table = (
        "| 171 | Meta | Row 68 → Row 151 Row 68 → Row 51 homogenization meta prelude capstone reunion | "
        "[Row 68 → Row 151 homogenization meta prelude capstone reunion index](sources.md#row68-row151-homogenization-meta-prelude-capstone-reunion-index-row-171) · "
        "[preface row 171 skill checkpoint](../preface.md#skill-navigation-row-171) · "
        "[prologue row 171 preview](../prologue/00-many-scales.md#prologue-preview-row-171) · "
        "[prologue row 171 closing stitch](../prologue/00-many-scales.md#row-171-closing-stitch) · "
        "[epilogue row 171 closing loop](../epilogue/multiscale.md#row-171-closing-loop) | "
        "Row 68 closed but row 51 VII.2 → VII.3 opening hinge feels disconnected from verified DDD meta prelude capstone on the capstone path — "
        "read row 68 + row 170 or row 151 gate + VII.2 Bridge → opening hinge → VII.3 homogenization + row 51; "
        "[row 171 baby picture](#row-171-baby-picture-row68-row151-homogenization-meta-prelude-capstone-reunion) |\n"
    )
    text = text.replace(
        "| 170 | Meta | Row 68 → Row 150 Row 68 → Row 50 DDD meta prelude capstone reunion |",
        mem_table + "| 170 | Meta | Row 68 → Row 150 Row 68 → Row 50 DDD meta prelude capstone reunion |",
    )
    if "When row 170 closed but homogenization meta reunion still lags" not in text:
        text = text.replace(
            "When row 150 closed but homogenization meta reunion still lags on the capstone path, switch to [row 151](#row-151-baby-picture-row68-row131-homogenization-meta-prelude-capstone-reunion).",
            "When row 150 closed but homogenization meta reunion still lags on the capstone path, switch to [row 151](#row-151-baby-picture-row68-row131-homogenization-meta-prelude-capstone-reunion). "
            "When row 170 closed but homogenization meta reunion still lags on the capstone path, switch to [row 171](#row-171-baby-picture-row68-row151-homogenization-meta-prelude-capstone-reunion).",
        )
    path.write_text(text)
    print("memory-sheet: added row 171")


def patch_row_170_proceed_links() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    text = text.replace(
        "proceed to [row 171](preface.md#skill-navigation-row-151)",
        "proceed to [row 171](preface.md#skill-navigation-row-171)",
    )
    old = (
        "Proceed to [row 171](#row-171-closing-loop) when row 68 closed but homogenization meta prelude capstone still lags after row 170 on the capstone path"
    )
    new = (
        "Proceed to [row 171](#row-171-closing-loop) when row 68 closed but homogenization meta prelude capstone still lags after row 170 on the capstone path"
    )
    path.write_text(text)
    ep = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep_text = ep.read_text()
    ep_text = ep_text.replace(
        "proceed to [row 171](preface.md#skill-navigation-row-151)",
        "proceed to [row 171](preface.md#skill-navigation-row-171)",
    )
    ep.write_text(ep_text)
    print("preface/epilogue: patched row 170 → row 171 proceed links")


def main() -> None:
    insert_preface_row()
    insert_epilogue_loop()
    add_prologue_compass()
    add_sources_row()
    add_memory_row()
    patch_row_170_proceed_links()


if __name__ == "__main__":
    main()
