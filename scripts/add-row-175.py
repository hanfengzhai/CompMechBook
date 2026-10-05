#!/usr/bin/env python3
"""Add row 175 meta-stitch (Row 68 → Row 155 ↔ Row 55 electronic audit meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def t155_to_175(text: str) -> str:
    """Transform row-155 capstone-path meta copy to row 175 (155→175, 135→155 inner, 174 gate)."""
    repl = [
        ("Row 68 → Row 135 Row 68 → Row 55", "Row 68 → Row 155 Row 68 → Row 55"),
        (
            "row68-row135-electronic-audit-meta-prelude-capstone-reunion-index-row-155",
            "TEMP_ROW175_EXP_INDEX",
        ),
        (
            "row-155-baby-picture-row68-row135-electronic-audit-meta-prelude-capstone-reunion",
            "row-175-baby-picture-row68-row155-electronic-audit-meta-prelude-capstone-reunion",
        ),
        ("skill-navigation-row-155", "TEMP_SKILL_NAV_155"),
        ("prologue-preview-row-155", "prologue-preview-row-175"),
        ("row-155-closing-stitch", "row-175-closing-stitch"),
        ("row-155-closing-loop", "row-175-closing-loop"),
        ("Row 155 three-way audit", "Row 175 three-way audit"),
        (
            "[row 154](preface.md#skill-navigation-row-154) or [row 135](TEMP_SKILL_NAV_155)",
            "[row 174](preface.md#skill-navigation-row-174) or [row 155](TEMP_SKILL_NAV_155)",
        ),
        (
            "[row 154](preface.md#skill-navigation-row-154) or [Row 68 → Row 115 electronic audit meta prelude capstone reunion index (row 135)](appendix/sources.md#row68-row115-electronic-audit-meta-prelude-capstone-reunion-index-row-135)",
            "[row 174](preface.md#skill-navigation-row-174) or [Row 68 → Row 155 electronic audit meta prelude capstone reunion index (row 175)](appendix/sources.md#row68-row155-electronic-audit-meta-prelude-capstone-reunion-index-row-175)",
        ),
        (
            "[row 154](preface.md#skill-navigation-row-154) or [Row 68 → Row 135 electronic audit meta prelude capstone reunion index (row 155)](appendix/sources.md#row68-row135-electronic-audit-meta-prelude-capstone-reunion-index-row-155)",
            "[row 174](preface.md#skill-navigation-row-174) or [Row 68 → Row 155 electronic audit meta prelude capstone reunion index (row 175)](appendix/sources.md#row68-row155-electronic-audit-meta-prelude-capstone-reunion-index-row-175)",
        ),
        (
            "verified export meta prelude capstone closure (row 154)",
            "verified export meta prelude capstone closure (row 174)",
        ),
        (
            "before row 156 Born–Oppenheimer meta prelude capstone reunion opens on the full capstone path",
            "before row 176 Born–Oppenheimer meta prelude capstone reunion opens on the full capstone path",
        ),
        (
            "before row 157 Kohn–Sham meta prelude capstone reunion opens on the full capstone path",
            "before row 177 Kohn–Sham meta prelude capstone reunion opens on the full capstone path",
        ),
    ]
    out = text
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW175_EXP_INDEX",
        "row68-row155-electronic-audit-meta-prelude-capstone-reunion-index-row-175",
    )
    out = out.replace("TEMP_SKILL_NAV_155", "skill-navigation-row-155")
    out = out.replace("row 155", "row 175")
    out = out.replace("Row 155", "Row 175")
    out = out.replace("skill-navigation-row-155", "skill-navigation-row-175")
    out = out.replace("[row 175](preface.md#skill-navigation-row-174)", "[row 174](preface.md#skill-navigation-row-174)")
    out = out.replace("[row 175](preface.md#skill-navigation-row-175)", "[row 175](preface.md#skill-navigation-row-175)")
    out = out.replace("[row 175](preface.md#skill-navigation-row-155)", "[row 155](preface.md#skill-navigation-row-155)")
    out = out.replace("[row 155](preface.md#skill-navigation-row-175)", "[row 155](preface.md#skill-navigation-row-155)")
    out = out.replace("when row 154 closed but row 55", "when row 174 closed but row 55")
    out = out.replace("[preface row 155](../preface.md#skill-navigation-row-175)", "[preface row 155](../preface.md#skill-navigation-row-155)")
    out = out.replace("row 1555", "row 176")
    out = out.replace("row 1556", "row 177")
    out = out.replace("row 175 or row 175", "row 174 or row 155")
    out = out.replace("When row 175 closed", "When row 174 closed")
    out = out.replace("after row 175 alone", "after row 174 alone")
    out = out.replace("Recite [preface row 175]", "Recite [preface row 174]")
    out = out.replace("row 175 or row 155 recited", "row 174 or row 155 recited")
    out = out.replace("When row 175 closed — electronic", "When row 174 closed — electronic")
    out = out.replace("When row 154 closed — electronic", "When row 174 closed — electronic")
    out = out.replace("row 154 or row 135 recited", "row 174 or row 155 recited")
    out = out.replace("row 154 or row 55 recited", "row 174 or row 55 recited")
    out = out.replace("when row 154 closed electronic", "when row 174 closed electronic")
    out = out.replace("(preface.md#skill-navigation-row-135)", "(preface.md#skill-navigation-row-155)")
    out = out.replace(
        "Row 68 → Row 175 electronic audit meta prelude capstone reunion index",
        "Row 68 → Row 155 electronic audit meta prelude capstone reunion index",
    )
    out = out.replace("row 153 or row 54 recited", "row 173 or row 154 recited")
    out = out.replace("row 135", "row 155")
    out = out.replace("Row 135", "Row 155")
    out = out.replace("row 115", "row 135")
    out = out.replace("Row 115", "Row 135")
    out = out.replace(
        "row68-row115-electronic-audit-meta-prelude-capstone-reunion-index-row-135",
        "row68-row135-electronic-audit-meta-prelude-capstone-reunion-index-row-155",
    )
    out = out.replace(
        "row68-row134-export-meta-prelude-capstone-reunion-index-row-154",
        "row68-row154-export-meta-prelude-capstone-reunion-index-row-174",
    )
    out = out.replace("Row 68 → Row 175 Row 68 → Row 55", "Row 68 → Row 155 Row 68 → Row 55")
    out = out.replace(
        "[preface row 155](../preface.md#skill-navigation-row-135)",
        "[preface row 155](../preface.md#skill-navigation-row-155)",
    )
    out = out.replace(
        "Confirm [row 154](preface.md#skill-navigation-row-154) or [Row 68 → Row 155",
        "Confirm [row 174](preface.md#skill-navigation-row-174) or [Row 68 → Row 155",
    )
    out = out.replace(
        "and [row 154](preface.md#skill-navigation-row-154) or [row 155]",
        "and [row 174](preface.md#skill-navigation-row-174) or [row 155]",
    )
    out = out.replace("[row 135](preface.md#skill-navigation-row-115)", "[row 135](preface.md#skill-navigation-row-135)")
    out = out.replace("(preface.md#skill-navigation-row-175) when the pedigree", "(preface.md#skill-navigation-row-155) when the pedigree")
    out = out.replace("when row 154 and row 55", "when row 174 and row 55")
    out = out.replace("after row 154 alone", "after row 174 alone")
    out = out.replace("Scene after row 154.", "Scene after row 174.")
    out = out.replace("from row 175's", "from row 174's")
    out = out.replace("row 154's yaml pedigree", "row 174's yaml pedigree")
    out = out.replace("row 154 tells you", "row 174 tells you")
    out = out.replace(
        "VIII.3 Bridge to Part IX",
        "VIII.3 Bridge → opening hinge → IX.0 SCF audit",
    )
    out = out.replace("row 154", "row 174")
    out = out.replace("Row 154", "Row 174")
    out = out.replace("[row 174](preface.md#skill-navigation-row-174)", "[row 174](preface.md#skill-navigation-row-174)")
    out = out.replace("[row 174](preface.md#skill-navigation-row-155)", "[row 155](preface.md#skill-navigation-row-155)")
    return out



def extract_preface_row155(preface: str) -> str:
    start = preface.index("### Row 155 skill checkpoint")
    end = preface.index("\n\n### Row 156 skill checkpoint")
    return preface[start:end]


ROW175_PREFACE = t155_to_175(extract_preface_row155((ROOT / "writings/preface/chapters/preface.md").read_text())) + "\n\n"

PROLOGUE_COMPASS = (
    "| Row 68 → Row 155 Row 68 → Row 55 electronic audit meta prelude capstone reunion (row 175) | [Preface: row 175 skill checkpoint](../preface.md#skill-navigation-row-175) · [Row 68 → Row 155 electronic audit meta prelude capstone reunion index](../appendix/sources.md#row68-row155-electronic-audit-meta-prelude-capstone-reunion-index-row-175) · [memory sheet row 175 baby picture](../appendix/memory-sheet.md#row-175-baby-picture-row68-row155-electronic-audit-meta-prelude-capstone-reunion) · [prologue row 175 preview row](#prologue-preview-row-175); [prologue row 175 closing stitch](#row-175-closing-stitch); [epilogue row 175 closing loop](../epilogue/multiscale.md#row-175-closing-loop) — read row 68 gate + row 174 or row 155 export meta prelude capstone / electronic audit meta prelude gate + VIII.3 Bridge → opening hinge → IX.0 SCF audit + row 55 meta aloud when pedigree checklist is clean on the full capstone path but Part IX still feels like standalone DFT coursework after verified export meta prelude capstone |"
)

_prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
_row155_stitch_body = (
    _prologue.split("**Row 155 closing stitch")[1].split("**Row 156 closing stitch")[0].lstrip().split("\n\n")[0]
)
PROLOGUE_STITCH = t155_to_175(
    "**Row 155 closing stitch (Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone reunion).** {#row-155-closing-stitch} "
    + _row155_stitch_body.split(".** {#row-155-closing-stitch} ", 1)[-1]
) + "\n\n"

PROLOGUE_PREVIEW = (
    "| <span id=\"prologue-preview-row-175\"></span>Row 175 preview (Row 68 → Row 155 Row 68 → Row 55 electronic audit meta prelude capstone reunion) | Explain why midpoint closure (row 68) and VIII.3 → IX.0 meta (row 55) must be read together with the Bridge → SCF audit chain after verified export meta prelude capstone before pedigree checklist and Part IX feel like separate courses on the full capstone path | One sentence: \"read row 68 gate + row 174 or row 155 export meta prelude capstone / electronic audit meta prelude gate + VIII.3 Bridge → opening hinge → IX.0 SCF audit + row 55 meta aloud when pedigree checklist is clean on the full capstone path but Part IX still feels like standalone DFT coursework after verified export meta prelude capstone\" — [preface row 175 skill checkpoint](../preface.md#skill-navigation-row-175); [prologue row 175 closing stitch](#row-175-closing-stitch); [Row 68 → Row 155 reunion index](../appendix/sources.md#row68-row155-electronic-audit-meta-prelude-capstone-reunion-index-row-175); [memory sheet row 175 baby picture](../appendix/memory-sheet.md#row-175-baby-picture-row68-row155-electronic-audit-meta-prelude-capstone-reunion); [VIII.3 Bridge → opening hinge → IX.0 SCF audit](../part08-md/03-ab-initio-and-coarse-graining.md#bridge-to-part-ix); [IX.0 opening hinge from VIII.3](../part09-dft/00-opening.md#opening-hinge-viii3-to-ix); [preface row 55 skill checkpoint](../preface.md#skill-navigation-row-55); [preface row 174 skill checkpoint](../preface.md#skill-navigation-row-154); [epilogue row 175 closing loop](../epilogue/multiscale.md#row-175-closing-loop) |"
)

_epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
EPILOGUE_LOOP = t155_to_175(
    "### Row 155 closing loop"
    + _epilogue.split("### Row 155 closing loop")[1].split("### Row 156 closing loop")[0]
)

SOURCES_TABLE = (
    "| 175 | Row 68 → Row 155 Row 68 → Row 55 electronic audit meta prelude capstone (midpoint prelude gate ↔ export meta prelude capstone on full capstone path ↔ row 55 meta) | [Row 68 → Row 155 electronic audit meta prelude capstone reunion index](#row68-row155-electronic-audit-meta-prelude-capstone-reunion-index-row-175) · [preface row 175](../preface.md#skill-navigation-row-175) · [prologue row 175 preview](../prologue/00-many-scales.md#prologue-preview-row-175) · [prologue row 175 closing stitch](../prologue/00-many-scales.md#row-175-closing-stitch) · [epilogue row 175 closing loop](../epilogue/multiscale.md#row-175-closing-loop) · [memory sheet row 175 baby picture](memory-sheet.md#row-175-baby-picture-row68-row155-electronic-audit-meta-prelude-capstone-reunion) | Row 68 closed but **row 55 VIII.3 → IX.0 opening hinge still feels disconnected from verified export meta prelude capstone on the full capstone path** — read row 68 + row 174 or row 155 gate + VIII.3 Bridge → opening hinge → IX.0 SCF audit + row 55; [preface row 55](../preface.md#skill-navigation-row-55) |"
)

SOURCES_INDEX = t155_to_175(
    (ROOT / "writings/appendix/chapters/sources.md")
    .read_text()
    .split("## Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 155)")[1]
    .split("## Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 155)")[0]
)
SOURCES_INDEX = (
    "## Row 68 → Row 155 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 175)"
    + SOURCES_INDEX
)

MEMORY_TABLE = (
    "| 175 | Meta | [Row 68 → Row 155 electronic audit meta prelude capstone reunion index](sources.md#row68-row155-electronic-audit-meta-prelude-capstone-reunion-index-row-175) · [preface row 175 skill checkpoint](../preface.md#skill-navigation-row-175) · [prologue row 175 preview](../prologue/00-many-scales.md#prologue-preview-row-175) · [prologue row 175 closing stitch](../prologue/00-many-scales.md#row-175-closing-stitch) · [epilogue row 175 closing loop](../epilogue/multiscale.md#row-175-closing-loop) | Row 68 closed but row 55 VIII.3 → IX.0 opening hinge feels disconnected from verified export meta prelude capstone on the full capstone path — read row 68 + row 174 or row 155 gate + VIII.3 Bridge → opening hinge → IX.0 SCF audit + row 55; [row 175 baby picture](#row-175-baby-picture-row68-row155-electronic-audit-meta-prelude-capstone-reunion) |"
)

MEMORY_BABY = t155_to_175(
    (ROOT / "writings/appendix/chapters/memory-sheet.md")
    .read_text()
    .split("### Row 155 baby picture (Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone reunion)")[1]
    .split("### Row 156 baby picture")[0]
)
MEMORY_BABY = (
    "### Row 175 baby picture (Row 68 → Row 155 Row 68 → Row 55 electronic audit meta prelude capstone reunion)"
    + MEMORY_BABY.split(")", 1)[1]
    if ")" in MEMORY_BABY
    else "### Row 175 baby picture" + MEMORY_BABY
)

ROW174_TAIL_MARKER = "**When to pause.** Read the [prologue row 174 closing stitch]"
ROW174_TAIL_END = "or extend prose only under `writings/` then sync.\n\n\n\n## The copper wire through the book"

ROW174_BABY_OLD = (
    "row 174 when **VIII.2 Bridge and Row 68 → Row 54 meta must read on the same wire before row 155 electronic audit meta prelude capstone opens on the full capstone path**"
)
ROW174_BABY_NEW = (
    "row 174 when **VIII.3 Bridge and Row 68 → Row 55 meta must read on the same wire before row 175 electronic audit meta prelude capstone opens on the full capstone path**"
)


def update_row173_tail_fix(preface: str) -> str:
    old = "When row 173 is complete, proceed to [row 154](preface.md#skill-navigation-row-154) when NPT converges"
    new = "When row 173 is complete, proceed to [row 174](preface.md#skill-navigation-row-174) when NPT converges"
    if old in preface:
        preface = preface.replace(old, new, 1)
    return preface


def update_row174_tail(preface: str) -> str:
    start = preface.index(ROW174_TAIL_MARKER)
    end = preface.index(ROW174_TAIL_END)
    block = preface[start:end]
    new_block = block.replace(
        "when opening [row 175](preface.md#skill-navigation-row-175) before row 55 closes on the full capstone path",
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
    if "skill-navigation-row-175" in preface:
        print("preface: row 175 already present")
    else:
        if "skill-navigation-row-174" in preface:
            preface = update_row173_tail_fix(preface)
            preface = update_row174_tail(preface)
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + ROW175_PREFACE + copper)
        preface_path.write_text(preface)
        print("preface: added row 175")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-175" not in prologue:
        needle = "| Row 68 → Row 154 Row 68 → Row 54 export meta prelude capstone reunion (row 174) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 174 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + PROLOGUE_COMPASS + prologue[line_end + 1 :]
        prologue = prologue.replace(
            "**Row 174 closing stitch",
            PROLOGUE_STITCH + "**Row 174 closing stitch",
        )
        prologue = prologue.replace(
            '| <span id="prologue-preview-row-174"></span>Row 174 preview',
            PROLOGUE_PREVIEW + '| <span id="prologue-preview-row-174"></span>Row 174 preview',
        )
        prologue_path.write_text(prologue)
        print("prologue: added row 175")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "row-175-closing-loop" not in epilogue:
        marker = (
            "Proceed to [row 155](#row-155-closing-loop) when row 68 closed but electronic audit meta prelude capstone still lags after row 174 on the full capstone path, to [row 135](#row-135-closing-loop) when row 68 closed but electronic audit meta prelude capstone still lags after row 154 on the opening-hinge capstone path alone, to [row 115](#row-115-closing-loop) for the Row 68 ↔ Row 55 electronic audit meta audit on the opening-hinge prelude path alone, to [row 134](#row-134-closing-loop) for the Row 68 ↔ Row 54 export meta audit on the opening-hinge prelude path alone, to [row 153](#row-153-closing-loop) when NVT/NPT still stalls after verified atomistic meta prelude capstone on the opening-hinge capstone path alone, to [row 54](#row-54-closing-loop) when only VIII.2 → VIII.3 stalls, or extend prose only under `writings/` then sync.\n\n\n\n\n\n"
        )
        replacement = (
            "Proceed to [row 175](#row-175-closing-loop) when row 68 closed but electronic audit meta prelude capstone still lags after row 174 on the full capstone path, to [row 155](#row-155-closing-loop) when electronic audit meta prelude capstone still lags after verified export meta prelude capstone on the opening-hinge capstone path alone, to [row 115](#row-115-closing-loop) for the Row 68 ↔ Row 55 electronic audit meta audit on the opening-hinge prelude path alone, to [row 134](#row-134-closing-loop) for the Row 68 ↔ Row 54 export meta audit on the opening-hinge prelude path alone, to [row 153](#row-153-closing-loop) when NVT/NPT still stalls after verified atomistic meta prelude capstone on the opening-hinge capstone path alone, to [row 55](#row-55-closing-loop) when only VIII.3 → IX.0 stalls, or extend prose only under `writings/` then sync.\n\n\n"
            + EPILOGUE_LOOP
            + "\n\n\n\n\n"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 174 end marker not found")
        epilogue = epilogue.replace(marker, replacement, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 175")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row155-electronic-audit-meta-prelude-capstone-reunion-index-row-175" not in sources:
        sources = sources.replace(
            "| 155 | Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone",
            SOURCES_TABLE + "| 155 | Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone",
        )
        sources = sources.replace(
            "## Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 155)",
            SOURCES_INDEX + "## Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 155)",
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 175")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-175-baby-picture-row68-row155" not in memory:
        memory = memory.replace(
            "| 174 | Meta | [Row 68 → Row 154 export meta prelude capstone reunion index]",
            MEMORY_TABLE + "| 174 | Meta | [Row 68 → Row 154 export meta prelude capstone reunion index]",
        )
        memory = memory.replace(
            "### Row 155 baby picture (Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone reunion) {#row-155-baby-picture-row68-row135-electronic-audit-meta-prelude-capstone-reunion}",
            MEMORY_BABY + "### Row 155 baby picture (Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone reunion) {#row-155-baby-picture-row68-row135-electronic-audit-meta-prelude-capstone-reunion}",
            1,
        )
        if ROW174_BABY_OLD in memory:
            memory = memory.replace(ROW174_BABY_OLD, ROW174_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 175")


if __name__ == "__main__":
    main()
