#!/usr/bin/env python3
"""Repair row 249/269 taxonomy meta-stitch anchors in prologue."""
from pathlib import Path
import importlib.util
import re

ROOT = Path(__file__).resolve().parents[1]


def _stitch(row: int) -> str:
    mod_path = ROOT / f"scripts/add-row-{row}.py"
    spec = importlib.util.spec_from_file_location(f"add{row}", mod_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod._build_blocks()["prologue_stitch"].strip() + "\n\n"


def fix_prologue(text: str) -> str:
    for row in (249, 269):
        stitch = _stitch(row)
        pattern = (
            rf"\*\*Row \d+ closing stitch \(Row 68 → Row \d+ Row 68 → Row 49 taxonomy meta prelude capstone reunion\)\.\*\* "
            rf"(\{{#row-{row}-closing-stitch\}}[^\n]*\n)*"
        )
        if re.search(pattern, text):
            text = re.sub(pattern, stitch.strip() + "\n\n", text, count=1)
        elif f"{{#row-{row}-closing-stitch}}" in text and stitch.strip() not in text:
            anchor = f"{{#row-{row}-closing-stitch}}"
            idx = text.index(anchor)
            start = text.rfind("\n\n**", 0, idx)
            end = text.find("\n\n**Row ", idx + 10)
            if end == -1:
                end = text.find("\n\n**Row 268", idx)
            if start != -1 and end != -1:
                text = text[: start + 2] + stitch + text[end + 2 :]
    return text


def main() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = path.read_text()
    fixed = fix_prologue(prologue)
    if fixed != prologue:
        path.write_text(fixed)
        print("prologue: repaired row 249/269 closing stitches")
    else:
        print("prologue: no stitch repair needed")


if __name__ == "__main__":
    main()
