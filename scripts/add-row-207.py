#!/usr/bin/env python3
"""Add row 207 meta-stitch (Row 68 → Row 187 ↔ Row 67 part-boundary meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]


def t187_to_207(text: str) -> str:
    """Transform row-187 capstone-path meta copy to row 207 (187→207, 167→187 inner, 206 gate)."""
    out = text.replace("row 208", "__R208__")
    out = text.replace("row 207", "__R207__")
    repl = [
        ("Row 68 → Row 167 Row 68 → Row 67", "TEMP207TITLE"),
        (
            "row68-row167-part-boundary-meta-prelude-capstone-reunion-index-row-187",
            "TEMP207IDX",
        ),
        (
            "row-187-baby-picture-row68-row167-part-boundary-meta-prelude-capstone-reunion",
            "row-207-baby-picture-row68-row187-part-boundary-meta-prelude-capstone-reunion",
        ),
        ("skill-navigation-row-187", "TEMP207NAV"),
        ("prologue-preview-row-187", "prologue-preview-row-207"),
        ("row-187-closing-stitch", "row-207-closing-stitch"),
        ("row-187-closing-loop", "row-207-closing-loop"),
        ("Row 187 three-way audit", "Row 207 three-way audit"),
        (
            "[row 206](preface.md#skill-navigation-row-206) or [row 187](skill-navigation-row-187)",
            "[row 206](preface.md#skill-navigation-row-206) or [row 207](TEMP207NAV)",
        ),
        (
            "[row 186](preface.md#skill-navigation-row-186) or [row 187](skill-navigation-row-187)",
            "[row 206](preface.md#skill-navigation-row-206) or [row 207](TEMP207NAV)",
        ),
        (
            "[row 186](preface.md#skill-navigation-row-186) or [Row 68 → Row 187 part-boundary meta prelude capstone reunion index (row 187)](appendix/sources.md#row68-row167-part-boundary-meta-prelude-capstone-reunion-index-row-187)",
            "[row 206](preface.md#skill-navigation-row-206) or [Row 68 → Row 187 part-boundary meta prelude capstone reunion index (row 207)](appendix/sources.md#row68-row187-part-boundary-meta-prelude-capstone-reunion-index-row-207)",
        ),
        (
            "verified Writings canonical meta prelude capstone closure on the full capstone path (row 186)",
            "verified Writings canonical meta prelude capstone closure on the full capstone path (row 206)",
        ),
        (
            "before row 188 midpoint meta prelude capstone reunion opens on the full capstone path",
            "before row 208 midpoint meta prelude capstone reunion opens on the full capstone path",
        ),
        (
            "before row 188 midpoint meta prelude capstone opens on the full capstone path",
            "before row 208 midpoint meta prelude capstone opens on the full capstone path",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP207IDX",
        "row68-row187-part-boundary-meta-prelude-capstone-reunion-index-row-207",
    )
    out = out.replace("TEMP207NAV", "skill-navigation-row-207")
    out = out.replace("row 187", "row 207")
    out = out.replace("Row 187", "Row 207")
    out = out.replace("TEMP207TITLE", "Row 68 → Row 187 Row 68 → Row 67")
    out = out.replace("skill-navigation-row-187", "skill-navigation-row-207")
    out = out.replace(
        "[row 207](preface.md#skill-navigation-row-206)",
        "[row 206](preface.md#skill-navigation-row-206)",
    )
    out = out.replace(
        "[row 207](preface.md#skill-navigation-row-187)",
        "[row 187](preface.md#skill-navigation-row-187)",
    )
    out = out.replace("when row 206 closed", "when row 206 closed")
    out = out.replace("When row 206 closed", "When row 206 closed")
    out = out.replace("when row 186 closed", "when row 206 closed")
    out = out.replace("When row 186 closed", "When row 206 closed")
    out = out.replace("row 186 closed", "row 206 closed")
    out = out.replace("after row 206 alone", "after row 206 alone")
    out = out.replace("after row 186 alone", "after row 206 alone")
    out = out.replace("Recite [preface row 206]", "Recite [preface row 206]")
    out = out.replace("Recite [preface row 186]", "Recite [preface row 206]")
    out = out.replace("from row 206's", "from row 206's")
    out = out.replace("from row 186's", "from row 206's")
    out = out.replace("row 206 and row 67", "row 206 and row 67")
    out = out.replace("row 186 and row 67", "row 206 and row 67")
    out = out.replace("row 206 or row 167", "row 206 or row 187")
    out = out.replace("row 186 or row 167", "row 206 or row 187")
    out = out.replace("row 167", "row 187")
    out = out.replace("Row 167", "Row 187")
    out = out.replace(
        "row68-row147-part-boundary-meta-prelude-capstone-reunion-index-row-167",
        "row68-row167-part-boundary-meta-prelude-capstone-reunion-index-row-187",
    )
    out = out.replace(
        "row68-row167-part-boundary-meta-prelude-capstone-reunion-index-row-187",
        "row68-row187-part-boundary-meta-prelude-capstone-reunion-index-row-207",
    )
    out = out.replace("row 186", "row 206")
    out = out.replace("Row 186", "Row 206")
    out = out.replace("row 185", "row 205")
    out = out.replace("Row 185", "Row 205")
    out = out.replace("row 165", "row 185")
    out = out.replace("Row 165", "Row 185")
    out = out.replace("row 188", "row 208")
    out = out.replace("Row 188", "Row 208")
    out = out.replace("row 168", "row 188")
    out = out.replace("Row 168", "Row 188")
    out = out.replace("row 148", "row 168")
    out = out.replace("Row 148", "Row 168")
    out = out.replace("row 128", "row 148")
    out = out.replace("Row 128", "Row 148")
    out = out.replace("row 126", "row 146")
    out = out.replace("Row 126", "Row 146")
    out = out.replace("row 107", "row 127")
    out = out.replace("Row 107", "Row 127")
    out = out.replace(
        "row 207 names **Row 68 → Row 147 Row 68 → Row 67 part-boundary meta prelude capstone reunion**",
        "row 187 names **Row 68 → Row 167 Row 68 → Row 67 part-boundary meta prelude capstone reunion**",
    )
    out = out.replace("__R207__", "row 207")
    out = out.replace("__R208__", "row 208")
    return out


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    memory = (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text()

    start = preface.index("### Row 187 skill checkpoint")
    end = preface.index("\n\n### Row 188 skill checkpoint", start)
    row207_preface = t187_to_207(preface[start:end]) + "\n\n"

    spec187 = importlib.util.spec_from_file_location("add187", ROOT / "scripts/add-row-187.py")
    add187 = importlib.util.module_from_spec(spec187)
    spec187.loader.exec_module(add187)
    prologue_stitch = t187_to_207(add187.PROLOGUE_STITCH.strip()) + "\n\n"

    prologue_compass = (
        "| Row 68 → Row 187 Row 68 → Row 67 part-boundary meta prelude capstone reunion (row 207) | "
        "[Preface: row 207 skill checkpoint](../preface.md#skill-navigation-row-207) · "
        "[Row 68 → Row 187 part-boundary meta prelude capstone reunion index](../appendix/sources.md#row68-row187-part-boundary-meta-prelude-capstone-reunion-index-row-207) · "
        "[memory sheet row 207 baby picture](../appendix/memory-sheet.md#row-207-baby-picture-row68-row187-part-boundary-meta-prelude-capstone-reunion) · "
        "[prologue row 207 preview row](#prologue-preview-row-207); [prologue row 207 closing stitch](#row-207-closing-stitch); "
        "[epilogue row 207 closing loop](../epilogue/multiscale.md#row-207-closing-loop) — "
        "read row 68 gate + row 206 or row 187 Writings canonical meta prelude capstone / part-boundary meta prelude gate + V.4 Bridge → VI.0 twin-ladder landing + row 67 meta aloud "
        "when canonical tree is clean on the full capstone path but writings/fvm → writings/continuum feels like two courses after verified Writings meta prelude capstone on the full capstone path |\n"
    )

    prologue_preview = (
        '| <span id="prologue-preview-row-207"></span>Row 207 preview (Row 68 → Row 187 Row 68 → Row 67 part-boundary meta prelude capstone reunion) | '
        "Explain why midpoint closure (row 68) and part-boundary meta (row 67) must be read together with the V.4 → VI.0 twin-ladder Bridge chain "
        "after verified Writings canonical meta prelude capstone on the full capstone path before canonical sync and fvm → continuum subtrees feel like separate courses | "
        'One sentence: "read row 68 gate + row 206 or row 187 Writings canonical meta prelude capstone / part-boundary meta prelude gate + V.4 Bridge → VI.0 twin-ladder landing + row 67 meta aloud '
        "when canonical tree is clean on the full capstone path but writings/fvm → writings/continuum feels like two courses after verified Writings meta prelude capstone on the full capstone path\" — "
        "[preface row 207 skill checkpoint](../preface.md#skill-navigation-row-207); [prologue row 207 closing stitch](#row-207-closing-stitch); "
        "[Row 68 → Row 187 reunion index](../appendix/sources.md#row68-row187-part-boundary-meta-prelude-capstone-reunion-index-row-207); "
        "[memory sheet row 207 baby picture](../appendix/memory-sheet.md#row-207-baby-picture-row68-row187-part-boundary-meta-prelude-capstone-reunion); "
        "[V.4 Bridge](../part05-fvm/04-navier-stokes-cfd.md#bridge-to-part-vi); "
        "[preface row 67 skill checkpoint](../preface.md#skill-navigation-row-67); "
        "[preface row 206 skill checkpoint](../preface.md#skill-navigation-row-206); "
        "[epilogue row 207 closing loop](../epilogue/multiscale.md#row-207-closing-loop) |\n"
    )

    row187_loop_anchor = (
        "### Row 187 closing loop (Row 68 → Row 167 Row 68 → Row 67 "
        "part-boundary meta prelude capstone reunion) {#row-187-closing-loop}"
    )
    row188_loop_end = (
        "### Row 188 closing loop (Row 68 → Row 168 Row 68 → Row 48 "
        "midpoint meta prelude capstone reunion) {#row-188-closing-loop}"
    )
    epilogue_loop = t187_to_207(
        row187_loop_anchor
        + epilogue.split(row187_loop_anchor, 1)[1].split(row188_loop_end, 1)[0]
    )

    src187_header = (
        "## Row 68 → Row 167 Row 68 → Row 67 part-boundary meta prelude capstone reunion index (row 187)"
    )
    next188_header = (
        "## Row 68 → Row 168 Row 68 → Row 48 midpoint meta prelude capstone reunion index (row 188)"
    )
    sources_index = t187_to_207(sources.split(src187_header, 1)[1].split(next188_header, 1)[0])
    sources_index = (
        "## Row 68 → Row 187 Row 68 → Row 67 part-boundary meta prelude capstone reunion index (row 207) "
        "{#row68-row187-part-boundary-meta-prelude-capstone-reunion-index-row-207}"
        + sources_index
    )

    sources_table = next(
        line for line in sources.splitlines() if line.startswith("| 187 | Row 68 → Row 167")
    )
    sources_table = (
        t187_to_207(sources_table).replace("| 187 | Row 68 → Row 187", "| 207 | Row 68 → Row 187", 1)
        + "\n"
    )

    memory_table = next(
        line for line in memory.splitlines() if line.startswith("| 187 | Meta |")
    )
    memory_table = t187_to_207(memory_table).replace("| 187 | Meta |", "| 207 | Meta |", 1) + "\n"

    baby_anchor = "### Row 187 baby picture {#row-187-baby-picture-row68-row167-part-boundary-meta-prelude-capstone-reunion}"
    baby_end = "### Row 119 baby picture"
    memory_baby = t187_to_207(
        baby_anchor + memory.split(baby_anchor, 1)[1].split(baby_end, 1)[0]
    )
    memory_baby = memory_baby.replace(
        "### Row 207 baby picture {#row-207-baby-picture-row68-row187-part-boundary-meta-prelude-capstone-reunion}",
        "### Row 207 baby picture {#row-207-baby-picture-row68-row187-part-boundary-meta-prelude-capstone-reunion}",
        1,
    )

    return {
        "row207_preface": row207_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW206_TAIL_OLD = (
    "When row 206 is complete, proceed to [row 207](preface.md#skill-navigation-row-207) when row 68 closed but part-boundary meta prelude capstone still lags after verified Writings canonical meta prelude capstone on the full capstone path"
)
ROW206_TAIL_NEW = (
    "When row 206 is complete, proceed to [row 207](preface.md#skill-navigation-row-207) when row 68 closed but part-boundary meta prelude capstone still lags after verified Writings canonical meta prelude capstone on the full capstone path"
)

ROW206_EPILOGUE_OLD = (
    "Proceed to [row 187](#row-187-closing-loop) when row 68 closed but part-boundary meta prelude capstone still lags after row 206 on the full capstone path,"
)
ROW206_EPILOGUE_NEW = (
    "Proceed to [row 207](#row-207-closing-loop) when row 68 closed but part-boundary meta prelude capstone still lags after row 206 on the full capstone path,"
)

ROW206_BABY_OLD = (
    "before row 187 part-boundary meta prelude capstone reunion opens on the full capstone path"
)
ROW206_BABY_NEW = (
    "before row 207 part-boundary meta prelude capstone reunion opens on the full capstone path"
)


def main() -> None:
    b = _build_blocks()

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "### Row 207 skill checkpoint" in preface:
        print("preface: row 207 already present")
    else:
        if "### Row 206 skill checkpoint" not in preface:
            raise SystemExit("row 206 must exist before row 207")
        preface = preface.replace(copper, "\n" + b["row207_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 207")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "**Row 207 closing stitch" not in prologue:
        needle = "| Row 68 → Row 186 Row 68 → Row 66 Writings canonical meta prelude capstone reunion (row 206) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 206 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 207 closing stitch" not in prologue:
            prologue = prologue.replace(
                "**Row 206 closing stitch",
                b["prologue_stitch"] + "**Row 206 closing stitch",
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-206"></span>Row 206 preview'
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        prologue_path.write_text(prologue)
        print("prologue: added row 207")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "### Row 207 closing loop" not in epilogue:
        if ROW206_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW206_EPILOGUE_OLD, ROW206_EPILOGUE_NEW, 1)
        marker = "### Row 187 closing loop (Row 68 → Row 167 Row 68 → Row 67 part-boundary meta prelude capstone reunion)"
        if marker not in epilogue:
            raise SystemExit("epilogue row 187 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 207")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row187-part-boundary-meta-prelude-capstone-reunion-index-row-207" not in sources:
        sources = sources.replace(
            "| 187 | Row 68 → Row 167 Row 68 → Row 67 part-boundary meta prelude capstone",
            b["sources_table"] + "| 187 | Row 68 → Row 167 Row 68 → Row 67 part-boundary meta prelude capstone",
            1,
        )
        sources = sources.replace(
            src187_header := (
                "## Row 68 → Row 167 Row 68 → Row 67 part-boundary meta prelude capstone reunion index (row 187)"
            ),
            b["sources_index"] + src187_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 207")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-207-baby-picture-row68-row187" not in memory:
        memory = memory.replace(
            "| 187 | Meta | [Row 68 → Row 167 part-boundary meta prelude capstone reunion index]",
            b["memory_table"] + "| 187 | Meta | [Row 68 → Row 167 part-boundary meta prelude capstone reunion index]",
            1,
        )
        memory = memory.replace(
            baby_anchor := (
                "### Row 187 baby picture {#row-187-baby-picture-row68-row167-part-boundary-meta-prelude-capstone-reunion}"
            ),
            b["memory_baby"] + baby_anchor,
            1,
        )
        if ROW206_BABY_OLD in memory:
            memory = memory.replace(ROW206_BABY_OLD, ROW206_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 207")


if __name__ == "__main__":
    main()
