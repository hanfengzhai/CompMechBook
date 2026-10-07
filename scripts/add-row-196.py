#!/usr/bin/env python3
"""Add row 196 meta-stitch (Row 68 → Row 176 ↔ Row 56 Born–Oppenheimer meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def bump176_to_196(text: str) -> str:
    out = text.replace("row 177", "TEMP_ROW177")
    out = out.replace("row 176", "TEMP_ROW176")
    out = out.replace("row 175", "TEMP_ROW175")
    repl = [
        ("Row 68 → Row 156 Row 68 → Row 56", "Row 68 → Row 176 Row 68 → Row 56"),
        (
            "row68-row156-born-oppenheimer-meta-prelude-capstone-reunion-index-row-176",
            "TEMP_ROW196_BO_INDEX",
        ),
        (
            "row-176-baby-picture-row68-row156-born-oppenheimer-meta-prelude-capstone-reunion",
            "row-196-baby-picture-row68-row176-born-oppenheimer-meta-prelude-capstone-reunion",
        ),
        ("### Row 176 skill checkpoint", "### Row 196 skill checkpoint"),
        ("skill-navigation-row-176", "skill-navigation-row-196"),
        ("prologue-preview-row-176", "prologue-preview-row-196"),
        ("row-176-closing-stitch", "row-196-closing-stitch"),
        ("row-176-closing-loop", "row-196-closing-loop"),
        ("Row 176 three-way audit", "Row 196 three-way audit"),
        (
            "[row 175](preface.md#skill-navigation-row-175) or [row 156](preface.md#skill-navigation-row-156)",
            "[row 195](preface.md#skill-navigation-row-195) or [row 176](preface.md#skill-navigation-row-176)",
        ),
        (
            "[row 175](preface.md#skill-navigation-row-175) or [Row 68 → Row 156 Born–Oppenheimer meta prelude capstone reunion index (row 176)](appendix/sources.md#row68-row156-born-oppenheimer-meta-prelude-capstone-reunion-index-row-176)",
            "[row 195](preface.md#skill-navigation-row-195) or [Row 68 → Row 176 Born–Oppenheimer meta prelude capstone reunion index (row 196)](appendix/sources.md#row68-row176-born-oppenheimer-meta-prelude-capstone-reunion-index-row-196)",
        ),
        (
            "verified electronic audit meta prelude capstone closure (row 175)",
            "verified electronic audit meta prelude capstone closure (row 195)",
        ),
        (
            "before row 177 Kohn–Sham meta prelude capstone reunion opens on the full capstone path",
            "before row 197 Kohn–Sham meta prelude capstone reunion opens on the full capstone path",
        ),
        (
            "before row 178 DFT workflows meta prelude capstone reunion opens on the full capstone path",
            "before row 198 DFT workflows meta prelude capstone reunion opens on the full capstone path",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW196_BO_INDEX",
        "row68-row176-born-oppenheimer-meta-prelude-capstone-reunion-index-row-196",
    )
    out = out.replace("TEMP_ROW175", "row 195")
    out = out.replace("TEMP_ROW176", "row 196")
    out = out.replace("TEMP_ROW177", "row 197")
    out = out.replace("skill-navigation-row-156", "TEMP_SKILL_156")
    out = out.replace("Row 176", "Row 196")
    out = out.replace("row 176", "row 196")
    out = out.replace("TEMP_SKILL_156", "skill-navigation-row-156")
    out = out.replace("[row 196](preface.md#skill-navigation-row-195)", "[row 195](preface.md#skill-navigation-row-195)")
    out = out.replace("[row 196](preface.md#skill-navigation-row-176)", "[row 176](preface.md#skill-navigation-row-176)")
    out = out.replace("when row 175 closed but row 56", "when row 195 closed but row 56")
    out = out.replace("When row 196 closed", "When row 195 closed")
    out = out.replace("after row 196 alone", "after row 195 alone")
    out = out.replace("Recite [preface row 196]", "Recite [preface row 195]")
    out = out.replace("row 196 or row 156 recited", "row 195 or row 176 recited")
    out = out.replace("row 175 or row 156 recited", "row 195 or row 176 recited")
    out = out.replace("row 156", "row 176")
    out = out.replace("Row 156", "Row 176")
    out = out.replace("row 136", "row 156")
    out = out.replace("Row 136", "Row 156")
    out = out.replace(
        "row68-row136-born-oppenheimer-meta-prelude-capstone-reunion-index-row-156",
        "row68-row156-born-oppenheimer-meta-prelude-capstone-reunion-index-row-176",
    )
    out = out.replace(
        "row68-row155-electronic-audit-meta-prelude-capstone-reunion-index-row-175",
        "row68-row175-electronic-audit-meta-prelude-capstone-reunion-index-row-195",
    )
    out = out.replace("Row 68 → Row 196 Row 68 → Row 56", "Row 68 → Row 176 Row 68 → Row 56")
    out = out.replace("memory sheet row 176 baby picture", "memory sheet row 196 baby picture")
    out = out.replace("prologue row 176 closing stitch", "prologue row 196 closing stitch")
    out = out.replace("prologue row 176 preview", "prologue row 196 preview")
    out = out.replace("epilogue row 176 closing loop", "epilogue row 196 closing loop")
    out = out.replace("opening [row 177]", "opening [row 197]")
    out = out.replace("skill-navigation-row-177", "skill-navigation-row-197")
    out = out.replace(
        "Prologue preview ([row 176](prologue/00-many-scales.md#prologue-preview-row-196))",
        "Prologue preview ([row 196](prologue/00-many-scales.md#prologue-preview-row-196))",
    )
    return out


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    memory = (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text()

    start = preface.index("### Row 176 skill checkpoint")
    end = preface.index("\n\n### Row 177 skill checkpoint", start)
    row196_preface = bump176_to_196(preface[start:end]) + "\n\n"

    row176_stitch = next(line for line in prologue.splitlines() if line.startswith("**Row 176 closing stitch"))

    prologue_compass = (
        "| Row 68 → Row 176 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion (row 196) | "
        "[Preface: row 196 skill checkpoint](../preface.md#skill-navigation-row-196) · "
        "[Row 68 → Row 176 Born–Oppenheimer meta prelude capstone reunion index](../appendix/sources.md#row68-row176-born-oppenheimer-meta-prelude-capstone-reunion-index-row-196) · "
        "[memory sheet row 196 baby picture](../appendix/memory-sheet.md#row-196-baby-picture-row68-row176-born-oppenheimer-meta-prelude-capstone-reunion) · "
        "[prologue row 196 preview row](#prologue-preview-row-196); [prologue row 196 closing stitch](#row-196-closing-stitch); "
        "[epilogue row 196 closing loop](../epilogue/multiscale.md#row-196-closing-loop) — "
        "read row 68 gate + row 195 or row 176 electronic audit meta prelude capstone / Born–Oppenheimer opening gate + IX.0 Bridge → opening hinge → IX.1 BO/HK + row 56 meta aloud "
        "when foundation SCF logs are clean on the full capstone path but Born–Oppenheimer still feels like standalone quantum chemistry after verified electronic audit meta prelude capstone |\n"
    )

    prologue_preview = (
        '| <span id="prologue-preview-row-196"></span>Row 196 preview (Row 68 → Row 176 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion) | '
        "Explain why midpoint closure (row 68) and IX.0 → IX.1 meta (row 56) must be read together with the Bridge → BO/HK chain after verified electronic audit meta prelude capstone before foundation SCF logs and Born–Oppenheimer feel like separate courses on the full capstone path | "
        'One sentence: "read row 68 gate + row 195 or row 176 electronic audit meta prelude capstone / Born–Oppenheimer opening gate + IX.0 Bridge → opening hinge → IX.1 BO/HK + row 56 meta aloud when foundation SCF logs are clean on the full capstone path but Born–Oppenheimer still feels like standalone quantum chemistry after verified electronic audit meta prelude capstone" — '
        "[preface row 196 skill checkpoint](../preface.md#skill-navigation-row-196); [prologue row 196 closing stitch](#row-196-closing-stitch); "
        "[Row 68 → Row 176 reunion index](../appendix/sources.md#row68-row176-born-oppenheimer-meta-prelude-capstone-reunion-index-row-196); "
        "[memory sheet row 196 baby picture](../appendix/memory-sheet.md#row-196-baby-picture-row68-row176-born-oppenheimer-meta-prelude-capstone-reunion); "
        "[IX.0 Bridge → opening hinge → IX.1 BO/HK](../part09-dft/00-opening.md#bridge); "
        "[IX.1 opening hinge from IX.0](../part09-dft/01-born-oppenheimer.md#opening-hinge-ix0-to-ix1); "
        "[preface row 56 skill checkpoint](../preface.md#skill-navigation-row-56); "
        "[preface row 195 skill checkpoint](../preface.md#skill-navigation-row-195); "
        "[epilogue row 196 closing loop](../epilogue/multiscale.md#row-196-closing-loop) |\n"
    )

    epilogue_loop = bump176_to_196(
        "### Row 176 closing loop"
        + epilogue.split("### Row 176 closing loop")[1].split("### Row 177 closing loop")[0]
    )

    sources_table = (
        "| 196 | Row 68 → Row 176 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone (midpoint prelude gate ↔ electronic audit meta prelude capstone on full capstone path ↔ row 56 meta) | "
        "[Row 68 → Row 176 Born–Oppenheimer meta prelude capstone reunion index](#row68-row176-born-oppenheimer-meta-prelude-capstone-reunion-index-row-196) · "
        "[preface row 196](../preface.md#skill-navigation-row-196) · "
        "[prologue row 196 preview](../prologue/00-many-scales.md#prologue-preview-row-196) · "
        "[prologue row 196 closing stitch](../prologue/00-many-scales.md#row-196-closing-stitch) · "
        "[epilogue row 196 closing loop](../epilogue/multiscale.md#row-196-closing-loop) · "
        "[memory sheet row 196 baby picture](memory-sheet.md#row-196-baby-picture-row68-row176-born-oppenheimer-meta-prelude-capstone-reunion) | "
        "Row 68 closed but **row 56 IX.0 → IX.1 opening hinge still feels disconnected from verified electronic audit meta prelude capstone on the full capstone path** — "
        "read row 68 + row 195 or row 176 gate + IX.0 Bridge → opening hinge → IX.1 BO/HK + row 56; "
        "[preface row 56](../preface.md#skill-navigation-row-56) |\n"
    )

    sources_index = bump176_to_196(
        sources.split("## Row 68 → Row 156 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion index (row 176)")[1]
        .split("## Row 68 → Row 157 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion index (row 177)")[0]
    )
    sources_index = (
        "## Row 68 → Row 176 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion index (row 196)"
        + sources_index
    )

    memory_table = (
        "| 196 | Meta | [Row 68 → Row 176 Born–Oppenheimer meta prelude capstone reunion index](sources.md#row68-row176-born-oppenheimer-meta-prelude-capstone-reunion-index-row-196) · "
        "[preface row 196 skill checkpoint](../preface.md#skill-navigation-row-196) · "
        "[prologue row 196 preview](../prologue/00-many-scales.md#prologue-preview-row-196) · "
        "[prologue row 196 closing stitch](../prologue/00-many-scales.md#row-196-closing-stitch) · "
        "[epilogue row 196 closing loop](../epilogue/multiscale.md#row-196-closing-loop) | "
        "Row 68 closed but row 56 IX.0 → IX.1 opening hinge feels disconnected from verified electronic audit meta prelude capstone on the full capstone path — "
        "read row 68 + row 195 or row 176 gate + IX.0 Bridge → opening hinge → IX.1 BO/HK + row 56; "
        "[row 196 baby picture](#row-196-baby-picture-row68-row176-born-oppenheimer-meta-prelude-capstone-reunion) |\n"
    )

    memory_baby = bump176_to_196(
        memory.split("### Row 176 baby picture (Row 68 → Row 156 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion)")[1]
        .split("### Row 177 baby picture")[0]
    )
    memory_baby = (
        "### Row 196 baby picture (Row 68 → Row 176 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion)"
        + memory_baby.split(")", 1)[1]
    )

    return {
        "row196_preface": row196_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": bump176_to_196(row176_stitch) + "\n\n",
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_table": memory_table,
        "memory_baby": memory_baby,
    }


ROW195_TAIL_OLD = (
    "When row 195 is complete, proceed to [row 156](preface.md#skill-navigation-row-156) when `cu.relax.out` exists on the full capstone path, to [row 136](preface.md#skill-navigation-row-136) when `cu.relax.out` exists but IX.1 still feels disconnected from verified electronic audit meta prelude capstone on the full capstone path, to [row 175](preface.md#skill-navigation-row-155) for the Row 68 ↔ Row 55 electronic audit meta audit on the opening-hinge capstone path alone, to [row 155](preface.md#skill-navigation-row-135) for the Row 68 ↔ Row 55 electronic audit meta audit on the opening-hinge prelude path alone, to [row 174](preface.md#skill-navigation-row-154) when yaml exports still stall after verified export meta prelude capstone on the full capstone path, to [row 134](preface.md#skill-navigation-row-134) for the Row 68 ↔ Row 54 export meta audit on the opening-hinge capstone path alone, to [row 55](preface.md#skill-navigation-row-55) when only VIII.3 → IX.0 stalls, or extend prose only under `writings/` then sync."
)
ROW195_TAIL_NEW = (
    "When row 195 is complete, proceed to [row 196](preface.md#skill-navigation-row-196) when `cu.relax.out` exists on the full capstone path, to [row 176](preface.md#skill-navigation-row-176) when `cu.relax.out` exists but IX.1 still feels disconnected from verified electronic audit meta prelude capstone on the opening-hinge capstone path alone, to [row 156](preface.md#skill-navigation-row-136) for the Row 68 ↔ Row 56 Born–Oppenheimer meta audit on the opening-hinge prelude path alone, to [row 175](preface.md#skill-navigation-row-175) for the Row 68 ↔ Row 55 electronic audit meta audit on the opening-hinge capstone path alone, to [row 194](preface.md#skill-navigation-row-194) when yaml exports still stall after verified export meta prelude capstone on the full capstone path, to [row 56](preface.md#skill-navigation-row-56) when only IX.0 → IX.1 stalls, or extend prose only under `writings/` then sync."
)

ROW195_STITCH_OLD = (
    "before row 176 Born–Oppenheimer meta prelude capstone reunion opens on the full capstone path."
)
ROW195_STITCH_NEW = (
    "before row 196 Born–Oppenheimer meta prelude capstone reunion opens on the full capstone path."
)

ROW195_EPILOGUE_PROCEED_OLD = (
    "Proceed to [row 176](#row-176-closing-loop) when row 68 closed but Born–Oppenheimer meta prelude capstone still lags after row 195 on the full capstone path,"
)
ROW195_EPILOGUE_PROCEED_NEW = (
    "Proceed to [row 196](#row-196-closing-loop) when row 68 closed but Born–Oppenheimer meta prelude capstone still lags after row 195 on the full capstone path,"
)

ROW195_BABY_OLD = (
    "row 195 when **VIII.3 Bridge and Row 68 → Row 55 meta must read on the same wire before row 176 Born–Oppenheimer meta prelude capstone opens on the full capstone path**"
)
ROW195_BABY_NEW = (
    "row 195 when **IX.0 Bridge and Row 68 → Row 56 meta must read on the same wire before row 196 Born–Oppenheimer meta prelude capstone opens on the full capstone path**"
)


def main() -> None:
    b = _build_blocks()

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "### Row 196 skill checkpoint" in preface and preface.index("### Row 196 skill checkpoint") < preface.index(
        copper
    ):
        print("preface: row 196 already present")
    else:
        if ROW195_TAIL_OLD not in preface:
            raise SystemExit("row 195 tail proceed string not found")
        preface = preface.replace(ROW195_TAIL_OLD, ROW195_TAIL_NEW, 1)
        preface = preface.replace(
            "when opening [row 156](preface.md#skill-navigation-row-156) before row 56 closes on the full capstone path",
            "when opening [row 196](preface.md#skill-navigation-row-196) before row 56 closes on the full capstone path",
            1,
        )
        preface = preface.replace(copper, "\n" + b["row196_preface"] + copper)
        preface_path.write_text(preface)
        print("preface: added row 196")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-196" not in prologue:
        needle = "| Row 68 → Row 175 Row 68 → Row 55 electronic audit meta prelude capstone reunion (row 195) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 195 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "row-196-closing-stitch" not in prologue:
            prologue = prologue.replace(
                "**Row 176 closing stitch",
                b["prologue_stitch"] + "**Row 176 closing stitch",
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-195"></span>Row 195 preview'
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW195_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW195_STITCH_OLD, ROW195_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 196")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "### Row 196 closing loop" not in epilogue:
        if ROW195_EPILOGUE_PROCEED_OLD in epilogue:
            epilogue = epilogue.replace(ROW195_EPILOGUE_PROCEED_OLD, ROW195_EPILOGUE_PROCEED_NEW, 1)
        marker = "### Row 186 closing loop (Row 68 → Row 166 Row 68 → Row 66 Writings canonical meta prelude capstone reunion)"
        if marker not in epilogue:
            raise SystemExit("epilogue row 186 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 196")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row176-born-oppenheimer-meta-prelude-capstone-reunion-index-row-196" not in sources:
        sources = sources.replace(
            "| 176 | Row 68 → Row 156 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone",
            b["sources_table"] + "| 176 | Row 68 → Row 156 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone",
            1,
        )
        sources = sources.replace(
            "## Row 68 → Row 156 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion index (row 176)",
            b["sources_index"] + "## Row 68 → Row 156 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion index (row 176)",
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 196")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-196-baby-picture-row68-row176" not in memory:
        memory = memory.replace(
            "| 195 | Meta | [Row 68 → Row 175 electronic audit meta prelude capstone reunion index]",
            b["memory_table"] + "| 195 | Meta | [Row 68 → Row 175 electronic audit meta prelude capstone reunion index]",
            1,
        )
        memory = memory.replace(
            "### Row 176 baby picture (Row 68 → Row 156 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion) {#row-176-baby-picture-row68-row156-born-oppenheimer-meta-prelude-capstone-reunion}",
            b["memory_baby"]
            + "### Row 176 baby picture (Row 68 → Row 156 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion) {#row-176-baby-picture-row68-row156-born-oppenheimer-meta-prelude-capstone-reunion}",
            1,
        )
        if ROW195_BABY_OLD in memory:
            memory = memory.replace(ROW195_BABY_OLD, ROW195_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 196")


if __name__ == "__main__":
    main()
