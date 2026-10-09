#!/usr/bin/env python3
"""One-off cleanup: dedupe row-257 epilogue loops and fix prologue stitch header."""
from pathlib import Path
import importlib.util
import re

ROOT = Path(__file__).resolve().parents[1]

ROW257_INSERT_MARKER = (
    "### Row 236 closing loop (Row 68 → Row 236 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion) "
    "{#row-256-closing-loop}"
)


def strip_misplaced_row257_loops(text: str) -> str:
    if ROW257_INSERT_MARKER not in text:
        return text
    cap_idx = text.index(ROW257_INSERT_MARKER)
    pattern = (
        r"\n\n### Row 257 closing loop \(Row 68 → Row \d+ Row 68 → Row 57 "
        r"Kohn–Sham meta prelude capstone reunion\) \{#row-257-closing-loop\}.*?"
        r"(?=\n\n### Row \d+ closing loop|\Z)"
    )

    def repl(m: re.Match[str]) -> str:
        if m.start() >= cap_idx:
            return m.group(0)
        return ""

    return re.sub(pattern, repl, text, flags=re.DOTALL)


def fix_row237_wrong_anchor(epilogue: str) -> str:
    """Restore row-237 closing-loop id when header says Row 217/237 but anchor says row-257."""
    return epilogue.replace(
        "### Row 217 closing loop (Row 68 → Row 217 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion) {#row-257-closing-loop}",
        "### Row 217 closing loop (Row 68 → Row 217 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion) {#row-237-closing-loop}",
    ).replace(
        "### Row 237 closing loop (Row 68 → Row 237 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion) {#row-257-closing-loop}",
        "### Row 237 closing loop (Row 68 → Row 237 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion) {#row-237-closing-loop}",
    )


def fix_prologue_stitch257(prologue: str) -> str:
    pattern = (
        r"\*\*Row 237 closing stitch \(Row 68 → Row 237 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion\)\.\*\* "
        r"\{#row-257-closing-stitch\}"
    )
    return re.sub(
        pattern,
        "**Row 257 closing stitch (Row 68 → Row 237 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion).** {#row-257-closing-stitch}",
        prologue,
        count=1,
    )


def fix_preview_index_links(prologue: str) -> str:
    return prologue.replace(
        "row68-row237-kohn-sham-meta-prelude-capstone-reunion-index-row-257",
        "row68-row257-kohn-sham-meta-prelude-capstone-reunion-index-row-257",
    )


def dedupe_memory_row257(memory: str) -> str:
    needle = "| 257 | Meta | [Row 68 → Row 237 Kohn–Sham meta prelude capstone reunion index]"
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
    spec = importlib.util.spec_from_file_location("add257", ROOT / "scripts/add-row-257.py")
    add257 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add257)
    loop_block = add257._build_blocks()["epilogue_loop"].rstrip() + "\n\n"

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    epilogue = strip_misplaced_row257_loops(epilogue)
    epilogue = fix_row237_wrong_anchor(epilogue)
    if ROW257_INSERT_MARKER in epilogue and not add257._epilogue_has_row257_at_capstone(epilogue):
        epilogue = epilogue.replace(ROW257_INSERT_MARKER, loop_block + ROW257_INSERT_MARKER, 1)
    epilogue_path.write_text(epilogue)
    print("epilogue: row 257 artifacts fixed")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    prologue = fix_prologue_stitch257(prologue)
    prologue = fix_preview_index_links(prologue)
    prologue_path.write_text(prologue)
    print("prologue: row 257 stitch/index fixed")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = dedupe_memory_row257(memory_path.read_text())
    memory_path.write_text(memory)
    print("memory-sheet: deduped row 257 table row")


if __name__ == "__main__":
    main()
