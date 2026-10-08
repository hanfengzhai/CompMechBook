#!/usr/bin/env python3
"""Add row 203 meta-stitch (Row 68 → Row 183 ↔ Row 63 orchestration meta prelude capstone reunion, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def t183_to_203(text: str) -> str:
    """Transform row-183 capstone-path meta copy to row 203 (183→203, 163→183 inner, 202 gate)."""
    out = text.replace("row 204", "__R204__")
    out = out.replace("row 203", "__R203__")
    out = out.replace("row 202", "__R202__")
    repl = [
        ("Row 68 → Row 163 Row 68 → Row 63", "Row 68 → Row 183 Row 68 → Row 63"),
        (
            "row68-row163-orchestration-meta-prelude-capstone-reunion-index-row-183",
            "TEMP_ROW203_EXP_INDEX",
        ),
        (
            "row-183-baby-picture-row68-row163-orchestration-meta-prelude-capstone-reunion",
            "row-203-baby-picture-row68-row183-orchestration-meta-prelude-capstone-reunion",
        ),
        ("skill-navigation-row-183", "TEMP_SKILL_NAV_183"),
        ("prologue-preview-row-183", "prologue-preview-row-203"),
        ("row-183-closing-stitch", "row-203-closing-stitch"),
        ("row-183-closing-loop", "row-203-closing-loop"),
        ("Row 183 three-way audit", "Row 203 three-way audit"),
        (
            "[row 182](preface.md#skill-navigation-row-182) or [row 163](TEMP_SKILL_NAV_183)",
            "[row 202](preface.md#skill-navigation-row-202) or [row 183](TEMP_SKILL_NAV_183)",
        ),
        (
            "[row 182](preface.md#skill-navigation-row-182) or [Row 68 → Row 163 orchestration meta prelude capstone reunion index (row 183)](appendix/sources.md#row68-row163-orchestration-meta-prelude-capstone-reunion-index-row-183)",
            "[row 202](preface.md#skill-navigation-row-202) or [Row 68 → Row 183 orchestration meta prelude capstone reunion index (row 203)](appendix/sources.md#row68-row183-orchestration-meta-prelude-capstone-reunion-index-row-203)",
        ),
        (
            "verified Handshake 4b meta prelude capstone closure (row 182)",
            "verified Handshake 4b meta prelude capstone closure (row 202)",
        ),
        (
            "before row 184 book-loop meta prelude capstone opens on the full capstone path",
            "before row 204 book-loop meta prelude capstone opens on the full capstone path",
        ),
        (
            "before row 184 book-loop meta prelude capstone reunion on the full capstone path",
            "before row 204 book-loop meta prelude capstone reunion on the full capstone path",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW203_EXP_INDEX",
        "row68-row183-orchestration-meta-prelude-capstone-reunion-index-row-203",
    )
    out = out.replace("TEMP_SKILL_NAV_183", "skill-navigation-row-183")
    out = out.replace("Row 68 → Row 183 Row 68 → Row 63", "TEMP_ROW183_TITLE")
    out = out.replace("row 183", "row 203")
    out = out.replace("Row 183", "Row 203")
    out = out.replace("TEMP_ROW183_TITLE", "Row 68 → Row 183 Row 68 → Row 63")
    out = out.replace("skill-navigation-row-183", "skill-navigation-row-203")
    out = out.replace("[row 203](preface.md#skill-navigation-row-202)", "[row 202](preface.md#skill-navigation-row-202)")
    out = out.replace("[row 203](preface.md#skill-navigation-row-203)", "[row 203](preface.md#skill-navigation-row-203)")
    out = out.replace("[row 203](preface.md#skill-navigation-row-183)", "[row 183](preface.md#skill-navigation-row-183)")
    out = out.replace("[row 183](preface.md#skill-navigation-row-203)", "[row 183](preface.md#skill-navigation-row-183)")
    out = out.replace("when row 182 closed but row 63", "when row 202 closed but row 63")
    out = out.replace("row 2033", "row 202")
    out = out.replace("row 2034", "row 204")
    out = out.replace("row 203 or row 203", "row 202 or row 183")
    out = out.replace("When row 203 closed", "When row 202 closed")
    out = out.replace("after row 203 alone", "after row 202 alone")
    out = out.replace("Recite [preface row 203]", "Recite [preface row 202]")
    out = out.replace("row 203 or row 183 recited", "row 202 or row 183 recited")
    out = out.replace("When row 182 closed — orchestration", "When row 202 closed — orchestration")
    out = out.replace("row 182 or row 163 recited", "row 202 or row 183 recited")
    out = out.replace("when row 182 closed orchestration", "when row 202 closed orchestration")
    out = out.replace("after row 182 alone", "after row 202 alone")
    out = out.replace("from row 203's", "from row 202's")
    out = out.replace("row 182's Handshake 4b meta", "row 202's Handshake 4b meta")
    out = out.replace("row 182 and row 63", "row 202 and row 63")
    out = out.replace("Recite [preface row 182]", "Recite [preface row 202]")
    out = out.replace("row 163", "row 183")
    out = out.replace("Row 163", "Row 183")
    out = out.replace("row 143", "row 163")
    out = out.replace("Row 143", "Row 163")
    out = out.replace("row 123", "row 143")
    out = out.replace("Row 123", "Row 143")
    out = out.replace(
        "row68-row143-orchestration-meta-prelude-capstone-reunion-index-row-163",
        "row68-row163-orchestration-meta-prelude-capstone-reunion-index-row-183",
    )
    out = out.replace(
        "row68-row163-orchestration-meta-prelude-capstone-reunion-index-row-183",
        "row68-row183-orchestration-meta-prelude-capstone-reunion-index-row-203",
    )
    out = out.replace(
        "[row 182](preface.md#skill-navigation-row-182) or [row 183]",
        "[row 202](preface.md#skill-navigation-row-202) or [row 183]",
    )
    out = out.replace("row 182", "row 202")
    out = out.replace("Row 182", "Row 202")
    out = out.replace(
        "Row 68 → Row 203 orchestration meta prelude capstone reunion index",
        "Row 68 → Row 183 orchestration meta prelude capstone reunion index",
    )
    out = out.replace("__R202__", "row 202")
    out = out.replace("__R203__", "row 203")
    out = out.replace("__R204__", "row 204")
    return out


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    memory = (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text()

    start = preface.index("### Row 183 skill checkpoint")
    end = preface.index("\n\n### Row 184 skill checkpoint", start)
    row203_preface = t183_to_203(preface[start:end]) + "\n\n"

    row183_stitch = next(line for line in prologue.splitlines() if line.startswith("**Row 183 closing stitch"))

    prologue_compass = (
        "| Row 68 → Row 183 Row 68 → Row 63 orchestration meta prelude capstone reunion (row 203) | "
        "[Preface: row 203 skill checkpoint](../preface.md#skill-navigation-row-203) · "
        "[Row 68 → Row 183 orchestration meta prelude capstone reunion index](../appendix/sources.md#row68-row183-orchestration-meta-prelude-capstone-reunion-index-row-203) · "
        "[memory sheet row 203 baby picture](../appendix/memory-sheet.md#row-203-baby-picture-row68-row183-orchestration-meta-prelude-capstone-reunion) · "
        "[prologue row 203 preview row](#prologue-preview-row-203); [prologue row 203 closing stitch](#row-203-closing-stitch); "
        "[epilogue row 203 closing loop](../epilogue/multiscale.md#row-203-closing-loop) — "
        "read row 68 gate + row 202 or row 183 Handshake 4b meta prelude capstone / orchestration meta capstone gate + epilogue orchestration cross-links + row 63 meta aloud "
        "when Handshakes 1–4b verify individually after Handshake 4b meta prelude capstone on the full capstone path but Act V notch and Act VI foundation still feel like separate afternoons without orchestrated `multiscale_export.yaml` |\n"
    )

    prologue_preview = (
        '| <span id="prologue-preview-row-203"></span>Row 203 preview (Row 68 → Row 183 Row 68 → Row 63 orchestration meta prelude capstone reunion) | '
        "Explain why midpoint closure (row 68) and orchestration meta (row 63) must be read together with the epilogue orchestration cross-links and H1→OUT chain after verified Handshake 4b meta prelude capstone on the full capstone path before Act V notch and Act VI foundation feel like separate courses | "
        'One sentence: "read row 68 gate + row 202 or row 183 Handshake 4b meta prelude capstone / orchestration meta capstone gate + epilogue orchestration cross-links + row 63 meta aloud when Handshakes 1–4b verify individually after Handshake 4b meta prelude capstone on the full capstone path but multiscale exports feed the book-loop deck without H1→OUT pedigree" — '
        "[preface row 203 skill checkpoint](../preface.md#skill-navigation-row-203); [prologue row 203 closing stitch](#row-203-closing-stitch); "
        "[Row 68 → Row 183 reunion index](../appendix/sources.md#row68-row183-orchestration-meta-prelude-capstone-reunion-index-row-203); "
        "[memory sheet row 203 baby picture](../appendix/memory-sheet.md#row-203-baby-picture-row68-row183-orchestration-meta-prelude-capstone-reunion); "
        "[preface row 202 skill checkpoint](../preface.md#skill-navigation-row-202); "
        "[epilogue row 203 closing loop](../epilogue/multiscale.md#row-203-closing-loop) |\n"
    )

    row183_loop_anchor = (
        "### Row 183 closing loop (Row 68 → Row 163 Row 68 → Row 63 "
        "orchestration meta prelude capstone reunion) {#row-183-closing-loop}"
    )
    row184_loop_end = (
        "### Row 184 closing loop (Row 68 → Row 164 Row 68 → Row 64 "
        "book-loop meta prelude capstone reunion) {#row-184-closing-loop}"
    )
    epilogue_loop = t183_to_203(
        row183_loop_anchor
        + epilogue.split(row183_loop_anchor, 1)[1].split(row184_loop_end, 1)[0]
    )

    src183_header = "## Row 68 → Row 163 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 183)"
    next184_header = "## Row 68 → Row 164 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 184)"
    sources_index = t183_to_203(sources.split(src183_header, 1)[1].split(next184_header, 1)[0])
    sources_index = (
        "## Row 68 → Row 183 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 203)"
        + sources_index
    )

    sources_table = next(
        line for line in sources.splitlines() if line.startswith("| 183 | Row 68 → Row 163")
    )
    sources_table = t183_to_203(sources_table).replace("| 183 | Row 68 → Row 183", "| 203 | Row 68 → Row 183", 1) + "\n"

    memory_table = next(
        line for line in memory.splitlines() if line.startswith("| 202 | Meta |")
    )
    memory_table = t183_to_203(memory_table).replace("| 202 | Meta |", "| 203 | Meta |", 1) + "\n"

    baby_anchor = (
        "### Row 183 baby picture (Row 68 → Row 163 Row 68 → Row 63 "
        "orchestration meta prelude capstone reunion)"
    )
    baby_end = "### Row 184 baby picture"
    memory_baby = t183_to_203(
        baby_anchor + memory.split(baby_anchor, 1)[1].split(baby_end, 1)[0]
    )

    return {
        "row203_preface": row203_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": t183_to_203(row183_stitch) + "\n\n",
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_table": memory_table,
        "memory_baby": memory_baby,
    }


ROW202_TAIL_MARKER = "When row 202 is complete, proceed to [row 183](preface.md#skill-navigation-row-183)"

ROW202_EPILOGUE_OLD = (
    "Proceed to [row 183](#row-183-closing-loop) when row 68 closed but orchestration meta still feels disconnected after row 202 on the full capstone path,"
)
ROW202_EPILOGUE_NEW = (
    "Proceed to [row 203](#row-203-closing-loop) when row 68 closed but orchestration meta still feels disconnected after row 202 on the full capstone path,"
)

ROW202_BABY_OLD = (
    "row 202 when **epilogue FE² cross-links and Row 61 → Row 42 Handshake 4b meta must read on the same wire before row 203 orchestration meta prelude capstone reunion opens on the full capstone path**"
)
ROW202_BABY_NEW = ROW202_BABY_OLD


def main() -> None:
    b = _build_blocks()

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "### Row 203 skill checkpoint" in preface:
        print("preface: row 203 already present")
    else:
        if ROW202_TAIL_MARKER not in preface:
            raise SystemExit("row 202 tail proceed marker not found")
        preface = preface.replace(
            ROW202_TAIL_MARKER,
            "When row 202 is complete, proceed to [row 203](preface.md#skill-navigation-row-203)",
            1,
        )
        preface = preface.replace(copper, "\n" + b["row203_preface"] + copper)
        preface_path.write_text(preface)
        print("preface: added row 203")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "**Row 203 closing stitch" not in prologue:
        needle = "| Row 68 → Row 182 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion (row 202) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 202 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        prologue = prologue.replace(
            "**Row 183 closing stitch",
            b["prologue_stitch"] + "**Row 183 closing stitch",
            1,
        )
        preview_anchor = '| <span id="prologue-preview-row-183"></span>Row 183 preview'
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        prologue_path.write_text(prologue)
        print("prologue: added row 203")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "### Row 203 closing loop" not in epilogue:
        if ROW202_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW202_EPILOGUE_OLD, ROW202_EPILOGUE_NEW, 1)
        marker = "### Row 186 closing loop (Row 68 → Row 166 Row 68 → Row 66 Writings canonical meta prelude capstone reunion)"
        if marker not in epilogue:
            raise SystemExit("epilogue row 186 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 203")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row183-orchestration-meta-prelude-capstone-reunion-index-row-203" not in sources:
        sources = sources.replace(
            "| 202 | Row 68 → Row 182 Row 68 → Row 62 Handshake 4b meta prelude capstone",
            b["sources_table"] + "| 202 | Row 68 → Row 182 Row 68 → Row 62 Handshake 4b meta prelude capstone",
            1,
        )
        sources = sources.replace(
            src183_header := "## Row 68 → Row 163 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 183)",
            b["sources_index"] + src183_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 203")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-203-baby-picture-row68-row183" not in memory:
        memory = memory.replace(
            "| 202 | Meta | [Row 68 → Row 182 Handshake 4b meta prelude capstone reunion index]",
            b["memory_table"] + "| 202 | Meta | [Row 68 → Row 182 Handshake 4b meta prelude capstone reunion index]",
            1,
        )
        memory = memory.replace(
            "### Row 183 baby picture (Row 68 → Row 163 Row 68 → Row 63 orchestration meta prelude capstone reunion)",
            b["memory_baby"]
            + "### Row 183 baby picture (Row 68 → Row 163 Row 68 → Row 63 orchestration meta prelude capstone reunion)",
            1,
        )
        if ROW202_BABY_OLD in memory and ROW202_BABY_OLD != ROW202_BABY_NEW:
            memory = memory.replace(ROW202_BABY_OLD, ROW202_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 203")


if __name__ == "__main__":
    main()
