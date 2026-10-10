#!/usr/bin/env python3
"""Repair row 266 meta-stitch anchors after add-row-266 bump."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ROW266_COMPASS = (
    "| Row 68 → Row 246 Row 68 → Row 66 Writings canonical meta prelude capstone reunion (row 266) | "
    "[Preface: row 266 skill checkpoint](../preface.md#skill-navigation-row-266) · "
    "[Row 68 → Row 246 Writings canonical meta prelude capstone reunion index]"
    "(../appendix/sources.md#row68-row246-writings-meta-prelude-capstone-reunion-index-row-266) · "
    "[memory sheet row 266 baby picture](../appendix/memory-sheet.md#row-266-baby-picture-row68-row266-writings-meta-prelude-capstone-reunion) · "
    "[prologue row 266 preview row](#prologue-preview-row-266); "
    "[prologue row 266 closing stitch](#row-266-closing-stitch); "
    "[epilogue row 266 closing loop](../epilogue/multiscale.md#row-266-closing-loop) — "
    "read row 68 gate + row 265 or row 246 second-pass meta prelude capstone / Writings canonical meta prelude gate + "
    "epilogue writings cross-links + row 66 meta aloud when second pass reads as a novel on the full capstone path but "
    "the next edit opens src/part* instead of writings/ subtrees |"
)

ROW266_STITCH = (
    "**Row 266 closing stitch (Row 68 → Row 246 Row 68 → Row 66 Writings canonical meta prelude capstone reunion).** "
    "{#row-266-closing-stitch} When row 265 closed — second-pass meta prelude capstone verified, row 265 or row 245 "
    "recited on the full capstone path, and the [prologue reopening anchor](#prologue-reopening-anchor) received the "
    "reader with `./scripts/test-fixtures.sh` green after verified second-pass meta prelude capstone on the full "
    "capstone path — but **row 66 Writings canonical meta reunion still opens like standalone maintainer coursework after "
    "verified novel rhythm on the full capstone path** — read [preface row 266](../preface.md#skill-navigation-row-266), "
    "then the [Row 68 → Row 246 reunion index](../appendix/sources.md#row68-row246-writings-meta-prelude-capstone-reunion-index-row-266), "
    "then [epilogue row 266 closing loop](../epilogue/multiscale.md#row-266-closing-loop) before row 267 part-boundary "
    "meta prelude capstone reunion opens on the full capstone path.\n\n"
)


def fix_prologue(prologue: str) -> str:
    broken_prefix = (
        "| Row 68 → Row 246 Row 68 → Row 66 Writings canonical meta prelude capstone reunion (row 266) |"
    )
    if ROW266_COMPASS not in prologue:
        idx = prologue.find(broken_prefix)
        if idx == -1:
            raise SystemExit("prologue row 266 compass not found")
        line_end = prologue.find("\n", idx)
        prologue = prologue[:idx] + ROW266_COMPASS + prologue[line_end:]

    bad_stitch = (
        "**Row 266 closing stitch (Row 68 → Row 266 Row 68 → Row 66 Writings canonical meta prelude capstone reunion).** "
        "{#row-266-closing-stitch}"
    )
    if bad_stitch in prologue:
        prologue = prologue.replace(bad_stitch, ROW266_STITCH.strip(), 1)

    chunk_start = prologue.find("prologue-preview-row-266")
    if chunk_start != -1:
        chunk = prologue[chunk_start : chunk_start + 3200]
        fixed = (
            chunk.replace("skill-navigation-row-246", "skill-navigation-row-266")
            .replace("#row-246-closing-stitch", "#row-266-closing-stitch")
            .replace(
                "row68-row226-writings-meta-prelude-capstone-reunion-index-row-246",
                "row68-row246-writings-meta-prelude-capstone-reunion-index-row-266",
            )
            .replace("#row-246-closing-loop", "#row-266-closing-loop")
            .replace(
                "row-246-baby-picture-row68-row226-writings-meta-prelude-capstone-reunion",
                "row-266-baby-picture-row68-row266-writings-meta-prelude-capstone-reunion",
            )
        )
        prologue = prologue[:chunk_start] + fixed + prologue[chunk_start + 3200 :]
    return prologue


def main() -> None:
    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = fix_prologue(prologue_path.read_text())
    prologue_path.write_text(prologue)
    print("prologue: fixed row 266 anchors")


if __name__ == "__main__":
    main()
