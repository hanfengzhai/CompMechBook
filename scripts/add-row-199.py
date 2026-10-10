#!/usr/bin/env python3
"""Add row 199 meta-stitch (Row 68 → Row 179 ↔ Row 59 Handshake 3 meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def bump179_to_199(text: str) -> str:
    """Transform row-179 capstone-path meta copy to row 199 (179→199, 159→179 inner, 198 gate)."""
    out = text.replace("row 200", "TEMP_ROW200")
    out = text.replace("row 199", "TEMP_ROW199")
    out = text.replace("row 198", "TEMP_ROW198")
    out = text.replace("row 179", "TEMP_ROW179")
    out = text.replace("row 178", "TEMP_ROW178")
    repl = [
        ("Row 68 → Row 159 Row 68 → Row 59", "Row 68 → Row 179 Row 68 → Row 59"),
        (
            "row68-row159-handshake3-meta-prelude-capstone-reunion-index-row-179",
            "TEMP_ROW199_HS_INDEX",
        ),
        (
            "row-179-baby-picture-row68-row159-handshake3-meta-prelude-capstone-reunion",
            "row-199-baby-picture-row68-row179-handshake3-meta-prelude-capstone-reunion",
        ),
        ("skill-navigation-row-179", "skill-navigation-row-199"),
        ("prologue-preview-row-179", "prologue-preview-row-199"),
        ("row-179-closing-stitch", "row-199-closing-stitch"),
        ("row-179-closing-loop", "row-199-closing-loop"),
        ("Row 179 three-way audit", "Row 199 three-way audit"),
        (
            "[TEMP_ROW178](preface.md#skill-navigation-row-178) or [row 159](preface.md#skill-navigation-row-159)",
            "[row 198](preface.md#skill-navigation-row-198) or [row 179](preface.md#skill-navigation-row-179)",
        ),
        (
            "[TEMP_ROW178](preface.md#skill-navigation-row-178) or [Row 68 → Row 159 Handshake 3 meta prelude capstone reunion index (row 179)](appendix/sources.md#row68-row159-handshake3-meta-prelude-capstone-reunion-index-row-179)",
            "[row 198](preface.md#skill-navigation-row-198) or [Row 68 → Row 179 Handshake 3 meta prelude capstone reunion index (row 199)](appendix/sources.md#row68-row179-handshake3-meta-prelude-capstone-reunion-index-row-199)",
        ),
        (
            "verified DFT workflows meta prelude capstone closure (row 178)",
            "verified DFT workflows meta prelude capstone closure (row 198)",
        ),
        (
            "before row 180 Handshake 3 meta prelude capstone reunion opens on the full capstone path",
            "before row 200 Handshake 3 meta prelude capstone reunion opens on the full capstone path",
        ),
        (
            "before row 180 Handshake 3 meta prelude capstone reunion on the full capstone path",
            "before row 200 Handshake 3 meta prelude capstone reunion on the full capstone path",
        ),
        (
            "before row 160 Handshake 3 meta prelude capstone opens on the full capstone path",
            "before row 180 Handshake 3 meta prelude capstone opens on the full capstone path",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW199_HS_INDEX",
        "row68-row179-handshake3-meta-prelude-capstone-reunion-index-row-199",
    )
    out = out.replace("TEMP_ROW200", "row 200")
    out = out.replace("TEMP_ROW199", "row 199")
    out = out.replace("TEMP_ROW198", "row 198")
    out = out.replace("TEMP_ROW179", "row 179")
    out = out.replace("TEMP_ROW178", "row 198")
    out = out.replace("skill-navigation-row-159", "TEMP_SKILL_159")
    out = out.replace("Row 179", "Row 199")
    out = out.replace("row 179", "row 199")
    out = out.replace("TEMP_SKILL_159", "skill-navigation-row-159")
    out = out.replace("Row 68 → Row 199 Row 68 → Row 59", "Row 68 → Row 179 Row 68 → Row 59")
    out = out.replace(
        "Row 68 → Row 199 Handshake 3 meta prelude capstone reunion index",
        "Row 68 → Row 179 Handshake 3 meta prelude capstone reunion index",
    )
    out = out.replace("[row 199](preface.md#skill-navigation-row-198)", "[row 198](preface.md#skill-navigation-row-198)")
    out = out.replace("[row 199](preface.md#skill-navigation-row-179)", "[row 179](preface.md#skill-navigation-row-179)")
    out = out.replace("[row 199](preface.md#skill-navigation-row-159)", "[row 159](preface.md#skill-navigation-row-159)")
    out = out.replace("when row 178 closed but row 59", "when row 198 closed but row 59")
    out = out.replace("When row 199 closed", "When row 198 closed")
    out = out.replace("after row 199 alone", "after row 198 alone")
    out = out.replace("Recite [preface row 199]", "Recite [preface row 198]")
    out = out.replace("row 199 or row 159 recited", "row 198 or row 179 recited")
    out = out.replace("row 178 or row 159 recited", "row 198 or row 179 recited")
    out = out.replace("when row 178 closed DFT", "when row 198 closed DFT")
    out = out.replace("after row 178 alone", "after row 198 alone")
    out = out.replace("from row 199's", "from row 198's")
    out = out.replace("after row 178 on", "after row 198 on")
    out = out.replace("Recite [preface row 178]", "Recite [preface row 198]")
    out = out.replace("row 159", "row 179")
    out = out.replace("Row 159", "Row 179")
    out = out.replace("row 139", "row 159")
    out = out.replace("Row 139", "Row 159")
    out = out.replace(
        "row68-row119-handshake3-meta-capstone-reunion-index-row-139",
        "row68-row139-handshake3-meta-capstone-reunion-index-row-159",
    )
    out = out.replace(
        "row68-row139-handshake3-meta-prelude-capstone-reunion-index-row-159",
        "row68-row159-handshake3-meta-prelude-capstone-reunion-index-row-179",
    )
    return out


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    memory = (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text()

    start = preface.index("### Row 179 skill checkpoint")
    end = preface.index("\n\n### Row 180 skill checkpoint", start)
    row199_preface = bump179_to_199(preface[start:end]) + "\n\n"

    row179_stitch = next(line for line in prologue.splitlines() if line.startswith("**Row 179 closing stitch"))

    prologue_compass = (
        "| Row 68 → Row 179 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion (row 199) | "
        "[Preface: row 199 skill checkpoint](../preface.md#skill-navigation-row-199) · "
        "[Row 68 → Row 179 Handshake 3 meta prelude capstone reunion index](../appendix/sources.md#row68-row179-handshake3-meta-prelude-capstone-reunion-index-row-199) · "
        "[memory sheet row 199 baby picture](../appendix/memory-sheet.md#row-199-baby-picture-row68-row179-handshake3-meta-prelude-capstone-reunion) · "
        "[prologue row 199 preview row](#prologue-preview-row-199); [prologue row 199 closing stitch](#row-199-closing-stitch); "
        "[epilogue row 199 closing loop](../epilogue/multiscale.md#row-199-closing-loop) — "
        "read row 68 gate + row 198 or row 179 DFT workflows meta prelude capstone / Handshake 3 meta capstone gate + IX.3 Bridge → opening hinge to Handshake 3 + row 59 meta aloud "
        "when foundation archive is clean on the full capstone path but handbook \\(\\alpha(300\\,\\text{K})\\) persists at the load cell after verified DFT workflows meta prelude capstone |\n"
    )

    prologue_preview = (
        '| <span id="prologue-preview-row-199"></span>Row 199 preview (Row 68 → Row 179 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion) | '
        "Explain why midpoint closure (row 68) and IX.3 → Handshake 3 meta (row 59) must be read together with the Bridge → quasiharmonic \\(\\alpha\\) chain after verified DFT workflows meta prelude capstone before foundation archive and fixed-grip stress feel like separate courses on the full capstone path | "
        'One sentence: "read row 68 gate + row 198 or row 179 DFT workflows meta prelude capstone / Handshake 3 meta capstone gate + IX.3 Bridge → opening hinge to Handshake 3 + row 59 meta aloud when foundation archive is clean on the full capstone path but handbook \\(\\alpha(300\\,\\text{K})\\) persists at the load cell after verified DFT workflows meta prelude capstone" — '
        "[preface row 199 skill checkpoint](../preface.md#skill-navigation-row-199); [prologue row 199 closing stitch](#row-199-closing-stitch); "
        "[Row 68 → Row 179 reunion index](../appendix/sources.md#row68-row179-handshake3-meta-prelude-capstone-reunion-index-row-199); "
        "[memory sheet row 199 baby picture](../appendix/memory-sheet.md#row-199-baby-picture-row68-row179-handshake3-meta-prelude-capstone-reunion); "
        "[IX.3 Bridge to the epilogue](../part09-dft/03-dft-workflows.md#bridge-to-the-epilogue); "
        "[opening hinge to Handshake 3](../part09-dft/03-dft-workflows.md#opening-hinge-ix3-to-handshake3); "
        "[preface row 59 skill checkpoint](../preface.md#skill-navigation-row-59); "
        "[preface row 198 skill checkpoint](../preface.md#skill-navigation-row-198); "
        "[epilogue row 199 closing loop](../epilogue/multiscale.md#row-199-closing-loop) |\n"
    )

    epilogue_loop = bump179_to_199(
        "### Row 179 closing loop"
        + epilogue.split("### Row 179 closing loop")[1].split("### Row 180 closing loop")[0]
    )

    src179_header = "## Row 68 → Row 159 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 179)"
    next179_header = "## Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 160)"
    sources_index = bump179_to_199(sources.split(src179_header, 1)[1].split(next179_header, 1)[0])
    sources_index = (
        "## Row 68 → Row 179 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 199)"
        + sources_index
    )

    sources_table = next(
        line for line in sources.splitlines() if line.startswith("| 179 | Row 68 → Row 159")
    )
    sources_table = bump179_to_199(sources_table).replace("| 179 | Row 68 → Row 179", "| 199 | Row 68 → Row 179", 1) + "\n"

    memory_table = next(
        line for line in memory.splitlines() if line.startswith("| 179 | Meta |")
    )
    memory_table = bump179_to_199(memory_table).replace("| 179 | Meta |", "| 199 | Meta |", 1) + "\n"

    baby_anchor = "### Row 179 baby picture {#row-179-baby-picture-row68-row159-handshake3-meta-prelude-capstone-reunion}"
    memory_baby = bump179_to_199(memory.split(baby_anchor)[1].split("### Row 180 baby picture")[0])
    memory_baby = (
        "### Row 199 baby picture (Row 68 → Row 179 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion)"
        + memory_baby.split(")", 1)[1]
    )

    return {
        "row199_preface": row199_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": bump179_to_199(row179_stitch) + "\n\n",
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_table": memory_table,
        "memory_baby": memory_baby,
    }


ROW198_TAIL_MARKER = "When row 198 is complete, proceed to [row 179](preface.md#skill-navigation-row-199)"

ROW198_EPILOGUE_OLD = (
    "Proceed to [row 179](#row-179-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 198 on the full capstone path,"
)
ROW198_EPILOGUE_NEW = (
    "Proceed to [row 199](#row-199-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 198 on the full capstone path,"
)

ROW198_EPILOGUE_BEFORE_OLD = (
    "before row 179 Handshake 3 meta prelude capstone reunion on the full capstone path (then row 160 on the capstone path)."
)
ROW198_EPILOGUE_BEFORE_NEW = (
    "before row 199 Handshake 3 meta prelude capstone reunion on the full capstone path (then row 180 on the capstone path)."
)

ROW198_BABY_OLD = (
    "row 198 when **IX.2 Bridge and Row 68 → Row 58 meta must read on the same wire before row 199 Handshake 3 meta prelude capstone reunion opens on the full capstone path**"
)
ROW198_BABY_NEW = (
    "row 198 when **IX.2 Bridge and Row 68 → Row 58 meta must read on the same wire before row 199 Handshake 3 meta prelude capstone reunion opens on the full capstone path**"
)


def main() -> None:
    b = _build_blocks()

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "### Row 199 skill checkpoint" in preface:
        print("preface: row 199 already present")
    else:
        if ROW198_TAIL_MARKER not in preface:
            raise SystemExit("row 198 tail proceed marker not found")
        preface = preface.replace(
            "When row 198 is complete, proceed to [row 179](preface.md#skill-navigation-row-199)",
            "When row 198 is complete, proceed to [row 199](preface.md#skill-navigation-row-199)",
            1,
        )
        preface = preface.replace(copper, "\n" + b["row199_preface"] + copper)
        preface_path.write_text(preface)
        print("preface: added row 199")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "**Row 199 closing stitch" not in prologue:
        needle = "| Row 68 → Row 178 Row 68 → Row 58 DFT workflows meta prelude capstone reunion (row 198) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 198 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        prologue = prologue.replace(
            "**Row 198 closing stitch",
            b["prologue_stitch"] + "**Row 198 closing stitch",
            1,
        )
        preview_anchor = '| <span id="prologue-preview-row-198"></span>Row 198 preview'
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        prologue_path.write_text(prologue)
        print("prologue: added row 199")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "### Row 199 closing loop" not in epilogue:
        if ROW198_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW198_EPILOGUE_OLD, ROW198_EPILOGUE_NEW, 1)
        if ROW198_EPILOGUE_BEFORE_OLD in epilogue:
            epilogue = epilogue.replace(ROW198_EPILOGUE_BEFORE_OLD, ROW198_EPILOGUE_BEFORE_NEW, 1)
        marker = "### Row 186 closing loop (Row 68 → Row 166 Row 68 → Row 66 Writings canonical meta prelude capstone reunion)"
        if marker not in epilogue:
            raise SystemExit("epilogue row 186 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 199")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row179-handshake3-meta-prelude-capstone-reunion-index-row-199" not in sources:
        sources = sources.replace(
            "| 179 | Row 68 → Row 159 Row 68 → Row 59 Handshake 3 meta prelude capstone",
            b["sources_table"] + "| 179 | Row 68 → Row 159 Row 68 → Row 59 Handshake 3 meta prelude capstone",
            1,
        )
        sources = sources.replace(
            src179_header := "## Row 68 → Row 159 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 179)",
            b["sources_index"] + src179_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 199")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-199-baby-picture-row68-row179" not in memory:
        memory = memory.replace(
            "| 198 | Meta | [Row 68 → Row 178 DFT workflows meta prelude capstone reunion index]",
            b["memory_table"] + "| 198 | Meta | [Row 68 → Row 178 DFT workflows meta prelude capstone reunion index]",
            1,
        )
        memory = memory.replace(
            "### Row 179 baby picture {#row-179-baby-picture-row68-row159-handshake3-meta-prelude-capstone-reunion}",
            b["memory_baby"]
            + "### Row 179 baby picture {#row-179-baby-picture-row68-row159-handshake3-meta-prelude-capstone-reunion}",
            1,
        )
        memory_path.write_text(memory)
        print("memory-sheet: added row 199")


if __name__ == "__main__":
    main()
