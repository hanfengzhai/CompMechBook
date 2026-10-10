#!/usr/bin/env python3
"""Add row 197 meta-stitch (Row 68 → Row 177 ↔ Row 57 Kohn–Sham meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def bump177_to_197(text: str) -> str:
    out = text.replace("row 178", "TEMP_ROW178")
    out = text.replace("row 177", "TEMP_ROW177")
    out = text.replace("row 176", "TEMP_ROW176")
    repl = [
        ("Row 68 → Row 157 Row 68 → Row 57", "Row 68 → Row 177 Row 68 → Row 57"),
        (
            "row68-row157-kohn-sham-meta-prelude-capstone-reunion-index-row-177",
            "TEMP_ROW197_KS_INDEX",
        ),
        (
            "row-177-baby-picture-row68-row157-kohn-sham-meta-prelude-capstone-reunion",
            "row-197-baby-picture-row68-row177-kohn-sham-meta-prelude-capstone-reunion",
        ),
        ("### Row 177 skill checkpoint", "### Row 197 skill checkpoint"),
        ("skill-navigation-row-177", "skill-navigation-row-197"),
        ("prologue-preview-row-177", "prologue-preview-row-197"),
        ("row-177-closing-stitch", "row-197-closing-stitch"),
        ("row-177-closing-loop", "row-197-closing-loop"),
        ("Row 177 three-way audit", "Row 197 three-way audit"),
        (
            "[row 176](preface.md#skill-navigation-row-176) or [row 157](preface.md#skill-navigation-row-157)",
            "[row 196](preface.md#skill-navigation-row-196) or [row 177](preface.md#skill-navigation-row-177)",
        ),
        (
            "[row 176](preface.md#skill-navigation-row-176) or [Row 68 → Row 157 Kohn–Sham meta prelude capstone reunion index (row 177)](appendix/sources.md#row68-row157-kohn-sham-meta-prelude-capstone-reunion-index-row-177)",
            "[row 196](preface.md#skill-navigation-row-196) or [Row 68 → Row 177 Kohn–Sham meta prelude capstone reunion index (row 197)](appendix/sources.md#row68-row177-kohn-sham-meta-prelude-capstone-reunion-index-row-197)",
        ),
        (
            "verified Born–Oppenheimer meta prelude capstone closure (row 176)",
            "verified Born–Oppenheimer meta prelude capstone closure (row 196)",
        ),
        (
            "before row 178 DFT workflows meta prelude capstone reunion opens on the full capstone path",
            "before row 198 DFT workflows meta prelude capstone reunion opens on the full capstone path",
        ),
        (
            "before row 138 DFT workflows meta prelude capstone opens in workflow time on the full capstone path",
            "before row 158 DFT workflows meta prelude capstone opens in workflow time on the full capstone path",
        ),
        (
            "before row 179 Handshake 3 meta prelude capstone reunion opens on the full capstone path",
            "before row 199 Handshake 3 meta prelude capstone reunion opens on the full capstone path",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW197_KS_INDEX",
        "row68-row177-kohn-sham-meta-prelude-capstone-reunion-index-row-197",
    )
    out = out.replace("TEMP_ROW176", "row 196")
    out = out.replace("TEMP_ROW177", "row 197")
    out = out.replace("TEMP_ROW178", "row 178")
    out = out.replace("skill-navigation-row-157", "TEMP_SKILL_157")
    out = out.replace("Row 177", "Row 197")
    out = out.replace("row 177", "row 197")
    out = out.replace("TEMP_SKILL_157", "skill-navigation-row-157")
    out = out.replace("[row 197](preface.md#skill-navigation-row-196)", "[row 196](preface.md#skill-navigation-row-196)")
    out = out.replace("[row 197](preface.md#skill-navigation-row-177)", "[row 177](preface.md#skill-navigation-row-177)")
    out = out.replace("when row 176 closed but row 57", "when row 196 closed but row 57")
    out = out.replace("When row 197 closed", "When row 196 closed")
    out = out.replace("after row 197 alone", "after row 196 alone")
    out = out.replace("Recite [preface row 197]", "Recite [preface row 196]")
    out = out.replace("row 197 or row 157 recited", "row 196 or row 177 recited")
    out = out.replace("row 176 or row 157 recited", "row 196 or row 177 recited")
    out = out.replace("row 157", "row 177")
    out = out.replace("Row 157", "Row 177")
    out = out.replace("row 137", "row 157")
    out = out.replace("Row 137", "Row 157")
    out = out.replace(
        "row68-row137-kohn-sham-meta-prelude-capstone-reunion-index-row-157",
        "row68-row157-kohn-sham-meta-prelude-capstone-reunion-index-row-177",
    )
    out = out.replace(
        "row68-row156-born-oppenheimer-meta-prelude-capstone-reunion-index-row-176",
        "row68-row176-born-oppenheimer-meta-prelude-capstone-reunion-index-row-196",
    )
    out = out.replace("Row 68 → Row 197 Row 68 → Row 57", "Row 68 → Row 177 Row 68 → Row 57")
    out = out.replace("memory sheet row 177 baby picture", "memory sheet row 197 baby picture")
    out = out.replace("prologue row 177 closing stitch", "prologue row 197 closing stitch")
    out = out.replace("prologue row 177 preview", "prologue row 197 preview")
    out = out.replace("epilogue row 177 closing loop", "epilogue row 197 closing loop")
    out = out.replace("opening [row 178]", "opening [row 198]")
    out = out.replace("skill-navigation-row-178", "skill-navigation-row-198")
    out = out.replace(
        "Prologue preview ([row 177](prologue/00-many-scales.md#prologue-preview-row-197))",
        "Prologue preview ([row 197](prologue/00-many-scales.md#prologue-preview-row-197))",
    )
    out = out.replace("row 175 or row 176 recited", "row 195 or row 196 recited")
    return out


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    memory = (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text()

    start = preface.index("### Row 177 skill checkpoint")
    end = preface.index("\n\n### Row 178 skill checkpoint", start)
    row197_preface = bump177_to_197(preface[start:end]) + "\n\n"

    row177_stitch = next(line for line in prologue.splitlines() if line.startswith("**Row 177 closing stitch"))

    prologue_compass = (
        "| Row 68 → Row 177 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion (row 197) | "
        "[Preface: row 197 skill checkpoint](../preface.md#skill-navigation-row-197) · "
        "[Row 68 → Row 177 Kohn–Sham meta prelude capstone reunion index](../appendix/sources.md#row68-row177-kohn-sham-meta-prelude-capstone-reunion-index-row-197) · "
        "[memory sheet row 197 baby picture](../appendix/memory-sheet.md#row-197-baby-picture-row68-row177-kohn-sham-meta-prelude-capstone-reunion) · "
        "[prologue row 197 preview row](#prologue-preview-row-197); [prologue row 197 closing stitch](#row-197-closing-stitch); "
        "[epilogue row 197 closing loop](../epilogue/multiscale.md#row-197-closing-loop) — "
        "read row 68 gate + row 196 or row 177 Born–Oppenheimer meta prelude capstone / Kohn–Sham opening gate + IX.1 Bridge → opening hinge → IX.2 Kohn–Sham SCF + row 57 meta aloud "
        "when Murnaghan fits are clean on the full capstone path but Kohn–Sham SCF still feels like standalone quantum chemistry after verified Born–Oppenheimer meta prelude capstone |\n"
    )

    prologue_preview = (
        '| <span id="prologue-preview-row-197"></span>Row 197 preview (Row 68 → Row 177 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion) | '
        "Explain why midpoint closure (row 68) and IX.1 → IX.2 meta (row 57) must be read together with the Bridge → SCF chain after verified Born–Oppenheimer meta prelude capstone before Murnaghan yaml and Kohn–Sham feel like separate courses on the full capstone path | "
        'One sentence: "read row 68 gate + row 196 or row 177 Born–Oppenheimer meta prelude capstone / Kohn–Sham opening gate + IX.1 Bridge → opening hinge → IX.2 Kohn–Sham SCF + row 57 meta aloud when Murnaghan fits are clean on the full capstone path but Kohn–Sham SCF still feels like standalone quantum chemistry after verified Born–Oppenheimer meta prelude capstone" — '
        "[preface row 197 skill checkpoint](../preface.md#skill-navigation-row-197); [prologue row 197 closing stitch](#row-197-closing-stitch); "
        "[Row 68 → Row 177 reunion index](../appendix/sources.md#row68-row177-kohn-sham-meta-prelude-capstone-reunion-index-row-197); "
        "[memory sheet row 197 baby picture](../appendix/memory-sheet.md#row-197-baby-picture-row68-row177-kohn-sham-meta-prelude-capstone-reunion); "
        "[IX.1 Bridge → opening hinge → IX.2 Kohn–Sham SCF](../part09-dft/01-born-oppenheimer.md#bridge); "
        "[IX.2 opening hinge from IX.1](../part09-dft/02-kohn-sham.md#opening-hinge-ix1-to-ix2); "
        "[preface row 57 skill checkpoint](../preface.md#skill-navigation-row-57); "
        "[preface row 196 skill checkpoint](../preface.md#skill-navigation-row-196); "
        "[epilogue row 197 closing loop](../epilogue/multiscale.md#row-197-closing-loop) |\n"
    )

    epilogue_loop = bump177_to_197(
        "### Row 177 closing loop"
        + epilogue.split("### Row 177 closing loop")[1].split("### Row 178 closing loop")[0]
    )

    sources_table = (
        "| 197 | Row 68 → Row 177 Row 68 → Row 57 Kohn–Sham meta prelude capstone (midpoint prelude gate ↔ Born–Oppenheimer meta prelude capstone on full capstone path ↔ row 57 meta) | "
        "[Row 68 → Row 177 Kohn–Sham meta prelude capstone reunion index](#row68-row177-kohn-sham-meta-prelude-capstone-reunion-index-row-197) · "
        "[preface row 197](../preface.md#skill-navigation-row-197) · "
        "[prologue row 197 preview](../prologue/00-many-scales.md#prologue-preview-row-197) · "
        "[prologue row 197 closing stitch](../prologue/00-many-scales.md#row-197-closing-stitch) · "
        "[epilogue row 197 closing loop](../epilogue/multiscale.md#row-197-closing-loop) · "
        "[memory sheet row 197 baby picture](memory-sheet.md#row-197-baby-picture-row68-row177-kohn-sham-meta-prelude-capstone-reunion) | "
        "Row 68 closed but **row 57 IX.1 → IX.2 opening hinge still feels disconnected from verified Born–Oppenheimer meta prelude capstone on the full capstone path** — "
        "read row 68 + row 196 or row 177 gate + IX.1 Bridge → opening hinge → IX.2 Kohn–Sham SCF + row 57; "
        "[preface row 57](../preface.md#skill-navigation-row-57) |\n"
    )

    sources_index = bump177_to_197(
        sources.split("## Row 68 → Row 157 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion index (row 177)")[1]
        .split("## Row 68 → Row 158 Row 68 → Row 58 DFT workflows meta prelude capstone reunion index (row 178)")[0]
    )
    sources_index = (
        "## Row 68 → Row 177 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion index (row 197)"
        + sources_index
    )

    memory_table = (
        "| 197 | Meta | [Row 68 → Row 177 Kohn–Sham meta prelude capstone reunion index](sources.md#row68-row177-kohn-sham-meta-prelude-capstone-reunion-index-row-197) · "
        "[preface row 197 skill checkpoint](../preface.md#skill-navigation-row-197) · "
        "[prologue row 197 preview](../prologue/00-many-scales.md#prologue-preview-row-197) · "
        "[prologue row 197 closing stitch](../prologue/00-many-scales.md#row-197-closing-stitch) · "
        "[epilogue row 197 closing loop](../epilogue/multiscale.md#row-197-closing-loop) | "
        "Row 68 closed but row 57 IX.1 → IX.2 opening hinge feels disconnected from verified Born–Oppenheimer meta prelude capstone on the full capstone path — "
        "read row 68 + row 196 or row 177 gate + IX.1 Bridge → opening hinge → IX.2 Kohn–Sham SCF + row 57; "
        "[row 197 baby picture](#row-197-baby-picture-row68-row177-kohn-sham-meta-prelude-capstone-reunion) |\n"
    )

    memory_baby = bump177_to_197(
        memory.split("### Row 177 baby picture (Row 68 → Row 157 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion)")[1]
        .split("### Row 158 baby picture")[0]
    )
    memory_baby = (
        "### Row 197 baby picture (Row 68 → Row 177 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion)"
        + memory_baby.split(")", 1)[1]
    )

    return {
        "row197_preface": row197_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": bump177_to_197(row177_stitch) + "\n\n",
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_table": memory_table,
        "memory_baby": memory_baby,
    }


ROW196_TAIL_OLD = (
    "When row 196 is complete, proceed to [row 157](preface.md#skill-navigation-row-157) when `murnaghan_eos.yaml` exists but IX.2 still feels disconnected from verified Born–Oppenheimer meta prelude capstone on the full capstone path, to [row 137](preface.md#skill-navigation-row-137) when `murnaghan_eos.yaml` exists but IX.2 still feels disconnected on the opening-hinge capstone path alone, to [row 156](preface.md#skill-navigation-row-136) for the Row 68 ↔ Row 56 Born–Oppenheimer meta audit on the opening-hinge prelude path alone, to [row 115](preface.md#skill-navigation-row-115) for the Row 68 ↔ Row 55 electronic audit meta audit on the opening-hinge prelude path alone, to [row 154](preface.md#skill-navigation-row-154) when `cu.relax.out` is missing after verified export meta prelude capstone on the full capstone path, to [row 134](preface.md#skill-navigation-row-134) for the Row 68 ↔ Row 54 export meta audit on the opening-hinge capstone path alone, to [row 176](preface.md#skill-navigation-row-156) for the Row 68 ↔ Row 56 Born–Oppenheimer meta audit on the opening-hinge capstone path alone, to [row 195](preface.md#skill-navigation-row-155) when foundation SCF is clean but Born–Oppenheimer still stalls on the full capstone path, to [row 56](preface.md#skill-navigation-row-56) when only IX.0 → IX.1 stalls, or extend prose only under `writings/` then sync."
)
ROW196_TAIL_NEW = (
    "When row 196 is complete, proceed to [row 197](preface.md#skill-navigation-row-197) when `murnaghan_eos.yaml` exists on the full capstone path, to [row 177](preface.md#skill-navigation-row-177) when `murnaghan_eos.yaml` exists but IX.2 still feels disconnected from verified Born–Oppenheimer meta prelude capstone on the opening-hinge capstone path alone, to [row 157](preface.md#skill-navigation-row-157) for the Row 68 ↔ Row 57 Kohn–Sham meta audit on the opening-hinge prelude path alone, to [row 176](preface.md#skill-navigation-row-176) for the Row 68 ↔ Row 56 Born–Oppenheimer meta audit on the opening-hinge capstone path alone, to [row 194](preface.md#skill-navigation-row-194) when `cu.relax.out` is missing after verified export meta prelude capstone on the full capstone path, to [row 57](preface.md#skill-navigation-row-57) when only IX.1 → IX.2 stalls, or extend prose only under `writings/` then sync."
)

ROW196_STITCH_OLD = (
    "before row 177 Kohn–Sham meta prelude capstone reunion opens on the full capstone path."
)
ROW196_STITCH_NEW = (
    "before row 197 Kohn–Sham meta prelude capstone reunion opens on the full capstone path."
)

ROW196_EPILOGUE_PROCEED_OLD = (
    "Proceed to [row 197](#row-177-closing-loop) when row 68 closed but Kohn–Sham meta prelude capstone still lags after row 196 on the full capstone path,"
)
ROW196_EPILOGUE_PROCEED_NEW = (
    "Proceed to [row 197](#row-197-closing-loop) when row 68 closed but Kohn–Sham meta prelude capstone still lags after row 196 on the full capstone path,"
)

ROW196_BABY_OLD = (
    "row 196 when **IX.1 Bridge and Row 68 → Row 57 meta must read on the same wire before row 177 Kohn–Sham meta prelude capstone opens on the full capstone path**"
)
ROW196_BABY_NEW = (
    "row 196 when **IX.1 Bridge and Row 68 → Row 57 meta must read on the same wire before row 197 Kohn–Sham meta prelude capstone opens on the full capstone path**"
)


def main() -> None:
    b = _build_blocks()

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "### Row 197 skill checkpoint" in preface and preface.index("### Row 197 skill checkpoint") < preface.index(
        copper
    ):
        print("preface: row 197 already present")
    else:
        if ROW196_TAIL_OLD not in preface:
            raise SystemExit("row 196 tail proceed string not found")
        preface = preface.replace(ROW196_TAIL_OLD, ROW196_TAIL_NEW, 1)
        preface = preface.replace(
            "when opening [row 157](preface.md#skill-navigation-row-157) before row 56 closes on the full capstone path",
            "when opening [row 197](preface.md#skill-navigation-row-197) before row 57 closes on the full capstone path",
            1,
        )
        preface = preface.replace(copper, "\n" + b["row197_preface"] + copper)
        preface_path.write_text(preface)
        print("preface: added row 197")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-197" not in prologue:
        needle = "| Row 68 → Row 176 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion (row 196) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 196 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "row-197-closing-stitch" not in prologue:
            prologue = prologue.replace(
                "**Row 177 closing stitch",
                b["prologue_stitch"] + "**Row 177 closing stitch",
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-196"></span>Row 196 preview'
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW196_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW196_STITCH_OLD, ROW196_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 197")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "### Row 197 closing loop" not in epilogue:
        if ROW196_EPILOGUE_PROCEED_OLD in epilogue:
            epilogue = epilogue.replace(ROW196_EPILOGUE_PROCEED_OLD, ROW196_EPILOGUE_PROCEED_NEW, 1)
        marker = "### Row 186 closing loop (Row 68 → Row 166 Row 68 → Row 66 Writings canonical meta prelude capstone reunion)"
        if marker not in epilogue:
            raise SystemExit("epilogue row 186 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 197")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row177-kohn-sham-meta-prelude-capstone-reunion-index-row-197" not in sources:
        sources = sources.replace(
            "| 177 | Row 68 → Row 157 Row 68 → Row 57 Kohn–Sham meta prelude capstone",
            b["sources_table"] + "| 177 | Row 68 → Row 157 Row 68 → Row 57 Kohn–Sham meta prelude capstone",
            1,
        )
        sources = sources.replace(
            "## Row 68 → Row 157 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion index (row 177)",
            b["sources_index"] + "## Row 68 → Row 157 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion index (row 177)",
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 197")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-197-baby-picture-row68-row177" not in memory:
        memory = memory.replace(
            "| 196 | Meta | [Row 68 → Row 176 Born–Oppenheimer meta prelude capstone reunion index]",
            b["memory_table"] + "| 196 | Meta | [Row 68 → Row 176 Born–Oppenheimer meta prelude capstone reunion index]",
            1,
        )
        memory = memory.replace(
            "### Row 177 baby picture (Row 68 → Row 157 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion)",
            b["memory_baby"]
            + "### Row 177 baby picture (Row 68 → Row 157 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion)",
            1,
        )
        if ROW196_BABY_OLD in memory:
            memory = memory.replace(ROW196_BABY_OLD, ROW196_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 197")


if __name__ == "__main__":
    main()
