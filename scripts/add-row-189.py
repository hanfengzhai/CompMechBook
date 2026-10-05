#!/usr/bin/env python3
"""Add row 189 meta-stitch (Row 68 → Row 169 ↔ Row 49 taxonomy meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def bump169_to_189(text: str) -> str:
    """Transform row-169 capstone-path meta copy to row 189 (149→169 inner, 188 gate)."""
    repl = [
        ("Row 68 → Row 149 Row 68 → Row 49", "Row 68 → Row 169 Row 68 → Row 49"),
        (
            "row68-row149-taxonomy-meta-prelude-capstone-reunion-index-row-169",
            "TEMP_ROW189_TAXONOMY_INDEX",
        ),
        (
            "row-169-baby-picture-row68-row149-taxonomy-meta-prelude-capstone-reunion",
            "row-189-baby-picture-row68-row169-taxonomy-meta-prelude-capstone-reunion",
        ),
        ("### Row 169 skill checkpoint", "### Row 189 skill checkpoint"),
        ("skill-navigation-row-169", "skill-navigation-row-189"),
        ("prologue-preview-row-169", "prologue-preview-row-189"),
        ("row-169-closing-stitch", "row-189-closing-stitch"),
        ("row-169-closing-loop", "row-189-closing-loop"),
        ("Row 169 three-way audit", "Row 189 three-way audit"),
        (
            "[row 168](preface.md#skill-navigation-row-168) or [row 149](preface.md#skill-navigation-row-149)",
            "[row 188](preface.md#skill-navigation-row-188) or [row 169](preface.md#skill-navigation-row-169)",
        ),
        (
            "[row 168](preface.md#skill-navigation-row-168) or [Row 68 → Row 129 taxonomy meta prelude capstone reunion index (row 149)](appendix/sources.md#row68-row129-taxonomy-meta-prelude-capstone-reunion-index-row-149)",
            "[row 188](preface.md#skill-navigation-row-188) or [Row 68 → Row 149 taxonomy meta prelude capstone reunion index (row 169)](appendix/sources.md#row68-row149-taxonomy-meta-prelude-capstone-reunion-index-row-169)",
        ),
        (
            "verified midpoint meta prelude capstone via [row 167](preface.md#skill-navigation-row-167)",
            "verified midpoint meta prelude capstone via [row 187](preface.md#skill-navigation-row-187)",
        ),
        (
            "verified midpoint meta prelude capstone on the full capstone path (row 168)",
            "verified midpoint meta prelude capstone on the full capstone path (row 188)",
        ),
    ]
    out = text
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace("TEMP_ROW189_TAXONOMY_INDEX", "row68-row169-taxonomy-meta-prelude-capstone-reunion-index-row-189")
    out = out.replace("Row 169 does not replace", "Row 189 does not replace")
    out = out.replace(
        "When row 169 is complete, proceed to [row 150](preface.md#skill-navigation-row-150) when taxonomy meta prelude capstone is clean but DDD meta prelude capstone still lags after verified Burgers closure on the full capstone path, to [row 130](preface.md#skill-navigation-row-130) when taxonomy meta prelude capstone is clean but DDD meta prelude capstone still lags after verified Burgers closure on the opening-hinge capstone path alone, to [row 110](preface.md#skill-navigation-row-110) for the Row 68 ↔ Row 50 DDD meta audit on the opening-hinge prelude path alone, to [row 129](preface.md#skill-navigation-row-129) for the Row 68 ↔ Row 49 meta audit on the opening-hinge prelude path alone, to [row 149](preface.md#skill-navigation-row-149) when taxonomy meta prelude capstone still lags after verified midpoint meta prelude capstone on the opening-hinge capstone path alone, to [row 168](preface.md#skill-navigation-row-168) when midpoint meta prelude capstone still lags after verified part-boundary meta prelude capstone on the full capstone path, to [row 89](preface.md#skill-navigation-row-89) for the Row 68 ↔ Row 49 taxonomy opening prelude audit alone, to [row 49](preface.md#skill-navigation-row-49) for the VII.0 → VII.1 meta audit alone, to [row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, or extend prose only under `writings/` then sync.",
        "When row 189 is complete, proceed to [row 170](preface.md#skill-navigation-row-170) when taxonomy meta prelude capstone is clean but DDD meta prelude capstone still lags after verified Burgers closure on the full capstone path, to [row 150](preface.md#skill-navigation-row-150) when taxonomy meta prelude capstone is clean but DDD meta prelude capstone still lags after verified Burgers closure on the opening-hinge capstone path alone, to [row 130](preface.md#skill-navigation-row-130) for the Row 68 ↔ Row 50 DDD meta audit on the opening-hinge prelude path alone, to [row 129](preface.md#skill-navigation-row-129) for the Row 68 ↔ Row 49 meta audit on the opening-hinge prelude path alone, to [row 169](preface.md#skill-navigation-row-169) when taxonomy meta prelude capstone still lags after verified midpoint meta prelude capstone on the opening-hinge capstone path alone, to [row 188](preface.md#skill-navigation-row-188) when midpoint meta prelude capstone still lags after verified part-boundary meta prelude capstone on the full capstone path, to [row 89](preface.md#skill-navigation-row-89) for the Row 68 ↔ Row 49 taxonomy opening prelude audit alone, to [row 49](preface.md#skill-navigation-row-49) for the VII.0 → VII.1 meta audit alone, to [row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, or extend prose only under `writings/` then sync.",
    )
    out = out.replace("When row 169 is complete", "When row 189 is complete")
    out = out.replace("When row 169 closed", "When row 188 closed")
    out = out.replace("after row 169 alone", "after row 188 alone")
    out = out.replace("Recite [preface row 169]", "Recite [preface row 188]")
    out = out.replace("row 169 or row 150 recited", "row 189 or row 170 recited")
    out = out.replace("row 168 closed", "row 188 closed")
    out = out.replace("Row 168 closed", "Row 188 closed")
    out = out.replace("row 167 or row 149 recited", "row 187 or row 169 recited")
    out = out.replace("row 129", "row 149")
    out = out.replace("Row 129", "Row 149")
    out = out.replace("row 149", "row 169")
    out = out.replace("Row 149", "Row 169")
    out = out.replace("row 148", "row 168")
    out = out.replace("Row 148", "Row 168")
    out = out.replace("row 167", "row 187")
    out = out.replace("Row 167", "Row 187")
    out = out.replace("row 109", "row 129")
    out = out.replace("Row 109", "Row 129")
    out = out.replace(
        "row68-row129-taxonomy-meta-prelude-capstone-reunion-index-row-149",
        "row68-row149-taxonomy-meta-prelude-capstone-reunion-index-row-169",
    )
    out = out.replace(
        "row68-row148-midpoint-meta-prelude-capstone-reunion-index-row-168",
        "row68-row168-midpoint-meta-prelude-capstone-reunion-index-row-188",
    )
    out = out.replace("[row 189](preface.md#skill-navigation-row-188)", "[row 188](preface.md#skill-navigation-row-188)")
    out = out.replace("[row 189](preface.md#skill-navigation-row-169)", "[row 169](preface.md#skill-navigation-row-169)")
    out = out.replace(
        "[row 170](preface.md#skill-navigation-row-170) before row 50",
        "[row 190](preface.md#skill-navigation-row-190) before row 50",
    )
    out = out.replace("memory sheet row 169 baby picture", "memory sheet row 189 baby picture")
    out = out.replace("prologue row 169 closing stitch", "prologue row 189 closing stitch")
    out = out.replace("prologue row 169 preview", "prologue row 189 preview")
    out = out.replace("epilogue row 169 closing loop", "epilogue row 189 closing loop")
    out = out.replace("row 168's forest", "row 188's forest")
    out = out.replace("after row 168 ", "after row 188 ")
    out = out.replace(
        "verified midpoint meta prelude capstone closure on the full capstone path (row 168)",
        "verified midpoint meta prelude capstone closure on the full capstone path (row 188)",
    )
    out = out.replace(
        "reunion index (row 169)](appendix/sources.md#row68-row149-taxonomy-meta-prelude-capstone-reunion-index-row-169)",
        "reunion index (row 189)](appendix/sources.md#row68-row169-taxonomy-meta-prelude-capstone-reunion-index-row-189)",
    )
    out = out.replace(
        "Prologue preview ([row 169](prologue/00-many-scales.md#prologue-preview-row-189))",
        "Prologue preview ([row 189](prologue/00-many-scales.md#prologue-preview-row-189))",
    )
    out = out.replace("when row 168 and row 49", "when row 188 and row 49")
    out = out.replace(
        "[row 169](preface.md#skill-navigation-row-129)",
        "[row 149](preface.md#skill-navigation-row-149)",
    )
    out = out.replace("row 169, row 129,", "row 189, row 149,")
    return out


def extract_preface_row169(preface: str) -> str:
    start = preface.index(
        "### Row 169 skill checkpoint — Row 68 → Row 149 Row 68 → Row 49"
    )
    end = preface.index("\n\n### Row 170 skill checkpoint", start)
    return preface[start:end]


ROW189_PREFACE = bump169_to_189(
    extract_preface_row169((ROOT / "writings/preface/chapters/preface.md").read_text())
) + "\n\n"

PROLOGUE_COMPASS = (
    "| Row 68 → Row 169 Row 68 → Row 49 taxonomy meta prelude capstone reunion (row 189) | "
    "[Preface: row 189 skill checkpoint](../preface.md#skill-navigation-row-189) · "
    "[Row 68 → Row 169 taxonomy meta prelude capstone reunion index](../appendix/sources.md#row68-row169-taxonomy-meta-prelude-capstone-reunion-index-row-189) · "
    "[memory sheet row 189 baby picture](../appendix/memory-sheet.md#row-189-baby-picture-row68-row169-taxonomy-meta-prelude-capstone-reunion) · "
    "[prologue row 189 preview row](#prologue-preview-row-189); [prologue row 189 closing stitch](#row-189-closing-stitch); "
    "[epilogue row 189 closing loop](../epilogue/multiscale.md#row-189-closing-loop) — "
    "read row 68 gate + row 188 or row 169 midpoint meta prelude capstone / taxonomy meta prelude gate + VII.0 Bridge → opening hinge → VII.1 taxonomy + row 49 meta aloud "
    "when forest landing is clean on the full capstone path but Burgers circuits feel like Defects Notes homework after verified midpoint meta prelude capstone on the full capstone path |\n"
)

_prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
PROLOGUE_STITCH = bump169_to_189(
    "**Row 169 closing stitch (Row 68 → Row 149 Row 68 → Row 49 taxonomy meta prelude capstone reunion).** {#row-169-closing-stitch} "
    + _prologue.split("**Row 169 closing stitch")[1].split("**Row 170 closing stitch")[0].lstrip()
    .split("\n\n")[0]
    + "\n\n"
)

PROLOGUE_PREVIEW = (
    '| <span id="prologue-preview-row-189"></span>Row 189 preview (Row 68 → Row 169 Row 68 → Row 49 taxonomy meta prelude capstone reunion) | '
    "Explain why midpoint closure (row 68) and VII.0 → VII.1 meta (row 49) must be read together with the Bridge → Burgers taxonomy chain after verified midpoint meta prelude capstone on the full capstone path before forest landing and dimension tables feel like separate courses | "
    'One sentence: "read row 68 gate + row 188 or row 169 midpoint meta prelude capstone / taxonomy meta prelude gate + VII.0 Bridge → opening hinge → VII.1 taxonomy + row 49 meta aloud when forest landing is clean on the full capstone path but Burgers circuits feel like Defects Notes homework after verified midpoint meta prelude capstone on the full capstone path" — '
    "[preface row 189 skill checkpoint](../preface.md#skill-navigation-row-189); [prologue row 189 closing stitch](#row-189-closing-stitch); "
    "[Row 68 → Row 169 reunion index](../appendix/sources.md#row68-row169-taxonomy-meta-prelude-capstone-reunion-index-row-189); "
    "[memory sheet row 189 baby picture](../appendix/memory-sheet.md#row-189-baby-picture-row68-row169-taxonomy-meta-prelude-capstone-reunion); "
    "[VII.0 Bridge](../part07-defects/00-opening.md#bridge); "
    "[VII.0 opening hinge to VII.1](../part07-defects/00-opening.md#opening-hinge-vii0-to-vii1); "
    "[preface row 49 skill checkpoint](../preface.md#skill-navigation-row-49); "
    "[preface row 188 skill checkpoint](../preface.md#skill-navigation-row-188); "
    "[epilogue row 189 closing loop](../epilogue/multiscale.md#row-189-closing-loop) |\n"
)

_epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
EPILOGUE_LOOP = bump169_to_189(
    "### Row 169 closing loop"
    + _epilogue.split("### Row 169 closing loop")[1].split("### Row 170 closing loop")[0]
)

SOURCES_TABLE = (
    "| 189 | Row 68 → Row 169 Row 68 → Row 49 taxonomy meta prelude capstone (midpoint prelude gate ↔ midpoint meta prelude capstone on full capstone path ↔ row 49 meta) | "
    "[Row 68 → Row 169 taxonomy meta prelude capstone reunion index](#row68-row169-taxonomy-meta-prelude-capstone-reunion-index-row-189) · "
    "[preface row 189](../preface.md#skill-navigation-row-189) · "
    "[prologue row 189 preview](../prologue/00-many-scales.md#prologue-preview-row-189) · "
    "[prologue row 189 closing stitch](../prologue/00-many-scales.md#row-189-closing-stitch) · "
    "[epilogue row 189 closing loop](../epilogue/multiscale.md#row-189-closing-loop) · "
    "[memory sheet row 189 baby picture](memory-sheet.md#row-189-baby-picture-row68-row169-taxonomy-meta-prelude-capstone-reunion) | "
    "Row 68 closed but **row 49 VII.0 → VII.1 opening hinge still feels disconnected from verified midpoint meta prelude capstone on the full capstone path** — "
    "read row 68 + row 188 or row 169 gate + VII.0 Bridge → opening hinge → VII.1 taxonomy + row 49; "
    "[preface row 49](../preface.md#skill-navigation-row-49) |\n"
)

SOURCES_INDEX = bump169_to_189(
    (ROOT / "writings/appendix/chapters/sources.md")
    .read_text()
    .split("## Row 68 → Row 149 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 169)")[1]
    .split("## Row 68 → Row 150 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 170)")[0]
)
SOURCES_INDEX = (
    "## Row 68 → Row 169 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 189)"
    + SOURCES_INDEX
)

MEMORY_TABLE = (
    "| 189 | Meta | [Row 68 → Row 169 taxonomy meta prelude capstone reunion index](sources.md#row68-row169-taxonomy-meta-prelude-capstone-reunion-index-row-189) · "
    "[preface row 189 skill checkpoint](../preface.md#skill-navigation-row-189) · "
    "[prologue row 189 preview](../prologue/00-many-scales.md#prologue-preview-row-189) · "
    "[prologue row 189 closing stitch](../prologue/00-many-scales.md#row-189-closing-stitch) · "
    "[epilogue row 189 closing loop](../epilogue/multiscale.md#row-189-closing-loop) | "
    "Row 68 closed but row 49 taxonomy meta reunion feels disconnected from verified midpoint meta prelude capstone on the full capstone path — "
    "read row 68 + row 188 or row 169 gate + VII.0 Bridge → opening hinge → VII.1 taxonomy + row 49; "
    "[row 189 baby picture](#row-189-baby-picture-row68-row169-taxonomy-meta-prelude-capstone-reunion) |\n"
)

MEMORY_BABY = bump169_to_189(
    (ROOT / "writings/appendix/chapters/memory-sheet.md")
    .read_text()
    .split("### Row 169 baby picture")[1]
    .split("### Row 170 baby picture")[0]
)
MEMORY_BABY = (
    "### Row 189 baby picture"
    + MEMORY_BABY.split(")", 1)[1]
    if ")" in MEMORY_BABY
    else "### Row 189 baby picture" + MEMORY_BABY
)

ROW188_TAIL_MARKER = "**When to pause.** Read the [prologue row 188 closing stitch]"
ROW188_TAIL_END = "or extend prose only under `writings/` then sync.\n\n\n\n\n## The copper wire through the book"

ROW188_STITCH_OLD = (
    "before row 169 taxonomy meta prelude capstone reunion opens on the full capstone path."
)
ROW188_STITCH_NEW = (
    "before row 189 taxonomy meta prelude capstone reunion opens on the full capstone path."
)

ROW188_EPILOGUE_PROCEED_OLD = (
    "Proceed to [row 169](#row-169-closing-loop) when row 68 closed but taxonomy meta prelude capstone still lags after row 168 on the full capstone path,"
)
ROW188_EPILOGUE_PROCEED_NEW = (
    "Proceed to [row 189](#row-189-closing-loop) when row 68 closed but taxonomy meta prelude capstone still lags after row 188 on the full capstone path,"
)

ROW188_BABY_OLD = (
    "row 168 when **VI.4 intermission and Row 67 → Row 48 meta must read on the same wire before row 169 taxonomy meta prelude capstone opens on the full capstone path**"
)
ROW188_BABY_NEW = (
    "row 188 when **VI.4 intermission and Row 67 → Row 48 meta must read on the same wire before row 189 taxonomy meta prelude capstone opens on the full capstone path**"
)

ROW188_TAIL_OLD = (
    "When row 188 is complete, proceed to [row 189](preface.md#skill-navigation-row-189) when midpoint meta prelude capstone is clean but taxonomy meta prelude capstone still lags after verified forest landing on the full capstone path, to [row 129](preface.md#skill-navigation-row-129) when midpoint meta prelude capstone is clean but taxonomy meta prelude capstone still lags after verified forest landing on the opening-hinge capstone path alone, to [row 109](preface.md#skill-navigation-row-109) for the Row 68 ↔ Row 49 meta audit on the opening-hinge prelude path alone, to [row 108](preface.md#skill-navigation-row-108) for the Row 68 ↔ Row 48 meta audit on the opening-hinge prelude path alone, to [row 168](preface.md#skill-navigation-row-168) for the Row 68 ↔ Row 48 meta audit on the opening-hinge capstone path alone, to [row 187](preface.md#skill-navigation-row-187) when part-boundary meta prelude capstone still lags after verified Writings canonical meta prelude capstone on the full capstone path, to [row 88](preface.md#skill-navigation-row-88) for the Row 68 ↔ Row 48 opening prelude audit alone, to [row 48](preface.md#skill-navigation-row-48) for the VI.4 → VII.0 meta audit alone, to [row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, or extend prose only under `writings/` then sync."
)
ROW188_TAIL_NEW = (
    "When row 188 is complete, proceed to [row 189](preface.md#skill-navigation-row-189) when midpoint meta prelude capstone is clean but taxonomy meta prelude capstone still lags after verified forest landing on the full capstone path, to [row 149](preface.md#skill-navigation-row-149) when midpoint meta prelude capstone is clean but taxonomy meta prelude capstone still lags after verified forest landing on the opening-hinge capstone path alone, to [row 109](preface.md#skill-navigation-row-109) for the Row 68 ↔ Row 49 meta audit on the opening-hinge prelude path alone, to [row 108](preface.md#skill-navigation-row-108) for the Row 68 ↔ Row 48 meta audit on the opening-hinge prelude path alone, to [row 168](preface.md#skill-navigation-row-168) for the Row 68 ↔ Row 48 meta audit on the opening-hinge capstone path alone, to [row 187](preface.md#skill-navigation-row-187) when part-boundary meta prelude capstone still lags after verified Writings canonical meta prelude capstone on the full capstone path, to [row 88](preface.md#skill-navigation-row-88) for the Row 68 ↔ Row 48 opening prelude audit alone, to [row 48](preface.md#skill-navigation-row-48) for the VI.4 → VII.0 meta audit alone, to [row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, or extend prose only under `writings/` then sync."
)


def update_row188_tail(preface: str) -> str:
    start = preface.index(ROW188_TAIL_MARKER)
    end = preface.index(ROW188_TAIL_END)
    block = preface[start:end]
    new_block = block.replace(
        "when opening [row 189](preface.md#skill-navigation-row-189) before row 49 closes on the full capstone path",
        "when opening [row 189](preface.md#skill-navigation-row-189) before row 49 closes on the full capstone path",
    )
    new_block = new_block.replace(ROW188_TAIL_OLD, ROW188_TAIL_NEW)
    return preface[:start] + new_block + preface[end:]


def main() -> None:
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "### Row 189 skill checkpoint" in preface and preface.index("### Row 189 skill checkpoint") < preface.index(copper):
        print("preface: row 189 already present")
    else:
        preface = update_row188_tail(preface)
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + ROW189_PREFACE + copper)
        preface_path.write_text(preface)
        print("preface: added row 189")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-189" not in prologue:
        needle = "| Row 68 → Row 168 Row 68 → Row 48 midpoint meta prelude capstone reunion (row 188) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 188 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + PROLOGUE_COMPASS + prologue[line_end + 1 :]
        stitch_anchor = "**Row 188 closing stitch"
        if stitch_anchor not in prologue:
            stitch_anchor = "**Row 169 closing stitch"
        prologue = prologue.replace(stitch_anchor, PROLOGUE_STITCH + stitch_anchor)
        preview_anchor = '| <span id="prologue-preview-row-188"></span>Row 188 preview'
        if preview_anchor not in prologue:
            preview_anchor = '| <span id="prologue-preview-row-169"></span>Row 169 preview'
        prologue = prologue.replace(preview_anchor, PROLOGUE_PREVIEW + preview_anchor)
        if ROW188_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW188_STITCH_OLD, ROW188_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 189")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "row-189-closing-loop" not in epilogue:
        if ROW188_EPILOGUE_PROCEED_OLD in epilogue:
            epilogue = epilogue.replace(ROW188_EPILOGUE_PROCEED_OLD, ROW188_EPILOGUE_PROCEED_NEW)
        marker = "### Row 186 closing loop (Row 68 → Row 166 Row 68 → Row 66 Writings canonical meta prelude capstone reunion)"
        if marker not in epilogue:
            raise SystemExit("epilogue row 186 insert anchor not found")
        epilogue = epilogue.replace(marker, EPILOGUE_LOOP + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 189")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row169-taxonomy-meta-prelude-capstone-reunion-index-row-189" not in sources:
        sources = sources.replace(
            "| 169 | Row 68 → Row 149 Row 68 → Row 49 taxonomy meta prelude capstone",
            SOURCES_TABLE + "| 169 | Row 68 → Row 149 Row 68 → Row 49 taxonomy meta prelude capstone",
            1,
        )
        sources = sources.replace(
            "## Row 68 → Row 149 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 169)",
            SOURCES_INDEX + "## Row 68 → Row 149 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 169)",
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 189")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-189-baby-picture-row68-row169" not in memory:
        memory = memory.replace(
            "| 188 | Meta | [Row 68 → Row 168 midpoint meta prelude capstone reunion index]",
            MEMORY_TABLE + "| 188 | Meta | [Row 68 → Row 168 midpoint meta prelude capstone reunion index]",
            1,
        )
        memory = memory.replace(
            "### Row 188 baby picture {#row-188-baby-picture-row68-row168-midpoint-meta-prelude-capstone-reunion}",
            MEMORY_BABY + "### Row 188 baby picture {#row-188-baby-picture-row68-row168-midpoint-meta-prelude-capstone-reunion}",
            1,
        )
        memory = memory.replace(ROW188_BABY_OLD, ROW188_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 189")


if __name__ == "__main__":
    main()
