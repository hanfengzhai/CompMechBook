#!/usr/bin/env python3
"""Repair row 163 insert artifacts and duplicate epilogue closing loops."""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

spec = importlib.util.spec_from_file_location("add_row_163", ROOT / "scripts/add-row-163.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def remove_between(text: str, start: str, end: str) -> str:
    i = text.find(start)
    if i < 0:
        return text
    j = text.find(end, i + len(start))
    if j < 0:
        return text
    return text[:i] + text[j:]


def polish_row_163_epilogue_block(block: str) -> str:
    fixes = [
        (
            "Row 68 → Row 63 meta (row 163) must read",
            "Row 68 → Row 63 meta (row 143) must read",
        ),
        (
            "Recite [preface row 162](../preface.md#skill-navigation-row-122)",
            "Recite [preface row 162](../preface.md#skill-navigation-row-162)",
        ),
        (
            "per [row 163](../preface.md#skill-navigation-row-103)",
            "per [row 143](../preface.md#skill-navigation-row-143)",
        ),
        (
            "Do not conflate row 163 (row 68 ↔ row 63 reunion on the capstone path) with row 163 (opening-hinge prelude stitch alone)",
            "Do not conflate row 163 (row 68 ↔ row 63 reunion continuation on the capstone path) with row 143 (opening-hinge capstone stitch alone)",
        ),
        (
            "row 163 names **Row 68 → Row 83 Row 68 → Row 63 orchestration meta prelude reunion**; row 163 names",
            "row 143 names **Row 68 → Row 123 Row 68 → Row 63 orchestration meta prelude capstone reunion**; row 163 names",
        ),
        (
            "Proceed to [row 144](#row-144-closing-loop) when row 68 closed but book-loop meta capstone still lags after row 163",
            "Proceed to [row 144](#row-144-closing-loop) when row 68 closed but book-loop meta prelude still lags after row 163 on the capstone path",
        ),
        (
            "row 162 or row 163 Handshake 4b meta prelude capstone / orchestration meta prelude gate",
            "row 162 or row 143 Handshake 4b meta prelude capstone / orchestration meta prelude gate",
        ),
        (
            "Proceed to [row 144](#row-144-closing-loop) when row 68 closed but book-loop meta capstone still lags after row 143",
            "Proceed to [row 144](#row-144-closing-loop) when row 68 closed but book-loop meta prelude still lags after row 163 on the capstone path, "
            "to [row 124](#row-124-closing-loop) when row 68 closed but book-loop meta still feels disconnected after row 143 on the opening-hinge path",
        ),
    ]
    for a, b in fixes:
        block = block.replace(a, b)
    return block


def polish_preface_row_163(s: str) -> str:
    fixes = [
        (
            "[row 162](preface.md#skill-navigation-row-122) or [row 163](preface.md#skill-navigation-row-163)",
            "[row 162](preface.md#skill-navigation-row-162) or [row 143](preface.md#skill-navigation-row-143)",
        ),
        (
            "Row 68 → Row 163 orchestration meta prelude capstone reunion index (row 163)",
            "Row 68 → Row 143 orchestration meta prelude capstone reunion continuation index (row 163)",
        ),
        (
            "Row 163 does not replace row 68, row 63, row 163, row 163, row 83",
            "Row 163 does not replace row 68, row 63, row 162, row 143, row 83",
        ),
        (
            "When row 163 is complete, proceed to [row 164](preface.md#skill-navigation-row-164)",
            "When row 163 is complete, proceed to [row 144](preface.md#skill-navigation-row-144)",
        ),
        (
            "When row 162 is complete, proceed to [row 163](preface.md#skill-navigation-row-163) when row 68 closed but orchestration meta prelude still lags on the capstone path",
            "When row 162 is complete, proceed to [row 163](preface.md#skill-navigation-row-163) when row 68 closed but orchestration meta prelude still lags after row 162 on the capstone path, "
            "to [row 143](preface.md#skill-navigation-row-143) when Handshake 4b meta prelude capstone is clean but orchestration meta prelude still lags on the capstone path without continuation",
        ),
    ]
    for a, b in fixes:
        s = s.replace(a, b)
    return s


def fix_epilogue() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()

    text = remove_between(
        text,
        "### Row 163 closing loop (Row 68 → Row 143 Row 68 → Row 63 orchestration meta prelude capstone reunion) {#row-143-closing-loop}",
        "### Row 163 closing loop (Row 68 → Row 143 Row 68 → Row 63 orchestration meta prelude capstone reunion continuation) {#row-163-closing-loop}",
    )
    text = remove_between(
        text,
        "### Row 144 closing loop (Row 68 → Row 124 Row 68 → Row 64 book-loop meta prelude capstone reunion) {#row-124-closing-loop}",
        "### Row 144 closing loop (Row 68 → Row 124 Row 68 → Row 64 book-loop meta prelude capstone reunion) {#row-144-closing-loop}",
    )

    m = re.search(
        r"(### Row 163 closing loop \(Row 68 → Row 143.*?\{#row-163-closing-loop\}.*?)(?=\n### Row 144 closing loop)",
        text,
        re.S,
    )
    if m:
        fixed = polish_row_163_epilogue_block(m.group(1))
        text = text.replace(m.group(1), fixed, 1)

    text = text.replace(
        "Proceed to [row 143](#row-143-closing-loop) when row 68 closed but orchestration meta prelude still lags after row 162 on the capstone path",
        "Proceed to [row 163](#row-163-closing-loop) when row 68 closed but orchestration meta prelude still lags after row 162 on the capstone path, "
        "to [row 143](#row-143-closing-loop) when Handshake 4b meta prelude capstone is clean but orchestration meta prelude still lags on the opening-hinge path",
    )

    path.write_text(text)
    print("epilogue: fixed row 163 artifacts")


def fix_preface() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = polish_preface_row_163(path.read_text())
    path.write_text(text)
    print("preface: polished row 163")


def main() -> None:
    fix_epilogue()
    fix_preface()
    mod.fix_row_163_corruptions()


if __name__ == "__main__":
    main()
