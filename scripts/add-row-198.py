#!/usr/bin/env python3
"""Add row 198 meta-stitch (Row 68 → Row 178 ↔ Row 58 DFT workflows meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def bump178_to_198(text: str) -> str:
    out = text.replace("row 199", "TEMP_ROW199")
    out = text.replace("row 198", "TEMP_ROW198")
    out = text.replace("row 179", "TEMP_ROW179")
    out = text.replace("row 178", "TEMP_ROW178")
    out = text.replace("row 197", "TEMP_ROW197")
    repl = [
        ("Row 68 → Row 158 Row 68 → Row 58", "Row 68 → Row 178 Row 68 → Row 58"),
        (
            "row68-row158-dft-workflows-meta-prelude-capstone-reunion-index-row-178",
            "TEMP_ROW198_DFT_INDEX",
        ),
        (
            "row-178-baby-picture-row68-row158-dft-workflows-meta-prelude-capstone-reunion",
            "row-198-baby-picture-row68-row178-dft-workflows-meta-prelude-capstone-reunion",
        ),
        ("### Row 178 skill checkpoint", "### Row 198 skill checkpoint"),
        ("skill-navigation-row-178", "skill-navigation-row-198"),
        ("prologue-preview-row-178", "prologue-preview-row-198"),
        ("row-178-closing-stitch", "row-198-closing-stitch"),
        ("row-178-closing-loop", "row-198-closing-loop"),
        ("Row 178 three-way audit", "Row 198 three-way audit"),
        (
            "[row 177](preface.md#skill-navigation-row-177) or [row 158](preface.md#skill-navigation-row-158)",
            "[row 197](preface.md#skill-navigation-row-197) or [row 178](preface.md#skill-navigation-row-178)",
        ),
        (
            "[row 177](preface.md#skill-navigation-row-177) or [Row 68 → Row 158 DFT workflows meta prelude capstone reunion index (row 178)](appendix/sources.md#row68-row158-dft-workflows-meta-prelude-capstone-reunion-index-row-178)",
            "[row 197](preface.md#skill-navigation-row-197) or [Row 68 → Row 178 DFT workflows meta prelude capstone reunion index (row 198)](appendix/sources.md#row68-row178-dft-workflows-meta-prelude-capstone-reunion-index-row-198)",
        ),
        (
            "verified Kohn–Sham meta prelude capstone closure (row 177)",
            "verified Kohn–Sham meta prelude capstone closure (row 197)",
        ),
        (
            "before row 179 Handshake 3 meta prelude capstone reunion opens on the full capstone path",
            "before row 199 Handshake 3 meta prelude capstone reunion opens on the full capstone path",
        ),
        (
            "before row 159 Handshake 3 meta prelude capstone opens on the full capstone path",
            "before row 179 Handshake 3 meta prelude capstone opens on the full capstone path",
        ),
        (
            "before row 139 Handshake 3 meta prelude capstone opens on the full capstone path",
            "before row 159 Handshake 3 meta prelude capstone opens on the full capstone path",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW198_DFT_INDEX",
        "row68-row178-dft-workflows-meta-prelude-capstone-reunion-index-row-198",
    )
    out = out.replace("TEMP_ROW197", "row 197")
    out = out.replace("TEMP_ROW178", "row 198")
    out = out.replace("TEMP_ROW179", "row 179")
    out = out.replace("TEMP_ROW198", "row 198")
    out = out.replace("TEMP_ROW199", "row 199")
    out = out.replace("skill-navigation-row-158", "TEMP_SKILL_158")
    out = out.replace("Row 178", "Row 198")
    out = out.replace("row 178", "row 198")
    out = out.replace("TEMP_SKILL_158", "skill-navigation-row-158")
    out = out.replace("[row 198](preface.md#skill-navigation-row-197)", "[row 197](preface.md#skill-navigation-row-197)")
    out = out.replace("[row 198](preface.md#skill-navigation-row-178)", "[row 178](preface.md#skill-navigation-row-178)")
    out = out.replace("when row 177 closed but row 58", "when row 197 closed but row 58")
    out = out.replace("When row 198 closed", "When row 197 closed")
    out = out.replace("after row 198 alone", "after row 197 alone")
    out = out.replace("Recite [preface row 198]", "Recite [preface row 197]")
    out = out.replace("row 198 or row 158 recited", "row 197 or row 178 recited")
    out = out.replace("row 177 or row 158 recited", "row 197 or row 178 recited")
    out = out.replace("when row 177 closed Kohn", "when row 197 closed Kohn")
    out = out.replace("When row 177 closed — Kohn", "When row 197 closed — Kohn")
    out = out.replace("row 158", "row 178")
    out = out.replace("Row 158", "Row 178")
    out = out.replace("row 138", "row 158")
    out = out.replace("Row 138", "Row 158")
    out = out.replace("row 118", "row 138")
    out = out.replace("Row 118", "Row 138")
    out = out.replace(
        "row68-row138-dft-workflows-meta-prelude-capstone-reunion-index-row-158",
        "row68-row158-dft-workflows-meta-prelude-capstone-reunion-index-row-178",
    )
    out = out.replace(
        "row68-row157-kohn-sham-meta-prelude-capstone-reunion-index-row-177",
        "row68-row177-kohn-sham-meta-prelude-capstone-reunion-index-row-197",
    )
    out = out.replace("Row 68 → Row 198 Row 68 → Row 58", "Row 68 → Row 178 Row 68 → Row 58")
    out = out.replace("memory sheet row 178 baby picture", "memory sheet row 198 baby picture")
    out = out.replace("prologue row 178 closing stitch", "prologue row 198 closing stitch")
    out = out.replace("prologue row 178 preview", "prologue row 198 preview")
    out = out.replace("epilogue row 178 closing loop", "epilogue row 198 closing loop")
    out = out.replace("opening [row 179]", "opening [row 199]")
    out = out.replace("skill-navigation-row-179", "skill-navigation-row-199")
    out = out.replace(
        "Prologue preview ([row 178](prologue/00-many-scales.md#prologue-preview-row-198))",
        "Prologue preview ([row 198](prologue/00-many-scales.md#prologue-preview-row-198))",
    )
    out = out.replace("after row 177 on the full capstone path", "after row 197 on the full capstone path")
    out = out.replace("row 177's SCF fixed-point", "row 197's SCF fixed-point")
    out = out.replace("row 177 tells you", "row 197 tells you")
    out = out.replace("from row 198's", "from row 197's")
    out = out.replace("Scene after row 177.", "Scene after row 197.")
    out = out.replace("after row 177 alone", "after row 197 alone")
    out = out.replace("when row 177 and row 58", "when row 197 and row 58")
    return out


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    memory = (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text()

    start = preface.index("### Row 178 skill checkpoint")
    end = preface.index("\n\n### Row 179 skill checkpoint", start)
    row198_preface = bump178_to_198(preface[start:end]) + "\n\n"

    row178_stitch = next(line for line in prologue.splitlines() if line.startswith("**Row 178 closing stitch"))

    prologue_compass = (
        "| Row 68 → Row 178 Row 68 → Row 58 DFT workflows meta prelude capstone reunion (row 198) | "
        "[Preface: row 198 skill checkpoint](../preface.md#skill-navigation-row-198) · "
        "[Row 68 → Row 178 DFT workflows meta prelude capstone reunion index](../appendix/sources.md#row68-row178-dft-workflows-meta-prelude-capstone-reunion-index-row-198) · "
        "[memory sheet row 198 baby picture](../appendix/memory-sheet.md#row-198-baby-picture-row68-row178-dft-workflows-meta-prelude-capstone-reunion) · "
        "[prologue row 198 preview row](#prologue-preview-row-198); [prologue row 198 closing stitch](#row-198-closing-stitch); "
        "[epilogue row 198 closing loop](../epilogue/multiscale.md#row-198-closing-loop) — "
        "read row 68 gate + row 197 or row 178 Kohn–Sham meta prelude capstone / DFT workflows opening gate + IX.2 Bridge → opening hinge → IX.3 calculation ladder + row 58 meta aloud "
        "when cutoff certificates are clean on the full capstone path but DFT workflows still feel like standalone coursework after verified Kohn–Sham meta prelude capstone |\n"
    )

    prologue_preview = (
        '| <span id="prologue-preview-row-198"></span>Row 198 preview (Row 68 → Row 178 Row 68 → Row 58 DFT workflows meta prelude capstone reunion) | '
        "Explain why midpoint closure (row 68) and IX.2 → IX.3 meta (row 58) must be read together with the Bridge → calculation ladder chain after verified Kohn–Sham meta prelude capstone before cutoff certificates and `cu.foundation/` feel like separate courses on the full capstone path | "
        'One sentence: "read row 68 gate + row 197 or row 178 Kohn–Sham meta prelude capstone / DFT workflows opening gate + IX.2 Bridge → opening hinge → IX.3 calculation ladder + row 58 meta aloud when cutoff certificates are clean on the full capstone path but DFT workflows still feel like standalone coursework after verified Kohn–Sham meta prelude capstone" — '
        "[preface row 198 skill checkpoint](../preface.md#skill-navigation-row-198); [prologue row 198 closing stitch](#row-198-closing-stitch); "
        "[Row 68 → Row 178 reunion index](../appendix/sources.md#row68-row178-dft-workflows-meta-prelude-capstone-reunion-index-row-198); "
        "[memory sheet row 198 baby picture](../appendix/memory-sheet.md#row-198-baby-picture-row68-row178-dft-workflows-meta-prelude-capstone-reunion); "
        "[IX.2 Bridge → opening hinge → IX.3 calculation ladder](../part09-dft/02-kohn-sham.md#bridge); "
        "[IX.3 opening hinge from IX.2](../part09-dft/03-dft-workflows.md#opening-hinge-ix2-to-ix3); "
        "[preface row 58 skill checkpoint](../preface.md#skill-navigation-row-58); "
        "[preface row 197 skill checkpoint](../preface.md#skill-navigation-row-197); "
        "[epilogue row 198 closing loop](../epilogue/multiscale.md#row-198-closing-loop) |\n"
    )

    epilogue_loop = bump178_to_198(
        "### Row 178 closing loop"
        + epilogue.split("### Row 178 closing loop")[1].split("### Row 179 closing loop")[0]
    )

    sources_table = (
        "| 198 | Row 68 → Row 178 Row 68 → Row 58 DFT workflows meta prelude capstone (midpoint prelude gate ↔ Kohn–Sham meta prelude capstone on full capstone path ↔ row 58 meta) | "
        "[Row 68 → Row 178 DFT workflows meta prelude capstone reunion index](#row68-row178-dft-workflows-meta-prelude-capstone-reunion-index-row-198) · "
        "[preface row 198](../preface.md#skill-navigation-row-198) · "
        "[prologue row 198 preview](../prologue/00-many-scales.md#prologue-preview-row-198) · "
        "[prologue row 198 closing stitch](../prologue/00-many-scales.md#row-198-closing-stitch) · "
        "[epilogue row 198 closing loop](../epilogue/multiscale.md#row-198-closing-loop) · "
        "[memory sheet row 198 baby picture](memory-sheet.md#row-198-baby-picture-row68-row178-dft-workflows-meta-prelude-capstone-reunion) | "
        "Row 68 closed but **row 58 IX.2 → IX.3 opening hinge still feels disconnected from verified Kohn–Sham meta prelude capstone on the full capstone path** — "
        "read row 68 + row 197 or row 178 gate + IX.2 Bridge → opening hinge → IX.3 calculation ladder + row 58; "
        "[preface row 58](../preface.md#skill-navigation-row-58) |\n"
    )

    sources_index = bump178_to_198(
        sources.split("## Row 68 → Row 158 Row 68 → Row 58 DFT workflows meta prelude capstone reunion index (row 178)")[1]
        .split("## Row 68 → Row 138 Row 68 → Row 58 DFT workflows meta prelude capstone reunion index (row 158)")[0]
    )
    sources_index = (
        "## Row 68 → Row 178 Row 68 → Row 58 DFT workflows meta prelude capstone reunion index (row 198)"
        + sources_index
    )

    memory_table = (
        "| 198 | Meta | [Row 68 → Row 178 DFT workflows meta prelude capstone reunion index](sources.md#row68-row178-dft-workflows-meta-prelude-capstone-reunion-index-row-198) · "
        "[preface row 198 skill checkpoint](../preface.md#skill-navigation-row-198) · "
        "[prologue row 198 preview](../prologue/00-many-scales.md#prologue-preview-row-198) · "
        "[prologue row 198 closing stitch](../prologue/00-many-scales.md#row-198-closing-stitch) · "
        "[epilogue row 198 closing loop](../epilogue/multiscale.md#row-198-closing-loop) | "
        "Row 68 closed but row 58 IX.2 → IX.3 opening hinge feels disconnected from verified Kohn–Sham meta prelude capstone on the full capstone path — "
        "read row 68 + row 197 or row 178 gate + IX.2 Bridge → opening hinge → IX.3 calculation ladder + row 58; "
        "[row 198 baby picture](#row-198-baby-picture-row68-row178-dft-workflows-meta-prelude-capstone-reunion) |\n"
    )

    memory_baby = bump178_to_198(
        memory.split("### Row 178 baby picture (Row 68 → Row 158 Row 68 → Row 58 DFT workflows meta prelude capstone reunion)")[1]
        .split("### Row 159 baby picture")[0]
    )
    memory_baby = (
        "### Row 198 baby picture (Row 68 → Row 178 Row 68 → Row 58 DFT workflows meta prelude capstone reunion)"
        + memory_baby.split(")", 1)[1]
    )

    return {
        "row198_preface": row198_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": bump178_to_198(row178_stitch) + "\n\n",
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_table": memory_table,
        "memory_baby": memory_baby,
    }


ROW197_TAIL_OLD = (
    "When row 197 is complete, proceed to [row 158](preface.md#skill-navigation-row-158) when `cutoff_convergence.yaml` exists but IX.3 still feels disconnected from verified Kohn–Sham meta prelude capstone on the full capstone path, to [row 138](preface.md#skill-navigation-row-138) for the Row 68 ↔ Row 58 DFT workflows meta audit on the opening-hinge capstone path alone, to [row 118](preface.md#skill-navigation-row-118) for the Row 68 ↔ Row 58 DFT workflows meta audit on the opening-hinge prelude path alone, to [row 157](preface.md#skill-navigation-row-137) for the Row 68 ↔ Row 57 Kohn–Sham meta audit on the opening-hinge capstone path alone, to [row 177](preface.md#skill-navigation-row-157) for the Row 68 ↔ Row 57 Kohn–Sham meta audit on the opening-hinge capstone path alone, to [row 97](preface.md#skill-navigation-row-97) for the Row 68 ↔ Row 57 Kohn–Sham opening prelude audit alone, to [row 77](preface.md#skill-navigation-row-77) for the Row 68 ↔ Row 57 prelude audit alone, to [row 196](preface.md#skill-navigation-row-156) when Born–Oppenheimer meta prelude capstone still lags after verified electronic audit meta prelude capstone on the full capstone path, to [row 154](preface.md#skill-navigation-row-154) when `murnaghan_eos.yaml` is missing after verified export meta prelude capstone on the full capstone path, to [row 57](preface.md#skill-navigation-row-57) when only IX.1 → IX.2 stalls, or extend prose only under `writings/` then sync."
)
ROW197_TAIL_NEW = (
    "When row 197 is complete, proceed to [row 198](preface.md#skill-navigation-row-198) when `cutoff_convergence.yaml` exists on the full capstone path, to [row 178](preface.md#skill-navigation-row-178) when `cutoff_convergence.yaml` exists but IX.3 still feels disconnected from verified Kohn–Sham meta prelude capstone on the opening-hinge capstone path alone, to [row 158](preface.md#skill-navigation-row-158) for the Row 68 ↔ Row 58 DFT workflows meta audit on the opening-hinge prelude path alone, to [row 177](preface.md#skill-navigation-row-177) for the Row 68 ↔ Row 57 Kohn–Sham meta audit on the opening-hinge capstone path alone, to [row 196](preface.md#skill-navigation-row-196) when Born–Oppenheimer meta prelude capstone still lags after verified electronic audit meta prelude capstone on the full capstone path, to [row 58](preface.md#skill-navigation-row-58) when only IX.2 → IX.3 stalls, or extend prose only under `writings/` then sync."
)

ROW197_STITCH_OLD = (
    "before row 178 DFT workflows meta prelude capstone reunion opens on the full capstone path."
)
ROW197_STITCH_NEW = (
    "before row 198 DFT workflows meta prelude capstone reunion opens on the full capstone path."
)

ROW197_EPILOGUE_PROCEED_OLD = (
    "Proceed to [row 178](#row-178-closing-loop) when row 68 closed but DFT workflows meta prelude capstone still lags after row 197 on the full capstone path,"
)
ROW197_EPILOGUE_PROCEED_NEW = (
    "Proceed to [row 198](#row-198-closing-loop) when row 68 closed but DFT workflows meta prelude capstone still lags after row 197 on the full capstone path,"
)

ROW197_BABY_OLD = (
    "row 197 when **IX.2 Bridge and Row 68 → Row 58 meta must read on the same wire before row 178 DFT workflows meta prelude capstone opens on the full capstone path**"
)
ROW197_BABY_NEW = (
    "row 197 when **IX.2 Bridge and Row 68 → Row 58 meta must read on the same wire before row 198 DFT workflows meta prelude capstone opens on the full capstone path**"
)


def main() -> None:
    b = _build_blocks()

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "### Row 198 skill checkpoint" in preface and preface.index("### Row 198 skill checkpoint") < preface.index(
        copper
    ):
        print("preface: row 198 already present")
    else:
        if ROW197_TAIL_OLD not in preface:
            raise SystemExit("row 197 tail proceed string not found")
        preface = preface.replace(ROW197_TAIL_OLD, ROW197_TAIL_NEW, 1)
        preface = preface.replace(
            "when opening [row 158](preface.md#skill-navigation-row-158) before row 58 closes on the full capstone path",
            "when opening [row 198](preface.md#skill-navigation-row-198) before row 59 closes on the full capstone path",
            1,
        )
        preface = preface.replace(copper, "\n" + b["row198_preface"] + copper)
        preface_path.write_text(preface)
        print("preface: added row 198")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "**Row 198 closing stitch" not in prologue:
        needle = "| Row 68 → Row 177 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion (row 197) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 197 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        prologue = prologue.replace(
            "**Row 178 closing stitch",
            b["prologue_stitch"] + "**Row 178 closing stitch",
            1,
        )
        preview_anchor = '| <span id="prologue-preview-row-197"></span>Row 197 preview'
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW197_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW197_STITCH_OLD, ROW197_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 198")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "### Row 198 closing loop" not in epilogue:
        if ROW197_EPILOGUE_PROCEED_OLD in epilogue:
            epilogue = epilogue.replace(ROW197_EPILOGUE_PROCEED_OLD, ROW197_EPILOGUE_PROCEED_NEW, 1)
        marker = "### Row 186 closing loop (Row 68 → Row 166 Row 68 → Row 66 Writings canonical meta prelude capstone reunion)"
        if marker not in epilogue:
            raise SystemExit("epilogue row 186 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 198")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row178-dft-workflows-meta-prelude-capstone-reunion-index-row-198" not in sources:
        sources = sources.replace(
            "| 178 | Row 68 → Row 158 Row 68 → Row 58 DFT workflows meta prelude capstone",
            b["sources_table"] + "| 178 | Row 68 → Row 158 Row 68 → Row 58 DFT workflows meta prelude capstone",
            1,
        )
        sources = sources.replace(
            "## Row 68 → Row 158 Row 68 → Row 58 DFT workflows meta prelude capstone reunion index (row 178)",
            b["sources_index"] + "## Row 68 → Row 158 Row 68 → Row 58 DFT workflows meta prelude capstone reunion index (row 178)",
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 198")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-198-baby-picture-row68-row178" not in memory:
        memory = memory.replace(
            "| 197 | Meta | [Row 68 → Row 177 Kohn–Sham meta prelude capstone reunion index]",
            b["memory_table"] + "| 197 | Meta | [Row 68 → Row 177 Kohn–Sham meta prelude capstone reunion index]",
            1,
        )
        memory = memory.replace(
            "### Row 178 baby picture (Row 68 → Row 158 Row 68 → Row 58 DFT workflows meta prelude capstone reunion)",
            b["memory_baby"]
            + "### Row 178 baby picture (Row 68 → Row 158 Row 68 → Row 58 DFT workflows meta prelude capstone reunion)",
            1,
        )
        if ROW197_BABY_OLD in memory:
            memory = memory.replace(ROW197_BABY_OLD, ROW197_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 198")


if __name__ == "__main__":
    main()
