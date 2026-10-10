#!/usr/bin/env python3
"""Repair row 265 meta-stitch anchors after add-row-265 bump."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ROW265_COMPASS = (
    "| Row 68 → Row 245 Row 68 → Row 65 second-pass meta prelude capstone reunion (row 265) | "
    "[Preface: row 265 skill checkpoint](../preface.md#skill-navigation-row-265) · "
    "[Row 68 → Row 245 second-pass meta prelude capstone reunion index]"
    "(../appendix/sources.md#row68-row245-second-pass-meta-prelude-capstone-reunion-index-row-265) · "
    "[memory sheet row 265 baby picture](../appendix/memory-sheet.md#row-265-baby-picture-row68-row245-second-pass-meta-prelude-capstone-reunion) · "
    "[prologue row 265 preview row](#prologue-preview-row-265); "
    "[prologue row 265 closing stitch](#row-265-closing-stitch); "
    "[epilogue row 265 closing loop](../epilogue/multiscale.md#row-265-closing-loop) — "
    "read row 68 gate + row 264 or row 245 book-loop meta prelude capstone / second-pass meta capstone gate + "
    "epilogue second-pass cross-links + row 65 meta aloud when the book loop closes on the full capstone path but "
    "every chapter boundary still opens a skill checkpoint instead of trusting Scene → Bridge rhythm |"
)

ROW265_STITCH = (
    "**Row 265 closing stitch (Row 68 → Row 245 Row 68 → Row 65 second-pass meta prelude capstone reunion).** "
    "{#row-265-closing-stitch} When row 264 closed — book-loop meta prelude capstone verified, row 264 or row 245 "
    "recited on the full capstone path, and the [prologue reopening anchor](#prologue-reopening-anchor) received the "
    "reader with `./scripts/test-fixtures.sh` green after verified book-loop meta prelude capstone on the full "
    "capstone path — but **row 65 second-pass meta reunion still opens like standalone appendix coursework after "
    "verified book-loop on the full capstone path** — read [preface row 265](../preface.md#skill-navigation-row-265), "
    "then the [Row 68 → Row 245 reunion index](../appendix/sources.md#row68-row245-second-pass-meta-prelude-capstone-reunion-index-row-265), "
    "then [epilogue row 265 closing loop](../epilogue/multiscale.md#row-265-closing-loop) before row 266 Writings "
    "canonical meta prelude capstone reunion opens on the full capstone path.\n\n"
)


def fix_prologue(prologue: str) -> str:
    broken_prefix = (
        "| Row 68 → Row 245 Row 68 → Row 65 second-pass meta prelude capstone reunion (row 265) |"
    )
    if ROW265_COMPASS not in prologue:
        idx = prologue.find(broken_prefix)
        if idx == -1:
            raise SystemExit("prologue row 265 compass not found")
        line_end = prologue.find("\n", idx)
        prologue = prologue[:idx] + ROW265_COMPASS + prologue[line_end:]

    bad_stitch = (
        "**Row 265 closing stitch (Row 68 → Row 265 Row 68 → Row 65 second-pass meta prelude capstone reunion).** "
        "{#row-265-closing-stitch}"
    )
    if bad_stitch in prologue:
        prologue = prologue.replace(bad_stitch, ROW265_STITCH.strip(), 1)

    chunk_start = prologue.find("prologue-preview-row-265")
    if chunk_start != -1:
        chunk = prologue[chunk_start : chunk_start + 2800]
        fixed = (
            chunk.replace("skill-navigation-row-245", "skill-navigation-row-265")
            .replace("#row-245-closing-stitch", "#row-265-closing-stitch")
            .replace(
                "row68-row225-second-pass-meta-prelude-capstone-reunion-index-row-245",
                "row68-row245-second-pass-meta-prelude-capstone-reunion-index-row-265",
            )
            .replace("#row-245-closing-loop", "#row-265-closing-loop")
        )
        prologue = prologue[:chunk_start] + fixed + prologue[chunk_start + 2800 :]
    return prologue


def main() -> None:
    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = fix_prologue(prologue_path.read_text())
    prologue_path.write_text(prologue)
    print("prologue: fixed row 265 anchors")


if __name__ == "__main__":
    main()
