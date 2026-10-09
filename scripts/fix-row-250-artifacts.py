#!/usr/bin/env python3
"""One-off cleanup: dedupe row-250 inserts and fix row-249 epilogue reference drift."""
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


def fix_prologue_stitch(text: str) -> str:
    pattern = (
        r"(\*\*Row 250 closing stitch \(Row 68 → Row 230 Row 68 → Row 50 DDD meta prelude capstone reunion\)\.\*\* \{#row-250-closing-stitch\})"
        r"(?: \(Row 68 → Row 230 Row 68 → Row 50 DDD meta prelude capstone reunion\)\.\*\* \{#row-250-closing-stitch\})+"
    )
    return re.sub(pattern, r"\1", text)


def fix_epilogue249_body(text: str) -> str:
    start = text.find(
        "### Row 229 closing loop (Row 68 → Row 229 Row 68 → Row 49 taxonomy meta prelude capstone reunion) {#row-249-closing-loop}"
    )
    if start == -1:
        return text
    end = text.find("\n\n### Row 250 closing loop", start)
    if end == -1:
        end = text.find("\n\n### Row 230 closing loop", start)
    if end == -1:
        return text
    block = text[start:end]
    repl = [
        ("row 230 DDD meta prelude capstone opens", "row 250 DDD meta prelude capstone opens"),
        ("Proceed to [row 230](#row-230-closing-loop)", "Proceed to [row 250](#row-250-closing-loop)"),
        (
            "Recite [preface row 248](../preface.md#skill-navigation-row-228)",
            "Recite [preface row 248](../preface.md#skill-navigation-row-248)",
        ),
        ("Row 68 → Row 49 meta (row 229)", "Row 68 → Row 49 meta (row 249)"),
    ]
    for old, new in repl:
        block = block.replace(old, new)
    return text[:start] + block + text[end:]


def strip_duplicate_row250_loops(text: str) -> str:
    """Keep only the row-250 loop immediately before the row-249 capstone marker."""
    marker = (
        "### Row 229 closing loop (Row 68 → Row 229 Row 68 → Row 49 taxonomy meta prelude capstone reunion) {#row-249-closing-loop}"
    )
    if marker not in text:
        return text
    idx = text.index(marker)
    before = text[:idx]
    after = text[idx:]
    pattern = (
        r"\n\n### Row 250 closing loop \(Row 68 → Row 230 Row 68 → Row 50 "
        r"DDD meta prelude capstone reunion\) \{#row-250-closing-loop\}.*?"
        r"(?=\n\n### Row \d+ closing loop|\n\n### Row 229 closing loop)"
    )
    before = re.sub(pattern, "", before, flags=re.DOTALL)
    return before + after


def _load_row250_preview() -> str:
    spec = importlib.util.spec_from_file_location("add250", ROOT / "scripts/add-row-250.py")
    add250 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add250)
    return add250._row250_prologue_preview().strip()


def fix_preview_row250(prologue: str) -> str:
    bad_prefix = '| <span id="prologue-preview-row-250"></span>'
    idx = prologue.find(bad_prefix)
    if idx == -1:
        return prologue
    bad_end = prologue.find("\n", idx)
    return prologue[:idx] + _load_row250_preview() + prologue[bad_end:]


def main() -> None:
    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    prologue = dedupe_adjacent_lines(prologue)
    prologue = fix_prologue_stitch(prologue)
    prologue = fix_preview_row250(prologue)
    prologue_path.write_text(prologue)
    print("prologue: cleaned row 250 artifacts")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    epilogue = strip_duplicate_row250_loops(epilogue)
    epilogue = fix_epilogue249_body(epilogue)
    epilogue_path.write_text(epilogue)
    print("epilogue: cleaned row 250 artifacts")


if __name__ == "__main__":
    main()
