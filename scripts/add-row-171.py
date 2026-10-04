#!/usr/bin/env python3
"""Add row 171 meta-stitch (Row 68 → Row 151 ↔ Row 51 homogenization meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def t151_to_171(text: str) -> str:
    """Transform row-151 capstone-path meta copy to row 171 (151→171, 131→151 inner, 170 gate)."""
    repl = [
        ("Row 68 → Row 131 Row 68 → Row 51", "Row 68 → Row 151 Row 68 → Row 51"),
        (
            "row68-row131-homogenization-meta-prelude-capstone-reunion-index-row-151",
            "TEMP_ROW171_HOMOG_INDEX",
        ),
        (
            "row-151-baby-picture-row68-row131-homogenization-meta-prelude-capstone-reunion",
            "row-171-baby-picture-row68-row151-homogenization-meta-prelude-capstone-reunion",
        ),
        ("skill-navigation-row-151", "skill-navigation-row-171"),
        ("prologue-preview-row-151", "prologue-preview-row-171"),
        ("row-151-closing-stitch", "row-171-closing-stitch"),
        ("row-151-closing-loop", "row-171-closing-loop"),
        ("Row 151 three-way audit", "Row 171 three-way audit"),
        (
            "[row 150](preface.md#skill-navigation-row-150) or [row 131](preface.md#skill-navigation-row-131)",
            "[row 170](preface.md#skill-navigation-row-170) or [row 151](preface.md#skill-navigation-row-151)",
        ),
        (
            "[row 150](preface.md#skill-navigation-row-150) or [Row 68 → Row 131 homogenization meta prelude capstone reunion index (row 151)](appendix/sources.md#row68-row131-homogenization-meta-prelude-capstone-reunion-index-row-151)",
            "[row 170](preface.md#skill-navigation-row-170) or [Row 68 → Row 151 homogenization meta prelude capstone reunion index (row 171)](appendix/sources.md#row68-row151-homogenization-meta-prelude-capstone-reunion-index-row-171)",
        ),
        (
            "verified DDD meta prelude capstone closure on the full capstone path (row 150)",
            "verified DDD meta prelude capstone closure on the full capstone path (row 170)",
        ),
        (
            "before row 152 atomistic meta prelude capstone reunion opens on the full capstone path",
            "before row 172 atomistic meta prelude capstone reunion opens on the full capstone path",
        ),
        (
            "before row 152 atomistic meta prelude opens on the full capstone path",
            "before row 172 atomistic meta prelude opens on the full capstone path",
        ),
    ]
    out = text
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW171_HOMOG_INDEX",
        "row68-row151-homogenization-meta-prelude-capstone-reunion-index-row-171",
    )
    out = out.replace("row 151", "row 171")
    out = out.replace("Row 151", "Row 171")
    out = out.replace("[row 171](preface.md#skill-navigation-row-170)", "[row 170](preface.md#skill-navigation-row-170)")
    out = out.replace("[row 171](preface.md#skill-navigation-row-151)", "[row 151](preface.md#skill-navigation-row-151)")
    out = out.replace("row 1715", "row 172")
    out = out.replace("row 1716", "row 173")
    out = out.replace("row 171 or row 171", "row 170 or row 151")
    out = out.replace("When row 171 closed", "When row 170 closed")
    out = out.replace("after row 171 alone", "after row 170 alone")
    out = out.replace("Recite [preface row 171]", "Recite [preface row 170]")
    out = out.replace("row 171 or row 151 recited", "row 170 or row 151 recited")
    out = out.replace("row 150 closed", "row 170 closed")
    out = out.replace("Row 150 closed", "Row 170 closed")
    out = out.replace("row 150 or row 131 recited", "row 170 or row 151 recited")
    out = out.replace("row 149 or row 50 recited", "row 169 or row 50 recited")
    out = out.replace("row 131", "row 151")
    out = out.replace("Row 131", "Row 151")
    out = out.replace("row 111", "row 131")
    out = out.replace("Row 111", "Row 131")
    out = out.replace(
        "row68-row111-homogenization-meta-prelude-capstone-reunion-index-row-131",
        "row68-row131-homogenization-meta-prelude-capstone-reunion-index-row-151",
    )
    out = out.replace(
        "row68-row130-ddd-meta-prelude-capstone-reunion-index-row-150",
        "row68-row150-ddd-meta-prelude-capstone-reunion-index-row-170",
    )
    out = out.replace("Row 68 → Row 171 Row 68 → Row 51", "Row 68 → Row 151 Row 68 → Row 51")
    out = out.replace(
        "[preface row 151](../preface.md#skill-navigation-row-131)",
        "[preface row 151](../preface.md#skill-navigation-row-151)",
    )
    return out


def extract_preface_row151(preface: str) -> str:
    start = preface.index("### Row 151 skill checkpoint")
    end = preface.index("\n\n### Row 152 skill checkpoint")
    return preface[start:end]


ROW171_PREFACE = t151_to_171(extract_preface_row151((ROOT / "writings/preface/chapters/preface.md").read_text())) + "\n\n"

PROLOGUE_COMPASS = (
    "| Row 68 → Row 151 Row 68 → Row 51 homogenization meta prelude capstone reunion (row 171) | "
    "[Preface: row 171 skill checkpoint](../preface.md#skill-navigation-row-171) · "
    "[Row 68 → Row 151 homogenization meta prelude capstone reunion index](../appendix/sources.md#row68-row151-homogenization-meta-prelude-capstone-reunion-index-row-171) · "
    "[memory sheet row 171 baby picture](../appendix/memory-sheet.md#row-171-baby-picture-row68-row151-homogenization-meta-prelude-capstone-reunion) · "
    "[prologue row 171 preview row](#prologue-preview-row-171); [prologue row 171 closing stitch](#row-171-closing-stitch); "
    "[epilogue row 171 closing loop](../epilogue/multiscale.md#row-171-closing-loop) — "
    "read row 68 gate + row 170 or row 151 DDD meta prelude capstone / homogenization meta prelude gate + VII.2 Bridge → opening hinge → VII.3 homogenization + row 51 meta aloud "
    "when Peach–Köhler DDD is clean on the full capstone path but DAMASK decks feel like CP homework after verified DDD meta prelude capstone on the full capstone path |\n"
)

_prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
_row151_stitch_body = (
    _prologue.split("**Row 151 closing stitch")[1].split("**Row 152 closing stitch")[0].lstrip().split("\n\n")[0]
)
PROLOGUE_STITCH = t151_to_171("**Row 151 closing stitch (Row 68 → Row 131 Row 68 → Row 51 homogenization meta prelude capstone reunion).** {#row-151-closing-stitch} " + _row151_stitch_body.split(".** {#row-151-closing-stitch} ", 1)[-1]) + "\n\n"

PROLOGUE_PREVIEW = (
    '| <span id="prologue-preview-row-171"></span>Row 171 preview (Row 68 → Row 151 Row 68 → Row 51 homogenization meta prelude capstone reunion) | '
    "Explain why midpoint closure (row 68) and VII.2 → VII.3 meta (row 51) must be read together with the Bridge → homogenization chain after verified DDD meta prelude capstone on the full capstone path before OpenDiS exports and DAMASK texture tables feel like separate courses | "
    'One sentence: "read row 68 gate + row 170 or row 151 DDD meta prelude capstone / homogenization meta prelude gate + VII.2 Bridge → opening hinge → VII.3 homogenization + row 51 meta aloud when Peach–Köhler DDD is clean on the full capstone path but DAMASK decks feel like CP homework after verified DDD meta prelude capstone on the full capstone path" — '
    "[preface row 171 skill checkpoint](../preface.md#skill-navigation-row-171); [prologue row 171 closing stitch](#row-171-closing-stitch); "
    "[Row 68 → Row 151 reunion index](../appendix/sources.md#row68-row151-homogenization-meta-prelude-capstone-reunion-index-row-171); "
    "[memory sheet row 171 baby picture](../appendix/memory-sheet.md#row-171-baby-picture-row68-row151-homogenization-meta-prelude-capstone-reunion); "
    "[VII.2 Bridge to VII.3](../part07-defects/02-dislocation-dynamics.md#bridge-to-vii3); "
    "[VII.2 opening hinge to VII.3](../part07-defects/02-dislocation-dynamics.md#opening-hinge-vii2-to-vii3); "
    "[preface row 51 skill checkpoint](../preface.md#skill-navigation-row-51); "
    "[preface row 170 skill checkpoint](../preface.md#skill-navigation-row-170); "
    "[epilogue row 171 closing loop](../epilogue/multiscale.md#row-171-closing-loop) |\n"
)

_epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
EPILOGUE_LOOP = t151_to_171(
    "### Row 151 closing loop"
    + _epilogue.split("### Row 151 closing loop")[1].split("### Row 152 closing loop")[0]
)

SOURCES_TABLE = (
    "| 171 | Row 68 → Row 151 Row 68 → Row 51 homogenization meta prelude capstone (midpoint prelude gate ↔ DDD meta prelude capstone on full capstone path ↔ row 51 meta) | "
    "[Row 68 → Row 151 homogenization meta prelude capstone reunion index](#row68-row151-homogenization-meta-prelude-capstone-reunion-index-row-171) · "
    "[preface row 171](../preface.md#skill-navigation-row-171) · "
    "[prologue row 171 preview](../prologue/00-many-scales.md#prologue-preview-row-171) · "
    "[prologue row 171 closing stitch](../prologue/00-many-scales.md#row-171-closing-stitch) · "
    "[epilogue row 171 closing loop](../epilogue/multiscale.md#row-171-closing-loop) · "
    "[memory sheet row 171 baby picture](memory-sheet.md#row-171-baby-picture-row68-row151-homogenization-meta-prelude-capstone-reunion) | "
    "Row 68 closed but **row 51 VII.2 → VII.3 opening hinge still feels disconnected from verified DDD meta prelude capstone on the full capstone path** — "
    "read row 68 + row 170 or row 151 gate + VII.2 Bridge → opening hinge → VII.3 homogenization + row 51; "
    "[preface row 51](../preface.md#skill-navigation-row-51) |\n"
)

SOURCES_INDEX = t151_to_171(
    (ROOT / "writings/appendix/chapters/sources.md")
    .read_text()
    .split("## Row 68 → Row 131 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 151)")[1]
    .split("## Row 68 → Row 111 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 131)")[0]
)
SOURCES_INDEX = (
    "## Row 68 → Row 151 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 171)"
    + SOURCES_INDEX
)

MEMORY_TABLE = (
    "| 171 | Meta | [Row 68 → Row 151 homogenization meta prelude capstone reunion index](sources.md#row68-row151-homogenization-meta-prelude-capstone-reunion-index-row-171) · "
    "[preface row 171 skill checkpoint](../preface.md#skill-navigation-row-171) · "
    "[prologue row 171 preview](../prologue/00-many-scales.md#prologue-preview-row-171) · "
    "[prologue row 171 closing stitch](../prologue/00-many-scales.md#row-171-closing-stitch) · "
    "[epilogue row 171 closing loop](../epilogue/multiscale.md#row-171-closing-loop) | "
    "Row 68 closed but row 51 homogenization meta reunion feels disconnected from verified DDD meta prelude capstone on the full capstone path — "
    "read row 68 + row 170 or row 151 gate + VII.2 Bridge → opening hinge → VII.3 homogenization + row 51; "
    "[row 171 baby picture](#row-171-baby-picture-row68-row151-homogenization-meta-prelude-capstone-reunion) |\n"
)

MEMORY_BABY = t151_to_171(
    (ROOT / "writings/appendix/chapters/memory-sheet.md")
    .read_text()
    .split("### Row 131 baby picture")[1]
    .split("### Row 147 baby picture")[0]
)
MEMORY_BABY = (
    "### Row 171 baby picture (Row 68 → Row 151 Row 68 → Row 51 homogenization meta prelude capstone reunion)"
    + MEMORY_BABY.split(")", 1)[1]
    if ")" in MEMORY_BABY
    else "### Row 171 baby picture" + MEMORY_BABY
)

ROW170_TAIL_MARKER = "**When to pause.** Read the [prologue row 170 closing stitch]"
ROW170_TAIL_END = "or extend prose only under `writings/` then sync.\n\n\n## The copper wire through the book"

ROW170_STITCH_OLD = (
    "before row 151 homogenization meta prelude capstone reunion opens on the full capstone path."
)
ROW170_STITCH_NEW = (
    "before row 171 homogenization meta prelude capstone reunion opens on the full capstone path."
)

ROW170_EPILOGUE_PROCEED_OLD = (
    "Proceed to [row 151](#row-151-closing-loop) when row 68 closed but homogenization meta prelude capstone still lags after row 170 on the full capstone path,"
)
ROW170_EPILOGUE_PROCEED_NEW = (
    "Proceed to [row 171](#row-171-closing-loop) when row 68 closed but homogenization meta prelude capstone still lags after row 170 on the full capstone path,"
)

ROW170_BABY_OLD = (
    "row 150 when **VII.1 Bridge and Row 68 → Row 50 meta must read on the same wire before row 151 homogenization meta prelude capstone opens on the full capstone path**"
)
ROW170_BABY_NEW = (
    "row 170 when **VII.1 Bridge and Row 68 → Row 50 meta must read on the same wire before row 171 homogenization meta prelude capstone opens on the full capstone path**"
)


def update_row170_tail(preface: str) -> str:
    start = preface.index(ROW170_TAIL_MARKER)
    end = preface.index(ROW170_TAIL_END)
    block = preface[start:end]
    new_block = block.replace(
        "when opening [row 151](preface.md#skill-navigation-row-151) before row 51 closes on the full capstone path",
        "when opening [row 171](preface.md#skill-navigation-row-171) before row 51 closes on the full capstone path",
    )
    new_block = new_block.replace(
        "When row 170 is complete, proceed to [row 151](preface.md#skill-navigation-row-151) when homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the full capstone path, to [row 150](preface.md#skill-navigation-row-130) when DDD meta prelude capstone still lags after verified taxonomy meta prelude capstone on the opening-hinge capstone path alone, to [row 130](preface.md#skill-navigation-row-110) for the Row 68 ↔ Row 50 DDD meta audit on the opening-hinge prelude path alone, to [row 149](preface.md#skill-navigation-row-149) when taxonomy meta prelude capstone still lags after verified midpoint meta prelude capstone on the full capstone path, to [row 149](preface.md#skill-navigation-row-129) when taxonomy meta prelude capstone still lags after verified midpoint meta prelude capstone on the opening-hinge capstone path alone, to [row 50](preface.md#skill-navigation-row-50) when only VII.1 → VII.2 stalls, to [row 90](preface.md#skill-navigation-row-90) for the Row 68 ↔ Row 50 DDD opening prelude audit alone, or extend prose only under `writings/` then sync.",
        "When row 170 is complete, proceed to [row 171](preface.md#skill-navigation-row-171) when homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the full capstone path, to [row 151](preface.md#skill-navigation-row-151) when homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the opening-hinge capstone path alone, to [row 131](preface.md#skill-navigation-row-131) for the Row 68 ↔ Row 51 homogenization meta audit on the opening-hinge prelude path alone, to [row 150](preface.md#skill-navigation-row-150) when DDD meta prelude capstone still lags after verified taxonomy meta prelude capstone on the full capstone path, to [row 130](preface.md#skill-navigation-row-130) when DDD meta prelude capstone still lags after verified taxonomy meta prelude capstone on the opening-hinge capstone path alone, to [row 50](preface.md#skill-navigation-row-50) when only VII.1 → VII.2 stalls, to [row 90](preface.md#skill-navigation-row-90) for the Row 68 ↔ Row 50 DDD opening prelude audit alone, or extend prose only under `writings/` then sync.",
    )
    return preface[:start] + new_block + preface[end:]


def main():
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "skill-navigation-row-171" in preface:
        print("preface: row 171 already present")
    else:
        if "skill-navigation-row-170" in preface:
            preface = update_row170_tail(preface)
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + ROW171_PREFACE + copper)
        preface_path.write_text(preface)
        print("preface: added row 171")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-171" not in prologue:
        needle = "| Row 68 → Row 150 Row 68 → Row 50 DDD meta prelude capstone reunion (row 170) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 170 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + PROLOGUE_COMPASS + prologue[line_end + 1 :]
        prologue = prologue.replace(
            "**Row 170 closing stitch",
            PROLOGUE_STITCH + "**Row 170 closing stitch",
        )
        prologue = prologue.replace(
            '| <span id="prologue-preview-row-170"></span>Row 170 preview',
            PROLOGUE_PREVIEW + '| <span id="prologue-preview-row-170"></span>Row 170 preview',
        )
        if ROW170_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW170_STITCH_OLD, ROW170_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 171")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "row-171-closing-loop" not in epilogue:
        marker = (
            "Proceed to [row 151](#row-151-closing-loop) when row 68 closed but homogenization meta prelude capstone still lags after row 170 on the full capstone path, to [row 130](#row-110-closing-loop) for the Row 68 ↔ Row 50 DDD meta audit on the opening-hinge prelude path alone, to [row 149](#row-129-closing-loop) when taxonomy meta prelude capstone still lags after verified midpoint meta prelude capstone, to [row 50](#row-50-closing-loop) when only VII.1 → VII.2 stalls, or extend prose only under `writings/` then sync.\n\n\n\n\n\n### Row 129 closing loop"
        )
        replacement = (
            "Proceed to [row 171](#row-171-closing-loop) when row 68 closed but homogenization meta prelude capstone still lags after row 170 on the full capstone path, to [row 130](#row-110-closing-loop) for the Row 68 ↔ Row 50 DDD meta audit on the opening-hinge prelude path alone, to [row 149](#row-129-closing-loop) when taxonomy meta prelude capstone still lags after verified midpoint meta prelude capstone, to [row 50](#row-50-closing-loop) when only VII.1 → VII.2 stalls, or extend prose only under `writings/` then sync.\n\n\n\n\n\n\n"
            + EPILOGUE_LOOP
            + "\n\n\n\n\n\n### Row 129 closing loop"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 170 end marker not found")
        epilogue = epilogue.replace(marker, replacement, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 171")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row151-homogenization-meta-prelude-capstone-reunion-index-row-171" not in sources:
        sources = sources.replace(
            "| 151 | Row 68 → Row 131 Row 68 → Row 51 homogenization meta prelude capstone",
            SOURCES_TABLE + "| 151 | Row 68 → Row 131 Row 68 → Row 51 homogenization meta prelude capstone",
        )
        sources = sources.replace(
            "## Row 68 → Row 131 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 151)",
            SOURCES_INDEX + "## Row 68 → Row 131 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 151)",
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 171")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-171-baby-picture-row68-row151" not in memory:
        memory = memory.replace(
            "| 170 | Meta | [Row 68 → Row 150 DDD meta prelude capstone reunion index]",
            MEMORY_TABLE + "| 170 | Meta | [Row 68 → Row 150 DDD meta prelude capstone reunion index]",
        )
        memory = memory.replace(
            "### Row 151 baby picture (Row 68 → Row 131 Row 68 → Row 51 homogenization meta prelude capstone reunion) {#row-151-baby-picture-row68-row131-homogenization-meta-prelude-capstone-reunion}",
            MEMORY_BABY + "### Row 151 baby picture (Row 68 → Row 131 Row 68 → Row 51 homogenization meta prelude capstone reunion) {#row-151-baby-picture-row68-row131-homogenization-meta-prelude-capstone-reunion}",
            1,
        )
        memory = memory.replace(ROW170_BABY_OLD, ROW170_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 171")


if __name__ == "__main__":
    main()
