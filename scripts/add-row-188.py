#!/usr/bin/env python3
"""Add row 188 meta-stitch (Row 68 → Row 168 ↔ Row 48 midpoint meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def bump168_to_188(text: str) -> str:
    """Lift row-168 capstone copy to row 188 on the full capstone path."""
    out = text
    out = out.replace("### Row 168 skill checkpoint", "### Row 188 skill checkpoint")
    out = out.replace("{#skill-navigation-row-168}", "{#skill-navigation-row-188}")
    out = out.replace("Row 68 → Row 148 Row 68 → Row 48", "Row 68 → Row 168 Row 68 → Row 48")
    out = out.replace(
        "row68-row148-midpoint-meta-prelude-capstone-reunion-index-row-168",
        "row68-row168-midpoint-meta-prelude-capstone-reunion-index-row-188",
    )
    out = out.replace(
        "row-168-baby-picture-row68-row148-midpoint-meta-prelude-capstone-reunion",
        "row-188-baby-picture-row68-row168-midpoint-meta-prelude-capstone-reunion",
    )
    out = out.replace("skill-navigation-row-168", "skill-navigation-row-188")
    out = out.replace("prologue-preview-row-168", "prologue-preview-row-188")
    out = out.replace("row-168-closing-stitch", "row-188-closing-stitch")
    out = out.replace("row-168-closing-loop", "row-188-closing-loop")
    out = out.replace("Row 168 three-way audit", "Row 188 three-way audit")
    out = out.replace(
        "[row 167](preface.md#skill-navigation-row-167) or [row 148](preface.md#skill-navigation-row-148)",
        "[row 187](preface.md#skill-navigation-row-187) or [row 168](preface.md#skill-navigation-row-168)",
    )
    out = out.replace(
        "row68-row128-midpoint-meta-prelude-capstone-reunion-index-row-148",
        "row68-row148-midpoint-meta-prelude-capstone-reunion-index-row-168",
    )
    out = out.replace(
        "verified part-boundary meta prelude capstone on the full capstone path (row 167)",
        "verified part-boundary meta prelude capstone on the full capstone path (row 187)",
    )
    out = out.replace(
        "verified part-boundary meta prelude capstone via [row 167]",
        "verified part-boundary meta prelude capstone via [row 187]",
    )
    out = out.replace("row 167's twin-ladder", "row 187's twin-ladder")
    out = out.replace("Row 168 does not replace", "Row 188 does not replace")
    out = out.replace("(row 167) with the full-book", "(row 187) with the full-book")
    out = out.replace("prologue row 168", "prologue row 188")
    out = out.replace("memory sheet row 168", "memory sheet row 188")
    out = out.replace("epilogue row 168", "epilogue row 188")
    out = out.replace("When row 168 is complete", "When row 188 is complete")
    out = out.replace("When row 167 closed", "When row 187 closed")
    out = out.replace("after row 167", "after row 187")
    out = out.replace(
        "[row 169](preface.md#skill-navigation-row-169) before row 49",
        "[row 189](preface.md#skill-navigation-row-189) before row 49",
    )
    out = out.replace(
        "proceed to [row 169](preface.md#skill-navigation-row-169) when midpoint",
        "proceed to [row 189](preface.md#skill-navigation-row-189) when midpoint",
    )
    out = out.replace(
        "[row 148](preface.md#skill-navigation-row-148) for the Row 68 ↔ Row 48 meta audit on the opening-hinge capstone path alone, to [row 167](preface.md#skill-navigation-row-167) when part-boundary",
        "[row 168](preface.md#skill-navigation-row-168) for the Row 68 ↔ Row 48 meta audit on the opening-hinge capstone path alone, to [row 187](preface.md#skill-navigation-row-187) when part-boundary",
    )
    out = out.replace("Row 68 → Row 148 reunion index", "Row 68 → Row 168 reunion index")
    out = out.replace(
        "Row 68 → Row 148 midpoint meta prelude capstone reunion index",
        "Row 68 → Row 168 midpoint meta prelude capstone reunion index",
    )
    out = out.replace(
        "Row 68 → Row 128 midpoint meta prelude capstone reunion index (row 148)",
        "Row 68 → Row 148 midpoint meta prelude capstone reunion index (row 168)",
    )
    out = out.replace("row 148, row 108", "row 168, row 108")
    out = out.replace("row 167, row 148", "row 187, row 168")
    return out


def t168_to_188(text: str) -> str:
    return bump168_to_188(text)


def extract_preface_row168(preface: str) -> str:
    start = preface.index(
        "### Row 168 skill checkpoint — Row 68 → Row 148 Row 68 → Row 48"
    )
    end = preface.index("\n\n### Row 169 skill checkpoint", start)
    return preface[start:end]


ROW188_PREFACE = t168_to_188(
    extract_preface_row168((ROOT / "writings/preface/chapters/preface.md").read_text())
) + "\n\n"

PROLOGUE_COMPASS = (
    "| Row 68 → Row 168 Row 68 → Row 48 midpoint meta prelude capstone reunion (row 188) | "
    "[Preface: row 188 skill checkpoint](../preface.md#skill-navigation-row-188) · "
    "[Row 68 → Row 168 midpoint meta prelude capstone reunion index](../appendix/sources.md#row68-row168-midpoint-meta-prelude-capstone-reunion-index-row-188) · "
    "[memory sheet row 188 baby picture](../appendix/memory-sheet.md#row-188-baby-picture-row68-row168-midpoint-meta-prelude-capstone-reunion) · "
    "[prologue row 188 preview row](#prologue-preview-row-188); [prologue row 188 closing stitch](#row-188-closing-stitch); "
    "[epilogue row 188 closing loop](../epilogue/multiscale.md#row-188-closing-loop) — "
    "read row 68 gate + row 187 or row 168 part-boundary meta prelude capstone / midpoint meta prelude gate + VI.4 intermission → Bridge → VII.0 landing + row 48 meta aloud "
    "when part-boundary meta prelude capstone is clean on the full capstone path but writings/continuum → writings/defects feels like two courses at the knee after verified twin-ladder reunion on the full capstone path |\n"
)

_prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
PROLOGUE_STITCH = t168_to_188(
    "**Row 168 closing stitch (Row 68 → Row 148 Row 68 → Row 48 midpoint meta prelude capstone reunion).** {#row-168-closing-stitch} "
    + _prologue.split("**Row 168 closing stitch")[1].split("**Row 169 closing stitch")[0].lstrip()
    .split("\n\n")[0]
    + "\n\n"
)

PROLOGUE_PREVIEW = (
    "| <span id=\"prologue-preview-row-188\"></span>Row 188 preview (Row 68 → Row 168 Row 68 → Row 48 midpoint meta prelude capstone reunion) | "
    "Explain why midpoint closure (row 68) and VI.4 → VII.0 meta (row 48) must be read together with the intermission → Bridge chain after verified part-boundary meta prelude capstone on the full capstone path before continuum and defects subtrees feel like separate courses at the knee | "
    "One sentence: \"read row 68 gate + row 187 or row 168 part-boundary meta prelude capstone / midpoint meta prelude gate + VI.4 intermission → Bridge → VII.0 landing + row 48 meta aloud when part-boundary meta prelude capstone is clean on the full capstone path but writings/continuum → writings/defects feels like two courses at the knee after verified twin-ladder reunion on the full capstone path\" — "
    "[preface row 188 skill checkpoint](../preface.md#skill-navigation-row-188); [prologue row 188 closing stitch](#row-188-closing-stitch); "
    "[Row 68 → Row 168 reunion index](../appendix/sources.md#row68-row168-midpoint-meta-prelude-capstone-reunion-index-row-188); "
    "[memory sheet row 188 baby picture](../appendix/memory-sheet.md#row-188-baby-picture-row68-row168-midpoint-meta-prelude-capstone-reunion); "
    "[VI.4 Writings canonical hinge](../part06-continuum/04-nonlinear-plasticity-preview.md#writings-canonical-hinge-vi4-to-vii0); "
    "[VII.0 descent hinge from VI.4](../part07-defects/00-opening.md#descent-hinge-from-vi4-energy-break-forest-begins); "
    "[preface row 48 skill checkpoint](../preface.md#skill-navigation-row-48); "
    "[preface row 187 skill checkpoint](../preface.md#skill-navigation-row-187); "
    "[epilogue row 188 closing loop](../epilogue/multiscale.md#row-188-closing-loop) |\n"
)

_epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
EPILOGUE_LOOP = t168_to_188(
    "### Row 168 closing loop"
    + _epilogue.split("### Row 168 closing loop")[1].split("### Row 169 closing loop")[0]
)

SOURCES_TABLE = (
    "| 188 | Row 68 → Row 168 Row 68 → Row 48 midpoint meta prelude capstone (midpoint prelude gate ↔ part-boundary meta prelude capstone on full capstone path ↔ row 48 meta) | "
    "[Row 68 → Row 168 midpoint meta prelude capstone reunion index](#row68-row168-midpoint-meta-prelude-capstone-reunion-index-row-188) · "
    "[preface row 188](../preface.md#skill-navigation-row-188) · "
    "[prologue row 188 preview](../prologue/00-many-scales.md#prologue-preview-row-188) · "
    "[prologue row 188 closing stitch](../prologue/00-many-scales.md#row-188-closing-stitch) · "
    "[epilogue row 188 closing loop](../epilogue/multiscale.md#row-188-closing-loop) · "
    "[memory sheet row 188 baby picture](memory-sheet.md#row-188-baby-picture-row68-row168-midpoint-meta-prelude-capstone-reunion) | "
    "Row 68 closed but **row 48 midpoint meta reunion still feels disconnected from verified part-boundary meta prelude capstone on the full capstone path** — "
    "read row 68 + row 187 or row 168 gate + VI.4 intermission → VII.0 landing + row 48; "
    "[preface row 48](../preface.md#skill-navigation-row-48) |\n"
)

SOURCES_INDEX = t168_to_188(
    (ROOT / "writings/appendix/chapters/sources.md")
    .read_text()
    .split("## Row 68 → Row 148 Row 68 → Row 48 midpoint meta prelude capstone reunion index (row 168)")[1]
    .split("## Row 68 → Row 149 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 169)")[0]
)
SOURCES_INDEX = (
    "## Row 68 → Row 168 Row 68 → Row 48 midpoint meta prelude capstone reunion index (row 188)"
    + SOURCES_INDEX
)

MEMORY_TABLE = (
    "| 188 | Meta | [Row 68 → Row 168 midpoint meta prelude capstone reunion index](sources.md#row68-row168-midpoint-meta-prelude-capstone-reunion-index-row-188) · "
    "[preface row 188 skill checkpoint](../preface.md#skill-navigation-row-188) · "
    "[prologue row 188 preview](../prologue/00-many-scales.md#prologue-preview-row-188) · "
    "[prologue row 188 closing stitch](../prologue/00-many-scales.md#row-188-closing-stitch) · "
    "[epilogue row 188 closing loop](../epilogue/multiscale.md#row-188-closing-loop) | "
    "Row 68 closed but row 48 midpoint meta reunion feels disconnected from verified part-boundary meta prelude capstone on the full capstone path — "
    "read row 68 + row 187 or row 168 gate + VI.4 intermission → VII.0 landing + row 48; "
    "[row 188 baby picture](#row-188-baby-picture-row68-row168-midpoint-meta-prelude-capstone-reunion) |\n"
)

MEMORY_BABY = t168_to_188(
    (ROOT / "writings/appendix/chapters/memory-sheet.md")
    .read_text()
    .split("### Row 168 baby picture")[1]
    .split("### Row 169 baby picture")[0]
)
MEMORY_BABY = (
    "### Row 188 baby picture"
    + MEMORY_BABY.split(")", 1)[1]
    if ")" in MEMORY_BABY
    else "### Row 188 baby picture" + MEMORY_BABY
)

ROW187_TAIL_MARKER = "**When to pause.** Read the [prologue row 187 closing stitch]"
ROW187_TAIL_END = "or extend prose only under `writings/` then sync.\n\n\n\n\n\n## The copper wire through the book"

ROW187_STITCH_OLD = (
    "before row 168 midpoint meta prelude capstone reunion opens on the full capstone path."
)
ROW187_STITCH_NEW = (
    "before row 188 midpoint meta prelude capstone reunion opens on the full capstone path."
)

ROW187_EPILOGUE_PROCEED_OLD = (
    "Proceed to [row 168](#row-168-closing-loop) when row 68 closed but midpoint meta prelude capstone still lags after row 187 on the full capstone path,"
)
ROW187_EPILOGUE_PROCEED_NEW = (
    "Proceed to [row 188](#row-188-closing-loop) when row 68 closed but midpoint meta prelude capstone still lags after row 187 on the full capstone path,"
)

ROW187_BABY_OLD = (
    "row 187 when **V.4 → VI.0 twin-ladder reunion and Row 66 → Row 47 meta must read on the same wire before row 168 midpoint meta prelude capstone opens on the full capstone path**"
)
ROW187_BABY_NEW = (
    "row 187 when **V.4 → VI.0 twin-ladder reunion and Row 66 → Row 47 meta must read on the same wire before row 188 midpoint meta prelude capstone opens on the full capstone path**"
)

ROW187_TAIL_OLD = (
    "When row 187 is complete, proceed to [row 168](preface.md#skill-navigation-row-168) when row 68 closed but midpoint meta prelude capstone still lags after verified part-boundary meta prelude capstone on the full capstone path, to [row 148](preface.md#skill-navigation-row-148) when row 68 closed but midpoint meta prelude capstone still lags after verified part-boundary meta prelude capstone on the opening-hinge capstone path alone, to [row 108](preface.md#skill-navigation-row-108) when twin-ladder reunion is clean but midpoint meta capstone still lags on the opening-hinge path, to [row 187](preface.md#skill-navigation-row-187) for the Row 68 ↔ Row 67 meta audit on the opening-hinge capstone path alone, to [row 186](preface.md#skill-navigation-row-166) when Writings canonical meta prelude capstone still lags after verified second-pass meta prelude capstone on the full capstone path, to [row 87](preface.md#skill-navigation-row-87) for the Row 68 ↔ Row 67 opening prelude audit alone, to [row 67](preface.md#skill-navigation-row-67) for the Row 66 ↔ Row 47 meta audit alone, to [row 47](preface.md#skill-navigation-row-47) for the V.4 → VI.0 meta audit alone, or extend prose only under `writings/` then sync."
)
ROW187_TAIL_NEW = (
    "When row 187 is complete, proceed to [row 188](preface.md#skill-navigation-row-188) when row 68 closed but midpoint meta prelude capstone still lags after verified part-boundary meta prelude capstone on the full capstone path, to [row 168](preface.md#skill-navigation-row-168) when row 68 closed but midpoint meta prelude capstone still lags after verified part-boundary meta prelude capstone on the opening-hinge capstone path alone, to [row 108](preface.md#skill-navigation-row-108) when twin-ladder reunion is clean but midpoint meta capstone still lags on the opening-hinge path, to [row 187](preface.md#skill-navigation-row-187) for the Row 68 ↔ Row 67 meta audit on the opening-hinge capstone path alone, to [row 186](preface.md#skill-navigation-row-186) when Writings canonical meta prelude capstone still lags after verified second-pass meta prelude capstone on the full capstone path, to [row 87](preface.md#skill-navigation-row-87) for the Row 68 ↔ Row 67 opening prelude audit alone, to [row 67](preface.md#skill-navigation-row-67) for the Row 66 ↔ Row 47 meta audit alone, to [row 47](preface.md#skill-navigation-row-47) for the V.4 → VI.0 meta audit alone, or extend prose only under `writings/` then sync."
)


def update_row187_tail(preface: str) -> str:
    start = preface.index(ROW187_TAIL_MARKER)
    end = preface.index(ROW187_TAIL_END)
    block = preface[start:end]
    new_block = block.replace(
        "when opening [row 168](preface.md#skill-navigation-row-168) before row 48 closes on the full capstone path",
        "when opening [row 188](preface.md#skill-navigation-row-188) before row 48 closes on the full capstone path",
    )
    new_block = new_block.replace(ROW187_TAIL_OLD, ROW187_TAIL_NEW)
    return preface[:start] + new_block + preface[end:]


def main() -> None:
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "### Row 188 skill checkpoint" in preface and preface.index("### Row 188 skill checkpoint") < preface.index(copper):
        print("preface: row 188 already present")
    else:
        preface = update_row187_tail(preface)
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + ROW188_PREFACE + copper)
        preface_path.write_text(preface)
        print("preface: added row 188")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-188" not in prologue:
        needle = "| Row 68 → Row 167 Row 68 → Row 67 part-boundary meta prelude capstone reunion (row 187) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 187 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + PROLOGUE_COMPASS + prologue[line_end + 1 :]
        prologue = prologue.replace(
            "**Row 187 closing stitch",
            PROLOGUE_STITCH + "**Row 187 closing stitch",
        )
        prologue = prologue.replace(
            '| <span id="prologue-preview-row-187"></span>Row 187 preview',
            PROLOGUE_PREVIEW + '| <span id="prologue-preview-row-187"></span>Row 187 preview',
        )
        if ROW187_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW187_STITCH_OLD, ROW187_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 188")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "row-188-closing-loop" not in epilogue:
        if ROW187_EPILOGUE_PROCEED_OLD in epilogue:
            epilogue = epilogue.replace(ROW187_EPILOGUE_PROCEED_OLD, ROW187_EPILOGUE_PROCEED_NEW)
        marker = "### Row 186 closing loop (Row 68 → Row 166 Row 68 → Row 66 Writings canonical meta prelude capstone reunion)"
        if marker not in epilogue:
            raise SystemExit("epilogue row 186 insert anchor not found")
        epilogue = epilogue.replace(marker, EPILOGUE_LOOP + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 188")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row168-midpoint-meta-prelude-capstone-reunion-index-row-188" not in sources:
        sources = sources.replace(
            "| 168 | Row 68 → Row 148 Row 68 → Row 48 midpoint meta prelude capstone",
            SOURCES_TABLE + "| 168 | Row 68 → Row 148 Row 68 → Row 48 midpoint meta prelude capstone",
            1,
        )
        sources = sources.replace(
            "## Row 68 → Row 148 Row 68 → Row 48 midpoint meta prelude capstone reunion index (row 168)",
            SOURCES_INDEX + "## Row 68 → Row 148 Row 68 → Row 48 midpoint meta prelude capstone reunion index (row 168)",
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 188")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-188-baby-picture-row68-row168" not in memory:
        memory = memory.replace(
            "| 187 | Meta | [Row 68 → Row 167 part-boundary meta prelude capstone reunion index]",
            MEMORY_TABLE + "| 187 | Meta | [Row 68 → Row 167 part-boundary meta prelude capstone reunion index]",
            1,
        )
        memory = memory.replace(
            "### Row 187 baby picture {#row-187-baby-picture-row68-row167-part-boundary-meta-prelude-capstone-reunion}",
            MEMORY_BABY + "### Row 187 baby picture {#row-187-baby-picture-row68-row167-part-boundary-meta-prelude-capstone-reunion}",
            1,
        )
        memory = memory.replace(ROW187_BABY_OLD, ROW187_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 188")


if __name__ == "__main__":
    main()
