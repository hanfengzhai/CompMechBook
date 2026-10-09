#!/usr/bin/env python3
"""Add row 166 meta-stitch (Row 68 → Row 146 ↔ Row 66 Writings canonical meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def t146_to_166(text: str) -> str:
    """Transform row-146 capstone-path meta copy to row 166 (146→166, 126→146 inner, 145→165 gate)."""
    repl = [
        ("Row 68 → Row 126 Row 68 → Row 66", "Row 68 → Row 146 Row 68 → Row 66"),
        (
            "row68-row126-writings-meta-prelude-capstone-reunion-index-row-146",
            "row68-row146-writings-meta-prelude-capstone-reunion-index-row-166",
        ),
        (
            "row-146-baby-picture-row68-row126-writings-meta-prelude-capstone-reunion",
            "row-166-baby-picture-row68-row146-writings-meta-prelude-capstone-reunion",
        ),
        ("skill-navigation-row-146", "skill-navigation-row-166"),
        ("prologue-preview-row-146", "prologue-preview-row-166"),
        ("row-146-closing-stitch", "row-166-closing-stitch"),
        ("row-146-closing-loop", "row-166-closing-loop"),
        ("Row 146 three-way audit", "Row 166 three-way audit"),
        (
            "[row 145](preface.md#skill-navigation-row-145) or [row 126](preface.md#skill-navigation-row-126)",
            "[row 165](preface.md#skill-navigation-row-165) or [row 146](preface.md#skill-navigation-row-146)",
        ),
        (
            "[Row 68 → Row 106 Writings meta prelude reunion index (row 126)](appendix/sources.md#row68-row106-writings-meta-prelude-capstone-reunion-index-row-126)",
            "[Row 68 → Row 126 Writings canonical meta prelude capstone reunion index (row 146)](appendix/sources.md#row68-row126-writings-meta-prelude-capstone-reunion-index-row-146)",
        ),
        (
            "[row 144](preface.md#skill-navigation-row-144)",
            "[row 164](preface.md#skill-navigation-row-164)",
        ),
        ("on the capstone path", "on the full capstone path"),
        ("(capstone path)", "(full capstone path)"),
        ("Row 68 ↔ Row 66 reunion (capstone path)", "Row 68 ↔ Row 66 reunion (full capstone path)"),
    ]
    out = text
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace("row 146", "row 166")
    out = out.replace("Row 146", "Row 166")
    out = out.replace("[row 166](preface.md#skill-navigation-row-164)", "[row 164](preface.md#skill-navigation-row-164)")
    out = out.replace("[row 166](preface.md#skill-navigation-row-146)", "[row 146](preface.md#skill-navigation-row-146)")
    out = out.replace("row 1665", "row 167")
    out = out.replace("row 1666", "row 168")
    out = out.replace("row 166 or row 166", "row 165 or row 146")
    out = out.replace("When row 166 closed — second-pass", "When row 165 closed — second-pass")
    out = out.replace("When row 166 closed — Writings", "When row 165 closed — Writings")
    out = out.replace("row 166 closed second-pass", "row 165 closed second-pass")
    out = out.replace("row 166 closed Writings", "row 165 closed Writings")
    out = out.replace("after row 166 alone", "after row 165 alone")
    out = out.replace("Recite [preface row 166]", "Recite [preface row 165]")
    out = out.replace("row 166 or row 146 recited", "row 165 or row 146 recited")
    out = out.replace("from row 166's", "from row 165's")
    out = out.replace(
        "verified second-pass meta prelude capstone closure on the full capstone path (row 166)",
        "verified second-pass meta prelude capstone closure on the full capstone path (row 165)",
    )
    out = out.replace(
        "verified second-pass meta prelude capstone closure on the full capstone path (row 145)",
        "verified second-pass meta prelude capstone closure on the full capstone path (row 165)",
    )
    out = out.replace("row 126", "row 146")
    out = out.replace("Row 126", "Row 146")
    out = out.replace("row 145", "row 165")
    out = out.replace("Row 145", "Row 165")
    out = out.replace(
        "before row 167 part-boundary meta prelude capstone reunion opens on the full capstone path",
        "before row 147 part-boundary meta prelude capstone reunion opens on the full capstone path",
    )
    out = out.replace(
        "Proceed to [row 167]",
        "Proceed to [row 147]",
    )
    out = out.replace(
        "Do not conflate row 166 (row 68 ↔ row 66 reunion on the full capstone path) with row 146",
        "Do not conflate row 166 (row 68 ↔ row 66 reunion on the full capstone path) with row 146",
    )
    out = out.replace(
        "row 146 names **Row 68 → Row 106 Row 68 → Row 66 Writings canonical meta prelude capstone reunion**",
        "row 146 names **Row 68 → Row 126 Row 68 → Row 66 Writings canonical meta prelude capstone reunion**",
    )
    out = out.replace(
        "Row 68 → Row 166 Row 68 → Row 66",
        "Row 68 → Row 146 Row 68 → Row 66",
    )
    out = out.replace("#skill-navigation-row-1665", "#skill-navigation-row-167")
    out = out.replace("#skill-navigation-row-147)", "#skill-navigation-row-147)")
    out = out.replace(
        "row68-row106-writings-meta-prelude-capstone-reunion-index-row-126",
        "row68-row146-writings-meta-prelude-capstone-reunion-index-row-166",
    )
    out = out.replace(
        "row68-row125-second-pass-meta-prelude-capstone-reunion-index-row-145",
        "row68-row145-second-pass-meta-prelude-capstone-reunion-index-row-165",
    )
    return out


def extract_preface_row146(preface: str) -> str:
    start = preface.index("### Row 146 skill checkpoint")
    end = preface.index("\n\n### Row 147 skill checkpoint")
    return preface[start:end]


ROW166_PREFACE = t146_to_166(
    extract_preface_row146((ROOT / "writings/preface/chapters/preface.md").read_text())
) + "\n\n"

PROLOGUE_COMPASS = (
    "| Row 68 → Row 146 Row 68 → Row 66 Writings canonical meta prelude capstone reunion (row 166) | "
    "[Preface: row 166 skill checkpoint](../preface.md#skill-navigation-row-166) · "
    "[Row 68 → Row 146 Writings canonical meta prelude capstone reunion index](../appendix/sources.md#row68-row146-writings-meta-prelude-capstone-reunion-index-row-166) · "
    "[memory sheet row 166 baby picture](../appendix/memory-sheet.md#row-166-baby-picture-row68-row146-writings-meta-prelude-capstone-reunion) · "
    "[prologue row 166 preview row](#prologue-preview-row-166); [prologue row 166 closing stitch](#row-166-closing-stitch); "
    "[epilogue row 166 closing loop](../epilogue/multiscale.md#row-166-closing-loop) — "
    "read row 68 gate + row 165 or row 146 second-pass meta prelude capstone / Writings canonical meta prelude gate + epilogue writings cross-links + row 66 meta aloud "
    "when second pass reads as a novel on the full capstone path after verified book-loop meta prelude capstone but the next edit opens src/part* instead of writings/ |\n"
)

PROLOGUE_STITCH = t146_to_166(
    "**Row 146 closing stitch (Row 68 → Row 126 Row 68 → Row 66 Writings canonical meta prelude capstone reunion).** {#row-146-closing-stitch} "
    "When row 145 closed — second-pass meta prelude capstone verified on the full capstone path, row 144 or row 125 recited, and Scene → Bridge rhythm trusted after verified book-loop meta prelude capstone on the capstone path — "
    "but **row 66 Writings canonical meta reunion still opens like standalone maintainer coursework after the Writings canonical opening prelude chapter hinge on the capstone path** — "
    "`./scripts/sync-writings.sh --check` fails, the next prose edit opens `src/part*` instead of `writings/<part>/chapters/`, or the [epilogue Writings canonical cross-links audit](../epilogue/multiscale.md#opening-hinge-rows17-45-writings) feels like a build appendix beside row 46's meta audit while the unified HTML reads smoothly — "
    "read [preface row 146](../preface.md#skill-navigation-row-146), then the "
    "[Row 68 → Row 126 reunion index](../appendix/sources.md#row68-row126-writings-meta-prelude-capstone-reunion-index-row-146), then "
    "[epilogue row 146 closing loop](../epilogue/multiscale.md#row-146-closing-loop) before row 147 part-boundary meta prelude capstone reunion opens on the full capstone path.\n\n"
)

PROLOGUE_PREVIEW = (
    "| <span id=\"prologue-preview-row-166\"></span>Row 166 preview (Row 68 → Row 146 Row 68 → Row 66 Writings canonical meta prelude capstone reunion) | "
    "Explain why midpoint closure (row 68) and Writings canonical meta (row 66) must be read together with the epilogue writings cross-links and sync discipline "
    "after verified second-pass meta prelude capstone on the full capstone path before novel rhythm and canonical source tree feel like separate courses | "
    "One sentence: \"read row 68 gate + row 165 or row 146 second-pass meta prelude capstone / Writings canonical meta prelude gate + epilogue writings cross-links + row 66 meta aloud "
    "when second pass reads as a novel on the full capstone path after verified book-loop meta prelude capstone but the next edit opens src/part* instead of writings/\" — "
    "[preface row 166 skill checkpoint](../preface.md#skill-navigation-row-166); [prologue row 166 closing stitch](#row-166-closing-stitch); "
    "[Row 68 → Row 146 reunion index](../appendix/sources.md#row68-row146-writings-meta-prelude-capstone-reunion-index-row-166); "
    "[memory sheet row 166 baby picture](../appendix/memory-sheet.md#row-166-baby-picture-row68-row146-writings-meta-prelude-capstone-reunion); "
    "[epilogue Writings canonical cross-links audit](../epilogue/multiscale.md#opening-hinge-rows17-45-writings); "
    "[preface row 66 skill checkpoint](../preface.md#skill-navigation-row-66); "
    "[preface row 165 skill checkpoint](../preface.md#skill-navigation-row-165); "
    "[epilogue row 166 closing loop](../epilogue/multiscale.md#row-166-closing-loop) |\n"
)

_epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
EPILOGUE_LOOP = t146_to_166(
    "### Row 146 closing loop"
    + _epilogue.split("### Row 146 closing loop")[1].split("### Row 147 closing loop")[0]
)

SOURCES_TABLE = (
    "| 166 | Row 68 → Row 146 Row 68 → Row 66 Writings canonical meta prelude capstone (midpoint prelude gate ↔ second-pass meta prelude capstone on full capstone path ↔ row 66 meta) | "
    "[Row 68 → Row 146 Writings canonical meta prelude capstone reunion index](#row68-row146-writings-meta-prelude-capstone-reunion-index-row-166) · "
    "[preface row 166](../preface.md#skill-navigation-row-166) · "
    "[prologue row 166 preview](../prologue/00-many-scales.md#prologue-preview-row-166) · "
    "[prologue row 166 closing stitch](../prologue/00-many-scales.md#row-166-closing-stitch) · "
    "[epilogue row 166 closing loop](../epilogue/multiscale.md#row-166-closing-loop) · "
    "[memory sheet row 166 baby picture](memory-sheet.md#row-166-baby-picture-row68-row146-writings-meta-prelude-capstone-reunion) | "
    "Row 68 closed but **row 66 Writings canonical meta reunion still feels disconnected from verified second-pass meta prelude capstone on the full capstone path** — "
    "read row 68 + row 165 or row 146 gate + epilogue writings cross-links + row 66; "
    "[preface row 66](../preface.md#skill-navigation-row-66) |\n"
)

SOURCES_INDEX = t146_to_166(
    (ROOT / "writings/appendix/chapters/sources.md")
    .read_text()
    .split("## Row 68 → Row 126 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 146)")[1]
    .split("## Row 68 → Row 127 Row 68 → Row 67 part-boundary meta prelude capstone reunion index (row 147)")[0]
)
SOURCES_INDEX = (
    "## Row 68 → Row 146 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 166)"
    + SOURCES_INDEX
)

MEMORY_TABLE = (
    "| 166 | Meta | [Row 68 → Row 146 Writings canonical meta prelude capstone reunion index](sources.md#row68-row146-writings-meta-prelude-capstone-reunion-index-row-166) · "
    "[preface row 166 skill checkpoint](../preface.md#skill-navigation-row-166) · "
    "[prologue row 166 preview](../prologue/00-many-scales.md#prologue-preview-row-166) · "
    "[prologue row 166 closing stitch](../prologue/00-many-scales.md#row-166-closing-stitch) · "
    "[epilogue row 166 closing loop](../epilogue/multiscale.md#row-166-closing-loop) | "
    "Row 68 closed but row 66 Writings canonical meta reunion feels disconnected from verified second-pass meta prelude capstone on the full capstone path — "
    "read row 68 + row 165 or row 146 gate + epilogue writings cross-links + row 66; "
    "[row 166 baby picture](#row-166-baby-picture-row68-row146-writings-meta-prelude-capstone-reunion) |\n"
)

MEMORY_BABY = t146_to_166(
    (ROOT / "writings/appendix/chapters/memory-sheet.md")
    .read_text()
    .split("### Row 146 baby picture")[1]
    .split("### Row 147 baby picture")[0]
)
MEMORY_BABY = "### Row 166 baby picture" + MEMORY_BABY.split(")", 1)[1] if ")" in MEMORY_BABY else "### Row 166 baby picture" + MEMORY_BABY

ROW165_TAIL_MARKER = "**When to pause.** Read the [prologue row 165 closing stitch]"
ROW165_TAIL_END = "or extend prose only under `writings/` then sync.\n\n\n\n## The copper wire through the book"

ROW165_STITCH_OLD = "before row 146 Writings canonical meta prelude capstone opens on the full capstone path."
ROW165_STITCH_NEW = (
    "before row 166 Writings canonical meta prelude capstone reunion on the full capstone path "
    "(then row 147 part-boundary meta prelude capstone on the full capstone path)."
)

ROW165_EPILOGUE_PROCEED_OLD = (
    "Proceed to [row 146](#row-146-closing-loop) when row 68 closed but Writings canonical meta prelude capstone still lags after row 165 on the full capstone path,"
)
ROW165_EPILOGUE_PROCEED_NEW = (
    "Proceed to [row 166](#row-166-closing-loop) when row 68 closed but Writings canonical meta prelude capstone still lags after row 165 on the full capstone path,"
)

ROW165_BABY_OLD = (
    "row 165 when **epilogue second-pass cross-links and Row 63 → Row 44 meta must read on the same wire before row 146 Writings canonical meta prelude capstone reunion opens on the full capstone path**"
)
ROW165_BABY_NEW = (
    "row 165 when **epilogue second-pass cross-links and Row 63 → Row 44 meta must read on the same wire before row 166 Writings canonical meta prelude capstone reunion opens on the full capstone path**"
)

ROW145_STITCH_BROKEN = (
    "**Row 145 closing stitch (Row 68 → Row 125 Row 68 → Row 65 second-pass meta prelude capstone reunion).** {#row-145-closing-stitch}\n"
    "**Row 146 closing stitch"
)
ROW145_STITCH_FIXED = (
    "**Row 145 closing stitch (Row 68 → Row 125 Row 68 → Row 65 second-pass meta prelude capstone reunion).** {#row-145-closing-stitch} "
    "When row 144 closed — book-loop meta prelude capstone verified, row 143 or row 124 recited on the capstone path, and the [prologue reopening anchor](#prologue-reopening-anchor) received the reader with `./scripts/test-fixtures.sh` green after verified orchestration meta prelude capstone on the capstone path — "
    "but **row 65 second-pass meta reunion still opens like standalone appendix coursework after the second-pass opening prelude chapter hinge on the capstone path** — "
    "the [epilogue second-pass cross-links audit](../epilogue/multiscale.md#opening-hinge-rows17-44-row17) lists continuous read-through → row 17 audit → Scene → Bridge rhythm while every chapter boundary still triggers a skill checkpoint instead of trusting Bridges, next-project restart and novel second pass feel like two afternoons on the capstone path, or row 65's five-step audit feels like a duplicate checklist rather than the rear-view mirror of row 144's book-loop meta → reopening anchor → Scene → Bridge novel-rhythm turn at the second-pass meta prelude capstone boundary on the capstone path — "
    "the [preface row 145 When-to-pause opening sentence](../preface.md#skill-navigation-row-145) names the dual reunion before the Writings canonical reunion on the capstone path; read [preface row 145](../preface.md#skill-navigation-row-145), then the "
    "[Row 68 → Row 125 reunion index](../appendix/sources.md#row68-row125-second-pass-meta-prelude-capstone-reunion-index-row-145), then "
    "[epilogue row 145 closing loop](../epilogue/multiscale.md#row-145-closing-loop) before row 146 Writings canonical meta prelude capstone reunion opens on the capstone path.\n\n"
    "**Row 146 closing stitch"
)

ROW145_ORPHAN_PREFIX = (
    "\n When row 144 closed — book-loop meta prelude capstone verified, row 143 or row 124 recited on the capstone path, and the [prologue reopening anchor](#prologue-reopening-anchor) received the reader with `./scripts/test-fixtures.sh` green after verified orchestration meta prelude capstone on the capstone path — but **row 65 second-pass meta reunion still opens like standalone appendix coursework after the second-pass opening prelude chapter hinge on the capstone path** — the [epilogue second-pass cross-links audit](../epilogue/multiscale.md#opening-hinge-rows17-44-row17) lists continuous read-through → row 17 audit → Scene → Bridge rhythm while every chapter boundary still triggers a skill checkpoint instead of trusting Bridges, next-project restart and novel second pass feel like two afternoons on the capstone path, or row 65's five-step audit feels like a duplicate checklist rather than the rear-view mirror of row 144's book-loop meta → reopening anchor → Scene → Bridge novel-rhythm turn at the second-pass meta prelude capstone boundary on the capstone path — the [preface row 145 When-to-pause opening sentence](../preface.md#skill-navigation-row-145) names the dual reunion before the Writings canonical reunion on the capstone path; read [preface row 145](../preface.md#skill-navigation-row-145), then the [Row 68 → Row 125 reunion index](../appendix/sources.md#row68-row125-second-pass-meta-prelude-capstone-reunion-index-row-145), then [epilogue row 145 closing loop](../epilogue/multiscale.md#row-145-closing-loop) before row 146 Writings canonical meta prelude capstone reunion opens on the capstone path.\n\n"
)


def update_row165_tail(preface: str) -> str:
    start = preface.index(ROW165_TAIL_MARKER)
    end = preface.index(ROW165_TAIL_END)
    block = preface[start:end]
    new_block = block.replace(
        "when opening [row 146](preface.md#skill-navigation-row-146) before row 65 closes on the full capstone path",
        "when opening [row 166](preface.md#skill-navigation-row-166) before row 66 closes on the full capstone path",
    )
    new_block = new_block.replace(
        "When row 165 is complete, proceed to [row 146](preface.md#skill-navigation-row-146) when row 68 closed but Writings canonical meta prelude capstone still lags after second-pass meta prelude capstone on the full capstone path, to [row 126](preface.md#skill-navigation-row-146) for the Row 68 ↔ Row 66 meta audit on the opening-hinge capstone path alone, to [row 106](preface.md#skill-navigation-row-106) for the Row 68 ↔ Row 66 meta audit on the opening-hinge prelude path alone, to [row 145](preface.md#skill-navigation-row-125) for the Row 68 ↔ Row 65 second-pass meta audit on the opening-hinge capstone path alone, to [row 164](preface.md#skill-navigation-row-144) when book-loop meta prelude capstone still lags after verified orchestration meta prelude capstone on the full capstone path, to [row 85](preface.md#skill-navigation-row-85) for the Row 68 ↔ Row 65 opening prelude audit alone, to [row 65](preface.md#skill-navigation-row-65) for the Row 64 ↔ Row 45 meta audit alone, to [row 45](preface.md#skill-navigation-row-45) for the full Rows 17–44 → row 17 meta audit, or extend prose only under `writings/` then sync.",
        "When row 165 is complete, proceed to [row 166](preface.md#skill-navigation-row-166) when row 68 closed but Writings canonical meta prelude capstone still lags after second-pass meta prelude capstone on the full capstone path, to [row 146](preface.md#skill-navigation-row-146) for the Row 68 ↔ Row 66 meta audit on the opening-hinge capstone path alone, to [row 106](preface.md#skill-navigation-row-106) for the Row 68 ↔ Row 66 meta audit on the opening-hinge prelude path alone, to [row 145](preface.md#skill-navigation-row-145) for the Row 68 ↔ Row 65 second-pass meta audit on the opening-hinge capstone path alone, to [row 164](preface.md#skill-navigation-row-164) when book-loop meta prelude capstone still lags after verified orchestration meta prelude capstone on the full capstone path, to [row 85](preface.md#skill-navigation-row-85) for the Row 68 ↔ Row 65 opening prelude audit alone, to [row 65](preface.md#skill-navigation-row-65) for the Row 64 ↔ Row 45 meta audit alone, to [row 45](preface.md#skill-navigation-row-45) for the full Rows 17–44 → row 17 meta audit, or extend prose only under `writings/` then sync.",
    )
    new_block = new_block.replace(
        "[row 164](preface.md#skill-navigation-row-144) or [Row 68 → Row 145 second-pass meta prelude capstone reunion index (row 145)](appendix/sources.md#row68-row145-second-pass-meta-prelude-capstone-reunion-index-row-165)",
        "[row 164](preface.md#skill-navigation-row-164) or [Row 68 → Row 145 second-pass meta prelude capstone reunion index (row 145)](appendix/sources.md#row68-row145-second-pass-meta-prelude-capstone-reunion-index-row-165)",
    )
    return preface[:start] + new_block + preface[end:]


def main():
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "skill-navigation-row-166" in preface:
        print("preface: row 166 already present")
    else:
        preface = update_row165_tail(preface)
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + ROW166_PREFACE + copper)
        preface_path.write_text(preface)
        print("preface: added row 166")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if ROW145_STITCH_BROKEN in prologue:
        prologue = prologue.replace(ROW145_STITCH_BROKEN, ROW145_STITCH_FIXED)
        print("prologue: fixed row 145 closing stitch")
    if ROW145_ORPHAN_PREFIX in prologue:
        prologue = prologue.replace(ROW145_ORPHAN_PREFIX, "\n")
        print("prologue: removed orphan row 145 paragraph")
    if "prologue-preview-row-166" not in prologue:
        needle = "| Row 68 → Row 145 Row 68 → Row 65 second-pass meta prelude capstone reunion (row 165) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 165 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + PROLOGUE_COMPASS + prologue[line_end + 1 :]
        prologue = prologue.replace(
            "**Row 165 closing stitch",
            PROLOGUE_STITCH + "**Row 165 closing stitch",
        )
        prologue = prologue.replace(
            '| <span id="prologue-preview-row-165"></span>Row 165 preview',
            PROLOGUE_PREVIEW + '| <span id="prologue-preview-row-165"></span>Row 165 preview',
        )
        prologue = prologue.replace(ROW165_STITCH_OLD, ROW165_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 166")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "row-166-closing-loop" not in epilogue:
        if ROW165_EPILOGUE_PROCEED_OLD in epilogue:
            epilogue = epilogue.replace(ROW165_EPILOGUE_PROCEED_OLD, ROW165_EPILOGUE_PROCEED_NEW)
        marker = (
            "to [row 65](#row-65-closing-loop) when only second-pass meta stalls, or extend prose only under `writings/` then sync.\n\n\n\n\n\n\n### Row 135 closing loop"
        )
        replacement = (
            "to [row 65](#row-65-closing-loop) when only second-pass meta stalls, or extend prose only under `writings/` then sync.\n\n\n"
            + EPILOGUE_LOOP
            + "\n\n\n\n\n### Row 135 closing loop"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 165 end marker not found")
        epilogue = epilogue.replace(marker, replacement, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 166")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row146-writings-meta-prelude-capstone-reunion-index-row-166" not in sources:
        sources = sources.replace(
            "| 146 | Row 68 → Row 126 Row 68 → Row 66 Writings canonical meta prelude capstone",
            SOURCES_TABLE + "| 146 | Row 68 → Row 126 Row 68 → Row 66 Writings canonical meta prelude capstone",
        )
        sources = sources.replace(
            "## Row 68 → Row 126 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 146)",
            SOURCES_INDEX + "## Row 68 → Row 126 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 146)",
        )
        sources = sources.replace(
            "before row 146 Writings canonical meta prelude capstone reunion opens on the capstone path;",
            "before row 146 Writings canonical meta prelude capstone reunion opens on the capstone path; [row 166](#row68-row146-writings-meta-prelude-capstone-reunion-index-row-166) reunites **Writings canonical meta prelude capstone with the canonical source-tree boundary on the full capstone path** when row 165 closed second-pass meta prelude capstone at verified reopening anchor but row 66 Writings canonical meta still reads like separate courses on the full capstone path;",
        )
        sources_path.write_text(sources)
        print("sources: added row 166")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-166-baby-picture-row68-row146" not in memory:
        memory = memory.replace(
            "| 165 | Meta | [Row 68 → Row 145 second-pass meta prelude capstone reunion index]",
            MEMORY_TABLE + "| 165 | Meta | [Row 68 → Row 145 second-pass meta prelude capstone reunion index]",
        )
        memory = memory.replace(
            "### Row 165 baby picture {#row-165-baby-picture-row68-row145-second-pass-meta-prelude-capstone-reunion}",
            MEMORY_BABY + "### Row 165 baby picture {#row-165-baby-picture-row68-row145-second-pass-meta-prelude-capstone-reunion}",
        )
        memory = memory.replace(ROW165_BABY_OLD, ROW165_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 166")


if __name__ == "__main__":
    main()
