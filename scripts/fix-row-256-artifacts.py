#!/usr/bin/env python3
"""One-off cleanup: dedupe row-256 epilogue loops and fix prologue stitch header."""
from pathlib import Path
import importlib.util
import re

ROOT = Path(__file__).resolve().parents[1]

ROW256_INSERT_MARKER = (
    "### Row 255 closing loop (Row 68 → Row 235 Row 68 → Row 55 electronic audit meta prelude capstone reunion) "
    "{#row-255-closing-loop}"
)
ROW256_LOOP_HEADER = (
    "### Row 256 closing loop (Row 68 → Row 236 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion) "
    "{#row-256-closing-loop}"
)


def strip_misplaced_row256_loops(text: str) -> str:
    if ROW256_INSERT_MARKER not in text:
        return text
    cap_idx = text.index(ROW256_INSERT_MARKER)
    pattern = (
        r"\n\n### Row 256 closing loop \(Row 68 → Row \d+ Row 68 → Row 56 "
        r"Born–Oppenheimer meta prelude capstone reunion\) \{#row-256-closing-loop\}.*?"
        r"(?=\n\n### Row \d+ closing loop|\Z)"
    )

    def repl(m: re.Match[str]) -> str:
        if m.start() >= cap_idx:
            return m.group(0)
        return ""

    return re.sub(pattern, repl, text, flags=re.DOTALL)


def fix_row236_wrong_anchor(epilogue: str) -> str:
    """Restore row-236 closing-loop id when header says Row 216/236 but anchor says row-256."""
    return epilogue.replace(
        "### Row 216 closing loop (Row 68 → Row 216 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion) {#row-256-closing-loop}",
        "### Row 216 closing loop (Row 68 → Row 216 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion) {#row-236-closing-loop}",
    ).replace(
        "### Row 236 closing loop (Row 68 → Row 236 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion) {#row-256-closing-loop}",
        "### Row 236 closing loop (Row 68 → Row 236 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion) {#row-236-closing-loop}",
    )


def fix_prologue_stitch256(prologue: str) -> str:
    pattern = (
        r"\*\*Row 236 closing stitch \(Row 68 → Row 236 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion\)\.\*\* "
        r"\{#row-256-closing-stitch\}"
    )
    return re.sub(
        pattern,
        "**Row 256 closing stitch (Row 68 → Row 236 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion).** {#row-256-closing-stitch}",
        prologue,
        count=1,
    )


def fix_preview_index_links(prologue: str) -> str:
    return prologue.replace(
        "row68-row236-born-oppenheimer-meta-prelude-capstone-reunion-index-row-256",
        "row68-row256-born-oppenheimer-meta-prelude-capstone-reunion-index-row-256",
    )


def dedupe_memory_row256(memory: str) -> str:
    needle = "| 256 | Meta | [Row 68 → Row 236 Born–Oppenheimer meta prelude capstone reunion index]"
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
    spec = importlib.util.spec_from_file_location("add256", ROOT / "scripts/add-row-256.py")
    add256 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add256)
    loop_block = add256._build_blocks()["epilogue_loop"].rstrip() + "\n\n"

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    epilogue = strip_misplaced_row256_loops(epilogue)
    epilogue = fix_row236_wrong_anchor(epilogue)
    if ROW256_INSERT_MARKER in epilogue and not add256._epilogue_has_row256_at_capstone(epilogue):
        epilogue = epilogue.replace(ROW256_INSERT_MARKER, loop_block + ROW256_INSERT_MARKER, 1)
    epilogue_path.write_text(epilogue)
    print("epilogue: row 256 artifacts fixed")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    prologue = fix_prologue_stitch256(prologue)
    prologue = fix_preview_index_links(prologue)
    prologue_path.write_text(prologue)
    print("prologue: row 256 stitch/index fixed")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = dedupe_memory_row256(memory_path.read_text())
    memory_path.write_text(memory)
    print("memory-sheet: deduped row 256 table row")


if __name__ == "__main__":
    main()
