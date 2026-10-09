#!/usr/bin/env python3
"""Add row 172 meta-stitch (Row 68 → Row 152 ↔ Row 52 atomistic meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def t152_to_172(text: str) -> str:
    """Transform row-152 capstone-path meta copy to row 172 (152→172, 132→152 inner, 171 gate)."""
    repl = [
        ("Row 68 → Row 132 Row 68 → Row 52", "Row 68 → Row 152 Row 68 → Row 52"),
        (
            "row68-row132-atomistic-meta-prelude-capstone-reunion-index-row-152",
            "TEMP_ROW172_ATOM_INDEX",
        ),
        (
            "row-152-baby-picture-row68-row132-atomistic-meta-prelude-capstone-reunion",
            "row-172-baby-picture-row68-row152-atomistic-meta-prelude-capstone-reunion",
        ),
        ("skill-navigation-row-152", "skill-navigation-row-172"),
        ("prologue-preview-row-152", "prologue-preview-row-172"),
        ("row-152-closing-stitch", "row-172-closing-stitch"),
        ("row-152-closing-loop", "row-172-closing-loop"),
        ("Row 152 three-way audit", "Row 172 three-way audit"),
        (
            "[row 151](preface.md#skill-navigation-row-151) or [row 132](preface.md#skill-navigation-row-132)",
            "[row 171](preface.md#skill-navigation-row-171) or [row 152](preface.md#skill-navigation-row-152)",
        ),
        (
            "[row 151](preface.md#skill-navigation-row-151) or [Row 68 → Row 132 atomistic meta prelude capstone reunion index (row 152)](appendix/sources.md#row68-row132-atomistic-meta-prelude-capstone-reunion-index-row-152)",
            "[row 171](preface.md#skill-navigation-row-171) or [Row 68 → Row 152 atomistic meta prelude capstone reunion index (row 172)](appendix/sources.md#row68-row152-atomistic-meta-prelude-capstone-reunion-index-row-172)",
        ),
        (
            "verified homogenization meta prelude capstone closure (row 151)",
            "verified homogenization meta prelude capstone closure (row 171)",
        ),
        (
            "before row 173 dynamics meta prelude capstone reunion opens on the full capstone path",
            "before row 173 dynamics meta prelude capstone reunion opens on the full capstone path",
        ),
        (
            "before row 154 export meta prelude capstone reunion opens on the full capstone path",
            "before row 174 export meta prelude capstone reunion opens on the full capstone path",
        ),
    ]
    out = text
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW172_ATOM_INDEX",
        "row68-row152-atomistic-meta-prelude-capstone-reunion-index-row-172",
    )
    out = out.replace("row 152", "row 172")
    out = out.replace("Row 152", "Row 172")
    out = out.replace("[row 172](preface.md#skill-navigation-row-171)", "[row 171](preface.md#skill-navigation-row-171)")
    out = out.replace("[row 172](preface.md#skill-navigation-row-152)", "[row 152](preface.md#skill-navigation-row-152)")
    out = out.replace("row 1725", "row 173")
    out = out.replace("row 1726", "row 174")
    out = out.replace("row 172 or row 172", "row 171 or row 152")
    out = out.replace("When row 172 closed", "When row 171 closed")
    out = out.replace("after row 172 alone", "after row 171 alone")
    out = out.replace("Recite [preface row 172]", "Recite [preface row 171]")
    out = out.replace("row 172 or row 152 recited", "row 171 or row 152 recited")
    out = out.replace("row 151 closed", "row 171 closed")
    out = out.replace("Row 151 closed", "Row 171 closed")
    out = out.replace("row 151 or row 132 recited", "row 171 or row 152 recited")
    out = out.replace("row 150 or row 51 recited", "row 170 or row 171 recited")
    out = out.replace("row 132", "row 152")
    out = out.replace("Row 132", "Row 152")
    out = out.replace("row 112", "row 132")
    out = out.replace("Row 112", "Row 152")
    out = out.replace(
        "row68-row112-atomistic-meta-prelude-capstone-reunion-index-row-132",
        "row68-row132-atomistic-meta-prelude-capstone-reunion-index-row-152",
    )
    out = out.replace(
        "row68-row131-homogenization-meta-prelude-capstone-reunion-index-row-151",
        "row68-row151-homogenization-meta-prelude-capstone-reunion-index-row-171",
    )
    out = out.replace("Row 68 → Row 172 Row 68 → Row 52", "Row 68 → Row 152 Row 68 → Row 52")
    out = out.replace(
        "[preface row 152](../preface.md#skill-navigation-row-132)",
        "[preface row 152](../preface.md#skill-navigation-row-152)",
    )
    out = out.replace("row 151's polycrystal", "row 171's polycrystal")
    out = out.replace("from row 172's", "from row 171's")
    return out


def extract_preface_row152(preface: str) -> str:
    start = preface.index("### Row 152 skill checkpoint")
    end = preface.index("\n\n### Row 153 skill checkpoint")
    return preface[start:end]


ROW172_PREFACE = t152_to_172(extract_preface_row152((ROOT / "writings/preface/chapters/preface.md").read_text())) + "\n\n"

PROLOGUE_COMPASS = (
    "| Row 68 → Row 152 Row 68 → Row 52 atomistic meta prelude capstone reunion (row 172) | "
    "[Preface: row 172 skill checkpoint](../preface.md#skill-navigation-row-172) · "
    "[Row 68 → Row 152 atomistic meta prelude capstone reunion index](../appendix/sources.md#row68-row152-atomistic-meta-prelude-capstone-reunion-index-row-172) · "
    "[memory sheet row 172 baby picture](../appendix/memory-sheet.md#row-172-baby-picture-row68-row152-atomistic-meta-prelude-capstone-reunion) · "
    "[prologue row 172 preview row](#prologue-preview-row-172); [prologue row 172 closing stitch](#row-172-closing-stitch); "
    "[epilogue row 172 closing loop](../epilogue/multiscale.md#row-172-closing-loop) — "
    "read row 68 gate + row 171 or row 152 homogenization meta prelude capstone / atomistic meta prelude gate + VII.3 Bridge → opening hinge → VIII.1 phase space + row 52 meta aloud "
    "when polycrystal handoff is clean on the full capstone path but LAMMPS decks feel like AtomModel homework after verified homogenization meta prelude capstone on the full capstone path |\n"
)

_prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
_row152_stitch_body = (
    _prologue.split("**Row 152 closing stitch")[1].split("**Row 153 closing stitch")[0].lstrip().split("\n\n")[0]
)
PROLOGUE_STITCH = t152_to_172(
    "**Row 152 closing stitch (Row 68 → Row 132 Row 68 → Row 52 atomistic meta prelude capstone reunion).** {#row-152-closing-stitch} "
    + _row152_stitch_body.split(".** {#row-152-closing-stitch} ", 1)[-1]
) + "\n\n"

PROLOGUE_PREVIEW = (
    '| <span id="prologue-preview-row-172"></span>Row 172 preview (Row 68 → Row 152 Row 68 → Row 52 atomistic meta prelude capstone reunion) | '
    "Explain why midpoint closure (row 68) and VII.3 → VIII.1 meta (row 52) must be read together with the Bridge → phase-space chain after verified homogenization meta prelude capstone on the full capstone path before DAMASK exports and LAMMPS EAM tables feel like separate courses | "
    'One sentence: "read row 68 gate + row 171 or row 152 homogenization meta prelude capstone / atomistic meta prelude gate + VII.3 Bridge → opening hinge → VIII.1 phase space + row 52 meta aloud when polycrystal handoff is clean on the full capstone path but LAMMPS decks feel like AtomModel homework after verified homogenization meta prelude capstone on the full capstone path" — '
    "[preface row 172 skill checkpoint](../preface.md#skill-navigation-row-172); [prologue row 172 closing stitch](#row-172-closing-stitch); "
    "[Row 68 → Row 152 reunion index](../appendix/sources.md#row68-row152-atomistic-meta-prelude-capstone-reunion-index-row-172); "
    "[memory sheet row 172 baby picture](../appendix/memory-sheet.md#row-172-baby-picture-row68-row152-atomistic-meta-prelude-capstone-reunion); "
    "[VII.3 Bridge to Part VIII](../part07-defects/03-polycrystal-and-fem-handoff.md#bridge-to-part-viii); "
    "[VII.3 opening hinge to VIII.1](../part07-defects/03-polycrystal-and-fem-handoff.md#opening-hinge-vii3-to-viii1); "
    "[preface row 52 skill checkpoint](../preface.md#skill-navigation-row-52); "
    "[preface row 171 skill checkpoint](../preface.md#skill-navigation-row-171); "
    "[epilogue row 172 closing loop](../epilogue/multiscale.md#row-172-closing-loop) |\n"
)

_epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
EPILOGUE_LOOP = t152_to_172(
    "### Row 152 closing loop"
    + _epilogue.split("### Row 152 closing loop")[1].split("### Row 153 closing loop")[0]
)

SOURCES_TABLE = (
    "| 172 | Row 68 → Row 152 Row 68 → Row 52 atomistic meta prelude capstone (midpoint prelude gate ↔ homogenization meta prelude capstone on full capstone path ↔ row 52 meta) | "
    "[Row 68 → Row 152 atomistic meta prelude capstone reunion index](#row68-row152-atomistic-meta-prelude-capstone-reunion-index-row-172) · "
    "[preface row 172](../preface.md#skill-navigation-row-172) · "
    "[prologue row 172 preview](../prologue/00-many-scales.md#prologue-preview-row-172) · "
    "[prologue row 172 closing stitch](../prologue/00-many-scales.md#row-172-closing-stitch) · "
    "[epilogue row 172 closing loop](../epilogue/multiscale.md#row-172-closing-loop) · "
    "[memory sheet row 172 baby picture](memory-sheet.md#row-172-baby-picture-row68-row152-atomistic-meta-prelude-capstone-reunion) | "
    "Row 68 closed but **row 52 VII.3 → VIII.1 opening hinge still feels disconnected from verified homogenization meta prelude capstone on the full capstone path** — "
    "read row 68 + row 171 or row 152 gate + VII.3 Bridge → opening hinge → VIII.1 phase space + row 52; "
    "[preface row 52](../preface.md#skill-navigation-row-52) |\n"
)

SOURCES_INDEX = t152_to_172(
    (ROOT / "writings/appendix/chapters/sources.md")
    .read_text()
    .split("## Row 68 → Row 132 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 152)")[1]
    .split("## Row 68 → Row 133 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 153)")[0]
)
SOURCES_INDEX = (
    "## Row 68 → Row 152 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 172)"
    + SOURCES_INDEX
)

MEMORY_TABLE = (
    "| 172 | Meta | [Row 68 → Row 152 atomistic meta prelude capstone reunion index](sources.md#row68-row152-atomistic-meta-prelude-capstone-reunion-index-row-172) · "
    "[preface row 172 skill checkpoint](../preface.md#skill-navigation-row-172) · "
    "[prologue row 172 preview](../prologue/00-many-scales.md#prologue-preview-row-172) · "
    "[prologue row 172 closing stitch](../prologue/00-many-scales.md#row-172-closing-stitch) · "
    "[epilogue row 172 closing loop](../epilogue/multiscale.md#row-172-closing-loop) | "
    "Row 68 closed but row 52 atomistic meta reunion feels disconnected from verified homogenization meta prelude capstone on the full capstone path — "
    "read row 68 + row 171 or row 152 gate + VII.3 Bridge → opening hinge → VIII.1 phase space + row 52; "
    "[row 172 baby picture](#row-172-baby-picture-row68-row152-atomistic-meta-prelude-capstone-reunion) |\n"
)

MEMORY_BABY = t152_to_172(
    (ROOT / "writings/appendix/chapters/memory-sheet.md")
    .read_text()
    .split("### Row 152 baby picture (Row 68 → Row 132 Row 68 → Row 52 atomistic meta prelude capstone reunion)")[1]
    .split("### Row 153 baby picture")[0]
)
MEMORY_BABY = (
    "### Row 172 baby picture (Row 68 → Row 152 Row 68 → Row 52 atomistic meta prelude capstone reunion)"
    + MEMORY_BABY.split(")", 1)[1]
    if ")" in MEMORY_BABY
    else "### Row 172 baby picture" + MEMORY_BABY
)

ROW171_TAIL_MARKER = "**When to pause.** Read the [prologue row 171 closing stitch]"
ROW171_TAIL_END = "or extend prose only under `writings/` then sync.\n\n\n\n## The copper wire through the book"

ROW171_BABY_OLD = (
    "row 151 when **VII.2 Bridge and Row 68 → Row 51 meta must read on the same wire before row 152 atomistic meta prelude capstone opens on the full capstone path**"
)
ROW171_BABY_NEW = (
    "row 171 when **VII.2 Bridge and Row 68 → Row 51 meta must read on the same wire before row 172 atomistic meta prelude capstone opens on the full capstone path**"
)


def update_row171_tail(preface: str) -> str:
    start = preface.index(ROW171_TAIL_MARKER)
    end = preface.index(ROW171_TAIL_END)
    block = preface[start:end]
    new_block = block.replace(
        "when opening [row 152](preface.md#skill-navigation-row-152) before row 52 closes on the full capstone path",
        "when opening [row 172](preface.md#skill-navigation-row-172) before row 52 closes on the full capstone path",
    )
    new_block = new_block.replace(
        "When row 171 is complete, proceed to [row 152](preface.md#skill-navigation-row-152) when LAMMPS decks feel like AtomModel homework after verified homogenization meta prelude capstone on the full capstone path, to [row 132](preface.md#skill-navigation-row-132) when atomistic meta prelude capstone still lags after verified homogenization meta prelude capstone on the opening-hinge capstone path alone, to [row 112](preface.md#skill-navigation-row-112) for the Row 68 ↔ Row 52 atomistic meta audit on the opening-hinge prelude path alone, to [row 151](preface.md#skill-navigation-row-151) when homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the opening-hinge capstone path alone, to [row 131](preface.md#skill-navigation-row-131) for the Row 68 ↔ Row 51 homogenization meta audit on the opening-hinge prelude path alone, to [row 170](preface.md#skill-navigation-row-170) when DDD meta prelude capstone still lags after verified taxonomy meta prelude capstone on the full capstone path, to [row 51](preface.md#skill-navigation-row-51) when only VII.2 → VII.3 stalls, or extend prose only under `writings/` then sync.",
        "When row 171 is complete, proceed to [row 172](preface.md#skill-navigation-row-172) when LAMMPS decks feel like AtomModel homework after verified homogenization meta prelude capstone on the full capstone path, to [row 152](preface.md#skill-navigation-row-152) when atomistic meta prelude capstone still lags after verified homogenization meta prelude capstone on the opening-hinge capstone path alone, to [row 132](preface.md#skill-navigation-row-132) for the Row 68 ↔ Row 52 atomistic meta audit on the opening-hinge prelude path alone, to [row 151](preface.md#skill-navigation-row-151) when homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the opening-hinge capstone path alone, to [row 131](preface.md#skill-navigation-row-131) for the Row 68 ↔ Row 51 homogenization meta audit on the opening-hinge prelude path alone, to [row 170](preface.md#skill-navigation-row-170) when DDD meta prelude capstone still lags after verified taxonomy meta prelude capstone on the full capstone path, to [row 51](preface.md#skill-navigation-row-51) when only VII.2 → VII.3 stalls, or extend prose only under `writings/` then sync.",
    )
    return preface[:start] + new_block + preface[end:]


def main():
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "skill-navigation-row-172" in preface:
        print("preface: row 172 already present")
    else:
        if "skill-navigation-row-171" in preface:
            preface = update_row171_tail(preface)
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + ROW172_PREFACE + copper)
        preface_path.write_text(preface)
        print("preface: added row 172")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-172" not in prologue:
        needle = "| Row 68 → Row 151 Row 68 → Row 51 homogenization meta prelude capstone reunion (row 171) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 171 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + PROLOGUE_COMPASS + prologue[line_end + 1 :]
        prologue = prologue.replace(
            "**Row 171 closing stitch",
            PROLOGUE_STITCH + "**Row 171 closing stitch",
        )
        prologue = prologue.replace(
            '| <span id="prologue-preview-row-171"></span>Row 171 preview',
            PROLOGUE_PREVIEW + '| <span id="prologue-preview-row-171"></span>Row 171 preview',
        )
        prologue_path.write_text(prologue)
        print("prologue: added row 172")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "row-172-closing-loop" not in epilogue:
        marker = (
            "Proceed to [row 152](#row-152-closing-loop) when row 68 closed but atomistic meta prelude capstone still lags after row 171 on the full capstone path, to [row 132](#row-132-closing-loop) when atomistic meta prelude capstone still lags after verified homogenization meta prelude capstone on the opening-hinge capstone path alone, to [row 112](#row-112-closing-loop) for the Row 68 ↔ Row 52 atomistic meta audit on the opening-hinge prelude path alone, to [row 151](#row-131-closing-loop) for the Row 68 ↔ Row 51 homogenization meta audit on the opening-hinge capstone path alone, to [row 150](#row-150-closing-loop) when DDD meta prelude capstone still lags after verified taxonomy meta prelude capstone on the full capstone path, to [row 51](#row-51-closing-loop) when only VII.2 → VII.3 stalls, or extend prose only under `writings/` then sync.\n\n\n\n\n\n\n\n\n### Row 129 closing loop"
        )
        replacement = (
            "Proceed to [row 172](#row-172-closing-loop) when row 68 closed but atomistic meta prelude capstone still lags after row 171 on the full capstone path, to [row 152](#row-152-closing-loop) when atomistic meta prelude capstone still lags after verified homogenization meta prelude capstone on the opening-hinge capstone path alone, to [row 132](#row-132-closing-loop) for the Row 68 ↔ Row 52 atomistic meta audit on the opening-hinge prelude path alone, to [row 151](#row-151-closing-loop) for the Row 68 ↔ Row 51 homogenization meta audit on the opening-hinge capstone path alone, to [row 170](#row-170-closing-loop) when DDD meta prelude capstone still lags after verified taxonomy meta prelude capstone on the full capstone path, to [row 51](#row-51-closing-loop) when only VII.2 → VII.3 stalls, or extend prose only under `writings/` then sync.\n\n\n\n\n\n\n\n\n"
            + EPILOGUE_LOOP
            + "\n\n\n\n\n\n\n\n### Row 129 closing loop"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 171 end marker not found")
        epilogue = epilogue.replace(marker, replacement, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 172")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row152-atomistic-meta-prelude-capstone-reunion-index-row-172" not in sources:
        sources = sources.replace(
            "| 152 | Row 68 → Row 132 Row 68 → Row 52 atomistic meta prelude capstone",
            SOURCES_TABLE + "| 152 | Row 68 → Row 132 Row 68 → Row 52 atomistic meta prelude capstone",
        )
        sources = sources.replace(
            "## Row 68 → Row 132 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 152)",
            SOURCES_INDEX + "## Row 68 → Row 132 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 152)",
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 172")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-172-baby-picture-row68-row152" not in memory:
        memory = memory.replace(
            "| 171 | Meta | [Row 68 → Row 151 homogenization meta prelude capstone reunion index]",
            MEMORY_TABLE + "| 171 | Meta | [Row 68 → Row 151 homogenization meta prelude capstone reunion index]",
        )
        memory = memory.replace(
            "### Row 152 baby picture (Row 68 → Row 132 Row 68 → Row 52 atomistic meta prelude capstone reunion) {#row-152-baby-picture-row68-row132-atomistic-meta-prelude-capstone-reunion}",
            MEMORY_BABY + "### Row 152 baby picture (Row 68 → Row 132 Row 68 → Row 52 atomistic meta prelude capstone reunion) {#row-152-baby-picture-row68-row132-atomistic-meta-prelude-capstone-reunion}",
            1,
        )
        if ROW171_BABY_OLD in memory:
            memory = memory.replace(ROW171_BABY_OLD, ROW171_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 172")


if __name__ == "__main__":
    main()
