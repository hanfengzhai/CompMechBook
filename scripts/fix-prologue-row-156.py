#!/usr/bin/env python3
"""Repair row 156 prologue compass/preview/stitch after add-row-156."""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GOLD = "origin/cursor/computational-mechanics-book-0a8a"


def gold_lines(pattern: str) -> list[str]:
    text = subprocess.run(
        ["git", "show", f"{GOLD}:writings/prologue/chapters/00-many-scales.md"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    return [ln for ln in text.splitlines() if pattern in ln]


def main() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    good_compass = [
        ln
        for ln in gold_lines("Born–Oppenheimer meta prelude capstone reunion (row 156)")
        if ln.startswith("| Row 68")
    ][0]
    text = re.sub(
        r"(\| Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone reunion \(row 155\) \|[^\n]*\n)"
        r"(?:\| Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion \(row 136\) \|[^\n]*\n)+",
        r"\1" + good_compass + "\n",
        text,
        count=1,
    )
    preview = [ln for ln in gold_lines("prologue-preview-row-156") if ln.startswith("|")][0]
    if "prologue-preview-row-156" not in text:
        for anchor in (
            '| <span id="prologue-preview-row-155"></span>',
            '| <span id="prologue-preview-row-154"></span>',
        ):
            if anchor in text:
                idx = text.find(anchor)
                line_end = text.find("\n", idx)
                text = text[: line_end + 1] + preview + "\n" + text[line_end + 1 :]
                break
    stitch_lines = [
        ln for ln in gold_lines("row-156-closing-stitch") if ln.startswith("**Row 156 closing stitch")
    ]
    if stitch_lines and stitch_lines[0] not in text:
        text = text.replace(
            "**Row 155 closing stitch",
            stitch_lines[0] + "\n\n**Row 155 closing stitch",
            1,
        )
    path.write_text(text)
    print("prologue row 156 repaired")


if __name__ == "__main__":
    main()
