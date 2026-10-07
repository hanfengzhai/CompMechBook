#!/usr/bin/env python3
"""Add row 194 meta-stitch (Row 68 → Row 174 ↔ Row 54 export meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def bump174_to_194(text: str) -> str:
    """Transform row-174 capstone-path meta copy to row 194 (154→174 inner, 193 gate)."""
    out = text.replace("row 195", "TEMP_ROW195")
    repl = [
        ("Row 68 → Row 154 Row 68 → Row 54", "Row 68 → Row 174 Row 68 → Row 54"),
        (
            "row68-row154-export-meta-prelude-capstone-reunion-index-row-174",
            "TEMP_ROW194_EXP_INDEX",
        ),
        (
            "row-174-baby-picture-row68-row154-export-meta-prelude-capstone-reunion",
            "row-194-baby-picture-row68-row174-export-meta-prelude-capstone-reunion",
        ),
        ("### Row 174 skill checkpoint", "### Row 194 skill checkpoint"),
        ("skill-navigation-row-174", "skill-navigation-row-194"),
        ("prologue-preview-row-174", "prologue-preview-row-194"),
        ("row-174-closing-stitch", "row-194-closing-stitch"),
        ("row-174-closing-loop", "row-194-closing-loop"),
        ("Row 174 three-way audit", "Row 194 three-way audit"),
        (
            "[row 173](preface.md#skill-navigation-row-173) or [row 154](preface.md#skill-navigation-row-154)",
            "[row 193](preface.md#skill-navigation-row-193) or [row 174](preface.md#skill-navigation-row-174)",
        ),
        (
            "[row 173](preface.md#skill-navigation-row-173) or [Row 68 → Row 154 export meta prelude capstone reunion index (row 174)](appendix/sources.md#row68-row154-export-meta-prelude-capstone-reunion-index-row-174)",
            "[row 193](preface.md#skill-navigation-row-193) or [Row 68 → Row 174 export meta prelude capstone reunion index (row 194)](appendix/sources.md#row68-row174-export-meta-prelude-capstone-reunion-index-row-194)",
        ),
        (
            "verified dynamics meta prelude capstone closure (row 173)",
            "verified dynamics meta prelude capstone closure (row 193)",
        ),
        (
            "before row 175 electronic audit meta prelude capstone reunion opens on the full capstone path",
            "before row 195 electronic audit meta prelude capstone reunion opens on the full capstone path",
        ),
        (
            "before row 176 Born–Oppenheimer meta prelude capstone reunion opens on the full capstone path",
            "before row 196 Born–Oppenheimer meta prelude capstone reunion opens on the full capstone path",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW194_EXP_INDEX",
        "row68-row174-export-meta-prelude-capstone-reunion-index-row-194",
    )
    out = out.replace("skill-navigation-row-154", "TEMP_SKILL_NAV_154")
    out = out.replace("row 174", "row 194")
    out = out.replace("Row 174", "Row 194")
    out = out.replace("TEMP_SKILL_NAV_154", "skill-navigation-row-154")
    out = out.replace("[row 194](preface.md#skill-navigation-row-193)", "[row 193](preface.md#skill-navigation-row-193)")
    out = out.replace("[row 194](preface.md#skill-navigation-row-174)", "[row 174](preface.md#skill-navigation-row-174)")
    out = out.replace("[row 174](preface.md#skill-navigation-row-194)", "[row 174](preface.md#skill-navigation-row-174)")
    out = out.replace("when row 173 closed but row 54", "when row 193 closed but row 54")
    out = out.replace("When row 194 closed", "When row 193 closed")
    out = out.replace("after row 194 alone", "after row 193 alone")
    out = out.replace("Recite [preface row 194]", "Recite [preface row 193]")
    out = out.replace("row 194 or row 154 recited", "row 193 or row 174 recited")
    out = out.replace("row 173 or row 154 recited", "row 193 or row 174 recited")
    out = out.replace("when row 173 and row 54", "when row 193 and row 54")
    out = out.replace("after row 173 alone", "after row 193 alone")
    out = out.replace("from row 194's", "from row 193's")
    out = out.replace("row 173's finite-\\(T\\) dynamics", "row 193's finite-\\(T\\) dynamics")
    out = out.replace("row 173 tells you", "row 193 tells you")
    out = out.replace("(preface.md#skill-navigation-row-154)", "(preface.md#skill-navigation-row-174)")
    out = out.replace(
        "Row 68 → Row 194 export meta prelude capstone reunion index",
        "Row 68 → Row 174 export meta prelude capstone reunion index",
    )
    out = out.replace("row 154", "row 174")
    out = out.replace("Row 154", "Row 174")
    out = out.replace("row 134", "row 154")
    out = out.replace("Row 134", "Row 154")
    out = out.replace("row 114", "row 134")
    out = out.replace("Row 114", "Row 134")
    out = out.replace(
        "row68-row114-export-meta-prelude-reunion-index-row-134",
        "row68-row134-export-meta-prelude-capstone-reunion-index-row-154",
    )
    out = out.replace(
        "row68-row134-export-meta-prelude-capstone-reunion-index-row-154",
        "row68-row154-export-meta-prelude-capstone-reunion-index-row-174",
    )
    out = out.replace(
        "row68-row153-dynamics-meta-prelude-capstone-reunion-index-row-173",
        "row68-row173-dynamics-meta-prelude-capstone-reunion-index-row-193",
    )
    out = out.replace("Row 68 → Row 194 Row 68 → Row 54", "Row 68 → Row 174 Row 68 → Row 54")
    out = out.replace(
        "[preface row 174](../preface.md#skill-navigation-row-154)",
        "[preface row 174](../preface.md#skill-navigation-row-174)",
    )
    out = out.replace(
        "Confirm [row 173](preface.md#skill-navigation-row-173) or [Row 68 → Row 174",
        "Confirm [row 193](preface.md#skill-navigation-row-193) or [Row 68 → Row 174",
    )
    out = out.replace(
        "and [row 173](preface.md#skill-navigation-row-173) or [row 174]",
        "and [row 193](preface.md#skill-navigation-row-193) or [row 174]",
    )
    out = out.replace("[row 134](preface.md#skill-navigation-row-114)", "[row 134](preface.md#skill-navigation-row-134)")
    out = out.replace("(preface.md#skill-navigation-row-194) when NPT", "(preface.md#skill-navigation-row-174) when NPT")
    out = out.replace("when row 153 and row 54", "when row 173 and row 54")
    out = out.replace("after row 153 alone", "after row 173 alone")
    out = out.replace("Scene after row 153.", "Scene after row 173.")
    out = out.replace("row 1945", "row 195")
    out = out.replace("row 1946", "row 196")
    out = out.replace("Row 194 does not replace", "Row 194 does not replace")
    out = out.replace("When row 194 is complete", "When row 194 is complete")
    out = out.replace("memory sheet row 174 baby picture", "memory sheet row 194 baby picture")
    out = out.replace("prologue row 174 closing stitch", "prologue row 194 closing stitch")
    out = out.replace("prologue row 174 preview", "prologue row 194 preview")
    out = out.replace("epilogue row 174 closing loop", "epilogue row 194 closing loop")
    out = out.replace("TEMP_ROW195", "row 195")
    return out


def extract_preface_row174(preface: str) -> str:
    start = preface.index("### Row 174 skill checkpoint")
    end = preface.index("\n\n### Row 175 skill checkpoint", start)
    return preface[start:end]


ROW194_PREFACE = bump174_to_194(
    extract_preface_row174((ROOT / "writings/preface/chapters/preface.md").read_text())
) + "\n\n"

PROLOGUE_COMPASS = (
    "| Row 68 → Row 174 Row 68 → Row 54 export meta prelude capstone reunion (row 194) | "
    "[Preface: row 194 skill checkpoint](../preface.md#skill-navigation-row-194) · "
    "[Row 68 → Row 174 export meta prelude capstone reunion index](../appendix/sources.md#row68-row174-export-meta-prelude-capstone-reunion-index-row-194) · "
    "[memory sheet row 194 baby picture](../appendix/memory-sheet.md#row-194-baby-picture-row68-row174-export-meta-prelude-capstone-reunion) · "
    "[prologue row 194 preview row](#prologue-preview-row-194); [prologue row 194 closing stitch](#row-194-closing-stitch); "
    "[epilogue row 194 closing loop](../epilogue/multiscale.md#row-194-closing-loop) — "
    "read row 68 gate + row 193 or row 174 dynamics meta prelude capstone / export meta prelude gate + VIII.2 Bridge → opening hinge → VIII.3 pedigree + row 54 meta aloud "
    "when NPT dynamics is clean on the full capstone path but yaml exports feel like standalone post-processing after verified dynamics meta prelude capstone |\n"
)

_prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
_row174_stitch_line = next(
    line for line in _prologue.splitlines() if line.startswith("**Row 174 closing stitch")
)
PROLOGUE_STITCH = bump174_to_194(_row174_stitch_line) + "\n\n"

PROLOGUE_PREVIEW = (
    '| <span id="prologue-preview-row-194"></span>Row 194 preview (Row 68 → Row 174 Row 68 → Row 54 export meta prelude capstone reunion) | '
    "Explain why midpoint closure (row 68) and VIII.2 → VIII.3 meta (row 54) must be read together with the Bridge → pedigree chain after verified dynamics meta prelude capstone on the full capstone path before dynamics manifest and coarse-graining sections feel like separate courses | "
    'One sentence: "read row 68 gate + row 193 or row 174 dynamics meta prelude capstone / export meta prelude gate + VIII.2 Bridge → opening hinge → VIII.3 pedigree + row 54 meta aloud when NPT dynamics is clean on the full capstone path but yaml exports feel like standalone post-processing after verified dynamics meta prelude capstone" — '
    "[preface row 194 skill checkpoint](../preface.md#skill-navigation-row-194); [prologue row 194 closing stitch](#row-194-closing-stitch); "
    "[Row 68 → Row 174 reunion index](../appendix/sources.md#row68-row174-export-meta-prelude-capstone-reunion-index-row-194); "
    "[memory sheet row 194 baby picture](../appendix/memory-sheet.md#row-194-baby-picture-row68-row174-export-meta-prelude-capstone-reunion); "
    "[VIII.2 Bridge](../part08-md/02-ensembles-integrators.md#bridge); "
    "[VIII.3 opening hinge from VIII.2](../part08-md/03-ab-initio-and-coarse-graining.md#opening-hinge-viii2-to-viii3); "
    "[preface row 54 skill checkpoint](../preface.md#skill-navigation-row-54); "
    "[preface row 193 skill checkpoint](../preface.md#skill-navigation-row-193); "
    "[epilogue row 194 closing loop](../epilogue/multiscale.md#row-194-closing-loop) |\n"
)

_epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
EPILOGUE_LOOP = bump174_to_194(
    "### Row 174 closing loop"
    + _epilogue.split("### Row 174 closing loop")[1].split("### Row 175 closing loop")[0]
)

SOURCES_TABLE = (
    "| 194 | Row 68 → Row 174 Row 68 → Row 54 export meta prelude capstone (midpoint prelude gate ↔ dynamics meta prelude capstone on full capstone path ↔ row 54 meta) | "
    "[Row 68 → Row 174 export meta prelude capstone reunion index](#row68-row174-export-meta-prelude-capstone-reunion-index-row-194) · "
    "[preface row 194](../preface.md#skill-navigation-row-194) · "
    "[prologue row 194 preview](../prologue/00-many-scales.md#prologue-preview-row-194) · "
    "[prologue row 194 closing stitch](../prologue/00-many-scales.md#row-194-closing-stitch) · "
    "[epilogue row 194 closing loop](../epilogue/multiscale.md#row-194-closing-loop) · "
    "[memory sheet row 194 baby picture](memory-sheet.md#row-194-baby-picture-row68-row174-export-meta-prelude-capstone-reunion) | "
    "Row 68 closed but **row 54 VIII.2 → VIII.3 opening hinge still feels disconnected from verified dynamics meta prelude capstone on the full capstone path** — "
    "read row 68 + row 193 or row 174 gate + VIII.2 Bridge → opening hinge → VIII.3 pedigree + row 54; "
    "[preface row 54](../preface.md#skill-navigation-row-54) |\n"
)

SOURCES_INDEX = bump174_to_194(
    (ROOT / "writings/appendix/chapters/sources.md")
    .read_text()
    .split("## Row 68 → Row 154 Row 68 → Row 54 export meta prelude capstone reunion index (row 174)")[1]
    .split("## Row 68 → Row 155 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 175)")[0]
)
SOURCES_INDEX = (
    "## Row 68 → Row 174 Row 68 → Row 54 export meta prelude capstone reunion index (row 194)"
    + SOURCES_INDEX
)

MEMORY_TABLE = (
    "| 194 | Meta | [Row 68 → Row 174 export meta prelude capstone reunion index](sources.md#row68-row174-export-meta-prelude-capstone-reunion-index-row-194) · "
    "[preface row 194 skill checkpoint](../preface.md#skill-navigation-row-194) · "
    "[prologue row 194 preview](../prologue/00-many-scales.md#prologue-preview-row-194) · "
    "[prologue row 194 closing stitch](../prologue/00-many-scales.md#row-194-closing-stitch) · "
    "[epilogue row 194 closing loop](../epilogue/multiscale.md#row-194-closing-loop) | "
    "Row 68 closed but row 54 VIII.2 → VIII.3 opening hinge feels disconnected from verified dynamics meta prelude capstone on the full capstone path — "
    "read row 68 + row 193 or row 174 gate + VIII.2 Bridge → opening hinge → VIII.3 pedigree + row 54; "
    "[row 194 baby picture](#row-194-baby-picture-row68-row174-export-meta-prelude-capstone-reunion) |\n"
)

MEMORY_BABY = bump174_to_194(
    (ROOT / "writings/appendix/chapters/memory-sheet.md")
    .read_text()
    .split("### Row 174 baby picture (Row 68 → Row 154 Row 68 → Row 54 export meta prelude capstone reunion)")[1]
    .split("### Row 175 baby picture")[0]
)
MEMORY_BABY = (
    "### Row 194 baby picture (Row 68 → Row 174 Row 68 → Row 54 export meta prelude capstone reunion)"
    + MEMORY_BABY.split(")", 1)[1]
    if ")" in MEMORY_BABY
    else "### Row 194 baby picture" + MEMORY_BABY
)

ROW193_TAIL_OLD = (
    "When row 193 is complete, proceed to [row 174](preface.md#skill-navigation-row-174) when NPT converges but the pedigree checklist still feels disconnected from verified dynamics meta prelude capstone on the full capstone path, to [row 134](preface.md#skill-navigation-row-134) when NPT converges but the pedigree checklist still feels disconnected from verified dynamics meta prelude capstone on the opening-hinge capstone path alone, to [row 173](preface.md#skill-navigation-row-153) when NVT/NPT still feels like thermostat homework after verified atomistic meta prelude capstone on the opening-hinge capstone path alone, to [row 173](preface.md#skill-navigation-row-133) for the Row 68 ↔ Row 53 dynamics meta audit on the opening-hinge prelude path alone, to [row 112](preface.md#skill-navigation-row-112) for the Row 68 ↔ Row 52 atomistic meta audit on the opening-hinge prelude path alone, to [row 152](preface.md#skill-navigation-row-152) when atomistic meta prelude capstone still lags after verified homogenization meta prelude capstone on the full capstone path, to [row 132](preface.md#skill-navigation-row-132) when atomistic meta prelude capstone still lags after verified homogenization meta prelude capstone on the opening-hinge capstone path alone, to [row 53](preface.md#skill-navigation-row-53) when only VIII.1 → VIII.2 stalls, to [row 93](preface.md#skill-navigation-row-93) for the Row 68 ↔ Row 53 dynamics opening prelude audit alone, or extend prose only under `writings/` then sync."
)
ROW193_TAIL_NEW = (
    "When row 193 is complete, proceed to [row 194](preface.md#skill-navigation-row-194) when NPT converges but the pedigree checklist still feels disconnected from verified dynamics meta prelude capstone on the full capstone path, to [row 174](preface.md#skill-navigation-row-174) when NPT converges but the pedigree checklist still feels disconnected from verified dynamics meta prelude capstone on the opening-hinge capstone path alone, to [row 173](preface.md#skill-navigation-row-173) when NVT/NPT still feels like thermostat homework after verified atomistic meta prelude capstone on the opening-hinge capstone path alone, to [row 153](preface.md#skill-navigation-row-153) for the Row 68 ↔ Row 53 dynamics meta audit on the opening-hinge capstone path alone, to [row 133](preface.md#skill-navigation-row-133) for the Row 68 ↔ Row 53 dynamics meta audit on the opening-hinge prelude path alone, to [row 172](preface.md#skill-navigation-row-172) for the Row 68 ↔ Row 52 atomistic meta audit on the opening-hinge capstone path alone, to [row 152](preface.md#skill-navigation-row-152) for the Row 68 ↔ Row 52 atomistic meta audit on the opening-hinge prelude path alone, to [row 192](preface.md#skill-navigation-row-192) when atomistic meta prelude capstone still lags after verified homogenization meta prelude capstone on the full capstone path, to [row 53](preface.md#skill-navigation-row-53) when only VIII.1 → VIII.2 stalls, to [row 93](preface.md#skill-navigation-row-93) for the Row 68 ↔ Row 53 dynamics opening prelude audit alone, or extend prose only under `writings/` then sync."
)

ROW193_EPILOGUE_PROCEED_OLD = (
    "Proceed to [row 174](#row-174-closing-loop) when row 68 closed but export meta prelude capstone still lags after row 173 on the full capstone path,"
)
ROW193_EPILOGUE_PROCEED_NEW = (
    "Proceed to [row 194](#row-194-closing-loop) when row 68 closed but export meta prelude capstone still lags after row 193 on the full capstone path,"
)

ROW193_BABY_OLD = (
    "row 193 when **VIII.2 Bridge and Row 68 → Row 54 meta must read on the same wire before row 174 export meta prelude capstone opens on the full capstone path**"
)
ROW193_BABY_NEW = (
    "row 193 when **VIII.2 Bridge and Row 68 → Row 54 meta must read on the same wire before row 194 export meta prelude capstone opens on the full capstone path**"
)


def main() -> None:
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "### Row 194 skill checkpoint" in preface and preface.index("### Row 194 skill checkpoint") < preface.index(
        copper
    ):
        print("preface: row 194 already present")
    else:
        if ROW193_TAIL_OLD not in preface:
            raise SystemExit("row 193 tail proceed string not found")
        preface = preface.replace(ROW193_TAIL_OLD, ROW193_TAIL_NEW, 1)
        preface = preface.replace(
            "when opening [row 174](preface.md#skill-navigation-row-174) before row 54 closes on the full capstone path",
            "when opening [row 194](preface.md#skill-navigation-row-194) before row 54 closes on the full capstone path",
            1,
        )
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + ROW194_PREFACE + copper)
        preface_path.write_text(preface)
        print("preface: added row 194")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-194" not in prologue:
        needle = "| Row 68 → Row 173 Row 68 → Row 53 dynamics meta prelude capstone reunion (row 193) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 193 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + PROLOGUE_COMPASS + prologue[line_end + 1 :]
        if "row-194-closing-stitch" not in prologue:
            prologue = prologue.replace(
                "**Row 174 closing stitch",
                PROLOGUE_STITCH + "**Row 174 closing stitch",
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-193"></span>Row 193 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview row 193 not found")
        prologue = prologue.replace(preview_anchor, PROLOGUE_PREVIEW + preview_anchor)
        prologue_path.write_text(prologue)
        print("prologue: added row 194")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "row-194-closing-loop" not in epilogue or "### Row 194 closing loop" not in epilogue:
        if ROW193_EPILOGUE_PROCEED_OLD in epilogue:
            epilogue = epilogue.replace(ROW193_EPILOGUE_PROCEED_OLD, ROW193_EPILOGUE_PROCEED_NEW, 1)
        marker = "### Row 186 closing loop (Row 68 → Row 166 Row 68 → Row 66 Writings canonical meta prelude capstone reunion)"
        if marker not in epilogue:
            raise SystemExit("epilogue row 186 insert anchor not found")
        if "### Row 194 closing loop" not in epilogue:
            epilogue = epilogue.replace(marker, EPILOGUE_LOOP + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 194")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row174-export-meta-prelude-capstone-reunion-index-row-194" not in sources:
        sources = sources.replace(
            "| 174 | Row 68 → Row 154 Row 68 → Row 54 export meta prelude capstone",
            SOURCES_TABLE + "| 174 | Row 68 → Row 154 Row 68 → Row 54 export meta prelude capstone",
            1,
        )
        sources = sources.replace(
            "## Row 68 → Row 154 Row 68 → Row 54 export meta prelude capstone reunion index (row 174)",
            SOURCES_INDEX + "## Row 68 → Row 154 Row 68 → Row 54 export meta prelude capstone reunion index (row 174)",
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 194")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-194-baby-picture-row68-row174" not in memory:
        memory = memory.replace(
            "| 193 | Meta | [Row 68 → Row 173 dynamics meta prelude capstone reunion index]",
            MEMORY_TABLE + "| 193 | Meta | [Row 68 → Row 173 dynamics meta prelude capstone reunion index]",
            1,
        )
        memory = memory.replace(
            "### Row 174 baby picture (Row 68 → Row 154 Row 68 → Row 54 export meta prelude capstone reunion) {#row-174-baby-picture-row68-row154-export-meta-prelude-capstone-reunion}",
            MEMORY_BABY
            + "### Row 174 baby picture (Row 68 → Row 154 Row 68 → Row 54 export meta prelude capstone reunion) {#row-174-baby-picture-row68-row154-export-meta-prelude-capstone-reunion}",
            1,
        )
        if ROW193_BABY_OLD in memory:
            memory = memory.replace(ROW193_BABY_OLD, ROW193_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 194")


if __name__ == "__main__":
    main()
