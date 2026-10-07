#!/usr/bin/env python3
"""Add row 190 meta-stitch (Row 68 → Row 170 ↔ Row 50 DDD meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def bump170_to_190(text: str) -> str:
    """Transform row-170 capstone-path meta copy to row 190 (150→170 inner, 189 gate)."""
    repl = [
        ("Row 68 → Row 150 Row 68 → Row 50", "Row 68 → Row 170 Row 68 → Row 50"),
        (
            "row68-row150-ddd-meta-prelude-capstone-reunion-index-row-170",
            "TEMP_ROW190_DDD_INDEX",
        ),
        (
            "row-170-baby-picture-row68-row150-ddd-meta-prelude-capstone-reunion",
            "row-190-baby-picture-row68-row170-ddd-meta-prelude-capstone-reunion",
        ),
        ("### Row 170 skill checkpoint", "### Row 190 skill checkpoint"),
        ("skill-navigation-row-170", "skill-navigation-row-190"),
        ("prologue-preview-row-170", "prologue-preview-row-190"),
        ("row-170-closing-stitch", "row-190-closing-stitch"),
        ("row-170-closing-loop", "row-190-closing-loop"),
        ("Row 170 three-way audit", "Row 190 three-way audit"),
        (
            "[row 169](preface.md#skill-navigation-row-169) or [row 150](preface.md#skill-navigation-row-150)",
            "[row 189](preface.md#skill-navigation-row-189) or [row 170](preface.md#skill-navigation-row-170)",
        ),
        (
            "[row 149](preface.md#skill-navigation-row-149) or [Row 68 → Row 150 DDD meta prelude capstone reunion index (row 170)](appendix/sources.md#row68-row150-ddd-meta-prelude-capstone-reunion-index-row-170)",
            "[row 189](preface.md#skill-navigation-row-189) or [Row 68 → Row 170 DDD meta prelude capstone reunion index (row 190)](appendix/sources.md#row68-row170-ddd-meta-prelude-capstone-reunion-index-row-190)",
        ),
        (
            "verified taxonomy meta prelude capstone on the full capstone path (row 149)",
            "verified taxonomy meta prelude capstone on the full capstone path (row 169)",
        ),
        (
            "verified taxonomy meta prelude capstone closure on the full capstone path (row 149)",
            "verified taxonomy meta prelude capstone closure on the full capstone path (row 169)",
        ),
    ]
    out = text
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace("TEMP_ROW190_DDD_INDEX", "row68-row170-ddd-meta-prelude-capstone-reunion-index-row-190")
    out = out.replace("Row 170 does not replace", "Row 190 does not replace")
    out = out.replace(
        "When row 170 is complete, proceed to [row 171](preface.md#skill-navigation-row-171) when homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the full capstone path, to [row 151](preface.md#skill-navigation-row-151) when homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the opening-hinge capstone path alone, to [row 131](preface.md#skill-navigation-row-131) for the Row 68 ↔ Row 51 homogenization meta audit on the opening-hinge prelude path alone, to [row 150](preface.md#skill-navigation-row-150) when DDD meta prelude capstone still lags after verified taxonomy meta prelude capstone on the full capstone path, to [row 130](preface.md#skill-navigation-row-130) when DDD meta prelude capstone still lags after verified taxonomy meta prelude capstone on the opening-hinge capstone path alone, to [row 50](preface.md#skill-navigation-row-50) when only VII.1 → VII.2 stalls, to [row 90](preface.md#skill-navigation-row-90) for the Row 68 ↔ Row 50 DDD opening prelude audit alone, or extend prose only under `writings/` then sync.",
        "When row 190 is complete, proceed to [row 171](preface.md#skill-navigation-row-171) when homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the full capstone path, to [row 151](preface.md#skill-navigation-row-151) when homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the opening-hinge capstone path alone, to [row 131](preface.md#skill-navigation-row-131) for the Row 68 ↔ Row 51 homogenization meta audit on the opening-hinge prelude path alone, to [row 170](preface.md#skill-navigation-row-170) when DDD meta prelude capstone still lags after verified taxonomy meta prelude capstone on the opening-hinge capstone path alone, to [row 150](preface.md#skill-navigation-row-150) when DDD meta prelude capstone still lags after verified taxonomy meta prelude capstone on the opening-hinge prelude path alone, to [row 50](preface.md#skill-navigation-row-50) when only VII.1 → VII.2 stalls, to [row 90](preface.md#skill-navigation-row-90) for the Row 68 ↔ Row 50 DDD opening prelude audit alone, or extend prose only under `writings/` then sync.",
    )
    out = out.replace("When row 170 is complete", "When row 190 is complete")
    out = out.replace("When row 169 closed", "When row 189 closed")
    out = out.replace("after row 170 alone", "after row 190 alone")
    out = out.replace("Recite [preface row 169]", "Recite [preface row 189]")
    out = out.replace("row 169 or row 150 recited", "row 189 or row 170 recited")
    out = out.replace("row 149 and row 50", "row 169 and row 50")
    out = out.replace("after row 149", "after row 189")
    out = out.replace("row 149's Burgers", "row 169's Burgers")
    out = out.replace("row 149 closed", "row 169 closed")
    out = out.replace("Row 149 closed", "Row 169 closed")
    out = out.replace("row 148 closed", "row 168 closed")
    out = out.replace("row 130", "row 150")
    out = out.replace("Row 130", "Row 150")
    out = out.replace("row 150", "row 170")
    out = out.replace("Row 150", "Row 170")
    out = out.replace("row 149", "row 169")
    out = out.replace("Row 149", "Row 169")
    out = out.replace("row 110", "row 130")
    out = out.replace("Row 110", "Row 130")
    out = out.replace(
        "row68-row110-ddd-meta-prelude-capstone-reunion-index-row-130",
        "row68-row130-ddd-meta-prelude-capstone-reunion-index-row-150",
    )
    out = out.replace(
        "row68-row130-ddd-meta-prelude-capstone-reunion-index-row-150",
        "row68-row150-ddd-meta-prelude-capstone-reunion-index-row-170",
    )
    out = out.replace("[row 190](preface.md#skill-navigation-row-189)", "[row 189](preface.md#skill-navigation-row-189)")
    out = out.replace("[row 190](preface.md#skill-navigation-row-170)", "[row 170](preface.md#skill-navigation-row-170)")
    out = out.replace(
        "[row 171](preface.md#skill-navigation-row-171) before row 51",
        "[row 191](preface.md#skill-navigation-row-191) before row 51",
    )
    out = out.replace(
        "[row 191](preface.md#skill-navigation-row-191) before row 51",
        "[row 171](preface.md#skill-navigation-row-171) before row 51",
    )
    out = out.replace("memory sheet row 170 baby picture", "memory sheet row 190 baby picture")
    out = out.replace("prologue row 170 closing stitch", "prologue row 190 closing stitch")
    out = out.replace("prologue row 170 preview", "prologue row 190 preview")
    out = out.replace("epilogue row 170 closing loop", "epilogue row 190 closing loop")
    out = out.replace(
        "reunion index (row 170)](appendix/sources.md#row68-row150-ddd-meta-prelude-capstone-reunion-index-row-170)",
        "reunion index (row 190)](appendix/sources.md#row68-row170-ddd-meta-prelude-capstone-reunion-index-row-190)",
    )
    out = out.replace(
        "Prologue preview ([row 170](prologue/00-many-scales.md#prologue-preview-row-190))",
        "Prologue preview ([row 190](prologue/00-many-scales.md#prologue-preview-row-190))",
    )
    out = out.replace(
        "[row 170](preface.md#skill-navigation-row-150)",
        "[row 150](preface.md#skill-navigation-row-150)",
    )
    return out


def extract_preface_row170(preface: str) -> str:
    start = preface.index(
        "### Row 170 skill checkpoint — Row 68 → Row 150 Row 68 → Row 50"
    )
    end = preface.index("\n\n### Row 171 skill checkpoint", start)
    return preface[start:end]


ROW190_PREFACE = bump170_to_190(
    extract_preface_row170((ROOT / "writings/preface/chapters/preface.md").read_text())
) + "\n\n"

PROLOGUE_COMPASS = (
    "| Row 68 → Row 170 Row 68 → Row 50 DDD meta prelude capstone reunion (row 190) | "
    "[Preface: row 190 skill checkpoint](../preface.md#skill-navigation-row-190) · "
    "[Row 68 → Row 170 DDD meta prelude capstone reunion index](../appendix/sources.md#row68-row170-ddd-meta-prelude-capstone-reunion-index-row-190) · "
    "[memory sheet row 190 baby picture](../appendix/memory-sheet.md#row-190-baby-picture-row68-row170-ddd-meta-prelude-capstone-reunion) · "
    "[prologue row 190 preview row](#prologue-preview-row-190); [prologue row 190 closing stitch](#row-190-closing-stitch); "
    "[epilogue row 190 closing loop](../epilogue/multiscale.md#row-190-closing-loop) — "
    "read row 68 gate + row 189 or row 170 taxonomy meta prelude capstone / DDD meta prelude gate + VII.1 Bridge → opening hinge → VII.2 Peach–Köhler + row 50 meta aloud "
    "when Burgers taxonomy is clean on the full capstone path but OpenDiS decks feel like DDD homework after verified taxonomy meta prelude capstone on the full capstone path |\n"
)

_prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
PROLOGUE_STITCH = bump170_to_190(
    "**Row 170 closing stitch (Row 68 → Row 150 Row 68 → Row 50 DDD meta prelude capstone reunion).** {#row-170-closing-stitch} "
    + _prologue.split("**Row 170 closing stitch")[1].split("**Row 171 closing stitch")[0].lstrip()
    .split("\n\n")[0]
    + "\n\n"
)

PROLOGUE_PREVIEW = (
    '| <span id="prologue-preview-row-190"></span>Row 190 preview (Row 68 → Row 170 Row 68 → Row 50 DDD meta prelude capstone reunion) | '
    "Explain why midpoint closure (row 68) and VII.1 → VII.2 meta (row 50) must be read together with the Bridge → Peach–Köhler chain after verified taxonomy meta prelude capstone on the full capstone path before Burgers tables and OpenDiS decks feel like separate courses | "
    'One sentence: "read row 68 gate + row 189 or row 170 taxonomy meta prelude capstone / DDD meta prelude gate + VII.1 Bridge → opening hinge → VII.2 Peach–Köhler + row 50 meta aloud when Burgers taxonomy is clean on the full capstone path but OpenDiS decks feel like DDD homework after verified taxonomy meta prelude capstone on the full capstone path" — '
    "[preface row 190 skill checkpoint](../preface.md#skill-navigation-row-190); [prologue row 190 closing stitch](#row-190-closing-stitch); "
    "[Row 68 → Row 170 reunion index](../appendix/sources.md#row68-row170-ddd-meta-prelude-capstone-reunion-index-row-190); "
    "[memory sheet row 190 baby picture](../appendix/memory-sheet.md#row-190-baby-picture-row68-row170-ddd-meta-prelude-capstone-reunion); "
    "[VII.1 Bridge](../part07-defects/01-defect-taxonomy.md#bridge); "
    "[VII.1 opening hinge to VII.2](../part07-defects/01-defect-taxonomy.md#opening-hinge-vii1-to-vii2); "
    "[preface row 50 skill checkpoint](../preface.md#skill-navigation-row-50); "
    "[preface row 189 skill checkpoint](../preface.md#skill-navigation-row-189); "
    "[epilogue row 190 closing loop](../epilogue/multiscale.md#row-190-closing-loop) |\n"
)

_epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
EPILOGUE_LOOP = bump170_to_190(
    "### Row 170 closing loop"
    + _epilogue.split("### Row 170 closing loop")[1].split("### Row 171 closing loop")[0]
)

SOURCES_TABLE = (
    "| 190 | Row 68 → Row 170 Row 68 → Row 50 DDD meta prelude capstone (midpoint prelude gate ↔ taxonomy meta prelude capstone on full capstone path ↔ row 50 meta) | "
    "[Row 68 → Row 170 DDD meta prelude capstone reunion index](#row68-row170-ddd-meta-prelude-capstone-reunion-index-row-190) · "
    "[preface row 190](../preface.md#skill-navigation-row-190) · "
    "[prologue row 190 preview](../prologue/00-many-scales.md#prologue-preview-row-190) · "
    "[prologue row 190 closing stitch](../prologue/00-many-scales.md#row-190-closing-stitch) · "
    "[epilogue row 190 closing loop](../epilogue/multiscale.md#row-190-closing-loop) · "
    "[memory sheet row 190 baby picture](memory-sheet.md#row-190-baby-picture-row68-row170-ddd-meta-prelude-capstone-reunion) | "
    "Row 68 closed but **row 50 VII.1 → VII.2 opening hinge still feels disconnected from verified taxonomy meta prelude capstone on the full capstone path** — "
    "read row 68 + row 189 or row 170 gate + VII.1 Bridge → opening hinge → VII.2 Peach–Köhler + row 50; "
    "[preface row 50](../preface.md#skill-navigation-row-50) |\n"
)

SOURCES_INDEX = bump170_to_190(
    (ROOT / "writings/appendix/chapters/sources.md")
    .read_text()
    .split("## Row 68 → Row 150 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 170)")[1]
    .split("## Row 68 → Row 151 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 171)")[0]
)
SOURCES_INDEX = (
    "## Row 68 → Row 170 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 190)"
    + SOURCES_INDEX
)

MEMORY_TABLE = (
    "| 190 | Meta | [Row 68 → Row 170 DDD meta prelude capstone reunion index](sources.md#row68-row170-ddd-meta-prelude-capstone-reunion-index-row-190) · "
    "[preface row 190 skill checkpoint](../preface.md#skill-navigation-row-190) · "
    "[prologue row 190 preview](../prologue/00-many-scales.md#prologue-preview-row-190) · "
    "[prologue row 190 closing stitch](../prologue/00-many-scales.md#row-190-closing-stitch) · "
    "[epilogue row 190 closing loop](../epilogue/multiscale.md#row-190-closing-loop) | "
    "Row 68 closed but row 50 DDD meta reunion feels disconnected from verified taxonomy meta prelude capstone on the full capstone path — "
    "read row 68 + row 189 or row 170 gate + VII.1 Bridge → opening hinge → VII.2 Peach–Köhler + row 50; "
    "[row 190 baby picture](#row-190-baby-picture-row68-row170-ddd-meta-prelude-capstone-reunion) |\n"
)

MEMORY_BABY = bump170_to_190(
    (ROOT / "writings/appendix/chapters/memory-sheet.md")
    .read_text()
    .split("### Row 170 baby picture")[1]
    .split("### Row 171 baby picture")[0]
)
MEMORY_BABY = (
    "### Row 190 baby picture"
    + MEMORY_BABY.split(")", 1)[1]
    if ")" in MEMORY_BABY
    else "### Row 190 baby picture" + MEMORY_BABY
)

ROW189_TAIL_MARKER = "**When to pause.** Read the [prologue row 189 closing stitch]"
ROW189_TAIL_END = "or extend prose only under `writings/` then sync.\n\n\n\n\n## The copper wire through the book"

ROW189_STITCH_OLD = (
    "before row 170 DDD meta prelude capstone reunion opens on the full capstone path."
)
ROW189_STITCH_NEW = (
    "before row 190 DDD meta prelude capstone reunion opens on the full capstone path."
)

ROW189_EPILOGUE_PROCEED_OLD = (
    "Proceed to [row 170](#row-170-closing-loop) when row 68 closed but DDD meta prelude capstone still lags after row 169 on the full capstone path,"
)
ROW189_EPILOGUE_PROCEED_NEW = (
    "Proceed to [row 190](#row-190-closing-loop) when row 68 closed but DDD meta prelude capstone still lags after row 189 on the full capstone path,"
)

ROW189_BABY_OLD = (
    "row 169 when **VII.0 Bridge and Row 68 → Row 49 meta must read on the same wire before row 170 DDD meta prelude capstone opens on the full capstone path**"
)
ROW189_BABY_NEW = (
    "row 189 when **VII.0 Bridge and Row 68 → Row 49 meta must read on the same wire before row 190 DDD meta prelude capstone opens on the full capstone path**"
)

ROW189_TAIL_OLD = (
    "When row 189 is complete, proceed to [row 170](preface.md#skill-navigation-row-170) when taxonomy meta prelude capstone is clean but DDD meta prelude capstone still lags after verified Burgers closure on the full capstone path, to [row 150](preface.md#skill-navigation-row-150) when taxonomy meta prelude capstone is clean but DDD meta prelude capstone still lags after verified Burgers closure on the opening-hinge capstone path alone, to [row 130](preface.md#skill-navigation-row-130) for the Row 68 ↔ Row 50 DDD meta audit on the opening-hinge prelude path alone, to [row 149](preface.md#skill-navigation-row-149) for the Row 68 ↔ Row 49 meta audit on the opening-hinge prelude path alone, to [row 169](preface.md#skill-navigation-row-169) when taxonomy meta prelude capstone still lags after verified midpoint meta prelude capstone on the opening-hinge capstone path alone, to [row 188](preface.md#skill-navigation-row-188) when midpoint meta prelude capstone still lags after verified part-boundary meta prelude capstone on the full capstone path, to [row 89](preface.md#skill-navigation-row-89) for the Row 68 ↔ Row 49 taxonomy opening prelude audit alone, to [row 49](preface.md#skill-navigation-row-49) for the VII.0 → VII.1 meta audit alone, to [row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, or extend prose only under `writings/` then sync."
)
ROW189_TAIL_NEW = (
    "When row 189 is complete, proceed to [row 190](preface.md#skill-navigation-row-190) when taxonomy meta prelude capstone is clean but DDD meta prelude capstone still lags after verified Burgers closure on the full capstone path, to [row 170](preface.md#skill-navigation-row-170) when taxonomy meta prelude capstone is clean but DDD meta prelude capstone still lags after verified Burgers closure on the opening-hinge capstone path alone, to [row 150](preface.md#skill-navigation-row-150) for the Row 68 ↔ Row 50 DDD meta audit on the opening-hinge prelude path alone, to [row 169](preface.md#skill-navigation-row-169) for the Row 68 ↔ Row 49 meta audit on the opening-hinge prelude path alone, to [row 189](preface.md#skill-navigation-row-189) when taxonomy meta prelude capstone still lags after verified midpoint meta prelude capstone on the opening-hinge capstone path alone, to [row 188](preface.md#skill-navigation-row-188) when midpoint meta prelude capstone still lags after verified part-boundary meta prelude capstone on the full capstone path, to [row 89](preface.md#skill-navigation-row-89) for the Row 68 ↔ Row 49 taxonomy opening prelude audit alone, to [row 49](preface.md#skill-navigation-row-49) for the VII.0 → VII.1 meta audit alone, to [row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, or extend prose only under `writings/` then sync."
)


def main() -> None:
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "### Row 190 skill checkpoint" in preface and preface.index("### Row 190 skill checkpoint") < preface.index(copper):
        print("preface: row 190 already present")
    else:
        if ROW189_TAIL_OLD not in preface:
            raise SystemExit("row 189 tail proceed string not found")
        preface = preface.replace(ROW189_TAIL_OLD, ROW189_TAIL_NEW, 1)
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + ROW190_PREFACE + copper)
        preface_path.write_text(preface)
        print("preface: added row 190")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-190" not in prologue:
        needle = "| Row 68 → Row 169 Row 68 → Row 49 taxonomy meta prelude capstone reunion (row 189) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 189 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + PROLOGUE_COMPASS + prologue[line_end + 1 :]
        if "row-190-closing-stitch" not in prologue:
            prologue = prologue.replace(
                "**Row 189 closing stitch",
                PROLOGUE_STITCH + "**Row 189 closing stitch",
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-189"></span>Row 189 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview row 189 not found")
        prologue = prologue.replace(preview_anchor, PROLOGUE_PREVIEW + preview_anchor)
        if ROW189_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW189_STITCH_OLD, ROW189_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 190")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "row-190-closing-loop" not in epilogue:
        if ROW189_EPILOGUE_PROCEED_OLD in epilogue:
            epilogue = epilogue.replace(ROW189_EPILOGUE_PROCEED_OLD, ROW189_EPILOGUE_PROCEED_NEW)
        marker = "### Row 186 closing loop (Row 68 → Row 166 Row 68 → Row 66 Writings canonical meta prelude capstone reunion)"
        if marker not in epilogue:
            raise SystemExit("epilogue row 186 insert anchor not found")
        epilogue = epilogue.replace(marker, EPILOGUE_LOOP + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 190")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row170-ddd-meta-prelude-capstone-reunion-index-row-190" not in sources:
        sources = sources.replace(
            "| 170 | Row 68 → Row 150 Row 68 → Row 50 DDD meta prelude capstone",
            SOURCES_TABLE + "| 170 | Row 68 → Row 150 Row 68 → Row 50 DDD meta prelude capstone",
            1,
        )
        sources = sources.replace(
            "## Row 68 → Row 150 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 170)",
            SOURCES_INDEX + "## Row 68 → Row 150 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 170)",
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 190")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-190-baby-picture-row68-row170" not in memory:
        memory = memory.replace(
            "| 189 | Meta | [Row 68 → Row 169 taxonomy meta prelude capstone reunion index]",
            MEMORY_TABLE + "| 189 | Meta | [Row 68 → Row 169 taxonomy meta prelude capstone reunion index]",
            1,
        )
        memory = memory.replace(
            "### Row 170 baby picture (Row 68 → Row 150 Row 68 → Row 50 DDD meta prelude capstone reunion) {#row-170-baby-picture-row68-row150-ddd-meta-prelude-capstone-reunion}",
            MEMORY_BABY
            + "### Row 170 baby picture (Row 68 → Row 150 Row 68 → Row 50 DDD meta prelude capstone reunion) {#row-170-baby-picture-row68-row150-ddd-meta-prelude-capstone-reunion}",
            1,
        )
        if ROW189_BABY_OLD in memory:
            memory = memory.replace(ROW189_BABY_OLD, ROW189_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 190")


if __name__ == "__main__":
    main()
