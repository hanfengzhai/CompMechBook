#!/usr/bin/env python3
"""Add row 205 meta-stitch (Row 68 → Row 185 ↔ Row 65 second-pass meta prelude capstone reunion, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def t185_to_205(text: str) -> str:
    """Transform row-185 capstone-path meta copy to row 205 (185→205, 165→185 inner, 204 gate)."""
    out = text.replace("row 206", "__R206__")
    out = text.replace("row 205", "__R205__")
    out = text.replace("row 204", "__R204__")
    repl = [
        ("Row 68 → Row 165 Row 68 → Row 65", "Row 68 → Row 185 Row 68 → Row 65"),
        (
            "row68-row145-second-pass-meta-prelude-capstone-reunion-index-row-165",
            "TEMP_ROW205_EXP_INDEX",
        ),
        (
            "row-165-baby-picture-row68-row145-second-pass-meta-prelude-capstone-reunion",
            "row-205-baby-picture-row68-row185-second-pass-meta-prelude-capstone-reunion",
        ),
        ("skill-navigation-row-185", "TEMP_SKILL_NAV_185"),
        ("prologue-preview-row-165", "prologue-preview-row-205"),
        ("row-165-closing-stitch", "row-205-closing-stitch"),
        ("row-185-closing-loop", "row-205-closing-loop"),
        ("Row 185 three-way audit", "Row 205 three-way audit"),
        (
            "[row 184](preface.md#skill-navigation-row-164) or [row 165](preface.md#skill-navigation-row-165)",
            "[row 204](preface.md#skill-navigation-row-204) or [row 185](preface.md#skill-navigation-row-185)",
        ),
        (
            "[row 184](preface.md#skill-navigation-row-144) or [Row 68 → Row 165 second-pass meta prelude capstone reunion index (row 165)](appendix/sources.md#row68-row145-second-pass-meta-prelude-capstone-reunion-index-row-165)",
            "[row 204](preface.md#skill-navigation-row-204) or [Row 68 → Row 185 second-pass meta prelude capstone reunion index (row 205)](appendix/sources.md#row68-row185-second-pass-meta-prelude-capstone-reunion-index-row-205)",
        ),
        (
            "verified book-loop meta prelude capstone closure (row 184)",
            "verified book-loop meta prelude capstone closure (row 204)",
        ),
        (
            "before row 186 Writings canonical meta prelude capstone opens on the full capstone path",
            "before row 206 Writings canonical meta prelude capstone opens on the full capstone path",
        ),
        (
            "before row 186 Writings canonical meta prelude capstone reunion on the full capstone path",
            "before row 206 Writings canonical meta prelude capstone reunion on the full capstone path",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW205_EXP_INDEX",
        "row68-row185-second-pass-meta-prelude-capstone-reunion-index-row-205",
    )
    out = out.replace("TEMP_SKILL_NAV_185", "skill-navigation-row-185")
    out = out.replace("Row 68 → Row 185 Row 68 → Row 65", "TEMP_ROW185_TITLE")
    out = out.replace(
        "**Row 165 closing stitch (Row 68 → Row 185",
        "**Row 205 closing stitch (Row 68 → Row 185",
    )
    out = out.replace("row 204 or row 184 recited", "row 204 or row 185 recited")
    out = out.replace("row 185", "row 205")
    out = out.replace("Row 185", "Row 205")
    out = out.replace("TEMP_ROW185_TITLE", "Row 68 → Row 185 Row 68 → Row 65")
    out = out.replace("skill-navigation-row-185", "skill-navigation-row-205")
    out = out.replace(
        "[row 205](preface.md#skill-navigation-row-204)",
        "[row 204](preface.md#skill-navigation-row-204)",
    )
    out = out.replace(
        "[row 205](preface.md#skill-navigation-row-205)",
        "[row 205](preface.md#skill-navigation-row-205)",
    )
    out = out.replace(
        "[row 205](preface.md#skill-navigation-row-185)",
        "[row 185](preface.md#skill-navigation-row-185)",
    )
    out = out.replace(
        "[row 185](preface.md#skill-navigation-row-205)",
        "[row 185](preface.md#skill-navigation-row-185)",
    )
    out = out.replace("when row 184 closed but row 65", "when row 204 closed but row 65")
    out = out.replace("row 2055", "row 204")
    out = out.replace("row 2056", "row 206")
    out = out.replace("row 205 or row 205", "row 204 or row 185")
    out = out.replace("When row 205 closed", "When row 204 closed")
    out = out.replace("after row 205 alone", "after row 204 alone")
    out = out.replace("When row 184 closed — book-loop", "When row 204 closed — book-loop")
    out = out.replace("When row 184 closed — second-pass", "When row 204 closed — second-pass")
    out = out.replace("row 184 closed book-loop", "row 204 closed book-loop")
    out = out.replace("row 184 closed second-pass", "row 204 closed second-pass")
    out = out.replace("after row 184 alone", "after row 204 alone")
    out = out.replace("Recite [preface row 205]", "Recite [preface row 204]")
    out = out.replace("row 204 or row 185 recited", "row 204 or row 185 recited")
    out = out.replace("from row 205's", "from row 204's")
    out = out.replace("row 184 and row 65", "row 204 and row 65")
    out = out.replace("Recite [preface row 184]", "Recite [preface row 204]")
    out = out.replace("row 165", "row 185")
    out = out.replace("Row 165", "Row 185")
    out = out.replace("row 145", "row 165")
    out = out.replace("Row 145", "Row 165")
    out = out.replace("row 125", "row 145")
    out = out.replace("Row 125", "Row 145")
    out = out.replace("row 105", "row 125")
    out = out.replace("Row 105", "Row 125")
    out = out.replace(
        "row68-row125-second-pass-meta-prelude-capstone-reunion-index-row-145",
        "row68-row145-second-pass-meta-prelude-capstone-reunion-index-row-165",
    )
    out = out.replace(
        "row68-row145-second-pass-meta-prelude-capstone-reunion-index-row-165",
        "row68-row185-second-pass-meta-prelude-capstone-reunion-index-row-205",
    )
    out = out.replace("row 184", "row 204")
    out = out.replace("Row 184", "Row 204")
    out = out.replace("row 164", "row 184")
    out = out.replace("Row 164", "Row 184")
    out = out.replace("row 144", "row 164")
    out = out.replace("Row 144", "Row 164")
    out = out.replace(
        "Row 68 → Row 205 second-pass meta prelude capstone reunion index",
        "Row 68 → Row 185 second-pass meta prelude capstone reunion index",
    )
    out = out.replace("__R204__", "row 204")
    out = out.replace("__R205__", "row 205")
    out = out.replace("__R206__", "row 206")
    return out


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    memory = (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text()

    start = preface.index("### Row 185 skill checkpoint")
    end = preface.index("\n\n### Row 186 skill checkpoint", start)
    row205_preface = t185_to_205(preface[start:end]) + "\n\n"

    row185_stitch = next(
        line
        for line in prologue.splitlines()
        if line.startswith("**Row 165 closing stitch") and "second-pass meta prelude capstone" in line
    )

    prologue_compass = (
        "| Row 68 → Row 185 Row 68 → Row 65 second-pass meta prelude capstone reunion (row 205) | "
        "[Preface: row 205 skill checkpoint](../preface.md#skill-navigation-row-205) · "
        "[Row 68 → Row 185 second-pass meta prelude capstone reunion index](../appendix/sources.md#row68-row185-second-pass-meta-prelude-capstone-reunion-index-row-205) · "
        "[memory sheet row 205 baby picture](../appendix/memory-sheet.md#row-205-baby-picture-row68-row185-second-pass-meta-prelude-capstone-reunion) · "
        "[prologue row 205 preview row](#prologue-preview-row-205); [prologue row 205 closing stitch](#row-205-closing-stitch); "
        "[epilogue row 205 closing loop](../epilogue/multiscale.md#row-205-closing-loop) — "
        "read row 68 gate + row 204 or row 185 book-loop meta prelude capstone / second-pass meta capstone gate + epilogue second-pass cross-links + row 65 meta aloud "
        "when the book loop closes on the full capstone path but every chapter boundary still opens a skill checkpoint instead of trusting Scene → Bridge rhythm |\n"
    )

    prologue_preview = (
        '| <span id="prologue-preview-row-205"></span>Row 205 preview (Row 68 → Row 185 Row 68 → Row 65 second-pass meta prelude capstone reunion) | '
        "Explain why midpoint closure (row 68) and second-pass meta (row 65) must be read together with the epilogue second-pass cross-links and continuous read-through guide after verified book-loop meta prelude capstone on the full capstone path before next-project restart and novel rhythm feel like separate courses | "
        'One sentence: "read row 68 gate + row 204 or row 185 book-loop meta prelude capstone / second-pass meta prelude gate + epilogue second-pass cross-links + row 65 meta aloud when the book loop closes on the full capstone path but every chapter boundary still opens a skill checkpoint instead of trusting Scene → Bridge rhythm" — '
        "[preface row 205 skill checkpoint](../preface.md#skill-navigation-row-205); [prologue row 205 closing stitch](#row-205-closing-stitch); "
        "[Row 68 → Row 185 reunion index](../appendix/sources.md#row68-row185-second-pass-meta-prelude-capstone-reunion-index-row-205); "
        "[memory sheet row 205 baby picture](../appendix/memory-sheet.md#row-205-baby-picture-row68-row185-second-pass-meta-prelude-capstone-reunion); "
        "[preface row 204 skill checkpoint](../preface.md#skill-navigation-row-204); "
        "[epilogue row 205 closing loop](../epilogue/multiscale.md#row-205-closing-loop) |\n"
    )

    row185_loop_anchor = (
        "### Row 185 closing loop (Row 68 → Row 165 Row 68 → Row 65 "
        "second-pass meta prelude capstone reunion) {#row-185-closing-loop}"
    )
    row186_loop_end = (
        "### Row 186 closing loop (Row 68 → Row 166 Row 68 → Row 66 "
        "Writings canonical meta prelude capstone reunion) {#row-186-closing-loop}"
    )
    epilogue_loop = t185_to_205(
        row185_loop_anchor
        + epilogue.split(row185_loop_anchor, 1)[1].split(row186_loop_end, 1)[0]
    )

    src185_header = "## Row 68 → Row 165 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 185)"
    next186_header = (
        "## Row 68 → Row 106 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 126)"
    )
    sources_index = t185_to_205(sources.split(src185_header, 1)[1].split(next186_header, 1)[0])
    sources_index = (
        "## Row 68 → Row 185 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 205)"
        + sources_index
    )

    sources_table = next(
        line for line in sources.splitlines() if line.startswith("| 185 | Row 68 → Row 165")
    )
    sources_table = (
        t185_to_205(sources_table).replace("| 185 | Row 68 → Row 185", "| 205 | Row 68 → Row 185", 1)
        + "\n"
    )

    memory_table = next(
        line for line in memory.splitlines() if line.startswith("| 204 | Meta |")
    )
    memory_table = t185_to_205(memory_table).replace("| 204 | Meta |", "| 205 | Meta |", 1) + "\n"

    baby_anchor = (
        "### Row 185 baby picture (Row 68 → Row 165 Row 68 → Row 65 "
        "second-pass meta prelude capstone reunion)"
    )
    baby_end = "### Row 204 baby picture"
    memory_baby = t185_to_205(
        baby_anchor + memory.split(baby_anchor, 1)[1].split(baby_end, 1)[0]
    )

    return {
        "row205_preface": row205_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": t185_to_205(row185_stitch) + "\n\n",
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW204_TAIL_OLD = (
    "When row 204 is complete, proceed to [row 185](preface.md#skill-navigation-row-185) when row 68 closed but second-pass meta still feels disconnected from novel rhythm after verified book-loop meta prelude capstone on the full capstone path"
)
ROW204_TAIL_NEW = (
    "When row 204 is complete, proceed to [row 205](preface.md#skill-navigation-row-205) when row 68 closed but second-pass meta still feels disconnected from novel rhythm after verified book-loop meta prelude capstone on the full capstone path"
)

ROW204_EPILOGUE_OLD = (
    "Proceed to [row 185](#row-185-closing-loop) when row 68 closed but second-pass meta capstone still lags after row 204 on the full capstone path,"
)
ROW204_EPILOGUE_NEW = (
    "Proceed to [row 205](#row-205-closing-loop) when row 68 closed but second-pass meta capstone still lags after row 204 on the full capstone path,"
)

ROW204_BABY_OLD = (
    "row 204 when **epilogue book-loop cross-links and Row 63 → Row 44 meta must read on the same wire before row 185 second-pass meta prelude capstone reunion opens on the full capstone path**"
)
ROW204_BABY_NEW = (
    "row 204 when **epilogue book-loop cross-links and Row 63 → Row 44 meta must read on the same wire before row 205 second-pass meta prelude capstone reunion opens on the full capstone path**"
)


def main() -> None:
    b = _build_blocks()

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "### Row 205 skill checkpoint" in preface:
        print("preface: row 205 already present")
    else:
        if ROW204_TAIL_OLD not in preface:
            raise SystemExit("row 204 tail proceed marker not found")
        preface = preface.replace(ROW204_TAIL_OLD, ROW204_TAIL_NEW, 1)
        if "### Row 204 skill checkpoint" not in preface:
            raise SystemExit("row 204 must exist before row 205")
        preface = preface.replace(copper, "\n" + b["row205_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 205")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "**Row 205 closing stitch" not in prologue:
        needle = "| Row 68 → Row 184 Row 68 → Row 64 book-loop meta prelude capstone reunion (row 204) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 204 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        prologue = prologue.replace(
            "**Row 204 closing stitch",
            b["prologue_stitch"] + "**Row 204 closing stitch",
            1,
        )
        preview_anchor = '| <span id="prologue-preview-row-204"></span>Row 204 preview'
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        prologue_path.write_text(prologue)
        print("prologue: added row 205")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "### Row 205 closing loop" not in epilogue:
        if ROW204_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW204_EPILOGUE_OLD, ROW204_EPILOGUE_NEW, 1)
        marker = "### Row 186 closing loop (Row 68 → Row 166 Row 68 → Row 66 Writings canonical meta prelude capstone reunion)"
        if marker not in epilogue:
            raise SystemExit("epilogue row 186 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 205")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row185-second-pass-meta-prelude-capstone-reunion-index-row-205" not in sources:
        sources = sources.replace(
            "| 185 | Row 68 → Row 165 Row 68 → Row 65 second-pass meta prelude capstone",
            b["sources_table"] + "| 185 | Row 68 → Row 165 Row 68 → Row 65 second-pass meta prelude capstone",
            1,
        )
        sources = sources.replace(
            src185_header := "## Row 68 → Row 165 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 185)",
            b["sources_index"] + src185_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 205")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-205-baby-picture-row68-row185" not in memory:
        memory = memory.replace(
            "| 204 | Meta | [Row 68 → Row 164 book-loop meta prelude capstone reunion index]",
            b["memory_table"] + "| 204 | Meta | [Row 68 → Row 164 book-loop meta prelude capstone reunion index]",
            1,
        )
        memory = memory.replace(
            "### Row 204 baby picture (Row 68 → Row 184 Row 68 → Row 64 book-loop meta prelude capstone reunion)",
            b["memory_baby"]
            + "### Row 204 baby picture (Row 68 → Row 184 Row 68 → Row 64 book-loop meta prelude capstone reunion)",
            1,
        )
        if ROW204_BABY_OLD in memory:
            memory = memory.replace(ROW204_BABY_OLD, ROW204_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 205")


if __name__ == "__main__":
    main()
