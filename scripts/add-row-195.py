#!/usr/bin/env python3
"""Add row 195 meta-stitch (Row 68 → Row 175 ↔ Row 55 electronic audit meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def bump175_to_195(text: str) -> str:
    out = text.replace("row 176", "TEMP_ROW176")
    out = out.replace("row 175", "TEMP_ROW175")
    repl = [
        ("Row 68 → Row 155 Row 68 → Row 55", "Row 68 → Row 175 Row 68 → Row 55"),
        (
            "row68-row155-electronic-audit-meta-prelude-capstone-reunion-index-row-175",
            "TEMP_ROW195_EA_INDEX",
        ),
        (
            "row-175-baby-picture-row68-row155-electronic-audit-meta-prelude-capstone-reunion",
            "row-195-baby-picture-row68-row175-electronic-audit-meta-prelude-capstone-reunion",
        ),
        ("### Row 175 skill checkpoint", "### Row 195 skill checkpoint"),
        ("skill-navigation-row-175", "skill-navigation-row-195"),
        ("prologue-preview-row-175", "prologue-preview-row-195"),
        ("row-175-closing-stitch", "row-195-closing-stitch"),
        ("row-175-closing-loop", "row-195-closing-loop"),
        ("Row 175 three-way audit", "Row 195 three-way audit"),
        (
            "[row 174](preface.md#skill-navigation-row-174) or [row 155](preface.md#skill-navigation-row-155)",
            "[row 194](preface.md#skill-navigation-row-194) or [row 175](preface.md#skill-navigation-row-175)",
        ),
        (
            "[row 174](preface.md#skill-navigation-row-174) or [Row 68 → Row 155 electronic audit meta prelude capstone reunion index (row 175)](appendix/sources.md#row68-row155-electronic-audit-meta-prelude-capstone-reunion-index-row-175)",
            "[row 194](preface.md#skill-navigation-row-194) or [Row 68 → Row 175 electronic audit meta prelude capstone reunion index (row 195)](appendix/sources.md#row68-row175-electronic-audit-meta-prelude-capstone-reunion-index-row-195)",
        ),
        (
            "verified export meta prelude capstone closure (row 174)",
            "verified export meta prelude capstone closure (row 194)",
        ),
        (
            "before row 176 Born–Oppenheimer meta prelude capstone reunion opens on the full capstone path",
            "before row 196 Born–Oppenheimer meta prelude capstone reunion opens on the full capstone path",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW195_EA_INDEX",
        "row68-row175-electronic-audit-meta-prelude-capstone-reunion-index-row-195",
    )
    out = out.replace("TEMP_ROW175", "row 175")
    out = out.replace("TEMP_ROW176", "row 176")
    out = out.replace("skill-navigation-row-155", "TEMP_SKILL_155")
    out = out.replace("Row 175", "Row 195")
    out = out.replace("row 175", "row 195")
    out = out.replace("TEMP_SKILL_155", "skill-navigation-row-155")
    out = out.replace("[row 195](preface.md#skill-navigation-row-194)", "[row 194](preface.md#skill-navigation-row-194)")
    out = out.replace("[row 195](preface.md#skill-navigation-row-175)", "[row 175](preface.md#skill-navigation-row-175)")
    out = out.replace("when row 174 closed but row 55", "when row 194 closed but row 55")
    out = out.replace("When row 195 closed", "When row 194 closed")
    out = out.replace("after row 195 alone", "after row 194 alone")
    out = out.replace("Recite [preface row 195]", "Recite [preface row 194]")
    out = out.replace("row 195 or row 155 recited", "row 194 or row 175 recited")
    out = out.replace("row 174 or row 155 recited", "row 194 or row 175 recited")
    out = out.replace("row 155", "row 175")
    out = out.replace("Row 155", "Row 175")
    out = out.replace("row 135", "row 155")
    out = out.replace("Row 135", "Row 155")
    out = out.replace(
        "row68-row135-electronic-audit-meta-prelude-capstone-reunion-index-row-155",
        "row68-row155-electronic-audit-meta-prelude-capstone-reunion-index-row-175",
    )
    out = out.replace(
        "row68-row154-export-meta-prelude-capstone-reunion-index-row-174",
        "row68-row174-export-meta-prelude-capstone-reunion-index-row-194",
    )
    out = out.replace("Row 68 → Row 195 Row 68 → Row 55", "Row 68 → Row 175 Row 68 → Row 55")
    out = out.replace("memory sheet row 175 baby picture", "memory sheet row 195 baby picture")
    out = out.replace("prologue row 175 closing stitch", "prologue row 195 closing stitch")
    out = out.replace("prologue row 175 preview", "prologue row 195 preview")
    out = out.replace("epilogue row 175 closing loop", "epilogue row 195 closing loop")
    out = out.replace("opening [row 176]", "opening [row 196]")
    out = out.replace("skill-navigation-row-176", "skill-navigation-row-196")
    out = out.replace(
        "Prologue preview ([row 175](prologue/00-many-scales.md#prologue-preview-row-195))",
        "Prologue preview ([row 195](prologue/00-many-scales.md#prologue-preview-row-195))",
    )
    return out


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    memory = (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text()

    start = preface.index("### Row 175 skill checkpoint")
    end = preface.index("\n\n### Row 176 skill checkpoint", start)
    row195_preface = bump175_to_195(preface[start:end]) + "\n\n"

    row175_stitch = next(line for line in prologue.splitlines() if line.startswith("**Row 175 closing stitch"))

    prologue_compass = (
        "| Row 68 → Row 175 Row 68 → Row 55 electronic audit meta prelude capstone reunion (row 195) | "
        "[Preface: row 195 skill checkpoint](../preface.md#skill-navigation-row-195) · "
        "[Row 68 → Row 175 electronic audit meta prelude capstone reunion index](../appendix/sources.md#row68-row175-electronic-audit-meta-prelude-capstone-reunion-index-row-195) · "
        "[memory sheet row 195 baby picture](../appendix/memory-sheet.md#row-195-baby-picture-row68-row175-electronic-audit-meta-prelude-capstone-reunion) · "
        "[prologue row 195 preview row](#prologue-preview-row-195); [prologue row 195 closing stitch](#row-195-closing-stitch); "
        "[epilogue row 195 closing loop](../epilogue/multiscale.md#row-195-closing-loop) — "
        "read row 68 gate + row 194 or row 175 export meta prelude capstone / electronic audit meta prelude gate + VIII.3 Bridge → opening hinge → IX.0 SCF audit + row 55 meta aloud "
        "when pedigree checklist is clean on the full capstone path but Part IX still feels like standalone DFT coursework after verified export meta prelude capstone |\n"
    )

    prologue_preview = (
        '| <span id="prologue-preview-row-195"></span>Row 195 preview (Row 68 → Row 175 Row 68 → Row 55 electronic audit meta prelude capstone reunion) | '
        "Explain why midpoint closure (row 68) and VIII.3 → IX.0 meta (row 55) must be read together with the Bridge → SCF audit chain after verified export meta prelude capstone before pedigree checklist and Part IX feel like separate courses on the full capstone path | "
        'One sentence: "read row 68 gate + row 194 or row 175 export meta prelude capstone / electronic audit meta prelude gate + VIII.3 Bridge → opening hinge → IX.0 SCF audit + row 55 meta aloud when pedigree checklist is clean on the full capstone path but Part IX still feels like standalone DFT coursework after verified export meta prelude capstone" — '
        "[preface row 195 skill checkpoint](../preface.md#skill-navigation-row-195); [prologue row 195 closing stitch](#row-195-closing-stitch); "
        "[Row 68 → Row 175 reunion index](../appendix/sources.md#row68-row175-electronic-audit-meta-prelude-capstone-reunion-index-row-195); "
        "[memory sheet row 195 baby picture](../appendix/memory-sheet.md#row-195-baby-picture-row68-row175-electronic-audit-meta-prelude-capstone-reunion); "
        "[VIII.3 Bridge → opening hinge → IX.0 SCF audit](../part08-md/03-ab-initio-and-coarse-graining.md#bridge-to-part-ix); "
        "[IX.0 opening hinge from VIII.3](../part09-dft/00-opening.md#opening-hinge-viii3-to-ix); "
        "[preface row 55 skill checkpoint](../preface.md#skill-navigation-row-55); "
        "[preface row 194 skill checkpoint](../preface.md#skill-navigation-row-194); "
        "[epilogue row 195 closing loop](../epilogue/multiscale.md#row-195-closing-loop) |\n"
    )

    epilogue_loop = bump175_to_195(
        "### Row 175 closing loop"
        + epilogue.split("### Row 175 closing loop")[1].split("### Row 176 closing loop")[0]
    )

    sources_table = (
        "| 195 | Row 68 → Row 175 Row 68 → Row 55 electronic audit meta prelude capstone (midpoint prelude gate ↔ export meta prelude capstone on full capstone path ↔ row 55 meta) | "
        "[Row 68 → Row 175 electronic audit meta prelude capstone reunion index](#row68-row175-electronic-audit-meta-prelude-capstone-reunion-index-row-195) · "
        "[preface row 195](../preface.md#skill-navigation-row-195) · "
        "[prologue row 195 preview](../prologue/00-many-scales.md#prologue-preview-row-195) · "
        "[prologue row 195 closing stitch](../prologue/00-many-scales.md#row-195-closing-stitch) · "
        "[epilogue row 195 closing loop](../epilogue/multiscale.md#row-195-closing-loop) · "
        "[memory sheet row 195 baby picture](memory-sheet.md#row-195-baby-picture-row68-row175-electronic-audit-meta-prelude-capstone-reunion) | "
        "Row 68 closed but **row 55 VIII.3 → IX.0 opening hinge still feels disconnected from verified export meta prelude capstone on the full capstone path** — "
        "read row 68 + row 194 or row 175 gate + VIII.3 Bridge → opening hinge → IX.0 SCF audit + row 55; "
        "[preface row 55](../preface.md#skill-navigation-row-55) |\n"
    )

    sources_index = bump175_to_195(
        sources.split("## Row 68 → Row 155 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 175)")[1]
        .split("## Row 68 → Row 156 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion index (row 176)")[0]
    )
    sources_index = (
        "## Row 68 → Row 175 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 195)"
        + sources_index
    )

    memory_table = (
        "| 195 | Meta | [Row 68 → Row 175 electronic audit meta prelude capstone reunion index](sources.md#row68-row175-electronic-audit-meta-prelude-capstone-reunion-index-row-195) · "
        "[preface row 195 skill checkpoint](../preface.md#skill-navigation-row-195) · "
        "[prologue row 195 preview](../prologue/00-many-scales.md#prologue-preview-row-195) · "
        "[prologue row 195 closing stitch](../prologue/00-many-scales.md#row-195-closing-stitch) · "
        "[epilogue row 195 closing loop](../epilogue/multiscale.md#row-195-closing-loop) | "
        "Row 68 closed but row 55 VIII.3 → IX.0 opening hinge feels disconnected from verified export meta prelude capstone on the full capstone path — "
        "read row 68 + row 194 or row 175 gate + VIII.3 Bridge → opening hinge → IX.0 SCF audit + row 55; "
        "[row 195 baby picture](#row-195-baby-picture-row68-row175-electronic-audit-meta-prelude-capstone-reunion) |\n"
    )

    memory_baby = bump175_to_195(
        memory.split("### Row 175 baby picture (Row 68 → Row 155 Row 68 → Row 55 electronic audit meta prelude capstone reunion)")[1]
        .split("### Row 176 baby picture")[0]
    )
    memory_baby = (
        "### Row 195 baby picture (Row 68 → Row 175 Row 68 → Row 55 electronic audit meta prelude capstone reunion)"
        + memory_baby.split(")", 1)[1]
    )

    return {
        "row195_preface": row195_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": bump175_to_195(row175_stitch) + "\n\n",
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_table": memory_table,
        "memory_baby": memory_baby,
    }


ROW194_TAIL_OLD = (
    "When row 194 is complete, proceed to [row 155](preface.md#skill-navigation-row-155) when the pedigree checklist is filled but Part IX still feels disconnected from verified export meta prelude capstone on the full capstone path, to [row 135](preface.md#skill-navigation-row-135) when the pedigree checklist is filled but Part IX still feels disconnected from verified export meta prelude capstone on the opening-hinge capstone path alone, to [row 174](preface.md#skill-navigation-row-174) for the Row 68 ↔ Row 54 export meta audit on the opening-hinge capstone path alone, to [row 154](preface.md#skill-navigation-row-134) for the Row 68 ↔ Row 54 export meta audit on the opening-hinge prelude path alone, to [row 113](preface.md#skill-navigation-row-113) for the Row 68 ↔ Row 53 dynamics meta audit on the opening-hinge prelude path alone, to [row 153](preface.md#skill-navigation-row-153) when NVT/NPT still stalls after verified atomistic meta prelude capstone on the opening-hinge capstone path alone, to [row 54](preface.md#skill-navigation-row-54) when only VIII.2 → VIII.3 stalls, or extend prose only under `writings/` then sync."
)
ROW194_TAIL_NEW = (
    "When row 194 is complete, proceed to [row 195](preface.md#skill-navigation-row-195) when the pedigree checklist is filled but Part IX still feels disconnected from verified export meta prelude capstone on the full capstone path, to [row 175](preface.md#skill-navigation-row-175) when the pedigree checklist is filled but Part IX still feels disconnected from verified export meta prelude capstone on the opening-hinge capstone path alone, to [row 155](preface.md#skill-navigation-row-155) for the Row 68 ↔ Row 55 electronic audit meta audit on the opening-hinge prelude path alone, to [row 174](preface.md#skill-navigation-row-174) for the Row 68 ↔ Row 54 export meta audit on the opening-hinge capstone path alone, to [row 193](preface.md#skill-navigation-row-193) when NVT/NPT still stalls after verified atomistic meta prelude capstone on the full capstone path, to [row 55](preface.md#skill-navigation-row-55) when only VIII.3 → IX.0 stalls, or extend prose only under `writings/` then sync."
)

ROW194_STITCH_OLD = (
    "before row 175 electronic audit meta prelude capstone reunion opens on the full capstone path."
)
ROW194_STITCH_NEW = (
    "before row 195 electronic audit meta prelude capstone reunion opens on the full capstone path."
)

ROW194_EPILOGUE_PROCEED_OLD = (
    "Proceed to [row 175](#row-175-closing-loop) when row 68 closed but electronic audit meta prelude capstone still lags after row 174 on the full capstone path,"
)
ROW194_EPILOGUE_PROCEED_NEW = (
    "Proceed to [row 195](#row-195-closing-loop) when row 68 closed but electronic audit meta prelude capstone still lags after row 194 on the full capstone path,"
)

ROW194_BABY_OLD = (
    "row 194 when **VIII.2 Bridge and Row 68 → Row 54 meta must read on the same wire before row 174 export meta prelude capstone opens on the full capstone path**"
)
ROW194_BABY_NEW = (
    "row 194 when **VIII.3 Bridge and Row 68 → Row 55 meta must read on the same wire before row 195 electronic audit meta prelude capstone opens on the full capstone path**"
)


def main() -> None:
    b = _build_blocks()

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "### Row 195 skill checkpoint" in preface and preface.index("### Row 195 skill checkpoint") < preface.index(
        copper
    ):
        print("preface: row 195 already present")
    else:
        if ROW194_TAIL_OLD not in preface:
            raise SystemExit("row 194 tail proceed string not found")
        preface = preface.replace(ROW194_TAIL_OLD, ROW194_TAIL_NEW, 1)
        preface = preface.replace(
            "when opening [row 135](preface.md#skill-navigation-row-135) before row 55 closes on the full capstone path",
            "when opening [row 195](preface.md#skill-navigation-row-195) before row 55 closes on the full capstone path",
            1,
        )
        preface = preface.replace(copper, "\n" + b["row195_preface"] + copper)
        preface_path.write_text(preface)
        print("preface: added row 195")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-195" not in prologue:
        needle = "| Row 68 → Row 174 Row 68 → Row 54 export meta prelude capstone reunion (row 194) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 194 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "row-195-closing-stitch" not in prologue:
            prologue = prologue.replace(
                "**Row 175 closing stitch",
                b["prologue_stitch"] + "**Row 175 closing stitch",
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-194"></span>Row 194 preview'
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW194_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW194_STITCH_OLD, ROW194_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 195")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "### Row 195 closing loop" not in epilogue:
        if ROW194_EPILOGUE_PROCEED_OLD in epilogue:
            epilogue = epilogue.replace(ROW194_EPILOGUE_PROCEED_OLD, ROW194_EPILOGUE_PROCEED_NEW, 1)
        marker = "### Row 186 closing loop (Row 68 → Row 166 Row 68 → Row 66 Writings canonical meta prelude capstone reunion)"
        if marker not in epilogue:
            raise SystemExit("epilogue row 186 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 195")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row175-electronic-audit-meta-prelude-capstone-reunion-index-row-195" not in sources:
        sources = sources.replace(
            "| 175 | Row 68 → Row 155 Row 68 → Row 55 electronic audit meta prelude capstone",
            b["sources_table"] + "| 175 | Row 68 → Row 155 Row 68 → Row 55 electronic audit meta prelude capstone",
            1,
        )
        sources = sources.replace(
            "## Row 68 → Row 155 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 175)",
            b["sources_index"] + "## Row 68 → Row 155 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 175)",
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 195")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-195-baby-picture-row68-row175" not in memory:
        memory = memory.replace(
            "| 194 | Meta | [Row 68 → Row 174 export meta prelude capstone reunion index]",
            b["memory_table"] + "| 194 | Meta | [Row 68 → Row 174 export meta prelude capstone reunion index]",
            1,
        )
        memory = memory.replace(
            "### Row 175 baby picture (Row 68 → Row 155 Row 68 → Row 55 electronic audit meta prelude capstone reunion) {#row-175-baby-picture-row68-row155-electronic-audit-meta-prelude-capstone-reunion}",
            b["memory_baby"]
            + "### Row 175 baby picture (Row 68 → Row 155 Row 68 → Row 55 electronic audit meta prelude capstone reunion) {#row-175-baby-picture-row68-row155-electronic-audit-meta-prelude-capstone-reunion}",
            1,
        )
        if ROW194_BABY_OLD in memory:
            memory = memory.replace(ROW194_BABY_OLD, ROW194_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 195")


if __name__ == "__main__":
    main()
