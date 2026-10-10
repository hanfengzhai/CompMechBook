#!/usr/bin/env python3
"""Repair row 264 meta-stitch anchors after add-row-264 bump."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ROW264_COMPASS = (
    "| Row 68 → Row 244 Row 68 → Row 64 book-loop meta prelude capstone reunion (row 264) | "
    "[Preface: row 264 skill checkpoint](../preface.md#skill-navigation-row-264) · "
    "[Row 68 → Row 244 book-loop meta prelude capstone reunion index]"
    "(../appendix/sources.md#row68-row244-book-loop-meta-prelude-capstone-reunion-index-row-264) · "
    "[memory sheet row 264 baby picture](../appendix/memory-sheet.md#row-264-baby-picture-row68-row244-book-loop-meta-prelude-capstone-reunion) · "
    "[prologue row 264 preview row](#prologue-preview-row-264); "
    "[prologue row 264 closing stitch](#row-264-closing-stitch); "
    "[epilogue row 264 closing loop](../epilogue/multiscale.md#row-264-closing-loop) — "
    "read row 68 gate + row 263 or row 244 orchestration meta prelude capstone / book-loop meta capstone gate + "
    "epilogue book-loop cross-links + row 64 meta aloud when orchestration verifies after orchestration meta prelude "
    "capstone on the full capstone path but the next terminal opens with copper decks copied blindly without "
    "reopening anchor rung audit |"
)

ROW264_STITCH = (
    "**Row 264 closing stitch (Row 68 → Row 244 Row 68 → Row 64 book-loop meta prelude capstone reunion).** "
    "{#row-264-closing-stitch} When row 263 closed — orchestration meta prelude capstone verified, row 263 or row 244 "
    "recited on the full capstone path, and [`parse_multiscale_workflow.sh`](../../scripts/parse_multiscale_workflow.sh) "
    "archived `multiscale_export.yaml` with H1→H2→H3→H4a→H4b→OUT after verified Handshake 4b meta prelude capstone on "
    "the full capstone path — but **row 64 book-loop meta reunion still opens like standalone epilogue coursework "
    "after verified orchestration on the full capstone path** — read [preface row 264](../preface.md#skill-navigation-row-264), "
    "then the [Row 68 → Row 244 reunion index](../appendix/sources.md#row68-row244-book-loop-meta-prelude-capstone-reunion-index-row-264), "
    "then [epilogue row 264 closing loop](../epilogue/multiscale.md#row-264-closing-loop) before row 265 second-pass meta "
    "prelude capstone reunion opens on the full capstone path.\n\n"
)


def fix_prologue(prologue: str) -> str:
    broken_prefix = (
        "| Row 68 → Row 244 Row 68 → Row 64 book-loop meta prelude capstone reunion (row 264) |"
    )
    if ROW264_COMPASS not in prologue:
        idx = prologue.find(broken_prefix)
        if idx == -1:
            raise SystemExit("prologue row 264 compass not found")
        line_end = prologue.find("\n", idx)
        prologue = prologue[:idx] + ROW264_COMPASS + prologue[line_end:]

    bad_stitch = "**Row 264 closing stitch (Row 68 → Row 264 Row 68 → Row 64 book-loop meta prelude capstone reunion).** {#row-264-closing-stitch}"
    if bad_stitch in prologue:
        prologue = prologue.replace(bad_stitch, ROW264_STITCH.strip(), 1)
    elif "{#row-264-closing-stitch}" not in prologue:
        anchor = (
            "**Row 263 closing stitch (Row 68 → Row 243 Row 68 → Row 63 orchestration meta prelude capstone reunion).** "
            "{#row-263-closing-stitch}"
        )
        if anchor not in prologue:
            raise SystemExit("row 263 stitch anchor not found")
        prologue = prologue.replace(anchor, ROW264_STITCH + anchor, 1)

    chunk_start = prologue.find("prologue-preview-row-264")
    if chunk_start != -1:
        chunk = prologue[chunk_start : chunk_start + 2500]
        fixed = (
            chunk.replace("skill-navigation-row-244", "skill-navigation-row-264")
            .replace("#row-244-closing-stitch", "#row-264-closing-stitch")
            .replace(
                "row68-row224-book-loop-meta-prelude-capstone-reunion-index-row-244",
                "row68-row244-book-loop-meta-prelude-capstone-reunion-index-row-264",
            )
        )
        prologue = prologue[:chunk_start] + fixed + prologue[chunk_start + 2500 :]
    return prologue


def main() -> None:
    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = fix_prologue(prologue_path.read_text())
    prologue_path.write_text(prologue)
    print("prologue: fixed row 264 anchors")


if __name__ == "__main__":
    main()
