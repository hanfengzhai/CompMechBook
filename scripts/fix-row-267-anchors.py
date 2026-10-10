#!/usr/bin/env python3
"""Repair row 267 meta-stitch anchors after add-row-267 bump."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ROW267_COMPASS = (
    "| Row 68 → Row 247 Row 68 → Row 67 part-boundary meta prelude capstone reunion (row 267) | "
    "[Preface: row 267 skill checkpoint](../preface.md#skill-navigation-row-267) · "
    "[Row 68 → Row 247 part-boundary meta prelude capstone reunion index]"
    "(../appendix/sources.md#row68-row247-part-boundary-meta-prelude-capstone-reunion-index-row-267) · "
    "[memory sheet row 267 baby picture](../appendix/memory-sheet.md#row-267-baby-picture-row68-row247-part-boundary-meta-prelude-capstone-reunion) · "
    "[prologue row 267 preview row](#prologue-preview-row-267); "
    "[prologue row 267 closing stitch](#row-267-closing-stitch); "
    "[epilogue row 267 closing loop](../epilogue/multiscale.md#row-267-closing-loop) — "
    "read row 68 gate + row 266 or row 247 Writings canonical meta prelude capstone / part-boundary meta prelude gate + "
    "V.4 Bridge → VI.0 twin-ladder landing + row 67 meta aloud when canonical tree is clean on the full capstone path but "
    "writings/fvm → writings/continuum feels like two courses after verified Writings meta prelude capstone on the full capstone path |"
)

ROW267_STITCH = (
    "**Row 267 closing stitch (Row 68 → Row 247 Row 68 → Row 67 part-boundary meta prelude capstone reunion).** "
    "{#row-267-closing-stitch} When row 266 closed — Writings canonical meta prelude capstone verified on the full "
    "capstone path, row 265 or row 246 recited, and `./scripts/sync-writings.sh --check` green with prose under "
    "`writings/` only — but **row 67 part-boundary meta reunion still opens like standalone elasticity coursework after "
    "Navier–Stokes on the full capstone path** — read [preface row 267](../preface.md#skill-navigation-row-267), then "
    "the [Row 68 → Row 247 reunion index](../appendix/sources.md#row68-row247-part-boundary-meta-prelude-capstone-reunion-index-row-267), "
    "then [epilogue row 267 closing loop](../epilogue/multiscale.md#row-267-closing-loop) before row 268 midpoint meta "
    "prelude capstone reunion opens on the full capstone path.\n\n"
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
        "| Row 68 → Row 247 Row 68 → Row 67 part-boundary meta prelude capstone reunion (row 267) |"
    )
    if ROW267_COMPASS not in prologue and broken_prefix in prologue:
        idx = prologue.find(broken_prefix)
        line_end = prologue.find("\n", idx)
        prologue = prologue[:idx] + ROW267_COMPASS + prologue[line_end:]

    if "**Row 266 closing stitch" not in prologue:
        anchor = (
            "**Row 265 closing stitch (Row 68 → Row 245 Row 68 → Row 65 second-pass meta prelude capstone reunion).** "
            "{#row-265-closing-stitch}"
        )
        if anchor in prologue:
            prologue = prologue.replace(anchor, ROW266_STITCH + anchor, 1)

    bad267 = (
        "**Row 267 closing stitch (Row 68 → Row 267 Row 68 → Row 67 part-boundary meta prelude capstone reunion).** "
        "{#row-267-closing-stitch}"
    )
    if bad267 in prologue:
        prologue = prologue.replace(bad267, ROW267_STITCH.strip(), 1)
    elif "{#row-267-closing-stitch}" not in prologue and "**Row 267 closing stitch" in prologue:
        pass
    elif "{#row-267-closing-stitch}" not in prologue:
        preview = prologue.find("prologue-preview-row-267")
        if preview != -1 and ROW267_STITCH.strip() not in prologue:
            prologue = prologue.replace(
                "**Row 266 closing stitch",
                ROW267_STITCH + "**Row 266 closing stitch",
                1,
            )

    chunk_start = prologue.find("prologue-preview-row-267")
    if chunk_start != -1:
        chunk = prologue[chunk_start : chunk_start + 3200]
        fixed = (
            chunk.replace("skill-navigation-row-247", "skill-navigation-row-267")
            .replace("#row-247-closing-stitch", "#row-267-closing-stitch")
            .replace(
                "row68-row227-part-boundary-meta-prelude-capstone-reunion-index-row-247",
                "row68-row247-part-boundary-meta-prelude-capstone-reunion-index-row-267",
            )
            .replace("#row-247-closing-loop", "#row-267-closing-loop")
            .replace(
                "row-247-baby-picture-row68-row227-part-boundary-meta-prelude-capstone-reunion",
                "row-267-baby-picture-row68-row247-part-boundary-meta-prelude-capstone-reunion",
            )
        )
        prologue = prologue[:chunk_start] + fixed + prologue[chunk_start + 3200 :]
    return prologue


def main() -> None:
    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = fix_prologue(prologue_path.read_text())
    prologue_path.write_text(prologue)
    print("prologue: fixed row 266/267 anchors")


if __name__ == "__main__":
    main()
