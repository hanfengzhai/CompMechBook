#!/usr/bin/env python3
"""Add row 169 meta-stitch (Row 68 → Row 149 ↔ Row 49 taxonomy meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def t149_to_169(text: str) -> str:
    """Transform row-149 capstone-path meta copy to row 169 (149→169, 129→149 inner, 168 gate)."""
    repl = [
        ("Row 68 → Row 129 Row 68 → Row 49", "Row 68 → Row 149 Row 68 → Row 49"),
        ("row68-row129-taxonomy-meta-prelude-capstone-reunion-index-row-149", "TEMP_ROW169_TAXONOMY_INDEX"),
        ("row-149-baby-picture-row68-row129-taxonomy-meta-prelude-capstone-reunion", "row-169-baby-picture-row68-row149-taxonomy-meta-prelude-capstone-reunion"),
        ("skill-navigation-row-149", "skill-navigation-row-169"),
        ("prologue-preview-row-149", "prologue-preview-row-169"),
        ("row-149-closing-stitch", "row-169-closing-stitch"),
        ("row-149-closing-loop", "row-169-closing-loop"),
        ("Row 149 three-way audit", "Row 169 three-way audit"),
        ("[row 148](preface.md#skill-navigation-row-148) or [row 129](preface.md#skill-navigation-row-129)", "[row 168](preface.md#skill-navigation-row-168) or [row 149](preface.md#skill-navigation-row-149)"),
        ("[row 148](preface.md#skill-navigation-row-148) or [Row 68 → Row 109 taxonomy meta prelude capstone reunion index (row 129)](appendix/sources.md#row68-row109-taxonomy-meta-prelude-capstone-reunion-index-row-129)", "[row 168](preface.md#skill-navigation-row-168) or [Row 68 → Row 129 taxonomy meta prelude capstone reunion index (row 149)](appendix/sources.md#row68-row129-taxonomy-meta-prelude-capstone-reunion-index-row-149)"),
        ("verified part-boundary meta prelude capstone via [row 147](preface.md#skill-navigation-row-147)", "verified midpoint meta prelude capstone via [row 167](preface.md#skill-navigation-row-167)"),
        ("verified midpoint meta prelude capstone on the full capstone path (row 148)", "verified midpoint meta prelude capstone on the full capstone path (row 168)"),
    ]
    out = text
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace("TEMP_ROW169_TAXONOMY_INDEX", "row68-row149-taxonomy-meta-prelude-capstone-reunion-index-row-169")
    out = out.replace("row 149", "row 169")
    out = out.replace("Row 149", "Row 169")
    out = out.replace("[row 169](preface.md#skill-navigation-row-168)", "[row 168](preface.md#skill-navigation-row-168)")
    out = out.replace("[row 169](preface.md#skill-navigation-row-149)", "[row 149](preface.md#skill-navigation-row-149)")
    out = out.replace("row 1695", "row 170")
    out = out.replace("row 1696", "row 171")
    out = out.replace("row 169 or row 169", "row 168 or row 149")
    out = out.replace("When row 169 closed", "When row 168 closed")
    out = out.replace("after row 169 alone", "after row 168 alone")
    out = out.replace("Recite [preface row 169]", "Recite [preface row 168]")
    out = out.replace("row 169 or row 149 recited", "row 168 or row 149 recited")
    out = out.replace("row 148 closed", "row 168 closed")
    out = out.replace("Row 148 closed", "Row 168 closed")
    out = out.replace("row 147 or row 128 recited", "row 167 or row 149 recited")
    out = out.replace("row 129", "row 149")
    out = out.replace("Row 129", "Row 149")
    out = out.replace("row 148", "row 168")
    out = out.replace("Row 148", "Row 168")
    out = out.replace("row 147", "row 167")
    out = out.replace("Row 147", "Row 167")
    out = out.replace("row 109", "row 129")
    out = out.replace("Row 109", "Row 129")
    out = out.replace("row68-row109-taxonomy-meta-prelude-capstone-reunion-index-row-129", "row68-row129-taxonomy-meta-prelude-capstone-reunion-index-row-149")
    out = out.replace(
        "row68-row128-midpoint-meta-prelude-capstone-reunion-index-row-148",
        "row68-row148-midpoint-meta-prelude-capstone-reunion-index-row-168",
    )
    out = out.replace("[row 166](preface.md#skill-navigation-row-146)", "[row 166](preface.md#skill-navigation-row-166)")
    out = out.replace("[row 167](preface.md#skill-navigation-row-147)", "[row 167](preface.md#skill-navigation-row-167)")
    out = out.replace("[preface row 167](../preface.md#skill-navigation-row-147)", "[preface row 167](../preface.md#skill-navigation-row-167)")
    out = out.replace("[preface row 149](../preface.md#skill-navigation-row-129)", "[preface row 149](../preface.md#skill-navigation-row-149)")
    return out



def extract_preface_row149(preface: str) -> str:
    start = preface.index("### Row 149 skill checkpoint")
    end = preface.index("\n\n### Row 150 skill checkpoint")
    return preface[start:end]


ROW169_PREFACE = t149_to_169(
    extract_preface_row149((ROOT / "writings/preface/chapters/preface.md").read_text())
) + "\n\n"

PROLOGUE_COMPASS = (
    "| Row 68 → Row 149 Row 68 → Row 49 taxonomy meta prelude capstone reunion (row 169) | "
    "[Preface: row 169 skill checkpoint](../preface.md#skill-navigation-row-169) · "
    "[Row 68 → Row 149 taxonomy meta prelude capstone reunion index](../appendix/sources.md#row68-row149-taxonomy-meta-prelude-capstone-reunion-index-row-169) · "
    "[memory sheet row 169 baby picture](../appendix/memory-sheet.md#row-169-baby-picture-row68-row149-taxonomy-meta-prelude-capstone-reunion) · "
    "[prologue row 169 preview row](#prologue-preview-row-169); [prologue row 169 closing stitch](#row-169-closing-stitch); "
    "[epilogue row 169 closing loop](../epilogue/multiscale.md#row-169-closing-loop) — "
    "read row 68 gate + row 168 or row 149 midpoint meta prelude capstone / taxonomy meta prelude gate + VII.0 Bridge → opening hinge → VII.1 taxonomy + row 49 meta aloud "
    "when forest landing is clean on the full capstone path but Burgers circuits feel like Defects Notes homework after verified midpoint meta prelude capstone on the full capstone path |\n"
)

_prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
PROLOGUE_STITCH = t149_to_169(
    "**Row 149 closing stitch (Row 68 → Row 129 Row 68 → Row 49 taxonomy meta prelude capstone reunion).** {#row-149-closing-stitch} "
    + _prologue.split("**Row 149 closing stitch")[1].split("**Row 150 closing stitch")[0].lstrip()
    .split("\n\n")[0]
    + "\n\n"
)

PROLOGUE_PREVIEW = (
    "| <span id=\"prologue-preview-row-169\"></span>Row 169 preview (Row 68 → Row 149 Row 68 → Row 49 taxonomy meta prelude capstone reunion) | "
    "Explain why midpoint closure (row 68) and VII.0 → VII.1 meta (row 49) must be read together with the Bridge → Burgers taxonomy chain after verified midpoint meta prelude capstone on the full capstone path before forest landing and dimension tables feel like separate courses | "
    "One sentence: \"read row 68 gate + row 168 or row 149 midpoint meta prelude capstone / taxonomy meta prelude gate + VII.0 Bridge → opening hinge → VII.1 taxonomy + row 49 meta aloud when forest landing is clean on the full capstone path but Burgers circuits feel like Defects Notes homework after verified midpoint meta prelude capstone on the full capstone path\" — "
    "[preface row 169 skill checkpoint](../preface.md#skill-navigation-row-169); [prologue row 169 closing stitch](#row-169-closing-stitch); "
    "[Row 68 → Row 149 reunion index](../appendix/sources.md#row68-row149-taxonomy-meta-prelude-capstone-reunion-index-row-169); "
    "[memory sheet row 169 baby picture](../appendix/memory-sheet.md#row-169-baby-picture-row68-row149-taxonomy-meta-prelude-capstone-reunion); "
    "[VII.0 Bridge](../part07-defects/00-opening.md#bridge); "
    "[VII.0 opening hinge to VII.1](../part07-defects/00-opening.md#opening-hinge-vii0-to-vii1); "
    "[preface row 49 skill checkpoint](../preface.md#skill-navigation-row-49); "
    "[preface row 168 skill checkpoint](../preface.md#skill-navigation-row-168); "
    "[epilogue row 169 closing loop](../epilogue/multiscale.md#row-169-closing-loop) |\n"
)

_epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
EPILOGUE_LOOP = t149_to_169(
    "### Row 149 closing loop"
    + _epilogue.split("### Row 149 closing loop")[1].split("### Row 150 closing loop")[0]
)

SOURCES_TABLE = (
    "| 169 | Row 68 → Row 149 Row 68 → Row 49 taxonomy meta prelude capstone (midpoint prelude gate ↔ midpoint meta prelude capstone on full capstone path ↔ row 49 meta) | "
    "[Row 68 → Row 149 taxonomy meta prelude capstone reunion index](#row68-row149-taxonomy-meta-prelude-capstone-reunion-index-row-169) · "
    "[preface row 169](../preface.md#skill-navigation-row-169) · "
    "[prologue row 169 preview](../prologue/00-many-scales.md#prologue-preview-row-169) · "
    "[prologue row 169 closing stitch](../prologue/00-many-scales.md#row-169-closing-stitch) · "
    "[epilogue row 169 closing loop](../epilogue/multiscale.md#row-169-closing-loop) · "
    "[memory sheet row 169 baby picture](memory-sheet.md#row-169-baby-picture-row68-row149-taxonomy-meta-prelude-capstone-reunion) | "
    "Row 68 closed but **row 49 VII.0 → VII.1 opening hinge still feels disconnected from verified midpoint meta prelude capstone on the full capstone path** — "
    "read row 68 + row 168 or row 149 gate + VII.0 Bridge → opening hinge → VII.1 taxonomy + row 49; "
    "[preface row 49](../preface.md#skill-navigation-row-49) |\n"
)

SOURCES_INDEX = t149_to_169(
    (ROOT / "writings/appendix/chapters/sources.md")
    .read_text()
    .split("## Row 68 → Row 129 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 149)")[1]
    .split("## Row 68 → Row 130 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 150)")[0]
)
SOURCES_INDEX = (
    "## Row 68 → Row 149 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 169)"
    + SOURCES_INDEX
)

MEMORY_TABLE = (
    "| 169 | Meta | [Row 68 → Row 149 taxonomy meta prelude capstone reunion index](sources.md#row68-row149-taxonomy-meta-prelude-capstone-reunion-index-row-169) · "
    "[preface row 169 skill checkpoint](../preface.md#skill-navigation-row-169) · "
    "[prologue row 169 preview](../prologue/00-many-scales.md#prologue-preview-row-169) · "
    "[prologue row 169 closing stitch](../prologue/00-many-scales.md#row-169-closing-stitch) · "
    "[epilogue row 169 closing loop](../epilogue/multiscale.md#row-169-closing-loop) | "
    "Row 68 closed but row 49 taxonomy meta reunion feels disconnected from verified midpoint meta prelude capstone on the full capstone path — "
    "read row 68 + row 168 or row 149 gate + VII.0 Bridge → opening hinge → VII.1 taxonomy + row 49; "
    "[row 169 baby picture](#row-169-baby-picture-row68-row149-taxonomy-meta-prelude-capstone-reunion) |\n"
)

MEMORY_BABY = t149_to_169(
    (ROOT / "writings/appendix/chapters/memory-sheet.md")
    .read_text()
    .split("### Row 149 baby picture")[1]
    .split("### Row 150 baby picture")[0]
)
MEMORY_BABY = (
    "### Row 169 baby picture"
    + MEMORY_BABY.split(")", 1)[1]
    if ")" in MEMORY_BABY
    else "### Row 169 baby picture" + MEMORY_BABY
)

ROW168_TAIL_MARKER = "**When to pause.** Read the [prologue row 168 closing stitch]"
ROW168_TAIL_END = "or extend prose only under `writings/` then sync.\n\n\n\n## The copper wire through the book"

ROW168_STITCH_OLD = (
    "before row 149 taxonomy meta prelude capstone reunion opens on the full capstone path."
)
ROW168_STITCH_NEW = (
    "before row 169 taxonomy meta prelude capstone reunion opens on the full capstone path."
)

ROW168_EPILOGUE_PROCEED_OLD = (
    "Proceed to [row 149](#row-149-closing-loop) when row 68 closed but taxonomy meta prelude capstone still lags after row 168 on the full capstone path,"
)
ROW168_EPILOGUE_PROCEED_NEW = (
    "Proceed to [row 169](#row-169-closing-loop) when row 68 closed but taxonomy meta prelude capstone still lags after row 168 on the full capstone path,"
)

ROW168_BABY_OLD = (
    "row 167 when **V.4 → VI.0 twin-ladder reunion and Row 66 → Row 47 meta must read on the same wire before row 148 midpoint meta prelude capstone opens on the full capstone path**"
)
ROW168_BABY_NEW = (
    "row 168 when **VI.4 intermission and Row 67 → Row 48 meta must read on the same wire before row 169 taxonomy meta prelude capstone opens on the full capstone path**"
)


def update_row168_tail(preface: str) -> str:
    start = preface.index(ROW168_TAIL_MARKER)
    end = preface.index(ROW168_TAIL_END)
    block = preface[start:end]
    new_block = block.replace(
        "when opening [row 149](preface.md#skill-navigation-row-149) before row 49 closes on the full capstone path",
        "when opening [row 169](preface.md#skill-navigation-row-169) before row 49 closes on the full capstone path",
    )
    new_block = new_block.replace(
        "When row 168 is complete, proceed to [row 149](preface.md#skill-navigation-row-149) when midpoint meta prelude capstone is clean but taxonomy meta prelude capstone still lags after verified forest landing on the full capstone path, to [row 129](preface.md#skill-navigation-row-129) when midpoint meta prelude capstone is clean but taxonomy meta prelude capstone still lags after verified forest landing on the opening-hinge capstone path alone, to [row 109](preface.md#skill-navigation-row-109) for the Row 68 ↔ Row 49 meta audit on the opening-hinge prelude path alone, to [row 108](preface.md#skill-navigation-row-108) for the Row 68 ↔ Row 48 meta audit on the opening-hinge prelude path alone, to [row 148](preface.md#skill-navigation-row-148) for the Row 68 ↔ Row 48 meta audit on the opening-hinge capstone path alone, to [row 167](preface.md#skill-navigation-row-167) when part-boundary meta prelude capstone still lags after verified Writings canonical meta prelude capstone on the full capstone path, to [row 88](preface.md#skill-navigation-row-88) for the Row 68 ↔ Row 48 opening prelude audit alone, to [row 48](preface.md#skill-navigation-row-48) for the VI.4 → VII.0 meta audit alone, to [row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, or extend prose only under `writings/` then sync.",
        "When row 168 is complete, proceed to [row 169](preface.md#skill-navigation-row-169) when midpoint meta prelude capstone is clean but taxonomy meta prelude capstone still lags after verified forest landing on the full capstone path, to [row 149](preface.md#skill-navigation-row-149) when midpoint meta prelude capstone is clean but taxonomy meta prelude capstone still lags after verified forest landing on the opening-hinge capstone path alone, to [row 109](preface.md#skill-navigation-row-109) for the Row 68 ↔ Row 49 meta audit on the opening-hinge prelude path alone, to [row 108](preface.md#skill-navigation-row-108) for the Row 68 ↔ Row 48 meta audit on the opening-hinge prelude path alone, to [row 148](preface.md#skill-navigation-row-148) for the Row 68 ↔ Row 48 meta audit on the opening-hinge capstone path alone, to [row 167](preface.md#skill-navigation-row-167) when part-boundary meta prelude capstone still lags after verified Writings canonical meta prelude capstone on the full capstone path, to [row 88](preface.md#skill-navigation-row-88) for the Row 68 ↔ Row 48 opening prelude audit alone, to [row 48](preface.md#skill-navigation-row-48) for the VI.4 → VII.0 meta audit alone, to [row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, or extend prose only under `writings/` then sync.",
    )
    return preface[:start] + new_block + preface[end:]


def main():
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "skill-navigation-row-169" in preface and preface.index("skill-navigation-row-169") < preface.index(copper):
        print("preface: row 169 already present")
    else:
        preface = update_row168_tail(preface)
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + ROW169_PREFACE + copper)
        preface_path.write_text(preface)
        print("preface: added row 169")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-169" not in prologue:
        needle = "| Row 68 → Row 148 Row 68 → Row 48 midpoint meta prelude capstone reunion (row 168) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 168 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + PROLOGUE_COMPASS + prologue[line_end + 1 :]
        prologue = prologue.replace(
            "**Row 168 closing stitch",
            PROLOGUE_STITCH + "**Row 168 closing stitch",
        )
        prologue = prologue.replace(
            '| <span id="prologue-preview-row-168"></span>Row 168 preview',
            PROLOGUE_PREVIEW + '| <span id="prologue-preview-row-168"></span>Row 168 preview',
        )
        if ROW168_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW168_STITCH_OLD, ROW168_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 169")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "row-169-closing-loop" not in epilogue:
        if ROW168_EPILOGUE_PROCEED_OLD in epilogue:
            epilogue = epilogue.replace(ROW168_EPILOGUE_PROCEED_OLD, ROW168_EPILOGUE_PROCEED_NEW)
        marker = (
            "to [row 48](#row-48-closing-loop) when only midpoint prelude meta stalls, or extend prose only under `writings/` then sync.\n\n\n\n\n\n\n\n### Row 135 closing loop"
        )
        replacement = (
            "to [row 48](#row-48-closing-loop) when only midpoint prelude meta stalls, or extend prose only under `writings/` then sync.\n\n\n"
            + EPILOGUE_LOOP
            + "\n\n\n\n\n### Row 135 closing loop"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 168 end marker not found")
        epilogue = epilogue.replace(marker, replacement, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 169")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row149-taxonomy-meta-prelude-capstone-reunion-index-row-169" not in sources:
        sources = sources.replace(
            "| 149 | Row 68 → Row 129 Row 68 → Row 49 taxonomy meta prelude capstone",
            SOURCES_TABLE + "| 149 | Row 68 → Row 129 Row 68 → Row 49 taxonomy meta prelude capstone",
        )
        sources = sources.replace(
            "## Row 68 → Row 129 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 149)",
            SOURCES_INDEX + "## Row 68 → Row 129 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 149)",
        )
        sources_path.write_text(sources)
        print("sources: added row 169")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-169-baby-picture-row68-row149" not in memory:
        memory = memory.replace(
            "| 168 | Meta | [Row 68 → Row 148 midpoint meta prelude capstone reunion index]",
            MEMORY_TABLE + "| 168 | Meta | [Row 68 → Row 148 midpoint meta prelude capstone reunion index]",
        )
        memory = memory.replace(
            "### Row 168 baby picture {#row-168-baby-picture-row68-row148-midpoint-meta-prelude-capstone-reunion}",
            MEMORY_BABY + "### Row 168 baby picture {#row-168-baby-picture-row68-row148-midpoint-meta-prelude-capstone-reunion}",
        )
        memory = memory.replace(ROW168_BABY_OLD, ROW168_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 169")


if __name__ == "__main__":
    main()
