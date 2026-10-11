#!/usr/bin/env python3
"""Add row 170 meta-stitch (Row 68 → Row 150 ↔ Row 50 DDD meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def taxonomy_stitch_to_ddd150(text: str) -> str:
    """Map row 149 taxonomy closing-stitch prose to row 150 DDD closing-stitch template."""
    repl = [
        ("Row 68 → Row 129 Row 68 → Row 49 taxonomy meta prelude capstone reunion", "Row 68 → Row 130 Row 68 → Row 50 DDD meta prelude capstone reunion"),
        ("{#row-149-closing-stitch}", "{#row-150-closing-stitch}"),
        ("Row 149 closing stitch", "Row 150 closing stitch"),
        ("When row 148 closed", "When row 149 closed"),
        ("row 147 or row 128 recited", "row 149 or row 130 recited"),
        ("intermission → VII.0 landing recited with `hardening.yaml` beside Act IV", "VII.0 Bridge → VII.1 taxonomy recited with slip-line Lab act classified line defects"),
        ("row 49 VII.0 → VII.1 opening hinge still opens like standalone Defects Notes homework after the forest Scene", "row 50 VII.1 → VII.2 opening hinge still opens like standalone OpenDiS homework after the slip-line Lab act"),
        ("chapter 00 and chapter 01", "chapter 01 and chapter 02"),
        ("Burgers dimension tables feel disconnected from fitted \\(H\\) at the load cell knee", "mobility tables feel disconnected from Burgers circuits at the yield knee"),
        ("row 49's Bridge → taxonomy audit feels disconnected from row 148's continuum → defects closure", "row 50's Bridge → Peach–Köhler audit feels disconnected from row 149's Burgers → segment-network turn"),
        ("skill-navigation-row-149", "skill-navigation-row-150"),
        ("Row 68 → Row 129 reunion index", "Row 68 → Row 130 reunion index"),
        ("row68-row129-taxonomy-meta-prelude-capstone-reunion-index-row-149", "row68-row130-ddd-meta-prelude-capstone-reunion-index-row-150"),
        ("row-149-closing-loop", "row-150-closing-loop"),
        ("before row 150 DDD meta prelude capstone reunion opens", "before row 151 homogenization meta prelude capstone reunion opens"),
        ("before the DDD meta prelude capstone", "before the homogenization meta prelude capstone"),
    ]
    out = text
    for old, new in repl:
        out = out.replace(old, new)
    return out


def t150_to_170(text: str) -> str:
    """Transform row-150 capstone-path meta copy to row 170 (150→170, 130→150 inner, 169 gate)."""
    repl = [
        ("Row 68 → Row 130 Row 68 → Row 50", "Row 68 → Row 150 Row 68 → Row 50"),
        (
            "row68-row130-ddd-meta-prelude-capstone-reunion-index-row-150",
            "TEMP_ROW170_DDD_INDEX",
        ),
        (
            "row-150-baby-picture-row68-row130-ddd-meta-prelude-capstone-reunion",
            "row-170-baby-picture-row68-row150-ddd-meta-prelude-capstone-reunion",
        ),
        ("skill-navigation-row-150", "skill-navigation-row-170"),
        ("prologue-preview-row-150", "prologue-preview-row-170"),
        ("row-150-closing-stitch", "row-170-closing-stitch"),
        ("row-150-closing-loop", "row-170-closing-loop"),
        ("Row 150 three-way audit", "Row 170 three-way audit"),
        (
            "[row 149](preface.md#skill-navigation-row-149) or [row 130](preface.md#skill-navigation-row-130)",
            "[row 169](preface.md#skill-navigation-row-169) or [row 150](preface.md#skill-navigation-row-150)",
        ),
        (
            "[row 149](preface.md#skill-navigation-row-149) or [Row 68 → Row 130 DDD meta prelude capstone reunion index (row 150)](appendix/sources.md#row68-row130-ddd-meta-prelude-capstone-reunion-index-row-150)",
            "[row 169](preface.md#skill-navigation-row-169) or [Row 68 → Row 150 DDD meta prelude capstone reunion index (row 170)](appendix/sources.md#row68-row150-ddd-meta-prelude-capstone-reunion-index-row-170)",
        ),
        (
            "verified taxonomy meta prelude capstone on the full capstone path (row 149)",
            "verified taxonomy meta prelude capstone on the full capstone path (row 169)",
        ),
    ]
    out = text
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace("TEMP_ROW170_DDD_INDEX", "row68-row150-ddd-meta-prelude-capstone-reunion-index-row-170")
    out = out.replace("row 150", "row 170")
    out = out.replace("Row 150", "Row 170")
    out = out.replace("[row 170](preface.md#skill-navigation-row-169)", "[row 169](preface.md#skill-navigation-row-169)")
    out = out.replace("[row 170](preface.md#skill-navigation-row-150)", "[row 150](preface.md#skill-navigation-row-150)")
    out = out.replace("row 1705", "row 171")
    out = out.replace("row 1706", "row 172")
    out = out.replace("row 170 or row 170", "row 169 or row 150")
    out = out.replace("When row 170 closed", "When row 169 closed")
    out = out.replace("after row 170 alone", "after row 169 alone")
    out = out.replace("Recite [preface row 170]", "Recite [preface row 169]")
    out = out.replace("row 170 or row 150 recited", "row 169 or row 150 recited")
    out = out.replace("row 149 closed", "row 169 closed")
    out = out.replace("Row 149 closed", "Row 169 closed")
    out = out.replace("row 148 closed", "row 168 closed")
    out = out.replace("Row 148 closed", "Row 168 closed")
    out = out.replace("row 149 or row 130 recited", "row 169 or row 150 recited")
    out = out.replace("row 130", "row 150")
    out = out.replace("Row 130", "Row 150")
    out = out.replace("row 129", "row 149")
    out = out.replace("Row 129", "Row 149")
    out = out.replace("row 110", "row 130")
    out = out.replace("Row 110", "Row 130")
    out = out.replace(
        "row68-row110-ddd-meta-prelude-capstone-reunion-index-row-130",
        "row68-row130-ddd-meta-prelude-capstone-reunion-index-row-150",
    )
    out = out.replace(
        "row68-row129-taxonomy-meta-prelude-capstone-reunion-index-row-149",
        "row68-row149-taxonomy-meta-prelude-capstone-reunion-index-row-169",
    )
    out = out.replace("[preface row 149](../preface.md#skill-navigation-row-129)", "[preface row 149](../preface.md#skill-navigation-row-149)")
    out = out.replace("[preface row 149](../preface.md#skill-navigation-row-149)", "[preface row 169](../preface.md#skill-navigation-row-169)")
    out = out.replace("Row 68 → Row 170 Row 68 → Row 50", "Row 68 → Row 150 Row 68 → Row 50")
    return out


def extract_preface_row150(preface: str) -> str:
    start = preface.index("### Row 150 skill checkpoint")
    end = preface.index("\n\n### Row 151 skill checkpoint")
    return preface[start:end]


ROW170_PREFACE = t150_to_170(extract_preface_row150((ROOT / "writings/preface/chapters/preface.md").read_text())) + "\n\n"

PROLOGUE_COMPASS = (
    "| Row 68 → Row 150 Row 68 → Row 50 DDD meta prelude capstone reunion (row 170) | "
    "[Preface: row 170 skill checkpoint](../preface.md#skill-navigation-row-170) · "
    "[Row 68 → Row 150 DDD meta prelude capstone reunion index](../appendix/sources.md#row68-row150-ddd-meta-prelude-capstone-reunion-index-row-170) · "
    "[memory sheet row 170 baby picture](../appendix/memory-sheet.md#row-170-baby-picture-row68-row150-ddd-meta-prelude-capstone-reunion) · "
    "[prologue row 170 preview row](#prologue-preview-row-170); [prologue row 170 closing stitch](#row-170-closing-stitch); "
    "[epilogue row 170 closing loop](../epilogue/multiscale.md#row-170-closing-loop) — "
    "read row 68 gate + row 169 or row 150 taxonomy meta prelude capstone / DDD meta prelude gate + VII.1 Bridge → opening hinge → VII.2 Peach–Köhler + row 50 meta aloud "
    "when Burgers taxonomy is clean on the full capstone path but OpenDiS decks feel like DDD homework after verified taxonomy meta prelude capstone on the full capstone path |\n"
)

_prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
_row149_stitch_body = (
    _prologue.split("**Row 149 closing stitch")[1].split("**Row 151 closing stitch")[0].lstrip().split("\n\n")[0]
)
PROLOGUE_STITCH = t150_to_170(
    taxonomy_stitch_to_ddd150(
        "**Row 150 closing stitch (Row 68 → Row 130 Row 68 → Row 50 DDD meta prelude capstone reunion).** {#row-150-closing-stitch} "
        + _row149_stitch_body[len("**Row 149 closing stitch (Row 68 → Row 129 Row 68 → Row 49 taxonomy meta prelude capstone reunion).** {#row-149-closing-stitch} ") :]
    )
) + "\n\n"

PROLOGUE_PREVIEW = (
    "| <span id=\"prologue-preview-row-170\"></span>Row 170 preview (Row 68 → Row 150 Row 68 → Row 50 DDD meta prelude capstone reunion) | "
    "Explain why midpoint closure (row 68) and VII.1 → VII.2 meta (row 50) must be read together with the Bridge → Peach–Köhler chain after verified taxonomy meta prelude capstone on the full capstone path before Burgers tables and OpenDiS decks feel like separate courses | "
    "One sentence: \"read row 68 gate + row 169 or row 150 taxonomy meta prelude capstone / DDD meta prelude gate + VII.1 Bridge → opening hinge → VII.2 Peach–Köhler + row 50 meta aloud when Burgers taxonomy is clean on the full capstone path but OpenDiS decks feel like DDD homework after verified taxonomy meta prelude capstone on the full capstone path\" — "
    "[preface row 170 skill checkpoint](../preface.md#skill-navigation-row-170); [prologue row 170 closing stitch](#row-170-closing-stitch); "
    "[Row 68 → Row 150 reunion index](../appendix/sources.md#row68-row150-ddd-meta-prelude-capstone-reunion-index-row-170); "
    "[memory sheet row 170 baby picture](../appendix/memory-sheet.md#row-170-baby-picture-row68-row150-ddd-meta-prelude-capstone-reunion); "
    "[VII.1 Bridge](../part07-defects/01-defect-taxonomy.md#bridge); "
    "[VII.1 opening hinge to VII.2](../part07-defects/01-defect-taxonomy.md#opening-hinge-vii1-to-vii2); "
    "[preface row 50 skill checkpoint](../preface.md#skill-navigation-row-50); "
    "[preface row 169 skill checkpoint](../preface.md#skill-navigation-row-169); "
    "[epilogue row 170 closing loop](../epilogue/multiscale.md#row-170-closing-loop) |\n"
)

_epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
EPILOGUE_LOOP = t150_to_170(
    "### Row 150 closing loop"
    + _epilogue.split("### Row 150 closing loop")[1].split("### Row 151 closing loop")[0]
)

SOURCES_TABLE = (
    "| 170 | Row 68 → Row 150 Row 68 → Row 50 DDD meta prelude capstone (midpoint prelude gate ↔ taxonomy meta prelude capstone on full capstone path ↔ row 50 meta) | "
    "[Row 68 → Row 150 DDD meta prelude capstone reunion index](#row68-row150-ddd-meta-prelude-capstone-reunion-index-row-170) · "
    "[preface row 170](../preface.md#skill-navigation-row-170) · "
    "[prologue row 170 preview](../prologue/00-many-scales.md#prologue-preview-row-170) · "
    "[prologue row 170 closing stitch](../prologue/00-many-scales.md#row-170-closing-stitch) · "
    "[epilogue row 170 closing loop](../epilogue/multiscale.md#row-170-closing-loop) · "
    "[memory sheet row 170 baby picture](memory-sheet.md#row-170-baby-picture-row68-row150-ddd-meta-prelude-capstone-reunion) | "
    "Row 68 closed but **row 50 VII.1 → VII.2 opening hinge still feels disconnected from verified taxonomy meta prelude capstone on the full capstone path** — "
    "read row 68 + row 169 or row 150 gate + VII.1 Bridge → opening hinge → VII.2 Peach–Köhler + row 50; "
    "[preface row 50](../preface.md#skill-navigation-row-50) |\n"
)

SOURCES_INDEX = t150_to_170(
    (ROOT / "writings/appendix/chapters/sources.md")
    .read_text()
    .split("## Row 68 → Row 110 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 150)")[1]
    .split("## Row 68 → Row 131 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 151)")[0]
)
SOURCES_INDEX = (
    "## Row 68 → Row 150 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 170)"
    + SOURCES_INDEX
)

MEMORY_TABLE = (
    "| 170 | Meta | [Row 68 → Row 150 DDD meta prelude capstone reunion index](sources.md#row68-row150-ddd-meta-prelude-capstone-reunion-index-row-170) · "
    "[preface row 170 skill checkpoint](../preface.md#skill-navigation-row-170) · "
    "[prologue row 170 preview](../prologue/00-many-scales.md#prologue-preview-row-170) · "
    "[prologue row 170 closing stitch](../prologue/00-many-scales.md#row-170-closing-stitch) · "
    "[epilogue row 170 closing loop](../epilogue/multiscale.md#row-170-closing-loop) | "
    "Row 68 closed but row 50 DDD meta reunion feels disconnected from verified taxonomy meta prelude capstone on the full capstone path — "
    "read row 68 + row 169 or row 150 gate + VII.1 Bridge → opening hinge → VII.2 Peach–Köhler + row 50; "
    "[row 170 baby picture](#row-170-baby-picture-row68-row150-ddd-meta-prelude-capstone-reunion) |\n"
)

MEMORY_BABY = t150_to_170(
    (ROOT / "writings/appendix/chapters/memory-sheet.md")
    .read_text()
    .split("### Row 130 baby picture")[1]
    .split("### Row 147 baby picture")[0]
)
MEMORY_BABY = (
    "### Row 170 baby picture (Row 68 → Row 150 Row 68 → Row 50 DDD meta prelude capstone reunion)"
    + MEMORY_BABY.split(")", 1)[1]
    if ")" in MEMORY_BABY
    else "### Row 170 baby picture" + MEMORY_BABY
)

ROW169_TAIL_MARKER = "**When to pause.** Read the [prologue row 169 closing stitch]"
ROW169_TAIL_END = "or extend prose only under `writings/` then sync.\n\n\n\n\n## The copper wire through the book"

ROW169_STITCH_OLD = (
    "before row 150 DDD meta prelude capstone reunion opens on the full capstone path."
)
ROW169_STITCH_NEW = (
    "before row 170 DDD meta prelude capstone reunion opens on the full capstone path."
)

ROW169_EPILOGUE_PROCEED_OLD = (
    "Proceed to [row 150](#row-150-closing-loop) when row 68 closed but DDD meta prelude capstone still lags after row 169 on the full capstone path,"
)
ROW169_EPILOGUE_PROCEED_NEW = (
    "Proceed to [row 170](#row-170-closing-loop) when row 68 closed but DDD meta prelude capstone still lags after row 169 on the full capstone path,"
)

ROW169_BABY_OLD = (
    "row 149 when **VII.0 Bridge and Row 68 → Row 49 meta must read on the same wire before row 150 DDD meta prelude capstone opens on the full capstone path**"
)
ROW169_BABY_NEW = (
    "row 169 when **VII.0 Bridge and Row 68 → Row 49 meta must read on the same wire before row 170 DDD meta prelude capstone opens on the full capstone path**"
)


def update_row169_tail(preface: str) -> str:
    start = preface.index(ROW169_TAIL_MARKER)
    end = preface.index(ROW169_TAIL_END)
    block = preface[start:end]
    new_block = block.replace(
        "when opening [row 150](preface.md#skill-navigation-row-150) before row 50 closes on the full capstone path",
        "when opening [row 170](preface.md#skill-navigation-row-170) before row 50 closes on the full capstone path",
    )
    new_block = new_block.replace(
        "When row 169 is complete, proceed to [row 150](preface.md#skill-navigation-row-150) when taxonomy meta prelude capstone is clean but DDD meta prelude capstone still lags after verified Burgers closure on the full capstone path, to [row 130](preface.md#skill-navigation-row-130) when taxonomy meta prelude capstone is clean but DDD meta prelude capstone still lags after verified Burgers closure on the opening-hinge capstone path alone, to [row 110](preface.md#skill-navigation-row-110) for the Row 68 ↔ Row 50 DDD meta audit on the opening-hinge prelude path alone, to [row 129](preface.md#skill-navigation-row-129) for the Row 68 ↔ Row 49 meta audit on the opening-hinge prelude path alone, to [row 149](preface.md#skill-navigation-row-149) when taxonomy meta prelude capstone still lags after verified midpoint meta prelude capstone on the opening-hinge capstone path alone, to [row 168](preface.md#skill-navigation-row-168) when midpoint meta prelude capstone still lags after verified part-boundary meta prelude capstone on the full capstone path, to [row 89](preface.md#skill-navigation-row-89) for the Row 68 ↔ Row 49 taxonomy opening prelude audit alone, to [row 49](preface.md#skill-navigation-row-49) for the VII.0 → VII.1 meta audit alone, to [row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, or extend prose only under `writings/` then sync.",
        "When row 169 is complete, proceed to [row 170](preface.md#skill-navigation-row-170) when taxonomy meta prelude capstone is clean but DDD meta prelude capstone still lags after verified Burgers closure on the full capstone path, to [row 150](preface.md#skill-navigation-row-150) when taxonomy meta prelude capstone is clean but DDD meta prelude capstone still lags after verified Burgers closure on the opening-hinge capstone path alone, to [row 110](preface.md#skill-navigation-row-110) for the Row 68 ↔ Row 50 DDD meta audit on the opening-hinge prelude path alone, to [row 129](preface.md#skill-navigation-row-129) for the Row 68 ↔ Row 49 meta audit on the opening-hinge prelude path alone, to [row 149](preface.md#skill-navigation-row-149) when taxonomy meta prelude capstone still lags after verified midpoint meta prelude capstone on the opening-hinge capstone path alone, to [row 168](preface.md#skill-navigation-row-168) when midpoint meta prelude capstone still lags after verified part-boundary meta prelude capstone on the full capstone path, to [row 89](preface.md#skill-navigation-row-89) for the Row 68 ↔ Row 49 taxonomy opening prelude audit alone, to [row 49](preface.md#skill-navigation-row-49) for the VII.0 → VII.1 meta audit alone, to [row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, or extend prose only under `writings/` then sync.",
    )
    return preface[:start] + new_block + preface[end:]


def main():
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "skill-navigation-row-170" in preface and preface.index("skill-navigation-row-170") < preface.index(copper):
        print("preface: row 170 already present")
    else:
        preface = update_row169_tail(preface)
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + ROW170_PREFACE + copper)
        preface_path.write_text(preface)
        print("preface: added row 170")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-170" not in prologue:
        needle = "| Row 68 → Row 149 Row 68 → Row 49 taxonomy meta prelude capstone reunion (row 169) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 169 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + PROLOGUE_COMPASS + prologue[line_end + 1 :]
        prologue = prologue.replace(
            "**Row 169 closing stitch",
            PROLOGUE_STITCH + "**Row 169 closing stitch",
        )
        prologue = prologue.replace(
            '| <span id="prologue-preview-row-169"></span>Row 169 preview',
            PROLOGUE_PREVIEW + '| <span id="prologue-preview-row-169"></span>Row 169 preview',
        )
        if ROW169_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW169_STITCH_OLD, ROW169_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 170")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "row-170-closing-loop" not in epilogue:
        if ROW169_EPILOGUE_PROCEED_OLD in epilogue:
            epilogue = epilogue.replace(ROW169_EPILOGUE_PROCEED_OLD, ROW169_EPILOGUE_PROCEED_NEW)
        marker = (
            "to [row 49](#row-49-closing-loop) when only VII.0 → VII.1 stalls, or extend prose only under `writings/` then sync.\n\n\n### Row 129 closing loop"
        )
        replacement = (
            "to [row 49](#row-49-closing-loop) when only VII.0 → VII.1 stalls, or extend prose only under `writings/` then sync.\n\n\n"
            + EPILOGUE_LOOP
            + "\n\n\n### Row 129 closing loop"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 169 end marker not found")
        epilogue = epilogue.replace(marker, replacement, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 170")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row150-ddd-meta-prelude-capstone-reunion-index-row-170" not in sources:
        sources = sources.replace(
            "| 150 | Row 68 → Row 130 Row 68 → Row 50 DDD meta prelude capstone",
            SOURCES_TABLE + "| 150 | Row 68 → Row 130 Row 68 → Row 50 DDD meta prelude capstone",
        )
        sources = sources.replace(
            "## Row 68 → Row 110 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 150)",
            SOURCES_INDEX + "## Row 68 → Row 110 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 150)",
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 170")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-170-baby-picture-row68-row150" not in memory:
        memory = memory.replace(
            "| 169 | Meta | [Row 68 → Row 149 taxonomy meta prelude capstone reunion index]",
            MEMORY_TABLE + "| 169 | Meta | [Row 68 → Row 149 taxonomy meta prelude capstone reunion index]",
        )
        memory = memory.replace(
            "### Row 169 baby picture (Row 68 → Row 149 Row 68 → Row 49 taxonomy meta prelude capstone reunion) {#row-149-baby-picture-row68-row129-taxonomy-meta-prelude-capstone-reunion}",
            MEMORY_BABY + "### Row 169 baby picture (Row 68 → Row 149 Row 68 → Row 49 taxonomy meta prelude capstone reunion) {#row-149-baby-picture-row68-row129-taxonomy-meta-prelude-capstone-reunion}",
        )
        memory = memory.replace(ROW169_BABY_OLD, ROW169_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 170")


if __name__ == "__main__":
    main()
