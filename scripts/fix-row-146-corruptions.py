#!/usr/bin/env python3
"""Fix double-substitution artifacts from lift_125_to_145 and rebuild row 145 checkpoint."""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

spec = importlib.util.spec_from_file_location("add_row_145", ROOT / "scripts/add-row-145.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def polish_row_145_text(s: str) -> str:
    fixes = [
        ("Row 68 → Row 145 Row 68 → Row 65", "Row 68 → Row 125 Row 68 → Row 65"),
        ("Row 68 → Row 145 reunion", "Row 68 → Row 125 reunion"),
        (
            "[preface row 125 skill checkpoint](../preface.md#skill-navigation-row-145)",
            "[preface row 145 skill checkpoint](../preface.md#skill-navigation-row-145)",
        ),
        (
            "[Preface: row 125 skill checkpoint](../preface.md#skill-navigation-row-145)",
            "[Preface: row 145 skill checkpoint](../preface.md#skill-navigation-row-145)",
        ),
        (
            "[prologue row 125 preview row](#prologue-preview-row-145)",
            "[prologue row 145 preview row](#prologue-preview-row-145)",
        ),
        (
            "[prologue row 125 closing stitch](#row-145-closing-stitch)",
            "[prologue row 145 closing stitch](#row-145-closing-stitch)",
        ),
        (
            "[epilogue row 125 closing loop](../epilogue/multiscale.md#row-145-closing-loop)",
            "[epilogue row 145 closing loop](../epilogue/multiscale.md#row-145-closing-loop)",
        ),
        (
            "[row 144](preface.md#skill-navigation-row-124) or [row 125](preface.md#skill-navigation-row-105)",
            "[row 144](preface.md#skill-navigation-row-144) or [row 125](preface.md#skill-navigation-row-125)",
        ),
        (
            "Prologue preview ([row 125](prologue/00-many-scales.md#prologue-preview-row-145))",
            "Prologue preview ([row 145](prologue/00-many-scales.md#prologue-preview-row-145))",
        ),
        (
            "[Preface row 125](../preface.md#skill-navigation-row-145)",
            "[Preface row 145](../preface.md#skill-navigation-row-145)",
        ),
        (
            "Row 145 does not replace row 68, row 65, row 145, row 125",
            "Row 145 does not replace row 68, row 65, row 144, row 125",
        ),
        (
            "[row 144](#row68-row104-book-loop-meta-prelude-capstone-reunion-index-row-124) or [row 125](#row68-row125-second-pass-meta-prelude-capstone-reunion-index-row-145)",
            "[row 144](#row68-row124-book-loop-meta-prelude-capstone-reunion-index-row-144) or [row 125](#row68-row105-second-pass-meta-prelude-capstone-reunion-index-row-125)",
        ),
        (
            "[Row 125 reunion (meta prelude)](#row68-row125-second-pass-meta-prelude-capstone-reunion-index-row-145)",
            "[Row 125 reunion (opening-hinge capstone)](#row68-row105-second-pass-meta-prelude-capstone-reunion-index-row-125)",
        ),
        (
            "The [preface row 125 skill checkpoint](../preface.md#skill-navigation-row-145)",
            "The [preface row 145 skill checkpoint](../preface.md#skill-navigation-row-145)",
        ),
        (
            "When row 125 feels disconnected from row 144",
            "When row 145 feels disconnected from row 144",
        ),
        (
            "switch to [row 125](#row-145-baby-picture-row68-row125-second-pass-meta-prelude-capstone-reunion)",
            "switch to [row 145](#row-145-baby-picture-row68-row125-second-pass-meta-prelude-capstone-reunion)",
        ),
        (
            "[preface row 144](../preface.md#skill-navigation-row-124) or [preface row 125](../preface.md#skill-navigation-row-105)",
            "[preface row 144](../preface.md#skill-navigation-row-144) or [preface row 125](../preface.md#skill-navigation-row-125)",
        ),
        (
            "The [prologue row 125 preview](../prologue/00-many-scales.md#prologue-preview-row-145) and [prologue row 125 closing stitch](../prologue/00-many-scales.md#row-145-closing-stitch)",
            "The [prologue row 145 preview](../prologue/00-many-scales.md#prologue-preview-row-145) and [prologue row 145 closing stitch](../prologue/00-many-scales.md#row-145-closing-stitch)",
        ),
        (
            "return there when row 144 closed book-loop meta prelude capstone",
            "return there when row 144 closed book-loop meta prelude capstone on the capstone path",
        ),
        ("Row 125 closes the **second-pass meta prelude capstone", "Row 145 closes the **second-pass meta prelude capstone"),
        (
            "read row 68 gate + row 144 or row 125 book-loop meta prelude capstone",
            "read row 68 gate + row 144 or row 125 book-loop meta prelude capstone",
        ),
        (
            "Prologue preview ([row 125](../prologue/00-many-scales.md#prologue-preview-row-145))",
            "Prologue preview ([row 145](../prologue/00-many-scales.md#prologue-preview-row-145))",
        ),
        (
            "When row 65 feels like appendix homework after row 124 alone",
            "When row 65 feels like appendix homework after row 144 alone on the capstone path",
        ),
        (
            "Recite [preface row 124](../preface.md#skill-navigation-row-124) to split book-loop meta prelude capstone",
            "Recite [preface row 144](../preface.md#skill-navigation-row-144) to split book-loop meta prelude capstone",
        ),
        (
            "matches the same novel-rhythm contract per [row 105](../preface.md#skill-navigation-row-105)",
            "matches the same novel-rhythm contract per [row 125](../preface.md#skill-navigation-row-125)",
        ),
        ("Book-loop meta prelude capstone row 124", "Book-loop meta prelude capstone row 144"),
    ]
    for a, b in fixes:
        s = s.replace(a, b)
    return s


def rebuild_row_145_preface(preface: str) -> str:
    m125 = re.search(
        r"(### Row 125 skill checkpoint.*?)(?=\n### Row 126 skill checkpoint)",
        preface,
        re.S,
    )
    if not m125:
        raise SystemExit("row 125 checkpoint missing")
    row145 = polish_row_145_text(mod.lift_125_to_145(m125.group(1)))
    row145 = re.sub(
        r"When row 145 is complete, proceed to.*?(?=or extend prose only under `writings/` then sync\.)",
        (
            "When row 145 is complete, proceed to [row 146](preface.md#skill-navigation-row-146) when row 68 closed but Writings canonical meta prelude still lags on the capstone path, "
            "to [row 126](preface.md#skill-navigation-row-126) when second-pass meta prelude capstone is clean but Writings canonical meta prelude still lags on the opening-hinge path, "
            "to [row 106](preface.md#skill-navigation-row-106) for the Row 68 ↔ Row 66 Writings meta prelude audit alone, "
            "to [row 105](preface.md#skill-navigation-row-105) for the Row 68 ↔ Row 65 second-pass meta prelude audit on the opening-hinge path alone, "
            "to [row 144](preface.md#skill-navigation-row-144) when book-loop meta prelude capstone still lags after verified orchestration meta prelude capstone on the capstone path, "
            "to [row 85](preface.md#skill-navigation-row-85) for the Row 68 ↔ Row 65 opening prelude audit alone, "
            "to [row 65](preface.md#skill-navigation-row-65) when only second-pass meta stalls, "
        ),
        row145,
        flags=re.S,
    )
    start = preface.find("\n### Row 145 skill checkpoint")
    end = preface.find("\n## The copper wire through the book", start)
    if start < 0 or end < 0:
        raise SystemExit("row 145 preface anchors missing")
    return preface[:start] + "\n" + row145 + preface[end:]


def add_row_144_closing_stitch(pro: str) -> str:
    if "row-144-closing-stitch" in pro and "**Row 144 closing stitch" in pro:
        return pro
    stitch = (
        "**Row 144 closing stitch (Row 68 → Row 124 Row 68 → Row 64 book-loop meta prelude capstone reunion).** {#row-144-closing-stitch} "
        "When row 143 closed — orchestration meta prelude capstone verified, row 142 or row 123 recited on the capstone path, and "
        "[`parse_multiscale_workflow.sh`](../../scripts/parse_multiscale_workflow.sh) archived `multiscale_export.yaml` with H1→H2→H3→H4a→H4b→OUT after verified Handshake 4b meta prelude capstone — "
        "but **row 64 book-loop meta reunion still opens like standalone epilogue coursework after the book-loop opening prelude chapter hinge on the capstone path** — "
        "the [preface row 144 When-to-pause opening sentence](../preface.md#skill-navigation-row-144) names the dual reunion before second-pass meta prelude reunion; "
        "read [preface row 144](../preface.md#skill-navigation-row-144), then the "
        "[Row 68 → Row 124 reunion index](../appendix/sources.md#row68-row124-book-loop-meta-prelude-capstone-reunion-index-row-144), then "
        "[epilogue row 144 closing loop](../epilogue/multiscale.md#row-144-closing-loop) before row 65 second-pass meta prelude opens on the capstone path.\n\n"
    )
    return pro.replace("**Row 145 closing stitch", stitch + "**Row 145 closing stitch", 1)


def main() -> None:
    for rel in [
        "writings/prologue/chapters/00-many-scales.md",
        "writings/appendix/chapters/sources.md",
        "writings/appendix/chapters/memory-sheet.md",
    ]:
        path = ROOT / rel
        text = polish_row_145_text(path.read_text())
        path.write_text(text)
        print(f"polished: {rel}")

    pro_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    pro = add_row_144_closing_stitch(pro_path.read_text())
    pro_path.write_text(pro)
    print("prologue: ensured row 144 closing stitch")

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = polish_row_145_text(preface_path.read_text())
    if "### Row 145 skill checkpoint" in preface:
        preface_path.write_text(rebuild_row_145_preface(preface))
        print("preface: rebuilt row 145 checkpoint")
    else:
        preface_path.write_text(preface)

    ep_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep = polish_row_145_text(ep_path.read_text())
    if "### Row 145 closing loop" not in ep:
        block125 = mod.extract_between(ep, "### Row 125 closing loop", "### Row 126 closing loop")
        block145 = polish_row_145_text(mod.lift_125_to_145(block125))
        ep = ep.replace("### Row 125 closing loop", block145 + "### Row 125 closing loop", 1)
        print("epilogue: added row 145 closing loop")
    ep_path.write_text(ep)
    print("epilogue: polished row 145 loop")


if __name__ == "__main__":
    main()
