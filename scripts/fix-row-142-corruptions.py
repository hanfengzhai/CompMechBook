#!/usr/bin/env python3
"""Fix double-substitution artifacts from lift_122_to_142 and rebuild row 142 checkpoint."""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

spec = importlib.util.spec_from_file_location("add_row_142", ROOT / "scripts/add-row-142.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def polish_row_142_text(s: str) -> str:
    fixes = [
        ("Row 68 → Row 142 Row 68 → Row 62", "Row 68 → Row 122 Row 68 → Row 62"),
        ("Row 68 → Row 142 Handshake", "Row 68 → Row 122 Handshake"),
        ("row 141 or row 142 closed Handshake", "row 141 or row 122 closed Handshake"),
        ("row 141 or row 142 Handshake", "row 141 or row 122 Handshake"),
        (
            "Row 68 → Row 142 Handshake 4b meta prelude reunion index (row 142)",
            "Row 68 → Row 122 Handshake 4b meta prelude reunion index (row 122)",
        ),
        (
            "appendix/sources.md#row68-row102-handshake4b-meta-prelude-capstone-reunion-index-row-122)",
            "appendix/sources.md#row68-row122-handshake4b-meta-prelude-capstone-reunion-index-row-142)",
        ),
        (
            "Row 142 does not replace row 68, row 62, row 141, row 142, row 82",
            "Row 142 does not replace row 68, row 62, row 141, row 122, row 102, row 82",
        ),
        (
            "Row 142 names **Row 68 → Row 82 Row 68 → Row 62 Handshake 4b meta prelude reunion**",
            "Row 122 names **Row 68 → Row 102 Row 68 → Row 62 Handshake 4b meta prelude reunion**",
        ),
        (
            "before row 143 orchestration meta prelude capstone opens",
            "before row 123 orchestration meta prelude capstone opens on the capstone path",
        ),
        (
            "Do not conflate row 142 (row 68 ↔ row 62 reunion on the capstone path) with row 142 (opening-hinge prelude stitch alone)",
            "Do not conflate row 142 (row 68 ↔ row 62 reunion on the capstone path) with row 122 (opening-hinge prelude stitch alone)",
        ),
        (
            "row 142 names **Row 68 → Row 82 Row 68 → Row 62 Handshake 4b meta prelude reunion**; row 142 names",
            "row 122 names **Row 68 → Row 102 Row 68 → Row 62 Handshake 4b meta prelude reunion**; row 142 names",
        ),
        ("Row 68 → Row 142 reunion", "Row 68 → Row 122 reunion"),
        (
            "[row 141](preface.md#skill-navigation-row-141) or [row 142](preface.md#skill-navigation-row-122) closed the Handshake 4a meta prelude capstone / Handshake 4b meta prelude hinge",
            "[row 141](preface.md#skill-navigation-row-141) or [row 122](preface.md#skill-navigation-row-122) closed the Handshake 4a meta prelude capstone / Handshake 4b meta prelude hinge",
        ),
        (
            "[row 141](preface.md#skill-navigation-row-141) or [row 142](preface.md#skill-navigation-row-142) closed the Handshake 4a meta prelude capstone / Handshake 4b meta prelude hinge",
            "[row 141](preface.md#skill-navigation-row-141) or [row 122](preface.md#skill-navigation-row-122) closed the Handshake 4a meta prelude capstone / Handshake 4b meta prelude hinge",
        ),
        (
            "Row 68 → Row 102 Handshake 4b meta prelude reunion index (row 122)](appendix/sources.md#row68-row122-handshake4b-meta-prelude-capstone-reunion-index-row-142)",
            "Row 68 → Row 122 Handshake 4b meta prelude capstone reunion index (row 142)](appendix/sources.md#row68-row122-handshake4b-meta-prelude-capstone-reunion-index-row-142)",
        ),
        (
            "or row 142's epilogue FE² cross-links recited after verified Handshake 4b opening prelude meta",
            "or row 122's epilogue FE² cross-links recited after verified Handshake 4b opening prelude meta",
        ),
        (
            "Row 68 → Row 122 Handshake 4b meta prelude reunion index (row 142)",
            "Row 68 → Row 102 Handshake 4b meta prelude reunion index (row 122)",
        ),
        (
            "to [row 102](preface.md#skill-navigation-row-122) for the Row 68 ↔ Row 62",
            "to [row 102](preface.md#skill-navigation-row-102) for the Row 68 ↔ Row 62",
        ),
        (
            "to [row 101](preface.md#skill-navigation-row-141) for the Row 68 ↔ Row 61",
            "to [row 101](preface.md#skill-navigation-row-101) for the Row 68 ↔ Row 61",
        ),
    ]
    for a, b in fixes:
        s = s.replace(a, b)
    return s


def rebuild_row_142_preface(preface: str) -> str:
    m122 = re.search(
        r"(### Row 122 skill checkpoint.*?)(?=\n### Row 123 skill checkpoint)",
        preface,
        re.S,
    )
    if not m122:
        raise SystemExit("row 122 checkpoint missing")
    row142 = polish_row_142_text(mod.lift_122_to_142(m122.group(1)))
    row142 = re.sub(
        r"When row 142 is complete, proceed to.*?(?=or extend prose only under `writings/` then sync\.)",
        (
            "When row 142 is complete, proceed to [row 143](preface.md#skill-navigation-row-143) when row 68 closed but orchestration meta prelude still lags on the capstone path, "
            "to [row 123](preface.md#skill-navigation-row-123) when Handshake 4b meta prelude capstone is clean but orchestration meta prelude still lags on the opening-hinge path, "
            "to [row 103](preface.md#skill-navigation-row-103) for the Row 68 ↔ Row 63 orchestration meta prelude audit alone, "
            "to [row 102](preface.md#skill-navigation-row-102) for the Row 68 ↔ Row 62 Handshake 4b meta prelude audit on the opening-hinge path alone, "
            "to [row 141](preface.md#skill-navigation-row-141) when Handshake 4a meta prelude capstone still lags after verified Handshake 4a meta capstone on the capstone path, "
            "to [row 82](preface.md#skill-navigation-row-82) for the Row 68 ↔ Row 62 opening prelude audit alone, "
            "to [row 62](preface.md#skill-navigation-row-62) for the Row 61 ↔ Row 42 meta audit alone, "
            "to [row 42](preface.md#skill-navigation-row-42) for the full VII.3 Step 4 → Handshake 4b meta audit, "
        ),
        row142,
        flags=re.S,
    )
    start = preface.find("\n### Row 142 skill checkpoint")
    end = preface.find("\n## The copper wire through the book", start)
    if start < 0 or end < 0:
        raise SystemExit("row 142 preface anchors missing")
    return preface[:start] + "\n" + row142 + preface[end:]


def main() -> None:
    for rel in [
        "writings/prologue/chapters/00-many-scales.md",
        "writings/appendix/chapters/sources.md",
        "writings/appendix/chapters/memory-sheet.md",
    ]:
        path = ROOT / rel
        text = polish_row_142_text(path.read_text())
        path.write_text(text)
        print(f"polished: {rel}")

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = polish_row_142_text(preface_path.read_text())
    if "### Row 142 skill checkpoint" in preface:
        preface_path.write_text(rebuild_row_142_preface(preface))
        print("preface: rebuilt row 142 checkpoint")
    else:
        preface_path.write_text(preface)
        print("preface: row 142 checkpoint missing (skip rebuild)")

    ep_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep = polish_row_142_text(ep_path.read_text())
    if "### Row 142 closing loop" not in ep:
        block122 = mod.extract_between(ep, "### Row 122 closing loop", "### Row 123 closing loop")
        block142 = polish_row_142_text(mod.lift_122_to_142(block122))
        ep = ep.replace("### Row 123 closing loop", block142 + "### Row 123 closing loop", 1)
        print("epilogue: added row 142 closing loop")
    ep_path.write_text(ep)
    print("epilogue: polished row 142 loop")


if __name__ == "__main__":
    main()
