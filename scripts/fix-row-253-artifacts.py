#!/usr/bin/env python3
"""One-off cleanup: dedupe row-253 inserts and fix prologue/epilogue artifacts."""
from pathlib import Path
import importlib.util
import re

ROOT = Path(__file__).resolve().parents[1]


def dedupe_adjacent_lines(text: str) -> str:
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    prev = None
    for line in lines:
        if line == prev:
            continue
        out.append(line)
        prev = line
    return "".join(out)


def fix_prologue_stitch253(text: str) -> str:
    pattern = (
        r"\*\*Row (?:233|253) closing stitch \(Row 68 → Row 233 Row 68 → Row 53 dynamics meta prelude capstone reunion\)\.\*\* \{#row-253-closing-stitch\}"
        r"(?: \(Row 68 → Row 233 Row 68 → Row 53 dynamics meta prelude capstone reunion\)\.\*\* \{#row-253-closing-stitch\})*"
    )
    return re.sub(
        pattern,
        "**Row 253 closing stitch (Row 68 → Row 233 Row 68 → Row 53 dynamics meta prelude capstone reunion).** {#row-253-closing-stitch}",
        text,
        count=1,
    )


def fix_preview_row253(prologue: str) -> str:
    spec = importlib.util.spec_from_file_location("add253", ROOT / "scripts/add-row-253.py")
    add253 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add253)
    good = add253._row253_prologue_preview().strip()
    for bad_prefix in (
        '| <span id="prologue-preview-row-253"></span>',
        '| <span id="prologue-preview-row-272"></span>',
    ):
        idx = prologue.find(bad_prefix)
        if idx == -1:
            continue
        bad_end = prologue.find("\n", idx)
        return prologue[:idx] + good + prologue[bad_end:]
    anchor = '| <span id="prologue-preview-row-233"></span>'
    if good not in prologue and anchor in prologue:
        return prologue.replace(anchor, good + "\n" + anchor, 1)
    return prologue


def strip_duplicate_row253_loops(text: str) -> str:
    """Drop the late duplicate loop (Row 68 → Row 253 header); keep the capstone-path block."""
    pattern = (
        r"\n\n### Row 253 closing loop \(Row 68 → Row 253 Row 68 → Row 53 "
        r"dynamics meta prelude capstone reunion\) \{#row-253-closing-loop\}.*?"
        r"(?=\n\n### Row \d+ closing loop|\n\n### Row 254 closing loop|\Z)"
    )
    return re.sub(pattern, "", text, flags=re.DOTALL)


def dedupe_memory_row253(memory: str) -> str:
    needle = "| 253 | Meta | [Row 68 → Row 233 dynamics meta prelude capstone reunion index]"
    first = memory.find(needle)
    if first == -1:
        return memory
    second = memory.find(needle, first + len(needle))
    while second != -1:
        line_end = memory.find("\n", second)
        if line_end == -1:
            break
        memory = memory[:second] + memory[line_end + 1 :]
        second = memory.find(needle, first + len(needle))
    return memory


def main() -> None:
    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    prologue = dedupe_adjacent_lines(prologue)
    prologue = fix_prologue_stitch253(prologue)
    prologue = fix_preview_row253(prologue)
    prologue_path.write_text(prologue)
    print("prologue: cleaned row 253 artifacts")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    epilogue = strip_duplicate_row253_loops(epilogue)
    epilogue_path.write_text(epilogue)
    print("epilogue: cleaned duplicate row 253 loops")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    memory = dedupe_memory_row253(memory)
    memory_path.write_text(memory)
    print("memory-sheet: deduped row 253 table rows")


if __name__ == "__main__":
    main()
