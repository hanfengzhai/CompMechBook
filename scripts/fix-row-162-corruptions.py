#!/usr/bin/env python3
"""Repair row 162 insert artifacts and duplicate epilogue closing loops."""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

spec = importlib.util.spec_from_file_location("add_row_162", ROOT / "scripts/add-row-162.py")
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


def polish_row_162_epilogue_block(block: str) -> str:
    fixes = [
        (
            "Row 68 → Row 62 meta (row 162) must read",
            "Row 68 → Row 62 meta (row 142) must read",
        ),
        (
            "per [row 162](../preface.md#skill-navigation-row-102)",
            "per [row 142](../preface.md#skill-navigation-row-142)",
        ),
        (
            "Recite [preface row 161](../preface.md#skill-navigation-row-121)",
            "Recite [preface row 161](../preface.md#skill-navigation-row-161)",
        ),
        (
            "Do not conflate row 162 (row 68 ↔ row 62 reunion on the capstone path) with row 162 (opening-hinge prelude stitch alone) — row 162 names **Row 68 → Row 102 Row 68 → Row 62 Handshake 4b meta prelude reunion**; row 162 names",
            "Do not conflate row 162 (row 68 ↔ row 62 reunion continuation on the capstone path) with row 142 (opening-hinge capstone stitch alone) — row 142 names **Row 68 → Row 122 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion**; row 162 names",
        ),
        (
            "Proceed to [row 143](#row-143-closing-loop) when row 68 closed but orchestration meta prelude still lags after row 162 on the capstone path, to [row 143](#row-123-closing-loop) when row 68 closed but orchestration meta still feels disconnected after row 162 on the opening-hinge path, to [row 143](#row-103-closing-loop) for the Row 68 ↔ Row 63 meta audit on the opening-hinge prelude path alone, to [row 162](#row-102-closing-loop) for the Row 68 ↔ Row 62 meta audit on the opening-hinge prelude path alone, to [row 161](#row-121-closing-loop) when Handshake 4a meta prelude capstone still lags after verified Handshake 3 meta prelude capstone, to [row 62](#row-62-closing-loop) when only Handshake 4b meta stalls, or extend prose only under `writings/` then sync.",
            "Proceed to [row 143](#row-143-closing-loop) when row 68 closed but orchestration meta prelude still lags after row 162 on the capstone path, to [row 123](#row-123-closing-loop) when Handshake 4b meta prelude capstone is clean but orchestration meta prelude still lags on the opening-hinge path, to [row 103](#row-103-closing-loop) for the Row 68 ↔ Row 63 orchestration meta prelude audit alone, to [row 142](#row-142-closing-loop) when Handshake 4a meta prelude capstone still lags after row 161 on the capstone path, to [row 62](#row-62-closing-loop) when only Handshake 4b meta stalls, or extend prose only under `writings/` then sync.",
        ),
    ]
    for a, b in fixes:
        block = block.replace(a, b)
    return block


def polish_preface_row_162(s: str) -> str:
    fixes = [
        (
            "[row 161](preface.md#skill-navigation-row-121) or [row 162](preface.md#skill-navigation-row-102)",
            "[row 161](preface.md#skill-navigation-row-161) or [row 142](preface.md#skill-navigation-row-142)",
        ),
        (
            "Row 68 → Row 142 Handshake 4b meta prelude reunion index (row 162)",
            "Row 68 → Row 142 Handshake 4b meta prelude capstone reunion continuation index (row 162)",
        ),
        (
            "Row 162 does not replace row 68, row 62, row 161, row 162, row 102",
            "Row 162 does not replace row 68, row 62, row 161, row 142, row 102",
        ),
        (
            "verified Handshake 4a meta prelude capstone closure (row 161) with the full-book Handshake 4b meta reunion (row 62)** when bulk",
            "verified Handshake 4a meta prelude capstone closure (row 161) with the full-book Handshake 4b meta reunion (row 62)** when bulk",
        ),
        (
            "When row 162 is complete, proceed to [row 143](preface.md#skill-navigation-row-143) when row 68 closed but orchestration meta prelude still lags on the capstone path, to [row 143](preface.md#skill-navigation-row-123) when Handshake 4b meta prelude capstone is clean but orchestration meta prelude still lags on the opening-hinge path",
            "When row 162 is complete, proceed to [row 143](preface.md#skill-navigation-row-143) when row 68 closed but orchestration meta prelude still lags on the capstone path, to [row 123](preface.md#skill-navigation-row-123) when Handshake 4b meta prelude capstone is clean but orchestration meta prelude still lags on the opening-hinge path",
        ),
        (
            "to [row 162](preface.md#skill-navigation-row-102) for the Row 68 ↔ Row 62 Handshake 4b meta prelude audit alone",
            "to [row 102](preface.md#skill-navigation-row-102) for the Row 68 ↔ Row 62 Handshake 4b meta prelude audit alone",
        ),
        (
            "to [row 161](preface.md#skill-navigation-row-141) when Handshake 4a meta prelude capstone still lags",
            "to [row 161](preface.md#skill-navigation-row-161) when Handshake 4a meta prelude capstone still lags",
        ),
        (
            "When row 161 is complete, proceed to [row 142](preface.md#skill-navigation-row-142) when row 68 closed but Handshake 4b meta prelude still lags on the capstone path, to [row 142](preface.md#skill-navigation-row-122) when Handshake 4a meta prelude capstone is clean but Handshake 4b meta prelude still lags on the opening-hinge path",
            "When row 161 is complete, proceed to [row 162](preface.md#skill-navigation-row-162) when row 68 closed but Handshake 4b meta prelude still lags after row 161 on the capstone path, to [row 142](preface.md#skill-navigation-row-142) when Handshake 4a meta prelude capstone is clean but Handshake 4b meta prelude still lags on the capstone path without continuation, to [row 122](preface.md#skill-navigation-row-122) when Handshake 4a meta prelude capstone is clean but Handshake 4b meta prelude still lags on the opening-hinge path",
        ),
    ]
    for a, b in fixes:
        s = s.replace(a, b)
    return s


def fix_epilogue() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()

    # Drop mistaken duplicate blocks from naive lift source.
    text = remove_between(
        text,
        "### Row 162 closing loop (Row 68 → Row 102 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion) {#row-122-closing-loop}",
        "### Row 162 closing loop (Row 68 → Row 142 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion continuation) {#row-162-closing-loop}",
    )
    text = remove_between(
        text,
        "### Row 143 closing loop (Row 68 → Row 103 Row 68 → Row 63 orchestration meta prelude capstone reunion) {#row-123-closing-loop}",
        "### Row 143 closing loop (Row 68 → Row 123 Row 68 → Row 63 orchestration meta prelude capstone reunion) {#row-143-closing-loop}",
    )
    text = remove_between(
        text,
        "### Row 142 closing loop (Row 68 → Row 102 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion) {#row-122-closing-loop}",
        "### Row 142 closing loop (Row 68 → Row 122 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion) {#row-142-closing-loop}",
    )

    m = re.search(
        r"(### Row 162 closing loop \(Row 68 → Row 142.*?\{#row-162-closing-loop\}.*?)(?=\n### Row 143 closing loop)",
        text,
        re.S,
    )
    if m:
        fixed = polish_row_162_epilogue_block(m.group(1))
        text = text.replace(m.group(1), fixed, 1)

    # Row 161 closing loop footer
    text = text.replace(
        "Do not conflate row 161 (row 68 ↔ row 61 reunion on the capstone path) with row 161 (opening-hinge prelude stitch alone) — row 161 names **Row 68 → Row 101 Row 68 → Row 61 Handshake 4a meta prelude reunion**; row 161 names",
        "Do not conflate row 161 (row 68 ↔ row 61 reunion continuation on the capstone path) with row 121 (opening-hinge capstone stitch alone) — row 121 names **Row 68 → Row 101 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion**; row 161 names",
    )
    text = text.replace(
        "Proceed to [row 142](#row-142-closing-loop) when row 68 closed but Handshake 4b meta prelude still lags after row 161 on the capstone path, to [row 142](#row-122-closing-loop) when Handshake 4a meta prelude capstone is clean but Handshake 4b meta prelude still lags on the opening-hinge path",
        "Proceed to [row 162](#row-162-closing-loop) when row 68 closed but Handshake 4b meta prelude still lags after row 161 on the capstone path, to [row 122](#row-122-closing-loop) when Handshake 4a meta prelude capstone is clean but Handshake 4b meta prelude still lags on the opening-hinge path",
    )
    text = text.replace(
        "[preface row 160](../preface.md#skill-navigation-row-140)",
        "[preface row 160](../preface.md#skill-navigation-row-160)",
    )
    text = text.replace(
        "to [row 160](#row-140-closing-loop) when Handshake 3 meta prelude capstone still lags",
        "to [row 160](#row-160-closing-loop) when Handshake 3 meta prelude capstone still lags",
    )

    path.write_text(text)
    print("epilogue: fixed row 162 artifacts")


def fix_preface() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = polish_preface_row_162(path.read_text())
    path.write_text(text)
    print("preface: polished row 162")


def main() -> None:
    fix_epilogue()
    fix_preface()
    mod.fix_row_162_corruptions()


if __name__ == "__main__":
    main()
