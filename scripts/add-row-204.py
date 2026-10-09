#!/usr/bin/env python3
"""Add row 204 meta-stitch (Row 68 → Row 184 ↔ Row 64 book-loop meta prelude capstone reunion, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def t184_to_204(text: str) -> str:
    """Transform row-184 capstone-path meta copy to row 204 (184→204, 164→184 inner, 203 gate)."""
    out = text.replace("row 205", "__R205__")
    out = out.replace("row 204", "__R204__")
    out = out.replace("row 203", "__R203__")
    repl = [
        ("Row 68 → Row 164 Row 68 → Row 64", "Row 68 → Row 184 Row 68 → Row 64"),
        (
            "row68-row144-book-loop-meta-prelude-capstone-reunion-index-row-164",
            "TEMP_ROW204_EXP_INDEX",
        ),
        (
            "row-164-baby-picture-row68-row144-book-loop-meta-prelude-capstone-reunion",
            "row-204-baby-picture-row68-row184-book-loop-meta-prelude-capstone-reunion",
        ),
        ("skill-navigation-row-184", "TEMP_SKILL_NAV_184"),
        ("prologue-preview-row-164", "prologue-preview-row-204"),
        ("row-164-closing-stitch", "row-204-closing-stitch"),
        ("row-184-closing-loop", "row-204-closing-loop"),
        ("Row 184 three-way audit", "Row 204 three-way audit"),
        (
            "[row 163](preface.md#skill-navigation-row-163) or [row 144](preface.md#skill-navigation-row-164)",
            "[row 203](preface.md#skill-navigation-row-203) or [row 183](preface.md#skill-navigation-row-183)",
        ),
        (
            "[row 163](preface.md#skill-navigation-row-163) or [Row 68 → Row 144 book-loop meta prelude capstone reunion index (row 144)](appendix/sources.md#row68-row124-book-loop-meta-prelude-capstone-reunion-index-row-144)",
            "[row 203](preface.md#skill-navigation-row-203) or [Row 68 → Row 184 book-loop meta prelude capstone reunion index (row 204)](appendix/sources.md#row68-row184-book-loop-meta-prelude-capstone-reunion-index-row-204)",
        ),
        (
            "verified orchestration meta prelude capstone closure (row 163)",
            "verified orchestration meta prelude capstone closure (row 203)",
        ),
        (
            "before row 185 second-pass meta prelude capstone opens on the full capstone path",
            "before row 205 second-pass meta prelude capstone opens on the full capstone path",
        ),
        (
            "before row 185 second-pass meta prelude capstone reunion on the full capstone path",
            "before row 205 second-pass meta prelude capstone reunion on the full capstone path",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW204_EXP_INDEX",
        "row68-row184-book-loop-meta-prelude-capstone-reunion-index-row-204",
    )
    out = out.replace("TEMP_SKILL_NAV_184", "skill-navigation-row-184")
    out = out.replace("Row 68 → Row 184 Row 68 → Row 64", "TEMP_ROW184_TITLE")
    out = out.replace(
        "**Row 164 closing stitch (Row 68 → Row 184",
        "**Row 204 closing stitch (Row 68 → Row 184",
    )
    out = out.replace("row 202 or row 164 recited", "row 203 or row 183 recited")
    out = out.replace("row 184", "row 204")
    out = out.replace("Row 184", "Row 204")
    out = out.replace("TEMP_ROW184_TITLE", "Row 68 → Row 184 Row 68 → Row 64")
    out = out.replace("skill-navigation-row-184", "skill-navigation-row-204")
    out = out.replace("[row 204](preface.md#skill-navigation-row-203)", "[row 203](preface.md#skill-navigation-row-203)")
    out = out.replace("[row 204](preface.md#skill-navigation-row-204)", "[row 204](preface.md#skill-navigation-row-204)")
    out = out.replace("[row 204](preface.md#skill-navigation-row-184)", "[row 184](preface.md#skill-navigation-row-184)")
    out = out.replace("[row 184](preface.md#skill-navigation-row-204)", "[row 184](preface.md#skill-navigation-row-184)")
    out = out.replace("when row 163 closed but row 64", "when row 203 closed but row 64")
    out = out.replace("row 2045", "row 203")
    out = out.replace("row 2046", "row 205")
    out = out.replace("row 204 or row 204", "row 203 or row 183")
    out = out.replace("When row 204 closed", "When row 203 closed")
    out = out.replace("after row 204 alone", "after row 203 alone")
    out = out.replace("When row 163 closed — orchestration", "When row 203 closed — orchestration")
    out = out.replace("When row 163 closed but row 64", "When row 203 closed but row 64")
    out = out.replace("row 163 or row 144 recited", "row 203 or row 183 recited")
    out = out.replace("when row 163 closed orchestration", "when row 203 closed orchestration")
    out = out.replace("after row 163 alone", "after row 203 alone")
    out = out.replace("from row 204's", "from row 203's")
    out = out.replace("row 163's orchestration meta", "row 203's orchestration meta")
    out = out.replace("row 163 and row 64", "row 203 and row 64")
    out = out.replace("Recite [preface row 163]", "Recite [preface row 203]")
    out = out.replace("row 144", "row 164")
    out = out.replace("Row 144", "Row 164")
    out = out.replace("row 124", "row 144")
    out = out.replace("Row 124", "Row 144")
    out = out.replace("row 104", "row 124")
    out = out.replace("Row 104", "Row 124")
    out = out.replace(
        "row68-row124-book-loop-meta-prelude-capstone-reunion-index-row-124",
        "row68-row144-book-loop-meta-prelude-capstone-reunion-index-row-144",
    )
    out = out.replace(
        "row68-row144-book-loop-meta-prelude-capstone-reunion-index-row-164",
        "row68-row184-book-loop-meta-prelude-capstone-reunion-index-row-204",
    )
    out = out.replace("row 163", "row 183")
    out = out.replace("Row 163", "Row 183")
    out = out.replace("row 162", "row 202")
    out = out.replace("Row 162", "Row 202")
    out = out.replace(
        "Row 68 → Row 204 book-loop meta prelude capstone reunion index",
        "Row 68 → Row 184 book-loop meta prelude capstone reunion index",
    )
    out = out.replace("__R203__", "row 203")
    out = out.replace("__R204__", "row 204")
    out = out.replace("__R205__", "row 205")
    return out


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    memory = (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text()

    start = preface.index("### Row 184 skill checkpoint")
    end = preface.index("\n\n### Row 185 skill checkpoint", start)
    row204_preface = t184_to_204(preface[start:end]) + "\n\n"

    row184_stitch = next(
        line
        for line in prologue.splitlines()
        if line.startswith("**Row 164 closing stitch") and "book-loop meta prelude capstone" in line
    )

    prologue_compass = (
        "| Row 68 → Row 184 Row 68 → Row 64 book-loop meta prelude capstone reunion (row 204) | "
        "[Preface: row 204 skill checkpoint](../preface.md#skill-navigation-row-204) · "
        "[Row 68 → Row 184 book-loop meta prelude capstone reunion index](../appendix/sources.md#row68-row184-book-loop-meta-prelude-capstone-reunion-index-row-204) · "
        "[memory sheet row 204 baby picture](../appendix/memory-sheet.md#row-204-baby-picture-row68-row184-book-loop-meta-prelude-capstone-reunion) · "
        "[prologue row 204 preview row](#prologue-preview-row-204); [prologue row 204 closing stitch](#row-204-closing-stitch); "
        "[epilogue row 204 closing loop](../epilogue/multiscale.md#row-204-closing-loop) — "
        "read row 68 gate + row 203 or row 183 orchestration meta prelude capstone / book-loop meta capstone gate + epilogue book-loop cross-links + row 64 meta aloud "
        "when orchestration verifies after orchestration meta prelude capstone on the full capstone path but the next terminal opens with copper decks copied blindly without reopening anchor rung audit |\n"
    )

    prologue_preview = (
        '| <span id="prologue-preview-row-204"></span>Row 204 preview (Row 68 → Row 184 Row 68 → Row 64 book-loop meta prelude capstone reunion) | '
        "Explain why midpoint closure (row 68) and book-loop meta (row 64) must be read together with the epilogue book-loop cross-links and restart chain after verified orchestration meta prelude capstone on the full capstone path before Act VI foundation and next-project restart feel like separate courses | "
        'One sentence: "read row 68 gate + row 203 or row 183 orchestration meta prelude capstone / book-loop meta capstone gate + epilogue book-loop cross-links + row 64 meta aloud when orchestration verifies after orchestration meta prelude capstone on the full capstone path but the next terminal opens with copper decks copied blindly without reopening anchor rung audit" — '
        "[preface row 204 skill checkpoint](../preface.md#skill-navigation-row-204); [prologue row 204 closing stitch](#row-204-closing-stitch); "
        "[Row 68 → Row 184 reunion index](../appendix/sources.md#row68-row184-book-loop-meta-prelude-capstone-reunion-index-row-204); "
        "[memory sheet row 204 baby picture](../appendix/memory-sheet.md#row-204-baby-picture-row68-row184-book-loop-meta-prelude-capstone-reunion); "
        "[preface row 203 skill checkpoint](../preface.md#skill-navigation-row-203); "
        "[epilogue row 204 closing loop](../epilogue/multiscale.md#row-204-closing-loop) |\n"
    )

    row184_loop_anchor = (
        "### Row 184 closing loop (Row 68 → Row 164 Row 68 → Row 64 "
        "book-loop meta prelude capstone reunion) {#row-184-closing-loop}"
    )
    row185_loop_end = (
        "### Row 185 closing loop (Row 68 → Row 165 Row 68 → Row 65 "
        "second-pass meta prelude capstone reunion) {#row-185-closing-loop}"
    )
    epilogue_loop = t184_to_204(
        row184_loop_anchor
        + epilogue.split(row184_loop_anchor, 1)[1].split(row185_loop_end, 1)[0]
    )

    src184_header = "## Row 68 → Row 164 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 184)"
    next185_header = (
        "## Row 68 → Row 165 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 185)"
    )
    sources_index = t184_to_204(sources.split(src184_header, 1)[1].split(next185_header, 1)[0])
    sources_index = (
        "## Row 68 → Row 184 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 204)"
        + sources_index
    )

    sources_table = next(
        line for line in sources.splitlines() if line.startswith("| 184 | Row 68 → Row 164")
    )
    sources_table = t184_to_204(sources_table).replace("| 184 | Row 68 → Row 184", "| 204 | Row 68 → Row 184", 1) + "\n"

    memory_table = next(
        line for line in memory.splitlines() if line.startswith("| 184 | Meta |")
    )
    memory_table = t184_to_204(memory_table).replace("| 184 | Meta |", "| 204 | Meta |", 1) + "\n"

    baby_anchor = (
        "### Row 184 baby picture (Row 68 → Row 164 Row 68 → Row 64 "
        "book-loop meta prelude capstone reunion)"
    )
    baby_end = "### Row 185 baby picture"
    memory_baby = t184_to_204(
        baby_anchor + memory.split(baby_anchor, 1)[1].split(baby_end, 1)[0]
    )

    return {
        "row204_preface": row204_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": t184_to_204(row184_stitch) + "\n\n",
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW203_TAIL_OLD = (
    "When row 203 is complete, proceed to [row 184](preface.md#skill-navigation-row-184) when orchestration verifies individually but book-loop meta still feels disconnected from next-project restart after verified orchestration meta prelude capstone on the full capstone path"
)
ROW203_TAIL_NEW = (
    "When row 203 is complete, proceed to [row 204](preface.md#skill-navigation-row-204) when orchestration verifies individually but book-loop meta still feels disconnected from next-project restart after verified orchestration meta prelude capstone on the full capstone path"
)

ROW203_EPILOGUE_OLD = (
    "Proceed to [row 184](#row-184-closing-loop) when row 68 closed but book-loop meta still feels disconnected after row 203 on the full capstone path,"
)
ROW203_EPILOGUE_NEW = (
    "Proceed to [row 204](#row-204-closing-loop) when row 68 closed but book-loop meta still feels disconnected after row 203 on the full capstone path,"
)

ROW203_BABY_OLD = (
    "row 203 when **epilogue orchestration cross-links and Row 62 → Row 43 meta must read on the same wire before row 184 book-loop meta prelude capstone reunion opens on the full capstone path**"
)
ROW203_BABY_NEW = (
    "row 203 when **epilogue orchestration cross-links and Row 62 → Row 43 meta must read on the same wire before row 204 book-loop meta prelude capstone reunion opens on the full capstone path**"
)


def main() -> None:
    b = _build_blocks()

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "### Row 204 skill checkpoint" in preface:
        print("preface: row 204 already present")
    else:
        if ROW203_TAIL_OLD not in preface:
            raise SystemExit("row 203 tail proceed marker not found")
        preface = preface.replace(ROW203_TAIL_OLD, ROW203_TAIL_NEW, 1)
        if "### Row 203 skill checkpoint" not in preface:
            raise SystemExit("row 203 must exist before row 204")
        preface = preface.replace(
            copper,
            "\n" + b["row204_preface"] + copper,
            1,
        )
        preface_path.write_text(preface)
        print("preface: added row 204")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "**Row 204 closing stitch" not in prologue:
        needle = "| Row 68 → Row 183 Row 68 → Row 63 orchestration meta prelude capstone reunion (row 203) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 203 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        prologue = prologue.replace(
            "**Row 203 closing stitch",
            b["prologue_stitch"] + "**Row 203 closing stitch",
            1,
        )
        preview_anchor = '| <span id="prologue-preview-row-203"></span>Row 203 preview'
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        prologue_path.write_text(prologue)
        print("prologue: added row 204")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "### Row 204 closing loop" not in epilogue:
        if ROW203_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW203_EPILOGUE_OLD, ROW203_EPILOGUE_NEW, 1)
        marker = "### Row 186 closing loop (Row 68 → Row 166 Row 68 → Row 66 Writings canonical meta prelude capstone reunion)"
        if marker not in epilogue:
            raise SystemExit("epilogue row 186 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 204")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row184-book-loop-meta-prelude-capstone-reunion-index-row-204" not in sources:
        sources = sources.replace(
            "| 184 | Row 68 → Row 164 Row 68 → Row 64 book-loop meta prelude capstone",
            b["sources_table"] + "| 184 | Row 68 → Row 164 Row 68 → Row 64 book-loop meta prelude capstone",
            1,
        )
        sources = sources.replace(
            src184_header := "## Row 68 → Row 164 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 184)",
            b["sources_index"] + src184_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 204")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-204-baby-picture-row68-row184" not in memory:
        memory = memory.replace(
            "| 184 | Meta | [Row 68 → Row 144 book-loop meta prelude capstone reunion index]",
            b["memory_table"] + "| 184 | Meta | [Row 68 → Row 144 book-loop meta prelude capstone reunion index]",
            1,
        )
        memory = memory.replace(
            "### Row 184 baby picture (Row 68 → Row 164 Row 68 → Row 64 book-loop meta prelude capstone reunion)",
            b["memory_baby"]
            + "### Row 184 baby picture (Row 68 → Row 164 Row 68 → Row 64 book-loop meta prelude capstone reunion)",
            1,
        )
        if ROW203_BABY_OLD in memory:
            memory = memory.replace(ROW203_BABY_OLD, ROW203_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 204")


if __name__ == "__main__":
    main()
