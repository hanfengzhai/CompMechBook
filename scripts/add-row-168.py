#!/usr/bin/env python3
"""Add row 168 meta-stitch (Row 68 → Row 148 ↔ Row 48 midpoint meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def t148_to_168(text: str) -> str:
    """Transform row-148 capstone-path meta copy to row 168 (148→168, 128→148 inner, 147→167 gate)."""
    repl = [
        ("Row 68 → Row 128 Row 68 → Row 48", "Row 68 → Row 148 Row 68 → Row 48"),
        (
            "row68-row128-midpoint-meta-prelude-capstone-reunion-index-row-148",
            "TEMP_ROW168_MIDPOINT_INDEX",
        ),
        (
            "row-148-baby-picture-row68-row128-midpoint-meta-prelude-capstone-reunion",
            "row-168-baby-picture-row68-row148-midpoint-meta-prelude-capstone-reunion",
        ),
        ("skill-navigation-row-148", "skill-navigation-row-168"),
        ("prologue-preview-row-148", "prologue-preview-row-168"),
        ("row-148-closing-stitch", "row-168-closing-stitch"),
        ("row-148-closing-loop", "row-168-closing-loop"),
        ("Row 148 three-way audit", "Row 168 three-way audit"),
        (
            "[row 147](preface.md#skill-navigation-row-147) or [row 128](preface.md#skill-navigation-row-128)",
            "[row 167](preface.md#skill-navigation-row-167) or [row 148](preface.md#skill-navigation-row-148)",
        ),
        (
            "[row 147](preface.md#skill-navigation-row-147) or [Row 68 → Row 108 midpoint meta prelude capstone reunion index (row 128)](appendix/sources.md#row68-row108-midpoint-meta-prelude-capstone-reunion-index-row-128)",
            "[row 167](preface.md#skill-navigation-row-167) or [Row 68 → Row 128 midpoint meta prelude capstone reunion index (row 148)](appendix/sources.md#row68-row128-midpoint-meta-prelude-capstone-reunion-index-row-148)",
        ),
        (
            "verified part-boundary meta prelude capstone on the full capstone path (row 147)",
            "verified part-boundary meta prelude capstone on the full capstone path (row 167)",
        ),
        (
            "verified part-boundary meta prelude capstone via [row 147](preface.md#skill-navigation-row-147)",
            "verified part-boundary meta prelude capstone via [row 167](preface.md#skill-navigation-row-167)",
        ),
        (
            "Row 68 ↔ Row 48 reunion (full capstone path)",
            "Row 68 ↔ Row 48 reunion (full capstone path)",
        ),
    ]
    out = text
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace("TEMP_ROW168_MIDPOINT_INDEX", "row68-row148-midpoint-meta-prelude-capstone-reunion-index-row-168")
    out = out.replace("row 148", "row 168")
    out = out.replace("Row 148", "Row 168")
    out = out.replace("[row 168](preface.md#skill-navigation-row-167)", "[row 167](preface.md#skill-navigation-row-167)")
    out = out.replace("[row 168](preface.md#skill-navigation-row-148)", "[row 148](preface.md#skill-navigation-row-148)")
    out = out.replace("row 1685", "row 169")
    out = out.replace("row 1686", "row 170")
    out = out.replace("row 168 or row 168", "row 167 or row 148")
    out = out.replace("When row 168 closed — midpoint", "When row 167 closed — midpoint")
    out = out.replace("When row 168 closed — part-boundary", "When row 167 closed — part-boundary")
    out = out.replace("row 168 closed midpoint", "row 167 closed midpoint")
    out = out.replace("row 168 closed part-boundary", "row 167 closed part-boundary")
    out = out.replace("after row 168 alone", "after row 167 alone")
    out = out.replace("Recite [preface row 168]", "Recite [preface row 167]")
    out = out.replace("row 168 or row 148 recited", "row 167 or row 148 recited")
    out = out.replace("from row 168's", "from row 167's")
    out = out.replace("row 147 closed", "row 167 closed")
    out = out.replace("Row 147 closed", "Row 167 closed")
    out = out.replace("row 146 or row 127 recited", "row 166 or row 147 recited")
    out = out.replace("row 128", "row 148")
    out = out.replace("Row 128", "Row 148")
    out = out.replace("row 147", "row 167")
    out = out.replace("Row 147", "Row 167")
    out = out.replace("row 146", "row 166")
    out = out.replace("Row 146", "Row 166")
    out = out.replace(
        "before row 149 taxonomy meta prelude capstone reunion opens on the full capstone path",
        "before row 149 taxonomy meta prelude capstone reunion opens on the full capstone path",
    )
    out = out.replace(
        "Proceed to [row 149]",
        "Proceed to [row 149]",
    )
    out = out.replace(
        "Do not conflate row 168 (row 68 ↔ row 48 reunion on the full capstone path) with row 148",
        "Do not conflate row 168 (row 68 ↔ row 48 reunion on the full capstone path) with row 148",
    )
    out = out.replace(
        "row 148 names **Row 68 → Row 108 Row 68 → Row 48 midpoint meta prelude capstone reunion**",
        "row 148 names **Row 68 → Row 128 Row 68 → Row 48 midpoint meta prelude capstone reunion**",
    )
    out = out.replace(
        "Row 68 → Row 168 Row 68 → Row 48",
        "Row 68 → Row 148 Row 68 → Row 48",
    )
    out = out.replace("#skill-navigation-row-1685", "#skill-navigation-row-169")
    out = out.replace(
        "row68-row108-midpoint-meta-prelude-capstone-reunion-index-row-128",
        "row68-row128-midpoint-meta-prelude-capstone-reunion-index-row-148",
    )
    out = out.replace(
        "row68-row127-part-boundary-meta-prelude-capstone-reunion-index-row-147",
        "row68-row147-part-boundary-meta-prelude-capstone-reunion-index-row-167",
    )
    out = out.replace("[row 166](preface.md#skill-navigation-row-146)", "[row 166](preface.md#skill-navigation-row-166)")
    out = out.replace("[row 167](preface.md#skill-navigation-row-147)", "[row 167](preface.md#skill-navigation-row-167)")
    out = out.replace("[row 148](preface.md#skill-navigation-row-128)", "[row 148](preface.md#skill-navigation-row-148)")
    out = out.replace(
        "[preface row 167](../preface.md#skill-navigation-row-147)",
        "[preface row 167](../preface.md#skill-navigation-row-167)",
    )
    out = out.replace(
        "[preface row 148](../preface.md#skill-navigation-row-128)",
        "[preface row 148](../preface.md#skill-navigation-row-148)",
    )
    return out


def extract_preface_row148(preface: str) -> str:
    start = preface.index("### Row 148 skill checkpoint")
    end = preface.index("\n\n### Row 149 skill checkpoint")
    return preface[start:end]


ROW168_PREFACE = t148_to_168(
    extract_preface_row148((ROOT / "writings/preface/chapters/preface.md").read_text())
) + "\n\n"

PROLOGUE_COMPASS = (
    "| Row 68 → Row 148 Row 68 → Row 48 midpoint meta prelude capstone reunion (row 168) | "
    "[Preface: row 168 skill checkpoint](../preface.md#skill-navigation-row-168) · "
    "[Row 68 → Row 148 midpoint meta prelude capstone reunion index](../appendix/sources.md#row68-row148-midpoint-meta-prelude-capstone-reunion-index-row-168) · "
    "[memory sheet row 168 baby picture](../appendix/memory-sheet.md#row-168-baby-picture-row68-row148-midpoint-meta-prelude-capstone-reunion) · "
    "[prologue row 168 preview row](#prologue-preview-row-168); [prologue row 168 closing stitch](#row-168-closing-stitch); "
    "[epilogue row 168 closing loop](../epilogue/multiscale.md#row-168-closing-loop) — "
    "read row 68 gate + row 167 or row 148 part-boundary meta prelude capstone / midpoint meta prelude gate + VI.4 intermission → Bridge → VII.0 landing + row 48 meta aloud "
    "when part-boundary meta prelude capstone is clean on the full capstone path but writings/continuum → writings/defects feels like two courses at the knee after verified twin-ladder reunion on the full capstone path |\n"
)

_prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
PROLOGUE_STITCH = t148_to_168(
    "**Row 148 closing stitch (Row 68 → Row 128 Row 68 → Row 48 midpoint meta prelude capstone reunion).** {#row-148-closing-stitch} "
    + _prologue.split("**Row 148 closing stitch")[1].split("**Row 149 closing stitch")[0].lstrip()
    .split("\n\n")[0]
    + "\n\n"
)

PROLOGUE_PREVIEW = (
    "| <span id=\"prologue-preview-row-168\"></span>Row 168 preview (Row 68 → Row 148 Row 68 → Row 48 midpoint meta prelude capstone reunion) | "
    "Explain why midpoint closure (row 68) and VI.4 → VII.0 meta (row 48) must be read together with the intermission → Bridge chain after verified part-boundary meta prelude capstone on the full capstone path before continuum and defects subtrees feel like separate courses at the knee | "
    "One sentence: \"read row 68 gate + row 167 or row 148 part-boundary meta prelude capstone / midpoint meta prelude gate + VI.4 intermission → Bridge → VII.0 landing + row 48 meta aloud when part-boundary meta prelude capstone is clean on the full capstone path but writings/continuum → writings/defects feels like two courses at the knee after verified twin-ladder reunion on the full capstone path\" — "
    "[preface row 168 skill checkpoint](../preface.md#skill-navigation-row-168); [prologue row 168 closing stitch](#row-168-closing-stitch); "
    "[Row 68 → Row 148 reunion index](../appendix/sources.md#row68-row148-midpoint-meta-prelude-capstone-reunion-index-row-168); "
    "[memory sheet row 168 baby picture](../appendix/memory-sheet.md#row-168-baby-picture-row68-row148-midpoint-meta-prelude-capstone-reunion); "
    "[VI.4 Writings canonical hinge](../part06-continuum/04-nonlinear-plasticity-preview.md#writings-canonical-hinge-vi4-to-vii0); "
    "[VII.0 descent hinge from VI.4](../part07-defects/00-opening.md#descent-hinge-from-vi4-energy-break-forest-begins); "
    "[preface row 48 skill checkpoint](../preface.md#skill-navigation-row-48); "
    "[preface row 167 skill checkpoint](../preface.md#skill-navigation-row-167); "
    "[epilogue row 168 closing loop](../epilogue/multiscale.md#row-168-closing-loop) |\n"
)

_epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
EPILOGUE_LOOP = t148_to_168(
    "### Row 148 closing loop"
    + _epilogue.split("### Row 148 closing loop")[1].split("### Row 149 closing loop")[0]
)

SOURCES_TABLE = (
    "| 168 | Row 68 → Row 148 Row 68 → Row 48 midpoint meta prelude capstone (midpoint prelude gate ↔ part-boundary meta prelude capstone on full capstone path ↔ row 48 meta) | "
    "[Row 68 → Row 148 midpoint meta prelude capstone reunion index](#row68-row148-midpoint-meta-prelude-capstone-reunion-index-row-168) · "
    "[preface row 168](../preface.md#skill-navigation-row-168) · "
    "[prologue row 168 preview](../prologue/00-many-scales.md#prologue-preview-row-168) · "
    "[prologue row 168 closing stitch](../prologue/00-many-scales.md#row-168-closing-stitch) · "
    "[epilogue row 168 closing loop](../epilogue/multiscale.md#row-168-closing-loop) · "
    "[memory sheet row 168 baby picture](memory-sheet.md#row-168-baby-picture-row68-row148-midpoint-meta-prelude-capstone-reunion) | "
    "Row 68 closed but **row 48 midpoint meta reunion still feels disconnected from verified part-boundary meta prelude capstone on the full capstone path** — "
    "read row 68 + row 167 or row 148 gate + VI.4 intermission → VII.0 landing + row 48; "
    "[preface row 48](../preface.md#skill-navigation-row-48) |\n"
)

SOURCES_INDEX = t148_to_168(
    (ROOT / "writings/appendix/chapters/sources.md")
    .read_text()
    .split("## Row 68 → Row 128 Row 68 → Row 48 midpoint meta prelude capstone reunion index (row 148)")[1]
    .split("## Row 68 → Row 129 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 149)")[0]
)
SOURCES_INDEX = (
    "## Row 68 → Row 148 Row 68 → Row 48 midpoint meta prelude capstone reunion index (row 168)"
    + SOURCES_INDEX
)

MEMORY_TABLE = (
    "| 168 | Meta | [Row 68 → Row 148 midpoint meta prelude capstone reunion index](sources.md#row68-row148-midpoint-meta-prelude-capstone-reunion-index-row-168) · "
    "[preface row 168 skill checkpoint](../preface.md#skill-navigation-row-168) · "
    "[prologue row 168 preview](../prologue/00-many-scales.md#prologue-preview-row-168) · "
    "[prologue row 168 closing stitch](../prologue/00-many-scales.md#row-168-closing-stitch) · "
    "[epilogue row 168 closing loop](../epilogue/multiscale.md#row-168-closing-loop) | "
    "Row 68 closed but row 48 midpoint meta reunion feels disconnected from verified part-boundary meta prelude capstone on the full capstone path — "
    "read row 68 + row 167 or row 148 gate + VI.4 intermission → VII.0 landing + row 48; "
    "[row 168 baby picture](#row-168-baby-picture-row68-row148-midpoint-meta-prelude-capstone-reunion) |\n"
)

MEMORY_BABY = t148_to_168(
    (ROOT / "writings/appendix/chapters/memory-sheet.md")
    .read_text()
    .split("### Row 148 baby picture")[1]
    .split("### Row 149 baby picture")[0]
)
MEMORY_BABY = (
    "### Row 168 baby picture"
    + MEMORY_BABY.split(")", 1)[1]
    if ")" in MEMORY_BABY
    else "### Row 168 baby picture" + MEMORY_BABY
)

ROW167_TAIL_MARKER = "**When to pause.** Read the [prologue row 167 closing stitch]"
ROW167_TAIL_END = "or extend prose only under `writings/` then sync.\n\n\n\n\n## The copper wire through the book"

ROW167_STITCH_OLD = (
    "before row 148 midpoint meta prelude capstone reunion opens on the full capstone path."
)
ROW167_STITCH_NEW = (
    "before row 168 midpoint meta prelude capstone reunion opens on the full capstone path."
)

ROW167_EPILOGUE_PROCEED_OLD = (
    "Proceed to [row 148](#row-148-closing-loop) when row 68 closed but midpoint meta prelude capstone still lags after row 167 on the full capstone path,"
)
ROW167_EPILOGUE_PROCEED_NEW = (
    "Proceed to [row 168](#row-168-closing-loop) when row 68 closed but midpoint meta prelude capstone still lags after row 167 on the full capstone path,"
)

ROW167_BABY_OLD = (
    "row 167 when **V.4 → VI.0 twin-ladder reunion and Row 66 → Row 47 meta must read on the same wire before row 148 midpoint meta prelude capstone opens on the full capstone path**"
)
ROW167_BABY_NEW = (
    "row 167 when **V.4 → VI.0 twin-ladder reunion and Row 66 → Row 47 meta must read on the same wire before row 168 midpoint meta prelude capstone opens on the full capstone path**"
)


def update_row167_tail(preface: str) -> str:
    start = preface.index(ROW167_TAIL_MARKER)
    end = preface.index(ROW167_TAIL_END)
    block = preface[start:end]
    new_block = block.replace(
        "when opening [row 148](preface.md#skill-navigation-row-148) before row 48 closes on the full capstone path",
        "when opening [row 168](preface.md#skill-navigation-row-168) before row 48 closes on the full capstone path",
    )
    new_block = new_block.replace(
        "When row 167 is complete, proceed to [row 148](preface.md#skill-navigation-row-148) when row 68 closed but midpoint meta prelude capstone still lags after verified part-boundary meta prelude capstone on the full capstone path, to [row 128](preface.md#skill-navigation-row-128) when row 68 closed but midpoint meta prelude capstone still lags after verified part-boundary meta prelude capstone on the opening-hinge capstone path alone, to [row 108](preface.md#skill-navigation-row-108) when twin-ladder reunion is clean but midpoint meta capstone still lags on the opening-hinge path, to [row 147](preface.md#skill-navigation-row-147) for the Row 68 ↔ Row 67 meta audit on the opening-hinge capstone path alone, to [row 166](preface.md#skill-navigation-row-166) when Writings canonical meta prelude capstone still lags after verified second-pass meta prelude capstone on the full capstone path, to [row 87](preface.md#skill-navigation-row-87) for the Row 68 ↔ Row 67 opening prelude audit alone, to [row 67](preface.md#skill-navigation-row-67) for the Row 66 ↔ Row 47 meta audit alone, to [row 47](preface.md#skill-navigation-row-47) for the V.4 → VI.0 meta audit alone, or extend prose only under `writings/` then sync.",
        "When row 167 is complete, proceed to [row 168](preface.md#skill-navigation-row-168) when row 68 closed but midpoint meta prelude capstone still lags after verified part-boundary meta prelude capstone on the full capstone path, to [row 148](preface.md#skill-navigation-row-148) when row 68 closed but midpoint meta prelude capstone still lags after verified part-boundary meta prelude capstone on the opening-hinge capstone path alone, to [row 108](preface.md#skill-navigation-row-108) when twin-ladder reunion is clean but midpoint meta capstone still lags on the opening-hinge path, to [row 167](preface.md#skill-navigation-row-167) for the Row 68 ↔ Row 67 meta audit on the opening-hinge capstone path alone, to [row 166](preface.md#skill-navigation-row-166) when Writings canonical meta prelude capstone still lags after verified second-pass meta prelude capstone on the full capstone path, to [row 87](preface.md#skill-navigation-row-87) for the Row 68 ↔ Row 67 opening prelude audit alone, to [row 67](preface.md#skill-navigation-row-67) for the Row 66 ↔ Row 47 meta audit alone, to [row 47](preface.md#skill-navigation-row-47) for the V.4 → VI.0 meta audit alone, or extend prose only under `writings/` then sync.",
    )
    return preface[:start] + new_block + preface[end:]


def main():
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "skill-navigation-row-168" in preface and preface.index("skill-navigation-row-168") < preface.index(copper):
        print("preface: row 168 already present")
    else:
        preface = update_row167_tail(preface)
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + ROW168_PREFACE + copper)
        preface_path.write_text(preface)
        print("preface: added row 168")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-168" not in prologue:
        needle = "| Row 68 → Row 147 Row 68 → Row 67 part-boundary meta prelude capstone reunion (row 167) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 167 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + PROLOGUE_COMPASS + prologue[line_end + 1 :]
        prologue = prologue.replace(
            "**Row 167 closing stitch",
            PROLOGUE_STITCH + "**Row 167 closing stitch",
        )
        prologue = prologue.replace(
            '| <span id="prologue-preview-row-167"></span>Row 167 preview',
            PROLOGUE_PREVIEW + '| <span id="prologue-preview-row-167"></span>Row 167 preview',
        )
        if ROW167_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW167_STITCH_OLD, ROW167_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 168")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "row-168-closing-loop" not in epilogue:
        if ROW167_EPILOGUE_PROCEED_OLD in epilogue:
            epilogue = epilogue.replace(ROW167_EPILOGUE_PROCEED_OLD, ROW167_EPILOGUE_PROCEED_NEW)
        marker = (
            "to [row 67](#row-67-closing-loop) when only part-boundary prelude meta stalls, or extend prose only under `writings/` then sync.\n\n\n\n\n\n\n\n### Row 135 closing loop"
        )
        replacement = (
            "to [row 67](#row-67-closing-loop) when only part-boundary prelude meta stalls, or extend prose only under `writings/` then sync.\n\n\n"
            + EPILOGUE_LOOP
            + "\n\n\n\n\n### Row 135 closing loop"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 167 end marker not found")
        epilogue = epilogue.replace(marker, replacement, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 168")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row148-midpoint-meta-prelude-capstone-reunion-index-row-168" not in sources:
        sources = sources.replace(
            "| 148 | Row 68 → Row 128 Row 68 → Row 48 midpoint meta prelude capstone",
            SOURCES_TABLE + "| 148 | Row 68 → Row 128 Row 68 → Row 48 midpoint meta prelude capstone",
        )
        sources = sources.replace(
            "## Row 68 → Row 128 Row 68 → Row 48 midpoint meta prelude capstone reunion index (row 148)",
            SOURCES_INDEX + "## Row 68 → Row 128 Row 68 → Row 48 midpoint meta prelude capstone reunion index (row 148)",
        )
        sources_path.write_text(sources)
        print("sources: added row 168")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-168-baby-picture-row68-row148" not in memory:
        memory = memory.replace(
            "| 167 | Meta | [Row 68 → Row 147 part-boundary meta prelude capstone reunion index]",
            MEMORY_TABLE + "| 167 | Meta | [Row 68 → Row 147 part-boundary meta prelude capstone reunion index]",
        )
        memory = memory.replace(
            "### Row 167 baby picture {#row-167-baby-picture-row68-row147-part-boundary-meta-prelude-capstone-reunion}",
            MEMORY_BABY + "### Row 167 baby picture {#row-167-baby-picture-row68-row147-part-boundary-meta-prelude-capstone-reunion}",
        )
        memory = memory.replace(ROW167_BABY_OLD, ROW167_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 168")


if __name__ == "__main__":
    main()
