#!/usr/bin/env python3
"""Add row 182 meta-stitch (Row 68 → Row 162 ↔ Row 62 Handshake 4b meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def t162_to_182(text: str) -> str:
    """Transform row-162 capstone-path meta copy to row 182 (162→182, 142→162 inner, 181 gate)."""
    repl = [
        ("Row 68 → Row 142 Row 68 → Row 62", "Row 68 → Row 162 Row 68 → Row 62"),
        (
            "row68-row142-handshake4b-meta-prelude-capstone-reunion-index-row-162",
            "TEMP_ROW182_EXP_INDEX",
        ),
        (
            "row-162-baby-picture-row68-row142-handshake4b-meta-prelude-capstone-reunion",
            "row-182-baby-picture-row68-row162-handshake4b-meta-prelude-capstone-reunion",
        ),
        ("skill-navigation-row-162", "TEMP_SKILL_NAV_162"),
        ("prologue-preview-row-162", "prologue-preview-row-182"),
        ("row-162-closing-stitch", "row-182-closing-stitch"),
        ("row-162-closing-loop", "row-182-closing-loop"),
        ("Row 162 three-way audit", "Row 182 three-way audit"),
        (
            "[row 161](preface.md#skill-navigation-row-161) or [row 142](TEMP_SKILL_NAV_162)",
            "[row 181](preface.md#skill-navigation-row-181) or [row 162](TEMP_SKILL_NAV_162)",
        ),
        (
            "[row 161](preface.md#skill-navigation-row-161) or [Row 68 → Row 122 Handshake 4b meta prelude capstone reunion index (row 142)](appendix/sources.md#row68-row122-handshake4b-meta-prelude-capstone-reunion-index-row-142)",
            "[row 181](preface.md#skill-navigation-row-181) or [Row 68 → Row 162 Handshake 4b meta prelude capstone reunion index (row 182)](appendix/sources.md#row68-row162-handshake4b-meta-prelude-capstone-reunion-index-row-182)",
        ),
        (
            "[row 161](preface.md#skill-navigation-row-161) or [Row 68 → Row 142 Handshake 4b meta prelude capstone reunion index (row 162)](appendix/sources.md#row68-row142-handshake4b-meta-prelude-capstone-reunion-index-row-162)",
            "[row 181](preface.md#skill-navigation-row-181) or [Row 68 → Row 162 Handshake 4b meta prelude capstone reunion index (row 182)](appendix/sources.md#row68-row162-handshake4b-meta-prelude-capstone-reunion-index-row-182)",
        ),
        (
            "verified Handshake 4a meta prelude capstone closure (row 161)",
            "verified Handshake 4a meta prelude capstone closure (row 181)",
        ),
        (
            "before row 163 orchestration meta prelude capstone opens on the full capstone path",
            "before row 183 orchestration meta prelude capstone opens on the full capstone path",
        ),
        (
            "before row 163 orchestration meta prelude capstone reunion on the full capstone path",
            "before row 183 orchestration meta prelude capstone reunion on the full capstone path",
        ),
        (
            "before row 143 orchestration meta prelude capstone opens on the full capstone path",
            "before row 183 orchestration meta prelude capstone opens on the full capstone path",
        ),
    ]
    out = text
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW182_EXP_INDEX",
        "row68-row162-handshake4b-meta-prelude-capstone-reunion-index-row-182",
    )
    out = out.replace("TEMP_SKILL_NAV_162", "skill-navigation-row-162")
    out = out.replace("Row 68 → Row 162 Row 68 → Row 62", "TEMP_ROW162_TITLE")
    out = out.replace("row 162", "row 182")
    out = out.replace("Row 162", "Row 182")
    out = out.replace("TEMP_ROW162_TITLE", "Row 68 → Row 162 Row 68 → Row 62")
    out = out.replace("skill-navigation-row-162", "skill-navigation-row-182")
    out = out.replace("[row 182](preface.md#skill-navigation-row-181)", "[row 181](preface.md#skill-navigation-row-181)")
    out = out.replace("[row 182](preface.md#skill-navigation-row-182)", "[row 182](preface.md#skill-navigation-row-182)")
    out = out.replace("[row 182](preface.md#skill-navigation-row-162)", "[row 162](preface.md#skill-navigation-row-162)")
    out = out.replace("[row 162](preface.md#skill-navigation-row-182)", "[row 162](preface.md#skill-navigation-row-162)")
    out = out.replace("when row 161 closed but row 62", "when row 181 closed but row 62")
    out = out.replace("[preface row 182](../preface.md#skill-navigation-row-182)", "[preface row 182](../preface.md#skill-navigation-row-182)")
    out = out.replace("[preface row 162](../preface.md#skill-navigation-row-182)", "[preface row 162](../preface.md#skill-navigation-row-162)")
    out = out.replace("row 1623", "row 181")
    out = out.replace("row 1624", "row 183")
    out = out.replace("row 182 or row 182", "row 181 or row 162")
    out = out.replace("When row 182 closed", "When row 181 closed")
    out = out.replace("after row 182 alone", "after row 181 alone")
    out = out.replace("Recite [preface row 182]", "Recite [preface row 181]")
    out = out.replace("row 182 or row 162 recited", "row 181 or row 162 recited")
    out = out.replace("When row 161 closed — Handshake 4b", "When row 181 closed — Handshake 4b")
    out = out.replace("row 161 or row 142 recited", "row 181 or row 162 recited")
    out = out.replace("when row 161 closed Handshake 4b", "when row 181 closed Handshake 4b")
    out = out.replace("after row 161 alone", "after row 181 alone")
    out = out.replace("from row 182's", "from row 181's")
    out = out.replace("row 161's Handshake 4a meta", "row 181's Handshake 4a meta")
    out = out.replace("row 161 and row 62", "row 181 and row 62")
    out = out.replace("Recite [preface row 161]", "Recite [preface row 181]")
    out = out.replace("row 142", "row 162")
    out = out.replace("Row 142", "Row 162")
    out = out.replace("row 122", "row 142")
    out = out.replace("Row 122", "Row 142")
    out = out.replace(
        "row68-row122-handshake4b-meta-prelude-capstone-reunion-index-row-142",
        "row68-row142-handshake4b-meta-prelude-capstone-reunion-index-row-162",
    )
    out = out.replace(
        "row68-row142-handshake4b-meta-prelude-capstone-reunion-index-row-162",
        "row68-row162-handshake4b-meta-prelude-capstone-reunion-index-row-182",
    )
    out = out.replace(
        "[row 161](preface.md#skill-navigation-row-161) or [row 162]",
        "[row 181](preface.md#skill-navigation-row-181) or [row 162]",
    )
    out = out.replace("row 161", "row 181")
    out = out.replace("Row 161", "Row 181")
    out = out.replace(
        "Row 68 → Row 182 Handshake 4b meta prelude capstone reunion index",
        "Row 68 → Row 162 Handshake 4b meta prelude capstone reunion index",
    )
    out = out.replace(
        "[row 162](preface.md#skill-navigation-row-142)",
        "[row 162](preface.md#skill-navigation-row-162)",
    )
    return out


def extract_preface_row162(preface: str) -> str:
    start = preface.index("### Row 162 skill checkpoint")
    end = preface.index("\n\n### Row 163 skill checkpoint")
    return preface[start:end]


ROW182_PREFACE = t162_to_182(
    extract_preface_row162((ROOT / "writings/preface/chapters/preface.md").read_text())
) + "\n\n"

_prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
_row162_compass = next(
    line for line in _prologue.splitlines() if "(row 162) |" in line and "Row 68 → Row 142" in line
)
PROLOGUE_COMPASS = t162_to_182(_row162_compass) + "\n"

_row162_stitch_body = (
    _prologue.split("**Row 162 closing stitch")[1].split("**Row 161 closing stitch")[0].lstrip().split("\n\n")[0]
)
PROLOGUE_STITCH = t162_to_182(
    "**Row 162 closing stitch (Row 68 → Row 142 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion).** {#row-162-closing-stitch} "
    + _row162_stitch_body.split(".** {#row-162-closing-stitch} ", 1)[-1]
) + "\n\n"

_row162_preview = next(line for line in _prologue.splitlines() if 'id="prologue-preview-row-162"' in line)
PROLOGUE_PREVIEW = t162_to_182(_row162_preview) + "\n"

_epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
EPILOGUE_LOOP = t162_to_182(
    "### Row 162 closing loop"
    + _epilogue.split("### Row 162 closing loop")[1].split("### Row 163 closing loop")[0]
)

_src162_header = "## Row 68 → Row 142 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion index (row 162)"
_next162_header = "## Row 68 → Row 143 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 163)"
_sources_blob = (ROOT / "writings/appendix/chapters/sources.md").read_text()
_src162_body = _sources_blob.split(_src162_header, 1)[1].split(_next162_header, 1)[0]
SOURCES_INDEX = (
    "## Row 68 → Row 162 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion index (row 182)"
    + t162_to_182(_src162_body)
)

_row162_table = next(
    line for line in _sources_blob.splitlines() if line.startswith("| 162 | Row 68 → Row 142")
)
SOURCES_TABLE = (
    t162_to_182(_row162_table).replace("| 162 | Row 68 → Row 142", "| 182 | Row 68 → Row 162", 1) + "\n"
)

_row162_mem_table = next(
    line for line in (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text().splitlines()
    if line.startswith("| 162 | Meta |")
)
MEMORY_TABLE = t162_to_182(_row162_mem_table).replace("| 162 | Meta |", "| 182 | Meta |", 1) + "\n"

_baby_anchor = "### Row 162 baby picture {#row-162-baby-picture-row68-row142-handshake4b-meta-prelude-capstone-reunion}"
MEMORY_BABY = t162_to_182(
    (ROOT / "writings/appendix/chapters/memory-sheet.md")
    .read_text()
    .split(_baby_anchor)[1]
    .split("### Row 163 baby picture")[0]
)
MEMORY_BABY = (
    "### Row 182 baby picture (Row 68 → Row 162 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion)"
    + MEMORY_BABY.split(")", 1)[1]
    if ")" in MEMORY_BABY
    else "### Row 182 baby picture" + MEMORY_BABY
)

ROW181_BABY_OLD = (
    "row 181 when **epilogue rate cross-links and Row 60 → Row 41 Handshake 4a meta must read on the same wire before row 162 Handshake 4b meta prelude capstone reunion opens on the full capstone path**"
)
ROW181_BABY_NEW = (
    "row 181 when **epilogue rate cross-links and Row 60 → Row 41 Handshake 4a meta must read on the same wire before row 182 Handshake 4b meta prelude capstone reunion opens on the full capstone path**"
)

ROW181_TAIL_OLD = (
    "Read the [memory sheet row 181 baby picture](appendix/memory-sheet.md#row-181-baby-picture-row68-row161-handshake4a-meta-prelude-capstone-reunion) when opening [row 162](preface.md#skill-navigation-row-162) before row 62 closes on the full capstone path; read the [epilogue row 181 closing loop](epilogue/multiscale.md#row-181-closing-loop) when the competence loop closes. When row 181 is complete, proceed to [row 162](preface.md#skill-navigation-row-162) when bulk hardening matches flow stress but Handshake 4b still feels disconnected from Part VII Step 4 after verified Handshake 4a meta prelude capstone on the full capstone path, to [row 142](preface.md#skill-navigation-row-142) for the Row 68 ↔ Row 62 Handshake 4b meta audit on the opening-hinge capstone path alone,"
)
ROW181_TAIL_NEW = (
    "Read the [memory sheet row 181 baby picture](appendix/memory-sheet.md#row-181-baby-picture-row68-row161-handshake4a-meta-prelude-capstone-reunion) when opening [row 182](preface.md#skill-navigation-row-182) before row 62 closes on the full capstone path; read the [epilogue row 181 closing loop](epilogue/multiscale.md#row-181-closing-loop) when the competence loop closes. When row 181 is complete, proceed to [row 182](preface.md#skill-navigation-row-182) when bulk hardening matches flow stress but Handshake 4b still feels disconnected from Part VII Step 4 after verified Handshake 4a meta prelude capstone on the full capstone path, to [row 162](preface.md#skill-navigation-row-162) for the Row 68 ↔ Row 62 Handshake 4b meta audit on the opening-hinge capstone path alone, to [row 142](preface.md#skill-navigation-row-142) for the Row 68 ↔ Row 62 Handshake 4b meta audit on the opening-hinge capstone path alone,"
)


def main():
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "skill-navigation-row-182" in preface and preface.index("skill-navigation-row-182") < preface.index(copper):
        print("preface: row 182 already present")
    elif "skill-navigation-row-182" in preface:
        raise SystemExit("preface row 182 exists but not at copper wire insert point")
    else:
        if "skill-navigation-row-181" not in preface:
            raise SystemExit("preface row 181 must exist before row 182")
        if ROW181_TAIL_OLD not in preface:
            raise SystemExit("preface row 181 tail not found")
        preface = preface.replace(ROW181_TAIL_OLD, ROW181_TAIL_NEW)
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + ROW182_PREFACE + copper)
        preface_path.write_text(preface)
        print("preface: added row 182")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-182" not in prologue:
        needle = "| Row 68 → Row 161 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion (row 181) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 181 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + PROLOGUE_COMPASS + prologue[line_end + 1 :]
        prologue = prologue.replace(
            "**Row 181 closing stitch",
            PROLOGUE_STITCH + "**Row 181 closing stitch",
        )
        prologue = prologue.replace(
            '| <span id="prologue-preview-row-181"></span>Row 181 preview',
            PROLOGUE_PREVIEW + '| <span id="prologue-preview-row-181"></span>Row 181 preview',
        )
        prologue = prologue.replace(
            "before row 182 Handshake 4b meta prelude capstone opens on the full capstone path.",
            "before row 183 orchestration meta prelude capstone opens on the full capstone path.",
            1,
        )
        prologue_path.write_text(prologue)
        print("prologue: added row 182")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "### Row 182 closing loop" not in epilogue:
        old_proceed = (
            "Proceed to [row 162](#row-162-closing-loop) when row 68 closed but Handshake 4b meta still feels disconnected after row 181 on the full capstone path, to [row 122](#row-122-closing-loop) for the Row 68 ↔ Row 62 meta audit on the opening-hinge capstone path alone,"
        )
        new_proceed = (
            "Proceed to [row 182](#row-182-closing-loop) when row 68 closed but Handshake 4b meta still feels disconnected after row 181 on the full capstone path, when bulk hardening matches flow stress but Handshake 4b still feels disconnected from Part VII Step 4 after verified Handshake 4a meta prelude capstone on the full capstone path, to [row 162](#row-162-closing-loop) for the Row 68 ↔ Row 62 Handshake 4b meta audit on the opening-hinge capstone path alone, to [row 142](#row-142-closing-loop) for the Row 68 ↔ Row 62 meta audit on the opening-hinge capstone path alone, to [row 122](#row-122-closing-loop) for the Row 68 ↔ Row 62 meta audit on the opening-hinge capstone path alone,"
        )
        if old_proceed not in epilogue:
            raise SystemExit("epilogue row 181 end marker not found")
        epilogue = epilogue.replace(old_proceed, new_proceed, 1)
        epilogue = epilogue.replace(
            "before row 182 Handshake 4b meta prelude capstone reunion on the full capstone path (then row 162 on the capstone path).",
            "before row 183 orchestration meta prelude capstone reunion on the full capstone path (then row 163 on the capstone path).",
            1,
        )
        marker = "### Row 181 closing loop (Row 68 → Row 161 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion)"
        if marker not in epilogue:
            raise SystemExit("epilogue row 181 insert anchor not found")
        epilogue = epilogue.replace(marker, EPILOGUE_LOOP + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 182")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row162-handshake4b-meta-prelude-capstone-reunion-index-row-182" not in sources:
        sources = sources.replace(
            "| 162 | Row 68 → Row 142 Row 68 → Row 62 Handshake 4b meta prelude capstone",
            SOURCES_TABLE + "| 162 | Row 68 → Row 142 Row 68 → Row 62 Handshake 4b meta prelude capstone",
        )
        sources = sources.replace(
            _src162_header,
            SOURCES_INDEX + _src162_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 182")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-182-baby-picture-row68-row162" not in memory:
        memory = memory.replace(
            "| 181 | Meta | [Row 68 → Row 161 Handshake 4a meta prelude capstone reunion index]",
            MEMORY_TABLE + "| 181 | Meta | [Row 68 → Row 161 Handshake 4a meta prelude capstone reunion index]",
        )
        if _baby_anchor in memory:
            memory = memory.replace(
                _baby_anchor,
                MEMORY_BABY + _baby_anchor,
                1,
            )
        else:
            memory = memory.replace(
                "### Row 181 baby picture (Row 68 → Row 161 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion)",
                MEMORY_BABY + "### Row 181 baby picture (Row 68 → Row 161 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion)",
                1,
            )
        if ROW181_BABY_OLD in memory:
            memory = memory.replace(ROW181_BABY_OLD, ROW181_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 182")


if __name__ == "__main__":
    main()
