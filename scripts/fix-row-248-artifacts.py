#!/usr/bin/env python3
"""One-off cleanup: dedupe row-248 prologue inserts and fix epilogue row references."""
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
    # Collapse repeated stitch header fragments from double-insert
    pattern = (
        r"(\*\*Row 248 closing stitch \(Row 68 → Row 228 Row 68 → Row 48 midpoint meta prelude capstone reunion\)\.\*\* \{#row-248-closing-stitch\})"
        r"(?: \(Row 68 → Row 228 Row 68 → Row 48 midpoint meta prelude capstone reunion\)\.\*\* \{#row-248-closing-stitch\})+"
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
        ("memory sheet row 208", "memory sheet row 248"),
        ("preface row 208 skill checkpoint", "preface row 248 skill checkpoint"),
        ("prologue row 208 preview", "prologue row 248 preview"),
        ("prologue row 208 closing stitch", "prologue row 248 closing stitch"),
        ("row 187 closed part-boundary", "row 247 closed part-boundary"),
        ("after row 187 alone", "after row 247 alone"),
        ("Recite [preface row 187]", "Recite [preface row 247]"),
        ("Row 208 closes", "Row 248 closes"),
        ("(row 187)", "(row 247)"),
        ("row 208) and Row 68 → Row 48 meta (row 208)", "row 248) and Row 68 → Row 48 meta (row 248)"),
        ("row 189 taxonomy meta prelude capstone opens", "row 229 taxonomy meta prelude capstone opens"),
        ("Prologue preview ([row 208]", "Prologue preview ([row 248]"),
        ("| [Preface row 208]", "| [Preface row 248]"),
        ("The [memory sheet row 208 baby picture]", "The [memory sheet row 248 baby picture]"),
        (
            "Do not conflate row 208 (row 68 ↔ row 48 reunion on the full capstone path) with row 208 (opening-hinge capstone stitch after row 187 alone) — row 208 names **Row 68 → Row 228 Row 68 → Row 48 midpoint meta prelude capstone reunion**; row 208 names **why that reunion must follow verified part-boundary meta prelude capstone on the full capstone path (row 187)",
            "Do not conflate row 248 (row 68 ↔ row 48 reunion on the full capstone path) with row 228 (opening-hinge capstone stitch after row 227 alone) — row 228 names **Row 68 → Row 208 Row 68 → Row 48 midpoint meta prelude capstone reunion**; row 248 names **why that reunion must follow verified part-boundary meta prelude capstone on the full capstone path (row 247)",
        ),
        ("Proceed to [row 209](#row-209-closing-loop) when row 68 closed but taxonomy meta prelude capstone still lags after row 228 on the full capstone path",
         "Proceed to [row 249](#row-249-closing-loop) when row 68 closed but taxonomy meta prelude capstone still lags after row 248 on the full capstone path"),
        ("to [row 187](#row-167-closing-loop) when part-boundary meta prelude capstone still lags",
         "to [row 247](#row-227-closing-loop) when part-boundary meta prelude capstone still lags"),
    ]
    for old, new in repl:
        block = block.replace(old, new)
    return text[:start] + block + text[end:]


def main() -> None:
    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    prologue = dedupe_adjacent_lines(prologue)
    prologue = fix_prologue_stitch(prologue)
    prologue = prologue.replace(
        "midpoint meta prelude capstone reunion (row 228) |",
        "midpoint meta prelude capstone reunion (row 248) |",
    )
    prologue = prologue.replace(
        "[Preface: row 228 skill checkpoint]",
        "[Preface: row 248 skill checkpoint]",
    )
    prologue = prologue.replace(
        "row 227 or row 208 part-boundary",
        "row 247 or row 228 part-boundary",
    )
    prologue = prologue.replace(
        "| <span id=\"prologue-preview-row-248\"></span>Row 228 preview",
        "| <span id=\"prologue-preview-row-248\"></span>Row 248 preview",
    )
    prologue = prologue.replace(
        "[preface row 228 skill checkpoint]",
        "[preface row 248 skill checkpoint]",
    )
    prologue_path.write_text(prologue)
    print("prologue: cleaned row 248 artifacts")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    epilogue = epilogue.replace(
        "Proceed to [row 248](#row-228-closing-loop) when row 68 closed but midpoint meta prelude capstone still lags after row 247 on the full capstone path,",
        "Proceed to [row 248](#row-248-closing-loop) when row 68 closed but midpoint meta prelude capstone still lags after row 247 on the full capstone path,",
    )
    epilogue = fix_epilogue248_body(epilogue)
    epilogue_path.write_text(epilogue)
    print("epilogue: fixed row 248 body and row 247 proceed link")


if __name__ == "__main__":
    main()
