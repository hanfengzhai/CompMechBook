#!/usr/bin/env python3
"""Add row 177 meta-stitch (Row 68 → Row 157 ↔ Row 57 Kohn–Sham meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def t157_to_177(text: str) -> str:
    """Transform row-157 capstone-path meta copy to row 177 (157→177, 137→157 inner, 176 gate)."""
    repl = [
        ("Row 68 → Row 137 Row 68 → Row 57", "Row 68 → Row 157 Row 68 → Row 57"),
        (
            "row68-row137-kohn-sham-meta-prelude-capstone-reunion-index-row-157",
            "TEMP_ROW177_EXP_INDEX",
        ),
        (
            "row-157-baby-picture-row68-row137-kohn-sham-meta-prelude-capstone-reunion",
            "row-177-baby-picture-row68-row157-kohn-sham-meta-prelude-capstone-reunion",
        ),
        ("skill-navigation-row-157", "TEMP_SKILL_NAV_157"),
        ("prologue-preview-row-157", "prologue-preview-row-177"),
        ("row-157-closing-stitch", "row-177-closing-stitch"),
        ("row-157-closing-loop", "row-177-closing-loop"),
        ("Row 157 three-way audit", "Row 177 three-way audit"),
        (
            "[row 156](preface.md#skill-navigation-row-156) or [row 137](TEMP_SKILL_NAV_157)",
            "[row 176](preface.md#skill-navigation-row-176) or [row 157](TEMP_SKILL_NAV_157)",
        ),
        (
            "[row 156](preface.md#skill-navigation-row-156) or [Row 68 → Row 117 Kohn–Sham meta prelude capstone reunion index (row 137)](appendix/sources.md#row68-row117-kohn-sham-meta-prelude-capstone-reunion-index-row-137)",
            "[row 176](preface.md#skill-navigation-row-176) or [Row 68 → Row 157 Kohn–Sham meta prelude capstone reunion index (row 177)](appendix/sources.md#row68-row157-kohn-sham-meta-prelude-capstone-reunion-index-row-177)",
        ),
        (
            "[row 156](preface.md#skill-navigation-row-156) or [Row 68 → Row 137 Kohn–Sham meta prelude capstone reunion index (row 157)](appendix/sources.md#row68-row137-kohn-sham-meta-prelude-capstone-reunion-index-row-157)",
            "[row 176](preface.md#skill-navigation-row-176) or [Row 68 → Row 157 Kohn–Sham meta prelude capstone reunion index (row 177)](appendix/sources.md#row68-row157-kohn-sham-meta-prelude-capstone-reunion-index-row-177)",
        ),
        (
            "verified Born–Oppenheimer meta prelude capstone closure (row 156)",
            "verified Born–Oppenheimer meta prelude capstone closure (row 176)",
        ),
        (
            "before row 158 DFT workflows meta prelude capstone reunion opens on the full capstone path",
            "before row 178 DFT workflows meta prelude capstone reunion opens on the full capstone path",
        ),
        (
            "before row 159 Handshake 3 meta prelude capstone reunion opens on the full capstone path",
            "before row 179 Handshake 3 meta prelude capstone reunion opens on the full capstone path",
        ),
    ]
    out = text
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW177_EXP_INDEX",
        "row68-row157-kohn-sham-meta-prelude-capstone-reunion-index-row-177",
    )
    out = out.replace("TEMP_SKILL_NAV_157", "skill-navigation-row-157")
    out = out.replace("row 157", "row 177")
    out = out.replace("Row 157", "Row 177")
    out = out.replace("skill-navigation-row-157", "skill-navigation-row-177")
    out = out.replace("[row 177](preface.md#skill-navigation-row-176)", "[row 176](preface.md#skill-navigation-row-176)")
    out = out.replace("[row 177](preface.md#skill-navigation-row-177)", "[row 177](preface.md#skill-navigation-row-177)")
    out = out.replace("[row 177](preface.md#skill-navigation-row-157)", "[row 157](preface.md#skill-navigation-row-157)")
    out = out.replace("[row 157](preface.md#skill-navigation-row-177)", "[row 157](preface.md#skill-navigation-row-157)")
    out = out.replace("when row 156 closed but row 57", "when row 176 closed but row 57")
    out = out.replace("[preface row 157](../preface.md#skill-navigation-row-177)", "[preface row 157](../preface.md#skill-navigation-row-157)")
    out = out.replace("row 1577", "row 178")
    out = out.replace("row 1578", "row 179")
    out = out.replace("row 177 or row 177", "row 176 or row 157")
    out = out.replace("When row 177 closed", "When row 176 closed")
    out = out.replace("after row 177 alone", "after row 176 alone")
    out = out.replace("Recite [preface row 177]", "Recite [preface row 176]")
    out = out.replace("row 177 or row 157 recited", "row 176 or row 157 recited")
    out = out.replace("When row 177 closed — Born", "When row 176 closed — Born")
    out = out.replace("When row 156 closed — Born", "When row 176 closed — Born")
    out = out.replace("row 156 or row 137 recited", "row 176 or row 157 recited")
    out = out.replace("row 155 or row 136 recited", "row 175 or row 156 recited")
    out = out.replace("row 156 or row 57 recited", "row 176 or row 57 recited")
    out = out.replace("when row 156 closed Born", "when row 176 closed Born")
    out = out.replace("(preface.md#skill-navigation-row-137)", "(preface.md#skill-navigation-row-157)")
    out = out.replace(
        "Row 68 → Row 177 Kohn–Sham meta prelude capstone reunion index",
        "Row 68 → Row 157 Kohn–Sham meta prelude capstone reunion index",
    )
    out = out.replace("row 155 or row 136 recited", "row 175 or row 156 recited")
    out = out.replace("row 137", "row 157")
    out = out.replace("Row 137", "Row 157")
    out = out.replace("row 117", "row 137")
    out = out.replace("Row 117", "Row 137")
    out = out.replace(
        "row68-row117-kohn-sham-meta-prelude-capstone-reunion-index-row-137",
        "row68-row137-kohn-sham-meta-prelude-capstone-reunion-index-row-157",
    )
    out = out.replace(
        "row68-row136-born-oppenheimer-meta-prelude-capstone-reunion-index-row-156",
        "row68-row156-born-oppenheimer-meta-prelude-capstone-reunion-index-row-176",
    )
    out = out.replace("Row 68 → Row 177 Row 68 → Row 57", "Row 68 → Row 157 Row 68 → Row 57")
    out = out.replace(
        "[preface row 157](../preface.md#skill-navigation-row-137)",
        "[preface row 157](../preface.md#skill-navigation-row-157)",
    )
    out = out.replace(
        "Confirm [row 156](preface.md#skill-navigation-row-156) or [Row 68 → Row 157",
        "Confirm [row 176](preface.md#skill-navigation-row-176) or [Row 68 → Row 157",
    )
    out = out.replace(
        "and [row 156](preface.md#skill-navigation-row-156) or [row 157]",
        "and [row 176](preface.md#skill-navigation-row-176) or [row 157]",
    )
    out = out.replace("[row 137](preface.md#skill-navigation-row-117)", "[row 137](preface.md#skill-navigation-row-137)")
    out = out.replace(
        "(preface.md#skill-navigation-row-177) when `murnaghan",
        "(preface.md#skill-navigation-row-157) when `murnaghan",
    )
    out = out.replace("when row 156 and row 57", "when row 176 and row 57")
    out = out.replace("after row 156 alone", "after row 176 alone")
    out = out.replace("Scene after row 156.", "Scene after row 176.")
    out = out.replace("from row 177's", "from row 176's")
    out = out.replace("row 156's theorem vocabulary", "row 176's theorem vocabulary")
    out = out.replace("row 156 tells you", "row 176 tells you")
    out = out.replace(
        "[IX.1 Bridge](part09-dft/01-born-oppenheimer.md#bridge)",
        "[IX.1 Bridge → opening hinge → IX.2 Kohn–Sham SCF](part09-dft/01-born-oppenheimer.md#bridge)",
    )
    out = out.replace("row 156", "row 176")
    out = out.replace("Row 156", "Row 176")
    out = out.replace("Row 68 → Row 176 Row 68 → Row 56", "Row 68 → Row 156 Row 68 → Row 56")
    out = out.replace("[row 176](preface.md#skill-navigation-row-176)", "[row 176](preface.md#skill-navigation-row-176)")
    out = out.replace("[row 176](preface.md#skill-navigation-row-157)", "[row 157](preface.md#skill-navigation-row-157)")
    return out


def extract_preface_row157(preface: str) -> str:
    start = preface.index("### Row 157 skill checkpoint")
    end = preface.index("\n\n### Row 158 skill checkpoint")
    return preface[start:end]


ROW177_PREFACE = t157_to_177(extract_preface_row157((ROOT / "writings/preface/chapters/preface.md").read_text())) + "\n\n"

_prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
_row157_compass = next(
    line for line in _prologue.splitlines() if "(row 157) |" in line and "Row 68 → Row 137" in line
)
PROLOGUE_COMPASS = t157_to_177(_row157_compass) + "\n"

_row157_stitch_body = (
    _prologue.split("**Row 157 closing stitch")[1].split("**Row 158 closing stitch")[0].lstrip().split("\n\n")[0]
)
PROLOGUE_STITCH = t157_to_177(
    "**Row 157 closing stitch (Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion).** {#row-157-closing-stitch} "
    + _row157_stitch_body.split(".** {#row-157-closing-stitch} ", 1)[-1]
) + "\n\n"

_row157_preview = next(line for line in _prologue.splitlines() if 'id="prologue-preview-row-157"' in line)
PROLOGUE_PREVIEW = t157_to_177(_row157_preview) + "\n"

_epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
EPILOGUE_LOOP = t157_to_177(
    "### Row 157 closing loop"
    + _epilogue.split("### Row 157 closing loop")[1].split("### Row 158 closing loop")[0]
)

_src157_header = "## Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion index (row 157)"
_next157_header = "## Row 68 → Row 118 Row 68 → Row 58 DFT workflows meta prelude capstone reunion index (row 138)"
_sources_blob = (ROOT / "writings/appendix/chapters/sources.md").read_text()
_src157_body = _sources_blob.split(_src157_header, 1)[1].split(_next157_header, 1)[0]
SOURCES_INDEX = (
    "## Row 68 → Row 157 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion index (row 177)"
    + t157_to_177(_src157_body)
)

_row157_table = next(
    line for line in _sources_blob.splitlines() if line.startswith("| 157 | Row 68 → Row 137")
)
SOURCES_TABLE = t157_to_177(_row157_table).replace("| 157 | Row 68 → Row 157", "| 177 | Row 68 → Row 157", 1) + "\n"

_row157_mem_table = next(
    line for line in (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text().splitlines()
    if line.startswith("| 157 | Meta |")
)
MEMORY_TABLE = t157_to_177(_row157_mem_table).replace("| 157 | Meta |", "| 177 | Meta |", 1) + "\n"

MEMORY_BABY = t157_to_177(
    (ROOT / "writings/appendix/chapters/memory-sheet.md")
    .read_text()
    .split("### Row 157 baby picture (Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion)")[1]
    .split("### Row 158 baby picture")[0]
)
MEMORY_BABY = (
    "### Row 177 baby picture (Row 68 → Row 157 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion)"
    + MEMORY_BABY.split(")", 1)[1]
    if ")" in MEMORY_BABY
    else "### Row 177 baby picture" + MEMORY_BABY
)

ROW176_BABY_OLD = (
    "row 176 when **IX.0 Bridge and Row 68 → Row 56 meta must read on the same wire before row 157 Kohn–Sham meta prelude capstone opens on the full capstone path**"
)
ROW176_BABY_NEW = (
    "row 176 when **IX.1 Bridge and Row 68 → Row 57 meta must read on the same wire before row 177 Kohn–Sham meta prelude capstone opens on the full capstone path**"
)


def main():
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "skill-navigation-row-177" in preface and preface.index("skill-navigation-row-177") < preface.index(copper):
        print("preface: row 177 already present")
    elif "skill-navigation-row-177" in preface:
        raise SystemExit("preface row 177 exists but not at copper wire insert point")
    else:
        if "skill-navigation-row-176" not in preface:
            raise SystemExit("preface row 176 must exist before row 177")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + ROW177_PREFACE + copper)
        preface_path.write_text(preface)
        print("preface: added row 177")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-177" not in prologue:
        needle = "| Row 68 → Row 156 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion (row 176) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 176 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + PROLOGUE_COMPASS + prologue[line_end + 1 :]
        prologue = prologue.replace(
            "**Row 176 closing stitch",
            PROLOGUE_STITCH + "**Row 176 closing stitch",
        )
        prologue = prologue.replace(
            '| <span id="prologue-preview-row-176"></span>Row 176 preview',
            PROLOGUE_PREVIEW + '| <span id="prologue-preview-row-176"></span>Row 176 preview',
        )
        prologue_path.write_text(prologue)
        print("prologue: added row 177")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "row-177-closing-loop" not in epilogue:
        marker = (
            "Proceed to [row 157](#row-157-closing-loop) when row 68 closed but Kohn–Sham meta prelude capstone still lags after row 176 on the full capstone path, to [row 137](#row-137-closing-loop) when row 68 closed but Kohn–Sham meta prelude capstone still lags after row 156 on the opening-hinge capstone path alone, to [row 156](#row-136-closing-loop) when row 68 closed but Born–Oppenheimer meta prelude capstone still lags after row 135 on the opening-hinge capstone path alone, to [row 117](#row-117-closing-loop) for the Row 68 ↔ Row 57 Kohn–Sham meta audit on the opening-hinge prelude path alone, to [row 136](#row-116-closing-loop) for the Row 68 ↔ Row 56 Born–Oppenheimer meta audit on the opening-hinge prelude path alone, to [row 154](#row-154-closing-loop) when `cu.relax.out` is missing after verified export meta prelude capstone on the full capstone path, to [row 175](#row-155-closing-loop) when foundation SCF still stalls on the full capstone path, to [row 56](#row-56-closing-loop) when only IX.0 → IX.1 stalls, or extend prose only under `writings/` then sync.\n\n\n\n\n\n"
        )
        replacement = (
            "Proceed to [row 177](#row-177-closing-loop) when row 68 closed but Kohn–Sham meta prelude capstone still lags after row 176 on the full capstone path, to [row 157](#row-157-closing-loop) when Kohn–Sham meta prelude capstone still lags after verified Born–Oppenheimer meta prelude capstone on the opening-hinge capstone path alone, to [row 137](#row-137-closing-loop) when row 68 closed but Kohn–Sham meta prelude capstone still lags after row 156 on the opening-hinge capstone path alone, to [row 117](#row-117-closing-loop) for the Row 68 ↔ Row 57 Kohn–Sham meta audit on the opening-hinge prelude path alone, to [row 136](#row-116-closing-loop) for the Row 68 ↔ Row 56 Born–Oppenheimer meta audit on the opening-hinge prelude path alone, to [row 154](#row-154-closing-loop) when `cu.relax.out` is missing after verified export meta prelude capstone on the full capstone path, to [row 176](#row-176-closing-loop) when `murnaghan_eos.yaml` is missing after verified Born–Oppenheimer meta prelude capstone on the full capstone path, to [row 156](#row-156-closing-loop) when `murnaghan_eos.yaml` is missing on the opening-hinge capstone path alone, to [row 57](#row-57-closing-loop) when only IX.1 → IX.2 stalls, or extend prose only under `writings/` then sync.\n\n\n"
            + EPILOGUE_LOOP
            + "\n\n\n\n\n"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 176 end marker not found")
        epilogue = epilogue.replace(marker, replacement, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 177")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row157-kohn-sham-meta-prelude-capstone-reunion-index-row-177" not in sources:
        sources = sources.replace(
            "| 157 | Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone",
            SOURCES_TABLE + "| 157 | Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone",
        )
        sources = sources.replace(
            _src157_header,
            SOURCES_INDEX + _src157_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 177")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-177-baby-picture-row68-row157" not in memory:
        memory = memory.replace(
            "| 176 | Meta | [Row 68 → Row 156 Born–Oppenheimer meta prelude capstone reunion index]",
            MEMORY_TABLE + "| 176 | Meta | [Row 68 → Row 156 Born–Oppenheimer meta prelude capstone reunion index]",
        )
        memory = memory.replace(
            "### Row 157 baby picture (Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion) {#row-157-baby-picture-row68-row137-kohn-sham-meta-prelude-capstone-reunion}",
            MEMORY_BABY + "### Row 157 baby picture (Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion) {#row-157-baby-picture-row68-row137-kohn-sham-meta-prelude-capstone-reunion}",
            1,
        )
        if ROW176_BABY_OLD in memory:
            memory = memory.replace(ROW176_BABY_OLD, ROW176_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 177")


if __name__ == "__main__":
    main()
