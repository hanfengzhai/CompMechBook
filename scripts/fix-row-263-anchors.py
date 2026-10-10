#!/usr/bin/env python3
"""Repair row 263 meta-stitch anchors after add-row-263 bump."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ROW263_COMPASS = (
    "| Row 68 → Row 243 Row 68 → Row 63 orchestration meta prelude capstone reunion (row 263) | "
    "[Preface: row 263 skill checkpoint](../preface.md#skill-navigation-row-263) · "
    "[Row 68 → Row 243 orchestration meta prelude capstone reunion index]"
    "(../appendix/sources.md#row68-row243-orchestration-meta-prelude-capstone-reunion-index-row-263) · "
    "[memory sheet row 263 baby picture](../appendix/memory-sheet.md#row-263-baby-picture-row68-row243-orchestration-meta-prelude-capstone-reunion) · "
    "[prologue row 263 preview row](#prologue-preview-row-263); "
    "[prologue row 263 closing stitch](#row-263-closing-stitch); "
    "[epilogue row 263 closing loop](../epilogue/multiscale.md#row-263-closing-loop) — "
    "read row 68 gate + row 262 or row 243 Handshake 4b meta prelude capstone / orchestration meta capstone gate + "
    "epilogue orchestration cross-links + row 63 meta aloud when Handshakes 1–4b verify individually after verified "
    "Handshake 4b meta prelude capstone on the full capstone path but Act V notch and Act VI foundation still feel "
    "like separate courses |"
)

ROW263_STITCH = (
    "**Row 263 closing stitch (Row 68 → Row 243 Row 68 → Row 63 orchestration meta prelude capstone reunion).** "
    "{#row-263-closing-stitch} When row 262 closed — Handshake 4b meta prelude capstone verified, row 261 or row 242 "
    "recited on the full capstone path, and [`parse_multiscale_workflow.sh`](../../scripts/parse_multiscale_workflow.sh) "
    "archived `multiscale_export.yaml` with H1→H2→H3→H4a→H4b→OUT after verified Handshake 4b meta prelude capstone on "
    "the full capstone path — but **row 63 orchestration meta reunion still opens like standalone epilogue coursework "
    "after verified notch-root parsing on the full capstone path** — read [preface row 263](../preface.md#skill-navigation-row-263), "
    "then the [Row 68 → Row 243 reunion index](../appendix/sources.md#row68-row243-orchestration-meta-prelude-capstone-reunion-index-row-263), "
    "then [epilogue row 263 closing loop](../epilogue/multiscale.md#row-263-closing-loop) before row 264 book-loop meta "
    "prelude capstone reunion opens on the full capstone path.\n\n"
)


def fix_prologue(prologue: str) -> str:
    broken_prefix = (
        "| Row 68 → Row 243 Row 68 → Row 63 orchestration meta prelude capstone reunion (row 263) |"
    )
    if ROW263_COMPASS not in prologue:
        idx = prologue.find(broken_prefix)
        if idx == -1:
            raise SystemExit("prologue row 263 compass not found")
        line_end = prologue.find("\n", idx)
        prologue = prologue[:idx] + ROW263_COMPASS + prologue[line_end:]

    bad_stitch = "**Row 263 closing stitch (Row 68 → Row 263 Row 68 → Row 63 orchestration meta prelude capstone reunion).** {#row-263-closing-stitch}"
    if bad_stitch in prologue:
        prologue = prologue.replace(bad_stitch, ROW263_STITCH.strip(), 1)
    elif "{#row-263-closing-stitch}" not in prologue:
        anchor = (
            "**Row 262 closing stitch (Row 68 → Row 242 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion).** "
            "{#row-262-closing-stitch}"
        )
        if anchor not in prologue:
            raise SystemExit("row 262 stitch anchor not found")
        prologue = prologue.replace(anchor, ROW263_STITCH + anchor, 1)

    chunk_start = prologue.find("prologue-preview-row-263")
    if chunk_start != -1:
        chunk = prologue[chunk_start : chunk_start + 2500]
        fixed = (
            chunk.replace("skill-navigation-row-243", "skill-navigation-row-263")
            .replace("#row-243-closing-stitch", "#row-263-closing-stitch")
            .replace(
                "row68-row223-orchestration-meta-prelude-capstone-reunion-index-row-243",
                "row68-row243-orchestration-meta-prelude-capstone-reunion-index-row-263",
            )
        )
        prologue = prologue[:chunk_start] + fixed + prologue[chunk_start + 2500 :]
    return prologue


def main() -> None:
    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = fix_prologue(prologue_path.read_text())
    prologue_path.write_text(prologue)
    print("prologue: fixed row 263 anchors")


if __name__ == "__main__":
    main()
