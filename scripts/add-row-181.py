#!/usr/bin/env python3
"""Add row 181 meta-stitch (Row 68 → Row 161 ↔ Row 61 Handshake 4a meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def t161_to_181(text: str) -> str:
    """Transform row-161 capstone-path meta copy to row 181 (161→181, 141→161 inner, 180 gate)."""
    repl = [
        ("Row 68 → Row 141 Row 68 → Row 61", "Row 68 → Row 161 Row 68 → Row 61"),
        (
            "row68-row141-handshake4a-meta-prelude-capstone-reunion-index-row-161",
            "TEMP_ROW181_EXP_INDEX",
        ),
        (
            "row-161-baby-picture-row68-row141-handshake4a-meta-prelude-capstone-reunion",
            "row-181-baby-picture-row68-row161-handshake4a-meta-prelude-capstone-reunion",
        ),
        ("skill-navigation-row-161", "TEMP_SKILL_NAV_161"),
        ("prologue-preview-row-161", "prologue-preview-row-181"),
        ("row-161-closing-stitch", "row-181-closing-stitch"),
        ("row-161-closing-loop", "row-181-closing-loop"),
        ("Row 161 three-way audit", "Row 181 three-way audit"),
        (
            "[row 160](preface.md#skill-navigation-row-160) or [row 141](TEMP_SKILL_NAV_161)",
            "[row 180](preface.md#skill-navigation-row-180) or [row 161](TEMP_SKILL_NAV_161)",
        ),
        (
            "[row 160](preface.md#skill-navigation-row-160) or [Row 68 → Row 141 Handshake 4a meta prelude reunion index (row 141)](appendix/sources.md#row68-row121-handshake4a-meta-prelude-capstone-reunion-index-row-141)",
            "[row 180](preface.md#skill-navigation-row-180) or [Row 68 → Row 161 Handshake 4a meta prelude capstone reunion index (row 181)](appendix/sources.md#row68-row161-handshake4a-meta-prelude-capstone-reunion-index-row-181)",
        ),
        (
            "[row 160](preface.md#skill-navigation-row-160) or [Row 68 → Row 141 Handshake 4a meta prelude capstone reunion index (row 161)](appendix/sources.md#row68-row141-handshake4a-meta-prelude-capstone-reunion-index-row-161)",
            "[row 180](preface.md#skill-navigation-row-180) or [Row 68 → Row 161 Handshake 4a meta prelude capstone reunion index (row 181)](appendix/sources.md#row68-row161-handshake4a-meta-prelude-capstone-reunion-index-row-181)",
        ),
        (
            "verified Handshake 4a meta prelude capstone closure (row 160)",
            "verified Handshake 4a meta prelude capstone closure (row 180)",
        ),
        (
            "before row 162 Handshake 4b meta prelude capstone opens on the full capstone path",
            "before row 182 Handshake 4b meta prelude capstone opens on the full capstone path",
        ),
        (
            "before row 162 Handshake 4b meta prelude capstone reunion on the full capstone path",
            "before row 182 Handshake 4b meta prelude capstone reunion on the full capstone path",
        ),
        (
            "before row 142 Handshake 4b meta prelude capstone opens on the full capstone path",
            "before row 182 Handshake 4b meta prelude capstone opens on the full capstone path",
        ),
    ]
    out = text
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW181_EXP_INDEX",
        "row68-row161-handshake4a-meta-prelude-capstone-reunion-index-row-181",
    )
    out = out.replace("TEMP_SKILL_NAV_161", "skill-navigation-row-161")
    out = out.replace("Row 68 → Row 161 Row 68 → Row 61", "TEMP_ROW161_TITLE")
    out = out.replace("row 161", "row 181")
    out = out.replace("Row 161", "Row 181")
    out = out.replace("TEMP_ROW161_TITLE", "Row 68 → Row 161 Row 68 → Row 61")
    out = out.replace("skill-navigation-row-161", "skill-navigation-row-181")
    out = out.replace("[row 181](preface.md#skill-navigation-row-180)", "[row 180](preface.md#skill-navigation-row-180)")
    out = out.replace("[row 181](preface.md#skill-navigation-row-181)", "[row 181](preface.md#skill-navigation-row-181)")
    out = out.replace("[row 181](preface.md#skill-navigation-row-161)", "[row 161](preface.md#skill-navigation-row-161)")
    out = out.replace("[row 161](preface.md#skill-navigation-row-181)", "[row 161](preface.md#skill-navigation-row-161)")
    out = out.replace("when row 160 closed but row 61", "when row 180 closed but row 61")
    out = out.replace("[preface row 181](../preface.md#skill-navigation-row-181)", "[preface row 181](../preface.md#skill-navigation-row-181)")
    out = out.replace("[preface row 161](../preface.md#skill-navigation-row-181)", "[preface row 161](../preface.md#skill-navigation-row-161)")
    out = out.replace("row 1617", "row 180")
    out = out.replace("row 1618", "row 182")
    out = out.replace("row 181 or row 181", "row 180 or row 161")
    out = out.replace("When row 181 closed", "When row 180 closed")
    out = out.replace("after row 181 alone", "after row 180 alone")
    out = out.replace("Recite [preface row 181]", "Recite [preface row 180]")
    out = out.replace("row 181 or row 161 recited", "row 180 or row 161 recited")
    out = out.replace("When row 160 closed — Handshake 4a", "When row 180 closed — Handshake 4a")
    out = out.replace("row 160 or row 141 recited", "row 180 or row 161 recited")
    out = out.replace("when row 160 closed Handshake 4a", "when row 180 closed Handshake 4a")
    out = out.replace("after row 160 alone", "after row 180 alone")
    out = out.replace("from row 181's", "from row 180's")
    out = out.replace("row 160's epilogue rate", "row 180's epilogue rate")
    out = out.replace("row 160 and row 61", "row 180 and row 61")
    out = out.replace("Recite [preface row 160]", "Recite [preface row 180]")
    out = out.replace("row 141", "row 161")
    out = out.replace("Row 141", "Row 161")
    out = out.replace("row 121", "row 141")
    out = out.replace("Row 121", "Row 141")
    out = out.replace(
        "row68-row121-handshake4a-meta-prelude-capstone-reunion-index-row-141",
        "row68-row141-handshake4a-meta-prelude-capstone-reunion-index-row-161",
    )
    out = out.replace(
        "row68-row141-handshake4a-meta-prelude-capstone-reunion-index-row-161",
        "row68-row161-handshake4a-meta-prelude-capstone-reunion-index-row-181",
    )
    out = out.replace(
        "[row 160](preface.md#skill-navigation-row-160) or [row 161]",
        "[row 180](preface.md#skill-navigation-row-180) or [row 161]",
    )
    out = out.replace("row 160", "row 180")
    out = out.replace("Row 160", "Row 180")
    out = out.replace(
        "Row 68 → Row 181 Handshake 4a meta prelude capstone reunion index",
        "Row 68 → Row 161 Handshake 4a meta prelude capstone reunion index",
    )
    out = out.replace(
        "[row 161](preface.md#skill-navigation-row-141)",
        "[row 161](preface.md#skill-navigation-row-161)",
    )
    return out


def extract_preface_row161(preface: str) -> str:
    start = preface.index("### Row 161 skill checkpoint")
    end = preface.index("\n\n### Row 162 skill checkpoint")
    return preface[start:end]


ROW181_PREFACE = t161_to_181(
    extract_preface_row161((ROOT / "writings/preface/chapters/preface.md").read_text())
) + "\n\n"

_prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
_row161_compass = next(
    line for line in _prologue.splitlines() if "(row 161) |" in line and "Row 68 → Row 141" in line
)
PROLOGUE_COMPASS = t161_to_181(_row161_compass) + "\n"

_row161_stitch_body = (
    _prologue.split("**Row 161 closing stitch")[1].split("**Row 160 closing stitch")[0].lstrip().split("\n\n")[0]
)
PROLOGUE_STITCH = t161_to_181(
    "**Row 161 closing stitch (Row 68 → Row 141 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion).** {#row-161-closing-stitch} "
    + _row161_stitch_body.split(".** {#row-161-closing-stitch} ", 1)[-1]
) + "\n\n"

_row161_preview = next(line for line in _prologue.splitlines() if 'id="prologue-preview-row-161"' in line)
PROLOGUE_PREVIEW = t161_to_181(_row161_preview) + "\n"

_epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
EPILOGUE_LOOP = t161_to_181(
    "### Row 161 closing loop"
    + _epilogue.split("### Row 161 closing loop")[1].split("### Row 162 closing loop")[0]
)

_src161_header = "## Row 68 → Row 141 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 161)"
_next161_header = "## Row 68 → Row 142 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion index (row 162)"
_sources_blob = (ROOT / "writings/appendix/chapters/sources.md").read_text()
_src161_body = _sources_blob.split(_src161_header, 1)[1].split(_next161_header, 1)[0]
SOURCES_INDEX = (
    "## Row 68 → Row 161 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 181)"
    + t161_to_181(_src161_body)
)

_row161_table = next(
    line for line in _sources_blob.splitlines() if line.startswith("| 161 | Row 68 → Row 141")
)
SOURCES_TABLE = (
    t161_to_181(_row161_table).replace("| 161 | Row 68 → Row 141", "| 181 | Row 68 → Row 161", 1) + "\n"
)

_row161_mem_table = next(
    line for line in (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text().splitlines()
    if line.startswith("| 161 | Meta |")
)
MEMORY_TABLE = t161_to_181(_row161_mem_table).replace("| 161 | Meta |", "| 181 | Meta |", 1) + "\n"

_baby_anchor = "### Row 161 baby picture {#row-161-baby-picture-row68-row141-handshake4a-meta-prelude-capstone-reunion}"
MEMORY_BABY = t161_to_181(
    (ROOT / "writings/appendix/chapters/memory-sheet.md")
    .read_text()
    .split(_baby_anchor)[1]
    .split("### Row 162 baby picture")[0]
)
MEMORY_BABY = (
    "### Row 181 baby picture (Row 68 → Row 161 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion)"
    + MEMORY_BABY.split(")", 1)[1]
    if ")" in MEMORY_BABY
    else "### Row 181 baby picture" + MEMORY_BABY
)

ROW180_BABY_OLD = (
    "row 180 when **epilogue α cross-links and Row 59 → Row 40 Handshake 3 meta must read on the same wire before row 181 Handshake 4a meta prelude capstone opens on the full capstone path**"
)
ROW180_BABY_NEW = (
    "row 180 when **epilogue α cross-links and Row 59 → Row 40 Handshake 3 meta must read on the same wire before row 181 Handshake 4a meta prelude capstone reunion opens on the full capstone path**"
)

ROW180_TAIL_OLD = (
    "Read the [memory sheet row 180 baby picture](appendix/memory-sheet.md#row-180-baby-picture-row68-row160-handshake3-meta-prelude-capstone-reunion) when opening [row 161](preface.md#skill-navigation-row-161) before row 61 closes on the full capstone path; read the [epilogue row 180 closing loop](epilogue/multiscale.md#row-180-closing-loop) when the competence loop closes. When row 180 is complete, proceed to [row 161](preface.md#skill-navigation-row-161) when bulk hardening parses at lab grip rate but Handshake 4a still feels disconnected from Part VII after verified Handshake 4a meta prelude capstone on the full capstone path, to [row 141](preface.md#skill-navigation-row-141) for the Row 68 ↔ Row 61 Handshake 4a meta audit on the opening-hinge capstone path alone,"
)
ROW180_TAIL_NEW = (
    "Read the [memory sheet row 180 baby picture](appendix/memory-sheet.md#row-180-baby-picture-row68-row160-handshake3-meta-prelude-capstone-reunion) when opening [row 181](preface.md#skill-navigation-row-181) before row 61 closes on the full capstone path; read the [epilogue row 180 closing loop](epilogue/multiscale.md#row-180-closing-loop) when the competence loop closes. When row 180 is complete, proceed to [row 181](preface.md#skill-navigation-row-181) when bulk hardening parses at lab grip rate but Handshake 4a still feels disconnected from Part VII after verified Handshake 4a meta prelude capstone on the full capstone path, to [row 161](preface.md#skill-navigation-row-161) for the Row 68 ↔ Row 61 Handshake 4a meta audit on the opening-hinge capstone path alone, to [row 141](preface.md#skill-navigation-row-141) for the Row 68 ↔ Row 61 Handshake 4a meta audit on the opening-hinge capstone path alone,"
)


def main():
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "skill-navigation-row-181" in preface and preface.index("skill-navigation-row-181") < preface.index(copper):
        print("preface: row 181 already present")
    elif "skill-navigation-row-181" in preface:
        raise SystemExit("preface row 181 exists but not at copper wire insert point")
    else:
        if "skill-navigation-row-180" not in preface:
            raise SystemExit("preface row 180 must exist before row 181")
        if ROW180_TAIL_OLD not in preface:
            raise SystemExit("preface row 180 tail not found")
        preface = preface.replace(ROW180_TAIL_OLD, ROW180_TAIL_NEW)
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + ROW181_PREFACE + copper)
        preface_path.write_text(preface)
        print("preface: added row 181")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-181" not in prologue:
        needle = "| Row 68 → Row 160 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion (row 180) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 180 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + PROLOGUE_COMPASS + prologue[line_end + 1 :]
        prologue = prologue.replace(
            "**Row 180 closing stitch",
            PROLOGUE_STITCH + "**Row 180 closing stitch",
        )
        prologue = prologue.replace(
            '| <span id="prologue-preview-row-180"></span>Row 180 preview',
            PROLOGUE_PREVIEW + '| <span id="prologue-preview-row-180"></span>Row 180 preview',
        )
        prologue = prologue.replace(
            "before row 181 Handshake 4a meta prelude capstone opens on the full capstone path.",
            "before row 182 Handshake 4b meta prelude capstone opens on the full capstone path.",
            1,
        )
        prologue_path.write_text(prologue)
        print("prologue: added row 181")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "### Row 181 closing loop" not in epilogue:
        old_proceed = (
            "Proceed to [row 141](#row-141-closing-loop) when row 68 closed but Handshake 4a meta still feels disconnected after row 180 on the full capstone path, to [row 121](#row-121-closing-loop) for the Row 68 ↔ Row 61 Handshake 4a meta audit on the opening-hinge capstone path alone,"
        )
        new_proceed = (
            "Proceed to [row 181](#row-181-closing-loop) when row 68 closed but Handshake 4a meta still feels disconnected after row 180 on the full capstone path, when bulk hardening parses at lab grip rate after verified Handshake 4a meta prelude capstone but Handshake 4a still feels disconnected from Part VII on the full capstone path, to [row 161](#row-161-closing-loop) for the Row 68 ↔ Row 61 Handshake 4a meta audit on the opening-hinge capstone path alone, to [row 141](#row-141-closing-loop) for the Row 68 ↔ Row 61 Handshake 4a meta audit on the opening-hinge capstone path alone, to [row 121](#row-121-closing-loop) for the Row 68 ↔ Row 61 Handshake 4a meta audit on the opening-hinge capstone path alone,"
        )
        if old_proceed not in epilogue:
            raise SystemExit("epilogue row 180 end marker not found")
        epilogue = epilogue.replace(old_proceed, new_proceed, 1)
        epilogue = epilogue.replace(
            "before row 181 Handshake 4a meta prelude capstone reunion on the full capstone path (then row 161 on the capstone path).",
            "before row 182 Handshake 4b meta prelude capstone reunion on the full capstone path (then row 162 on the capstone path).",
            1,
        )
        marker = "### Row 180 closing loop (Row 68 → Row 160 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion)"
        if marker not in epilogue:
            raise SystemExit("epilogue row 180 insert anchor not found")
        epilogue = epilogue.replace(marker, EPILOGUE_LOOP + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 181")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row161-handshake4a-meta-prelude-capstone-reunion-index-row-181" not in sources:
        sources = sources.replace(
            "| 161 | Row 68 → Row 141 Row 68 → Row 61 Handshake 4a meta prelude capstone",
            SOURCES_TABLE + "| 161 | Row 68 → Row 141 Row 68 → Row 61 Handshake 4a meta prelude capstone",
        )
        sources = sources.replace(
            _src161_header,
            SOURCES_INDEX + _src161_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 181")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-181-baby-picture-row68-row161" not in memory:
        memory = memory.replace(
            "| 180 | Meta | [Row 68 → Row 160 Handshake 3 meta prelude capstone reunion index]",
            MEMORY_TABLE + "| 180 | Meta | [Row 68 → Row 160 Handshake 3 meta prelude capstone reunion index]",
        )
        if _baby_anchor in memory:
            memory = memory.replace(
                _baby_anchor,
                MEMORY_BABY + _baby_anchor,
                1,
            )
        else:
            memory = memory.replace(
                "### Row 180 baby picture (Row 68 → Row 160 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion)",
                MEMORY_BABY + "### Row 180 baby picture (Row 68 → Row 160 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion)",
                1,
            )
        if ROW180_BABY_OLD in memory:
            memory = memory.replace(ROW180_BABY_OLD, ROW180_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 181")


if __name__ == "__main__":
    main()
