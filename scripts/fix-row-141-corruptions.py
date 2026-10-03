#!/usr/bin/env python3
"""Fix double-substitution artifacts from lift_121_to_141 and rebuild row 141 checkpoint."""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

spec = importlib.util.spec_from_file_location("add_row_141", ROOT / "scripts/add-row-141.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def polish_row_141_text(s: str) -> str:
    fixes = [
        ("Row 68 → Row 141 Row 68 → Row 61", "Row 68 → Row 121 Row 68 → Row 61"),
        ("Row 68 → Row 141 Handshake", "Row 68 → Row 121 Handshake"),
        ("row 140 or row 141 closed Handshake", "row 140 or row 121 closed Handshake"),
        ("row 140 or row 141 Handshake", "row 140 or row 121 Handshake"),
        ("preface.md#skill-navigation-row-120)", "preface.md#skill-navigation-row-140)"),
        ("preface.md#skill-navigation-row-101)", "preface.md#skill-navigation-row-121)"),
        (
            "Row 68 → Row 141 Handshake 4a meta prelude reunion index (row 141)",
            "Row 68 → Row 121 Handshake 4a meta prelude reunion index (row 121)",
        ),
        (
            "appendix/sources.md#row68-row101-handshake4a-meta-prelude-capstone-reunion-index-row-121)",
            "appendix/sources.md#row68-row121-handshake4a-meta-prelude-capstone-reunion-index-row-141)",
        ),
        (
            "Row 141 does not replace row 68, row 61, row 140, row 141, row 81",
            "Row 141 does not replace row 68, row 61, row 140, row 121, row 101, row 81",
        ),
        (
            "Row 141 names **Row 68 → Row 81 Row 68 → Row 61 Handshake 4a meta prelude reunion**",
            "Row 121 names **Row 68 → Row 101 Row 68 → Row 61 Handshake 4a meta prelude reunion**",
        ),
        ("Handshake 3 meta prelude capstone row 141", "Handshake 3 meta prelude capstone row 140"),
        (
            "before row 142 Handshake 4b meta prelude capstone opens",
            "before row 122 Handshake 4b meta prelude capstone opens on the capstone path",
        ),
        (
            "when thermal pre-stress is verified after Handshake 3 meta prelude capstone but OpenDiS exports feed the plasticity deck without power-law extrapolation |",
            "when thermal pre-stress is verified on the capstone path after Handshake 3 meta prelude capstone but OpenDiS exports feed the plasticity deck without power-law extrapolation |",
        ),
        (
            "when thermal pre-stress is verified after Handshake 3 meta prelude capstone but OpenDiS exports feed the plasticity deck without power-law extrapolation\"",
            "when thermal pre-stress is verified on the capstone path after Handshake 3 meta prelude capstone but OpenDiS exports feed the plasticity deck without power-law extrapolation\"",
        ),
        (
            "Do not conflate row 141 (row 68 ↔ row 61 reunion on the capstone path) with row 141 (opening-hinge prelude stitch alone)",
            "Do not conflate row 141 (row 68 ↔ row 61 reunion on the capstone path) with row 121 (opening-hinge prelude stitch alone)",
        ),
        (
            "row 141 names **Row 68 → Row 81 Row 68 → Row 61 Handshake 4a meta prelude reunion**; row 141 names",
            "row 121 names **Row 68 → Row 101 Row 68 → Row 61 Handshake 4a meta prelude reunion**; row 141 names",
        ),
        ("Row 68 → Row 141 reunion", "Row 68 → Row 121 reunion"),
        ("Row 68 → Row 140 reunion", "Row 68 → Row 120 reunion"),
        (
            "[row 140](preface.md#skill-navigation-row-140) or [row 141](preface.md#skill-navigation-row-121) closed the Handshake 3 meta prelude capstone / Handshake 4a meta prelude hinge",
            "[row 140](preface.md#skill-navigation-row-140) or [row 121](preface.md#skill-navigation-row-121) closed the Handshake 3 meta prelude capstone / Handshake 4a meta prelude hinge",
        ),
        (
            "[row 140](preface.md#skill-navigation-row-140) or [row 141](preface.md#skill-navigation-row-141) closed the Handshake 3 meta prelude capstone / Handshake 4a meta prelude hinge",
            "[row 140](preface.md#skill-navigation-row-140) or [row 121](preface.md#skill-navigation-row-121) closed the Handshake 3 meta prelude capstone / Handshake 4a meta prelude hinge",
        ),
        (
            "Row 68 → Row 101 Handshake 4a meta prelude reunion index (row 121)](appendix/sources.md#row68-row121-handshake4a-meta-prelude-capstone-reunion-index-row-141)",
            "Row 68 → Row 121 Handshake 4a meta prelude capstone reunion index (row 141)](appendix/sources.md#row68-row121-handshake4a-meta-prelude-capstone-reunion-index-row-141)",
        ),
        (
            "or row 141's epilogue rate cross-links recited after verified Handshake 4a opening prelude meta",
            "or row 121's epilogue rate cross-links recited after verified Handshake 4a opening prelude meta",
        ),
        (
            "Row 68 → Row 121 Handshake 4a meta prelude reunion index (row 141)",
            "Row 68 → Row 101 Handshake 4a meta prelude reunion index (row 121)",
        ),
        (
            "to [row 101](preface.md#skill-navigation-row-121) for the Row 68 ↔ Row 61",
            "to [row 101](preface.md#skill-navigation-row-101) for the Row 68 ↔ Row 61",
        ),
        (
            "to [row 120](preface.md#skill-navigation-row-140) for the Row 68 ↔ Row 60",
            "to [row 120](preface.md#skill-navigation-row-120) for the Row 68 ↔ Row 60",
        ),
    ]
    for a, b in fixes:
        s = s.replace(a, b)
    return s


def rebuild_row_141_preface(preface: str) -> str:
    m121 = re.search(
        r"(### Row 121 skill checkpoint.*?)(?=\n### Row 122 skill checkpoint)",
        preface,
        re.S,
    )
    if not m121:
        raise SystemExit("row 121 checkpoint missing")
    row141 = polish_row_141_text(mod.lift_121_to_141(m121.group(1)))
    row141 = re.sub(
        r"When row 141 is complete, proceed to.*?(?=or extend prose only under `writings/` then sync\.)",
        (
            "When row 141 is complete, proceed to [row 142](preface.md#skill-navigation-row-142) when row 68 closed but Handshake 4b meta prelude still lags on the capstone path, "
            "to [row 122](preface.md#skill-navigation-row-122) when Handshake 4a meta prelude capstone is clean but Handshake 4b meta prelude still lags on the opening-hinge path, "
            "to [row 102](preface.md#skill-navigation-row-102) for the Row 68 ↔ Row 62 Handshake 4b meta prelude audit alone, "
            "to [row 101](preface.md#skill-navigation-row-101) for the Row 68 ↔ Row 61 Handshake 4a meta prelude audit on the opening-hinge path alone, "
            "to [row 140](preface.md#skill-navigation-row-140) when Handshake 3 meta prelude capstone still lags after verified Handshake 3 meta capstone on the capstone path, "
            "to [row 81](preface.md#skill-navigation-row-81) for the Row 68 ↔ Row 61 opening prelude audit alone, "
            "to [row 61](preface.md#skill-navigation-row-61) for the Row 60 ↔ Row 41 meta audit alone, "
            "to [row 41](preface.md#skill-navigation-row-41) for the full VII.3 → Handshake 4a meta audit, "
        ),
        row141,
        flags=re.S,
    )
    start = preface.find("\n### Row 141 skill checkpoint")
    end = preface.find("\n## The copper wire through the book", start)
    if start < 0 or end < 0:
        raise SystemExit("row 141 preface anchors missing")
    return preface[:start] + "\n" + row141 + preface[end:]


def main() -> None:
    for rel in [
        "writings/prologue/chapters/00-many-scales.md",
        "writings/appendix/chapters/sources.md",
        "writings/appendix/chapters/memory-sheet.md",
    ]:
        path = ROOT / rel
        text = polish_row_141_text(path.read_text())
        path.write_text(text)
        print(f"polished: {rel}")

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    if "### Row 141 skill checkpoint" in preface_path.read_text():
        preface_path.write_text(rebuild_row_141_preface(preface_path.read_text()))
        print("preface: rebuilt row 141 checkpoint")
    else:
        print("preface: row 141 checkpoint missing (skip rebuild)")

    ep_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep = polish_row_141_text(ep_path.read_text())
    if "### Row 141 closing loop" not in ep:
        block121 = mod.extract_between(ep, "### Row 121 closing loop", "### Row 122 closing loop")
        block141 = polish_row_141_text(mod.lift_121_to_141(block121))
        ep = ep.replace("### Row 122 closing loop", block141 + "### Row 122 closing loop", 1)
        print("epilogue: added row 141 closing loop")
    ep_path.write_text(ep)
    print("epilogue: polished row 141 loop")


if __name__ == "__main__":
    main()
