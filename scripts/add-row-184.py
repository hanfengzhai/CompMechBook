#!/usr/bin/env python3
"""Add row 184 meta-stitch (Row 68 → Row 164 ↔ Row 64 book-loop meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def t164_to_184(text: str) -> str:
    """Transform row-144 capstone-path meta copy to row 164 (164→184, 144→164 inner, 183 gate)."""
    repl = [
        ("Row 68 → Row 144 Row 68 → Row 64", "Row 68 → Row 164 Row 68 → Row 64"),
        (
            "row68-row144-book-loop-meta-prelude-capstone-reunion-index-row-144",
            "row68-row144-book-loop-meta-prelude-capstone-reunion-index-row-164",
        ),
        (
            "row-144-baby-picture-row68-row144-book-loop-meta-prelude-capstone-reunion",
            "row-164-baby-picture-row68-row144-book-loop-meta-prelude-capstone-reunion",
        ),
        ("skill-navigation-row-144", "skill-navigation-row-164"),
        ("prologue-preview-row-144", "prologue-preview-row-164"),
        ("row-144-closing-stitch", "row-164-closing-stitch"),
        ("row-144-closing-loop", "row-164-closing-loop"),
        ("Row 164 three-way audit", "Row 164 three-way audit"),
        (
            "[row 163](preface.md#skill-navigation-row-143) or [row 164](preface.md#skill-navigation-row-124)",
            "[row 163](preface.md#skill-navigation-row-163) or [row 164](preface.md#skill-navigation-row-144)",
        ),
        (
            "[row 163](preface.md#skill-navigation-row-143) or [Row 68 → Row 124",
            "[row 163](preface.md#skill-navigation-row-163) or [Row 68 → Row 164",
        ),
        ("on the capstone path", "on the full capstone path"),
        ("(capstone path)", "(full capstone path)"),
        ("Row 68 ↔ Row 64 reunion (capstone path)", "Row 68 ↔ Row 64 reunion (full capstone path)"),
    ]
    out = text
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace("row 164", "row 184")
    out = out.replace("Row 164", "Row 164")
    out = out.replace("[row 164](preface.md#skill-navigation-row-163)", "[row 163](preface.md#skill-navigation-row-163)")
    out = out.replace("[row 164](preface.md#skill-navigation-row-144)", "[row 164](preface.md#skill-navigation-row-144)")
    out = out.replace("row 185", "row 165")
    out = out.replace("row 186", "row 166")
    out = out.replace("row 164 or row 164", "row 163 or row 164")
    out = out.replace("When row 164 closed — orchestration", "When row 183 closed — orchestration")
    out = out.replace("When row 164 closed — book-loop", "When row 183 closed — book-loop")
    out = out.replace("row 164 closed orchestration", "row 183 closed orchestration")
    out = out.replace("row 164 closed book-loop", "row 183 closed book-loop")
    out = out.replace("after row 164 alone", "after row 183 alone")
    out = out.replace("Recite [preface row 164]", "Recite [preface row 183]")
    out = out.replace("row 164 or row 164 recited", "row 163 or row 164 recited")
    out = out.replace("from row 164's", "from row 183's")
    out = out.replace(
        "verified orchestration meta prelude capstone closure (row 164)",
        "verified orchestration meta prelude capstone closure (row 183)",
    )
    out = out.replace(
        "verified orchestration meta prelude capstone closure (row 183)",
        "verified orchestration meta prelude capstone closure (row 183)",
    )
    out = out.replace(
        "verified orchestration meta prelude capstone closure (row 182)",
        "verified orchestration meta prelude capstone closure (row 183)",
    )
    out = out.replace("row 164", "row 184")
    out = out.replace("Row 164", "Row 164")
    out = out.replace("row 163", "row 163")
    out = out.replace("Row 163", "Row 163")
    out = out.replace("row 182", "row 182")
    out = out.replace("Row 182", "Row 182")
    out = out.replace(
        "before row 165 second-pass meta prelude capstone opens on the full capstone path",
        "before row 165 second-pass meta prelude capstone opens on the full capstone path",
    )
    out = out.replace(
        "Proceed to [row 165]",
        "Proceed to [row 165]",
    )
    out = out.replace(
        "Do not conflate row 184 (row 68 ↔ row 64 reunion on the full capstone path) with row 164",
        "Do not conflate row 184 (row 68 ↔ row 64 reunion on the full capstone path) with row 164",
    )
    out = out.replace(
        "row 164 names **Row 68 → Row 124 Row 68 → Row 64 book-loop meta prelude capstone reunion**",
        "row 164 names **Row 68 → Row 164 Row 68 → Row 64 book-loop meta prelude capstone reunion**",
    )
    out = out.replace(
        "Row 68 → Row 164 Row 68 → Row 64",
        "Row 68 → Row 164 Row 68 → Row 64",
    )
    out = out.replace("#skill-navigation-row-1645", "#skill-navigation-row-165")
    out = out.replace("#skill-navigation-row-162)", "#skill-navigation-row-162)")
    out = out.replace("#skill-navigation-row-143)", "#skill-navigation-row-163)")
    out = out.replace(
        "row68-row124-book-loop-meta-prelude-capstone-reunion-index-row-124",
        "row68-row144-book-loop-meta-prelude-capstone-reunion-index-row-144",
    )
    out = out.replace(
        "row68-row123-orchestration-meta-prelude-capstone-reunion-index-row-143",
        "row68-row143-orchestration-meta-prelude-capstone-reunion-index-row-163",
    )
    out = out.replace("#row-124-closing-loop)", "#row-164-closing-loop)")
    out = out.replace("#row-143-closing-loop)", "#row-183-closing-loop)")
    out = out.replace(
        "Row 164 names **Row 68 → Row 124 Row 68 → Row 64 book-loop meta prelude capstone reunion**",
        "Row 164 names **Row 68 → Row 164 Row 68 → Row 64 book-loop meta prelude capstone reunion**",
    )
    out = out.replace(
        "row 183 names **Row 68 → Row 123 Row 68 → Row 63 orchestration meta prelude capstone reunion**",
        "row 183 names **Row 68 → Row 163 Row 68 → Row 63 orchestration meta prelude capstone reunion**",
    )
    return out


def extract_preface_row164(preface: str) -> str:
    start = preface.index("### Row 164 skill checkpoint")
    end = preface.index("\n\n### Row 165 skill checkpoint")
    return preface[start:end]


ROW184_PREFACE = t164_to_184(
    extract_preface_row164((ROOT / "writings/preface/chapters/preface.md").read_text())
) + "\n\n"

_prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
_row164_compass = next(
    line for line in _prologue.splitlines() if "(row 164) |" in line and "Row 68 → Row 144" in line
)
PROLOGUE_COMPASS = t164_to_184(_row164_compass) + "\n"

_row164_stitch_body = (
    _prologue.split("**Row 164 closing stitch")[1].split("**Row 163 closing stitch")[0].lstrip().split("\n\n")[0]
)
PROLOGUE_STITCH = t164_to_184(
    "**Row 164 closing stitch (Row 68 → Row 144 Row 68 → Row 64 book-loop meta prelude capstone reunion).** {#row-164-closing-stitch} "
    + _row164_stitch_body.split(".** {#row-164-closing-stitch} ", 1)[-1]
) + "\n\n"

_row164_preview = next(line for line in _prologue.splitlines() if 'id="prologue-preview-row-164"' in line)
PROLOGUE_PREVIEW = t164_to_184(_row164_preview) + "\n"

_epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
EPILOGUE_LOOP = t164_to_184(
    "### Row 164 closing loop"
    + _epilogue.split("### Row 164 closing loop")[1].split("### Row 165 closing loop")[0]
)

_src164_header = "## Row 68 → Row 144 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 164)"
_next164_header = "## Row 68 → Row 145 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 165)"
_sources_blob = (ROOT / "writings/appendix/chapters/sources.md").read_text()
_src164_body = _sources_blob.split(_src164_header, 1)[1].split(_next164_header, 1)[0]
SOURCES_INDEX = (
    "## Row 68 → Row 164 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 184)"
    + t164_to_184(_src164_body)
)

_row164_table = next(
    line for line in _sources_blob.splitlines() if line.startswith("| 164 | Row 68 → Row 144")
)
SOURCES_TABLE = (
    t164_to_184(_row164_table).replace("| 164 | Row 68 → Row 164", "| 184 | Row 68 → Row 164", 1) + "\n"
)

_row164_mem_table = next(
    line for line in (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text().splitlines()
    if line.startswith("| 164 | Meta |")
)
MEMORY_TABLE = t164_to_184(_row164_mem_table).replace("| 164 | Meta |", "| 184 | Meta |", 1) + "\n"

_baby_anchor = "### Row 164 baby picture {#row-164-baby-picture-row68-row144-book-loop-meta-prelude-capstone-reunion}"
MEMORY_BABY = t164_to_184(
    (ROOT / "writings/appendix/chapters/memory-sheet.md")
    .read_text()
    .split(_baby_anchor)[1]
    .split("### Row 165 baby picture")[0]
)
MEMORY_BABY = (
    "### Row 184 baby picture (Row 68 → Row 164 Row 68 → Row 64 book-loop meta prelude capstone reunion)"
    + MEMORY_BABY.split(")", 1)[1]
    if ")" in MEMORY_BABY
    else "### Row 184 baby picture" + MEMORY_BABY
)

ROW183_BABY_OLD = (
    "row 183 when **epilogue orchestration cross-links and Row 62 → Row 43 meta must read on the same wire before row 164 book-loop meta prelude capstone reunion opens on the full capstone path**"
)
ROW183_BABY_NEW = (
    "row 183 when **epilogue orchestration cross-links and Row 62 → Row 43 meta must read on the same wire before row 184 book-loop meta prelude capstone reunion opens on the full capstone path**"
)

ROW183_TAIL_OLD = (
    "Read the [memory sheet row 183 baby picture](appendix/memory-sheet.md#row-183-baby-picture-row68-row163-orchestration-meta-prelude-capstone-reunion) when opening [row 164](preface.md#skill-navigation-row-164) before row 64 closes on the full capstone path; read the [epilogue row 183 closing loop](epilogue/multiscale.md#row-183-closing-loop) when the competence loop closes. When row 183 is complete, proceed to [row 164](preface.md#skill-navigation-row-164) when orchestration verifies individually but book-loop meta still feels disconnected from next-project restart after verified orchestration meta prelude capstone on the full capstone path, to [row 144](preface.md#skill-navigation-row-144) for the Row 68 ↔ Row 64 book-loop meta audit on the opening-hinge capstone path alone, to [row 104](preface.md#skill-navigation-row-104) for the Row 68 ↔ Row 64 meta audit on the opening-hinge prelude path alone, to [row 163](preface.md#skill-navigation-row-163) for the Row 68 ↔ Row 63 meta audit on the opening-hinge capstone path alone, to [row 182](preface.md#skill-navigation-row-162) when Handshake 4b meta prelude capstone still lags after verified Handshake 4a meta prelude capstone on the full capstone path, to [row 83](preface.md#skill-navigation-row-83) for the Row 68 ↔ Row 63 opening prelude audit alone, to [row 63](preface.md#skill-navigation-row-63) for the Row 62 ↔ Row 43 meta audit alone, to [row 43](preface.md#skill-navigation-row-43) for the full Rows 17–42 → row 16 meta audit, or extend prose only under `writings/` then sync."
)
ROW183_TAIL_NEW = (
    "Read the [memory sheet row 183 baby picture](appendix/memory-sheet.md#row-183-baby-picture-row68-row163-orchestration-meta-prelude-capstone-reunion) when opening [row 184](preface.md#skill-navigation-row-184) before row 64 closes on the full capstone path; read the [epilogue row 183 closing loop](epilogue/multiscale.md#row-183-closing-loop) when the competence loop closes. When row 183 is complete, proceed to [row 184](preface.md#skill-navigation-row-184) when orchestration verifies individually but book-loop meta still feels disconnected from next-project restart after verified orchestration meta prelude capstone on the full capstone path, to [row 164](preface.md#skill-navigation-row-164) for the Row 68 ↔ Row 64 book-loop meta audit on the opening-hinge capstone path alone, to [row 144](preface.md#skill-navigation-row-144) for the Row 68 ↔ Row 64 book-loop meta audit on the opening-hinge capstone path alone, to [row 104](preface.md#skill-navigation-row-104) for the Row 68 ↔ Row 64 meta audit on the opening-hinge prelude path alone, to [row 163](preface.md#skill-navigation-row-163) for the Row 68 ↔ Row 63 meta audit on the opening-hinge capstone path alone, to [row 182](preface.md#skill-navigation-row-162) when Handshake 4b meta prelude capstone still lags after verified Handshake 4a meta prelude capstone on the full capstone path, to [row 83](preface.md#skill-navigation-row-83) for the Row 68 ↔ Row 63 opening prelude audit alone, to [row 63](preface.md#skill-navigation-row-63) for the Row 62 ↔ Row 43 meta audit alone, to [row 43](preface.md#skill-navigation-row-43) for the full Rows 17–42 → row 16 meta audit, or extend prose only under `writings/` then sync."
)


def main():
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "{#skill-navigation-row-184}" in preface and preface.index("{#skill-navigation-row-184}") < preface.index(copper):
        print("preface: row 184 already present")
    elif "{#skill-navigation-row-184}" in preface:
        raise SystemExit("preface row 184 exists but not at copper wire insert point")
    else:
        if "skill-navigation-row-183" not in preface:
            raise SystemExit("preface row 183 must exist before row 184")
        if ROW183_TAIL_OLD not in preface:
            raise SystemExit("preface row 183 tail not found")
        preface = preface.replace(ROW183_TAIL_OLD, ROW183_TAIL_NEW)
        preface = preface.replace(copper, "\n" + ROW184_PREFACE + copper)
        preface_path.write_text(preface)
        print("preface: added row 184")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "reunion (row 184) |" in prologue:
        print("prologue: row 184 already present")
    else:
        needle = "| Row 68 → Row 163 Row 68 → Row 63 orchestration meta prelude capstone reunion (row 183) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 183 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + PROLOGUE_COMPASS + prologue[line_end + 1 :]
        prologue = prologue.replace(
            "**Row 183 closing stitch",
            PROLOGUE_STITCH + "**Row 183 closing stitch",
        )
        prologue = prologue.replace(
            '| <span id="prologue-preview-row-183"></span>Row 183 preview',
            PROLOGUE_PREVIEW + '| <span id="prologue-preview-row-183"></span>Row 183 preview',
        )
        prologue = prologue.replace(
            "before row 184 book-loop meta prelude capstone reunion on the full capstone path (then row 145 second-pass meta p",
            "before row 185 second-pass meta prelude capstone reunion on the full capstone path (then row 165 second-pass meta p",
            1,
        )
        prologue_path.write_text(prologue)
        print("prologue: added row 184")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "### Row 184 closing loop" not in epilogue:
        old_proceed = (
            "Proceed to [row 184](#row-184-closing-loop) when row 68 closed but book-loop meta still feels disconnected after row 183 on the full capstone path,"
        )
        if old_proceed not in epilogue:
            old_proceed = (
                "Proceed to [row 164](#row-164-closing-loop) when row 68 closed but book-loop meta still feels disconnected after row 183 on the full capstone path,"
            )
            new_proceed = (
                "Proceed to [row 184](#row-184-closing-loop) when row 68 closed but book-loop meta still feels disconnected after row 183 on the full capstone path,"
            )
            if old_proceed not in epilogue:
                raise SystemExit("epilogue row 183 end marker not found")
            epilogue = epilogue.replace(old_proceed, new_proceed, 1)
        epilogue = epilogue.replace(
            "before row 184 book-loop meta prelude capstone reunion on the full capstone path (then row 164 on the capstone path).",
            "before row 185 second-pass meta prelude capstone reunion on the full capstone path (then row 165 on the capstone path).",
            1,
        )
        marker = "### Row 183 closing loop (Row 68 → Row 163 Row 68 → Row 63 orchestration meta prelude capstone reunion)"
        if marker not in epilogue:
            raise SystemExit("epilogue row 183 insert anchor not found")
        epilogue = epilogue.replace(marker, EPILOGUE_LOOP + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 184")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "| 184 | Row 68 → Row 164" not in sources:
        sources = sources.replace(
            "| 164 | Row 68 → Row 144 Row 68 → Row 64 book-loop meta prelude capstone",
            SOURCES_TABLE + "| 164 | Row 68 → Row 144 Row 68 → Row 64 book-loop meta prelude capstone",
        )
        sources = sources.replace(
            _src164_header,
            SOURCES_INDEX + _src164_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 184")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "### Row 184 baby picture" not in memory:
        memory = memory.replace(
            "| 183 | Meta | [Row 68 → Row 163 orchestration meta prelude capstone reunion index]",
            MEMORY_TABLE + "| 183 | Meta | [Row 68 → Row 163 orchestration meta prelude capstone reunion index]",
        )
        memory = memory.replace(
            _baby_anchor,
            MEMORY_BABY + _baby_anchor,
            1,
        )
        if ROW183_BABY_OLD in memory:
            memory = memory.replace(ROW183_BABY_OLD, ROW183_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 184")


if __name__ == "__main__":
    main()
