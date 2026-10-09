#!/usr/bin/env python3
"""One-off cleanup: dedupe row-249 inserts and fix row-248 epilogue reference drift."""
from pathlib import Path
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
        r"(\*\*Row 249 closing stitch \(Row 68 → Row 229 Row 68 → Row 49 taxonomy meta prelude capstone reunion\)\.\*\* \{#row-249-closing-stitch\})"
        r"(?: \(Row 68 → Row 229 Row 68 → Row 49 taxonomy meta prelude capstone reunion\)\.\*\* \{#row-249-closing-stitch\})+"
    )
    return re.sub(pattern, r"\1", text)


def fix_epilogue248_body(text: str) -> str:
    start = text.find(
        "### Row 228 closing loop (Row 68 → Row 228 Row 68 → Row 48 midpoint meta prelude capstone reunion) {#row-248-closing-loop}"
    )
    if start == -1:
        return text
    end = text.find("\n\n### Row 249 closing loop", start)
    if end == -1:
        end = text.find("\n\n### Row 227 closing loop", start)
    if end == -1:
        return text
    block = text[start:end]
    repl = [
        ("Row 68 → Row 48 meta (row 208)", "Row 68 → Row 48 meta (row 248)"),
        ("row 229 taxonomy meta prelude capstone opens", "row 249 taxonomy meta prelude capstone opens"),
        ("Recite [preface row 247](../preface.md#skill-navigation-row-187)", "Recite [preface row 247](../preface.md#skill-navigation-row-247)"),
        ("after row 247 alone", "after row 247 alone"),
        ("row 208 (row 68 ↔ row 48 reunion", "row 248 (row 68 ↔ row 48 reunion"),
        ("row 208 (opening-hinge capstone stitch after row 247 alone) — row 208 names", "row 228 (opening-hinge capstone stitch after row 247 alone) — row 228 names"),
        ("row 208 names **why that reunion", "row 248 names **why that reunion"),
    ]
    for old, new in repl:
        block = block.replace(old, new)
    return text[:start] + block + text[end:]


def strip_duplicate_row249_loops(text: str) -> str:
    """Keep only the row-249 loop immediately before the row-248 capstone marker."""
    marker = (
        "### Row 228 closing loop (Row 68 → Row 228 Row 68 → Row 48 midpoint meta prelude capstone reunion) {#row-248-closing-loop}"
    )
    if marker not in text:
        return text
    idx = text.index(marker)
    before = text[:idx]
    after = text[idx:]
    pattern = (
        r"\n\n### Row 249 closing loop \(Row 68 → Row 229 Row 68 → Row 49 "
        r"taxonomy meta prelude capstone reunion\) \{#row-249-closing-loop\}.*?"
        r"(?=\n\n### Row \d+ closing loop|\n\n### Row 228 closing loop)"
    )
    before = re.sub(pattern, "", before, flags=re.DOTALL)
    return before + after


def main() -> None:
    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    prologue = dedupe_adjacent_lines(prologue)
    prologue = fix_prologue_stitch(prologue)
    prologue = prologue.replace(
        "| <span id=\"prologue-preview-row-249\"></span>Row 229 preview",
        "| <span id=\"prologue-preview-row-249\"></span>Row 249 preview",
    )
    prologue_path.write_text(prologue)
    print("prologue: cleaned row 249 artifacts")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    epilogue = strip_duplicate_row249_loops(epilogue)
    epilogue = fix_epilogue248_body(epilogue)
    epilogue_path.write_text(epilogue)
    print("epilogue: cleaned row 249 artifacts")


if __name__ == "__main__":
    main()
