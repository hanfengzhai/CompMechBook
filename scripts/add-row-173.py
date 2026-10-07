#!/usr/bin/env python3
"""Add row 173 meta-stitch (Row 68 → Row 153 ↔ Row 53 dynamics meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def t153_to_173(text: str) -> str:
    """Transform row-153 capstone-path meta copy to row 173 (153→173, 133→153 inner, 172 gate)."""
    repl = [
        ("Row 68 → Row 133 Row 68 → Row 53", "Row 68 → Row 153 Row 68 → Row 53"),
        (
            "row68-row133-dynamics-meta-prelude-capstone-reunion-index-row-153",
            "TEMP_ROW173_DYN_INDEX",
        ),
        (
            "row-153-baby-picture-row68-row133-dynamics-meta-prelude-capstone-reunion",
            "row-173-baby-picture-row68-row153-dynamics-meta-prelude-capstone-reunion",
        ),
        (
            "skill-navigation-row-153",
            "TEMP_SKILL_NAV_153",
        ),
        ("prologue-preview-row-153", "prologue-preview-row-173"),
        ("row-153-closing-stitch", "row-173-closing-stitch"),
        ("row-153-closing-loop", "row-173-closing-loop"),
        ("Row 153 three-way audit", "Row 173 three-way audit"),
        (
            "[row 152](preface.md#skill-navigation-row-152) or [row 133](TEMP_SKILL_NAV_153)",
            "[row 172](preface.md#skill-navigation-row-172) or [row 153](TEMP_SKILL_NAV_153)",
        ),
        (
            "[row 152](preface.md#skill-navigation-row-152) or [Row 68 → Row 133 dynamics meta prelude capstone reunion index (row 153)](appendix/sources.md#row68-row133-dynamics-meta-prelude-capstone-reunion-index-row-153)",
            "[row 172](preface.md#skill-navigation-row-172) or [Row 68 → Row 153 dynamics meta prelude capstone reunion index (row 173)](appendix/sources.md#row68-row153-dynamics-meta-prelude-capstone-reunion-index-row-173)",
        ),
        (
            "verified atomistic meta prelude capstone closure (row 152)",
            "verified atomistic meta prelude capstone closure (row 172)",
        ),
        (
            "before row 154 export meta prelude capstone reunion opens on the full capstone path",
            "before row 174 export meta prelude capstone reunion opens on the full capstone path",
        ),
        (
            "before row 155 export meta prelude opens on the full capstone path",
            "before row 175 export meta prelude opens on the full capstone path",
        ),
    ]
    out = text
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW173_DYN_INDEX",
        "row68-row153-dynamics-meta-prelude-capstone-reunion-index-row-173",
    )
    out = out.replace("TEMP_SKILL_NAV_153", "skill-navigation-row-153")
    out = out.replace("row 153", "row 173")
    out = out.replace("Row 153", "Row 173")
    out = out.replace("skill-navigation-row-153", "skill-navigation-row-173")
    out = out.replace("[row 173](preface.md#skill-navigation-row-172)", "[row 172](preface.md#skill-navigation-row-172)")
    out = out.replace("[row 173](preface.md#skill-navigation-row-173)", "[row 173](preface.md#skill-navigation-row-173)")
    out = out.replace("[row 173](preface.md#skill-navigation-row-153)", "[row 153](preface.md#skill-navigation-row-153)")
    out = out.replace("[row 153](preface.md#skill-navigation-row-173)", "[row 153](preface.md#skill-navigation-row-153)")
    out = out.replace("when row 152 closed but row 53", "when row 172 closed but row 53")
    out = out.replace("[preface row 153](../preface.md#skill-navigation-row-173)", "[preface row 153](../preface.md#skill-navigation-row-153)")
    out = out.replace("row 1535", "row 174")
    out = out.replace("row 1536", "row 175")
    out = out.replace("row 173 or row 173", "row 172 or row 153")
    out = out.replace("When row 173 closed", "When row 172 closed")
    out = out.replace("after row 173 alone", "after row 172 alone")
    out = out.replace("Recite [preface row 173]", "Recite [preface row 172]")
    out = out.replace("row 173 or row 153 recited", "row 172 or row 153 recited")
    out = out.replace("When row 173 closed — atomistic", "When row 172 closed — atomistic")
    out = out.replace("When row 152 closed — atomistic", "When row 172 closed — atomistic")
    out = out.replace("row 152 or row 133 recited", "row 172 or row 153 recited")
    out = out.replace("row 151 or row 52 recited", "row 171 or row 152 recited")
    out = out.replace("row 133", "row 153")
    out = out.replace("Row 133", "Row 153")
    out = out.replace("row 113", "row 133")
    out = out.replace("Row 113", "Row 133")
    out = out.replace(
        "row68-row113-dynamics-meta-prelude-capstone-reunion-index-row-133",
        "row68-row133-dynamics-meta-prelude-capstone-reunion-index-row-153",
    )
    out = out.replace(
        "row68-row132-atomistic-meta-prelude-capstone-reunion-index-row-152",
        "row68-row152-atomistic-meta-prelude-capstone-reunion-index-row-172",
    )
    out = out.replace("Row 68 → Row 173 Row 68 → Row 53", "Row 68 → Row 153 Row 68 → Row 53")
    out = out.replace(
        "[preface row 153](../preface.md#skill-navigation-row-133)",
        "[preface row 153](../preface.md#skill-navigation-row-153)",
    )
    out = out.replace(
        "Confirm [row 152](preface.md#skill-navigation-row-152) or [Row 68 → Row 153",
        "Confirm [row 172](preface.md#skill-navigation-row-172) or [Row 68 → Row 153",
    )
    out = out.replace(
        "and [row 152](preface.md#skill-navigation-row-152) or [row 153]",
        "and [row 172](preface.md#skill-navigation-row-172) or [row 153]",
    )
    out = out.replace("[row 133](preface.md#skill-navigation-row-113)", "[row 133](preface.md#skill-navigation-row-133)")
    out = out.replace("(preface.md#skill-navigation-row-173) when NVT", "(preface.md#skill-navigation-row-153) when NVT")
    out = out.replace("when row 152 and row 53", "when row 172 and row 53")
    out = out.replace("after row 152 alone", "after row 172 alone")
    out = out.replace("Scene after row 152.", "Scene after row 172.")
    out = out.replace("from row 173's", "from row 172's")
    out = out.replace("row 152's static potential", "row 172's static potential")
    out = out.replace("row 152 tells you", "row 172 tells you")
    out = out.replace("VII.3 Bridge → VIII.1 phase space", "VIII.1 Bridge → opening hinge → VIII.2 ensembles")
    return out


def extract_preface_row153(preface: str) -> str:
    start = preface.index("### Row 153 skill checkpoint")
    end = preface.index("\n\n### Row 154 skill checkpoint")
    return preface[start:end]


ROW173_PREFACE = t153_to_173(extract_preface_row153((ROOT / "writings/preface/chapters/preface.md").read_text())) + "\n\n"

PROLOGUE_COMPASS = (
    "| Row 68 → Row 153 Row 68 → Row 53 dynamics meta prelude capstone reunion (row 173) | "
    "[Preface: row 173 skill checkpoint](../preface.md#skill-navigation-row-173) · "
    "[Row 68 → Row 153 dynamics meta prelude capstone reunion index](../appendix/sources.md#row68-row153-dynamics-meta-prelude-capstone-reunion-index-row-173) · "
    "[memory sheet row 173 baby picture](../appendix/memory-sheet.md#row-173-baby-picture-row68-row153-dynamics-meta-prelude-capstone-reunion) · "
    "[prologue row 173 preview row](#prologue-preview-row-173); [prologue row 173 closing stitch](#row-173-closing-stitch); "
    "[epilogue row 173 closing loop](../epilogue/multiscale.md#row-173-closing-loop) — "
    "read row 68 gate + row 172 or row 153 atomistic meta prelude capstone / dynamics meta prelude gate + VIII.1 Bridge → opening hinge → VIII.2 ensembles + row 53 meta aloud "
    "when EAM foundation is clean on the full capstone path but NVT/NPT feels like AtomModel homework after verified atomistic meta prelude capstone |\n"
)

_prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
_row153_stitch_body = (
    _prologue.split("**Row 153 closing stitch")[1].split("**Row 154 closing stitch")[0].lstrip().split("\n\n")[0]
)
PROLOGUE_STITCH = t153_to_173(
    "**Row 153 closing stitch (Row 68 → Row 133 Row 68 → Row 53 dynamics meta prelude capstone reunion).** {#row-153-closing-stitch} "
    + _row153_stitch_body.split(".** {#row-153-closing-stitch} ", 1)[-1]
) + "\n\n"

PROLOGUE_PREVIEW = (
    '| <span id="prologue-preview-row-173"></span>Row 173 preview (Row 68 → Row 153 Row 68 → Row 53 dynamics meta prelude capstone reunion) | '
    "Explain why midpoint closure (row 68) and VIII.1 → VIII.2 meta (row 53) must be read together with the Bridge → NPT chain after verified atomistic meta prelude capstone on the full capstone path before foundation manifest and thermostat sections feel like separate courses | "
    'One sentence: "read row 68 gate + row 172 or row 153 atomistic meta prelude capstone / dynamics meta prelude gate + VIII.1 Bridge → opening hinge → VIII.2 ensembles + row 53 meta aloud when EAM foundation is clean on the full capstone path but NVT/NPT feels like AtomModel homework after verified atomistic meta prelude capstone" — '
    "[preface row 173 skill checkpoint](../preface.md#skill-navigation-row-173); [prologue row 173 closing stitch](#row-173-closing-stitch); "
    "[Row 68 → Row 153 reunion index](../appendix/sources.md#row68-row153-dynamics-meta-prelude-capstone-reunion-index-row-173); "
    "[memory sheet row 173 baby picture](../appendix/memory-sheet.md#row-173-baby-picture-row68-row153-dynamics-meta-prelude-capstone-reunion); "
    "[VIII.1 Bridge](../part08-md/01-potentials-phase-space.md#bridge); "
    "[VIII.2 opening hinge from VIII.1](../part08-md/02-ensembles-integrators.md#opening-hinge-viii1-to-viii2); "
    "[preface row 53 skill checkpoint](../preface.md#skill-navigation-row-53); "
    "[preface row 172 skill checkpoint](../preface.md#skill-navigation-row-172); "
    "[epilogue row 173 closing loop](../epilogue/multiscale.md#row-173-closing-loop) |\n"
)

_epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
EPILOGUE_LOOP = t153_to_173(
    "### Row 153 closing loop"
    + _epilogue.split("### Row 153 closing loop")[1].split("### Row 154 closing loop")[0]
)

SOURCES_TABLE = (
    "| 173 | Row 68 → Row 153 Row 68 → Row 53 dynamics meta prelude capstone (midpoint prelude gate ↔ atomistic meta prelude capstone on full capstone path ↔ row 53 meta) | "
    "[Row 68 → Row 153 dynamics meta prelude capstone reunion index](#row68-row153-dynamics-meta-prelude-capstone-reunion-index-row-173) · "
    "[preface row 173](../preface.md#skill-navigation-row-173) · "
    "[prologue row 173 preview](../prologue/00-many-scales.md#prologue-preview-row-173) · "
    "[prologue row 173 closing stitch](../prologue/00-many-scales.md#row-173-closing-stitch) · "
    "[epilogue row 173 closing loop](../epilogue/multiscale.md#row-173-closing-loop) · "
    "[memory sheet row 173 baby picture](memory-sheet.md#row-173-baby-picture-row68-row153-dynamics-meta-prelude-capstone-reunion) | "
    "Row 68 closed but **row 53 VIII.1 → VIII.2 opening hinge still feels disconnected from verified atomistic meta prelude capstone on the full capstone path** — "
    "read row 68 + row 172 or row 153 gate + VIII.1 Bridge → opening hinge → VIII.2 ensembles + row 53; "
    "[preface row 53](../preface.md#skill-navigation-row-53) |\n"
)

SOURCES_INDEX = t153_to_173(
    (ROOT / "writings/appendix/chapters/sources.md")
    .read_text()
    .split("## Row 68 → Row 133 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 153)")[1]
    .split("## Row 68 → Row 134 Row 68 → Row 54 export meta prelude capstone reunion index (row 154)")[0]
)
SOURCES_INDEX = (
    "## Row 68 → Row 153 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 173)"
    + SOURCES_INDEX
)

MEMORY_TABLE = (
    "| 173 | Meta | [Row 68 → Row 153 dynamics meta prelude capstone reunion index](sources.md#row68-row153-dynamics-meta-prelude-capstone-reunion-index-row-173) · "
    "[preface row 173 skill checkpoint](../preface.md#skill-navigation-row-173) · "
    "[prologue row 173 preview](../prologue/00-many-scales.md#prologue-preview-row-173) · "
    "[prologue row 173 closing stitch](../prologue/00-many-scales.md#row-173-closing-stitch) · "
    "[epilogue row 173 closing loop](../epilogue/multiscale.md#row-173-closing-loop) | "
    "Row 68 closed but row 53 VIII.1 → VIII.2 opening hinge feels disconnected from verified atomistic meta prelude capstone on the full capstone path — "
    "read row 68 + row 172 or row 153 gate + VIII.1 Bridge → opening hinge → VIII.2 ensembles + row 53; "
    "[row 173 baby picture](#row-173-baby-picture-row68-row153-dynamics-meta-prelude-capstone-reunion) |\n"
)

MEMORY_BABY = t153_to_173(
    (ROOT / "writings/appendix/chapters/memory-sheet.md")
    .read_text()
    .split("### Row 153 baby picture (Row 68 → Row 133 Row 68 → Row 53 dynamics meta prelude capstone reunion)")[1]
    .split("### Row 154 baby picture")[0]
)
MEMORY_BABY = (
    "### Row 173 baby picture (Row 68 → Row 153 Row 68 → Row 53 dynamics meta prelude capstone reunion)"
    + MEMORY_BABY.split(")", 1)[1]
    if ")" in MEMORY_BABY
    else "### Row 173 baby picture" + MEMORY_BABY
)

ROW172_TAIL_MARKER = "**When to pause.** Read the [prologue row 172 closing stitch]"
ROW172_TAIL_END = "or extend prose only under `writings/` then sync.\n\n\n## The copper wire through the book"

ROW172_BABY_OLD = (
    "row 152 when **VIII.1 Bridge and Row 68 → Row 53 meta must read on the same wire before row 153 dynamics meta prelude capstone opens on the full capstone path**"
)
ROW172_BABY_NEW = (
    "row 172 when **VIII.1 Bridge and Row 68 → Row 53 meta must read on the same wire before row 173 dynamics meta prelude capstone opens on the full capstone path**"
)


def update_row172_tail(preface: str) -> str:
    start = preface.index(ROW172_TAIL_MARKER)
    end = preface.index(ROW172_TAIL_END)
    block = preface[start:end]
    new_block = block.replace(
        "when opening [row 153](preface.md#skill-navigation-row-153) before row 53 closes on the full capstone path",
        "when opening [row 173](preface.md#skill-navigation-row-173) before row 53 closes on the full capstone path",
    )
    new_block = new_block.replace(
        "When row 172 is complete, proceed to [row 153](preface.md#skill-navigation-row-153) when NVT/NPT still feels like thermostat homework after verified atomistic meta prelude capstone on the full capstone path, to [row 133](preface.md#skill-navigation-row-153) when NVT/NPT still feels like thermostat homework after verified atomistic meta prelude capstone on the opening-hinge capstone path alone, to [row 152](preface.md#skill-navigation-row-152) for the Row 68 ↔ Row 52 atomistic meta audit on the opening-hinge capstone path alone, to [row 132](preface.md#skill-navigation-row-132) for the Row 68 ↔ Row 52 atomistic meta audit on the opening-hinge prelude path alone, to [row 171](preface.md#skill-navigation-row-171) when homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the full capstone path, to [row 131](preface.md#skill-navigation-row-131) when homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the opening-hinge capstone path alone, to [row 52](preface.md#skill-navigation-row-52) when only VII.3 → VIII.1 stalls, to [row 92](preface.md#skill-navigation-row-92) for the Row 68 ↔ Row 52 atomistic opening prelude audit alone, or extend prose only under `writings/` then sync.",
        "When row 172 is complete, proceed to [row 173](preface.md#skill-navigation-row-173) when NVT/NPT still feels like thermostat homework after verified atomistic meta prelude capstone on the full capstone path, to [row 153](preface.md#skill-navigation-row-153) when NVT/NPT still feels like thermostat homework after verified atomistic meta prelude capstone on the opening-hinge capstone path alone, to [row 152](preface.md#skill-navigation-row-152) for the Row 68 ↔ Row 52 atomistic meta audit on the opening-hinge capstone path alone, to [row 132](preface.md#skill-navigation-row-132) for the Row 68 ↔ Row 52 atomistic meta audit on the opening-hinge prelude path alone, to [row 171](preface.md#skill-navigation-row-171) when homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the full capstone path, to [row 131](preface.md#skill-navigation-row-131) when homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the opening-hinge capstone path alone, to [row 52](preface.md#skill-navigation-row-52) when only VII.3 → VIII.1 stalls, to [row 92](preface.md#skill-navigation-row-92) for the Row 68 ↔ Row 52 atomistic opening prelude audit alone, or extend prose only under `writings/` then sync.",
    )
    return preface[:start] + new_block + preface[end:]


def main():
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "skill-navigation-row-173" in preface:
        print("preface: row 173 already present")
    else:
        if "skill-navigation-row-172" in preface:
            preface = update_row172_tail(preface)
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + ROW173_PREFACE + copper)
        preface_path.write_text(preface)
        print("preface: added row 173")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-173" not in prologue:
        needle = "| Row 68 → Row 152 Row 68 → Row 52 atomistic meta prelude capstone reunion (row 172) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 172 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + PROLOGUE_COMPASS + prologue[line_end + 1 :]
        prologue = prologue.replace(
            "**Row 172 closing stitch",
            PROLOGUE_STITCH + "**Row 172 closing stitch",
        )
        prologue = prologue.replace(
            '| <span id="prologue-preview-row-172"></span>Row 172 preview',
            PROLOGUE_PREVIEW + '| <span id="prologue-preview-row-172"></span>Row 172 preview',
        )
        prologue_path.write_text(prologue)
        print("prologue: added row 173")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "row-173-closing-loop" not in epilogue:
        marker = (
            "Proceed to [row 153](#row-153-closing-loop) when row 68 closed but dynamics meta prelude capstone still lags after row 172 on the full capstone path, to [row 152](#row-132-closing-loop) for the Row 68 ↔ Row 52 atomistic meta audit on the opening-hinge capstone path alone, to [row 113](#row-113-closing-loop) for the Row 68 ↔ Row 53 dynamics meta audit on the opening-hinge prelude path alone, to [row 132](#row-112-closing-loop) for the Row 68 ↔ Row 52 atomistic meta audit on the opening-hinge prelude path alone, to [row 151](#row-151-closing-loop) when homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the full capstone path, to [row 52](#row-52-closing-loop) when only VII.3 → VIII.1 stalls, or extend prose only under `writings/` then sync.\n\n\n\n\n\n\n\n\n\n\n### Row 129 closing loop"
        )
        replacement = (
            "Proceed to [row 173](#row-173-closing-loop) when row 68 closed but dynamics meta prelude capstone still lags after row 172 on the full capstone path, to [row 153](#row-153-closing-loop) when dynamics meta prelude capstone still lags after verified atomistic meta prelude capstone on the opening-hinge capstone path alone, to [row 152](#row-152-closing-loop) for the Row 68 ↔ Row 52 atomistic meta audit on the opening-hinge capstone path alone, to [row 133](#row-133-closing-loop) for the Row 68 ↔ Row 53 dynamics meta audit on the opening-hinge prelude path alone, to [row 132](#row-112-closing-loop) for the Row 68 ↔ Row 52 atomistic meta audit on the opening-hinge prelude path alone, to [row 171](#row-171-closing-loop) when homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the full capstone path, to [row 52](#row-52-closing-loop) when only VII.3 → VIII.1 stalls, or extend prose only under `writings/` then sync.\n\n\n\n\n\n\n\n\n\n\n"
            + EPILOGUE_LOOP
            + "\n\n\n\n\n\n\n\n\n\n\n### Row 129 closing loop"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 172 end marker not found")
        epilogue = epilogue.replace(marker, replacement, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 173")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row153-dynamics-meta-prelude-capstone-reunion-index-row-173" not in sources:
        sources = sources.replace(
            "| 153 | Row 68 → Row 133 Row 68 → Row 53 dynamics meta prelude capstone",
            SOURCES_TABLE + "| 153 | Row 68 → Row 133 Row 68 → Row 53 dynamics meta prelude capstone",
        )
        sources = sources.replace(
            "## Row 68 → Row 133 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 153)",
            SOURCES_INDEX + "## Row 68 → Row 133 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 153)",
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 173")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-173-baby-picture-row68-row153" not in memory:
        memory = memory.replace(
            "| 172 | Meta | [Row 68 → Row 152 atomistic meta prelude capstone reunion index]",
            MEMORY_TABLE + "| 172 | Meta | [Row 68 → Row 152 atomistic meta prelude capstone reunion index]",
        )
        memory = memory.replace(
            "### Row 153 baby picture (Row 68 → Row 133 Row 68 → Row 53 dynamics meta prelude capstone reunion) {#row-153-baby-picture-row68-row133-dynamics-meta-prelude-capstone-reunion}",
            MEMORY_BABY + "### Row 153 baby picture (Row 68 → Row 133 Row 68 → Row 53 dynamics meta prelude capstone reunion) {#row-153-baby-picture-row68-row133-dynamics-meta-prelude-capstone-reunion}",
            1,
        )
        if ROW172_BABY_OLD in memory:
            memory = memory.replace(ROW172_BABY_OLD, ROW172_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 173")


if __name__ == "__main__":
    main()
