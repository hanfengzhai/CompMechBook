#!/usr/bin/env python3
"""Repair row 268 meta-stitch anchors after add-row-268 bump."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ROW268_COMPASS = (
    "| Row 68 → Row 248 Row 68 → Row 48 midpoint meta prelude capstone reunion (row 268) | "
    "[Preface: row 268 skill checkpoint](../preface.md#skill-navigation-row-268) · "
    "[Row 68 → Row 248 midpoint meta prelude capstone reunion index]"
    "(../appendix/sources.md#row68-row248-midpoint-meta-prelude-capstone-reunion-index-row-268) · "
    "[memory sheet row 268 baby picture](../appendix/memory-sheet.md#row-268-baby-picture-row68-row248-midpoint-meta-prelude-capstone-reunion) · "
    "[prologue row 268 preview row](#prologue-preview-row-268); "
    "[prologue row 268 closing stitch](#row-268-closing-stitch); "
    "[epilogue row 268 closing loop](../epilogue/multiscale.md#row-268-closing-loop) — "
    "read row 68 gate + row 267 or row 248 part-boundary meta prelude capstone / midpoint meta prelude gate + "
    "VI.4 intermission → Bridge → VII.0 landing + row 48 meta aloud when part-boundary meta prelude capstone is clean "
    "on the full capstone path but writings/continuum → writings/defects feels like two courses at the knee after "
    "verified twin-ladder reunion on the full capstone path |"
)

ROW268_STITCH = (
    "**Row 268 closing stitch (Row 68 → Row 248 Row 68 → Row 48 midpoint meta prelude capstone reunion).** "
    "{#row-268-closing-stitch} When row 267 closed — part-boundary meta prelude capstone verified on the full "
    "capstone path, row 266 or row 247 recited, and twin-ladder Bridge through VI.0 landing recited with "
    "`cht_export.yaml` beside both decks on the full capstone path — but **row 48 midpoint meta reunion still opens "
    "like standalone defect coursework after VI.4's return-mapping chapter on the full capstone path** — read "
    "[preface row 268](../preface.md#skill-navigation-row-268), then the "
    "[Row 68 → Row 248 reunion index](../appendix/sources.md#row68-row248-midpoint-meta-prelude-capstone-reunion-index-row-268), "
    "then [epilogue row 268 closing loop](../epilogue/multiscale.md#row-268-closing-loop) before row 269 taxonomy "
    "meta prelude capstone reunion opens on the full capstone path.\n\n"
)


def fix_prologue(prologue: str) -> str:
    broken_prefix = (
        "| Row 68 → Row 248 Row 68 → Row 48 midpoint meta prelude capstone reunion (row 268) |"
    )
    if ROW268_COMPASS not in prologue and broken_prefix in prologue:
        idx = prologue.find(broken_prefix)
        line_end = prologue.find("\n", idx)
        prologue = prologue[:idx] + ROW268_COMPASS + prologue[line_end:]

    bad268 = (
        "**Row 268 closing stitch (Row 68 → Row 268 Row 68 → Row 48 midpoint meta prelude capstone reunion).** "
        "{#row-268-closing-stitch}"
    )
    if bad268 in prologue:
        start = prologue.index(bad268)
        end = prologue.find("\n\n**Row 267 closing stitch", start)
        if end == -1:
            end = prologue.find("\n\n**Row 265 closing stitch", start)
        if end != -1:
            prologue = prologue[:start] + ROW268_STITCH + prologue[end + 2 :]
    elif "{#row-268-closing-stitch}" in prologue and ROW268_STITCH.strip() not in prologue:
        anchor = (
            "**Row 267 closing stitch (Row 68 → Row 247 Row 68 → Row 67 part-boundary meta prelude capstone reunion).** "
            "{#row-267-closing-stitch}"
        )
        if anchor in prologue:
            prologue = prologue.replace(anchor, ROW268_STITCH + anchor, 1)

    chunk_start = prologue.find("prologue-preview-row-268")
    if chunk_start != -1:
        chunk = prologue[chunk_start : chunk_start + 3500]
        fixed = (
            chunk.replace("skill-navigation-row-248", "skill-navigation-row-268")
            .replace("Preface: row 248 skill checkpoint", "Preface: row 268 skill checkpoint")
            .replace("prologue row 248 preview", "prologue row 268 preview")
            .replace("prologue row 248 closing stitch", "prologue row 268 closing stitch")
            .replace("epilogue row 248 closing loop", "epilogue row 268 closing loop")
            .replace("memory sheet row 248 baby picture", "memory sheet row 268 baby picture")
            .replace(
                "row68-row228-midpoint-meta-prelude-capstone-reunion-index-row-248",
                "row68-row248-midpoint-meta-prelude-capstone-reunion-index-row-268",
            )
            .replace(
                "row-248-baby-picture-row68-row228-midpoint-meta-prelude-capstone-reunion",
                "row-268-baby-picture-row68-row248-midpoint-meta-prelude-capstone-reunion",
            )
        )
        prologue = prologue[:chunk_start] + fixed + prologue[chunk_start + 3500 :]
    return prologue


def main() -> None:
    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = fix_prologue(prologue_path.read_text())
    prologue_path.write_text(prologue)
    print("prologue: fixed row 268 anchors")


if __name__ == "__main__":
    main()
