#!/usr/bin/env python3
"""One-off cleanup: dedupe row-251 inserts and fix row-250 prologue stitch gap."""
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


def fix_prologue_stitch249(text: str) -> str:
    pattern = (
        r"(\*\*Row 249 closing stitch \(Row 68 → Row 229 Row 68 → Row 49 taxonomy meta prelude capstone reunion\)\.\*\* \{#row-249-closing-stitch\})"
        r"(?: \(Row 68 → Row 229 Row 68 → Row 49 taxonomy meta prelude capstone reunion\)\.\*\* \{#row-249-closing-stitch\})+"
    )
    return re.sub(pattern, r"\1", text)


def fix_prologue_stitch251(text: str) -> str:
    pattern = (
        r"(\*\*Row 251 closing stitch \(Row 68 → Row 231 Row 68 → Row 51 homogenization meta prelude capstone reunion\)\.\*\* \{#row-251-closing-stitch\})"
        r"(?: \(Row 68 → Row 231 Row 68 → Row 51 homogenization meta prelude capstone reunion\)\.\*\* \{#row-251-closing-stitch\})+"
    )
    return re.sub(pattern, r"\1", text)


def strip_duplicate_row251_loops(text: str) -> str:
    """Keep only the row-251 loop immediately before the row-250 capstone marker."""
    marker = (
        "### Row 230 closing loop (Row 68 → Row 230 Row 68 → Row 50 "
        "DDD meta prelude capstone reunion) {#row-250-closing-loop}"
    )
    if marker not in text:
        return text
    idx = text.index(marker)
    before = text[:idx]
    after = text[idx:]
    pattern = (
        r"\n\n### Row 251 closing loop \(Row 68 → Row 231 Row 68 → Row 51 "
        r"homogenization meta prelude capstone reunion\) \{#row-251-closing-loop\}.*?"
        r"(?=\n\n### Row \d+ closing loop|\n\n### Row 230 closing loop)"
    )
    matches = list(re.finditer(pattern, before, flags=re.DOTALL))
    if len(matches) <= 1:
        return text
    # Keep the last match before the marker (capstone-adjacent).
    keep = matches[-1]
    for m in reversed(matches[:-1]):
        before = before[: m.start()] + before[m.end() :]
    return before + after


def _load_row250_stitch() -> str:
    spec = importlib.util.spec_from_file_location("add250", ROOT / "scripts/add-row-250.py")
    add250 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add250)
    b230 = add250._load_add230()._build_blocks()
    return add250.bump230_to_250(b230["prologue_stitch"].strip()) + "\n\n"


def ensure_row250_stitch(prologue: str) -> str:
    if "{#row-250-closing-stitch}" in prologue:
        return prologue
    anchor = (
        "**Row 249 closing stitch (Row 68 → Row 229 Row 68 → Row 49 taxonomy meta prelude capstone reunion).** {#row-249-closing-stitch}"
    )
    if anchor not in prologue:
        return prologue
    return prologue.replace(anchor, _load_row250_stitch() + anchor, 1)


def fix_preview_row251(prologue: str) -> str:
    spec = importlib.util.spec_from_file_location("add251", ROOT / "scripts/add-row-251.py")
    add251 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add251)
    good = add251._row251_prologue_preview().strip()
    bad_prefix = '| <span id="prologue-preview-row-251"></span>'
    idx = prologue.find(bad_prefix)
    if idx == -1:
        return prologue
    bad_end = prologue.find("\n", idx)
    return prologue[:idx] + good + prologue[bad_end:]


def dedupe_memory_row251(memory: str) -> str:
    needle = "| 251 | Meta | [Row 68 → Row 231 homogenization meta prelude capstone reunion index]"
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
    prologue = fix_prologue_stitch249(prologue)
    prologue = fix_prologue_stitch251(prologue)
    prologue = ensure_row250_stitch(prologue)
    prologue = fix_preview_row251(prologue)
    prologue_path.write_text(prologue)
    print("prologue: cleaned row 251 artifacts")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    epilogue = strip_duplicate_row251_loops(epilogue)
    epilogue_path.write_text(epilogue)
    print("epilogue: cleaned duplicate row 251 loops")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    memory = dedupe_memory_row251(memory)
    memory_path.write_text(memory)
    print("memory-sheet: deduped row 251 table rows")


if __name__ == "__main__":
    main()
