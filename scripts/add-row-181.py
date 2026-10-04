#!/usr/bin/env python3
"""Add row 181 (Row 68 → Row 151 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion)."""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

_spec = importlib.util.spec_from_file_location(
    "add_row_160_mod", ROOT / "scripts" / "add-row-160.py"
)
_mod = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_mod)
extract_between = _mod.extract_between
tx = _mod.tx


def lift_161_to_181(s: str) -> str:
    s = s.replace("[row 180](preface.md#skill-navigation-row-181)", "[row 180](preface.md#skill-navigation-row-180)")
    s = s.replace("[row 161](preface.md#skill-navigation-row-162)", "[row 161](preface.md#skill-navigation-row-161)")
    s = s.replace(
        "[row 151](prologue/00-many-scales.md#prologue-preview-row-162)",
        "__ROW161_PREVIEW__",
    )
    pairs = [
        ("Row 162 closing loop", "__ROW161_LOOP__"),
        ("Row 181 closing loop", "__ROW180_LOOP__"),
        ("Row 161 closing loop", "Row 181 closing loop"),
        ("row-162-closing-loop", "__ROW161_LOOP_ANCHOR__"),
        ("row-181-closing-loop", "__ROW180_LOOP_ANCHOR__"),
        ("row-161-closing-loop", "row-181-closing-loop"),
        ("Row 162 closing stitch", "__ROW161_STITCH__"),
        ("Row 181 closing stitch", "__ROW180_STITCH__"),
        ("Row 161 closing stitch", "Row 181 closing stitch"),
        ("row-162-closing-stitch", "__ROW161_STITCH_ANCHOR__"),
        ("row-181-closing-stitch", "__ROW180_STITCH_ANCHOR__"),
        ("row-161-closing-stitch", "row-181-closing-stitch"),
        ("prologue-preview-row-162", "__ROW161_PREVIEW__"),
        ("prologue-preview-row-181", "__ROW180_PREVIEW__"),
        ("prologue-preview-row-161", "prologue-preview-row-181"),
        ("Row 162 preview", "__ROW161_PREVIEW_TEXT__"),
        ("Row 181 preview", "__ROW180_PREVIEW_TEXT__"),
        ("Row 161 preview", "Row 181 preview"),
        ("Row 162 skill checkpoint", "__ROW161_SKILL__"),
        ("Row 181 skill checkpoint", "__ROW180_SKILL__"),
        ("Row 161 skill checkpoint", "Row 181 skill checkpoint"),
        ("skill-navigation-row-162", "__ROW161_SKILL_NAV__"),
        ("skill-navigation-row-181", "__ROW180_SKILL_NAV__"),
        ("skill-navigation-row-161", "skill-navigation-row-181"),
        ("memory sheet row 162", "__ROW161_MEM__"),
        ("memory sheet row 181", "__ROW180_MEM__"),
        ("memory sheet row 161", "memory sheet row 181"),
        ("Row 162 baby picture", "__ROW161_BABY__"),
        ("Row 181 baby picture", "__ROW180_BABY__"),
        ("Row 161 baby picture", "Row 181 baby picture"),
        ("Row 162 three-way audit", "__ROW161_AUDIT__"),
        ("Row 181 three-way audit", "__ROW180_AUDIT__"),
        ("Row 161 three-way audit", "Row 181 three-way audit"),
        (
            "Row 68 → Row 140 Row 68 → Row 61 Handshake 4a meta prelude capstone",
            "Row 68 → Row 151 Row 68 → Row 61 Handshake 4a meta prelude capstone",
        ),
        (
            "row68-row140-handshake4a-meta-prelude-capstone-reunion-index-row-160",
            "row68-row151-handshake4a-meta-prelude-capstone-reunion-index-row-180",
        ),
        (
            "row-160-baby-picture-row68-row140-handshake4a-meta-prelude-capstone-reunion",
            "row-180-baby-picture-row68-row151-handshake4a-meta-prelude-capstone-reunion",
        ),
        ("[row 161]", "__ROW161_REF__"),
        ("[row 141]", "[row 161]"),
        ("row 141", "row 161"),
        ("Row 141", "Row 161"),
        ("__ROW161_REF__", "[row 161]"),
        ("[row 179]", "__ROW159_REF__"),
        ("[row 180]", "__ROW179_REF__"),
        ("[row 140]", "[row 151]"),
        ("row 140", "row 151"),
        ("Row 140", "Row 151"),
        ("__ROW159_REF__", "[row 180]"),
        ("row 179", "row 180"),
        ("Row 179", "Row 180"),
        ("__ROW179_REF__", "[row 180]"),
        ("[row 120]", "[row 140]"),
        ("row 120", "row 140"),
        ("Row 120", "Row 140"),
        ("[row 100]", "[row 120]"),
        ("row 100", "row 120"),
        ("Row 100", "Row 120"),
        ("(row 161)", "(row 181)"),
        ("__ROW161_LOOP__", "Row 162 closing loop"),
        ("__ROW161_LOOP_ANCHOR__", "row-162-closing-loop"),
        ("__ROW180_LOOP__", "Row 181 closing loop"),
        ("__ROW180_LOOP_ANCHOR__", "row-181-closing-loop"),
        ("__ROW161_STITCH__", "Row 162 closing stitch"),
        ("__ROW161_STITCH_ANCHOR__", "row-162-closing-stitch"),
        ("__ROW180_STITCH__", "Row 181 closing stitch"),
        ("__ROW180_STITCH_ANCHOR__", "row-181-closing-stitch"),
        ("__ROW161_PREVIEW__", "prologue-preview-row-162"),
        ("__ROW180_PREVIEW__", "prologue-preview-row-181"),
        ("__ROW161_PREVIEW_TEXT__", "Row 162 preview"),
        ("__ROW180_PREVIEW_TEXT__", "Row 181 preview"),
        ("__ROW161_SKILL__", "Row 162 skill checkpoint"),
        ("__ROW180_SKILL__", "Row 181 skill checkpoint"),
        ("__ROW161_SKILL_NAV__", "skill-navigation-row-162"),
        ("__ROW180_SKILL_NAV__", "skill-navigation-row-181"),
        ("__ROW161_MEM__", "memory sheet row 162"),
        ("__ROW180_MEM__", "memory sheet row 181"),
        ("__ROW161_BABY__", "Row 162 baby picture"),
        ("__ROW180_BABY__", "Row 181 baby picture"),
        ("__ROW161_AUDIT__", "Row 162 three-way audit"),
        ("__ROW180_AUDIT__", "Row 181 three-way audit"),
        (
            "verified Handshake 3 meta prelude capstone closure (row 180)",
            "verified Handshake 4a meta prelude capstone closure (row 180)",
        ),
        (
            "When row 160 is complete, proceed to [row 161]",
            "When row 181 is complete, proceed to [row 182]",
        ),
        (
            "when opening [row 161](preface.md#skill-navigation-row-162) before row 61 closes",
            "when opening [row 182](preface.md#skill-navigation-row-182) before row 62 closes",
        ),
        (
            "Row 68 → Row 140 Handshake 4a meta prelude capstone reunion index (row 161)",
            "Row 68 → Row 151 Handshake 4a meta prelude capstone reunion index (row 181)",
        ),
        (
            "Row 68 → Row 140 Handshake 4a meta prelude reunion index (row 161)",
            "Row 68 → Row 151 Handshake 4a meta prelude capstone reunion index (row 181)",
        ),
        (
            "Row 68 → Row 140 reunion index",
            "Row 68 → Row 151 reunion index",
        ),
        (
            "row 160 names **why that reunion must follow verified Handshake 4a meta prelude capstone (row 179)",
            "row 180 names **why that reunion must follow verified Handshake 4a meta prelude capstone (row 180)",
        ),
        (
            "When row 179 closed — Handshake 4a meta prelude capstone verified, row 158 or row 139 recited",
            "When row 180 closed — Handshake 4a meta prelude capstone verified, row 158 or row 158 recited",
        ),
        (
            "when row 179 closed but row 61",
            "when row 180 closed but row 61",
        ),
        (
            "when row 179 and row 61 both verify individually",
            "when row 180 and row 61 both verify individually",
        ),
        (
            "rear-view mirror of row 179's foundation archive",
            "rear-view mirror of row 180's foundation archive",
        ),
        (
            "Do not conflate row 160 (row 68 ↔ row 61 reunion on the capstone path) with row 140 (opening-hinge prelude stitch alone)",
            "Do not conflate row 180 (row 68 ↔ row 61 reunion on the capstone path) with row 151 (opening-hinge prelude stitch alone)",
        ),
        (
            "Row 160 does not replace row 68, row 61, row 179, row 140, row 120, row 80, row 59, or row 40",
            "Row 181 does not replace row 68, row 61, row 180, row 151, row 140, row 100, row 59, or row 40",
        ),
        (
            "When row 160 is complete, proceed to [row 161](preface.md#skill-navigation-row-162) when row 68 closed but Handshake 4a meta prelude still lags on the capstone path, to [row 141](preface.md#skill-navigation-row-141) when Handshake 4a meta prelude capstone is clean but Handshake 4a meta prelude still lags on the opening-hinge path, to [row 101](preface.md#skill-navigation-row-101) for the Row 68 ↔ Row 61 Handshake 4a meta prelude audit alone, to [row 140](preface.md#skill-navigation-row-140) for the Row 68 ↔ Row 61 Handshake 4a meta prelude audit on the opening-hinge path alone, to [row 179](preface.md#skill-navigation-row-159) when Handshake 4a meta prelude capstone still lags after verified DFT workflows meta prelude capstone on the capstone path, to [row 61](preface.md#skill-navigation-row-60) when only Handshake 4a meta stalls, or extend prose only under `writings/` then sync.",
            "When row 181 is complete, proceed to [row 182](preface.md#skill-navigation-row-181) when row 68 closed but Handshake 4a meta prelude still lags on the capstone path, to [row 161](preface.md#skill-navigation-row-162) when Handshake 4a meta prelude capstone is clean but Handshake 4a meta prelude still lags on the opening-hinge path, to [row 101](preface.md#skill-navigation-row-101) for the Row 68 ↔ Row 61 Handshake 4a meta prelude audit alone, to [row 161](preface.md#skill-navigation-row-162) for the Row 68 ↔ Row 61 Handshake 4a meta prelude audit on the opening-hinge path alone, to [row 180](preface.md#skill-navigation-row-181) when Handshake 4a meta prelude capstone still lags after verified DFT workflows meta prelude capstone on the capstone path, to [row 61](preface.md#skill-navigation-row-60) when only Handshake 4a meta stalls, or extend prose only under `writings/` then sync.",
        ),
        (
            "read [preface row 160](../preface.md#skill-navigation-row-161)",
            "read [preface row 180](../preface.md#skill-navigation-row-181)",
        ),
        (
            "prologue row 160 closing stitch",
            "prologue row 180 closing stitch",
        ),
        (
            "epilogue row 160 closing loop",
            "epilogue row 180 closing loop",
        ),
        (
            "before row 61 Handshake 4a meta prelude opens on the capstone path",
            "before row 62 Handshake 4b meta prelude capstone opens on the capstone path",
        ),
        ("prologue row 160 preview", "prologue row 180 preview"),
        ("Preface row 160", "Preface row 180"),
        ("Row 160 closes the", "Row 180 closes the"),
        ("Row 160 does not replace", "Row 180 does not replace"),
    ]
    s = tx(s, pairs)
    s = s.replace("[row 180](preface.md#skill-navigation-row-180)", "[row 180](preface.md#skill-navigation-row-181)")
    s = s.replace("[row 161](preface.md#skill-navigation-row-161)", "[row 161](preface.md#skill-navigation-row-162)")
    s = s.replace(
        "__ROW161_PREVIEW__",
        "[row 151](prologue/00-many-scales.md#prologue-preview-row-162)",
    )
    s = s.replace(
        "When row 181 is complete, proceed to [row 182]",
        "When row 181 is complete, proceed to [row 182](preface.md#skill-navigation-row-181)",
    )
    s = s.replace(
        "([row 151](prologue/00-many-scales.md#prologue-preview-row-181))",
        "([row 180](prologue/00-many-scales.md#prologue-preview-row-181))",
    )
    return s


def export_index_to_handshake4a_181(block: str) -> str:
    return lift_161_to_181(block)


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
    compass = "| Row 68 → Row 151 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion (row 180) |"
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
            "**Row 181 closing stitch (Row 68 → Row 151 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion).** {#row-181-closing-stitch} "
            "When row 179 closed — Handshake 3 meta prelude capstone verified, row 178 or row 158 recited on the capstone path, and [`parse_alpha.sh`](../../scripts/parse_alpha.sh) archived `alpha_export.yaml` at \\(T_w\\) — but **row 60 Handshake 3 meta reunion still opens like standalone epilogue coursework after the load-cell chapter hinge on the capstone path** — "
            "the [preface row 180 When-to-pause opening sentence](../preface.md#skill-navigation-row-180) names the dual reunion before the Handshake 4a meta prelude capstone reunion; "
            "read [preface row 180](../preface.md#skill-navigation-row-180), the "
            "[Row 68 → Row 151 reunion index](../appendix/sources.md#row68-row151-handshake4a-meta-prelude-capstone-reunion-index-row-181), and "
            "[epilogue row 180 closing loop](../epilogue/multiscale.md#row-180-closing-loop) before row 62 Handshake 4a meta prelude capstone opens on the capstone path.\n\n"
        )
        text = text.replace("**Row 180 closing stitch", stitch + "**Row 180 closing stitch", 1)
    path.write_text(text)
    print("prologue: row 181 compass/preview/stitch")


def add_sources_row() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    idx_key = "row68-row151-handshake4a-meta-prelude-capstone-reunion-index-row-181"
    if idx_key in text:
        print("sources: row 180 already present")
        return
    mem = (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text()
    src_anchor = "{#row-140-baby-picture-row68-row120-handshake3-meta-prelude-capstone-reunion}"
    end_anchor = "{#row-140-baby-picture-row68-row120-handshake3-meta-prelude-capstone-reunion}"
    i = mem.find(src_anchor)
    if i < 0:
        raise SystemExit("memory row 140 baby picture anchor missing")
    i = mem.rfind("### Row 140 baby picture", 0, i)
    j = mem.find("\n\n### ", i + 10)
    baby140 = mem[i:j]
    block = (
        f"\n\n## Row 68 → Row 151 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 180) {{#{idx_key}}}\n\n"
        + export_index_to_handshake4a_181(baby140).lstrip()
    )
    insert_at = text.find("\n\nrow68-row151-handshake3-meta-prelude-capstone-reunion-index-row-179}")
    if insert_at < 0:
        insert_at = text.find(start179 := "row68-row151-handshake3-meta-prelude-capstone-reunion-index-row-179")
        if insert_at < 0:
            raise SystemExit("sources row 179 index missing")
        text = text[:insert_at] + block + "\n\n" + text[insert_at:]
    else:
        text = text[:insert_at] + block + text[insert_at:]
    path.write_text(text)
    print("sources: added row 180")


def add_memory_row() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    anchor_id = "row-180-baby-picture-row68-row151-handshake3-meta-prelude-capstone-reunion"
    if anchor_id in text:
        print("memory-sheet: row 180 already present")
        return
    src = "{#row-140-baby-picture-row68-row120-handshake3-meta-prelude-capstone-reunion}"
    i = text.find(src)
    if i < 0:
        raise SystemExit("memory row 140 baby picture anchor missing")
    i = text.rfind("### Row 140 baby picture", 0, i)
    j = text.find("\n\n### ", i + 10)
    baby = lift_161_to_181(text[i:j]) + "\n\n"
    insert = text.find("### Row 179 baby picture (Row 68 → Row 151 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion) {#row-179-baby-picture-row68-row151-handshake3-meta-prelude-capstone-reunion}")
    if insert < 0:
        raise SystemExit("memory row 179 baby picture anchor missing")
    text = text[:insert] + baby + text[insert:]
    mem_table = (
        "| 180 | Meta | Row 68 → Row 151 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion | "
        "[Row 68 → Row 151 Handshake 3 meta prelude capstone reunion index](sources.md#row68-row151-handshake4a-meta-prelude-capstone-reunion-index-row-181) · "
        "[preface row 180 skill checkpoint](../preface.md#skill-navigation-row-180) · "
        "[prologue row 180 preview](../prologue/00-many-scales.md#prologue-preview-row-181) · "
        "[prologue row 180 closing stitch](../prologue/00-many-scales.md#row-181-closing-stitch) · "
        "[epilogue row 180 closing loop](../epilogue/multiscale.md#row-180-closing-loop) | "
        "Row 68 closed but row 60 Handshake 3 meta reunion feels disconnected from verified Handshake 3 meta prelude capstone on the capstone path — "
        "read row 68 + row 179 or row 151 gate + epilogue α cross-links + row 60; "
        "[row 180 baby picture](#row-180-baby-picture-row68-row151-handshake3-meta-prelude-capstone-reunion) |\n"
    )
    text = text.replace(
        "| 179 | Meta | Row 68 → Row 151 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion |",
        mem_table + "| 179 | Meta | Row 68 → Row 151 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion |",
    )
    if "When row 179 closed but Handshake 3 meta reunion still lags" not in text:
        text = text.replace(
            "When row 178 closed but Handshake 3 meta reunion still lags on the capstone path, switch to [row 179](#row-179-baby-picture-row68-row151-handshake3-meta-prelude-capstone-reunion).",
            "When row 178 closed but Handshake 3 meta reunion still lags on the capstone path, switch to [row 179](#row-179-baby-picture-row68-row151-handshake3-meta-prelude-capstone-reunion). "
            "When row 179 closed but Handshake 3 meta reunion still lags on the capstone path, switch to [row 180](#row-180-baby-picture-row68-row151-handshake3-meta-prelude-capstone-reunion).",
        )
    path.write_text(text)
    print("memory-sheet: added row 180")


def patch_row_180_proceed_links() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    if "proceed to [row 181](preface.md#skill-navigation-row-181)" in text:
        print("preface: row 180 proceed hints already patched")
        return
    text = text.replace(
        "when opening [row 160](preface.md#skill-navigation-row-160) before row 60 closes on the capstone path",
        "when opening [row 181](preface.md#skill-navigation-row-181) before row 61 closes on the capstone path",
    )
    text = text.replace(
        "When row 179 is complete, proceed to [row 160]",
        "When row 179 is complete, proceed to [row 181](preface.md#skill-navigation-row-181)",
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
