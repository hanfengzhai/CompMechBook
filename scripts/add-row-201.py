#!/usr/bin/env python3
"""Add row 201 meta-stitch (Row 68 → Row 181 ↔ Row 61 Handshake 4a meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def t181_to_201(text: str) -> str:
    """Transform row-181 capstone-path meta copy to row 201 (181→201, 161→181 inner, 200 gate)."""
    out = text.replace("row 202", "TEMP_ROW202")
    out = out.replace("row 201", "TEMP_ROW201")
    out = out.replace("row 200", "TEMP_ROW200")
    repl = [
        ("Row 68 → Row 161 Row 68 → Row 61", "Row 68 → Row 181 Row 68 → Row 61"),
        (
            "row68-row161-handshake4a-meta-prelude-capstone-reunion-index-row-181",
            "TEMP_ROW201_EXP_INDEX",
        ),
        (
            "row-181-baby-picture-row68-row161-handshake4a-meta-prelude-capstone-reunion",
            "row-201-baby-picture-row68-row181-handshake4a-meta-prelude-capstone-reunion",
        ),
        ("skill-navigation-row-181", "TEMP_SKILL_NAV_181"),
        ("prologue-preview-row-181", "prologue-preview-row-201"),
        ("row-181-closing-stitch", "row-201-closing-stitch"),
        ("row-181-closing-loop", "row-201-closing-loop"),
        ("Row 181 three-way audit", "Row 201 three-way audit"),
        (
            "[row 180](preface.md#skill-navigation-row-180) or [row 161](TEMP_SKILL_NAV_181)",
            "[row 200](preface.md#skill-navigation-row-200) or [row 181](TEMP_SKILL_NAV_181)",
        ),
        (
            "[row 180](preface.md#skill-navigation-row-180) or [Row 68 → Row 161 Handshake 4a meta prelude capstone reunion index (row 181)](appendix/sources.md#row68-row161-handshake4a-meta-prelude-capstone-reunion-index-row-181)",
            "[row 200](preface.md#skill-navigation-row-200) or [Row 68 → Row 181 Handshake 4a meta prelude capstone reunion index (row 201)](appendix/sources.md#row68-row181-handshake4a-meta-prelude-capstone-reunion-index-row-201)",
        ),
        (
            "verified Handshake 4a meta prelude capstone closure (row 180)",
            "verified Handshake 4a meta prelude capstone closure (row 200)",
        ),
        (
            "before row 182 Handshake 4b meta prelude capstone opens on the full capstone path",
            "before row 202 Handshake 4b meta prelude capstone opens on the full capstone path",
        ),
        (
            "before row 182 Handshake 4b meta prelude capstone reunion on the full capstone path",
            "before row 202 Handshake 4b meta prelude capstone reunion on the full capstone path",
        ),
        (
            "before row 162 Handshake 4b meta prelude capstone opens on the full capstone path",
            "before row 182 Handshake 4b meta prelude capstone opens on the full capstone path",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW201_EXP_INDEX",
        "row68-row181-handshake4a-meta-prelude-capstone-reunion-index-row-201",
    )
    out = out.replace("TEMP_SKILL_NAV_181", "skill-navigation-row-181")
    out = out.replace("Row 68 → Row 181 Row 68 → Row 61", "TEMP_ROW181_TITLE")
    out = out.replace("row 181", "row 201")
    out = out.replace("Row 181", "Row 201")
    out = out.replace("TEMP_ROW181_TITLE", "Row 68 → Row 181 Row 68 → Row 61")
    out = out.replace("skill-navigation-row-181", "skill-navigation-row-201")
    out = out.replace("[row 201](preface.md#skill-navigation-row-200)", "[row 200](preface.md#skill-navigation-row-200)")
    out = out.replace("[row 201](preface.md#skill-navigation-row-201)", "[row 201](preface.md#skill-navigation-row-201)")
    out = out.replace("[row 201](preface.md#skill-navigation-row-181)", "[row 181](preface.md#skill-navigation-row-181)")
    out = out.replace("[row 181](preface.md#skill-navigation-row-201)", "[row 181](preface.md#skill-navigation-row-181)")
    out = out.replace("when row 180 closed but row 61", "when row 200 closed but row 61")
    out = out.replace("[preface row 181](../preface.md#skill-navigation-row-201)", "[preface row 181](../preface.md#skill-navigation-row-181)")
    out = out.replace("row 201 or row 201", "row 200 or row 181")
    out = out.replace("When row 201 closed", "When row 200 closed")
    out = out.replace("after row 201 alone", "after row 200 alone")
    out = out.replace("Recite [preface row 201]", "Recite [preface row 200]")
    out = out.replace("row 201 or row 181 recited", "row 200 or row 181 recited")
    out = out.replace("When row 180 closed — Handshake 4a", "When row 200 closed — Handshake 4a")
    out = out.replace("row 180 or row 161 recited", "row 200 or row 181 recited")
    out = out.replace("row 180 or row 161 recited", "row 200 or row 181 recited")
    out = out.replace("when row 180 closed Handshake 4a", "when row 200 closed Handshake 4a")
    out = out.replace("after row 180 alone", "after row 200 alone")
    out = out.replace("from row 201's", "from row 200's")
    out = out.replace("row 180's epilogue rate", "row 200's epilogue rate")
    out = out.replace("row 180 and row 61", "row 200 and row 61")
    out = out.replace("Recite [preface row 180]", "Recite [preface row 200]")
    out = out.replace("row 161", "row 181")
    out = out.replace("Row 161", "Row 181")
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
        "row68-row161-handshake4a-meta-prelude-capstone-reunion-index-row-181",
        "row68-row181-handshake4a-meta-prelude-capstone-reunion-index-row-201",
    )
    out = out.replace(
        "[row 180](preface.md#skill-navigation-row-180) or [row 181]",
        "[row 200](preface.md#skill-navigation-row-200) or [row 181]",
    )
    out = out.replace("row 180", "row 200")
    out = out.replace("Row 180", "Row 200")
    out = out.replace("[row 200](preface.md#skill-navigation-row-200)", "[row 200](preface.md#skill-navigation-row-200)")
    out = out.replace("[row 200](preface.md#skill-navigation-row-181)", "[row 181](preface.md#skill-navigation-row-181)")
    out = out.replace(
        "Row 68 → Row 201 Handshake 4a meta prelude capstone reunion index",
        "Row 68 → Row 181 Handshake 4a meta prelude capstone reunion index",
    )
    out = out.replace(
        "[row 181](preface.md#skill-navigation-row-161)",
        "[row 181](preface.md#skill-navigation-row-181)",
    )
    out = out.replace("TEMP_ROW202", "row 202")
    out = out.replace("TEMP_ROW201", "row 201")
    out = out.replace("TEMP_ROW200", "row 200")
    return out


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    memory = (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text()

    start = preface.index("### Row 181 skill checkpoint")
    end = preface.index("\n\n### Row 182 skill checkpoint", start)
    row201_preface = t181_to_201(preface[start:end]) + "\n\n"

    row181_stitch = next(line for line in prologue.splitlines() if line.startswith("**Row 181 closing stitch"))

    prologue_compass = (
        "| Row 68 → Row 181 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion (row 201) | "
        "[Preface: row 201 skill checkpoint](../preface.md#skill-navigation-row-201) · "
        "[Row 68 → Row 181 Handshake 4a meta prelude capstone reunion index](../appendix/sources.md#row68-row181-handshake4a-meta-prelude-capstone-reunion-index-row-201) · "
        "[memory sheet row 201 baby picture](../appendix/memory-sheet.md#row-201-baby-picture-row68-row181-handshake4a-meta-prelude-capstone-reunion) · "
        "[prologue row 201 preview row](#prologue-preview-row-201); [prologue row 201 closing stitch](#row-201-closing-stitch); "
        "[epilogue row 201 closing loop](../epilogue/multiscale.md#row-201-closing-loop) — "
        "read row 68 gate + row 200 or row 181 Handshake 4a meta prelude capstone / Handshake 4a meta capstone gate + epilogue rate cross-links + row 61 meta aloud "
        "when bulk hardening parses at lab grip rate after verified Handshake 4a meta prelude capstone on the full capstone path but Handshake 4a still feels disconnected from Part VII |\n"
    )

    prologue_preview = (
        '| <span id="prologue-preview-row-201"></span>Row 201 preview (Row 68 → Row 181 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion) | '
        "Explain why midpoint closure (row 68) and Handshake 4a meta (row 61) must be read together with the epilogue rate cross-links and descent chain after verified Handshake 4a meta prelude capstone on the full capstone path before Act III pulling and Act IV hardening feel like separate courses | "
        'One sentence: "read row 68 gate + row 200 or row 181 Handshake 4a meta prelude capstone / Handshake 4a meta capstone gate + epilogue rate cross-links + row 61 meta aloud when bulk hardening parses at lab grip rate after verified Handshake 4a meta prelude capstone on the full capstone path but OpenDiS exports feed the plasticity deck without power-law extrapolation" — '
        "[preface row 201 skill checkpoint](../preface.md#skill-navigation-row-201); [prologue row 201 closing stitch](#row-201-closing-stitch); "
        "[Row 68 → Row 181 reunion index](../appendix/sources.md#row68-row181-handshake4a-meta-prelude-capstone-reunion-index-row-201); "
        "[memory sheet row 201 baby picture](../appendix/memory-sheet.md#row-201-baby-picture-row68-row181-handshake4a-meta-prelude-capstone-reunion); "
        "[preface row 200 skill checkpoint](../preface.md#skill-navigation-row-200); "
        "[epilogue row 201 closing loop](../epilogue/multiscale.md#row-201-closing-loop) |\n"
    )

    row181_loop_anchor = (
        "### Row 181 closing loop (Row 68 → Row 161 Row 68 → Row 61 "
        "Handshake 4a meta prelude capstone reunion) {#row-181-closing-loop}"
    )
    row181_loop_end = (
        "### Row 180 closing loop (Row 68 → Row 160 Row 68 → Row 60 "
        "Handshake 3 meta prelude capstone reunion) {#row-180-closing-loop}"
    )
    epilogue_loop = t181_to_201(
        row181_loop_anchor
        + epilogue.split(row181_loop_anchor, 1)[1].split(row181_loop_end, 1)[0]
    )

    src181_header = "## Row 68 → Row 161 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 181)"
    next181_header = "## Row 68 → Row 162 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion index (row 182)"
    sources_index = t181_to_201(sources.split(src181_header, 1)[1].split(next181_header, 1)[0])
    sources_index = (
        "## Row 68 → Row 181 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 201)"
        + sources_index
    )

    sources_table = next(
        line for line in sources.splitlines() if line.startswith("| 161 | Row 68 → Row 161")
    )
    sources_table = t181_to_201(sources_table).replace("| 161 | Row 68 → Row 161", "| 201 | Row 68 → Row 181", 1) + "\n"

    memory_table = next(
        line for line in memory.splitlines() if line.startswith("| 181 | Meta |")
    )
    memory_table = t181_to_201(memory_table).replace("| 181 | Meta |", "| 201 | Meta |", 1) + "\n"

    baby_anchor = (
        "### Row 181 baby picture (Row 68 → Row 161 Row 68 → Row 61 "
        "Handshake 4a meta prelude capstone reunion)"
    )
    baby_end = "### Row 190 baby picture"
    memory_baby = t181_to_201(
        baby_anchor + memory.split(baby_anchor, 1)[1].split(baby_end, 1)[0]
    )

    return {
        "row201_preface": row201_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": t181_to_201(row181_stitch) + "\n\n",
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_table": memory_table,
        "memory_baby": memory_baby,
    }


ROW200_TAIL_MARKER = "When row 200 is complete, proceed to [row 181](preface.md#skill-navigation-row-181)"

ROW200_EPILOGUE_OLD = (
    "Proceed to [row 181](#row-181-closing-loop) when row 68 closed but Handshake 4a meta still feels disconnected after row 200 on the full capstone path,"
)
ROW200_EPILOGUE_NEW = (
    "Proceed to [row 201](#row-201-closing-loop) when row 68 closed but Handshake 4a meta still feels disconnected after row 200 on the full capstone path,"
)

ROW200_EPILOGUE_BEFORE_OLD = (
    "before row 201 Handshake 4a meta prelude capstone reunion on the full capstone path (then row 181 Handshake 4a on the full capstone path)."
)
ROW200_EPILOGUE_BEFORE_NEW = (
    "before row 202 Handshake 4b meta prelude capstone reunion on the full capstone path (then row 182 Handshake 4b on the full capstone path)."
)


def main() -> None:
    b = _build_blocks()

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "### Row 201 skill checkpoint" in preface:
        print("preface: row 201 already present")
    else:
        if ROW200_TAIL_MARKER not in preface:
            raise SystemExit("row 200 tail proceed marker not found")
        preface = preface.replace(
            ROW200_TAIL_MARKER,
            "When row 200 is complete, proceed to [row 201](preface.md#skill-navigation-row-201)",
            1,
        )
        preface = preface.replace(copper, "\n" + b["row201_preface"] + copper)
        preface_path.write_text(preface)
        print("preface: added row 201")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "**Row 201 closing stitch" not in prologue:
        needle = "| Row 68 → Row 180 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion (row 200) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 200 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        prologue = prologue.replace(
            "**Row 200 closing stitch",
            b["prologue_stitch"] + "**Row 200 closing stitch",
            1,
        )
        preview_anchor = '| <span id="prologue-preview-row-200"></span>Row 200 preview'
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        prologue_path.write_text(prologue)
        print("prologue: added row 201")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "### Row 201 closing loop" not in epilogue:
        if ROW200_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW200_EPILOGUE_OLD, ROW200_EPILOGUE_NEW, 1)
        if ROW200_EPILOGUE_BEFORE_OLD in epilogue:
            epilogue = epilogue.replace(ROW200_EPILOGUE_BEFORE_OLD, ROW200_EPILOGUE_BEFORE_NEW, 1)
        marker = "### Row 186 closing loop (Row 68 → Row 166 Row 68 → Row 66 Writings canonical meta prelude capstone reunion)"
        if marker not in epilogue:
            raise SystemExit("epilogue row 186 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 201")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row181-handshake4a-meta-prelude-capstone-reunion-index-row-201" not in sources:
        sources = sources.replace(
            "| 200 | Row 68 → Row 180 Row 68 → Row 60 Handshake 3 meta prelude capstone",
            b["sources_table"] + "| 200 | Row 68 → Row 180 Row 68 → Row 60 Handshake 3 meta prelude capstone",
            1,
        )
        sources = sources.replace(
            src181_header := "## Row 68 → Row 161 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 181)",
            b["sources_index"] + src181_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 201")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-201-baby-picture-row68-row181" not in memory:
        memory = memory.replace(
            "| 200 | Meta | [Row 68 → Row 180 Handshake 3 meta prelude capstone reunion index]",
            b["memory_table"] + "| 200 | Meta | [Row 68 → Row 180 Handshake 3 meta prelude capstone reunion index]",
            1,
        )
        memory = memory.replace(
            "### Row 200 baby picture (Row 68 → Row 180 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion)",
            b["memory_baby"]
            + "### Row 200 baby picture (Row 68 → Row 180 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion)",
            1,
        )
        memory_path.write_text(memory)
        print("memory-sheet: added row 201")


if __name__ == "__main__":
    main()
