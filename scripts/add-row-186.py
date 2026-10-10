#!/usr/bin/env python3
"""Add row 186 meta-stitch (Row 68 → Row 166 ↔ Row 66 Writings canonical meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def t166_to_186(text: str) -> str:
    """Transform row-166 capstone-path meta copy to row 186 (166→186, 146→166 inner, 185 gate)."""
    repl = [
        ("Row 68 → Row 146 Row 68 → Row 66", "Row 68 → Row 166 Row 68 → Row 66"),
        (
            "row68-row146-writings-meta-prelude-capstone-reunion-index-row-166",
            "TEMP186IDX",
        ),
        (
            "row-166-baby-picture-row68-row146-writings-meta-prelude-capstone-reunion",
            "row-186-baby-picture-row68-row166-writings-meta-prelude-capstone-reunion",
        ),
        ("skill-navigation-row-166", "TEMP166NAV"),
        ("prologue-preview-row-166", "prologue-preview-row-186"),
        ("row-166-closing-stitch", "row-186-closing-stitch"),
        ("row-166-closing-loop", "row-186-closing-loop"),
        ("Row 166 three-way audit", "Row 186 three-way audit"),
        (
            "[row 165](preface.md#skill-navigation-row-165) or [row 146](preface.md#skill-navigation-row-146)",
            "[row 185](preface.md#skill-navigation-row-185) or [row 166](TEMP166NAV)",
        ),
        (
            "[Row 68 → Row 126 Writings canonical meta prelude capstone reunion index (row 146)](appendix/sources.md#row68-row126-writings-meta-prelude-capstone-reunion-index-row-146)",
            "[Row 68 → Row 166 Writings canonical meta prelude capstone reunion index (row 186)](appendix/sources.md#row68-row166-writings-meta-prelude-capstone-reunion-index-row-186)",
        ),
        (
            "[row 164](preface.md#skill-navigation-row-164) or [Row 68 → Row 145 second-pass meta prelude capstone reunion index (row 165)](appendix/sources.md#row68-row145-second-pass-meta-prelude-capstone-reunion-index-row-165)",
            "[row 184](preface.md#skill-navigation-row-184) or [Row 68 → Row 165 second-pass meta prelude capstone reunion index (row 185)](appendix/sources.md#row68-row145-second-pass-meta-prelude-capstone-reunion-index-row-165)",
        ),
        ("on the capstone path", "on the full capstone path"),
        ("(capstone path)", "(full capstone path)"),
        ("Row 68 ↔ Row 66 reunion (capstone path)", "Row 68 ↔ Row 66 reunion (full capstone path)"),
    ]
    out = text
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace("TEMP186IDX", "row68-row166-writings-meta-prelude-capstone-reunion-index-row-186")
    out = out.replace("TEMP166NAV", "skill-navigation-row-166")
    out = out.replace("Row 68 → Row 166 Row 68 → Row 66", "TEMP166TITLE")
    out = out.replace("row 166", "row 186")
    out = out.replace("Row 166", "Row 186")
    out = out.replace("TEMP166TITLE", "Row 68 → Row 166 Row 68 → Row 66")
    out = out.replace("skill-navigation-row-166", "skill-navigation-row-186")
    out = out.replace("[row 186](preface.md#skill-navigation-row-185)", "[row 185](preface.md#skill-navigation-row-185)")
    out = out.replace("[row 186](preface.md#skill-navigation-row-166)", "[row 166](preface.md#skill-navigation-row-166)")
    out = out.replace("when row 165 closed", "when row 185 closed")
    out = out.replace("When row 165 closed", "When row 185 closed")
    out = out.replace("row 165 closed", "row 185 closed")
    out = out.replace("after row 165 alone", "after row 185 alone")
    out = out.replace("Recite [preface row 165]", "Recite [preface row 185]")
    out = out.replace("from row 165's", "from row 185's")
    out = out.replace("row 165 and row 66", "row 185 and row 66")
    out = out.replace("row 165 or row 146", "row 185 or row 166")
    out = out.replace("row 146", "row 166")
    out = out.replace("Row 146", "Row 166")
    out = out.replace(
        "row68-row126-writings-meta-prelude-capstone-reunion-index-row-146",
        "row68-row146-writings-meta-prelude-capstone-reunion-index-row-166",
    )
    out = out.replace(
        "row68-row146-writings-meta-prelude-capstone-reunion-index-row-166",
        "row68-row166-writings-meta-prelude-capstone-reunion-index-row-186",
    )
    out = out.replace("row 165", "row 185")
    out = out.replace("Row 165", "Row 185")
    out = out.replace(
        "before row 147 part-boundary meta prelude capstone reunion opens on the full capstone path",
        "before row 187 part-boundary meta prelude capstone reunion opens on the full capstone path",
    )
    out = out.replace(
        "Do not conflate row 186 (row 68 ↔ row 66 reunion on the full capstone path) with row 166",
        "Do not conflate row 186 (row 68 ↔ row 66 reunion on the full capstone path) with row 166",
    )
    out = out.replace(
        "row 166 names **Row 68 → Row 126 Row 68 → Row 66 Writings canonical meta prelude capstone reunion**",
        "row 166 names **Row 68 → Row 146 Row 68 → Row 66 Writings canonical meta prelude capstone reunion**",
    )
    return out


def extract_preface_row166(preface: str) -> str:
    start = preface.index("### Row 166 skill checkpoint")
    end = preface.index("\n\n### Row 167 skill checkpoint")
    return preface[start:end]


ROW186_PREFACE = t166_to_186(
    extract_preface_row166((ROOT / "writings/preface/chapters/preface.md").read_text())
) + "\n\n"

PROLOGUE_COMPASS = (
    "| Row 68 → Row 166 Row 68 → Row 66 Writings canonical meta prelude capstone reunion (row 186) | "
    "[Preface: row 186 skill checkpoint](../preface.md#skill-navigation-row-186) · "
    "[Row 68 → Row 166 Writings canonical meta prelude capstone reunion index](../appendix/sources.md#row68-row166-writings-meta-prelude-capstone-reunion-index-row-186) · "
    "[memory sheet row 186 baby picture](../appendix/memory-sheet.md#row-186-baby-picture-row68-row166-writings-meta-prelude-capstone-reunion) · "
    "[prologue row 186 preview row](#prologue-preview-row-186); [prologue row 186 closing stitch](#row-186-closing-stitch); "
    "[epilogue row 186 closing loop](../epilogue/multiscale.md#row-186-closing-loop) — "
    "read row 68 gate + row 185 or row 166 second-pass meta prelude capstone / Writings canonical meta prelude gate + epilogue writings cross-links + row 66 meta aloud "
    "when second pass reads as a novel on the full capstone path after verified book-loop meta prelude capstone but the next edit opens src/part* instead of writings/ |\n"
)

PROLOGUE_STITCH = t166_to_186(
    "**Row 166 closing stitch (Row 68 → Row 146 Row 68 → Row 66 Writings canonical meta prelude capstone reunion).** {#row-166-closing-stitch} "
    "When row 165 closed — second-pass meta prelude capstone verified on the full capstone path, row 164 or row 145 recited, and Scene → Bridge rhythm trusted after verified book-loop meta prelude capstone on the full capstone path — "
    "but **row 66 Writings canonical meta reunion still opens like standalone maintainer coursework after the Writings canonical opening prelude chapter hinge on the full capstone path** — "
    "`./scripts/sync-writings.sh --check` fails, the next prose edit opens `src/part*` instead of `writings/<part>/chapters/`, or the [epilogue Writings canonical cross-links audit](../epilogue/multiscale.md#opening-hinge-rows17-45-writings) feels like a build appendix beside row 46's meta audit while the unified HTML reads smoothly — "
    "read [preface row 166](../preface.md#skill-navigation-row-166), then the "
    "[Row 68 → Row 146 reunion index](../appendix/sources.md#row68-row146-writings-meta-prelude-capstone-reunion-index-row-166), then "
    "[epilogue row 166 closing loop](../epilogue/multiscale.md#row-166-closing-loop) before row 187 part-boundary meta prelude capstone reunion opens on the full capstone path.\n\n"
)

PROLOGUE_PREVIEW = (
    "| <span id=\"prologue-preview-row-186\"></span>Row 186 preview (Row 68 → Row 166 Row 68 → Row 66 Writings canonical meta prelude capstone reunion) | "
    "Explain why midpoint closure (row 68) and Writings canonical meta (row 66) must be read together with the epilogue writings cross-links and sync discipline "
    "after verified second-pass meta prelude capstone on the full capstone path before novel rhythm and canonical source tree feel like separate courses | "
    "One sentence: \"read row 68 gate + row 185 or row 166 second-pass meta prelude capstone / Writings canonical meta prelude gate + epilogue writings cross-links + row 66 meta aloud "
    "when second pass reads as a novel on the full capstone path after verified book-loop meta prelude capstone but the next edit opens src/part* instead of writings/\" — "
    "[preface row 186 skill checkpoint](../preface.md#skill-navigation-row-186); [prologue row 186 closing stitch](#row-186-closing-stitch); "
    "[Row 68 → Row 166 reunion index](../appendix/sources.md#row68-row166-writings-meta-prelude-capstone-reunion-index-row-186); "
    "[memory sheet row 186 baby picture](../appendix/memory-sheet.md#row-186-baby-picture-row68-row166-writings-meta-prelude-capstone-reunion); "
    "[epilogue Writings canonical cross-links audit](../epilogue/multiscale.md#opening-hinge-rows17-45-writings); "
    "[preface row 66 skill checkpoint](../preface.md#skill-navigation-row-66); "
    "[preface row 185 skill checkpoint](../preface.md#skill-navigation-row-185); "
    "[epilogue row 186 closing loop](../epilogue/multiscale.md#row-186-closing-loop) |\n"
)

_epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
EPILOGUE_LOOP = t166_to_186(
    "### Row 166 closing loop"
    + _epilogue.split("### Row 166 closing loop")[1].split("### Row 167 closing loop")[0]
)

SOURCES_TABLE = (
    "| 186 | Row 68 → Row 166 Row 68 → Row 66 Writings canonical meta prelude capstone (midpoint prelude gate ↔ second-pass meta prelude capstone on full capstone path ↔ row 66 meta) | "
    "[Row 68 → Row 166 Writings canonical meta prelude capstone reunion index](#row68-row166-writings-meta-prelude-capstone-reunion-index-row-186) · "
    "[preface row 186](../preface.md#skill-navigation-row-186) · "
    "[prologue row 186 preview](../prologue/00-many-scales.md#prologue-preview-row-186) · "
    "[prologue row 186 closing stitch](../prologue/00-many-scales.md#row-186-closing-stitch) · "
    "[epilogue row 186 closing loop](../epilogue/multiscale.md#row-186-closing-loop) · "
    "[memory sheet row 186 baby picture](memory-sheet.md#row-186-baby-picture-row68-row166-writings-meta-prelude-capstone-reunion) | "
    "Row 68 closed but **row 66 Writings canonical meta reunion still feels disconnected from verified second-pass meta prelude capstone on the full capstone path** — "
    "read row 68 + row 185 or row 166 gate + epilogue writings cross-links + row 66; "
    "[preface row 66](../preface.md#skill-navigation-row-66) |\n"
)

SOURCES_INDEX = t166_to_186(
    (ROOT / "writings/appendix/chapters/sources.md")
    .read_text()
    .split("## Row 68 → Row 146 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 166)")[1]
    .split("## Row 68 → Row 127 Row 68 → Row 67 part-boundary meta prelude capstone reunion index (row 167)")[0]
)
SOURCES_INDEX = (
    "## Row 68 → Row 166 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 186) {#row68-row166-writings-meta-prelude-capstone-reunion-index-row-186}"
    + SOURCES_INDEX
)

MEMORY_TABLE = (
    "| 186 | Meta | [Row 68 → Row 166 Writings canonical meta prelude capstone reunion index](sources.md#row68-row166-writings-meta-prelude-capstone-reunion-index-row-186) · "
    "[preface row 186 skill checkpoint](../preface.md#skill-navigation-row-186) · "
    "[prologue row 186 preview](../prologue/00-many-scales.md#prologue-preview-row-186) · "
    "[prologue row 186 closing stitch](../prologue/00-many-scales.md#row-186-closing-stitch) · "
    "[epilogue row 186 closing loop](../epilogue/multiscale.md#row-186-closing-loop) | "
    "Row 68 closed but row 66 Writings canonical meta reunion feels disconnected from verified second-pass meta prelude capstone on the full capstone path — "
    "read row 68 + row 185 or row 166 gate + epilogue writings cross-links + row 66; "
    "[row 186 baby picture](#row-186-baby-picture-row68-row166-writings-meta-prelude-capstone-reunion) |\n"
)

MEMORY_BABY = t166_to_186(
    (ROOT / "writings/appendix/chapters/memory-sheet.md")
    .read_text()
    .split("### Row 166 baby picture")[1]
    .split("### Row 167 baby picture")[0]
)
MEMORY_BABY = "### Row 186 baby picture" + MEMORY_BABY.split(")", 1)[1] if ")" in MEMORY_BABY else "### Row 186 baby picture" + MEMORY_BABY

ROW185_TAIL_OLD = (
    "When row 185 is complete, proceed to [row 146](preface.md#skill-navigation-row-146) when row 68 closed but Writings canonical meta prelude capstone still lags after second-pass meta prelude capstone on the full capstone path, to [row 126](preface.md#skill-navigation-row-146) for the Row 68 ↔ Row 66 meta audit on the opening-hinge capstone path alone, to [row 106](preface.md#skill-navigation-row-106) for the Row 68 ↔ Row 66 meta audit on the opening-hinge prelude path alone, to [row 165](preface.md#skill-navigation-row-125) for the Row 68 ↔ Row 65 second-pass meta audit on the opening-hinge capstone path alone, to [row 184](preface.md#skill-navigation-row-144) when book-loop meta prelude capstone still lags after verified orchestration meta prelude capstone on the full capstone path, to [row 85](preface.md#skill-navigation-row-85) for the Row 68 ↔ Row 65 opening prelude audit alone, to [row 65](preface.md#skill-navigation-row-65) for the Row 64 ↔ Row 45 meta audit alone, to [row 45](preface.md#skill-navigation-row-45) for the full Rows 17–44 → row 17 meta audit, or extend prose only under `writings/` then sync."
)
ROW185_TAIL_NEW = (
    "When row 185 is complete, proceed to [row 186](preface.md#skill-navigation-row-186) when row 68 closed but Writings canonical meta prelude capstone still lags after second-pass meta prelude capstone on the full capstone path, to [row 166](preface.md#skill-navigation-row-166) for the Row 68 ↔ Row 66 meta audit on the opening-hinge capstone path alone, to [row 106](preface.md#skill-navigation-row-106) for the Row 68 ↔ Row 66 meta audit on the opening-hinge prelude path alone, to [row 165](preface.md#skill-navigation-row-165) for the Row 68 ↔ Row 65 second-pass meta audit on the opening-hinge capstone path alone, to [row 184](preface.md#skill-navigation-row-184) when book-loop meta prelude capstone still lags after verified orchestration meta prelude capstone on the full capstone path, to [row 85](preface.md#skill-navigation-row-85) for the Row 68 ↔ Row 65 opening prelude audit alone, to [row 65](preface.md#skill-navigation-row-65) for the Row 64 ↔ Row 45 meta audit alone, to [row 45](preface.md#skill-navigation-row-45) for the full Rows 17–44 → row 17 meta audit, or extend prose only under `writings/` then sync."
)

ROW185_EPILOGUE_PROCEED_OLD = (
    "Proceed to [row 166](#row-166-closing-loop) when row 68 closed but Writings canonical meta prelude capstone still lags after row 165 on the full capstone path,"
)
ROW185_EPILOGUE_PROCEED_NEW = (
    "Proceed to [row 186](#row-186-closing-loop) when row 68 closed but Writings canonical meta prelude capstone still lags after row 185 on the full capstone path,"
)

ROW185_BABY_OLD = (
    "row 185 when **epilogue second-pass cross-links and Row 63 → Row 44 meta must read on the same wire before row 166 Writings canonical meta prelude capstone reunion opens on the full capstone path**"
)
ROW185_BABY_NEW = (
    "row 185 when **epilogue second-pass cross-links and Row 63 → Row 44 meta must read on the same wire before row 186 Writings canonical meta prelude capstone reunion opens on the full capstone path**"
)


def main() -> None:
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "{#skill-navigation-row-186}" in preface and preface.index("{#skill-navigation-row-186}") < preface.index(copper):
        print("preface: row 186 already present")
    elif "{#skill-navigation-row-186}" in preface:
        raise SystemExit("preface row 186 exists but not at copper wire insert point")
    else:
        if ROW185_TAIL_OLD not in preface:
            raise SystemExit("preface row 185 tail not found")
        preface = preface.replace(ROW185_TAIL_OLD, ROW185_TAIL_NEW)
        preface = preface.replace(copper, "\n" + ROW186_PREFACE + copper)
        preface_path.write_text(preface)
        print("preface: added row 186")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-186" not in prologue:
        needle = "| Row 68 → Row 165 Row 68 → Row 65 second-pass meta prelude capstone reunion (row 185) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 185 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + PROLOGUE_COMPASS + prologue[line_end + 1 :]
        prologue = prologue.replace(
            "**Row 185 closing stitch",
            PROLOGUE_STITCH + "**Row 185 closing stitch",
        )
        prologue = prologue.replace(
            '| <span id="prologue-preview-row-185"></span>Row 185 preview',
            PROLOGUE_PREVIEW + '| <span id="prologue-preview-row-185"></span>Row 185 preview',
        )
        prologue_path.write_text(prologue)
        print("prologue: added row 186")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "### Row 186 closing loop" not in epilogue:
        if ROW185_EPILOGUE_PROCEED_OLD in epilogue:
            epilogue = epilogue.replace(ROW185_EPILOGUE_PROCEED_OLD, ROW185_EPILOGUE_PROCEED_NEW)
        marker = "### Row 185 closing loop (Row 68 → Row 165 Row 68 → Row 65 second-pass meta prelude capstone reunion)"
        if marker not in epilogue:
            raise SystemExit("epilogue row 185 insert anchor not found")
        epilogue = epilogue.replace(marker, EPILOGUE_LOOP + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 186")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row166-writings-meta-prelude-capstone-reunion-index-row-186" not in sources:
        sources = sources.replace(
            "| 166 | Row 68 → Row 146 Row 68 → Row 66 Writings canonical meta prelude capstone",
            SOURCES_TABLE + "| 166 | Row 68 → Row 146 Row 68 → Row 66 Writings canonical meta prelude capstone",
        )
        sources = sources.replace(
            "## Row 68 → Row 146 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 166)",
            SOURCES_INDEX + "## Row 68 → Row 146 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 166)",
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 186")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-186-baby-picture-row68-row166" not in memory:
        memory = memory.replace(
            "| 185 | Meta | [Row 68 → Row 165 second-pass meta prelude capstone reunion index]",
            MEMORY_TABLE + "| 185 | Meta | [Row 68 → Row 165 second-pass meta prelude capstone reunion index]",
        )
        memory = memory.replace(
            "### Row 166 baby picture {#row-166-baby-picture-row68-row146-writings-meta-prelude-capstone-reunion}",
            MEMORY_BABY + "### Row 166 baby picture {#row-166-baby-picture-row68-row146-writings-meta-prelude-capstone-reunion}",
            1,
        )
        if ROW185_BABY_OLD in memory:
            memory = memory.replace(ROW185_BABY_OLD, ROW185_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 186")


if __name__ == "__main__":
    main()
