#!/usr/bin/env python3
"""Add row 181 (Row 68 → Row 151 ↔ Row 61 Handshake 4a meta prelude capstone reunion on capstone path)."""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

_spec = importlib.util.spec_from_file_location("add_row_161_mod", ROOT / "scripts" / "add-row-161.py")
_mod = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_mod)
extract_between = _mod.extract_between
tx = _mod.tx


def lift_161_to_181(s: str) -> str:
    s = s.replace(
        "[row 161](preface.md#skill-navigation-row-161)",
        "__ROW161_HINGE__",
    )
    s = s.replace(
        "[row 180](preface.md#skill-navigation-row-180)",
        "__ROW180_GATE__",
    )
    p = [
        ("Row 162 closing loop", "__PH162_LOOP__"),
        ("Row 161 closing loop", "Row 181 closing loop"),
        ("row-162-closing-loop", "__PH162_LOOP_ANCHOR__"),
        ("row-161-closing-loop", "row-181-closing-loop"),
        ("Row 162 closing stitch", "__PH162_STITCH__"),
        ("Row 161 closing stitch", "Row 181 closing stitch"),
        ("row-162-closing-stitch", "__PH162_STITCH_ANCHOR__"),
        ("row-161-closing-stitch", "row-181-closing-stitch"),
        ("prologue-preview-row-162", "__PH162_PREVIEW__"),
        ("prologue-preview-row-161", "prologue-preview-row-181"),
        ("Row 162 preview", "__PH162_PREVIEW_TEXT__"),
        ("Row 161 preview", "Row 181 preview"),
        ("Row 162 skill checkpoint", "__PH162_SKILL__"),
        ("Row 161 skill checkpoint", "Row 181 skill checkpoint"),
        ("skill-navigation-row-162", "__PH162_SKILL_NAV__"),
        ("skill-navigation-row-161", "skill-navigation-row-181"),
        ("memory sheet row 162", "__PH162_MEM__"),
        ("memory sheet row 161", "memory sheet row 181"),
        ("Row 162 baby picture", "__PH162_BABY__"),
        ("Row 161 baby picture", "Row 181 baby picture"),
        ("Row 162 three-way audit", "__PH162_AUDIT__"),
        ("Row 161 three-way audit", "Row 181 three-way audit"),
        (
            "Row 68 → Row 141 Row 68 → Row 61 Handshake 4a meta prelude capstone",
            "Row 68 → Row 151 Row 68 → Row 61 Handshake 4a meta prelude capstone",
        ),
        (
            "row68-row141-handshake4a-meta-prelude-capstone-reunion-index-row-161",
            "row68-row151-handshake4a-meta-prelude-capstone-reunion-index-row-181",
        ),
        (
            "row-161-baby-picture-row68-row141-handshake4a-meta-prelude-capstone-reunion",
            "row-181-baby-picture-row68-row151-handshake4a-meta-prelude-capstone-reunion",
        ),
        ("[row 162]", "__ROW162_REF__"),
        ("__ROW180_GATE__", "[row 180](preface.md#skill-navigation-row-180)"),
        ("row 160", "row 180"),
        ("Row 160", "Row 180"),
        ("(row 161)", "(row 181)"),
        ("Row 161 closes the", "Row 181 closes the"),
        ("Row 161 does not conflate", "Row 181 does not conflate"),
        ("Row 161 does not replace", "Row 181 does not replace"),
        ("__PH162_LOOP__", "Row 162 closing loop"),
        ("__PH162_LOOP_ANCHOR__", "row-162-closing-loop"),
        ("__PH162_STITCH__", "Row 162 closing stitch"),
        ("__PH162_STITCH_ANCHOR__", "row-162-closing-stitch"),
        ("__PH162_PREVIEW__", "prologue-preview-row-162"),
        ("__PH162_PREVIEW_TEXT__", "Row 162 preview"),
        ("__PH162_SKILL__", "Row 162 skill checkpoint"),
        ("__PH162_SKILL_NAV__", "skill-navigation-row-162"),
        ("__PH162_MEM__", "memory sheet row 162"),
        ("__PH162_BABY__", "Row 162 baby picture"),
        ("__PH162_AUDIT__", "Row 162 three-way audit"),
        ("__ROW162_REF__", "[row 182]"),
        (
            "verified Handshake 3 meta prelude capstone closure (row 160)",
            "verified Handshake 4a meta prelude capstone closure (row 180)",
        ),
        ("when row 160 closed but row 61", "when row 180 closed but row 61"),
        (
            "When row 160 closed — Handshake 3 meta prelude capstone verified",
            "When row 180 closed — Handshake 3 meta prelude capstone reunion verified",
        ),
        (
            "when row 160 and row 61 both verify individually",
            "when row 180 and row 61 both verify individually",
        ),
        (
            "rear-view mirror of row 160's Handshake 3 meta → forest → power-law",
            "rear-view mirror of row 180's Handshake 3 meta prelude capstone → forest → power-law",
        ),
        (
            "when opening [row 162](preface.md#skill-navigation-row-162) before row 62 closes on the capstone path",
            "when opening [row 182](preface.md#skill-navigation-row-182) before row 62 closes on the capstone path",
        ),
        (
            "When row 161 is complete, proceed to [row 162]",
            "When row 181 is complete, proceed to [row 182]",
        ),
        (
            "When row 161 is complete, proceed to [row 162](preface.md#skill-navigation-row-162)",
            "When row 181 is complete, proceed to [row 182](preface.md#skill-navigation-row-182)",
        ),
        (
            "row 161 names **why that reunion must follow verified Handshake 3 meta prelude capstone (row 160)",
            "row 181 names **why that reunion must follow verified Handshake 4a meta prelude capstone (row 180)",
        ),
        ("Row 68 → Row 61 meta (row 161)", "Row 68 → Row 61 meta (row 181)"),
        (
            "When row 61 feels like epilogue homework after row 140 alone on the capstone path",
            "When row 61 feels like epilogue homework after row 180 alone on the capstone path",
        ),
        (
            "read row 68 + row 160 or row 141 gate",
            "read row 68 + row 180 or row 161 gate",
        ),
        (
            "When row 160 closed but row 61 Handshake 4a meta still feels",
            "When row 180 closed but row 61 Handshake 4a meta still feels",
        ),
        ("Row 68 → Row 141 reunion index", "Row 68 → Row 151 reunion index"),
        ("Row 68 → Row 141 Handshake 4a", "Row 68 → Row 151 Handshake 4a"),
    ]
    out = tx(s, p)
    out = out.replace(
        "__ROW161_HINGE__",
        "[row 161](preface.md#skill-navigation-row-161)",
    )
    out = re.sub(
        r"(### Row 181 skill checkpoint[^\n]*)\{#skill-navigation-row-161\}",
        r"\1{#skill-navigation-row-181}",
        out,
        count=1,
    )
    out = out.replace(
        "[row 140](preface.md#skill-navigation-row-140) or [row 141](preface.md#skill-navigation-row-141)",
        "[row 180](preface.md#skill-navigation-row-180) or [row 161](preface.md#skill-navigation-row-161)",
    )
    out = out.replace(
        "Do not conflate row 161 (row 68 ↔ row 61 reunion on the capstone path) with row 141 (opening-hinge prelude stitch alone)",
        "Do not conflate row 181 (row 68 ↔ row 61 reunion on the capstone path) with row 161 (opening-hinge prelude stitch alone)",
    )
    out = out.replace(
        "row 141 names **Row 68 → Row 141 Row 68 → Row 61 Handshake 4a meta prelude reunion**",
        "row 161 names **Row 68 → Row 141 Row 68 → Row 61 Handshake 4a meta prelude reunion**",
    )
    return out


def export_index_to_handshake4a_meta_181(block: str) -> str:
    pairs = [
        (
            "Handshake 4a meta prelude capstone reunion index (row 161)",
            "Handshake 4a meta prelude capstone reunion index (row 181)",
        ),
        ("row 60", "row 61"),
        ("Row 60", "Row 61"),
        ("VII.3 → Handshake 4a", "epilogue Handshake 4a meta"),
        ("row 178", "row 180"),
        ("Row 178", "Row 180"),
        ("row 180", "row 181"),
        ("Row 180", "Row 181"),
        ("skill-navigation-row-180", "skill-navigation-row-181"),
        ("row-180-baby-picture", "row-181-baby-picture"),
        (
            "row68-row151-handshake4a-meta-prelude-capstone-reunion-index-row-180",
            "row68-row151-handshake4a-meta-prelude-capstone-reunion-index-row-181",
        ),
    ]
    return lift_161_to_181(tx(block, pairs))


def insert_preface_row() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    if "### Row 181 skill checkpoint" in text:
        print("preface: row 181 already present")
        return
    m = re.search(
        r"(### Row 161 skill checkpoint.*?)(?=\n### Row 162 skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 161 checkpoint missing")
    block = lift_161_to_181(m.group(1))
    anchor = "\n### Row 180 skill checkpoint"
    idx = text.find(anchor)
    if idx < 0:
        raise SystemExit("row 180 anchor missing")
    text = text[:idx] + "\n" + block + text[idx:]
    path.write_text(text)
    print("preface: added row 181")


def insert_epilogue_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "### Row 181 closing loop" in text:
        print("epilogue: row 181 loop already present")
        return
    block = lift_161_to_181(
        extract_between(
            text,
            "### Row 161 closing loop",
            "### Row 160 closing loop",
        )
    )
    needle = "### Row 180 closing loop"
    text = text.replace(needle, block + needle, 1)
    path.write_text(text)
    print("epilogue: added row 181 loop")


def add_prologue_compass() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    compass = "| Row 68 → Row 151 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion (row 181) |"
    if compass in text:
        print("prologue: row 181 compass already present")
    else:
        after = "| Row 68 → Row 151 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion (row 180) |"
        idx = text.find(after)
        if idx < 0:
            raise SystemExit("prologue row 180 compass missing")
        line_end = text.find("\n", idx)
        src = "| Row 68 → Row 141 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion (row 161) |"
        sidx = text.find(src)
        if sidx < 0:
            raise SystemExit("prologue row 161 compass missing")
        new_line = lift_161_to_181(text[sidx : text.find("\n", sidx)]) + "\n"
        text = text[: line_end + 1] + new_line + text[line_end + 1 :]
    preview_src = '| <span id="prologue-preview-row-161"></span>'
    preview_dst = '| <span id="prologue-preview-row-181"></span>'
    if preview_src in text and preview_dst not in text:
        i = text.find(preview_src)
        j = text.find("\n|", i + 1)
        preview_block = lift_161_to_181(text[i:j]) + "\n"
        text = text.replace(preview_src, preview_block + preview_src, 1)
    if "**Row 181 closing stitch" not in text:
        stitch = (
            "**Row 181 closing stitch (Row 68 → Row 151 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion).** {#row-181-closing-stitch} "
            "When row 180 closed — Handshake 3 meta prelude capstone reunion verified, row 179 or row 180 recited on the capstone path, and [`parse_rate.sh`](../../scripts/parse_rate.sh) archived `rate_export.yaml` at lab grip rate — but **row 61 Handshake 4a meta reunion still opens like standalone epilogue coursework after the Handshake 4a chapter hinge on the capstone path** — "
            "the [preface row 181 When-to-pause opening sentence](../preface.md#skill-navigation-row-181) names the dual reunion before Handshake 4b meta prelude capstone reunion; "
            "read [preface row 181](../preface.md#skill-navigation-row-181), then the "
            "[Row 68 → Row 151 Handshake 4a meta prelude capstone reunion index](../appendix/sources.md#row68-row151-handshake4a-meta-prelude-capstone-reunion-index-row-181), then "
            "[epilogue row 181 closing loop](../epilogue/multiscale.md#row-181-closing-loop) before row 62 Handshake 4b meta prelude opens on the capstone path.\n\n"
        )
        text = text.replace("**Row 180 closing stitch", stitch + "**Row 180 closing stitch", 1)
    path.write_text(text)
    print("prologue: row 181 compass/preview/stitch")


def add_sources_row() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    idx_key = "row68-row151-handshake4a-meta-prelude-capstone-reunion-index-row-181"
    if idx_key in text:
        print("sources: row 181 already present")
        return
    epilogue = ROOT / "writings/epilogue/chapters/multiscale.md"
    seed = lift_161_to_181(
        extract_between(
            epilogue.read_text(),
            "### Row 161 closing loop",
            "### Row 160 closing loop",
        )
    )
    block = export_index_to_handshake4a_meta_181(seed)
    block = block.replace(
        "## Row 68 → Row 151 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 181)",
        f"## Row 68 → Row 151 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 181) {{#{idx_key}}}",
        1,
    )
    if f"{{#{idx_key}}}" not in block:
        block = (
            f"## Row 68 → Row 151 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 181) {{#{idx_key}}}\n\n"
            + block
        )
    table_row = (
        "| 181 | Row 68 → Row 151 Row 68 → Row 61 Handshake 4a meta prelude capstone "
        "(midpoint prelude gate ↔ Handshake 4a meta prelude capstone ↔ row 61 meta) | "
        f"[Row 68 → Row 151 Handshake 4a meta prelude capstone reunion index](#{idx_key}) · "
        "[preface row 181](../preface.md#skill-navigation-row-181) · "
        "[prologue row 181 preview](../prologue/00-many-scales.md#prologue-preview-row-181) · "
        "[prologue row 181 closing stitch](../prologue/00-many-scales.md#row-181-closing-stitch) · "
        "[epilogue row 181 closing loop](../epilogue/multiscale.md#row-181-closing-loop) · "
        "[memory sheet row 181 baby picture](memory-sheet.md#row-181-baby-picture-row68-row151-handshake4a-meta-prelude-capstone-reunion) | "
        "Row 68 closed but **row 61 Handshake 4a meta reunion still feels disconnected from verified Handshake 4a meta prelude capstone on the capstone path** — "
        "read row 68 + row 180 or row 161 gate + epilogue rate cross-links + row 61; "
        "[preface row 61](../preface.md#skill-navigation-row-61) |\n"
    )
    text = text.replace(
        "| 180 | Row 68 → Row 151 Row 68 → Row 60 Handshake 3 meta prelude capstone",
        table_row + "| 180 | Row 68 → Row 151 Row 68 → Row 60 Handshake 3 meta prelude capstone",
    )
    anchor = "row68-row151-handshake3-meta-prelude-capstone-reunion-index-row-180"
    if anchor not in text:
        text = block + "\n\n" + text
    else:
        text = text.replace(anchor, block + anchor, 1)
    path.write_text(text)
    print("sources: added row 181")


def add_memory_row() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    if "row-181-baby-picture-row68-row151-handshake4a-meta-prelude-capstone-reunion" in text:
        print("memory-sheet: row 181 already present")
        return
    baby = lift_161_to_181(
        extract_between(
            text,
            "### Row 161 baby picture",
            "### Row 162 baby picture",
        )
    )
    anchor = "### Row 161 baby picture"
    text = text.replace(anchor, baby + anchor, 1)
    mem_table = (
        "| 181 | Meta | Row 68 → Row 151 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion | "
        "[Row 68 → Row 151 Handshake 4a meta prelude capstone reunion index](sources.md#row68-row151-handshake4a-meta-prelude-capstone-reunion-index-row-181) · "
        "[preface row 181 skill checkpoint](../preface.md#skill-navigation-row-181) · "
        "[prologue row 181 preview](../prologue/00-many-scales.md#prologue-preview-row-181) · "
        "[prologue row 181 closing stitch](../prologue/00-many-scales.md#row-181-closing-stitch) · "
        "[epilogue row 181 closing loop](../epilogue/multiscale.md#row-181-closing-loop) | "
        "Row 68 closed but row 61 Handshake 4a meta reunion feels disconnected from verified Handshake 4a meta prelude capstone on the capstone path — "
        "read row 68 + row 180 or row 161 gate + epilogue rate cross-links + row 61; "
        "[row 181 baby picture](#row-181-baby-picture-row68-row151-handshake4a-meta-prelude-capstone-reunion) |\n"
    )
    text = text.replace(
        "| 180 | Meta | Row 68 → Row 151 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion |",
        mem_table + "| 180 | Meta | Row 68 → Row 151 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion |",
    )
    switch = (
        "When row 180 closed but Handshake 4a meta prelude capstone reunion still lags on the capstone path, switch to [row 181](#row-181-baby-picture-row68-row151-handshake4a-meta-prelude-capstone-reunion)."
    )
    if "When row 180 closed but Handshake 4a meta prelude capstone reunion still lags" not in text:
        text = text.replace(
            "When row 179 closed but Handshake 3 meta prelude capstone reunion still lags on the capstone path, switch to [row 180](#row-180-baby-picture-row68-row151-handshake3-meta-prelude-capstone-reunion).",
            "When row 179 closed but Handshake 3 meta prelude capstone reunion still lags on the capstone path, switch to [row 180](#row-180-baby-picture-row68-row151-handshake3-meta-prelude-capstone-reunion). "
            + switch,
        )
    path.write_text(text)
    print("memory-sheet: added row 181")


def patch_row_180_proceed_links() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    if "proceed to [row 181](preface.md#skill-navigation-row-181)" in text and "When row 180 is complete" in text:
        text = text.replace(
            "When row 180 is complete, proceed to [row 181](preface.md#skill-navigation-row-161)",
            "When row 180 is complete, proceed to [row 181](preface.md#skill-navigation-row-181)",
        )
        text = text.replace(
            "When row 180 is complete, proceed to [row 181](preface.md#skill-navigation-row-141)",
            "When row 180 is complete, proceed to [row 181](preface.md#skill-navigation-row-181)",
        )
    path.write_text(text)
    print("preface: patched row 180 → row 181 proceed hints")


def main() -> None:
    insert_preface_row()
    insert_epilogue_loop()
    add_prologue_compass()
    add_sources_row()
    add_memory_row()
    patch_row_180_proceed_links()


if __name__ == "__main__":
    main()
