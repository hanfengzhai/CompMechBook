#!/usr/bin/env python3
"""Fix double-substitution artifacts from lift_123_to_143 and rebuild row 143 checkpoint."""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

spec = importlib.util.spec_from_file_location("add_row_143", ROOT / "scripts/add-row-143.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def polish_row_143_text(s: str) -> str:
    fixes = [
        ("Row 68 → Row 143 Row 68 → Row 63", "Row 68 → Row 123 Row 68 → Row 63"),
        ("Row 68 → Row 143 reunion", "Row 68 → Row 123 reunion"),
        (
            "[preface row 123 skill checkpoint](../preface.md#skill-navigation-row-143)",
            "[preface row 143 skill checkpoint](../preface.md#skill-navigation-row-143)",
        ),
        (
            "[Preface: row 123 skill checkpoint](../preface.md#skill-navigation-row-143)",
            "[Preface: row 143 skill checkpoint](../preface.md#skill-navigation-row-143)",
        ),
        (
            "[prologue row 123 preview row](#prologue-preview-row-143)",
            "[prologue row 143 preview row](#prologue-preview-row-143)",
        ),
        (
            "[prologue row 123 closing stitch](#row-143-closing-stitch)",
            "[prologue row 143 closing stitch](#row-143-closing-stitch)",
        ),
        (
            "[epilogue row 123 closing loop](../epilogue/multiscale.md#row-143-closing-loop)",
            "[epilogue row 143 closing loop](../epilogue/multiscale.md#row-143-closing-loop)",
        ),
        (
            "[row 142](preface.md#skill-navigation-row-122) or [row 123](preface.md#skill-navigation-row-103)",
            "[row 142](preface.md#skill-navigation-row-142) or [row 123](preface.md#skill-navigation-row-123)",
        ),
        (
            "[row 142](preface.md#skill-navigation-row-122) or [Row 68 → Row 83 orchestration meta prelude reunion index (row 143)]",
            "[row 142](preface.md#skill-navigation-row-142) or [Row 68 → Row 123 orchestration meta prelude capstone reunion index (row 143)]",
        ),
        (
            "Row 68 → Row 83 orchestration meta prelude reunion index (row 143)",
            "Row 68 → Row 123 orchestration meta prelude capstone reunion index (row 143)",
        ),
        (
            "Prologue preview ([row 123](prologue/00-many-scales.md#prologue-preview-row-143))",
            "Prologue preview ([row 143](prologue/00-many-scales.md#prologue-preview-row-143))",
        ),
        (
            "[Preface row 123](../preface.md#skill-navigation-row-143)",
            "[Preface row 143](../preface.md#skill-navigation-row-143)",
        ),
        (
            "Row 143 does not replace row 68, row 63, row 143, row 123",
            "Row 143 does not replace row 68, row 63, row 142, row 123",
        ),
        (
            "[row 142](#row68-row102-handshake4b-meta-prelude-capstone-reunion-index-row-122) or [row 123](#row68-row123-orchestration-meta-prelude-capstone-reunion-index-row-143)",
            "[row 142](#row68-row122-handshake4b-meta-prelude-capstone-reunion-index-row-142) or [row 123](#row68-row103-orchestration-meta-prelude-capstone-reunion-index-row-123)",
        ),
        (
            "[Row 123 reunion (meta prelude)](#row68-row123-orchestration-meta-prelude-capstone-reunion-index-row-143)",
            "[Row 123 reunion (opening-hinge capstone)](#row68-row103-orchestration-meta-prelude-capstone-reunion-index-row-123)",
        ),
        (
            "The [preface row 123 skill checkpoint](../preface.md#skill-navigation-row-143)",
            "The [preface row 143 skill checkpoint](../preface.md#skill-navigation-row-143)",
        ),
        (
            "When row 123 feels disconnected from row 142",
            "When row 143 feels disconnected from row 142",
        ),
        (
            "switch to [row 123](#row-143-baby-picture-row68-row123-orchestration-meta-prelude-capstone-reunion)",
            "switch to [row 143](#row-143-baby-picture-row68-row123-orchestration-meta-prelude-capstone-reunion)",
        ),
        (
            "row 123 when **epilogue orchestration cross-links and Row 62 → Row 43 meta must read on the same wire before row 64 book-loop meta prelude opens on the capstone path**",
            "row 143 when **epilogue orchestration cross-links and Row 62 → Row 43 meta must read on the same wire before row 64 book-loop meta prelude opens on the capstone path**",
        ),
        (
            "[preface row 142](../preface.md#skill-navigation-row-122) or [preface row 123](../preface.md#skill-navigation-row-103)",
            "[preface row 142](../preface.md#skill-navigation-row-142) or [preface row 123](../preface.md#skill-navigation-row-123)",
        ),
    ]
    for a, b in fixes:
        s = s.replace(a, b)
    return s


def rebuild_row_143_preface(preface: str) -> str:
    m123 = re.search(
        r"(### Row 123 skill checkpoint.*?)(?=\n### Row 124 skill checkpoint)",
        preface,
        re.S,
    )
    if not m123:
        raise SystemExit("row 123 checkpoint missing")
    row143 = polish_row_143_text(mod.lift_123_to_143(m123.group(1)))
    row143 = re.sub(
        r"When row 143 is complete, proceed to.*?(?=or extend prose only under `writings/` then sync\.)",
        (
            "When row 143 is complete, proceed to [row 144](preface.md#skill-navigation-row-144) when row 68 closed but book-loop meta prelude still lags on the capstone path, "
            "to [row 124](preface.md#skill-navigation-row-124) when orchestration meta prelude capstone is clean but book-loop meta prelude still lags on the opening-hinge path, "
            "to [row 104](preface.md#skill-navigation-row-104) for the Row 68 ↔ Row 64 book-loop meta prelude audit alone, "
            "to [row 103](preface.md#skill-navigation-row-103) for the Row 68 ↔ Row 63 orchestration meta prelude audit on the opening-hinge path alone, "
            "to [row 142](preface.md#skill-navigation-row-142) when Handshake 4b meta prelude capstone still lags after verified Handshake 4a meta prelude capstone on the capstone path, "
            "to [row 83](preface.md#skill-navigation-row-83) for the Row 68 ↔ Row 63 opening prelude audit alone, "
            "to [row 63](preface.md#skill-navigation-row-63) when only orchestration meta stalls, "
        ),
        row143,
        flags=re.S,
    )
    start = preface.find("\n### Row 143 skill checkpoint")
    end = preface.find("\n## The copper wire through the book", start)
    if start < 0 or end < 0:
        raise SystemExit("row 143 preface anchors missing")
    return preface[:start] + "\n" + row143 + preface[end:]


def add_row_142_closing_stitch(pro: str) -> str:
    if "row-142-closing-stitch" in pro and "**Row 142 closing stitch" in pro:
        return pro
    stitch = (
        "**Row 142 closing stitch (Row 68 → Row 122 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion).** {#row-142-closing-stitch} "
        "When row 141 closed — Handshake 4a meta prelude capstone verified, row 140 or row 121 recited on the capstone path, and "
        "[`parse_rate.sh`](../../scripts/parse_rate.sh) archived `rate_export.yaml` with lab grip rate matching "
        "[`fixtures/cht_export.yaml`](../../fixtures/cht_export.yaml) at \\(T_w\\) after verified Handshake 4a meta prelude capstone — "
        "but **row 62 Handshake 4b meta reunion still opens like standalone epilogue coursework after the Handshake 4b opening prelude chapter hinge on the capstone path** — "
        "the [preface row 142 When-to-pause opening sentence](../preface.md#skill-navigation-row-142) names the dual reunion before orchestration meta prelude reunion; "
        "read [preface row 142](../preface.md#skill-navigation-row-142), then the "
        "[Row 68 → Row 122 reunion index](../appendix/sources.md#row68-row122-handshake4b-meta-prelude-capstone-reunion-index-row-142), then "
        "[epilogue row 142 closing loop](../epilogue/multiscale.md#row-142-closing-loop) before row 63 orchestration meta prelude opens on the capstone path.\n\n"
    )
    return pro.replace("**Row 143 closing stitch", stitch + "**Row 143 closing stitch", 1)


def main() -> None:
    for rel in [
        "writings/prologue/chapters/00-many-scales.md",
        "writings/appendix/chapters/sources.md",
        "writings/appendix/chapters/memory-sheet.md",
    ]:
        path = ROOT / rel
        text = polish_row_143_text(path.read_text())
        path.write_text(text)
        print(f"polished: {rel}")

    pro_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    pro = add_row_142_closing_stitch(pro_path.read_text())
    pro_path.write_text(pro)
    print("prologue: ensured row 142 closing stitch")

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = polish_row_143_text(preface_path.read_text())
    if "### Row 143 skill checkpoint" in preface:
        preface_path.write_text(rebuild_row_143_preface(preface))
        print("preface: rebuilt row 143 checkpoint")
    else:
        preface_path.write_text(preface)

    ep_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep = polish_row_143_text(ep_path.read_text())
    if "### Row 143 closing loop" not in ep:
        block123 = mod.extract_between(ep, "### Row 123 closing loop", "### Row 124 closing loop")
        block143 = polish_row_143_text(mod.lift_123_to_143(block123))
        ep = ep.replace("### Row 124 closing loop", block143 + "### Row 124 closing loop", 1)
        print("epilogue: added row 143 closing loop")
    ep_path.write_text(ep)
    print("epilogue: polished row 143 loop")


if __name__ == "__main__":
    main()
