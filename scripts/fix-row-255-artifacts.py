#!/usr/bin/env python3
"""One-off cleanup: dedupe row-255 epilogue loops and fix prologue stitch header."""
from pathlib import Path
import importlib.util
import re

ROOT = Path(__file__).resolve().parents[1]

ROW255_LOOP_HEADER = (
    "### Row 255 closing loop (Row 68 → Row 235 Row 68 → Row 55 electronic audit meta prelude capstone reunion) "
    "{#row-255-closing-loop}"
)
ROW252_MARKER = (
    "### Row 252 closing loop (Row 68 → Row 232 Row 68 → Row 52 atomistic meta prelude capstone reunion) "
    "{#row-252-closing-loop}"
)


def strip_all_row255_loops(text: str) -> str:
    pattern = (
        r"\n\n### Row 255 closing loop \(Row 68 → Row \d+ Row 68 → Row 55 "
        r"electronic audit meta prelude capstone reunion\) \{#row-255-closing-loop\}.*?"
        r"(?=\n\n### Row \d+ closing loop|\Z)"
    )
    return re.sub(pattern, "", text, flags=re.DOTALL)


def fix_prologue_stitch255(prologue: str) -> str:
    pattern = (
        r"\*\*Row 235 closing stitch \(Row 68 → Row 235 Row 68 → Row 55 electronic audit meta prelude capstone reunion\)\.\*\* "
        r"\{#row-255-closing-stitch\}"
    )
    return re.sub(
        pattern,
        "**Row 255 closing stitch (Row 68 → Row 235 Row 68 → Row 55 electronic audit meta prelude capstone reunion).** {#row-255-closing-stitch}",
        prologue,
        count=1,
    )


def fix_preview_index_links(prologue: str) -> str:
    return prologue.replace(
        "row68-row235-electronic-audit-meta-prelude-capstone-reunion-index-row-255",
        "row68-row255-electronic-audit-meta-prelude-capstone-reunion-index-row-255",
    )


def dedupe_memory_row255(memory: str) -> str:
    needle = "| 255 | Meta | [Row 68 → Row 235 electronic audit meta prelude capstone reunion index]"
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
    spec = importlib.util.spec_from_file_location("add255", ROOT / "scripts/add-row-255.py")
    add255 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add255)
    loop_block = add255._build_blocks()["epilogue_loop"].rstrip() + "\n\n"

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    epilogue = strip_all_row255_loops(epilogue)
    row254_proceed = (
        "Proceed to [row 215](#row-215-closing-loop) when row 68 closed but electronic audit meta prelude capstone still lags after row 234 on the full capstone path,"
    )
    if row254_proceed in epilogue:
        epilogue = epilogue.replace(
            row254_proceed,
            "Proceed to [row 255](#row-255-closing-loop) when row 68 closed but electronic audit meta prelude capstone still lags after row 254 on the full capstone path,",
            1,
        )
    if ROW252_MARKER not in epilogue:
        raise SystemExit("row 252 capstone marker missing from epilogue")
    if ROW255_LOOP_HEADER.split("{")[0] not in epilogue:
        epilogue = epilogue.replace(ROW252_MARKER, loop_block + ROW252_MARKER, 1)
    epilogue_path.write_text(epilogue)
    print("epilogue: row 255 loop canonicalized before row 252")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = fix_prologue_stitch255(prologue_path.read_text())
    prologue = fix_preview_index_links(prologue)
    prologue_path.write_text(prologue)
    print("prologue: row 255 stitch and index links fixed")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = dedupe_memory_row255(memory_path.read_text())
    memory_path.write_text(memory)
    print("memory-sheet: deduped row 255 table row if needed")


if __name__ == "__main__":
    main()
