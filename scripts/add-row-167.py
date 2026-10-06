#!/usr/bin/env python3
"""Add row 167 meta-stitch (Row 68 → Row 147 ↔ Row 67 part-boundary meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def t147_to_167(text: str) -> str:
    """Transform row-147 capstone-path meta copy to row 167 (147→167, 127→147 inner, 146→166 gate)."""
    repl = [
        ("Row 68 → Row 127 Row 68 → Row 67", "Row 68 → Row 147 Row 68 → Row 67"),
        (
            "row68-row127-part-boundary-meta-prelude-capstone-reunion-index-row-147",
            "row68-row147-part-boundary-meta-prelude-capstone-reunion-index-row-167",
        ),
        (
            "row-147-baby-picture-row68-row127-part-boundary-meta-prelude-capstone-reunion",
            "row-167-baby-picture-row68-row147-part-boundary-meta-prelude-capstone-reunion",
        ),
        ("skill-navigation-row-147", "skill-navigation-row-167"),
        ("prologue-preview-row-147", "prologue-preview-row-167"),
        ("row-147-closing-stitch", "row-167-closing-stitch"),
        ("row-147-closing-loop", "row-167-closing-loop"),
        ("Row 147 three-way audit", "Row 167 three-way audit"),
        (
            "[row 146](preface.md#skill-navigation-row-146) or [row 127](preface.md#skill-navigation-row-127)",
            "[row 166](preface.md#skill-navigation-row-166) or [row 147](preface.md#skill-navigation-row-147)",
        ),
        (
            "[row 146](preface.md#skill-navigation-row-146) or [Row 68 → Row 107 part-boundary meta prelude capstone reunion index (row 127)](appendix/sources.md#row68-row107-part-boundary-meta-prelude-capstone-reunion-index-row-127)",
            "[row 166](preface.md#skill-navigation-row-166) or [Row 68 → Row 127 part-boundary meta prelude capstone reunion index (row 147)](appendix/sources.md#row68-row127-part-boundary-meta-prelude-capstone-reunion-index-row-147)",
        ),
        (
            "verified Writings canonical meta prelude capstone closure on the full capstone path (row 146)",
            "verified Writings canonical meta prelude capstone closure on the full capstone path (row 166)",
        ),
        (
            "verified Writings canonical meta prelude capstone via [row 145](preface.md#skill-navigation-row-145)",
            "verified Writings canonical meta prelude capstone via [row 165](preface.md#skill-navigation-row-165)",
        ),
        ("on the capstone path", "on the full capstone path"),
        ("(capstone path)", "(full capstone path)"),
        (
            "Row 68 ↔ Row 67 reunion (capstone path)",
            "Row 68 ↔ Row 67 reunion (full capstone path)",
        ),
    ]
    out = text
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace("row 147", "row 167")
    out = out.replace("Row 147", "Row 167")
    out = out.replace("[row 167](preface.md#skill-navigation-row-166)", "[row 166](preface.md#skill-navigation-row-166)")
    out = out.replace("[row 167](preface.md#skill-navigation-row-147)", "[row 147](preface.md#skill-navigation-row-147)")
    out = out.replace("row 1675", "row 168")
    out = out.replace("row 1676", "row 169")
    out = out.replace("row 167 or row 167", "row 166 or row 147")
    out = out.replace("When row 167 closed — Writings", "When row 166 closed — Writings")
    out = out.replace("When row 167 closed — part-boundary", "When row 166 closed — part-boundary")
    out = out.replace("row 167 closed Writings", "row 166 closed Writings")
    out = out.replace("row 167 closed part-boundary", "row 166 closed part-boundary")
    out = out.replace("after row 167 alone", "after row 166 alone")
    out = out.replace("Recite [preface row 167]", "Recite [preface row 166]")
    out = out.replace("row 167 or row 147 recited", "row 166 or row 147 recited")
    out = out.replace("from row 167's", "from row 166's")
    out = out.replace("row 146 closed", "row 166 closed")
    out = out.replace("Row 146 closed", "Row 166 closed")
    out = out.replace("row 145 or row 126 recited", "row 165 or row 146 recited")
    out = out.replace("row 127", "row 147")
    out = out.replace("Row 127", "Row 147")
    out = out.replace("row 146", "row 166")
    out = out.replace("Row 146", "Row 166")
    out = out.replace("row 145", "row 165")
    out = out.replace("Row 145", "Row 165")
    out = out.replace(
        "before row 168 midpoint meta prelude capstone reunion opens on the full capstone path",
        "before row 148 midpoint meta prelude capstone reunion opens on the full capstone path",
    )
    out = out.replace(
        "Proceed to [row 168]",
        "Proceed to [row 148]",
    )
    out = out.replace(
        "Do not conflate row 167 (row 68 ↔ row 67 reunion on the full capstone path) with row 147",
        "Do not conflate row 167 (row 68 ↔ row 67 reunion on the full capstone path) with row 147",
    )
    out = out.replace(
        "row 147 names **Row 68 → Row 107 Row 68 → Row 67 part-boundary meta prelude capstone reunion**",
        "row 147 names **Row 68 → Row 127 Row 68 → Row 67 part-boundary meta prelude capstone reunion**",
    )
    out = out.replace(
        "Row 68 → Row 167 Row 68 → Row 67",
        "Row 68 → Row 147 Row 68 → Row 67",
    )
    out = out.replace("#skill-navigation-row-1675", "#skill-navigation-row-168")
    out = out.replace(
        "row68-row107-part-boundary-meta-prelude-capstone-reunion-index-row-127",
        "row68-row147-part-boundary-meta-prelude-capstone-reunion-index-row-167",
    )
    out = out.replace(
        "row68-row126-writings-meta-prelude-capstone-reunion-index-row-146",
        "row68-row146-writings-meta-prelude-capstone-reunion-index-row-166",
    )
    return out


def extract_preface_row147(preface: str) -> str:
    start = preface.index("### Row 147 skill checkpoint")
    end = preface.index("\n\n### Row 148 skill checkpoint")
    return preface[start:end]


ROW167_PREFACE = t147_to_167(
    extract_preface_row147((ROOT / "writings/preface/chapters/preface.md").read_text())
) + "\n\n"

PROLOGUE_COMPASS = (
    "| Row 68 → Row 147 Row 68 → Row 67 part-boundary meta prelude capstone reunion (row 167) | "
    "[Preface: row 167 skill checkpoint](../preface.md#skill-navigation-row-167) · "
    "[Row 68 → Row 147 part-boundary meta prelude capstone reunion index](../appendix/sources.md#row68-row147-part-boundary-meta-prelude-capstone-reunion-index-row-167) · "
    "[memory sheet row 167 baby picture](../appendix/memory-sheet.md#row-167-baby-picture-row68-row147-part-boundary-meta-prelude-capstone-reunion) · "
    "[prologue row 167 preview row](#prologue-preview-row-167); [prologue row 167 closing stitch](#row-167-closing-stitch); "
    "[epilogue row 167 closing loop](../epilogue/multiscale.md#row-167-closing-loop) — "
    "read row 68 gate + row 166 or row 147 Writings canonical meta prelude capstone / part-boundary meta prelude gate + V.4 Bridge → VI.0 twin-ladder landing + row 67 meta aloud "
    "when canonical tree is clean on the full capstone path but writings/fvm → writings/continuum feels like two courses after verified Writings meta prelude capstone on the full capstone path |\n"
)

PROLOGUE_STITCH = t147_to_167(
    "**Row 147 closing stitch (Row 68 → Row 127 Row 68 → Row 67 part-boundary meta prelude capstone reunion).** {#row-147-closing-stitch} "
    "When row 146 closed — Writings canonical meta prelude capstone verified on the full capstone path, row 145 or row 126 recited, and `./scripts/sync-writings.sh --check` green with prose under `writings/` only — "
    "but **row 67 part-boundary meta reunion still opens like standalone elasticity coursework after Navier–Stokes on the full capstone path** — "
    "`writings/fvm` closes and `writings/continuum` opens like separate mdBooks, Galerkin assembly and face fluxes feel unrelated to Cauchy stress, or row 47's twin-ladder audit feels disconnected from row 146's canonical-tree closure while the unified HTML reads smoothly — "
    "read [preface row 147](../preface.md#skill-navigation-row-147), then the "
    "[Row 68 → Row 127 reunion index](../appendix/sources.md#row68-row127-part-boundary-meta-prelude-capstone-reunion-index-row-147), then "
    "[epilogue row 147 closing loop](../epilogue/multiscale.md#row-147-closing-loop) before row 148 midpoint meta prelude capstone reunion opens on the full capstone path.\n\n"
)

PROLOGUE_PREVIEW = (
    "| <span id=\"prologue-preview-row-167\"></span>Row 167 preview (Row 68 → Row 147 Row 68 → Row 67 part-boundary meta prelude capstone reunion) | "
    "Explain why midpoint closure (row 68) and part-boundary meta (row 67) must be read together with the V.4 → VI.0 twin-ladder Bridge chain after verified Writings canonical meta prelude capstone on the full capstone path before canonical sync and fvm → continuum subtrees feel like separate courses | "
    "One sentence: \"read row 68 gate + row 166 or row 147 Writings canonical meta prelude capstone / part-boundary meta prelude gate + V.4 Bridge → VI.0 twin-ladder landing + row 67 meta aloud when canonical tree is clean on the full capstone path but writings/fvm → writings/continuum feels like two courses after verified Writings meta prelude capstone on the full capstone path\" — "
    "[preface row 167 skill checkpoint](../preface.md#skill-navigation-row-167); [prologue row 167 closing stitch](#row-167-closing-stitch); "
    "[Row 68 → Row 147 reunion index](../appendix/sources.md#row68-row147-part-boundary-meta-prelude-capstone-reunion-index-row-167); "
    "[memory sheet row 167 baby picture](../appendix/memory-sheet.md#row-167-baby-picture-row68-row147-part-boundary-meta-prelude-capstone-reunion); "
    "[V.4 Bridge](../part05-fvm/04-navier-stokes-cfd.md#bridge-to-part-vi); "
    "[preface row 67 skill checkpoint](../preface.md#skill-navigation-row-67); "
    "[preface row 166 skill checkpoint](../preface.md#skill-navigation-row-166); "
    "[epilogue row 167 closing loop](../epilogue/multiscale.md#row-167-closing-loop) |\n"
)

_epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
EPILOGUE_LOOP = t147_to_167(
    "### Row 147 closing loop"
    + _epilogue.split("### Row 147 closing loop")[1].split("### Row 148 closing loop")[0]
)

SOURCES_TABLE = (
    "| 167 | Row 68 → Row 147 Row 68 → Row 67 part-boundary meta prelude capstone (midpoint prelude gate ↔ Writings canonical meta prelude capstone on full capstone path ↔ row 67 meta) | "
    "[Row 68 → Row 147 part-boundary meta prelude capstone reunion index](#row68-row147-part-boundary-meta-prelude-capstone-reunion-index-row-167) · "
    "[preface row 167](../preface.md#skill-navigation-row-167) · "
    "[prologue row 167 preview](../prologue/00-many-scales.md#prologue-preview-row-167) · "
    "[prologue row 167 closing stitch](../prologue/00-many-scales.md#row-167-closing-stitch) · "
    "[epilogue row 167 closing loop](../epilogue/multiscale.md#row-167-closing-loop) · "
    "[memory sheet row 167 baby picture](memory-sheet.md#row-167-baby-picture-row68-row147-part-boundary-meta-prelude-capstone-reunion) | "
    "Row 68 closed but **row 67 part-boundary meta reunion still feels disconnected from verified Writings canonical meta prelude capstone on the full capstone path** — "
    "read row 68 + row 166 or row 147 gate + V.4 Bridge → VI.0 twin-ladder + row 67; "
    "[preface row 67](../preface.md#skill-navigation-row-67) |\n"
)

SOURCES_INDEX = t147_to_167(
    (ROOT / "writings/appendix/chapters/sources.md")
    .read_text()
    .split("## Row 68 → Row 127 Row 68 → Row 67 part-boundary meta prelude capstone reunion index (row 147)")[1]
    .split("## Row 68 → Row 128 Row 68 → Row 48 midpoint meta prelude capstone reunion index (row 148)")[0]
)
SOURCES_INDEX = (
    "## Row 68 → Row 147 Row 68 → Row 67 part-boundary meta prelude capstone reunion index (row 167)"
    + SOURCES_INDEX
)

MEMORY_TABLE = (
    "| 167 | Meta | [Row 68 → Row 147 part-boundary meta prelude capstone reunion index](sources.md#row68-row147-part-boundary-meta-prelude-capstone-reunion-index-row-167) · "
    "[preface row 167 skill checkpoint](../preface.md#skill-navigation-row-167) · "
    "[prologue row 167 preview](../prologue/00-many-scales.md#prologue-preview-row-167) · "
    "[prologue row 167 closing stitch](../prologue/00-many-scales.md#row-167-closing-stitch) · "
    "[epilogue row 167 closing loop](../epilogue/multiscale.md#row-167-closing-loop) | "
    "Row 68 closed but row 67 part-boundary meta reunion feels disconnected from verified Writings canonical meta prelude capstone on the full capstone path — "
    "read row 68 + row 166 or row 147 gate + V.4 Bridge → VI.0 twin-ladder + row 67; "
    "[row 167 baby picture](#row-167-baby-picture-row68-row147-part-boundary-meta-prelude-capstone-reunion) |\n"
)

MEMORY_BABY = t147_to_167(
    (ROOT / "writings/appendix/chapters/memory-sheet.md")
    .read_text()
    .split("### Row 147 baby picture")[1]
    .split("### Row 148 baby picture")[0]
)
MEMORY_BABY = "### Row 167 baby picture" + MEMORY_BABY.split(")", 1)[1] if ")" in MEMORY_BABY else "### Row 167 baby picture" + MEMORY_BABY

ROW166_TAIL_MARKER = "**When to pause.** Read the [prologue row 166 closing stitch]"
ROW166_TAIL_END = "or extend prose only under `writings/` then sync.\n\n\n\n## The copper wire through the book"

ROW166_STITCH_OLD = (
    "before row 167 part-boundary meta prelude capstone reunion opens on the full capstone path "
    "(then row 148 midpoint meta prelude capstone on the full capstone path)."
)
ROW166_STITCH_NEW = (
    "before row 167 part-boundary meta prelude capstone reunion opens on the full capstone path "
    "(then row 168 midpoint meta prelude capstone reunion on the full capstone path)."
)

ROW166_EPILOGUE_PROCEED_OLD = (
    "Proceed to [row 147](#row-147-closing-loop) when row 68 closed but part-boundary meta prelude capstone still lags after row 166 on the full capstone path,"
)
ROW166_EPILOGUE_PROCEED_NEW = (
    "Proceed to [row 167](#row-167-closing-loop) when row 68 closed but part-boundary meta prelude capstone still lags after row 166 on the full capstone path,"
)

ROW166_BABY_OLD = (
    "row 166 when **epilogue writings cross-links and Row 65 → Row 46 meta must read on the same wire before row 147 part-boundary meta prelude capstone reunion opens on the full capstone path**"
)
ROW166_BABY_NEW = (
    "row 166 when **epilogue writings cross-links and Row 65 → Row 46 meta must read on the same wire before row 167 part-boundary meta prelude capstone reunion opens on the full capstone path**"
)


def update_row166_tail(preface: str) -> str:
    start = preface.index(ROW166_TAIL_MARKER)
    end = preface.index(ROW166_TAIL_END)
    block = preface[start:end]
    new_block = block.replace(
        "when opening [row 147](preface.md#skill-navigation-row-147) before row 67 closes on the full capstone path",
        "when opening [row 167](preface.md#skill-navigation-row-167) before row 67 closes on the full capstone path",
    )
    new_block = new_block.replace(
        "When row 166 is complete, proceed to [row 147](preface.md#skill-navigation-row-147) when row 68 closed but part-boundary meta prelude capstone still lags after verified Writings canonical meta prelude capstone on the full capstone path, to [row 127](preface.md#skill-navigation-row-127) when row 68 closed but part-boundary meta prelude capstone still lags after verified Writings canonical meta prelude capstone on the opening-hinge capstone path alone, to [row 107](preface.md#skill-navigation-row-107) when sync is clean but part-boundary meta capstone still lags after verified Writings canonical meta on the opening-hinge path, to [row 146](preface.md#skill-navigation-row-126) for the Row 68 ↔ Row 66 meta audit on the opening-hinge capstone path alone, to [row 165](preface.md#skill-navigation-row-145) when second-pass meta prelude capstone still lags after verified book-loop meta prelude capstone on the full capstone path, to [row 86](preface.md#skill-navigation-row-86) for the Row 68 ↔ Row 66 opening prelude audit alone, to [row 66](preface.md#skill-navigation-row-66) for the Row 65 ↔ Row 46 meta audit alone, to [row 46](preface.md#skill-navigation-row-46) for the Rows 17–45 → Writings meta audit alone, or extend prose only under `writings/` then sync.",
        "When row 166 is complete, proceed to [row 167](preface.md#skill-navigation-row-167) when row 68 closed but part-boundary meta prelude capstone still lags after verified Writings canonical meta prelude capstone on the full capstone path, to [row 147](preface.md#skill-navigation-row-147) when row 68 closed but part-boundary meta prelude capstone still lags after verified Writings canonical meta prelude capstone on the opening-hinge capstone path alone, to [row 107](preface.md#skill-navigation-row-107) when sync is clean but part-boundary meta capstone still lags after verified Writings canonical meta on the opening-hinge path, to [row 166](preface.md#skill-navigation-row-146) for the Row 68 ↔ Row 66 meta audit on the opening-hinge capstone path alone, to [row 165](preface.md#skill-navigation-row-165) when second-pass meta prelude capstone still lags after verified book-loop meta prelude capstone on the full capstone path, to [row 86](preface.md#skill-navigation-row-86) for the Row 68 ↔ Row 66 opening prelude audit alone, to [row 66](preface.md#skill-navigation-row-66) for the Row 65 ↔ Row 46 meta audit alone, to [row 46](preface.md#skill-navigation-row-46) for the Rows 17–45 → Writings meta audit alone, or extend prose only under `writings/` then sync.",
    )
    return preface[:start] + new_block + preface[end:]


def main():
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "skill-navigation-row-167" in preface and preface.index("skill-navigation-row-167") < preface.index(copper):
        print("preface: row 167 already present")
    else:
        preface = update_row166_tail(preface)
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + ROW167_PREFACE + copper)
        preface_path.write_text(preface)
        print("preface: added row 167")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-167" not in prologue:
        needle = "| Row 68 → Row 146 Row 68 → Row 66 Writings canonical meta prelude capstone reunion (row 166) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 166 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + PROLOGUE_COMPASS + prologue[line_end + 1 :]
        prologue = prologue.replace(
            "**Row 166 closing stitch",
            PROLOGUE_STITCH + "**Row 166 closing stitch",
        )
        prologue = prologue.replace(
            '| <span id="prologue-preview-row-166"></span>Row 166 preview',
            PROLOGUE_PREVIEW + '| <span id="prologue-preview-row-166"></span>Row 166 preview',
        )
        if ROW166_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW166_STITCH_OLD, ROW166_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 167")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "row-167-closing-loop" not in epilogue:
        if ROW166_EPILOGUE_PROCEED_OLD in epilogue:
            epilogue = epilogue.replace(ROW166_EPILOGUE_PROCEED_OLD, ROW166_EPILOGUE_PROCEED_NEW)
        marker = (
            "to [row 66](#row-66-closing-loop) when only Writings prelude meta stalls, or extend prose only under `writings/` then sync.\n\n\n\n\n\n\n\n### Row 135 closing loop"
        )
        replacement = (
            "to [row 66](#row-66-closing-loop) when only Writings prelude meta stalls, or extend prose only under `writings/` then sync.\n\n\n"
            + EPILOGUE_LOOP
            + "\n\n\n\n\n### Row 135 closing loop"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 166 end marker not found")
        epilogue = epilogue.replace(marker, replacement, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 167")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row147-part-boundary-meta-prelude-capstone-reunion-index-row-167" not in sources:
        sources = sources.replace(
            "| 147 | Row 68 → Row 127 Row 68 → Row 67 part-boundary meta prelude capstone",
            SOURCES_TABLE + "| 147 | Row 68 → Row 127 Row 68 → Row 67 part-boundary meta prelude capstone",
        )
        sources = sources.replace(
            "## Row 68 → Row 127 Row 68 → Row 67 part-boundary meta prelude capstone reunion index (row 147)",
            SOURCES_INDEX + "## Row 68 → Row 127 Row 68 → Row 67 part-boundary meta prelude capstone reunion index (row 147)",
        )
        sources_path.write_text(sources)
        print("sources: added row 167")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-167-baby-picture-row68-row147" not in memory:
        memory = memory.replace(
            "| 166 | Meta | [Row 68 → Row 146 Writings canonical meta prelude capstone reunion index]",
            MEMORY_TABLE + "| 166 | Meta | [Row 68 → Row 146 Writings canonical meta prelude capstone reunion index]",
        )
        memory = memory.replace(
            "### Row 166 baby picture {#row-166-baby-picture-row68-row146-writings-meta-prelude-capstone-reunion}",
            MEMORY_BABY + "### Row 166 baby picture {#row-166-baby-picture-row68-row146-writings-meta-prelude-capstone-reunion}",
        )
        memory = memory.replace(ROW166_BABY_OLD, ROW166_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 167")


if __name__ == "__main__":
    main()
