#!/usr/bin/env python3
"""Add row 183 meta-stitch (Row 68 → Row 163 ↔ Row 63 orchestration meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def t163_to_183(text: str) -> str:
    """Transform row-163 capstone-path meta copy to row 183 (163→183, 143→163 inner, 182 gate)."""
    repl = [
        ("Row 68 → Row 143 Row 68 → Row 63", "Row 68 → Row 163 Row 68 → Row 63"),
        (
            "row68-row143-orchestration-meta-prelude-capstone-reunion-index-row-163",
            "TEMP_ROW183_EXP_INDEX",
        ),
        (
            "row-163-baby-picture-row68-row143-orchestration-meta-prelude-capstone-reunion",
            "row-183-baby-picture-row68-row163-orchestration-meta-prelude-capstone-reunion",
        ),
        ("skill-navigation-row-163", "TEMP_SKILL_NAV_163"),
        ("prologue-preview-row-163", "prologue-preview-row-183"),
        ("row-163-closing-stitch", "row-183-closing-stitch"),
        ("row-163-closing-loop", "row-183-closing-loop"),
        ("Row 163 three-way audit", "Row 183 three-way audit"),
        (
            "[row 162](preface.md#skill-navigation-row-162) or [row 143](TEMP_SKILL_NAV_163)",
            "[row 182](preface.md#skill-navigation-row-182) or [row 163](TEMP_SKILL_NAV_163)",
        ),
        (
            "[row 162](preface.md#skill-navigation-row-162) or [Row 68 → Row 123 orchestration meta prelude capstone reunion index (row 143)](appendix/sources.md#row68-row123-orchestration-meta-prelude-capstone-reunion-index-row-143)",
            "[row 182](preface.md#skill-navigation-row-182) or [Row 68 → Row 163 orchestration meta prelude capstone reunion index (row 183)](appendix/sources.md#row68-row163-orchestration-meta-prelude-capstone-reunion-index-row-183)",
        ),
        (
            "[row 162](preface.md#skill-navigation-row-162) or [Row 68 → Row 143 orchestration meta prelude capstone reunion index (row 143)](appendix/sources.md#row68-row143-orchestration-meta-prelude-capstone-reunion-index-row-143)",
            "[row 182](preface.md#skill-navigation-row-182) or [Row 68 → Row 163 orchestration meta prelude capstone reunion index (row 183)](appendix/sources.md#row68-row163-orchestration-meta-prelude-capstone-reunion-index-row-183)",
        ),
        (
            "verified Handshake 4b meta prelude capstone closure (row 162)",
            "verified Handshake 4b meta prelude capstone closure (row 182)",
        ),
        (
            "before row 164 book-loop meta prelude capstone opens on the full capstone path",
            "before row 184 book-loop meta prelude capstone opens on the full capstone path",
        ),
        (
            "before row 164 book-loop meta prelude capstone reunion on the full capstone path",
            "before row 184 book-loop meta prelude capstone reunion on the full capstone path",
        ),
        (
            "before row 144 book-loop meta prelude capstone opens on the full capstone path",
            "before row 184 book-loop meta prelude capstone opens on the full capstone path",
        ),
    ]
    out = text
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW183_EXP_INDEX",
        "row68-row163-orchestration-meta-prelude-capstone-reunion-index-row-183",
    )
    out = out.replace("TEMP_SKILL_NAV_163", "skill-navigation-row-163")
    out = out.replace("Row 68 → Row 163 Row 68 → Row 63", "TEMP_ROW163_TITLE")
    out = out.replace("row 163", "row 183")
    out = out.replace("Row 163", "Row 183")
    out = out.replace("TEMP_ROW163_TITLE", "Row 68 → Row 163 Row 68 → Row 63")
    out = out.replace("skill-navigation-row-163", "skill-navigation-row-183")
    out = out.replace("[row 183](preface.md#skill-navigation-row-182)", "[row 182](preface.md#skill-navigation-row-182)")
    out = out.replace("[row 183](preface.md#skill-navigation-row-183)", "[row 183](preface.md#skill-navigation-row-183)")
    out = out.replace("[row 183](preface.md#skill-navigation-row-163)", "[row 163](preface.md#skill-navigation-row-163)")
    out = out.replace("[row 163](preface.md#skill-navigation-row-183)", "[row 163](preface.md#skill-navigation-row-163)")
    out = out.replace("when row 162 closed but row 63", "when row 182 closed but row 63")
    out = out.replace("[preface row 183](../preface.md#skill-navigation-row-183)", "[preface row 183](../preface.md#skill-navigation-row-183)")
    out = out.replace("[preface row 163](../preface.md#skill-navigation-row-183)", "[preface row 163](../preface.md#skill-navigation-row-163)")
    out = out.replace("row 1633", "row 182")
    out = out.replace("row 1634", "row 184")
    out = out.replace("row 183 or row 183", "row 182 or row 163")
    out = out.replace("When row 183 closed", "When row 182 closed")
    out = out.replace("after row 183 alone", "after row 182 alone")
    out = out.replace("Recite [preface row 183]", "Recite [preface row 182]")
    out = out.replace("row 183 or row 163 recited", "row 182 or row 163 recited")
    out = out.replace("When row 162 closed — orchestration", "When row 182 closed — orchestration")
    out = out.replace("row 162 or row 143 recited", "row 182 or row 163 recited")
    out = out.replace("when row 162 closed orchestration", "when row 182 closed orchestration")
    out = out.replace("after row 162 alone", "after row 182 alone")
    out = out.replace("from row 183's", "from row 182's")
    out = out.replace("row 162's Handshake 4b meta", "row 182's Handshake 4b meta")
    out = out.replace("row 162 and row 63", "row 182 and row 63")
    out = out.replace("Recite [preface row 162]", "Recite [preface row 182]")
    out = out.replace("row 143", "row 163")
    out = out.replace("Row 143", "Row 163")
    out = out.replace("row 123", "row 143")
    out = out.replace("Row 123", "Row 143")
    out = out.replace(
        "row68-row123-orchestration-meta-prelude-capstone-reunion-index-row-143",
        "row68-row143-orchestration-meta-prelude-capstone-reunion-index-row-163",
    )
    out = out.replace(
        "row68-row143-orchestration-meta-prelude-capstone-reunion-index-row-163",
        "row68-row163-orchestration-meta-prelude-capstone-reunion-index-row-183",
    )
    out = out.replace(
        "[row 162](preface.md#skill-navigation-row-162) or [row 163]",
        "[row 182](preface.md#skill-navigation-row-182) or [row 163]",
    )
    out = out.replace("row 162", "row 182")
    out = out.replace("Row 162", "Row 182")
    out = out.replace(
        "Row 68 → Row 183 orchestration meta prelude capstone reunion index",
        "Row 68 → Row 163 orchestration meta prelude capstone reunion index",
    )
    out = out.replace(
        "[row 163](preface.md#skill-navigation-row-143)",
        "[row 163](preface.md#skill-navigation-row-163)",
    )
    return out


def extract_preface_row163(preface: str) -> str:
    start = preface.index("### Row 163 skill checkpoint")
    end = preface.index("\n\n### Row 164 skill checkpoint")
    return preface[start:end]


ROW183_PREFACE = t163_to_183(
    extract_preface_row163((ROOT / "writings/preface/chapters/preface.md").read_text())
) + "\n\n"

_prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
_row163_compass = next(
    line for line in _prologue.splitlines() if "(row 163) |" in line and "Row 68 → Row 143" in line
)
PROLOGUE_COMPASS = t163_to_183(_row163_compass) + "\n"

_row163_stitch_body = (
    _prologue.split("**Row 163 closing stitch")[1].split("**Row 162 closing stitch")[0].lstrip().split("\n\n")[0]
)
PROLOGUE_STITCH = t163_to_183(
    "**Row 163 closing stitch (Row 68 → Row 143 Row 68 → Row 63 orchestration meta prelude capstone reunion).** {#row-163-closing-stitch} "
    + _row163_stitch_body.split(".** {#row-163-closing-stitch} ", 1)[-1]
) + "\n\n"

_row163_preview = next(line for line in _prologue.splitlines() if 'id="prologue-preview-row-163"' in line)
PROLOGUE_PREVIEW = t163_to_183(_row163_preview) + "\n"

_epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
EPILOGUE_LOOP = t163_to_183(
    "### Row 163 closing loop"
    + _epilogue.split("### Row 163 closing loop")[1].split("### Row 164 closing loop")[0]
)

_src163_header = "## Row 68 → Row 143 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 163)"
_next163_header = "## Row 68 → Row 144 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 164)"
_sources_blob = (ROOT / "writings/appendix/chapters/sources.md").read_text()
_src163_body = _sources_blob.split(_src163_header, 1)[1].split(_next163_header, 1)[0]
SOURCES_INDEX = (
    "## Row 68 → Row 163 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 183)"
    + t163_to_183(_src163_body)
)

_row163_table = next(
    line for line in _sources_blob.splitlines() if line.startswith("| 163 | Row 68 → Row 143")
)
SOURCES_TABLE = (
    t163_to_183(_row163_table).replace("| 163 | Row 68 → Row 163", "| 183 | Row 68 → Row 163", 1) + "\n"
)

_row163_mem_table = next(
    line for line in (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text().splitlines()
    if line.startswith("| 163 | Meta |")
)
MEMORY_TABLE = t163_to_183(_row163_mem_table).replace("| 163 | Meta |", "| 183 | Meta |", 1) + "\n"

_baby_anchor = "### Row 163 baby picture {#row-163-baby-picture-row68-row143-orchestration-meta-prelude-capstone-reunion}"
MEMORY_BABY = t163_to_183(
    (ROOT / "writings/appendix/chapters/memory-sheet.md")
    .read_text()
    .split(_baby_anchor)[1]
    .split("### Row 164 baby picture")[0]
)
MEMORY_BABY = (
    "### Row 183 baby picture (Row 68 → Row 163 Row 68 → Row 63 orchestration meta prelude capstone reunion)"
    + MEMORY_BABY.split(")", 1)[1]
    if ")" in MEMORY_BABY
    else "### Row 183 baby picture" + MEMORY_BABY
)

ROW182_BABY_OLD = (
    "row 182 when **epilogue FE² cross-links and Row 61 → Row 42 Handshake 4b meta must read on the same wire before row 163 orchestration meta prelude capstone reunion opens on the full capstone path**"
)
ROW182_BABY_NEW = (
    "row 182 when **epilogue FE² cross-links and Row 61 → Row 42 Handshake 4b meta must read on the same wire before row 183 orchestration meta prelude capstone reunion opens on the full capstone path**"
)

ROW182_TAIL_OLD = (
    "Read the [memory sheet row 182 baby picture](appendix/memory-sheet.md#row-182-baby-picture-row68-row162-handshake4b-meta-prelude-capstone-reunion) when opening [row 163](preface.md#skill-navigation-row-163) before row 63 closes on the full capstone path; read the [epilogue row 182 closing loop](epilogue/multiscale.md#row-182-closing-loop) when the competence loop closes. When row 182 is complete, proceed to [row 163](preface.md#skill-navigation-row-163) when Handshakes 1–4b verify individually but orchestration meta still feels disconnected from Act VI foundation after verified Handshake 4b meta prelude capstone on the full capstone path, to [row 143](preface.md#skill-navigation-row-143) for the Row 68 ↔ Row 63 orchestration meta audit on the opening-hinge capstone path alone,"
)
ROW182_TAIL_NEW = (
    "Read the [memory sheet row 182 baby picture](appendix/memory-sheet.md#row-182-baby-picture-row68-row162-handshake4b-meta-prelude-capstone-reunion) when opening [row 183](preface.md#skill-navigation-row-183) before row 63 closes on the full capstone path; read the [epilogue row 182 closing loop](epilogue/multiscale.md#row-182-closing-loop) when the competence loop closes. When row 182 is complete, proceed to [row 183](preface.md#skill-navigation-row-183) when Handshakes 1–4b verify individually but orchestration meta still feels disconnected from Act VI foundation after verified Handshake 4b meta prelude capstone on the full capstone path, to [row 163](preface.md#skill-navigation-row-163) for the Row 68 ↔ Row 63 orchestration meta audit on the opening-hinge capstone path alone, to [row 143](preface.md#skill-navigation-row-143) for the Row 68 ↔ Row 63 orchestration meta audit on the opening-hinge capstone path alone,"
)


def main():
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "skill-navigation-row-183" in preface and preface.index("skill-navigation-row-183") < preface.index(copper):
        print("preface: row 183 already present")
    elif "skill-navigation-row-183" in preface:
        raise SystemExit("preface row 183 exists but not at copper wire insert point")
    else:
        if "skill-navigation-row-182" not in preface:
            raise SystemExit("preface row 182 must exist before row 183")
        if ROW182_TAIL_OLD not in preface:
            raise SystemExit("preface row 182 tail not found")
        preface = preface.replace(ROW182_TAIL_OLD, ROW182_TAIL_NEW)
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + ROW183_PREFACE + copper)
        preface_path.write_text(preface)
        print("preface: added row 183")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-183" not in prologue:
        needle = "| Row 68 → Row 162 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion (row 182) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 182 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + PROLOGUE_COMPASS + prologue[line_end + 1 :]
        prologue = prologue.replace(
            "**Row 182 closing stitch",
            PROLOGUE_STITCH + "**Row 182 closing stitch",
        )
        prologue = prologue.replace(
            '| <span id="prologue-preview-row-182"></span>Row 182 preview',
            PROLOGUE_PREVIEW + '| <span id="prologue-preview-row-182"></span>Row 182 preview',
        )
        prologue = prologue.replace(
            "before row 183 orchestration meta prelude capstone opens on the full capstone path.",
            "before row 184 book-loop meta prelude capstone opens on the full capstone path.",
            1,
        )
        prologue_path.write_text(prologue)
        print("prologue: added row 183")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "### Row 183 closing loop" not in epilogue:
        old_proceed = (
            "Proceed to [row 163](#row-163-closing-loop) when row 68 closed but orchestration meta still feels disconnected after row 182 on the full capstone path, to [row 123](#row-123-closing-loop) for the Row 68 ↔ Row 63 meta audit on the opening-hinge capstone path alone,"
        )
        new_proceed = (
            "Proceed to [row 183](#row-183-closing-loop) when row 68 closed but orchestration meta still feels disconnected after row 182 on the full capstone path, when Handshakes 1–4b verify individually but orchestration meta still feels disconnected from Act VI foundation after verified Handshake 4b meta prelude capstone on the full capstone path, to [row 163](#row-163-closing-loop) for the Row 68 ↔ Row 63 orchestration meta audit on the opening-hinge capstone path alone, to [row 143](#row-143-closing-loop) for the Row 68 ↔ Row 63 meta audit on the opening-hinge capstone path alone, to [row 123](#row-123-closing-loop) for the Row 68 ↔ Row 63 meta audit on the opening-hinge capstone path alone,"
        )
        if old_proceed not in epilogue:
            raise SystemExit("epilogue row 182 end marker not found")
        epilogue = epilogue.replace(old_proceed, new_proceed, 1)
        epilogue = epilogue.replace(
            "before row 183 orchestration meta prelude capstone reunion on the full capstone path (then row 163 on the capstone path).",
            "before row 184 book-loop meta prelude capstone reunion on the full capstone path (then row 164 on the capstone path).",
            1,
        )
        marker = "### Row 182 closing loop (Row 68 → Row 162 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion)"
        if marker not in epilogue:
            raise SystemExit("epilogue row 182 insert anchor not found")
        epilogue = epilogue.replace(marker, EPILOGUE_LOOP + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 183")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row163-orchestration-meta-prelude-capstone-reunion-index-row-183" not in sources:
        sources = sources.replace(
            "| 163 | Row 68 → Row 143 Row 68 → Row 63 orchestration meta prelude capstone",
            SOURCES_TABLE + "| 163 | Row 68 → Row 143 Row 68 → Row 63 orchestration meta prelude capstone",
        )
        sources = sources.replace(
            _src163_header,
            SOURCES_INDEX + _src163_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 183")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-183-baby-picture-row68-row163" not in memory:
        memory = memory.replace(
            "| 182 | Meta | [Row 68 → Row 162 Handshake 4b meta prelude capstone reunion index]",
            MEMORY_TABLE + "| 182 | Meta | [Row 68 → Row 162 Handshake 4b meta prelude capstone reunion index]",
        )
        if _baby_anchor in memory:
            memory = memory.replace(
                _baby_anchor,
                MEMORY_BABY + _baby_anchor,
                1,
            )
        else:
            memory = memory.replace(
                "### Row 182 baby picture (Row 68 → Row 162 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion)",
                MEMORY_BABY + "### Row 182 baby picture (Row 68 → Row 162 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion)",
                1,
            )
        if ROW182_BABY_OLD in memory:
            memory = memory.replace(ROW182_BABY_OLD, ROW182_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 183")


if __name__ == "__main__":
    main()
