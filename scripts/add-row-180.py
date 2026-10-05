#!/usr/bin/env python3
"""Add row 180 meta-stitch (Row 68 → Row 160 ↔ Row 60 Handshake 3 meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def t160_to_180(text: str) -> str:
    """Transform row-160 capstone-path meta copy to row 180 (160→180, 140→160 inner, 179 gate)."""
    repl = [
        ("Row 68 → Row 140 Row 68 → Row 60", "Row 68 → Row 160 Row 68 → Row 60"),
        (
            "row68-row140-handshake3-meta-prelude-capstone-reunion-index-row-160",
            "TEMP_ROW180_EXP_INDEX",
        ),
        (
            "row-160-baby-picture-row68-row140-handshake3-meta-prelude-capstone-reunion",
            "row-180-baby-picture-row68-row160-handshake3-meta-prelude-capstone-reunion",
        ),
        ("skill-navigation-row-160", "TEMP_SKILL_NAV_160"),
        ("prologue-preview-row-160", "prologue-preview-row-180"),
        ("row-160-closing-stitch", "row-180-closing-stitch"),
        ("row-160-closing-loop", "row-180-closing-loop"),
        ("Row 160 three-way audit", "Row 180 three-way audit"),
        (
            "[row 159](preface.md#skill-navigation-row-159) or [row 140](TEMP_SKILL_NAV_160)",
            "[row 179](preface.md#skill-navigation-row-179) or [row 160](TEMP_SKILL_NAV_160)",
        ),
        (
            "[row 159](preface.md#skill-navigation-row-159) or [Row 68 → Row 140 Handshake 3 meta prelude reunion index (row 140)](appendix/sources.md#row68-row100-handshake3-meta-prelude-capstone-reunion-index-row-120)",
            "[row 179](preface.md#skill-navigation-row-179) or [Row 68 → Row 160 Handshake 3 meta prelude capstone reunion index (row 180)](appendix/sources.md#row68-row160-handshake3-meta-prelude-capstone-reunion-index-row-180)",
        ),
        (
            "[row 159](preface.md#skill-navigation-row-159) or [Row 68 → Row 140 Handshake 3 meta prelude capstone reunion index (row 160)](appendix/sources.md#row68-row140-handshake3-meta-prelude-capstone-reunion-index-row-160)",
            "[row 179](preface.md#skill-navigation-row-179) or [Row 68 → Row 160 Handshake 3 meta prelude capstone reunion index (row 180)](appendix/sources.md#row68-row160-handshake3-meta-prelude-capstone-reunion-index-row-180)",
        ),
        (
            "verified Handshake 3 meta prelude capstone closure (row 159)",
            "verified Handshake 3 meta prelude capstone closure (row 179)",
        ),
        (
            "before row 161 Handshake 4a meta prelude capstone opens on the full capstone path",
            "before row 181 Handshake 4a meta prelude capstone opens on the full capstone path",
        ),
        (
            "before row 161 Handshake 4a meta prelude capstone reunion on the full capstone path",
            "before row 181 Handshake 4a meta prelude capstone reunion on the full capstone path",
        ),
        (
            "before row 141 Handshake 4a meta prelude capstone opens on the full capstone path",
            "before row 181 Handshake 4a meta prelude capstone opens on the full capstone path",
        ),
    ]
    out = text
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW180_EXP_INDEX",
        "row68-row160-handshake3-meta-prelude-capstone-reunion-index-row-180",
    )
    out = out.replace("TEMP_SKILL_NAV_160", "skill-navigation-row-160")
    out = out.replace("Row 68 → Row 160 Row 68 → Row 60", "TEMP_ROW160_TITLE")
    out = out.replace("row 160", "row 180")
    out = out.replace("Row 160", "Row 180")
    out = out.replace("TEMP_ROW160_TITLE", "Row 68 → Row 160 Row 68 → Row 60")
    out = out.replace("skill-navigation-row-160", "skill-navigation-row-180")
    out = out.replace("[row 180](preface.md#skill-navigation-row-179)", "[row 179](preface.md#skill-navigation-row-179)")
    out = out.replace("[row 180](preface.md#skill-navigation-row-180)", "[row 180](preface.md#skill-navigation-row-180)")
    out = out.replace("[row 180](preface.md#skill-navigation-row-160)", "[row 160](preface.md#skill-navigation-row-160)")
    out = out.replace("[row 160](preface.md#skill-navigation-row-180)", "[row 160](preface.md#skill-navigation-row-160)")
    out = out.replace("when row 159 closed but row 60", "when row 179 closed but row 60")
    out = out.replace("[preface row 160](../preface.md#skill-navigation-row-180)", "[preface row 160](../preface.md#skill-navigation-row-160)")
    out = out.replace("row 1607", "row 179")
    out = out.replace("row 1608", "row 181")
    out = out.replace("row 180 or row 180", "row 179 or row 160")
    out = out.replace("When row 180 closed", "When row 179 closed")
    out = out.replace("after row 180 alone", "after row 179 alone")
    out = out.replace("Recite [preface row 180]", "Recite [preface row 179]")
    out = out.replace("row 180 or row 160 recited", "row 179 or row 160 recited")
    out = out.replace("When row 159 closed — Handshake", "When row 179 closed — Handshake")
    out = out.replace("row 158 or row 139 recited", "row 178 or row 159 recited")
    out = out.replace("row 159 or row 140 recited", "row 179 or row 160 recited")
    out = out.replace("when row 159 closed Handshake", "when row 179 closed Handshake")
    out = out.replace("after row 159 alone", "after row 179 alone")
    out = out.replace("from row 180's", "from row 179's")
    out = out.replace("row 159's foundation", "row 179's foundation")
    out = out.replace("row 159's quasiharmonic", "row 179's quasiharmonic")
    out = out.replace("row 159 and row 60", "row 179 and row 60")
    out = out.replace("Recite [preface row 159]", "Recite [preface row 179]")
    out = out.replace("row 140", "row 160")
    out = out.replace("Row 140", "Row 160")
    out = out.replace("row 120", "row 140")
    out = out.replace("Row 120", "Row 140")
    out = out.replace(
        "row68-row100-handshake3-meta-prelude-capstone-reunion-index-row-120",
        "row68-row120-handshake3-meta-prelude-capstone-reunion-index-row-140",
    )
    out = out.replace(
        "row68-row140-handshake3-meta-prelude-capstone-reunion-index-row-160",
        "row68-row160-handshake3-meta-prelude-capstone-reunion-index-row-180",
    )
    out = out.replace(
        "[row 159](preface.md#skill-navigation-row-159) or [row 160]",
        "[row 179](preface.md#skill-navigation-row-179) or [row 160]",
    )
    out = out.replace("row 159", "row 179")
    out = out.replace("Row 159", "Row 179")
    out = out.replace("[row 179](preface.md#skill-navigation-row-179)", "[row 179](preface.md#skill-navigation-row-179)")
    out = out.replace("[row 179](preface.md#skill-navigation-row-160)", "[row 160](preface.md#skill-navigation-row-160)")
    out = out.replace(
        "Row 68 → Row 180 Handshake 3 meta prelude capstone reunion index",
        "Row 68 → Row 160 Handshake 3 meta prelude capstone reunion index",
    )
    out = out.replace(
        "[row 160](preface.md#skill-navigation-row-140)",
        "[row 160](preface.md#skill-navigation-row-160)",
    )
    return out


def extract_preface_row160(preface: str) -> str:
    start = preface.index("### Row 160 skill checkpoint")
    end = preface.index("\n\n### Row 161 skill checkpoint")
    return preface[start:end]


ROW180_PREFACE = t160_to_180(extract_preface_row160((ROOT / "writings/preface/chapters/preface.md").read_text())) + "\n\n"

_prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
_row160_compass = next(
    line for line in _prologue.splitlines() if "(row 160) |" in line and "Row 68 → Row 140" in line
)
PROLOGUE_COMPASS = t160_to_180(_row160_compass) + "\n"

_row160_stitch_body = (
    _prologue.split("**Row 160 closing stitch")[1].split("**Row 159 closing stitch")[0].lstrip().split("\n\n")[0]
)
PROLOGUE_STITCH = t160_to_180(
    "**Row 160 closing stitch (Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion).** {#row-160-closing-stitch} "
    + _row160_stitch_body.split(".** {#row-160-closing-stitch} ", 1)[-1]
) + "\n\n"

_row160_preview = next(line for line in _prologue.splitlines() if 'id="prologue-preview-row-160"' in line)
PROLOGUE_PREVIEW = t160_to_180(_row160_preview) + "\n"

_epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
EPILOGUE_LOOP = t160_to_180(
    "### Row 160 closing loop"
    + _epilogue.split("### Row 160 closing loop")[1].split("### Row 161 closing loop")[0]
)

_src160_header = "## Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 160)"
_next160_header = "## Row 68 → Row 121 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 141)"
_sources_blob = (ROOT / "writings/appendix/chapters/sources.md").read_text()
_src160_body = _sources_blob.split(_src160_header, 1)[1].split(_next160_header, 1)[0]
SOURCES_INDEX = (
    "## Row 68 → Row 160 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 180)"
    + t160_to_180(_src160_body)
)

_row160_table = next(
    line for line in _sources_blob.splitlines() if line.startswith("| 160 | Row 68 → Row 140")
)
SOURCES_TABLE = (
    t160_to_180(_row160_table).replace("| 160 | Row 68 → Row 140", "| 180 | Row 68 → Row 160", 1) + "\n"
)

_row160_mem_table = next(
    line for line in (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text().splitlines()
    if line.startswith("| 160 | Meta |")
)
MEMORY_TABLE = t160_to_180(_row160_mem_table).replace("| 160 | Meta |", "| 180 | Meta |", 1) + "\n"

_baby_anchor = "### Row 160 baby picture {#row-160-baby-picture-row68-row140-handshake3-meta-prelude-capstone-reunion}"
MEMORY_BABY = t160_to_180(
    (ROOT / "writings/appendix/chapters/memory-sheet.md")
    .read_text()
    .split(_baby_anchor)[1]
    .split("### Row 161 baby picture")[0]
)
MEMORY_BABY = (
    "### Row 180 baby picture (Row 68 → Row 160 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion)"
    + MEMORY_BABY.split(")", 1)[1]
    if ")" in MEMORY_BABY
    else "### Row 180 baby picture" + MEMORY_BABY
)

ROW179_BABY_OLD = (
    "row 179 when **foundation export manifest and IX.3 → Handshake 3 meta must read on the same wire before row 180 Handshake 3 meta prelude capstone opens on the full capstone path**"
)
ROW179_BABY_NEW = (
    "row 179 when **foundation export manifest and IX.3 → Handshake 3 meta must read on the same wire before row 180 Handshake 3 meta prelude capstone reunion opens on the full capstone path**"
)

ROW179_TAIL_OLD = (
    "Read the [memory sheet row 179 baby picture](appendix/memory-sheet.md#row-179-baby-picture-row68-row159-handshake3-meta-prelude-capstone-reunion) when opening [row 160](preface.md#skill-navigation-row-160) before row 60 closes on the full capstone path; read the [epilogue row 179 closing loop](epilogue/multiscale.md#row-179-closing-loop) when the competence loop closes. When row 179 is complete, proceed to [row 160](preface.md#skill-navigation-row-160) when load cell parses at \\(T_w\\) but Handshake 3 still feels disconnected from Parts III–VI after verified Handshake 3 meta prelude capstone on the full capstone path, to [row 140](preface.md#skill-navigation-row-140) for the Row 68 ↔ Row 60 Handshake 3 meta audit on the opening-hinge capstone path alone,"
)
ROW179_TAIL_NEW = (
    "Read the [memory sheet row 179 baby picture](appendix/memory-sheet.md#row-179-baby-picture-row68-row159-handshake3-meta-prelude-capstone-reunion) when opening [row 180](preface.md#skill-navigation-row-180) before row 60 closes on the full capstone path; read the [epilogue row 179 closing loop](epilogue/multiscale.md#row-179-closing-loop) when the competence loop closes. When row 179 is complete, proceed to [row 180](preface.md#skill-navigation-row-180) when load cell parses at \\(T_w\\) but Handshake 3 still feels disconnected from Parts III–VI after verified Handshake 3 meta prelude capstone on the full capstone path, to [row 160](preface.md#skill-navigation-row-160) for the Row 68 ↔ Row 60 Handshake 3 meta audit on the opening-hinge capstone path alone, to [row 140](preface.md#skill-navigation-row-140) for the Row 68 ↔ Row 60 Handshake 3 meta audit on the opening-hinge capstone path alone,"
)


def main():
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "skill-navigation-row-180" in preface and preface.index("skill-navigation-row-180") < preface.index(copper):
        print("preface: row 180 already present")
    elif "skill-navigation-row-180" in preface:
        raise SystemExit("preface row 180 exists but not at copper wire insert point")
    else:
        if "skill-navigation-row-179" not in preface:
            raise SystemExit("preface row 179 must exist before row 180")
        if ROW179_TAIL_OLD not in preface:
            raise SystemExit("preface row 179 tail not found")
        preface = preface.replace(ROW179_TAIL_OLD, ROW179_TAIL_NEW)
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + ROW180_PREFACE + copper)
        preface_path.write_text(preface)
        print("preface: added row 180")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-180" not in prologue:
        needle = "| Row 68 → Row 159 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion (row 179) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 179 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + PROLOGUE_COMPASS + prologue[line_end + 1 :]
        prologue = prologue.replace(
            "**Row 179 closing stitch",
            PROLOGUE_STITCH + "**Row 179 closing stitch",
        )
        prologue = prologue.replace(
            '| <span id="prologue-preview-row-179"></span>Row 179 preview',
            PROLOGUE_PREVIEW + '| <span id="prologue-preview-row-179"></span>Row 179 preview',
        )
        prologue_path.write_text(prologue)
        print("prologue: added row 180")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "### Row 180 closing loop" not in epilogue:
        old_proceed = (
            "Proceed to [row 180](#row-180-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 179 on the full capstone path, when load cell parses at \\(T_w\\) after verified Handshake 3 meta prelude capstone but Handshake 3 still feels disconnected from Parts III–VI on the full capstone path, to [row 140](#row-140-closing-loop) for the Row 68 ↔ Row 60 Handshake 3 meta audit on the opening-hinge capstone path alone,"
        )
        new_proceed = (
            "Proceed to [row 180](#row-180-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 179 on the full capstone path, when load cell parses at \\(T_w\\) after verified Handshake 3 meta prelude capstone but Handshake 3 still feels disconnected from Parts III–VI on the full capstone path, to [row 160](#row-160-closing-loop) for the Row 68 ↔ Row 60 Handshake 3 meta audit on the opening-hinge capstone path alone, to [row 140](#row-140-closing-loop) for the Row 68 ↔ Row 60 Handshake 3 meta audit on the opening-hinge capstone path alone,"
        )
        if old_proceed not in epilogue:
            raise SystemExit("epilogue row 179 end marker not found")
        epilogue = epilogue.replace(old_proceed, new_proceed, 1)
        epilogue = epilogue.replace(
            "before row 180 Handshake 3 meta prelude capstone reunion on the full capstone path (then row 160 on the capstone path).",
            "before row 181 Handshake 4a meta prelude capstone reunion on the full capstone path (then row 161 on the capstone path).",
            1,
        )
        marker = "### Row 131 closing loop (Row 68 → Row 111 Row 68 → Row 51 homogenization meta prelude capstone reunion)"
        if marker not in epilogue:
            raise SystemExit("epilogue row 179 insert anchor not found")
        epilogue = epilogue.replace(marker, EPILOGUE_LOOP + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 180")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row160-handshake3-meta-prelude-capstone-reunion-index-row-180" not in sources:
        sources = sources.replace(
            "| 160 | Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone",
            SOURCES_TABLE + "| 160 | Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone",
        )
        sources = sources.replace(
            _src160_header,
            SOURCES_INDEX + _src160_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 180")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-180-baby-picture-row68-row160" not in memory:
        memory = memory.replace(
            "| 179 | Meta | [Row 68 → Row 159 Handshake 3 meta prelude capstone reunion index]",
            MEMORY_TABLE + "| 179 | Meta | [Row 68 → Row 159 Handshake 3 meta prelude capstone reunion index]",
        )
        memory = memory.replace(
            _baby_anchor,
            MEMORY_BABY + _baby_anchor,
            1,
        )
        if ROW179_BABY_OLD in memory:
            memory = memory.replace(ROW179_BABY_OLD, ROW179_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 180")


if __name__ == "__main__":
    main()
