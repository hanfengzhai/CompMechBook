#!/usr/bin/env python3
"""Add row 193 meta-stitch (Row 68 → Row 173 ↔ Row 53 dynamics meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def bump173_to_193(text: str) -> str:
    """Transform row-173 capstone-path meta copy to row 193 (153→173 inner, 192 gate)."""
    out = text.replace("row 194", "TEMP_ROW194")
    repl = [
        ("Row 68 → Row 153 Row 68 → Row 53", "Row 68 → Row 173 Row 68 → Row 53"),
        (
            "row68-row153-dynamics-meta-prelude-capstone-reunion-index-row-173",
            "TEMP_ROW193_DYN_INDEX",
        ),
        (
            "row-173-baby-picture-row68-row153-dynamics-meta-prelude-capstone-reunion",
            "row-193-baby-picture-row68-row173-dynamics-meta-prelude-capstone-reunion",
        ),
        ("### Row 173 skill checkpoint", "### Row 193 skill checkpoint"),
        ("skill-navigation-row-173", "skill-navigation-row-193"),
        ("prologue-preview-row-173", "prologue-preview-row-193"),
        ("row-173-closing-stitch", "row-193-closing-stitch"),
        ("row-173-closing-loop", "row-193-closing-loop"),
        ("Row 173 three-way audit", "Row 193 three-way audit"),
        (
            "[row 172](preface.md#skill-navigation-row-172) or [row 153](preface.md#skill-navigation-row-153)",
            "[row 192](preface.md#skill-navigation-row-192) or [row 173](preface.md#skill-navigation-row-173)",
        ),
        (
            "[row 172](preface.md#skill-navigation-row-172) or [Row 68 → Row 153 dynamics meta prelude capstone reunion index (row 173)](appendix/sources.md#row68-row153-dynamics-meta-prelude-capstone-reunion-index-row-173)",
            "[row 192](preface.md#skill-navigation-row-192) or [Row 68 → Row 173 dynamics meta prelude capstone reunion index (row 193)](appendix/sources.md#row68-row173-dynamics-meta-prelude-capstone-reunion-index-row-193)",
        ),
        (
            "verified atomistic meta prelude capstone closure (row 172)",
            "verified atomistic meta prelude capstone closure (row 192)",
        ),
        (
            "before row 174 export meta prelude capstone reunion opens on the full capstone path",
            "before row 194 export meta prelude capstone reunion opens on the full capstone path",
        ),
        (
            "before row 175 export meta prelude opens on the full capstone path",
            "before row 195 export meta prelude opens on the full capstone path",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW193_DYN_INDEX",
        "row68-row173-dynamics-meta-prelude-capstone-reunion-index-row-193",
    )
    out = out.replace("Row 173 does not replace", "Row 193 does not replace")
    out = out.replace("When row 173 is complete", "When row 193 is complete")
    out = out.replace("When row 172 closed", "When row 192 closed")
    out = out.replace("after row 173 alone", "after row 193 alone")
    out = out.replace("Recite [preface row 172]", "Recite [preface row 192]")
    out = out.replace("row 173 or row 153 recited", "row 193 or row 173 recited")
    out = out.replace("row 172 or row 153 recited", "row 192 or row 173 recited")
    out = out.replace("when row 172 closed but row 53", "when row 192 closed but row 53")
    out = out.replace("when row 172 and row 53", "when row 192 and row 53")
    out = out.replace("after row 172 alone", "after row 192 alone")
    out = out.replace("Scene after row 172.", "Scene after row 192.")
    out = out.replace("from row 173's", "from row 192's")
    out = out.replace("row 172's static potential", "row 192's static potential")
    out = out.replace("row 133", "row 153")
    out = out.replace("Row 133", "Row 153")
    out = out.replace("row 113", "row 133")
    out = out.replace("Row 113", "Row 133")
    out = out.replace(
        "row68-row113-dynamics-meta-prelude-capstone-reunion-index-row-133",
        "row68-row133-dynamics-meta-prelude-capstone-reunion-index-row-153",
    )
    out = out.replace("row 153", "row 173")
    out = out.replace("Row 153", "Row 173")
    out = out.replace(
        "row68-row133-dynamics-meta-prelude-capstone-reunion-index-row-153",
        "TEMP_DYN153IDX",
    )
    out = out.replace(
        "row68-row152-atomistic-meta-prelude-capstone-reunion-index-row-172",
        "row68-row172-atomistic-meta-prelude-capstone-reunion-index-row-192",
    )
    out = out.replace("TEMP_DYN153IDX", "row68-row153-dynamics-meta-prelude-capstone-reunion-index-row-173")
    out = out.replace("row 172", "row 192")
    out = out.replace("Row 172", "Row 192")
    out = out.replace("[row 193](preface.md#skill-navigation-row-192)", "[row 192](preface.md#skill-navigation-row-192)")
    out = out.replace("[row 193](preface.md#skill-navigation-row-173)", "[row 173](preface.md#skill-navigation-row-173)")
    out = out.replace("row 193 or row 173", "row 192 or row 173")
    out = out.replace("Row 68 → Row 193 Row 68 → Row 53", "Row 68 → Row 173 Row 68 → Row 53")
    out = out.replace("memory sheet row 173 baby picture", "memory sheet row 193 baby picture")
    out = out.replace("prologue row 173 closing stitch", "prologue row 193 closing stitch")
    out = out.replace("prologue row 173 preview", "prologue row 193 preview")
    out = out.replace("epilogue row 173 closing loop", "epilogue row 193 closing loop")
    out = out.replace(
        "reunion index (row 173)](appendix/sources.md#row68-row153-dynamics-meta-prelude-capstone-reunion-index-row-173)",
        "reunion index (row 193)](appendix/sources.md#row68-row173-dynamics-meta-prelude-capstone-reunion-index-row-193)",
    )
    out = out.replace(
        "Prologue preview ([row 173](prologue/00-many-scales.md#prologue-preview-row-193))",
        "Prologue preview ([row 193](prologue/00-many-scales.md#prologue-preview-row-193))",
    )
    out = out.replace("TEMP_ROW194", "row 194")
    return out


def extract_preface_row173(preface: str) -> str:
    start = preface.index("### Row 173 skill checkpoint")
    end = preface.index("\n\n### Row 174 skill checkpoint", start)
    return preface[start:end]


ROW193_PREFACE = bump173_to_193(
    extract_preface_row173((ROOT / "writings/preface/chapters/preface.md").read_text())
) + "\n\n"

PROLOGUE_COMPASS = (
    "| Row 68 → Row 173 Row 68 → Row 53 dynamics meta prelude capstone reunion (row 193) | "
    "[Preface: row 193 skill checkpoint](../preface.md#skill-navigation-row-193) · "
    "[Row 68 → Row 173 dynamics meta prelude capstone reunion index](../appendix/sources.md#row68-row173-dynamics-meta-prelude-capstone-reunion-index-row-193) · "
    "[memory sheet row 193 baby picture](../appendix/memory-sheet.md#row-193-baby-picture-row68-row173-dynamics-meta-prelude-capstone-reunion) · "
    "[prologue row 193 preview row](#prologue-preview-row-193); [prologue row 193 closing stitch](#row-193-closing-stitch); "
    "[epilogue row 193 closing loop](../epilogue/multiscale.md#row-193-closing-loop) — "
    "read row 68 gate + row 192 or row 173 atomistic meta prelude capstone / dynamics meta prelude gate + VIII.1 Bridge → opening hinge → VIII.2 ensembles + row 53 meta aloud "
    "when EAM foundation is clean on the full capstone path but NVT/NPT feels like AtomModel homework after verified atomistic meta prelude capstone |\n"
)

_prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
_row173_stitch_line = next(
    line for line in _prologue.splitlines() if line.startswith("**Row 173 closing stitch")
)
PROLOGUE_STITCH = bump173_to_193(_row173_stitch_line) + "\n\n"

PROLOGUE_PREVIEW = (
    '| <span id="prologue-preview-row-193"></span>Row 193 preview (Row 68 → Row 173 Row 68 → Row 53 dynamics meta prelude capstone reunion) | '
    "Explain why midpoint closure (row 68) and VIII.1 → VIII.2 meta (row 53) must be read together with the Bridge → NPT chain after verified atomistic meta prelude capstone on the full capstone path before foundation manifest and thermostat sections feel like separate courses | "
    'One sentence: "read row 68 gate + row 192 or row 173 atomistic meta prelude capstone / dynamics meta prelude gate + VIII.1 Bridge → opening hinge → VIII.2 ensembles + row 53 meta aloud when EAM foundation is clean on the full capstone path but NVT/NPT feels like AtomModel homework after verified atomistic meta prelude capstone" — '
    "[preface row 193 skill checkpoint](../preface.md#skill-navigation-row-193); [prologue row 193 closing stitch](#row-193-closing-stitch); "
    "[Row 68 → Row 173 reunion index](../appendix/sources.md#row68-row173-dynamics-meta-prelude-capstone-reunion-index-row-193); "
    "[memory sheet row 193 baby picture](../appendix/memory-sheet.md#row-193-baby-picture-row68-row173-dynamics-meta-prelude-capstone-reunion); "
    "[VIII.1 Bridge](../part08-md/01-potentials-phase-space.md#bridge); "
    "[VIII.2 opening hinge from VIII.1](../part08-md/02-ensembles-integrators.md#opening-hinge-viii1-to-viii2); "
    "[preface row 53 skill checkpoint](../preface.md#skill-navigation-row-53); "
    "[preface row 192 skill checkpoint](../preface.md#skill-navigation-row-192); "
    "[epilogue row 193 closing loop](../epilogue/multiscale.md#row-193-closing-loop) |\n"
)

_epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
EPILOGUE_LOOP = bump173_to_193(
    "### Row 173 closing loop"
    + _epilogue.split("### Row 173 closing loop")[1].split("### Row 174 closing loop")[0]
)

SOURCES_TABLE = (
    "| 193 | Row 68 → Row 173 Row 68 → Row 53 dynamics meta prelude capstone (midpoint prelude gate ↔ atomistic meta prelude capstone on full capstone path ↔ row 53 meta) | "
    "[Row 68 → Row 173 dynamics meta prelude capstone reunion index](#row68-row173-dynamics-meta-prelude-capstone-reunion-index-row-193) · "
    "[preface row 193](../preface.md#skill-navigation-row-193) · "
    "[prologue row 193 preview](../prologue/00-many-scales.md#prologue-preview-row-193) · "
    "[prologue row 193 closing stitch](../prologue/00-many-scales.md#row-193-closing-stitch) · "
    "[epilogue row 193 closing loop](../epilogue/multiscale.md#row-193-closing-loop) · "
    "[memory sheet row 193 baby picture](memory-sheet.md#row-193-baby-picture-row68-row173-dynamics-meta-prelude-capstone-reunion) | "
    "Row 68 closed but **row 53 VIII.1 → VIII.2 opening hinge still feels disconnected from verified atomistic meta prelude capstone on the full capstone path** — "
    "read row 68 + row 192 or row 173 gate + VIII.1 Bridge → opening hinge → VIII.2 ensembles + row 53; "
    "[preface row 53](../preface.md#skill-navigation-row-53) |\n"
)

SOURCES_INDEX = bump173_to_193(
    (ROOT / "writings/appendix/chapters/sources.md")
    .read_text()
    .split("## Row 68 → Row 153 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 173)")[1]
    .split("## Row 68 → Row 134 Row 68 → Row 54 export meta prelude capstone reunion index (row 154)")[0]
)
SOURCES_INDEX = (
    "## Row 68 → Row 173 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 193)"
    + SOURCES_INDEX
)

MEMORY_TABLE = (
    "| 193 | Meta | [Row 68 → Row 173 dynamics meta prelude capstone reunion index](sources.md#row68-row173-dynamics-meta-prelude-capstone-reunion-index-row-193) · "
    "[preface row 193 skill checkpoint](../preface.md#skill-navigation-row-193) · "
    "[prologue row 193 preview](../prologue/00-many-scales.md#prologue-preview-row-193) · "
    "[prologue row 193 closing stitch](../prologue/00-many-scales.md#row-193-closing-stitch) · "
    "[epilogue row 193 closing loop](../epilogue/multiscale.md#row-193-closing-loop) | "
    "Row 68 closed but row 53 dynamics meta reunion feels disconnected from verified atomistic meta prelude capstone on the full capstone path — "
    "read row 68 + row 192 or row 173 gate + VIII.1 Bridge → opening hinge → VIII.2 ensembles + row 53; "
    "[row 193 baby picture](#row-193-baby-picture-row68-row173-dynamics-meta-prelude-capstone-reunion) |\n"
)

MEMORY_BABY = bump173_to_193(
    (ROOT / "writings/appendix/chapters/memory-sheet.md")
    .read_text()
    .split("### Row 173 baby picture")[1]
    .split("### Row 174 baby picture")[0]
)
MEMORY_BABY = (
    "### Row 193 baby picture (Row 68 → Row 173 Row 68 → Row 53 dynamics meta prelude capstone reunion)"
    + MEMORY_BABY.split(")", 1)[1]
    if ")" in MEMORY_BABY
    else "### Row 193 baby picture" + MEMORY_BABY
)

ROW192_TAIL_OLD = (
    "When row 192 is complete, proceed to [row 173](preface.md#skill-navigation-row-173) when NVT/NPT still feels like thermostat homework after verified atomistic meta prelude capstone on the full capstone path, to [row 153](preface.md#skill-navigation-row-153) when dynamics meta prelude capstone still lags after verified atomistic meta prelude capstone on the opening-hinge capstone path alone, to [row 152](preface.md#skill-navigation-row-152) for the Row 68 ↔ Row 52 atomistic meta audit on the opening-hinge capstone path alone, to [row 132](preface.md#skill-navigation-row-132) for the Row 68 ↔ Row 52 atomistic meta audit on the opening-hinge prelude path alone, to [row 191](preface.md#skill-navigation-row-191) when homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the full capstone path, to [row 171](preface.md#skill-navigation-row-171) when homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the opening-hinge capstone path alone, to [row 52](preface.md#skill-navigation-row-52) when only VII.3 → VIII.1 stalls, to [row 92](preface.md#skill-navigation-row-92) for the Row 68 ↔ Row 52 atomistic opening prelude audit alone, or extend prose only under `writings/` then sync."
)
ROW192_TAIL_NEW = (
    "When row 192 is complete, proceed to [row 193](preface.md#skill-navigation-row-193) when NVT/NPT still feels like thermostat homework after verified atomistic meta prelude capstone on the full capstone path, to [row 173](preface.md#skill-navigation-row-173) when dynamics meta prelude capstone still lags after verified atomistic meta prelude capstone on the opening-hinge capstone path alone, to [row 153](preface.md#skill-navigation-row-153) for the Row 68 ↔ Row 53 dynamics meta audit on the opening-hinge capstone path alone, to [row 133](preface.md#skill-navigation-row-133) for the Row 68 ↔ Row 53 dynamics meta audit on the opening-hinge prelude path alone, to [row 172](preface.md#skill-navigation-row-172) for the Row 68 ↔ Row 52 atomistic meta audit on the opening-hinge capstone path alone, to [row 152](preface.md#skill-navigation-row-152) for the Row 68 ↔ Row 52 atomistic meta audit on the opening-hinge prelude path alone, to [row 191](preface.md#skill-navigation-row-191) when homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the full capstone path, to [row 52](preface.md#skill-navigation-row-52) when only VII.3 → VIII.1 stalls, to [row 92](preface.md#skill-navigation-row-92) for the Row 68 ↔ Row 52 atomistic opening prelude audit alone, or extend prose only under `writings/` then sync."
)

ROW192_STITCH_OLD = (
    "before row 173 dynamics meta prelude capstone reunion opens on the full capstone path."
)
ROW192_STITCH_NEW = (
    "before row 193 dynamics meta prelude capstone reunion opens on the full capstone path."
)

ROW192_EPILOGUE_PROCEED_OLD = (
    "Proceed to [row 173](#row-173-closing-loop) when row 68 closed but dynamics meta prelude capstone still lags after row 172 on the full capstone path,"
)
ROW192_EPILOGUE_PROCEED_NEW = (
    "Proceed to [row 193](#row-193-closing-loop) when row 68 closed but dynamics meta prelude capstone still lags after row 192 on the full capstone path,"
)

ROW192_BABY_OLD = (
    "row 172 when **VIII.1 Bridge and Row 68 → Row 53 meta must read on the same wire before row 173 dynamics meta prelude capstone opens on the full capstone path**"
)
ROW192_BABY_NEW = (
    "row 192 when **VIII.1 Bridge and Row 68 → Row 53 meta must read on the same wire before row 193 dynamics meta prelude capstone opens on the full capstone path**"
)


def main() -> None:
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "### Row 193 skill checkpoint" in preface and preface.index("### Row 193 skill checkpoint") < preface.index(
        copper
    ):
        print("preface: row 193 already present")
    else:
        if ROW192_TAIL_OLD not in preface:
            raise SystemExit("row 192 tail proceed string not found")
        preface = preface.replace(ROW192_TAIL_OLD, ROW192_TAIL_NEW, 1)
        preface = preface.replace(
            "when opening [row 173](preface.md#skill-navigation-row-173) before row 53 closes on the full capstone path",
            "when opening [row 193](preface.md#skill-navigation-row-193) before row 53 closes on the full capstone path",
            1,
        )
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + ROW193_PREFACE + copper)
        preface_path.write_text(preface)
        print("preface: added row 193")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-193" not in prologue:
        needle = "| Row 68 → Row 172 Row 68 → Row 52 atomistic meta prelude capstone reunion (row 192) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 192 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + PROLOGUE_COMPASS + prologue[line_end + 1 :]
        if "row-193-closing-stitch" not in prologue:
            prologue = prologue.replace(
                "**Row 173 closing stitch",
                PROLOGUE_STITCH + "**Row 173 closing stitch",
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-192"></span>Row 192 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview row 192 not found")
        prologue = prologue.replace(preview_anchor, PROLOGUE_PREVIEW + preview_anchor)
        if ROW192_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW192_STITCH_OLD, ROW192_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 193")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "row-193-closing-loop" not in epilogue:
        if ROW192_EPILOGUE_PROCEED_OLD in epilogue:
            epilogue = epilogue.replace(ROW192_EPILOGUE_PROCEED_OLD, ROW192_EPILOGUE_PROCEED_NEW)
        marker = "### Row 186 closing loop (Row 68 → Row 166 Row 68 → Row 66 Writings canonical meta prelude capstone reunion)"
        if marker not in epilogue:
            raise SystemExit("epilogue row 186 insert anchor not found")
        epilogue = epilogue.replace(marker, EPILOGUE_LOOP + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 193")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row173-dynamics-meta-prelude-capstone-reunion-index-row-193" not in sources:
        sources = sources.replace(
            "| 173 | Row 68 → Row 153 Row 68 → Row 53 dynamics meta prelude capstone",
            SOURCES_TABLE + "| 173 | Row 68 → Row 153 Row 68 → Row 53 dynamics meta prelude capstone",
            1,
        )
        sources = sources.replace(
            "## Row 68 → Row 153 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 173)",
            SOURCES_INDEX + "## Row 68 → Row 153 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 173)",
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 193")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-193-baby-picture-row68-row173" not in memory:
        memory = memory.replace(
            "| 192 | Meta | [Row 68 → Row 172 atomistic meta prelude capstone reunion index]",
            MEMORY_TABLE + "| 192 | Meta | [Row 68 → Row 172 atomistic meta prelude capstone reunion index]",
            1,
        )
        memory = memory.replace(
            "### Row 173 baby picture (Row 68 → Row 153 Row 68 → Row 53 dynamics meta prelude capstone reunion) {#row-173-baby-picture-row68-row153-dynamics-meta-prelude-capstone-reunion}",
            MEMORY_BABY
            + "### Row 173 baby picture (Row 68 → Row 153 Row 68 → Row 53 dynamics meta prelude capstone reunion) {#row-173-baby-picture-row68-row153-dynamics-meta-prelude-capstone-reunion}",
            1,
        )
        if ROW192_BABY_OLD in memory:
            memory = memory.replace(ROW192_BABY_OLD, ROW192_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 193")


if __name__ == "__main__":
    main()
