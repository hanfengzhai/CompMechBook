#!/usr/bin/env python3
"""Polish row 166 sections after lift_146_to_166 label substitutions."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def polish_row_166_text(s: str) -> str:
    fixes = [
        (
            "[preface row 146 skill checkpoint](../preface.md#skill-navigation-row-166)",
            "[preface row 166 skill checkpoint](../preface.md#skill-navigation-row-166)",
        ),
        (
            "[Preface: row 146 skill checkpoint](../preface.md#skill-navigation-row-166)",
            "[Preface: row 166 skill checkpoint](../preface.md#skill-navigation-row-166)",
        ),
        (
            "[prologue row 146 preview row](#prologue-preview-row-166)",
            "[prologue row 166 preview row](#prologue-preview-row-166)",
        ),
        (
            "[prologue row 146 closing stitch](#row-166-closing-stitch)",
            "[prologue row 166 closing stitch](#row-166-closing-stitch)",
        ),
        (
            "[epilogue row 146 closing loop](../epilogue/multiscale.md#row-166-closing-loop)",
            "[epilogue row 166 closing loop](../epilogue/multiscale.md#row-166-closing-loop)",
        ),
        (
            "Prologue preview ([row 146](prologue/00-many-scales.md#prologue-preview-row-166))",
            "Prologue preview ([row 166](prologue/00-many-scales.md#prologue-preview-row-166))",
        ),
        (
            "[Preface row 146](../preface.md#skill-navigation-row-166)",
            "[Preface row 166](../preface.md#skill-navigation-row-166)",
        ),
        (
            "Read the [prologue row 146 closing stitch]",
            "Read the [prologue row 166 closing stitch]",
        ),
        (
            "read the [prologue row 146 preview]",
            "read the [prologue row 146 preview]",
        ),
        (
            "Then read the [prologue row 146 preview](prologue/00-many-scales.md#prologue-preview-row-166)",
            "Then read the [prologue row 166 preview](prologue/00-many-scales.md#prologue-preview-row-166)",
        ),
        (
            "[preface row 146 skill checkpoint](../preface.md#skill-navigation-row-166); [prologue row 146 closing stitch]",
            "[preface row 166 skill checkpoint](../preface.md#skill-navigation-row-166); [prologue row 166 closing stitch]",
        ),
        (
            "read row 68 gate + row 145 or row 146 second-pass",
            "read row 68 gate + row 165 or row 146 second-pass",
        ),
        (
            "when Preface → Epilogue reads as one novel after row 145 but git diff",
            "when Preface → Epilogue reads as one novel after row 165 but git diff",
        ),
        (
            "[row 145](preface.md#skill-navigation-row-145) or [row 146](preface.md#skill-navigation-row-126)",
            "[row 165](preface.md#skill-navigation-row-165) or [row 146](preface.md#skill-navigation-row-146)",
        ),
        (
            "Confirm [row 145](preface.md#skill-navigation-row-145) or",
            "Confirm [row 165](preface.md#skill-navigation-row-165) or",
        ),
        ("on the capstone path on the capstone path", "on the capstone path"),
    ]
    for a, b in fixes:
        s = s.replace(a, b)
    return s


def main() -> None:
    paths = [
        ROOT / "writings/preface/chapters/preface.md",
        ROOT / "writings/prologue/chapters/00-many-scales.md",
        ROOT / "writings/epilogue/chapters/multiscale.md",
        ROOT / "writings/appendix/chapters/sources.md",
        ROOT / "writings/appendix/chapters/memory-sheet.md",
    ]
    for path in paths:
        text = polish_row_166_text(path.read_text())
        path.write_text(text)
        print(f"polished: {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
