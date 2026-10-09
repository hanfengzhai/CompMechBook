#!/usr/bin/env python3
"""One-off cleanup: dedupe row-252 inserts and fix prologue/epilogue artifacts."""
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


def fix_prologue_stitch252(text: str) -> str:
    pattern = (
        r"\*\*Row (?:232|252) closing stitch \(Row 68 → Row 232 Row 68 → Row 52 atomistic meta prelude capstone reunion\)\.\*\* \{#row-252-closing-stitch\}"
        r"(?: \(Row 68 → Row 232 Row 68 → Row 52 atomistic meta prelude capstone reunion\)\.\*\* \{#row-252-closing-stitch\})*"
    )
    text = re.sub(
        pattern,
        "**Row 252 closing stitch (Row 68 → Row 232 Row 68 → Row 52 atomistic meta prelude capstone reunion).** {#row-252-closing-stitch}",
        text,
        count=1,
    )
    return text


def fix_preview_row252(prologue: str) -> str:
    spec = importlib.util.spec_from_file_location("add252", ROOT / "scripts/add-row-252.py")
    add252 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add252)
    good = add252._row252_prologue_preview().strip()
    bad_prefix = '| <span id="prologue-preview-row-252"></span>'
    idx = prologue.find(bad_prefix)
    if idx == -1:
        return prologue
    bad_end = prologue.find("\n", idx)
    return prologue[:idx] + good + prologue[bad_end:]


def strip_duplicate_row252_loops(text: str) -> str:
    marker = (
        "### Row 231 closing loop (Row 68 → Row 231 Row 68 → Row 51 "
        "homogenization meta prelude capstone reunion) {#row-251-closing-loop}"
    )
    if marker not in text:
        return text
    idx = text.index(marker)
    before = text[:idx]
    after = text[idx:]
    pattern = (
        r"\n\n### Row 252 closing loop \(Row 68 → Row 232 Row 68 → Row 52 "
        r"atomistic meta prelude capstone reunion\) \{#row-252-closing-loop\}.*?"
        r"(?=\n\n### Row \d+ closing loop|\n\n### Row 231 closing loop)"
    )
    matches = list(re.finditer(pattern, before, flags=re.DOTALL))
    if len(matches) <= 1:
        return text
    for m in reversed(matches[:-1]):
        before = before[: m.start()] + before[m.end() :]
    return before + after


def dedupe_memory_row252(memory: str) -> str:
    needle = "| 252 | Meta | [Row 68 → Row 232 atomistic meta prelude capstone reunion index]"
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
    prologue = fix_prologue_stitch252(prologue)
    prologue = fix_preview_row252(prologue)
    prologue_path.write_text(prologue)
    print("prologue: cleaned row 252 artifacts")

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    preface = preface.replace(
        "[row 252](preface.md#skill-navigation-row-232) when homogenization meta prelude capstone is clean but atomistic",
        "[row 252](preface.md#skill-navigation-row-252) when homogenization meta prelude capstone is clean but atomistic",
    )
    preface_path.write_text(preface)
    print("preface: fixed row 251 → row 252 proceed link where needed")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    epilogue = strip_duplicate_row252_loops(epilogue)
    epilogue_path.write_text(epilogue)
    print("epilogue: cleaned duplicate row 252 loops")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    memory = dedupe_memory_row252(memory)
    memory_path.write_text(memory)
    print("memory-sheet: deduped row 252 table rows")


if __name__ == "__main__":
    main()
