#!/usr/bin/env python3
"""Fix double-substitution artifacts from lift_120_to_140 and add missing epilogue loop."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Import lift from add-row-140 after patching
import importlib.util

spec = importlib.util.spec_from_file_location("add_row_140", ROOT / "scripts/add-row-140.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def polish_row_140_text(s: str) -> str:
    fixes = [
        ("Row 68 → Row 140 Row 68 → Row 60", "Row 68 → Row 120 Row 68 → Row 60"),
        ("Row 68 → Row 140 Handshake", "Row 68 → Row 120 Handshake"),
        ("row 139 or row 140 closed Handshake", "row 139 or row 120 closed Handshake"),
        ("row 139 or row 140 Handshake", "row 139 or row 120 Handshake"),
        ("preface.md#skill-navigation-row-119)", "preface.md#skill-navigation-row-139)"),
        ("preface.md#skill-navigation-row-100)", "preface.md#skill-navigation-row-120)"),
        (
            "Row 68 → Row 140 Handshake 3 meta prelude reunion index (row 140)",
            "Row 68 → Row 120 Handshake 3 meta prelude reunion index (row 120)",
        ),
        (
            "appendix/sources.md#row68-row100-handshake3-meta-prelude-capstone-reunion-index-row-120)",
            "appendix/sources.md#row68-row120-handshake3-meta-prelude-capstone-reunion-index-row-140)",
        ),
        (
            "Row 140 does not replace row 68, row 60, row 139, row 140, row 80",
            "Row 140 does not replace row 68, row 60, row 139, row 120, row 100, row 80",
        ),
        (
            "Row 140 names **Row 68 → Row 80 Row 68 → Row 60 Handshake 3 meta prelude reunion**",
            "Row 120 names **Row 68 → Row 100 Row 68 → Row 60 Handshake 3 meta prelude reunion**",
        ),
        (
            "Row 140 names **Row 68 → Row 99 Row 68 → Row 59 Handshake 3 meta capstone reunion**",
            "Row 139 names **Row 68 → Row 119 Row 68 → Row 59 Handshake 3 meta capstone reunion**",
        ),
        ("Handshake 3 meta capstone row 140", "Handshake 3 meta capstone row 139"),
        (
            "before row 141 Handshake 4a meta prelude capstone opens",
            "before row 121 Handshake 4a meta prelude capstone opens on the capstone path",
        ),
        (
            "when load cell parses at \\(T_w\\) after verified DFT workflows meta capstone but Handshake 3 still feels disconnected from Parts III–VI |",
            "when load cell parses at \\(T_w\\) on the capstone path after verified Handshake 3 meta capstone but Handshake 3 still feels disconnected from Parts III–VI |",
        ),
        (
            "when load cell parses at \\(T_w\\) after verified DFT workflows meta capstone but Handshake 3 still feels disconnected from Parts III–VI\"",
            "when load cell parses at \\(T_w\\) on the capstone path after verified Handshake 3 meta capstone but Handshake 3 still feels disconnected from Parts III–VI\"",
        ),
    ]
    for a, b in fixes:
        s = s.replace(a, b)
    return s


def rebuild_row_140_preface(preface: str) -> str:
    m120 = re.search(
        r"(### Row 120 skill checkpoint.*?)(?=\n### Row 121 skill checkpoint)",
        preface,
        re.S,
    )
    if not m120:
        raise SystemExit("row 120 checkpoint missing")
    row140 = polish_row_140_text(mod.lift_120_to_140(m120.group(1)))
    row140 = re.sub(
        r"When row 140 is complete, proceed to.*?(?=or extend prose only under `writings/` then sync\.)",
        (
            "When row 140 is complete, proceed to [row 141](preface.md#skill-navigation-row-141) when row 68 closed but Handshake 4a meta prelude still lags on the capstone path, "
            "to [row 121](preface.md#skill-navigation-row-121) when Handshake 3 meta prelude capstone is clean but Handshake 4a meta prelude still lags on the opening-hinge path, "
            "to [row 101](preface.md#skill-navigation-row-101) for the Row 68 ↔ Row 61 Handshake 4a meta prelude audit alone, "
            "to [row 120](preface.md#skill-navigation-row-120) for the Row 68 ↔ Row 60 Handshake 3 meta prelude audit on the opening-hinge path alone, "
            "to [row 139](preface.md#skill-navigation-row-139) when Handshake 3 meta capstone still lags after verified DFT workflows meta capstone on the capstone path, "
            "to [row 80](preface.md#skill-navigation-row-80) for the Row 68 ↔ Row 60 meta audit alone, "
            "to [row 60](preface.md#skill-navigation-row-60) for the Row 59 ↔ Row 40 meta audit alone, "
            "to [row 40](preface.md#skill-navigation-row-40) for the full-book \\(\\alpha(T_w)\\) audit, "
        ),
        row140,
        flags=re.S,
    )
    start = preface.find("\n### Row 140 skill checkpoint")
    end = preface.find("\n## The copper wire through the book", start)
    if start < 0 or end < 0:
        raise SystemExit("row 140 preface anchors missing")
    return preface[:start] + "\n" + row140 + preface[end:]


def main() -> None:
    for rel in [
        "writings/preface/chapters/preface.md",
        "writings/prologue/chapters/00-many-scales.md",
        "writings/appendix/chapters/sources.md",
        "writings/appendix/chapters/memory-sheet.md",
    ]:
        path = ROOT / rel
        text = polish_row_140_text(path.read_text())
        path.write_text(text)
        print(f"polished: {rel}")

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface_path.write_text(rebuild_row_140_preface(preface_path.read_text()))
    print("preface: rebuilt row 140 checkpoint")

    ep_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep = ep_path.read_text()
    if "### Row 140 closing loop" not in ep:
        block120 = mod.extract_between(ep, "### Row 120 closing loop", "### Row 121 closing loop")
        block140 = polish_row_140_text(mod.lift_120_to_140(block120))
        ep = ep.replace("### Row 121 closing loop", block140 + "### Row 121 closing loop", 1)
        ep_path.write_text(ep)
        print("epilogue: added row 140 closing loop")
    else:
        ep_path.write_text(polish_row_140_text(ep))
        print("epilogue: polished row 140 loop")


if __name__ == "__main__":
    main()
