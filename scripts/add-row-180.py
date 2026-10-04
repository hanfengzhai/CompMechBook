#!/usr/bin/env python3
"""Add row 180 (Row 68 → Row 151 ↔ Row 60 Handshake 3 meta prelude capstone on capstone path)."""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

_spec = importlib.util.spec_from_file_location("add_row_160_mod", ROOT / "scripts" / "add-row-160.py")
_mod = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_mod)
extract_between = _mod.extract_between
tx = _mod.tx


def lift_160_to_180(s: str) -> str:
    s = s.replace(
        "[row 140](preface.md#skill-navigation-row-140)",
        "__ROW140_HINGE__",
    )
    s = s.replace(
        "[row 159](preface.md#skill-navigation-row-159)",
        "__ROW179_GATE__",
    )
    p = [
        ("Row 161 closing loop", "__PH161_LOOP__"),
        ("Row 160 closing loop", "Row 180 closing loop"),
        ("row-161-closing-loop", "__PH161_LOOP_ANCHOR__"),
        ("row-160-closing-loop", "row-180-closing-loop"),
        ("Row 161 closing stitch", "__PH161_STITCH__"),
        ("Row 160 closing stitch", "Row 180 closing stitch"),
        ("row-161-closing-stitch", "__PH161_STITCH_ANCHOR__"),
        ("row-160-closing-stitch", "row-180-closing-stitch"),
        ("prologue-preview-row-161", "__PH161_PREVIEW__"),
        ("prologue-preview-row-160", "prologue-preview-row-180"),
        ("Row 161 preview", "__PH161_PREVIEW_TEXT__"),
        ("Row 160 preview", "Row 180 preview"),
        ("Row 161 skill checkpoint", "__PH161_SKILL__"),
        ("Row 160 skill checkpoint", "Row 180 skill checkpoint"),
        ("skill-navigation-row-161", "__PH161_SKILL_NAV__"),
        ("skill-navigation-row-160", "skill-navigation-row-180"),
        ("memory sheet row 161", "__PH161_MEM__"),
        ("memory sheet row 160", "memory sheet row 180"),
        ("Row 161 baby picture", "__PH161_BABY__"),
        ("Row 160 baby picture", "Row 180 baby picture"),
        ("Row 161 three-way audit", "__PH161_AUDIT__"),
        ("Row 160 three-way audit", "Row 180 three-way audit"),
        (
            "Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone",
            "Row 68 → Row 151 Row 68 → Row 60 Handshake 3 meta prelude capstone",
        ),
        (
            "row68-row140-handshake3-meta-prelude-capstone-reunion-index-row-160",
            "row68-row151-handshake3-meta-prelude-capstone-reunion-index-row-180",
        ),
        (
            "row-160-baby-picture-row68-row140-handshake3-meta-prelude-capstone-reunion",
            "row-180-baby-picture-row68-row151-handshake3-meta-prelude-capstone-reunion",
        ),
        ("[row 141]", "__ROW141_REF__"),
        ("[row 120]", "[row 140]"),
        ("row 120", "row 140"),
        ("Row 120", "Row 140"),
        ("__ROW179_GATE__", "[row 179](preface.md#skill-navigation-row-179)"),
        ("row 159", "row 179"),
        ("Row 159", "Row 179"),
        ("(row 160)", "(row 180)"),
        ("Row 160 closes the", "Row 180 closes the"),
        ("Row 160 does not conflate", "Row 180 does not conflate"),
        ("Row 160 does not replace", "Row 180 does not replace"),
        ("__PH161_LOOP__", "Row 161 closing loop"),
        ("__PH161_LOOP_ANCHOR__", "row-161-closing-loop"),
        ("__PH161_STITCH__", "Row 161 closing stitch"),
        ("__PH161_STITCH_ANCHOR__", "row-161-closing-stitch"),
        ("__PH161_PREVIEW__", "prologue-preview-row-161"),
        ("__PH161_PREVIEW_TEXT__", "Row 161 preview"),
        ("__PH161_SKILL__", "Row 161 skill checkpoint"),
        ("__PH161_SKILL_NAV__", "skill-navigation-row-161"),
        ("__PH161_MEM__", "memory sheet row 161"),
        ("__PH161_BABY__", "Row 161 baby picture"),
        ("__PH161_AUDIT__", "Row 161 three-way audit"),
        ("__ROW141_REF__", "[row 181]"),
        (
            "verified Handshake 3 meta prelude capstone closure (row 159)",
            "verified Handshake 3 meta prelude capstone closure (row 179)",
        ),
        (
            "when row 159 closed but row 60",
            "when row 179 closed but row 60",
        ),
        (
            "When row 159 closed — Handshake 3 meta prelude capstone verified",
            "When row 179 closed — Handshake 3 meta prelude capstone verified",
        ),
        (
            "when row 159 and row 60 both verify individually",
            "when row 179 and row 60 both verify individually",
        ),
        (
            "rear-view mirror of row 159's foundation archive",
            "rear-view mirror of row 179's foundation archive",
        ),
        (
            "when opening [row 161](preface.md#skill-navigation-row-161) before row 61 closes on the capstone path",
            "when opening [row 181](preface.md#skill-navigation-row-181) before row 61 closes on the capstone path",
        ),
        (
            "When row 160 is complete, proceed to [row 161]",
            "When row 180 is complete, proceed to [row 181]",
        ),
        (
            "When row 160 is complete, proceed to [row 161](preface.md#skill-navigation-row-161)",
            "When row 180 is complete, proceed to [row 181](preface.md#skill-navigation-row-181)",
        ),
        (
            "row 160 names **why that reunion must follow verified Handshake 3 meta prelude capstone (row 159)",
            "row 180 names **why that reunion must follow verified Handshake 3 meta prelude capstone (row 179)",
        ),
        ("Row 68 → Row 60 meta (row 160)", "Row 68 → Row 60 meta (row 180)"),
        (
            "When row 60 feels like epilogue homework after row 159 alone on the capstone path",
            "When row 60 feels like epilogue homework after row 179 alone on the capstone path",
        ),
        (
            "read row 68 + row 159 or row 140 gate",
            "read row 68 + row 179 or row 160 gate",
        ),
        (
            "When row 159 closed but Parts III–VI still lag",
            "When row 179 closed but Parts III–VI still lag",
        ),
    ]
    out = tx(s, p)
    out = out.replace(
        "__ROW140_HINGE__",
        "[row 160](preface.md#skill-navigation-row-160)",
    )
    out = re.sub(
        r"(### Row 180 skill checkpoint[^\n]*)\{#skill-navigation-row-160\}",
        r"\1{#skill-navigation-row-180}",
        out,
        count=1,
    )
    out = out.replace(
        "Do not conflate row 180 (row 68 ↔ row 60 reunion on the capstone path) with row 140 (opening-hinge prelude stitch alone)",
        "Do not conflate row 180 (row 68 ↔ row 60 reunion on the capstone path) with row 160 (opening-hinge prelude stitch alone)",
    )
    out = out.replace(
        "row 140 names **Row 68 → Row 80 Row 68 → Row 60 Handshake 3 meta prelude reunion**",
        "row 160 names **Row 68 → Row 100 Row 68 → Row 60 Handshake 3 meta prelude reunion**",
    )
    return out


def export_index_to_handshake3_meta_180(block: str) -> str:
    pairs = [
        (
            "Handshake 3 meta prelude capstone reunion index (row 160)",
            "Handshake 3 meta prelude capstone reunion index (row 180)",
        ),
        ("row 59", "row 60"),
        ("Row 59", "Row 60"),
        ("IX.3 → Handshake 3", "epilogue Handshake 3 meta"),
        ("opening hinge to Handshake 3", "epilogue opening hinge from IX.3"),
        ("foundation archive Lab act", "load-cell α export Lab act"),
        ("`foundation_export.yaml`", "`alpha_export.yaml`"),
        ("handbook \\alpha(300", "handbook default at load cell"),
        ("row 158", "row 178"),
        ("Row 158", "Row 178"),
        ("Kohn–Sham meta capstone", "Handshake 3 meta prelude capstone"),
        ("DFT workflows meta", "Handshake 3 meta prelude"),
        ("row 179", "row 180"),
        ("Row 179", "Row 180"),
        ("skill-navigation-row-179", "skill-navigation-row-180"),
        ("row-179-baby-picture", "row-180-baby-picture"),
        (
            "row68-row151-handshake3-meta-prelude-capstone-reunion-index-row-179",
            "row68-row151-handshake3-meta-prelude-capstone-reunion-index-row-180",
        ),
    ]
    return lift_160_to_180(tx(block, pairs))


def insert_preface_row() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    if "### Row 180 skill checkpoint" in text:
        print("preface: row 180 already present")
        return
    m = re.search(
        r"(### Row 160 skill checkpoint.*?)(?=\n### Row 161 skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 160 checkpoint missing")
    block = lift_160_to_180(m.group(1))
    anchor = "\n### Row 179 skill checkpoint"
    idx = text.find(anchor)
    if idx < 0:
        raise SystemExit("row 179 anchor missing")
    text = text[:idx] + "\n" + block + text[idx:]
    path.write_text(text)
    print("preface: added row 180")


def insert_epilogue_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "### Row 180 closing loop" in text:
        print("epilogue: row 180 loop already present")
        return
    block = lift_160_to_180(
        extract_between(
            text,
            "### Row 160 closing loop",
            "### Row 159 closing loop",
        )
    )
    needle = "### Row 179 closing loop"
    text = text.replace(needle, block + needle, 1)
    path.write_text(text)
    print("epilogue: added row 180 loop")


def add_prologue_compass() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    compass = "| Row 68 → Row 151 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion (row 180) |"
    if compass in text:
        print("prologue: row 180 compass already present")
    else:
        after = "| Row 68 → Row 151 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion (row 159) |"
        idx = text.find(after)
        if idx < 0:
            raise SystemExit("prologue row 179 compass missing")
        line_end = text.find("\n", idx)
        src = "| Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion (row 160) |"
        sidx = text.find(src)
        if sidx < 0:
            raise SystemExit("prologue row 160 compass missing")
        new_line = lift_160_to_180(text[sidx : text.find("\n", sidx)]) + "\n"
        text = text[: line_end + 1] + new_line + text[line_end + 1 :]
    preview_src = '| <span id="prologue-preview-row-160"></span>'
    preview_dst = '| <span id="prologue-preview-row-180"></span>'
    if preview_src in text and preview_dst not in text:
        i = text.find(preview_src)
        j = text.find("\n|", i + 1)
        preview_block = lift_160_to_180(text[i:j]) + "\n"
        text = text.replace(preview_src, preview_block + preview_src, 1)
    if "**Row 180 closing stitch" not in text:
        stitch = (
            "**Row 180 closing stitch (Row 68 → Row 151 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion).** {#row-180-closing-stitch} "
            "When row 179 closed — Handshake 3 meta prelude capstone verified, row 178 or row 179 recited on the capstone path, and [`parse_alpha.sh`](../../scripts/parse_alpha.sh) archived `alpha_export.yaml` at \\(T_w\\) — but **row 60 Handshake 3 meta reunion still opens like standalone epilogue coursework after the load-cell chapter hinge on the capstone path** — "
            "the [preface row 180 When-to-pause opening sentence](../preface.md#skill-navigation-row-180) names the dual reunion before the Handshake 4a meta prelude capstone reunion; "
            "read [preface row 180](../preface.md#skill-navigation-row-180), then the "
            "[Row 68 → Row 151 Handshake 3 meta prelude capstone reunion index](../appendix/sources.md#row68-row151-handshake3-meta-prelude-capstone-reunion-index-row-180), then "
            "[epilogue row 180 closing loop](../epilogue/multiscale.md#row-180-closing-loop) before row 61 Handshake 4a meta prelude opens on the capstone path.\n\n"
        )
        text = text.replace("**Row 179 closing stitch", stitch + "**Row 179 closing stitch", 1)
    path.write_text(text)
    print("prologue: row 180 compass/preview/stitch")


def add_sources_row() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    idx_key = "row68-row151-handshake3-meta-prelude-capstone-reunion-index-row-180"
    if idx_key in text:
        print("sources: row 180 already present")
        return
    start179 = "row68-row151-handshake3-meta-prelude-capstone-reunion-index-row-179"
    i = text.find(start179)
    if i < 0:
        raise SystemExit("sources row 179 index missing")
    i = text.rfind("\n## ", 0, i)
    if i < 0:
        i = text.rfind("\nrow68-row151-handshake3", 0, text.find(start179))
    j179 = text.find(start179, i)
    block = export_index_to_handshake3_meta_180(
        lift_160_to_180(text[i:j179] if i >= 0 and j179 > i else text[j179 : j179 + 4000])
    )
    block = block.replace(
        "## Row 68 → Row 151 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 180)",
        f"## Row 68 → Row 151 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 180) {{#{idx_key}}}",
        1,
    )
    if f"{{#{idx_key}}}" not in block:
        block = (
            f"## Row 68 → Row 151 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 180) {{#{idx_key}}}\n\n"
            + block
        )
    table_row = (
        "| 180 | Row 68 → Row 151 Row 68 → Row 60 Handshake 3 meta prelude capstone "
        "(midpoint prelude gate ↔ Handshake 3 meta prelude capstone ↔ row 60 meta) | "
        f"[Row 68 → Row 151 Handshake 3 meta prelude capstone reunion index](#{idx_key}) · "
        "[preface row 180](../preface.md#skill-navigation-row-180) · "
        "[prologue row 180 preview](../prologue/00-many-scales.md#prologue-preview-row-180) · "
        "[prologue row 180 closing stitch](../prologue/00-many-scales.md#row-180-closing-stitch) · "
        "[epilogue row 180 closing loop](../epilogue/multiscale.md#row-180-closing-loop) · "
        "[memory sheet row 180 baby picture](memory-sheet.md#row-180-baby-picture-row68-row151-handshake3-meta-prelude-capstone-reunion) | "
        "Row 68 closed but **row 60 Handshake 3 meta reunion still feels disconnected from verified Handshake 3 meta prelude capstone on the capstone path** — "
        "read row 68 + row 179 or row 160 gate + epilogue α cross-links + row 60; "
        "[preface row 60](../preface.md#skill-navigation-row-60) |\n"
    )
    text = text.replace(
        "| 179 | Row 68 → Row 151 Row 68 → Row 59 Handshake 3 meta prelude capstone",
        table_row + "| 179 | Row 68 → Row 151 Row 68 → Row 59 Handshake 3 meta prelude capstone",
    )
    text = text.replace(start179, block + start179, 1)
    path.write_text(text)
    print("sources: added row 180")


def add_memory_row() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    if "row-180-baby-picture-row68-row151-handshake3-meta-prelude-capstone-reunion" in text:
        print("memory-sheet: row 180 already present")
        return
    baby = lift_160_to_180(
        extract_between(
            text,
            "### Row 160 baby picture",
            "### Row 161 baby picture",
        )
    )
    anchor = "### Row 160 baby picture"
    text = text.replace(anchor, baby + anchor, 1)
    mem_table = (
        "| 180 | Meta | Row 68 → Row 151 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion | "
        "[Row 68 → Row 151 Handshake 3 meta prelude capstone reunion index](sources.md#row68-row151-handshake3-meta-prelude-capstone-reunion-index-row-180) · "
        "[preface row 180 skill checkpoint](../preface.md#skill-navigation-row-180) · "
        "[prologue row 180 preview](../prologue/00-many-scales.md#prologue-preview-row-180) · "
        "[prologue row 180 closing stitch](../prologue/00-many-scales.md#row-180-closing-stitch) · "
        "[epilogue row 180 closing loop](../epilogue/multiscale.md#row-180-closing-loop) | "
        "Row 68 closed but row 60 Handshake 3 meta reunion feels disconnected from verified Handshake 3 meta prelude capstone on the capstone path — "
        "read row 68 + row 179 or row 160 gate + epilogue α cross-links + row 60; "
        "[row 180 baby picture](#row-180-baby-picture-row68-row151-handshake3-meta-prelude-capstone-reunion) |\n"
    )
    text = text.replace(
        "| 179 | Meta | Row 68 → Row 151 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion |",
        mem_table + "| 179 | Meta | Row 68 → Row 151 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion |",
    )
    if "When row 179 closed but Handshake 3 meta prelude capstone reunion still lags" not in text:
        text = text.replace(
            "When row 178 closed but Handshake 3 meta reunion still lags on the capstone path, switch to [row 179](#row-179-baby-picture-row68-row151-handshake3-meta-prelude-capstone-reunion).",
            "When row 178 closed but Handshake 3 meta reunion still lags on the capstone path, switch to [row 179](#row-179-baby-picture-row68-row151-handshake3-meta-prelude-capstone-reunion). "
            "When row 179 closed but Handshake 3 meta prelude capstone reunion still lags on the capstone path, switch to [row 180](#row-180-baby-picture-row68-row151-handshake3-meta-prelude-capstone-reunion).",
        )
    path.write_text(text)
    print("memory-sheet: added row 180")


def patch_row_179_proceed_links() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    if "proceed to [row 180](preface.md#skill-navigation-row-180)" not in text:
        text = text.replace(
            "when opening [row 160](preface.md#skill-navigation-row-160) before row 60 closes on the capstone path",
            "when opening [row 180](preface.md#skill-navigation-row-180) before row 61 closes on the capstone path",
            1,
        )
        text = text.replace(
            "When row 159 is complete, proceed to [row 160](preface.md#skill-navigation-row-160) when load cell parses",
            "When row 179 is complete, proceed to [row 180](preface.md#skill-navigation-row-180) when load cell parses",
            1,
        )
    path.write_text(text)
    print("preface: patched row 179 → row 180 proceed hints")


def main() -> None:
    insert_preface_row()
    insert_epilogue_loop()
    add_prologue_compass()
    add_sources_row()
    add_memory_row()
    patch_row_179_proceed_links()


if __name__ == "__main__":
    main()
