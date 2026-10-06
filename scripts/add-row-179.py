#!/usr/bin/env python3
"""Add row 179 meta-stitch (Row 68 → Row 159 ↔ Row 59 Handshake 3 meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def t159_to_179(text: str) -> str:
    """Transform row-159 capstone-path meta copy to row 179 (159→179, 139→159 inner, 178 gate)."""
    repl = [
        ("Row 68 → Row 139 Row 68 → Row 59", "Row 68 → Row 159 Row 68 → Row 59"),
        (
            "row68-row139-handshake3-meta-prelude-capstone-reunion-index-row-159",
            "TEMP_ROW179_EXP_INDEX",
        ),
        (
            "row-159-baby-picture-row68-row139-handshake3-meta-prelude-capstone-reunion",
            "row-179-baby-picture-row68-row159-handshake3-meta-prelude-capstone-reunion",
        ),
        ("skill-navigation-row-159", "TEMP_SKILL_NAV_159"),
        ("prologue-preview-row-159", "prologue-preview-row-179"),
        ("row-159-closing-stitch", "row-179-closing-stitch"),
        ("row-159-closing-loop", "row-179-closing-loop"),
        ("Row 159 three-way audit", "Row 179 three-way audit"),
        (
            "[row 158](preface.md#skill-navigation-row-158) or [row 139](TEMP_SKILL_NAV_159)",
            "[row 178](preface.md#skill-navigation-row-178) or [row 159](TEMP_SKILL_NAV_159)",
        ),
        (
            "[row 158](preface.md#skill-navigation-row-158) or [Row 68 → Row 119 Handshake 3 meta capstone reunion index (row 139)](appendix/sources.md#row68-row99-handshake3-meta-capstone-reunion-index-row-119)",
            "[row 178](preface.md#skill-navigation-row-178) or [Row 68 → Row 159 Handshake 3 meta prelude capstone reunion index (row 179)](appendix/sources.md#row68-row159-handshake3-meta-prelude-capstone-reunion-index-row-179)",
        ),
        (
            "[row 158](preface.md#skill-navigation-row-158) or [Row 68 → Row 139 Handshake 3 meta prelude capstone reunion index (row 159)](appendix/sources.md#row68-row139-handshake3-meta-prelude-capstone-reunion-index-row-159)",
            "[row 178](preface.md#skill-navigation-row-178) or [Row 68 → Row 159 Handshake 3 meta prelude capstone reunion index (row 179)](appendix/sources.md#row68-row159-handshake3-meta-prelude-capstone-reunion-index-row-179)",
        ),
        (
            "verified DFT workflows meta prelude capstone closure (row 158)",
            "verified DFT workflows meta prelude capstone closure (row 178)",
        ),
        (
            "before row 160 Handshake 3 meta prelude capstone reunion opens on the full capstone path",
            "before row 180 Handshake 3 meta prelude capstone reunion opens on the full capstone path",
        ),
        (
            "before row 160 Handshake 3 meta prelude capstone reunion on the full capstone path",
            "before row 180 Handshake 3 meta prelude capstone reunion on the full capstone path",
        ),
        (
            "before row 140 Handshake 3 meta prelude capstone opens on the full capstone path",
            "before row 180 Handshake 3 meta prelude capstone opens on the full capstone path",
        ),
    ]
    out = text
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW179_EXP_INDEX",
        "row68-row159-handshake3-meta-prelude-capstone-reunion-index-row-179",
    )
    out = out.replace("TEMP_SKILL_NAV_159", "skill-navigation-row-159")
    out = out.replace("row 159", "row 179")
    out = out.replace("Row 159", "Row 179")
    out = out.replace("skill-navigation-row-159", "skill-navigation-row-179")
    out = out.replace("[row 179](preface.md#skill-navigation-row-178)", "[row 178](preface.md#skill-navigation-row-178)")
    out = out.replace("[row 179](preface.md#skill-navigation-row-179)", "[row 179](preface.md#skill-navigation-row-179)")
    out = out.replace("[row 179](preface.md#skill-navigation-row-159)", "[row 159](preface.md#skill-navigation-row-159)")
    out = out.replace("[row 159](preface.md#skill-navigation-row-179)", "[row 159](preface.md#skill-navigation-row-159)")
    out = out.replace("when row 158 closed but row 59", "when row 178 closed but row 59")
    out = out.replace("[preface row 159](../preface.md#skill-navigation-row-179)", "[preface row 159](../preface.md#skill-navigation-row-159)")
    out = out.replace("row 1597", "row 179")
    out = out.replace("row 1598", "row 180")
    out = out.replace("row 179 or row 179", "row 178 or row 159")
    out = out.replace("When row 179 closed", "When row 178 closed")
    out = out.replace("after row 179 alone", "after row 178 alone")
    out = out.replace("Recite [preface row 179]", "Recite [preface row 178]")
    out = out.replace("row 179 or row 159 recited", "row 178 or row 159 recited")
    out = out.replace("When row 158 closed — DFT", "When row 178 closed — DFT")
    out = out.replace("row 157 or row 138 recited", "row 177 or row 158 recited")
    out = out.replace("row 158 or row 139 recited", "row 178 or row 159 recited")
    out = out.replace("when row 158 closed DFT", "when row 178 closed DFT")
    out = out.replace("after row 158 alone", "after row 178 alone")
    out = out.replace("from row 179's", "from row 178's")
    out = out.replace("row 158's calculation", "row 178's calculation")
    out = out.replace("row 158 and row 59", "row 178 and row 59")
    out = out.replace("after row 158 on", "after row 178 on")
    out = out.replace("Recite [preface row 158]", "Recite [preface row 178]")
    out = out.replace("row 139", "row 159")
    out = out.replace("Row 139", "Row 159")
    out = out.replace("row 119", "row 139")
    out = out.replace("Row 119", "Row 139")
    out = out.replace(
        "row68-row99-handshake3-meta-capstone-reunion-index-row-119",
        "row68-row119-handshake3-meta-capstone-reunion-index-row-139",
    )
    out = out.replace(
        "row68-row139-handshake3-meta-prelude-capstone-reunion-index-row-159",
        "row68-row159-handshake3-meta-prelude-capstone-reunion-index-row-179",
    )
    out = out.replace(
        "[row 158](preface.md#skill-navigation-row-158) or [row 159]",
        "[row 178](preface.md#skill-navigation-row-178) or [row 159]",
    )
    out = out.replace("row 158", "row 178")
    out = out.replace("Row 158", "Row 178")
    out = out.replace("[row 178](preface.md#skill-navigation-row-178)", "[row 178](preface.md#skill-navigation-row-178)")
    out = out.replace("[row 178](preface.md#skill-navigation-row-159)", "[row 159](preface.md#skill-navigation-row-159)")
    out = out.replace(
        "Row 68 → Row 179 Handshake 3 meta prelude capstone reunion index",
        "Row 68 → Row 159 Handshake 3 meta prelude capstone reunion index",
    )
    return out


def extract_preface_row159(preface: str) -> str:
    start = preface.index("### Row 159 skill checkpoint")
    end = preface.index("\n\n### Row 160 skill checkpoint")
    return preface[start:end]


ROW179_PREFACE = t159_to_179(extract_preface_row159((ROOT / "writings/preface/chapters/preface.md").read_text())) + "\n\n"

_prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
_row159_compass = next(
    line for line in _prologue.splitlines() if "(row 159) |" in line and "Row 68 → Row 139" in line
)
PROLOGUE_COMPASS = t159_to_179(_row159_compass) + "\n"

_row159_stitch_body = (
    _prologue.split("**Row 159 closing stitch")[1].split("**Row 178 closing stitch")[0].lstrip().split("\n\n")[0]
)
PROLOGUE_STITCH = t159_to_179(
    "**Row 159 closing stitch (Row 68 → Row 139 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion).** {#row-159-closing-stitch} "
    + _row159_stitch_body.split(".** {#row-159-closing-stitch} ", 1)[-1]
) + "\n\n"

_row159_preview = next(line for line in _prologue.splitlines() if 'id="prologue-preview-row-159"' in line)
PROLOGUE_PREVIEW = t159_to_179(_row159_preview) + "\n"

_epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
EPILOGUE_LOOP = t159_to_179(
    "### Row 159 closing loop"
    + _epilogue.split("### Row 159 closing loop")[1].split("### Row 160 closing loop")[0]
)

_src159_header = "## Row 68 → Row 139 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 159)"
_next159_header = "## Row 68 → Row 120 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 140)"
_sources_blob = (ROOT / "writings/appendix/chapters/sources.md").read_text()
_src159_body = _sources_blob.split(_src159_header, 1)[1].split(_next159_header, 1)[0]
SOURCES_INDEX = (
    "## Row 68 → Row 159 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 179)"
    + t159_to_179(_src159_body)
)

_row159_table = next(
    line for line in _sources_blob.splitlines() if line.startswith("| 159 | Row 68 → Row 139")
)
SOURCES_TABLE = t159_to_179(_row159_table).replace("| 159 | Row 68 → Row 159", "| 179 | Row 68 → Row 159", 1) + "\n"

_row159_mem_table = next(
    line for line in (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text().splitlines()
    if line.startswith("| 159 | Meta |")
)
MEMORY_TABLE = t159_to_179(_row159_mem_table).replace("| 159 | Meta |", "| 179 | Meta |", 1) + "\n"

_baby_anchor = "### Row 159 baby picture {#row-159-baby-picture-row68-row139-handshake3-meta-prelude-capstone-reunion}"
MEMORY_BABY = t159_to_179(
    (ROOT / "writings/appendix/chapters/memory-sheet.md")
    .read_text()
    .split(_baby_anchor)[1]
    .split("### Row 160 baby picture")[0]
)
MEMORY_BABY = (
    "### Row 179 baby picture (Row 68 → Row 159 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion)"
    + MEMORY_BABY.split(")", 1)[1]
    if ")" in MEMORY_BABY
    else "### Row 179 baby picture" + MEMORY_BABY
)

ROW178_BABY_OLD = (
    "row 178 when **IX.2 Bridge and Row 68 → Row 58 meta must read on the same wire before row 179 Handshake 3 meta prelude capstone opens on the full capstone path**"
)
ROW178_BABY_NEW = (
    "row 178 when **IX.2 Bridge and Row 68 → Row 58 meta must read on the same wire before row 179 Handshake 3 meta prelude capstone reunion opens on the full capstone path**"
)

ROW178_TAIL_OLD = (
    "Read the [memory sheet row 178 baby picture](appendix/memory-sheet.md#row-178-baby-picture-row68-row158-dft-workflows-meta-prelude-capstone-reunion) when opening [row 159](preface.md#skill-navigation-row-159) before row 59 closes on the full capstone path; read the [epilogue row 178 closing loop](epilogue/multiscale.md#row-178-closing-loop) when the competence loop closes. When row 178 is complete, proceed to [row 159](preface.md#skill-navigation-row-159) when `foundation_export.yaml` exists but Handshake 3 meta prelude capstone still lags after verified DFT workflows meta prelude capstone on the full capstone path, to [row 139](preface.md#skill-navigation-row-139) for the Row 68 ↔ Row 59 Handshake 3 meta audit on the opening-hinge capstone path alone,"
)
ROW178_TAIL_NEW = (
    "Read the [memory sheet row 178 baby picture](appendix/memory-sheet.md#row-178-baby-picture-row68-row158-dft-workflows-meta-prelude-capstone-reunion) when opening [row 179](preface.md#skill-navigation-row-179) before row 59 closes on the full capstone path; read the [epilogue row 178 closing loop](epilogue/multiscale.md#row-178-closing-loop) when the competence loop closes. When row 178 is complete, proceed to [row 179](preface.md#skill-navigation-row-179) when `foundation_export.yaml` exists but Handshake 3 meta prelude capstone still lags after verified DFT workflows meta prelude capstone on the full capstone path, to [row 159](preface.md#skill-navigation-row-159) for the Row 68 ↔ Row 59 Handshake 3 meta audit on the opening-hinge capstone path alone, to [row 139](preface.md#skill-navigation-row-139) for the Row 68 ↔ Row 59 Handshake 3 meta audit on the opening-hinge capstone path alone,"
)


def main():
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "skill-navigation-row-179" in preface and preface.index("skill-navigation-row-179") < preface.index(copper):
        print("preface: row 179 already present")
    elif "skill-navigation-row-179" in preface:
        raise SystemExit("preface row 179 exists but not at copper wire insert point")
    else:
        if "skill-navigation-row-178" not in preface:
            raise SystemExit("preface row 178 must exist before row 179")
        if ROW178_TAIL_OLD not in preface:
            raise SystemExit("preface row 178 tail not found")
        preface = preface.replace(ROW178_TAIL_OLD, ROW178_TAIL_NEW)
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + ROW179_PREFACE + copper)
        preface_path.write_text(preface)
        print("preface: added row 179")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-179" not in prologue:
        needle = "| Row 68 → Row 158 Row 68 → Row 58 DFT workflows meta prelude capstone reunion (row 178) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 178 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + PROLOGUE_COMPASS + prologue[line_end + 1 :]
        prologue = prologue.replace(
            "**Row 178 closing stitch",
            PROLOGUE_STITCH + "**Row 178 closing stitch",
        )
        prologue = prologue.replace(
            '| <span id="prologue-preview-row-178"></span>Row 178 preview',
            PROLOGUE_PREVIEW + '| <span id="prologue-preview-row-178"></span>Row 178 preview',
        )
        prologue_path.write_text(prologue)
        print("prologue: added row 179")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "row-179-closing-loop" not in epilogue:
        old_proceed = (
            "Proceed to [row 159](#row-159-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 178 on the full capstone path, to [row 139](#row-139-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 158 on the opening-hinge capstone path alone,"
        )
        new_proceed = (
            "Proceed to [row 179](#row-179-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 178 on the full capstone path, to [row 159](#row-159-closing-loop) when Handshake 3 meta prelude capstone still lags after verified DFT workflows meta prelude capstone on the opening-hinge capstone path alone, to [row 139](#row-139-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 158 on the opening-hinge capstone path alone,"
        )
        if old_proceed not in epilogue:
            raise SystemExit("epilogue row 178 end marker not found")
        epilogue = epilogue.replace(old_proceed, new_proceed, 1)
        epilogue = epilogue.replace(
            "before row 179 Handshake 3 meta prelude capstone reunion on the full capstone path (then row 140 on the capstone path).",
            "before row 180 Handshake 3 meta prelude capstone reunion on the full capstone path (then row 160 on the capstone path).",
            1,
        )
        marker = "### Row 131 closing loop (Row 68 → Row 111 Row 68 → Row 51 homogenization meta prelude capstone reunion)"
        if marker not in epilogue:
            raise SystemExit("epilogue row 178 insert anchor not found")
        epilogue = epilogue.replace(marker, EPILOGUE_LOOP + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 179")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row159-handshake3-meta-prelude-capstone-reunion-index-row-179" not in sources:
        sources = sources.replace(
            "| 159 | Row 68 → Row 139 Row 68 → Row 59 Handshake 3 meta prelude capstone",
            SOURCES_TABLE + "| 159 | Row 68 → Row 139 Row 68 → Row 59 Handshake 3 meta prelude capstone",
        )
        sources = sources.replace(
            _src159_header,
            SOURCES_INDEX + _src159_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 179")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-179-baby-picture-row68-row159" not in memory:
        memory = memory.replace(
            "| 178 | Meta | [Row 68 → Row 158 DFT workflows meta prelude capstone reunion index]",
            MEMORY_TABLE + "| 178 | Meta | [Row 68 → Row 158 DFT workflows meta prelude capstone reunion index]",
        )
        memory = memory.replace(
            _baby_anchor,
            MEMORY_BABY + _baby_anchor,
            1,
        )
        if ROW178_BABY_OLD in memory:
            memory = memory.replace(ROW178_BABY_OLD, ROW178_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 179")


if __name__ == "__main__":
    main()
