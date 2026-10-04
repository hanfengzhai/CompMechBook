#!/usr/bin/env python3
"""Fix double-substitution artifacts from lift_124_to_144 and rebuild row 144 checkpoint."""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

spec = importlib.util.spec_from_file_location("add_row_144", ROOT / "scripts/add-row-144.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def polish_row_144_text(s: str) -> str:
    fixes = [
        ("Row 68 → Row 144 Row 68 → Row 64", "Row 68 → Row 124 Row 68 → Row 64"),
        ("Row 68 → Row 144 reunion", "Row 68 → Row 124 reunion"),
        (
            "[preface row 124 skill checkpoint](../preface.md#skill-navigation-row-144)",
            "[preface row 144 skill checkpoint](../preface.md#skill-navigation-row-144)",
        ),
        (
            "[Preface: row 124 skill checkpoint](../preface.md#skill-navigation-row-144)",
            "[Preface: row 144 skill checkpoint](../preface.md#skill-navigation-row-144)",
        ),
        (
            "[prologue row 124 preview row](#prologue-preview-row-144)",
            "[prologue row 144 preview row](#prologue-preview-row-144)",
        ),
        (
            "[prologue row 124 closing stitch](#row-144-closing-stitch)",
            "[prologue row 144 closing stitch](#row-144-closing-stitch)",
        ),
        (
            "[epilogue row 124 closing loop](../epilogue/multiscale.md#row-144-closing-loop)",
            "[epilogue row 144 closing loop](../epilogue/multiscale.md#row-144-closing-loop)",
        ),
        (
            "[row 143](preface.md#skill-navigation-row-123) or [row 124](preface.md#skill-navigation-row-104)",
            "[row 143](preface.md#skill-navigation-row-143) or [row 124](preface.md#skill-navigation-row-124)",
        ),
        (
            "Prologue preview ([row 124](prologue/00-many-scales.md#prologue-preview-row-144))",
            "Prologue preview ([row 144](prologue/00-many-scales.md#prologue-preview-row-144))",
        ),
        (
            "[Preface row 124](../preface.md#skill-navigation-row-144)",
            "[Preface row 144](../preface.md#skill-navigation-row-144)",
        ),
        (
            "Row 144 does not replace row 68, row 64, row 144, row 124",
            "Row 144 does not replace row 68, row 64, row 143, row 124",
        ),
        (
            "[row 143](#row68-row104-book-loop-meta-prelude-capstone-reunion-index-row-124) or [row 124](#row68-row124-book-loop-meta-prelude-capstone-reunion-index-row-144)",
            "[row 143](#row68-row123-orchestration-meta-prelude-capstone-reunion-index-row-143) or [row 124](#row68-row104-book-loop-meta-prelude-capstone-reunion-index-row-124)",
        ),
        (
            "[Row 124 reunion (meta prelude)](#row68-row124-book-loop-meta-prelude-capstone-reunion-index-row-144)",
            "[Row 124 reunion (opening-hinge capstone)](#row68-row104-book-loop-meta-prelude-capstone-reunion-index-row-124)",
        ),
        (
            "The [preface row 124 skill checkpoint](../preface.md#skill-navigation-row-144)",
            "The [preface row 144 skill checkpoint](../preface.md#skill-navigation-row-144)",
        ),
        (
            "When row 124 feels disconnected from row 143",
            "When row 144 feels disconnected from row 143",
        ),
        (
            "switch to [row 124](#row-144-baby-picture-row68-row124-book-loop-meta-prelude-capstone-reunion)",
            "switch to [row 144](#row-144-baby-picture-row68-row124-book-loop-meta-prelude-capstone-reunion)",
        ),
        (
            "[preface row 143](../preface.md#skill-navigation-row-123) or [preface row 124](../preface.md#skill-navigation-row-104)",
            "[preface row 143](../preface.md#skill-navigation-row-143) or [preface row 124](../preface.md#skill-navigation-row-124)",
        ),
        (
            "The [prologue row 124 preview](../prologue/00-many-scales.md#prologue-preview-row-144) and [prologue row 124 closing stitch](../prologue/00-many-scales.md#row-144-closing-stitch)",
            "The [prologue row 144 preview](../prologue/00-many-scales.md#prologue-preview-row-144) and [prologue row 144 closing stitch](../prologue/00-many-scales.md#row-144-closing-stitch)",
        ),
        (
            "return there when row 123 closed orchestration meta prelude capstone",
            "return there when row 143 closed orchestration meta prelude capstone on the capstone path",
        ),
        ("Row 124 closes the **book-loop meta prelude capstone", "Row 144 closes the **book-loop meta prelude capstone"),
        (
            "read row 68 gate + row 123 or row 124 orchestration meta prelude capstone",
            "read row 68 gate + row 143 or row 124 orchestration meta prelude capstone",
        ),
        (
            '"read row 68 gate + row 123 or row 124 orchestration meta prelude capstone',
            '"read row 68 gate + row 143 or row 124 orchestration meta prelude capstone',
        ),
        (
            "Prologue preview ([row 124](../prologue/00-many-scales.md#prologue-preview-row-144))",
            "Prologue preview ([row 144](../prologue/00-many-scales.md#prologue-preview-row-144))",
        ),
        (
            "When row 64 feels like epilogue homework after row 123 alone",
            "When row 64 feels like epilogue homework after row 143 alone on the capstone path",
        ),
        (
            "Recite [preface row 123](../preface.md#skill-navigation-row-123) to split orchestration meta prelude capstone",
            "Recite [preface row 143](../preface.md#skill-navigation-row-143) to split orchestration meta prelude capstone",
        ),
        (
            "matches the same restart contract per [row 104](../preface.md#skill-navigation-row-104)",
            "matches the same restart contract per [row 124](../preface.md#skill-navigation-row-124)",
        ),
    ]
    for a, b in fixes:
        s = s.replace(a, b)
    return s


def rebuild_row_144_preface(preface: str) -> str:
    m124 = re.search(
        r"(### Row 124 skill checkpoint.*?)(?=\n### Row 125 skill checkpoint)",
        preface,
        re.S,
    )
    if not m124:
        raise SystemExit("row 124 checkpoint missing")
    row144 = polish_row_144_text(mod.lift_124_to_144(m124.group(1)))
    row144 = re.sub(
        r"When row 144 is complete, proceed to.*?(?=or extend prose only under `writings/` then sync\.)",
        (
            "When row 144 is complete, proceed to [row 145](preface.md#skill-navigation-row-145) when row 68 closed but second-pass meta prelude still lags on the capstone path, "
            "to [row 125](preface.md#skill-navigation-row-125) when book-loop meta prelude capstone is clean but second-pass meta prelude still lags on the opening-hinge path, "
            "to [row 105](preface.md#skill-navigation-row-105) for the Row 68 ↔ Row 65 second-pass meta prelude audit alone, "
            "to [row 104](preface.md#skill-navigation-row-104) for the Row 68 ↔ Row 64 book-loop meta prelude audit on the opening-hinge path alone, "
            "to [row 143](preface.md#skill-navigation-row-143) when orchestration meta prelude capstone still lags after verified Handshake 4b meta prelude capstone on the capstone path, "
            "to [row 84](preface.md#skill-navigation-row-84) for the Row 68 ↔ Row 64 opening prelude audit alone, "
            "to [row 64](preface.md#skill-navigation-row-64) when only book-loop meta stalls, "
        ),
        row144,
        flags=re.S,
    )
    start = preface.find("\n### Row 144 skill checkpoint")
    end = preface.find("\n## The copper wire through the book", start)
    if start < 0 or end < 0:
        raise SystemExit("row 144 preface anchors missing")
    return preface[:start] + "\n" + row144 + preface[end:]


def add_row_143_closing_stitch(pro: str) -> str:
    if "row-143-closing-stitch" in pro and "**Row 143 closing stitch" in pro:
        return pro
    stitch = (
        "**Row 143 closing stitch (Row 68 → Row 123 Row 68 → Row 63 orchestration meta prelude capstone reunion).** {#row-143-closing-stitch} "
        "When row 142 closed — Handshake 4b meta prelude capstone verified, row 141 or row 122 recited on the capstone path, and "
        "[`parse_fe2.sh`](../../scripts/parse_fe2.sh) archived `fe2_export.yaml` with enrichment when uplift exceeds 10% after verified Handshake 4b meta prelude capstone — "
        "but **row 63 orchestration meta reunion still opens like standalone epilogue coursework after the orchestration opening prelude chapter hinge on the capstone path** — "
        "the [preface row 143 When-to-pause opening sentence](../preface.md#skill-navigation-row-143) names the dual reunion before book-loop meta prelude reunion; "
        "read [preface row 143](../preface.md#skill-navigation-row-143), then the "
        "[Row 68 → Row 123 reunion index](../appendix/sources.md#row68-row123-orchestration-meta-prelude-capstone-reunion-index-row-143), then "
        "[epilogue row 143 closing loop](../epilogue/multiscale.md#row-143-closing-loop) before row 64 book-loop meta prelude opens on the capstone path.\n\n"
    )
    return pro.replace("**Row 144 closing stitch", stitch + "**Row 144 closing stitch", 1)


def main() -> None:
    for rel in [
        "writings/prologue/chapters/00-many-scales.md",
        "writings/appendix/chapters/sources.md",
        "writings/appendix/chapters/memory-sheet.md",
    ]:
        path = ROOT / rel
        text = polish_row_144_text(path.read_text())
        path.write_text(text)
        print(f"polished: {rel}")

    pro_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    pro = add_row_143_closing_stitch(pro_path.read_text())
    pro_path.write_text(pro)
    print("prologue: ensured row 143 closing stitch")

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = polish_row_144_text(preface_path.read_text())
    if "### Row 144 skill checkpoint" in preface:
        preface_path.write_text(rebuild_row_144_preface(preface))
        print("preface: rebuilt row 144 checkpoint")
    else:
        preface_path.write_text(preface)

    ep_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep = polish_row_144_text(ep_path.read_text())
    if "### Row 144 closing loop" not in ep:
        block124 = mod.extract_between(ep, "### Row 124 closing loop", "### Row 125 closing loop")
        block144 = polish_row_144_text(mod.lift_124_to_144(block124))
        ep = ep.replace("### Row 124 closing loop", block144 + "### Row 124 closing loop", 1)
        print("epilogue: added row 144 closing loop")
    ep_path.write_text(ep)
    print("epilogue: polished row 144 loop")


if __name__ == "__main__":
    main()
