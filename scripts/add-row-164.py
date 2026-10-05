#!/usr/bin/env python3
"""Add row 164 meta-stitch (Row 68 → Row 144 ↔ Row 64 book-loop meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def t144_to_164(text: str) -> str:
    """Transform row-144 capstone-path meta copy to row 164 (144→164, 124→144 inner, 143→163 gate)."""
    repl = [
        ("Row 68 → Row 124 Row 68 → Row 64", "Row 68 → Row 144 Row 68 → Row 64"),
        (
            "row68-row124-book-loop-meta-prelude-capstone-reunion-index-row-144",
            "row68-row144-book-loop-meta-prelude-capstone-reunion-index-row-164",
        ),
        (
            "row-144-baby-picture-row68-row124-book-loop-meta-prelude-capstone-reunion",
            "row-164-baby-picture-row68-row144-book-loop-meta-prelude-capstone-reunion",
        ),
        ("skill-navigation-row-144", "skill-navigation-row-164"),
        ("prologue-preview-row-144", "prologue-preview-row-164"),
        ("row-144-closing-stitch", "row-164-closing-stitch"),
        ("row-144-closing-loop", "row-164-closing-loop"),
        ("Row 144 three-way audit", "Row 164 three-way audit"),
        (
            "[row 143](preface.md#skill-navigation-row-143) or [row 124](preface.md#skill-navigation-row-124)",
            "[row 163](preface.md#skill-navigation-row-163) or [row 144](preface.md#skill-navigation-row-144)",
        ),
        (
            "[row 143](preface.md#skill-navigation-row-143) or [Row 68 → Row 104",
            "[row 163](preface.md#skill-navigation-row-163) or [Row 68 → Row 124",
        ),
        ("on the capstone path", "on the full capstone path"),
        ("(capstone path)", "(full capstone path)"),
        ("Row 68 ↔ Row 64 reunion (capstone path)", "Row 68 ↔ Row 64 reunion (full capstone path)"),
    ]
    out = text
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace("row 144", "row 164")
    out = out.replace("Row 144", "Row 164")
    out = out.replace("[row 164](preface.md#skill-navigation-row-163)", "[row 163](preface.md#skill-navigation-row-163)")
    out = out.replace("[row 164](preface.md#skill-navigation-row-144)", "[row 144](preface.md#skill-navigation-row-144)")
    out = out.replace("row 1645", "row 165")
    out = out.replace("row 1646", "row 166")
    out = out.replace("row 164 or row 164", "row 163 or row 144")
    out = out.replace("When row 164 closed — orchestration", "When row 163 closed — orchestration")
    out = out.replace("When row 164 closed — book-loop", "When row 163 closed — book-loop")
    out = out.replace("row 164 closed orchestration", "row 163 closed orchestration")
    out = out.replace("row 164 closed book-loop", "row 163 closed book-loop")
    out = out.replace("after row 164 alone", "after row 163 alone")
    out = out.replace("Recite [preface row 164]", "Recite [preface row 163]")
    out = out.replace("row 164 or row 144 recited", "row 163 or row 144 recited")
    out = out.replace("from row 164's", "from row 163's")
    out = out.replace(
        "verified orchestration meta prelude capstone closure (row 164)",
        "verified orchestration meta prelude capstone closure (row 163)",
    )
    out = out.replace(
        "verified orchestration meta prelude capstone closure (row 143)",
        "verified orchestration meta prelude capstone closure (row 163)",
    )
    out = out.replace(
        "verified orchestration meta prelude capstone closure (row 142)",
        "verified orchestration meta prelude capstone closure (row 163)",
    )
    out = out.replace("row 124", "row 144")
    out = out.replace("Row 124", "Row 144")
    out = out.replace("row 143", "row 163")
    out = out.replace("Row 143", "Row 163")
    out = out.replace("row 142", "row 162")
    out = out.replace("Row 142", "Row 162")
    out = out.replace(
        "before row 165 second-pass meta prelude capstone opens on the full capstone path",
        "before row 145 second-pass meta prelude capstone opens on the full capstone path",
    )
    out = out.replace(
        "Proceed to [row 165]",
        "Proceed to [row 145]",
    )
    out = out.replace(
        "Do not conflate row 164 (row 68 ↔ row 64 reunion on the full capstone path) with row 144",
        "Do not conflate row 164 (row 68 ↔ row 64 reunion on the full capstone path) with row 144",
    )
    out = out.replace(
        "row 144 names **Row 68 → Row 104 Row 68 → Row 64 book-loop meta prelude capstone reunion**",
        "row 144 names **Row 68 → Row 124 Row 68 → Row 64 book-loop meta prelude capstone reunion**",
    )
    out = out.replace(
        "Row 68 → Row 164 Row 68 → Row 64",
        "Row 68 → Row 144 Row 68 → Row 64",
    )
    out = out.replace("#skill-navigation-row-1645", "#skill-navigation-row-145")
    out = out.replace("#skill-navigation-row-162)", "#skill-navigation-row-162)")
    out = out.replace("#skill-navigation-row-143)", "#skill-navigation-row-163)")
    out = out.replace(
        "row68-row104-book-loop-meta-prelude-capstone-reunion-index-row-124",
        "row68-row144-book-loop-meta-prelude-capstone-reunion-index-row-144",
    )
    out = out.replace(
        "row68-row123-orchestration-meta-prelude-capstone-reunion-index-row-143",
        "row68-row143-orchestration-meta-prelude-capstone-reunion-index-row-163",
    )
    out = out.replace("#row-124-closing-loop)", "#row-144-closing-loop)")
    out = out.replace("#row-143-closing-loop)", "#row-163-closing-loop)")
    out = out.replace(
        "Row 144 names **Row 68 → Row 104 Row 68 → Row 64 book-loop meta prelude capstone reunion**",
        "Row 144 names **Row 68 → Row 124 Row 68 → Row 64 book-loop meta prelude capstone reunion**",
    )
    out = out.replace(
        "row 163 names **Row 68 → Row 123 Row 68 → Row 63 orchestration meta prelude capstone reunion**",
        "row 163 names **Row 68 → Row 143 Row 68 → Row 63 orchestration meta prelude capstone reunion**",
    )
    return out


def extract_preface_row144(preface: str) -> str:
    start = preface.index("### Row 144 skill checkpoint")
    end = preface.index("\n\n### Row 145 skill checkpoint")
    return preface[start:end]


ROW164_PREFACE = t144_to_164(
    extract_preface_row144((ROOT / "writings/preface/chapters/preface.md").read_text())
) + "\n\n"

PROLOGUE_COMPASS = (
    "| Row 68 → Row 144 Row 68 → Row 64 book-loop meta prelude capstone reunion (row 164) | "
    "[Preface: row 164 skill checkpoint](../preface.md#skill-navigation-row-164) · "
    "[Row 68 → Row 144 book-loop meta prelude capstone reunion index](../appendix/sources.md#row68-row144-book-loop-meta-prelude-capstone-reunion-index-row-164) · "
    "[memory sheet row 164 baby picture](../appendix/memory-sheet.md#row-164-baby-picture-row68-row144-book-loop-meta-prelude-capstone-reunion) · "
    "[prologue row 164 preview row](#prologue-preview-row-164); [prologue row 164 closing stitch](#row-164-closing-stitch); "
    "[epilogue row 164 closing loop](../epilogue/multiscale.md#row-164-closing-loop) — "
    "read row 68 gate + row 163 or row 144 orchestration meta prelude capstone / book-loop meta capstone gate + epilogue book-loop cross-links + row 64 meta aloud "
    "when orchestration verifies after orchestration meta prelude capstone on the full capstone path but the next terminal opens with copper decks copied blindly without reopening anchor rung audit |\n"
)

PROLOGUE_STITCH = t144_to_164(
    "**Row 144 closing stitch (Row 68 → Row 124 Row 68 → Row 64 book-loop meta prelude capstone reunion).** {#row-144-closing-stitch} "
    "When row 143 closed — orchestration meta prelude capstone verified, row 142 or row 124 recited on the capstone path, and [`parse_multiscale_workflow.sh`](../../scripts/parse_multiscale_workflow.sh) archived `multiscale_export.yaml` with H1→H2→H3→H4a→H4b→OUT after verified Handshake 4b meta prelude capstone on the capstone path — "
    "but **row 64 book-loop meta reunion still opens like standalone epilogue coursework after verified orchestration on the capstone path** — "
    "read [preface row 144](../preface.md#skill-navigation-row-144), then the "
    "[Row 68 → Row 124 reunion index](../appendix/sources.md#row68-row124-book-loop-meta-prelude-capstone-reunion-index-row-144), then "
    "[epilogue row 144 closing loop](../epilogue/multiscale.md#row-144-closing-loop) before row 145 second-pass meta prelude capstone opens on the capstone path.\n\n"
)

PROLOGUE_PREVIEW = (
    "| <span id=\"prologue-preview-row-164\"></span>Row 164 preview (Row 68 → Row 144 Row 68 → Row 64 book-loop meta prelude capstone reunion) | "
    "Explain why midpoint closure (row 68) and book-loop meta (row 64) must be read together with the epilogue book-loop cross-links and restart chain "
    "after verified orchestration meta prelude capstone on the full capstone path before Act VI foundation and next-project restart feel like separate courses | "
    "One sentence: \"read row 68 gate + row 163 or row 144 orchestration meta prelude capstone / book-loop meta capstone gate + epilogue book-loop cross-links + row 64 meta aloud "
    "when orchestration verifies after orchestration meta prelude capstone on the full capstone path but the next terminal opens with copper decks copied blindly without reopening anchor rung audit\" — "
    "[preface row 164 skill checkpoint](../preface.md#skill-navigation-row-164); [prologue row 164 closing stitch](#row-164-closing-stitch); "
    "[Row 68 → Row 144 reunion index](../appendix/sources.md#row68-row144-book-loop-meta-prelude-capstone-reunion-index-row-164); "
    "[memory sheet row 164 baby picture](../appendix/memory-sheet.md#row-164-baby-picture-row68-row144-book-loop-meta-prelude-capstone-reunion); "
    "[epilogue book-loop cross-links audit](../epilogue/multiscale.md#opening-hinge-rows17-43-row12); "
    "[preface row 64 skill checkpoint](../preface.md#skill-navigation-row-64); "
    "[preface row 163 skill checkpoint](../preface.md#skill-navigation-row-163); "
    "[epilogue row 164 closing loop](../epilogue/multiscale.md#row-164-closing-loop) |\n"
)

_epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
EPILOGUE_LOOP = t144_to_164(
    "### Row 144 closing loop"
    + _epilogue.split("### Row 144 closing loop")[1].split("### Row 145 closing loop")[0]
)

SOURCES_TABLE = (
    "| 164 | Row 68 → Row 144 Row 68 → Row 64 book-loop meta prelude capstone (midpoint prelude gate ↔ book-loop meta prelude capstone on full capstone path ↔ row 64 meta) | "
    "[Row 68 → Row 144 book-loop meta prelude capstone reunion index](#row68-row144-book-loop-meta-prelude-capstone-reunion-index-row-164) · "
    "[preface row 164](../preface.md#skill-navigation-row-164) · "
    "[prologue row 164 preview](../prologue/00-many-scales.md#prologue-preview-row-164) · "
    "[prologue row 164 closing stitch](../prologue/00-many-scales.md#row-164-closing-stitch) · "
    "[epilogue row 164 closing loop](../epilogue/multiscale.md#row-164-closing-loop) · "
    "[memory sheet row 164 baby picture](memory-sheet.md#row-164-baby-picture-row68-row144-book-loop-meta-prelude-capstone-reunion) | "
    "Row 68 closed but **row 64 book-loop meta reunion still feels disconnected from verified orchestration meta prelude capstone on the full capstone path** — "
    "read row 68 + row 163 or row 144 gate + epilogue book-loop cross-links + row 64; "
    "[preface row 64](../preface.md#skill-navigation-row-64) |\n"
)

SOURCES_INDEX = t144_to_164(
    (ROOT / "writings/appendix/chapters/sources.md")
    .read_text()
    .split("## Row 68 → Row 124 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 144)")[1]
    .split("## Row 68 → Row 105 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 125)")[0]
)
SOURCES_INDEX = (
    "## Row 68 → Row 144 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 164)"
    + SOURCES_INDEX
)

MEMORY_TABLE = (
    "| 164 | Meta | [Row 68 → Row 144 book-loop meta prelude capstone reunion index](sources.md#row68-row144-book-loop-meta-prelude-capstone-reunion-index-row-164) · "
    "[preface row 164 skill checkpoint](../preface.md#skill-navigation-row-164) · "
    "[prologue row 164 preview](../prologue/00-many-scales.md#prologue-preview-row-164) · "
    "[prologue row 164 closing stitch](../prologue/00-many-scales.md#row-164-closing-stitch) · "
    "[epilogue row 164 closing loop](../epilogue/multiscale.md#row-164-closing-loop) | "
    "Row 68 closed but row 64 book-loop meta reunion feels disconnected from verified orchestration meta prelude capstone on the full capstone path — "
    "read row 68 + row 163 or row 144 gate + epilogue book-loop cross-links + row 64; "
    "[row 164 baby picture](#row-164-baby-picture-row68-row144-book-loop-meta-prelude-capstone-reunion) |\n"
)

MEMORY_BABY = t144_to_164(
    (ROOT / "writings/appendix/chapters/memory-sheet.md")
    .read_text()
    .split("### Row 144 baby picture")[1]
    .split("### Row 145 baby picture")[0]
)
MEMORY_BABY = "### Row 164 baby picture" + MEMORY_BABY.split(")", 1)[1] if ")" in MEMORY_BABY else "### Row 164 baby picture" + MEMORY_BABY

ROW163_TAIL_OLD = (
    "Read the [memory sheet row 163 baby picture](appendix/memory-sheet.md#row-163-baby-picture-row68-row143-orchestration-meta-prelude-capstone-reunion) when opening [row 144](preface.md#skill-navigation-row-144) before row 63 closes; read the [epilogue row 163 closing loop](epilogue/multiscale.md#row-163-closing-loop) when the competence loop closes. When row 163 is complete, proceed to [row 144](preface.md#skill-navigation-row-144) when row 68 closed but book-loop meta capstone still lags after orchestration meta prelude capstone on the full capstone path, to [row 124](preface.md#skill-navigation-row-124) for the Row 68 ↔ Row 64 book-loop meta audit on the opening-hinge capstone path alone, to [row 104](preface.md#skill-navigation-row-104) for the Row 68 ↔ Row 64 meta audit on the opening-hinge prelude path alone, to [row 143](preface.md#skill-navigation-row-143) for the Row 68 ↔ Row 63 meta audit on the opening-hinge capstone path alone, to [row 162](preface.md#skill-navigation-row-162) when Handshake 4b meta prelude capstone still lags after verified Handshake 4a meta prelude capstone on the full capstone path, to [row 83](preface.md#skill-navigation-row-83) for the Row 68 ↔ Row 63 opening prelude audit alone, to [row 63](preface.md#skill-navigation-row-63) for the Row 62 ↔ Row 43 meta audit alone, to [row 43](preface.md#skill-navigation-row-43) for the full Rows 17–42 → row 16 meta audit, or extend prose only under `writings/` then sync."
)
ROW163_TAIL_NEW = (
    "Read the [memory sheet row 163 baby picture](appendix/memory-sheet.md#row-163-baby-picture-row68-row143-orchestration-meta-prelude-capstone-reunion) when opening [row 164](preface.md#skill-navigation-row-164) before row 64 closes on the full capstone path; read the [epilogue row 163 closing loop](epilogue/multiscale.md#row-163-closing-loop) when the competence loop closes. When row 163 is complete, proceed to [row 164](preface.md#skill-navigation-row-164) when orchestration verifies individually but book-loop meta still feels disconnected from next-project restart after verified orchestration meta prelude capstone on the full capstone path, to [row 144](preface.md#skill-navigation-row-144) for the Row 68 ↔ Row 64 book-loop meta audit on the opening-hinge capstone path alone, to [row 124](preface.md#skill-navigation-row-124) for the Row 68 ↔ Row 64 book-loop meta audit on the opening-hinge capstone path alone, to [row 104](preface.md#skill-navigation-row-104) for the Row 68 ↔ Row 64 meta audit on the opening-hinge prelude path alone, to [row 143](preface.md#skill-navigation-row-143) for the Row 68 ↔ Row 63 meta audit on the opening-hinge capstone path alone, to [row 162](preface.md#skill-navigation-row-162) when Handshake 4b meta prelude capstone still lags after verified Handshake 4a meta prelude capstone on the full capstone path, to [row 83](preface.md#skill-navigation-row-83) for the Row 68 ↔ Row 63 opening prelude audit alone, to [row 63](preface.md#skill-navigation-row-63) for the Row 62 ↔ Row 43 meta audit alone, to [row 43](preface.md#skill-navigation-row-43) for the full Rows 17–42 → row 16 meta audit, or extend prose only under `writings/` then sync."
)

ROW163_STITCH_OLD = "before row 144 book-loop meta prelude capstone opens on the full capstone path"
ROW163_STITCH_NEW = (
    "before row 164 book-loop meta prelude capstone reunion on the full capstone path "
    "(then row 145 second-pass meta prelude capstone on the full capstone path)"
)

ROW163_EPILOGUE_PROCEED_OLD = (
    "Proceed to [row 144](#row-144-closing-loop) when row 68 closed but book-loop meta still feels disconnected after row 163 on the full capstone path,"
)
ROW163_EPILOGUE_PROCEED_NEW = (
    "Proceed to [row 164](#row-164-closing-loop) when row 68 closed but book-loop meta still feels disconnected after row 163 on the full capstone path,"
)

ROW163_BABY_OLD = (
    "row 163 when **epilogue orchestration cross-links and Row 62 → Row 43 meta must read on the same wire before row 144 book-loop meta prelude capstone reunion opens on the full capstone path**"
)
ROW163_BABY_NEW = (
    "row 163 when **epilogue orchestration cross-links and Row 62 → Row 43 meta must read on the same wire before row 164 book-loop meta prelude capstone reunion opens on the full capstone path**"
)


def main():
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "skill-navigation-row-164" in preface:
        print("preface: row 164 already present")
    else:
        if ROW163_TAIL_OLD not in preface:
            raise SystemExit("preface row 163 tail not found")
        preface = preface.replace(ROW163_TAIL_OLD, ROW163_TAIL_NEW)
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + ROW164_PREFACE + copper)
        preface_path.write_text(preface)
        print("preface: added row 164")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-164" not in prologue:
        needle = "| Row 68 → Row 143 Row 68 → Row 63 orchestration meta prelude capstone reunion (row 163) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 163 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + PROLOGUE_COMPASS + prologue[line_end + 1 :]
        prologue = prologue.replace(
            "**Row 163 closing stitch",
            PROLOGUE_STITCH + "**Row 163 closing stitch",
        )
        prologue = prologue.replace(
            '| <span id="prologue-preview-row-163"></span>Row 163 preview',
            PROLOGUE_PREVIEW + '| <span id="prologue-preview-row-163"></span>Row 163 preview',
        )
        prologue = prologue.replace(ROW163_STITCH_OLD, ROW163_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 164")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "row-164-closing-loop" not in epilogue:
        if ROW163_EPILOGUE_PROCEED_OLD in epilogue:
            epilogue = epilogue.replace(ROW163_EPILOGUE_PROCEED_OLD, ROW163_EPILOGUE_PROCEED_NEW)
        marker = (
            "to [row 63](#row-63-closing-loop) when only orchestration meta stalls, or extend prose only under `writings/` then sync.\n\n\n\n\n### Row 135 closing loop"
        )
        replacement = (
            "to [row 63](#row-63-closing-loop) when only orchestration meta stalls, or extend prose only under `writings/` then sync.\n\n\n"
            + EPILOGUE_LOOP
            + "\n\n### Row 135 closing loop"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 163 end marker not found")
        epilogue = epilogue.replace(marker, replacement, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 164")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row144-book-loop-meta-prelude-capstone-reunion-index-row-164" not in sources:
        sources = sources.replace(
            "| 163 | Row 68 → Row 143 Row 68 → Row 63 orchestration meta prelude capstone",
            SOURCES_TABLE + "| 163 | Row 68 → Row 143 Row 68 → Row 63 orchestration meta prelude capstone",
        )
        sources = sources.replace(
            "## Row 68 → Row 124 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 144)",
            SOURCES_INDEX + "## Row 68 → Row 124 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 144)",
        )
        sources = sources.replace(
            "before row 144 book-loop meta prelude capstone reunion opens on the capstone path;",
            "before row 144 book-loop meta prelude capstone reunion opens on the capstone path; [row 164](#row68-row144-book-loop-meta-prelude-capstone-reunion-index-row-164) reunites **book-loop meta prelude capstone with the book-loop meta boundary on the full capstone path** when row 163 closed orchestration meta prelude capstone at verified H1→OUT pedigree but row 64 book-loop meta still reads like separate courses on the full capstone path;",
        )
        sources_path.write_text(sources)
        print("sources: added row 164")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-164-baby-picture-row68-row144" not in memory:
        memory = memory.replace(
            "| 163 | Meta | [Row 68 → Row 143 orchestration meta prelude capstone reunion index]",
            MEMORY_TABLE + "| 163 | Meta | [Row 68 → Row 143 orchestration meta prelude capstone reunion index]",
        )
        memory = memory.replace(
            "### Row 163 baby picture {#row-163-baby-picture-row68-row143-orchestration-meta-prelude-capstone-reunion}",
            MEMORY_BABY + "### Row 163 baby picture {#row-163-baby-picture-row68-row143-orchestration-meta-prelude-capstone-reunion}",
        )
        memory = memory.replace(ROW163_BABY_OLD, ROW163_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 164")


if __name__ == "__main__":
    main()
