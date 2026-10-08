#!/usr/bin/env python3
"""Add row 174 meta-stitch (Row 68 → Row 154 ↔ Row 54 export meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def t154_to_174(text: str) -> str:
    """Transform row-154 capstone-path meta copy to row 174 (154→174, 134→154 inner, 173 gate)."""
    repl = [
        ("Row 68 → Row 134 Row 68 → Row 54", "Row 68 → Row 154 Row 68 → Row 54"),
        (
            "row68-row134-export-meta-prelude-capstone-reunion-index-row-154",
            "TEMP_ROW174_EXP_INDEX",
        ),
        (
            "row-154-baby-picture-row68-row134-export-meta-prelude-capstone-reunion",
            "row-174-baby-picture-row68-row154-export-meta-prelude-capstone-reunion",
        ),
        (
            "skill-navigation-row-154",
            "TEMP_SKILL_NAV_154",
        ),
        ("prologue-preview-row-154", "prologue-preview-row-174"),
        ("row-154-closing-stitch", "row-174-closing-stitch"),
        ("row-154-closing-loop", "row-174-closing-loop"),
        ("Row 154 three-way audit", "Row 174 three-way audit"),
        (
            "[row 153](preface.md#skill-navigation-row-153) or [row 134](TEMP_SKILL_NAV_154)",
            "[row 173](preface.md#skill-navigation-row-173) or [row 154](TEMP_SKILL_NAV_154)",
        ),
        (
            "[row 153](preface.md#skill-navigation-row-153) or [Row 68 → Row 94 export meta prelude reunion index (row 134)](appendix/sources.md#row68-row114-export-meta-prelude-reunion-index-row-134)",
            "[row 173](preface.md#skill-navigation-row-173) or [Row 68 → Row 154 export meta prelude capstone reunion index (row 174)](appendix/sources.md#row68-row154-export-meta-prelude-capstone-reunion-index-row-174)",
        ),
        (
            "[row 153](preface.md#skill-navigation-row-153) or [Row 68 → Row 134 export meta prelude capstone reunion index (row 154)](appendix/sources.md#row68-row134-export-meta-prelude-capstone-reunion-index-row-154)",
            "[row 173](preface.md#skill-navigation-row-173) or [Row 68 → Row 154 export meta prelude capstone reunion index (row 174)](appendix/sources.md#row68-row154-export-meta-prelude-capstone-reunion-index-row-174)",
        ),
        (
            "verified dynamics meta prelude capstone closure (row 153)",
            "verified dynamics meta prelude capstone closure (row 173)",
        ),
        (
            "before row 155 electronic audit meta prelude capstone reunion opens on the full capstone path",
            "before row 175 electronic audit meta prelude capstone reunion opens on the full capstone path",
        ),
        (
            "before row 156 Born–Oppenheimer meta prelude capstone reunion opens on the full capstone path",
            "before row 176 Born–Oppenheimer meta prelude capstone reunion opens on the full capstone path",
        ),
    ]
    out = text
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW174_EXP_INDEX",
        "row68-row154-export-meta-prelude-capstone-reunion-index-row-174",
    )
    out = out.replace("TEMP_SKILL_NAV_154", "skill-navigation-row-154")
    out = out.replace("row 154", "row 174")
    out = out.replace("Row 154", "Row 174")
    out = out.replace("skill-navigation-row-154", "skill-navigation-row-174")
    out = out.replace("[row 174](preface.md#skill-navigation-row-173)", "[row 173](preface.md#skill-navigation-row-173)")
    out = out.replace("[row 174](preface.md#skill-navigation-row-174)", "[row 174](preface.md#skill-navigation-row-174)")
    out = out.replace("[row 174](preface.md#skill-navigation-row-154)", "[row 154](preface.md#skill-navigation-row-154)")
    out = out.replace("[row 154](preface.md#skill-navigation-row-174)", "[row 154](preface.md#skill-navigation-row-154)")
    out = out.replace("when row 153 closed but row 54", "when row 173 closed but row 54")
    out = out.replace("[preface row 154](../preface.md#skill-navigation-row-174)", "[preface row 154](../preface.md#skill-navigation-row-154)")
    out = out.replace("row 1545", "row 175")
    out = out.replace("row 1546", "row 176")
    out = out.replace("row 174 or row 174", "row 173 or row 154")
    out = out.replace("When row 174 closed", "When row 173 closed")
    out = out.replace("after row 174 alone", "after row 173 alone")
    out = out.replace("Recite [preface row 174]", "Recite [preface row 173]")
    out = out.replace("row 174 or row 154 recited", "row 173 or row 154 recited")
    out = out.replace("When row 174 closed — dynamics", "When row 173 closed — dynamics")
    out = out.replace("When row 153 closed — dynamics", "When row 173 closed — dynamics")
    out = out.replace("row 153 or row 134 recited", "row 173 or row 154 recited")
    out = out.replace("row 153 or row 54 recited", "row 173 or row 154 recited")
    out = out.replace("when row 153 closed dynamics", "when row 173 closed dynamics")
    out = out.replace("(preface.md#skill-navigation-row-134)", "(preface.md#skill-navigation-row-154)")
    out = out.replace("Row 68 → Row 174 export meta prelude capstone reunion index", "Row 68 → Row 154 export meta prelude capstone reunion index")
    out = out.replace("row 152 or row 53 recited", "row 172 or row 153 recited")
    out = out.replace("row 134", "row 154")
    out = out.replace("Row 134", "Row 154")
    out = out.replace("row 114", "row 134")
    out = out.replace("Row 114", "Row 134")
    out = out.replace(
        "row68-row114-export-meta-prelude-reunion-index-row-134",
        "row68-row134-export-meta-prelude-capstone-reunion-index-row-154",
    )
    out = out.replace(
        "row68-row133-dynamics-meta-prelude-capstone-reunion-index-row-153",
        "row68-row153-dynamics-meta-prelude-capstone-reunion-index-row-173",
    )
    out = out.replace("Row 68 → Row 174 Row 68 → Row 54", "Row 68 → Row 154 Row 68 → Row 54")
    out = out.replace(
        "[preface row 154](../preface.md#skill-navigation-row-134)",
        "[preface row 154](../preface.md#skill-navigation-row-154)",
    )
    out = out.replace(
        "Confirm [row 153](preface.md#skill-navigation-row-153) or [Row 68 → Row 154",
        "Confirm [row 173](preface.md#skill-navigation-row-173) or [Row 68 → Row 154",
    )
    out = out.replace(
        "and [row 153](preface.md#skill-navigation-row-153) or [row 154]",
        "and [row 173](preface.md#skill-navigation-row-173) or [row 154]",
    )
    out = out.replace("[row 134](preface.md#skill-navigation-row-114)", "[row 134](preface.md#skill-navigation-row-134)")
    out = out.replace("(preface.md#skill-navigation-row-174) when NPT", "(preface.md#skill-navigation-row-154) when NPT")
    out = out.replace("when row 153 and row 54", "when row 173 and row 54")
    out = out.replace("after row 153 alone", "after row 173 alone")
    out = out.replace("Scene after row 153.", "Scene after row 173.")
    out = out.replace("from row 174's", "from row 173's")
    out = out.replace("row 153's finite-\\(T\\) dynamics", "row 173's finite-\\(T\\) dynamics")
    out = out.replace("row 153 tells you", "row 173 tells you")
    out = out.replace("VIII.2 Bridge → VIII.3 pedigree", "VIII.2 Bridge → opening hinge → VIII.3 pedigree")
    return out


def extract_preface_row154(preface: str) -> str:
    start = preface.index("### Row 154 skill checkpoint")
    end = preface.index("\n\n### Row 155 skill checkpoint")
    return preface[start:end]


ROW174_PREFACE = t154_to_174(extract_preface_row154((ROOT / "writings/preface/chapters/preface.md").read_text())) + "\n\n"

PROLOGUE_COMPASS = (
    "| Row 68 → Row 154 Row 68 → Row 54 export meta prelude capstone reunion (row 174) | "
    "[Preface: row 174 skill checkpoint](../preface.md#skill-navigation-row-174) · "
    "[Row 68 → Row 154 export meta prelude capstone reunion index](../appendix/sources.md#row68-row154-export-meta-prelude-capstone-reunion-index-row-174) · "
    "[memory sheet row 174 baby picture](../appendix/memory-sheet.md#row-174-baby-picture-row68-row154-export-meta-prelude-capstone-reunion) · "
    "[prologue row 174 preview row](#prologue-preview-row-174); [prologue row 174 closing stitch](#row-174-closing-stitch); "
    "[epilogue row 174 closing loop](../epilogue/multiscale.md#row-174-closing-loop) — "
    "read row 68 gate + row 173 or row 154 dynamics meta prelude capstone / export meta prelude gate + VIII.2 Bridge → opening hinge → VIII.3 pedigree + row 54 meta aloud "
    "when NPT dynamics is clean on the full capstone path but yaml exports feel like standalone post-processing after verified dynamics meta prelude capstone |\n"
)

_prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
_row154_stitch_body = (
    _prologue.split("**Row 154 closing stitch")[1].split("**Row 155 closing stitch")[0].lstrip().split("\n\n")[0]
)
PROLOGUE_STITCH = t154_to_174(
    "**Row 154 closing stitch (Row 68 → Row 134 Row 68 → Row 54 export meta prelude capstone reunion).** {#row-154-closing-stitch} "
    + _row154_stitch_body.split(".** {#row-154-closing-stitch} ", 1)[-1]
) + "\n\n"

PROLOGUE_PREVIEW = (
    '| <span id="prologue-preview-row-174"></span>Row 174 preview (Row 68 → Row 154 Row 68 → Row 54 export meta prelude capstone reunion) | '
    "Explain why midpoint closure (row 68) and VIII.2 → VIII.3 meta (row 54) must be read together with the Bridge → pedigree chain after verified dynamics meta prelude capstone on the full capstone path before dynamics manifest and coarse-graining sections feel like separate courses | "
    'One sentence: "read row 68 gate + row 173 or row 154 dynamics meta prelude capstone / export meta prelude gate + VIII.2 Bridge → opening hinge → VIII.3 pedigree + row 54 meta aloud when NPT dynamics is clean on the full capstone path but yaml exports feel like standalone post-processing after verified dynamics meta prelude capstone" — '
    "[preface row 174 skill checkpoint](../preface.md#skill-navigation-row-174); [prologue row 174 closing stitch](#row-174-closing-stitch); "
    "[Row 68 → Row 154 reunion index](../appendix/sources.md#row68-row154-export-meta-prelude-capstone-reunion-index-row-174); "
    "[memory sheet row 174 baby picture](../appendix/memory-sheet.md#row-174-baby-picture-row68-row154-export-meta-prelude-capstone-reunion); "
    "[VIII.2 Bridge](../part08-md/02-ensembles-integrators.md#bridge); "
    "[VIII.3 opening hinge from VIII.2](../part08-md/03-ab-initio-and-coarse-graining.md#opening-hinge-viii2-to-viii3); "
    "[preface row 54 skill checkpoint](../preface.md#skill-navigation-row-54); "
    "[preface row 173 skill checkpoint](../preface.md#skill-navigation-row-173); "
    "[epilogue row 174 closing loop](../epilogue/multiscale.md#row-174-closing-loop) |\n"
)

_epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
EPILOGUE_LOOP = t154_to_174(
    "### Row 154 closing loop"
    + _epilogue.split("### Row 154 closing loop")[1].split("### Row 155 closing loop")[0]
)

SOURCES_TABLE = (
    "| 174 | Row 68 → Row 154 Row 68 → Row 54 export meta prelude capstone (midpoint prelude gate ↔ dynamics meta prelude capstone on full capstone path ↔ row 54 meta) | "
    "[Row 68 → Row 154 export meta prelude capstone reunion index](#row68-row154-export-meta-prelude-capstone-reunion-index-row-174) · "
    "[preface row 174](../preface.md#skill-navigation-row-174) · "
    "[prologue row 174 preview](../prologue/00-many-scales.md#prologue-preview-row-174) · "
    "[prologue row 174 closing stitch](../prologue/00-many-scales.md#row-174-closing-stitch) · "
    "[epilogue row 174 closing loop](../epilogue/multiscale.md#row-174-closing-loop) · "
    "[memory sheet row 174 baby picture](memory-sheet.md#row-174-baby-picture-row68-row154-export-meta-prelude-capstone-reunion) | "
    "Row 68 closed but **row 54 VIII.2 → VIII.3 opening hinge still feels disconnected from verified dynamics meta prelude capstone on the full capstone path** — "
    "read row 68 + row 173 or row 154 gate + VIII.2 Bridge → opening hinge → VIII.3 pedigree + row 54; "
    "[preface row 54](../preface.md#skill-navigation-row-54) |\n"
)

SOURCES_INDEX = t154_to_174(
    (ROOT / "writings/appendix/chapters/sources.md")
    .read_text()
    .split("## Row 68 → Row 134 Row 68 → Row 54 export meta prelude capstone reunion index (row 154)")[1]
    .split("## Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 155)")[0]
)
SOURCES_INDEX = (
    "## Row 68 → Row 154 Row 68 → Row 54 export meta prelude capstone reunion index (row 174)"
    + SOURCES_INDEX
)

MEMORY_TABLE = (
    "| 174 | Meta | [Row 68 → Row 154 export meta prelude capstone reunion index](sources.md#row68-row154-export-meta-prelude-capstone-reunion-index-row-174) · "
    "[preface row 174 skill checkpoint](../preface.md#skill-navigation-row-174) · "
    "[prologue row 174 preview](../prologue/00-many-scales.md#prologue-preview-row-174) · "
    "[prologue row 174 closing stitch](../prologue/00-many-scales.md#row-174-closing-stitch) · "
    "[epilogue row 174 closing loop](../epilogue/multiscale.md#row-174-closing-loop) | "
    "Row 68 closed but row 54 VIII.2 → VIII.3 opening hinge feels disconnected from verified dynamics meta prelude capstone on the full capstone path — "
    "read row 68 + row 173 or row 154 gate + VIII.2 Bridge → opening hinge → VIII.3 pedigree + row 54; "
    "[row 174 baby picture](#row-174-baby-picture-row68-row154-export-meta-prelude-capstone-reunion) |\n"
)

MEMORY_BABY = t154_to_174(
    (ROOT / "writings/appendix/chapters/memory-sheet.md")
    .read_text()
    .split("### Row 154 baby picture (Row 68 → Row 134 Row 68 → Row 54 export meta prelude capstone reunion)")[1]
    .split("### Row 155 baby picture")[0]
)
MEMORY_BABY = (
    "### Row 174 baby picture (Row 68 → Row 154 Row 68 → Row 54 export meta prelude capstone reunion)"
    + MEMORY_BABY.split(")", 1)[1]
    if ")" in MEMORY_BABY
    else "### Row 174 baby picture" + MEMORY_BABY
)

ROW173_TAIL_MARKER = "**When to pause.** Read the [prologue row 173 closing stitch]"
ROW173_TAIL_END = "or extend prose only under `writings/` then sync.\n\n\n\n## The copper wire through the book"

ROW173_BABY_OLD = (
    "row 173 when **VIII.1 Bridge and Row 68 → Row 53 meta must read on the same wire before row 154 export meta prelude capstone opens on the full capstone path**"
)
ROW173_BABY_NEW = (
    "row 173 when **VIII.2 Bridge and Row 68 → Row 54 meta must read on the same wire before row 174 export meta prelude capstone opens on the full capstone path**"
)


def update_row173_tail(preface: str) -> str:
    start = preface.index(ROW173_TAIL_MARKER)
    end = preface.index(ROW173_TAIL_END)
    block = preface[start:end]
    new_block = block.replace(
        "when opening [row 154](preface.md#skill-navigation-row-154) before row 54 closes on the full capstone path",
        "when opening [row 174](preface.md#skill-navigation-row-174) before row 54 closes on the full capstone path",
    )
    new_block = new_block.replace(
        "When row 173 is complete, proceed to [row 154](preface.md#skill-navigation-row-154) when NPT converges but the pedigree checklist still feels disconnected from verified dynamics meta prelude capstone on the full capstone path, to [row 134](preface.md#skill-navigation-row-134) when NPT converges but the pedigree checklist still feels disconnected from verified dynamics meta prelude capstone on the opening-hinge capstone path alone, to [row 153](preface.md#skill-navigation-row-153) when NVT/NPT still feels like thermostat homework after verified atomistic meta prelude capstone on the opening-hinge capstone path alone, to [row 133](preface.md#skill-navigation-row-133) for the Row 68 ↔ Row 53 dynamics meta audit on the opening-hinge prelude path alone, to [row 112](preface.md#skill-navigation-row-112) for the Row 68 ↔ Row 52 atomistic meta audit on the opening-hinge prelude path alone, to [row 152](preface.md#skill-navigation-row-152) when atomistic meta prelude capstone still lags after verified homogenization meta prelude capstone on the full capstone path, to [row 132](preface.md#skill-navigation-row-132) when atomistic meta prelude capstone still lags after verified homogenization meta prelude capstone on the opening-hinge capstone path alone, to [row 53](preface.md#skill-navigation-row-53) when only VIII.1 → VIII.2 stalls, to [row 93](preface.md#skill-navigation-row-93) for the Row 68 ↔ Row 53 dynamics opening prelude audit alone, or extend prose only under `writings/` then sync.",
        "When row 173 is complete, proceed to [row 174](preface.md#skill-navigation-row-174) when NPT converges but the pedigree checklist still feels disconnected from verified dynamics meta prelude capstone on the full capstone path, to [row 154](preface.md#skill-navigation-row-154) when NPT converges but the pedigree checklist still feels disconnected from verified dynamics meta prelude capstone on the opening-hinge capstone path alone, to [row 153](preface.md#skill-navigation-row-153) when NVT/NPT still feels like thermostat homework after verified atomistic meta prelude capstone on the opening-hinge capstone path alone, to [row 133](preface.md#skill-navigation-row-133) for the Row 68 ↔ Row 53 dynamics meta audit on the opening-hinge prelude path alone, to [row 112](preface.md#skill-navigation-row-112) for the Row 68 ↔ Row 52 atomistic meta audit on the opening-hinge prelude path alone, to [row 152](preface.md#skill-navigation-row-152) when atomistic meta prelude capstone still lags after verified homogenization meta prelude capstone on the full capstone path, to [row 132](preface.md#skill-navigation-row-132) when atomistic meta prelude capstone still lags after verified homogenization meta prelude capstone on the opening-hinge capstone path alone, to [row 53](preface.md#skill-navigation-row-53) when only VIII.1 → VIII.2 stalls, to [row 93](preface.md#skill-navigation-row-93) for the Row 68 ↔ Row 53 dynamics opening prelude audit alone, or extend prose only under `writings/` then sync.",
    )
    return preface[:start] + new_block + preface[end:]


def main():
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "skill-navigation-row-174" in preface:
        print("preface: row 174 already present")
    else:
        if "skill-navigation-row-173" in preface:
            preface = update_row173_tail(preface)
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + ROW174_PREFACE + copper)
        preface_path.write_text(preface)
        print("preface: added row 174")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-174" not in prologue:
        needle = "| Row 68 → Row 153 Row 68 → Row 53 dynamics meta prelude capstone reunion (row 173) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 173 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + PROLOGUE_COMPASS + prologue[line_end + 1 :]
        prologue = prologue.replace(
            "**Row 173 closing stitch",
            PROLOGUE_STITCH + "**Row 173 closing stitch",
        )
        prologue = prologue.replace(
            '| <span id="prologue-preview-row-173"></span>Row 173 preview',
            PROLOGUE_PREVIEW + '| <span id="prologue-preview-row-173"></span>Row 173 preview',
        )
        prologue_path.write_text(prologue)
        print("prologue: added row 174")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "row-174-closing-loop" not in epilogue:
        marker = (
            "Proceed to [row 154](#row-154-closing-loop) when row 68 closed but export meta prelude capstone still lags after row 173 on the full capstone path, to [row 114](#row-114-closing-loop) for the Row 68 ↔ Row 54 export meta audit on the opening-hinge prelude path alone, to [row 133](#row-113-closing-loop) for the Row 68 ↔ Row 53 dynamics meta audit on the opening-hinge prelude path alone, to [row 153](#row-133-closing-loop) when NVT/NPT still stalls after verified atomistic meta prelude capstone on the opening-hinge capstone path alone, to [row 152](#row-152-closing-loop) when atomistic meta prelude capstone still lags after verified homogenization meta prelude capstone on the full capstone path, to [row 53](#row-53-closing-loop) when only VIII.1 → VIII.2 stalls, or extend prose only under `writings/` then sync.\n\n\n### Row 131 closing loop"
        )
        replacement = (
            "Proceed to [row 174](#row-174-closing-loop) when row 68 closed but export meta prelude capstone still lags after row 173 on the full capstone path, to [row 154](#row-154-closing-loop) when export meta prelude capstone still lags after verified dynamics meta prelude capstone on the opening-hinge capstone path alone, to [row 114](#row-114-closing-loop) for the Row 68 ↔ Row 54 export meta audit on the opening-hinge prelude path alone, to [row 133](#row-133-closing-loop) for the Row 68 ↔ Row 53 dynamics meta audit on the opening-hinge prelude path alone, to [row 153](#row-153-closing-loop) when NVT/NPT still stalls after verified atomistic meta prelude capstone on the opening-hinge capstone path alone, to [row 152](#row-152-closing-loop) when atomistic meta prelude capstone still lags after verified homogenization meta prelude capstone on the full capstone path, to [row 53](#row-53-closing-loop) when only VIII.1 → VIII.2 stalls, or extend prose only under `writings/` then sync.\n\n\n"
            + EPILOGUE_LOOP
            + "\n\n\n### Row 131 closing loop"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 173 end marker not found")
        epilogue = epilogue.replace(marker, replacement, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 174")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row154-export-meta-prelude-capstone-reunion-index-row-174" not in sources:
        sources = sources.replace(
            "| 154 | Row 68 → Row 134 Row 68 → Row 54 export meta prelude capstone",
            SOURCES_TABLE + "| 154 | Row 68 → Row 134 Row 68 → Row 54 export meta prelude capstone",
        )
        sources = sources.replace(
            "## Row 68 → Row 134 Row 68 → Row 54 export meta prelude capstone reunion index (row 154)",
            SOURCES_INDEX + "## Row 68 → Row 134 Row 68 → Row 54 export meta prelude capstone reunion index (row 154)",
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 174")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-174-baby-picture-row68-row154" not in memory:
        memory = memory.replace(
            "| 173 | Meta | [Row 68 → Row 153 dynamics meta prelude capstone reunion index]",
            MEMORY_TABLE + "| 173 | Meta | [Row 68 → Row 153 dynamics meta prelude capstone reunion index]",
        )
        memory = memory.replace(
            "### Row 154 baby picture (Row 68 → Row 134 Row 68 → Row 54 export meta prelude capstone reunion) {#row-154-baby-picture-row68-row134-export-meta-prelude-capstone-reunion}",
            MEMORY_BABY + "### Row 154 baby picture (Row 68 → Row 134 Row 68 → Row 54 export meta prelude capstone reunion) {#row-154-baby-picture-row68-row134-export-meta-prelude-capstone-reunion}",
            1,
        )
        if ROW173_BABY_OLD in memory:
            memory = memory.replace(ROW173_BABY_OLD, ROW173_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 174")


if __name__ == "__main__":
    main()
