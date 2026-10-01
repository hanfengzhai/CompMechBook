#!/usr/bin/env python3
"""Add row 176 meta-stitch (Row 68 → Row 156 ↔ Row 56 Born–Oppenheimer meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def t156_to_176(text: str) -> str:
    """Transform row-156 capstone-path meta copy to row 176 (156→176, 136→156 inner, 175 gate)."""
    repl = [
        ("Row 68 → Row 136 Row 68 → Row 56", "Row 68 → Row 156 Row 68 → Row 56"),
        (
            "row68-row136-born-oppenheimer-meta-prelude-capstone-reunion-index-row-156",
            "TEMP_ROW176_EXP_INDEX",
        ),
        (
            "row-156-baby-picture-row68-row136-born-oppenheimer-meta-prelude-capstone-reunion",
            "row-176-baby-picture-row68-row156-born-oppenheimer-meta-prelude-capstone-reunion",
        ),
        ("skill-navigation-row-156", "TEMP_SKILL_NAV_156"),
        ("prologue-preview-row-156", "prologue-preview-row-176"),
        ("row-156-closing-stitch", "row-176-closing-stitch"),
        ("row-156-closing-loop", "row-176-closing-loop"),
        ("Row 156 three-way audit", "Row 176 three-way audit"),
        (
            "[row 155](preface.md#skill-navigation-row-155) or [row 136](TEMP_SKILL_NAV_156)",
            "[row 175](preface.md#skill-navigation-row-175) or [row 156](TEMP_SKILL_NAV_156)",
        ),
        (
            "[row 155](preface.md#skill-navigation-row-155) or [Row 68 → Row 116 Born–Oppenheimer meta prelude capstone reunion index (row 136)](appendix/sources.md#row68-row116-born-oppenheimer-meta-prelude-capstone-reunion-index-row-136)",
            "[row 175](preface.md#skill-navigation-row-175) or [Row 68 → Row 156 Born–Oppenheimer meta prelude capstone reunion index (row 176)](appendix/sources.md#row68-row156-born-oppenheimer-meta-prelude-capstone-reunion-index-row-176)",
        ),
        (
            "[row 155](preface.md#skill-navigation-row-155) or [Row 68 → Row 136 Born–Oppenheimer meta prelude capstone reunion index (row 156)](appendix/sources.md#row68-row136-born-oppenheimer-meta-prelude-capstone-reunion-index-row-156)",
            "[row 175](preface.md#skill-navigation-row-175) or [Row 68 → Row 156 Born–Oppenheimer meta prelude capstone reunion index (row 176)](appendix/sources.md#row68-row156-born-oppenheimer-meta-prelude-capstone-reunion-index-row-176)",
        ),
        (
            "verified electronic audit meta prelude capstone closure (row 155)",
            "verified electronic audit meta prelude capstone closure (row 175)",
        ),
        (
            "before row 157 Kohn–Sham meta prelude capstone reunion opens on the full capstone path",
            "before row 177 Kohn–Sham meta prelude capstone reunion opens on the full capstone path",
        ),
        (
            "before row 158 DFT workflows meta prelude capstone reunion opens on the full capstone path",
            "before row 178 DFT workflows meta prelude capstone reunion opens on the full capstone path",
        ),
    ]
    out = text
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW176_EXP_INDEX",
        "row68-row156-born-oppenheimer-meta-prelude-capstone-reunion-index-row-176",
    )
    out = out.replace("TEMP_SKILL_NAV_156", "skill-navigation-row-156")
    out = out.replace("row 156", "row 176")
    out = out.replace("Row 156", "Row 176")
    out = out.replace("skill-navigation-row-156", "skill-navigation-row-176")
    out = out.replace("[row 176](preface.md#skill-navigation-row-175)", "[row 175](preface.md#skill-navigation-row-175)")
    out = out.replace("[row 176](preface.md#skill-navigation-row-176)", "[row 176](preface.md#skill-navigation-row-176)")
    out = out.replace("[row 176](preface.md#skill-navigation-row-156)", "[row 156](preface.md#skill-navigation-row-156)")
    out = out.replace("[row 156](preface.md#skill-navigation-row-176)", "[row 156](preface.md#skill-navigation-row-156)")
    out = out.replace("when row 155 closed but row 56", "when row 175 closed but row 56")
    out = out.replace("[preface row 156](../preface.md#skill-navigation-row-176)", "[preface row 156](../preface.md#skill-navigation-row-156)")
    out = out.replace("row 1566", "row 177")
    out = out.replace("row 1567", "row 178")
    out = out.replace("row 176 or row 176", "row 175 or row 156")
    out = out.replace("When row 176 closed", "When row 175 closed")
    out = out.replace("after row 176 alone", "after row 175 alone")
    out = out.replace("Recite [preface row 176]", "Recite [preface row 175]")
    out = out.replace("row 176 or row 156 recited", "row 175 or row 156 recited")
    out = out.replace("When row 176 closed — Born", "When row 175 closed — Born")
    out = out.replace("When row 155 closed — Born", "When row 175 closed — Born")
    out = out.replace("row 155 or row 136 recited", "row 175 or row 156 recited")
    out = out.replace("row 155 or row 56 recited", "row 175 or row 56 recited")
    out = out.replace("when row 155 closed Born", "when row 175 closed Born")
    out = out.replace("(preface.md#skill-navigation-row-136)", "(preface.md#skill-navigation-row-156)")
    out = out.replace(
        "Row 68 → Row 176 Born–Oppenheimer meta prelude capstone reunion index",
        "Row 68 → Row 156 Born–Oppenheimer meta prelude capstone reunion index",
    )
    out = out.replace("row 154 or row 135 recited", "row 175 or row 156 recited")
    out = out.replace("row 154 or row 55 recited", "row 174 or row 155 recited")
    out = out.replace("row 136", "row 156")
    out = out.replace("Row 136", "Row 156")
    out = out.replace("row 116", "row 136")
    out = out.replace("Row 116", "Row 136")
    out = out.replace(
        "row68-row116-born-oppenheimer-meta-prelude-capstone-reunion-index-row-136",
        "row68-row136-born-oppenheimer-meta-prelude-capstone-reunion-index-row-156",
    )
    out = out.replace(
        "row68-row135-electronic-audit-meta-prelude-capstone-reunion-index-row-155",
        "row68-row155-electronic-audit-meta-prelude-capstone-reunion-index-row-175",
    )
    out = out.replace("Row 68 → Row 176 Row 68 → Row 56", "Row 68 → Row 156 Row 68 → Row 56")
    out = out.replace(
        "[preface row 156](../preface.md#skill-navigation-row-136)",
        "[preface row 156](../preface.md#skill-navigation-row-156)",
    )
    out = out.replace(
        "Confirm [row 155](preface.md#skill-navigation-row-155) or [Row 68 → Row 156",
        "Confirm [row 175](preface.md#skill-navigation-row-175) or [Row 68 → Row 156",
    )
    out = out.replace(
        "and [row 155](preface.md#skill-navigation-row-155) or [row 156]",
        "and [row 175](preface.md#skill-navigation-row-175) or [row 156]",
    )
    out = out.replace("[row 136](preface.md#skill-navigation-row-116)", "[row 136](preface.md#skill-navigation-row-136)")
    out = out.replace("(preface.md#skill-navigation-row-176) when `cu.relax", "(preface.md#skill-navigation-row-156) when `cu.relax")
    out = out.replace("when row 155 and row 56", "when row 175 and row 56")
    out = out.replace("after row 155 alone", "after row 175 alone")
    out = out.replace("Scene after row 155.", "Scene after row 175.")
    out = out.replace("from row 176's", "from row 175's")
    out = out.replace("row 155's foundation SCF", "row 175's foundation SCF")
    out = out.replace("row 155 tells you", "row 175 tells you")
    out = out.replace(
        "[IX.0 Bridge](part09-dft/00-opening.md#bridge)",
        "[IX.0 Bridge → opening hinge → IX.1 BO/HK](part09-dft/00-opening.md#bridge)",
    )
    out = out.replace("row 155", "row 175")
    out = out.replace("Row 155", "Row 175")
    out = out.replace("[row 175](preface.md#skill-navigation-row-175)", "[row 175](preface.md#skill-navigation-row-175)")
    out = out.replace("[row 175](preface.md#skill-navigation-row-156)", "[row 156](preface.md#skill-navigation-row-156)")
    return out


def extract_preface_row156(preface: str) -> str:
    start = preface.index("### Row 156 skill checkpoint")
    end = preface.index("\n\n### Row 157 skill checkpoint")
    return preface[start:end]


ROW176_PREFACE = t156_to_176(extract_preface_row156((ROOT / "writings/preface/chapters/preface.md").read_text())) + "\n\n"

_prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
_row156_compass = next(
    line for line in _prologue.splitlines() if "(row 156) |" in line and "Row 68 → Row 136" in line
)
PROLOGUE_COMPASS = t156_to_176(_row156_compass) + "\n"

_row156_stitch_body = (
    _prologue.split("**Row 156 closing stitch")[1].split("**Row 175 closing stitch")[0].lstrip().split("\n\n")[0]
)
PROLOGUE_STITCH = t156_to_176(
    "**Row 156 closing stitch (Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion).** {#row-156-closing-stitch} "
    + _row156_stitch_body.split(".** {#row-156-closing-stitch} ", 1)[-1]
) + "\n\n"

_row156_preview = next(
    line for line in _prologue.splitlines() if 'id="prologue-preview-row-156"' in line
)
PROLOGUE_PREVIEW = t156_to_176(_row156_preview) + "\n"

_epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
EPILOGUE_LOOP = t156_to_176(
    "### Row 156 closing loop"
    + _epilogue.split("### Row 156 closing loop")[1].split("### Row 157 closing loop")[0]
)

_src156_header = "## Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion index (row 156)"
_sources_blob = (ROOT / "writings/appendix/chapters/sources.md").read_text()
SOURCES_INDEX = t156_to_176(
    _sources_blob.split(_src156_header)[1].split(_src156_header)[0]
)
SOURCES_INDEX = (
    "## Row 68 → Row 156 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion index (row 176)"
    + SOURCES_INDEX
)

_row156_table = next(
    line for line in _sources_blob.splitlines() if line.startswith("| 156 | Row 68 → Row 136")
)
SOURCES_TABLE = t156_to_176(_row156_table).replace("| 156 | Row 68 → Row 156", "| 176 | Row 68 → Row 156", 1) + "\n"

_row156_mem_table = next(
    line for line in (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text().splitlines()
    if line.startswith("| 156 | Meta |")
)
MEMORY_TABLE = t156_to_176(_row156_mem_table).replace("| 156 | Meta |", "| 176 | Meta |", 1) + "\n"

MEMORY_BABY = t156_to_176(
    (ROOT / "writings/appendix/chapters/memory-sheet.md")
    .read_text()
    .split("### Row 156 baby picture (Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion)")[1]
    .split("### Row 157 baby picture")[0]
)
MEMORY_BABY = (
    "### Row 176 baby picture (Row 68 → Row 156 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion)"
    + MEMORY_BABY.split(")", 1)[1]
    if ")" in MEMORY_BABY
    else "### Row 176 baby picture" + MEMORY_BABY
)

ROW175_BABY_OLD = (
    "row 175 when **VIII.3 Bridge and Row 68 → Row 55 meta must read on the same wire before row 156 Born–Oppenheimer meta prelude capstone opens on the full capstone path**"
)
ROW175_BABY_NEW = (
    "row 175 when **IX.0 Bridge and Row 68 → Row 56 meta must read on the same wire before row 176 Born–Oppenheimer meta prelude capstone opens on the full capstone path**"
)


def main():
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "skill-navigation-row-176" in preface:
        print("preface: row 176 already present")
    else:
        if "skill-navigation-row-175" not in preface:
            raise SystemExit("preface row 175 must exist before row 176")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + ROW176_PREFACE + copper)
        preface_path.write_text(preface)
        print("preface: added row 176")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-176" not in prologue:
        needle = "| Row 68 → Row 155 Row 68 → Row 55 electronic audit meta prelude capstone reunion (row 175) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 175 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + PROLOGUE_COMPASS + prologue[line_end + 1 :]
        prologue = prologue.replace(
            "**Row 175 closing stitch",
            PROLOGUE_STITCH + "**Row 175 closing stitch",
        )
        prologue = prologue.replace(
            '| <span id="prologue-preview-row-175"></span>Row 175 preview',
            PROLOGUE_PREVIEW + '| <span id="prologue-preview-row-175"></span>Row 175 preview',
        )
        prologue_path.write_text(prologue)
        print("prologue: added row 176")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "row-176-closing-loop" not in epilogue:
        marker = (
            "Proceed to [row 156](#row-156-closing-loop) when row 68 closed but Born–Oppenheimer meta prelude capstone still lags after row 175 on the full capstone path, to [row 136](#row-136-closing-loop) when row 68 closed but Born–Oppenheimer meta prelude capstone still lags after row 155 on the opening-hinge capstone path alone, to [row 116](#row-116-closing-loop) for the Row 68 ↔ Row 56 Born–Oppenheimer meta audit on the opening-hinge prelude path alone, to [row 155](#row-135-closing-loop) for the Row 68 ↔ Row 55 electronic audit meta audit on the opening-hinge capstone path alone, to [row 174](#row-154-closing-loop) when yaml exports still stall after verified dynamics meta prelude capstone on the full capstone path, to [row 55](#row-55-closing-loop) when only VIII.3 → IX.0 stalls, or extend prose only under `writings/` then sync.\n\n\n\n\n\n"
        )
        replacement = (
            "Proceed to [row 176](#row-176-closing-loop) when row 68 closed but Born–Oppenheimer meta prelude capstone still lags after row 175 on the full capstone path, to [row 156](#row-156-closing-loop) when Born–Oppenheimer meta prelude capstone still lags after verified electronic audit meta prelude capstone on the opening-hinge capstone path alone, to [row 116](#row-116-closing-loop) for the Row 68 ↔ Row 56 Born–Oppenheimer meta audit on the opening-hinge prelude path alone, to [row 155](#row-155-closing-loop) for the Row 68 ↔ Row 55 electronic audit meta audit on the opening-hinge capstone path alone, to [row 174](#row-174-closing-loop) when yaml exports still stall after verified dynamics meta prelude capstone on the full capstone path, to [row 56](#row-56-closing-loop) when only IX.0 → IX.1 stalls, or extend prose only under `writings/` then sync.\n\n\n"
            + EPILOGUE_LOOP
            + "\n\n\n\n\n"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 175 end marker not found")
        epilogue = epilogue.replace(marker, replacement, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 176")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row156-born-oppenheimer-meta-prelude-capstone-reunion-index-row-176" not in sources:
        sources = sources.replace(
            "| 156 | Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone",
            SOURCES_TABLE + "| 156 | Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone",
        )
        sources = sources.replace(
            _src156_header,
            SOURCES_INDEX + _src156_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 176")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-176-baby-picture-row68-row156" not in memory:
        memory = memory.replace(
            "| 175 | Meta | [Row 68 → Row 155 electronic audit meta prelude capstone reunion index]",
            MEMORY_TABLE + "| 175 | Meta | [Row 68 → Row 155 electronic audit meta prelude capstone reunion index]",
        )
        memory = memory.replace(
            "### Row 156 baby picture (Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion) {#row-156-baby-picture-row68-row136-born-oppenheimer-meta-prelude-capstone-reunion}",
            MEMORY_BABY + "### Row 156 baby picture (Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion) {#row-156-baby-picture-row68-row136-born-oppenheimer-meta-prelude-capstone-reunion}",
            1,
        )
        if ROW175_BABY_OLD in memory:
            memory = memory.replace(ROW175_BABY_OLD, ROW175_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 176")


if __name__ == "__main__":
    main()
