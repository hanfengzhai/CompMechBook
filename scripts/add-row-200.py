#!/usr/bin/env python3
"""Add row 200 meta-stitch (Row 68 → Row 180 ↔ Row 60 Handshake 3 meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def t180_to_200(text: str) -> str:
    """Transform row-180 capstone-path meta copy to row 200 (180→200, 160→180 inner, 199 gate)."""
    out = text.replace("row 201", "TEMP_ROW201")
    out = out.replace("row 200", "TEMP_ROW200")
    out = out.replace("row 199", "TEMP_ROW199")
    repl = [
        ("Row 68 → Row 160 Row 68 → Row 60", "Row 68 → Row 180 Row 68 → Row 60"),
        (
            "row68-row160-handshake3-meta-prelude-capstone-reunion-index-row-180",
            "TEMP_ROW200_EXP_INDEX",
        ),
        (
            "row-180-baby-picture-row68-row160-handshake3-meta-prelude-capstone-reunion",
            "row-200-baby-picture-row68-row180-handshake3-meta-prelude-capstone-reunion",
        ),
        ("skill-navigation-row-180", "TEMP_SKILL_NAV_180"),
        ("prologue-preview-row-180", "prologue-preview-row-200"),
        ("row-180-closing-stitch", "row-200-closing-stitch"),
        ("row-180-closing-loop", "row-200-closing-loop"),
        ("Row 180 three-way audit", "Row 200 three-way audit"),
        (
            "[row 179](preface.md#skill-navigation-row-179) or [row 160](TEMP_SKILL_NAV_180)",
            "[row 199](preface.md#skill-navigation-row-199) or [row 180](TEMP_SKILL_NAV_180)",
        ),
        (
            "[row 179](preface.md#skill-navigation-row-179) or [Row 68 → Row 160 Handshake 3 meta prelude capstone reunion index (row 180)](appendix/sources.md#row68-row160-handshake3-meta-prelude-capstone-reunion-index-row-180)",
            "[row 199](preface.md#skill-navigation-row-199) or [Row 68 → Row 180 Handshake 3 meta prelude capstone reunion index (row 200)](appendix/sources.md#row68-row180-handshake3-meta-prelude-capstone-reunion-index-row-200)",
        ),
        (
            "verified Handshake 3 meta prelude capstone closure (row 179)",
            "verified Handshake 3 meta prelude capstone closure (row 199)",
        ),
        (
            "before row 181 Handshake 4a meta prelude capstone opens on the full capstone path",
            "before row 201 Handshake 4a meta prelude capstone opens on the full capstone path",
        ),
        (
            "before row 181 Handshake 4a meta prelude capstone reunion on the full capstone path",
            "before row 201 Handshake 4a meta prelude capstone reunion on the full capstone path",
        ),
        (
            "before row 161 Handshake 4a meta prelude capstone opens on the full capstone path",
            "before row 181 Handshake 4a meta prelude capstone opens on the full capstone path",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW200_EXP_INDEX",
        "row68-row180-handshake3-meta-prelude-capstone-reunion-index-row-200",
    )
    out = out.replace("TEMP_SKILL_NAV_180", "skill-navigation-row-180")
    out = out.replace("Row 68 → Row 180 Row 68 → Row 60", "TEMP_ROW180_TITLE")
    out = out.replace("row 180", "row 200")
    out = out.replace("Row 180", "Row 200")
    out = out.replace("TEMP_ROW180_TITLE", "Row 68 → Row 180 Row 68 → Row 60")
    out = out.replace("skill-navigation-row-180", "skill-navigation-row-200")
    out = out.replace("[row 200](preface.md#skill-navigation-row-199)", "[row 199](preface.md#skill-navigation-row-199)")
    out = out.replace("[row 200](preface.md#skill-navigation-row-200)", "[row 200](preface.md#skill-navigation-row-200)")
    out = out.replace("[row 200](preface.md#skill-navigation-row-180)", "[row 180](preface.md#skill-navigation-row-180)")
    out = out.replace("[row 180](preface.md#skill-navigation-row-200)", "[row 180](preface.md#skill-navigation-row-180)")
    out = out.replace("when row 179 closed but row 60", "when row 199 closed but row 60")
    out = out.replace("[preface row 180](../preface.md#skill-navigation-row-200)", "[preface row 180](../preface.md#skill-navigation-row-180)")
    out = out.replace("row 200 or row 200", "row 199 or row 180")
    out = out.replace("When row 200 closed", "When row 199 closed")
    out = out.replace("after row 200 alone", "after row 199 alone")
    out = out.replace("Recite [preface row 200]", "Recite [preface row 199]")
    out = out.replace("row 200 or row 180 recited", "row 199 or row 180 recited")
    out = out.replace("When row 179 closed — Handshake", "When row 199 closed — Handshake")
    out = out.replace("row 178 or row 159 recited", "row 198 or row 179 recited")
    out = out.replace("row 179 or row 160 recited", "row 199 or row 180 recited")
    out = out.replace("when row 179 closed Handshake", "when row 199 closed Handshake")
    out = out.replace("after row 179 alone", "after row 199 alone")
    out = out.replace("from row 200's", "from row 199's")
    out = out.replace("row 179's foundation", "row 199's foundation")
    out = out.replace("row 179's quasiharmonic", "row 199's quasiharmonic")
    out = out.replace("row 179 and row 60", "row 199 and row 60")
    out = out.replace("Recite [preface row 179]", "Recite [preface row 199]")
    out = out.replace("row 160", "row 180")
    out = out.replace("Row 160", "Row 180")
    out = out.replace("row 140", "row 160")
    out = out.replace("Row 140", "Row 160")
    out = out.replace("row 120", "row 140")
    out = out.replace("Row 120", "Row 140")
    out = out.replace(
        "row68-row140-handshake3-meta-prelude-capstone-reunion-index-row-160",
        "row68-row160-handshake3-meta-prelude-capstone-reunion-index-row-180",
    )
    out = out.replace(
        "row68-row160-handshake3-meta-prelude-capstone-reunion-index-row-180",
        "row68-row180-handshake3-meta-prelude-capstone-reunion-index-row-200",
    )
    out = out.replace(
        "[row 179](preface.md#skill-navigation-row-179) or [row 180]",
        "[row 199](preface.md#skill-navigation-row-199) or [row 180]",
    )
    out = out.replace("row 179", "row 199")
    out = out.replace("Row 179", "Row 199")
    out = out.replace("[row 199](preface.md#skill-navigation-row-199)", "[row 199](preface.md#skill-navigation-row-199)")
    out = out.replace("[row 199](preface.md#skill-navigation-row-180)", "[row 180](preface.md#skill-navigation-row-180)")
    out = out.replace(
        "Row 68 → Row 200 Handshake 3 meta prelude capstone reunion index",
        "Row 68 → Row 180 Handshake 3 meta prelude capstone reunion index",
    )
    out = out.replace(
        "[row 180](preface.md#skill-navigation-row-160)",
        "[row 180](preface.md#skill-navigation-row-180)",
    )
    out = out.replace("TEMP_ROW201", "row 201")
    out = out.replace("TEMP_ROW200", "row 200")
    out = out.replace("TEMP_ROW199", "row 199")
    return out


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    memory = (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text()

    start = preface.index("### Row 180 skill checkpoint")
    end = preface.index("\n\n### Row 181 skill checkpoint", start)
    row200_preface = t180_to_200(preface[start:end]) + "\n\n"

    row180_stitch = next(line for line in prologue.splitlines() if line.startswith("**Row 180 closing stitch"))

    prologue_compass = (
        "| Row 68 → Row 180 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion (row 200) | "
        "[Preface: row 200 skill checkpoint](../preface.md#skill-navigation-row-200) · "
        "[Row 68 → Row 180 Handshake 3 meta prelude capstone reunion index](../appendix/sources.md#row68-row180-handshake3-meta-prelude-capstone-reunion-index-row-200) · "
        "[memory sheet row 200 baby picture](../appendix/memory-sheet.md#row-200-baby-picture-row68-row180-handshake3-meta-prelude-capstone-reunion) · "
        "[prologue row 200 preview row](#prologue-preview-row-200); [prologue row 200 closing stitch](#row-200-closing-stitch); "
        "[epilogue row 200 closing loop](../epilogue/multiscale.md#row-200-closing-loop) — "
        "read row 68 gate + row 199 or row 180 Handshake 3 meta prelude capstone / Handshake 3 meta capstone gate + epilogue α cross-links + row 60 meta aloud "
        "when load cell parses at \\(T_w\\) after verified Handshake 3 meta prelude capstone on the full capstone path but Handshake 3 still feels disconnected from Parts III–VI |\n"
    )

    prologue_preview = (
        '| <span id="prologue-preview-row-200"></span>Row 200 preview (Row 68 → Row 180 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion) | '
        "Explain why midpoint closure (row 68) and Handshake 3 meta (row 60) must be read together with the epilogue α cross-links and ascent chain after verified Handshake 3 meta prelude capstone on the full capstone path before Act II warming and Act III pulling feel like separate courses | "
        'One sentence: "read row 68 gate + row 199 or row 180 Handshake 3 meta prelude capstone / Handshake 3 meta capstone gate + epilogue α cross-links + row 60 meta aloud when load cell parses at \\(T_w\\) after verified Handshake 3 meta prelude capstone on the full capstone path but Handshake 3 still feels disconnected from Parts III–VI" — '
        "[preface row 200 skill checkpoint](../preface.md#skill-navigation-row-200); [prologue row 200 closing stitch](#row-200-closing-stitch); "
        "[Row 68 → Row 180 reunion index](../appendix/sources.md#row68-row180-handshake3-meta-prelude-capstone-reunion-index-row-200); "
        "[memory sheet row 200 baby picture](../appendix/memory-sheet.md#row-200-baby-picture-row68-row180-handshake3-meta-prelude-capstone-reunion); "
        "[preface row 199 skill checkpoint](../preface.md#skill-navigation-row-199); "
        "[epilogue row 200 closing loop](../epilogue/multiscale.md#row-200-closing-loop) |\n"
    )

    epilogue_loop = t180_to_200(
        "### Row 180 closing loop"
        + epilogue.split("### Row 180 closing loop")[1].split("### Row 181 closing loop")[0]
    )

    src180_header = "## Row 68 → Row 160 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 180)"
    next180_header = "## Row 68 → Row 121 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 141)"
    sources_index = t180_to_200(sources.split(src180_header, 1)[1].split(next180_header, 1)[0])
    sources_index = (
        "## Row 68 → Row 180 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 200)"
        + sources_index
    )

    sources_table = next(
        line for line in sources.splitlines() if line.startswith("| 180 | Row 68 → Row 160")
    )
    sources_table = t180_to_200(sources_table).replace("| 180 | Row 68 → Row 180", "| 200 | Row 68 → Row 180", 1) + "\n"

    memory_table = next(
        line for line in memory.splitlines() if line.startswith("| 180 | Meta |")
    )
    memory_table = t180_to_200(memory_table).replace("| 180 | Meta |", "| 200 | Meta |", 1) + "\n"

    baby_anchor = (
        "### Row 180 baby picture (Row 68 → Row 160 Row 68 → Row 60 "
        "Handshake 3 meta prelude capstone reunion)"
    )
    memory_baby = t180_to_200(memory.split(baby_anchor, 1)[1].split("### Row 181 baby picture")[0])
    memory_baby = (
        "### Row 200 baby picture (Row 68 → Row 180 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion)"
        + memory_baby.split(")", 1)[1]
    )

    return {
        "row200_preface": row200_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": t180_to_200(row180_stitch) + "\n\n",
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_table": memory_table,
        "memory_baby": memory_baby,
    }


ROW199_TAIL_MARKER = "When row 199 is complete, proceed to [row 180](preface.md#skill-navigation-row-180)"

ROW199_EPILOGUE_OLD = (
    "Proceed to [row 180](#row-180-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 199 on the full capstone path,"
)
ROW199_EPILOGUE_NEW = (
    "Proceed to [row 200](#row-200-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 199 on the full capstone path,"
)

ROW199_EPILOGUE_BEFORE_OLD = (
    "before row 200 Handshake 3 meta prelude capstone reunion on the full capstone path (then row 161 Handshake 4a on the full capstone path)."
)
ROW199_EPILOGUE_BEFORE_NEW = (
    "before row 201 Handshake 4a meta prelude capstone reunion on the full capstone path (then row 181 Handshake 4a on the full capstone path)."
)

ROW199_BABY_OLD = (
    "row 199 when **foundation export manifest and IX.3 → Handshake 3 meta must read on the same wire before row 200 Handshake 3 meta prelude capstone reunion opens on the full capstone path**"
)
ROW199_BABY_NEW = (
    "row 199 when **foundation export manifest and IX.3 → Handshake 3 meta must read on the same wire before row 200 Handshake 3 meta prelude capstone reunion opens on the full capstone path**"
)


def main() -> None:
    b = _build_blocks()

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "### Row 200 skill checkpoint" in preface:
        print("preface: row 200 already present")
    else:
        if ROW199_TAIL_MARKER not in preface:
            raise SystemExit("row 199 tail proceed marker not found")
        preface = preface.replace(
            ROW199_TAIL_MARKER,
            "When row 199 is complete, proceed to [row 200](preface.md#skill-navigation-row-200)",
            1,
        )
        preface = preface.replace(copper, "\n" + b["row200_preface"] + copper)
        preface_path.write_text(preface)
        print("preface: added row 200")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "**Row 200 closing stitch" not in prologue:
        needle = "| Row 68 → Row 179 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion (row 199) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 199 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        prologue = prologue.replace(
            "**Row 199 closing stitch",
            b["prologue_stitch"] + "**Row 199 closing stitch",
            1,
        )
        preview_anchor = '| <span id="prologue-preview-row-199"></span>Row 199 preview'
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        prologue_path.write_text(prologue)
        print("prologue: added row 200")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "### Row 200 closing loop" not in epilogue:
        if ROW199_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW199_EPILOGUE_OLD, ROW199_EPILOGUE_NEW, 1)
        if ROW199_EPILOGUE_BEFORE_OLD in epilogue:
            epilogue = epilogue.replace(ROW199_EPILOGUE_BEFORE_OLD, ROW199_EPILOGUE_BEFORE_NEW, 1)
        marker = "### Row 186 closing loop (Row 68 → Row 166 Row 68 → Row 66 Writings canonical meta prelude capstone reunion)"
        if marker not in epilogue:
            raise SystemExit("epilogue row 186 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 200")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row180-handshake3-meta-prelude-capstone-reunion-index-row-200" not in sources:
        sources = sources.replace(
            "| 180 | Row 68 → Row 160 Row 68 → Row 60 Handshake 3 meta prelude capstone",
            b["sources_table"] + "| 180 | Row 68 → Row 160 Row 68 → Row 60 Handshake 3 meta prelude capstone",
            1,
        )
        sources = sources.replace(
            src180_header := "## Row 68 → Row 160 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 180)",
            b["sources_index"] + src180_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 200")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-200-baby-picture-row68-row180" not in memory:
        memory = memory.replace(
            "| 199 | Meta | [Row 68 → Row 179 Handshake 3 meta prelude capstone reunion index]",
            b["memory_table"] + "| 199 | Meta | [Row 68 → Row 179 Handshake 3 meta prelude capstone reunion index]",
            1,
        )
        memory = memory.replace(
            "### Row 180 baby picture (Row 68 → Row 160 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion)",
            b["memory_baby"]
            + "### Row 180 baby picture (Row 68 → Row 160 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion)",
            1,
        )
        memory_path.write_text(memory)
        print("memory-sheet: added row 200")


if __name__ == "__main__":
    main()
