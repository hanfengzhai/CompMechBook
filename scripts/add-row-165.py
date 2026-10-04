#!/usr/bin/env python3
"""Add row 165 meta-stitch (Row 68 → Row 145 ↔ Row 65 second-pass meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def t145_to_165(text: str) -> str:
    """Transform row-145 capstone-path meta copy to row 165 (145→165, 125→145 inner, 144→164 gate)."""
    repl = [
        ("Row 68 → Row 125 Row 68 → Row 65", "Row 68 → Row 145 Row 68 → Row 65"),
        (
            "row68-row125-second-pass-meta-prelude-capstone-reunion-index-row-145",
            "row68-row145-second-pass-meta-prelude-capstone-reunion-index-row-165",
        ),
        (
            "row-145-baby-picture-row68-row125-second-pass-meta-prelude-capstone-reunion",
            "row-165-baby-picture-row68-row145-second-pass-meta-prelude-capstone-reunion",
        ),
        ("skill-navigation-row-145", "skill-navigation-row-165"),
        ("prologue-preview-row-145", "prologue-preview-row-165"),
        ("row-145-closing-stitch", "row-165-closing-stitch"),
        ("row-145-closing-loop", "row-165-closing-loop"),
        ("Row 145 three-way audit", "Row 165 three-way audit"),
        (
            "[row 144](preface.md#skill-navigation-row-144) or [row 125](preface.md#skill-navigation-row-125)",
            "[row 164](preface.md#skill-navigation-row-164) or [row 145](preface.md#skill-navigation-row-145)",
        ),
        (
            "[row 144](preface.md#skill-navigation-row-144) or [Row 68 → Row 105",
            "[row 164](preface.md#skill-navigation-row-164) or [Row 68 → Row 125",
        ),
        ("on the capstone path", "on the full capstone path"),
        ("(capstone path)", "(full capstone path)"),
        ("Row 68 ↔ Row 65 reunion (capstone path)", "Row 68 ↔ Row 65 reunion (full capstone path)"),
    ]
    out = text
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace("row 145", "row 165")
    out = out.replace("Row 145", "Row 165")
    out = out.replace("[row 165](preface.md#skill-navigation-row-164)", "[row 164](preface.md#skill-navigation-row-164)")
    out = out.replace("[row 165](preface.md#skill-navigation-row-145)", "[row 145](preface.md#skill-navigation-row-145)")
    out = out.replace("row 1655", "row 166")
    out = out.replace("row 1656", "row 167")
    out = out.replace("row 165 or row 165", "row 164 or row 145")
    out = out.replace("When row 165 closed — second-pass", "When row 164 closed — second-pass")
    out = out.replace("When row 165 closed — book-loop", "When row 164 closed — book-loop")
    out = out.replace("row 165 closed book-loop", "row 164 closed book-loop")
    out = out.replace("row 165 closed second-pass", "row 164 closed second-pass")
    out = out.replace("after row 165 alone", "after row 164 alone")
    out = out.replace("Recite [preface row 165]", "Recite [preface row 164]")
    out = out.replace("row 165 or row 145 recited", "row 164 or row 145 recited")
    out = out.replace("from row 165's", "from row 164's")
    out = out.replace(
        "verified book-loop meta prelude capstone closure (row 165)",
        "verified book-loop meta prelude capstone closure (row 164)",
    )
    out = out.replace(
        "verified book-loop meta prelude capstone closure (row 144)",
        "verified book-loop meta prelude capstone closure (row 164)",
    )
    out = out.replace("row 125", "row 145")
    out = out.replace("Row 125", "Row 145")
    out = out.replace("row 144", "row 164")
    out = out.replace("Row 144", "Row 164")
    out = out.replace(
        "before row 166 Writings canonical meta prelude capstone opens on the full capstone path",
        "before row 146 Writings canonical meta prelude capstone opens on the full capstone path",
    )
    out = out.replace(
        "Proceed to [row 166]",
        "Proceed to [row 146]",
    )
    out = out.replace(
        "Do not conflate row 165 (row 68 ↔ row 65 reunion on the full capstone path) with row 145",
        "Do not conflate row 165 (row 68 ↔ row 65 reunion on the full capstone path) with row 145",
    )
    out = out.replace(
        "row 145 names **Row 68 → Row 105 Row 68 → Row 65 second-pass meta prelude capstone reunion**",
        "row 145 names **Row 68 → Row 125 Row 68 → Row 65 second-pass meta prelude capstone reunion**",
    )
    out = out.replace(
        "Row 68 → Row 165 Row 68 → Row 65",
        "Row 68 → Row 145 Row 68 → Row 65",
    )
    out = out.replace("#skill-navigation-row-1655", "#skill-navigation-row-166")
    out = out.replace("#skill-navigation-row-126)", "#skill-navigation-row-146)")
    out = out.replace(
        "row68-row105-second-pass-meta-prelude-capstone-reunion-index-row-125",
        "row68-row145-second-pass-meta-prelude-capstone-reunion-index-row-145",
    )
    out = out.replace(
        "row68-row124-book-loop-meta-prelude-capstone-reunion-index-row-144",
        "row68-row144-book-loop-meta-prelude-capstone-reunion-index-row-164",
    )
    out = out.replace("#row-125-closing-loop)", "#row-145-closing-loop)")
    out = out.replace(
        "Row 145 names **Row 68 → Row 105 Row 68 → Row 65 second-pass meta prelude capstone reunion**",
        "Row 145 names **Row 68 → Row 125 Row 68 → Row 65 second-pass meta prelude capstone reunion**",
    )
    out = out.replace(
        "row 164 names **Row 68 → Row 124 Row 68 → Row 64 book-loop meta prelude capstone reunion**",
        "row 164 names **Row 68 → Row 144 Row 68 → Row 64 book-loop meta prelude capstone reunion**",
    )
    return out


def extract_preface_row145(preface: str) -> str:
    start = preface.index("### Row 145 skill checkpoint")
    end = preface.index("\n\n### Row 146 skill checkpoint")
    return preface[start:end]


ROW165_PREFACE = t145_to_165(
    extract_preface_row145((ROOT / "writings/preface/chapters/preface.md").read_text())
) + "\n\n"

PROLOGUE_COMPASS = (
    "| Row 68 → Row 145 Row 68 → Row 65 second-pass meta prelude capstone reunion (row 165) | "
    "[Preface: row 165 skill checkpoint](../preface.md#skill-navigation-row-165) · "
    "[Row 68 → Row 145 second-pass meta prelude capstone reunion index](../appendix/sources.md#row68-row145-second-pass-meta-prelude-capstone-reunion-index-row-165) · "
    "[memory sheet row 165 baby picture](../appendix/memory-sheet.md#row-165-baby-picture-row68-row145-second-pass-meta-prelude-capstone-reunion) · "
    "[prologue row 165 preview row](#prologue-preview-row-165); [prologue row 165 closing stitch](#row-165-closing-stitch); "
    "[epilogue row 165 closing loop](../epilogue/multiscale.md#row-165-closing-loop) — "
    "read row 68 gate + row 164 or row 145 book-loop meta prelude capstone / second-pass meta prelude gate + epilogue second-pass cross-links + row 65 meta aloud "
    "when the book loop closes on the full capstone path but every chapter boundary still opens a skill checkpoint instead of trusting Scene → Bridge rhythm |\n"
)

PROLOGUE_STITCH = t145_to_165(
    "**Row 145 closing stitch (Row 68 → Row 125 Row 68 → Row 65 second-pass meta prelude capstone reunion).** {#row-145-closing-stitch} "
    "When row 144 closed — book-loop meta prelude capstone verified, row 143 or row 124 recited on the capstone path, and the [prologue reopening anchor](#prologue-reopening-anchor) received the reader with `./scripts/test-fixtures.sh` green after verified orchestration meta prelude capstone on the capstone path — "
    "but **row 65 second-pass meta reunion still opens like standalone appendix coursework after the second-pass opening prelude chapter hinge on the capstone path** — "
    "read [preface row 145](../preface.md#skill-navigation-row-145), then the "
    "[Row 68 → Row 125 reunion index](../appendix/sources.md#row68-row125-second-pass-meta-prelude-capstone-reunion-index-row-145), then "
    "[epilogue row 145 closing loop](../epilogue/multiscale.md#row-145-closing-loop) before row 146 Writings canonical meta prelude capstone opens on the capstone path.\n\n"
)

PROLOGUE_PREVIEW = (
    "| <span id=\"prologue-preview-row-165\"></span>Row 165 preview (Row 68 → Row 145 Row 68 → Row 65 second-pass meta prelude capstone reunion) | "
    "Explain why midpoint closure (row 68) and second-pass meta (row 65) must be read together with the epilogue second-pass cross-links and continuous read-through guide "
    "after verified book-loop meta prelude capstone on the full capstone path before next-project restart and novel rhythm feel like separate courses | "
    "One sentence: \"read row 68 gate + row 164 or row 145 book-loop meta prelude capstone / second-pass meta prelude gate + epilogue second-pass cross-links + row 65 meta aloud "
    "when the book loop closes on the full capstone path but every chapter boundary still opens a skill checkpoint instead of trusting Scene → Bridge rhythm\" — "
    "[preface row 165 skill checkpoint](../preface.md#skill-navigation-row-165); [prologue row 165 closing stitch](#row-165-closing-stitch); "
    "[Row 68 → Row 145 reunion index](../appendix/sources.md#row68-row145-second-pass-meta-prelude-capstone-reunion-index-row-165); "
    "[memory sheet row 165 baby picture](../appendix/memory-sheet.md#row-165-baby-picture-row68-row145-second-pass-meta-prelude-capstone-reunion); "
    "[epilogue second-pass cross-links audit](../epilogue/multiscale.md#opening-hinge-rows17-44-row17); "
    "[preface row 65 skill checkpoint](../preface.md#skill-navigation-row-65); "
    "[preface row 164 skill checkpoint](../preface.md#skill-navigation-row-164); "
    "[epilogue row 165 closing loop](../epilogue/multiscale.md#row-165-closing-loop) |\n"
)

_epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
EPILOGUE_LOOP = t145_to_165(
    "### Row 145 closing loop"
    + _epilogue.split("### Row 145 closing loop")[1].split("### Row 146 closing loop")[0]
)

SOURCES_TABLE = (
    "| 165 | Row 68 → Row 145 Row 68 → Row 65 second-pass meta prelude capstone (midpoint prelude gate ↔ book-loop meta prelude capstone on full capstone path ↔ row 65 meta) | "
    "[Row 68 → Row 145 second-pass meta prelude capstone reunion index](#row68-row145-second-pass-meta-prelude-capstone-reunion-index-row-165) · "
    "[preface row 165](../preface.md#skill-navigation-row-165) · "
    "[prologue row 165 preview](../prologue/00-many-scales.md#prologue-preview-row-165) · "
    "[prologue row 165 closing stitch](../prologue/00-many-scales.md#row-165-closing-stitch) · "
    "[epilogue row 165 closing loop](../epilogue/multiscale.md#row-165-closing-loop) · "
    "[memory sheet row 165 baby picture](memory-sheet.md#row-165-baby-picture-row68-row145-second-pass-meta-prelude-capstone-reunion) | "
    "Row 68 closed but **row 65 second-pass meta reunion still feels disconnected from verified book-loop meta prelude capstone on the full capstone path** — "
    "read row 68 + row 164 or row 145 gate + epilogue second-pass cross-links + row 65; "
    "[preface row 65](../preface.md#skill-navigation-row-65) |\n"
)

SOURCES_INDEX = t145_to_165(
    (ROOT / "writings/appendix/chapters/sources.md")
    .read_text()
    .split("## Row 68 → Row 125 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 145)")[1]
    .split("## Row 68 → Row 106 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 126)")[0]
)
SOURCES_INDEX = (
    "## Row 68 → Row 145 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 165)"
    + SOURCES_INDEX
)

MEMORY_TABLE = (
    "| 165 | Meta | [Row 68 → Row 145 second-pass meta prelude capstone reunion index](sources.md#row68-row145-second-pass-meta-prelude-capstone-reunion-index-row-165) · "
    "[preface row 165 skill checkpoint](../preface.md#skill-navigation-row-165) · "
    "[prologue row 165 preview](../prologue/00-many-scales.md#prologue-preview-row-165) · "
    "[prologue row 165 closing stitch](../prologue/00-many-scales.md#row-165-closing-stitch) · "
    "[epilogue row 165 closing loop](../epilogue/multiscale.md#row-165-closing-loop) | "
    "Row 68 closed but row 65 second-pass meta reunion feels disconnected from verified book-loop meta prelude capstone on the full capstone path — "
    "read row 68 + row 164 or row 145 gate + epilogue second-pass cross-links + row 65; "
    "[row 165 baby picture](#row-165-baby-picture-row68-row145-second-pass-meta-prelude-capstone-reunion) |\n"
)

MEMORY_BABY = t145_to_165(
    (ROOT / "writings/appendix/chapters/memory-sheet.md")
    .read_text()
    .split("### Row 145 baby picture")[1]
    .split("### Row 146 baby picture")[0]
)
MEMORY_BABY = "### Row 165 baby picture" + MEMORY_BABY.split(")", 1)[1] if ")" in MEMORY_BABY else "### Row 165 baby picture" + MEMORY_BABY

ROW164_TAIL_OLD = (
    "Read the [memory sheet row 164 baby picture](appendix/memory-sheet.md#row-164-baby-picture-row68-row144-book-loop-meta-prelude-capstone-reunion) when opening [row 145](preface.md#skill-navigation-row-145) before row 64 closes; read the [epilogue row 164 closing loop](epilogue/multiscale.md#row-164-closing-loop) when the competence loop closes. When row 164 is complete, proceed to [row 145](preface.md#skill-navigation-row-145) when row 68 closed but second-pass meta capstone still lags after book-loop meta prelude capstone on the full capstone path, to [row 125](preface.md#skill-navigation-row-125) for the Row 68 ↔ Row 65 second-pass meta audit on the opening-hinge capstone path alone, to [row 105](preface.md#skill-navigation-row-105) for the Row 68 ↔ Row 65 meta audit on the opening-hinge prelude path alone, to [row 163](preface.md#skill-navigation-row-163) when orchestration meta prelude capstone still lags after verified Handshake 4b meta prelude capstone on the full capstone path, to [row 84](preface.md#skill-navigation-row-84) for the Row 68 ↔ Row 64 opening prelude audit alone, to [row 64](preface.md#skill-navigation-row-64) for the Row 63 ↔ Row 44 meta audit alone, to [row 44](preface.md#skill-navigation-row-44) for the full Rows 17–43 → row 12 meta audit, or extend prose only under `writings/` then sync."
)
ROW164_TAIL_NEW = (
    "Read the [memory sheet row 164 baby picture](appendix/memory-sheet.md#row-164-baby-picture-row68-row144-book-loop-meta-prelude-capstone-reunion) when opening [row 165](preface.md#skill-navigation-row-165) before row 65 closes on the full capstone path; read the [epilogue row 164 closing loop](epilogue/multiscale.md#row-164-closing-loop) when the competence loop closes. When row 164 is complete, proceed to [row 165](preface.md#skill-navigation-row-165) when row 68 closed but second-pass meta still feels disconnected from novel rhythm after verified book-loop meta prelude capstone on the full capstone path, to [row 145](preface.md#skill-navigation-row-145) for the Row 68 ↔ Row 65 second-pass meta audit on the opening-hinge capstone path alone, to [row 125](preface.md#skill-navigation-row-125) for the Row 68 ↔ Row 65 second-pass meta audit on the opening-hinge capstone path alone, to [row 105](preface.md#skill-navigation-row-105) for the Row 68 ↔ Row 65 meta audit on the opening-hinge prelude path alone, to [row 163](preface.md#skill-navigation-row-163) when orchestration meta prelude capstone still lags after verified Handshake 4b meta prelude capstone on the full capstone path, to [row 84](preface.md#skill-navigation-row-84) for the Row 68 ↔ Row 64 opening prelude audit alone, to [row 64](preface.md#skill-navigation-row-64) for the Row 63 ↔ Row 44 meta audit alone, to [row 44](preface.md#skill-navigation-row-44) for the full Rows 17–43 → row 12 meta audit, or extend prose only under `writings/` then sync."
)

ROW164_STITCH_OLD = "before row 145 second-pass meta prelude capstone opens on the full capstone path"
ROW164_STITCH_NEW = (
    "before row 165 second-pass meta prelude capstone reunion on the full capstone path "
    "(then row 146 Writings canonical meta prelude capstone on the full capstone path)"
)

ROW164_EPILOGUE_PROCEED_OLD = (
    "Proceed to [row 145](#row-145-closing-loop) when row 68 closed but second-pass meta capstone still lags after row 164 on the full capstone path,"
)
ROW164_EPILOGUE_PROCEED_NEW = (
    "Proceed to [row 165](#row-165-closing-loop) when row 68 closed but second-pass meta capstone still lags after row 164 on the full capstone path,"
)

ROW164_BABY_OLD = (
    "row 164 when **epilogue book-loop cross-links and Row 63 → Row 44 meta must read on the same wire before row 145 second-pass meta prelude capstone reunion opens on the full capstone path**"
)
ROW164_BABY_NEW = (
    "row 164 when **epilogue book-loop cross-links and Row 63 → Row 44 meta must read on the same wire before row 165 second-pass meta prelude capstone reunion opens on the full capstone path**"
)


def main():
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "skill-navigation-row-165" in preface:
        print("preface: row 165 already present")
    else:
        if ROW164_TAIL_OLD not in preface:
            raise SystemExit("preface row 164 tail not found")
        preface = preface.replace(ROW164_TAIL_OLD, ROW164_TAIL_NEW)
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + ROW165_PREFACE + copper)
        preface_path.write_text(preface)
        print("preface: added row 165")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-165" not in prologue:
        needle = "| Row 68 → Row 144 Row 68 → Row 64 book-loop meta prelude capstone reunion (row 164) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 164 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + PROLOGUE_COMPASS + prologue[line_end + 1 :]
        prologue = prologue.replace(
            "**Row 164 closing stitch",
            PROLOGUE_STITCH + "**Row 164 closing stitch",
        )
        prologue = prologue.replace(
            '| <span id="prologue-preview-row-164"></span>Row 164 preview',
            PROLOGUE_PREVIEW + '| <span id="prologue-preview-row-164"></span>Row 164 preview',
        )
        prologue = prologue.replace(ROW164_STITCH_OLD, ROW164_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 165")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "row-165-closing-loop" not in epilogue:
        if ROW164_EPILOGUE_PROCEED_OLD in epilogue:
            epilogue = epilogue.replace(ROW164_EPILOGUE_PROCEED_OLD, ROW164_EPILOGUE_PROCEED_NEW)
        marker = (
            "to [row 64](#row-64-closing-loop) when only book-loop meta stalls, or extend prose only under `writings/` then sync.\n\n\n\n\n### Row 135 closing loop"
        )
        replacement = (
            "to [row 64](#row-64-closing-loop) when only book-loop meta stalls, or extend prose only under `writings/` then sync.\n\n\n"
            + EPILOGUE_LOOP
            + "\n\n### Row 135 closing loop"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 164 end marker not found")
        epilogue = epilogue.replace(marker, replacement, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 165")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row145-second-pass-meta-prelude-capstone-reunion-index-row-165" not in sources:
        sources = sources.replace(
            "| 145 | Row 68 → Row 125 Row 68 → Row 65 second-pass meta prelude capstone",
            SOURCES_TABLE + "| 145 | Row 68 → Row 125 Row 68 → Row 65 second-pass meta prelude capstone",
        )
        sources = sources.replace(
            "## Row 68 → Row 125 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 145)",
            SOURCES_INDEX + "## Row 68 → Row 125 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 145)",
        )
        sources = sources.replace(
            "before row 145 second-pass meta prelude capstone reunion opens on the capstone path;",
            "before row 145 second-pass meta prelude capstone reunion opens on the capstone path; [row 165](#row68-row145-second-pass-meta-prelude-capstone-reunion-index-row-165) reunites **second-pass meta prelude capstone with the second-pass meta boundary on the full capstone path** when row 164 closed book-loop meta prelude capstone at verified reopening anchor but row 65 second-pass meta still reads like separate courses on the full capstone path;",
        )
        sources_path.write_text(sources)
        print("sources: added row 165")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-165-baby-picture-row68-row145" not in memory:
        memory = memory.replace(
            "| 164 | Meta | [Row 68 → Row 144 book-loop meta prelude capstone reunion index]",
            MEMORY_TABLE + "| 164 | Meta | [Row 68 → Row 144 book-loop meta prelude capstone reunion index]",
        )
        memory = memory.replace(
            "### Row 164 baby picture {#row-164-baby-picture-row68-row144-book-loop-meta-prelude-capstone-reunion}",
            MEMORY_BABY + "### Row 164 baby picture {#row-164-baby-picture-row68-row144-book-loop-meta-prelude-capstone-reunion}",
        )
        memory = memory.replace(ROW164_BABY_OLD, ROW164_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 165")


if __name__ == "__main__":
    main()
