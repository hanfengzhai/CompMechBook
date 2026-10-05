#!/usr/bin/env python3
"""Add row 160 meta-stitch (Row 68 → Row 140 ↔ Row 60 Handshake 3 meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def t140_to_160(text: str) -> str:
    """Transform row-140 capstone-path meta copy to row 160 (140→160, 120→140 inner, 139→159 gate)."""
    repl = [
        ("Row 68 → Row 120 Row 68 → Row 60", "Row 68 → Row 140 Row 68 → Row 60"),
        (
            "row68-row120-handshake3-meta-prelude-capstone-reunion-index-row-140",
            "row68-row140-handshake3-meta-prelude-capstone-reunion-index-row-160",
        ),
        (
            "row-140-baby-picture-row68-row120-handshake3-meta-prelude-capstone-reunion",
            "row-160-baby-picture-row68-row140-handshake3-meta-prelude-capstone-reunion",
        ),
        ("skill-navigation-row-140", "skill-navigation-row-160"),
        ("prologue-preview-row-140", "prologue-preview-row-160"),
        ("row-140-closing-stitch", "row-160-closing-stitch"),
        ("row-140-closing-loop", "row-160-closing-loop"),
        ("Row 140 three-way audit", "Row 160 three-way audit"),
        (
            "[row 139](preface.md#skill-navigation-row-139) or [row 120](preface.md#skill-navigation-row-120)",
            "[row 159](preface.md#skill-navigation-row-159) or [row 140](preface.md#skill-navigation-row-140)",
        ),
        (
            "[row 139](preface.md#skill-navigation-row-139) or [Row 68 → Row 100",
            "[row 159](preface.md#skill-navigation-row-159) or [Row 68 → Row 120",
        ),
        ("on the capstone path", "on the full capstone path"),
        ("(capstone path)", "(full capstone path)"),
        ("Row 68 ↔ Row 60 reunion (capstone path)", "Row 68 ↔ Row 60 reunion (full capstone path)"),
    ]
    out = text
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace("row 140", "row 160")
    out = out.replace("Row 140", "Row 160")
    out = out.replace("[row 160](preface.md#skill-navigation-row-159)", "[row 159](preface.md#skill-navigation-row-159)")
    out = out.replace("[row 160](preface.md#skill-navigation-row-140)", "[row 140](preface.md#skill-navigation-row-140)")
    out = out.replace("row 1607", "row 157")
    out = out.replace("row 1608", "row 158")
    out = out.replace("row 160 or row 160", "row 159 or row 140")
    out = out.replace("When row 160 closed — Handshake 3", "When row 159 closed — Handshake 3")
    out = out.replace("row 160 closed Handshake 3", "row 159 closed Handshake 3")
    out = out.replace("after row 160 alone", "after row 159 alone")
    out = out.replace("Recite [preface row 160]", "Recite [preface row 159]")
    out = out.replace("row 160 or row 140 recited", "row 159 or row 140 recited")
    out = out.replace("from row 160's", "from row 159's")
    out = out.replace(
        "verified Handshake 3 meta prelude capstone closure (row 160)",
        "verified Handshake 3 meta prelude capstone closure (row 159)",
    )
    out = out.replace(
        "verified Handshake 3 meta prelude capstone closure (row 139)",
        "verified Handshake 3 meta prelude capstone closure (row 159)",
    )
    out = out.replace("row 120", "row 140")
    out = out.replace("Row 120", "Row 140")
    out = out.replace("row 139", "row 159")
    out = out.replace("Row 139", "Row 159")
    out = out.replace("row 138", "row 158")
    out = out.replace("Row 138", "Row 158")
    out = out.replace("row 119", "row 139")
    out = out.replace(
        "before row 161 Handshake 4a meta prelude capstone opens on the full capstone path",
        "before row 141 Handshake 4a meta prelude capstone opens on the full capstone path",
    )
    out = out.replace(
        "Proceed to [row 161]",
        "Proceed to [row 141]",
    )
    out = out.replace("row 141 Handshake 4a meta prelude capstone opens", "row 141 Handshake 4a meta prelude capstone opens")
    out = out.replace(
        "Do not conflate row 160 (row 68 ↔ row 60 reunion on the full capstone path) with row 140",
        "Do not conflate row 160 (row 68 ↔ row 60 reunion on the full capstone path) with row 140",
    )
    out = out.replace(
        "row 140 names **Row 68 → Row 100 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion**",
        "row 140 names **Row 68 → Row 120 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion**",
    )
    out = out.replace("#skill-navigation-row-1601", "#skill-navigation-row-141")
    out = out.replace(
        "Row 68 → Row 160 Row 68 → Row 60",
        "Row 68 → Row 140 Row 68 → Row 60",
    )
    return out


def extract_preface_row140(preface: str) -> str:
    start = preface.index("### Row 140 skill checkpoint")
    end = preface.index("\n\n\n### Row 141 skill checkpoint")
    return preface[start:end]


ROW160_PREFACE = t140_to_160(
    extract_preface_row140((ROOT / "writings/preface/chapters/preface.md").read_text())
) + "\n\n"

PROLOGUE_COMPASS = (
    "| Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion (row 160) | "
    "[Preface: row 160 skill checkpoint](../preface.md#skill-navigation-row-160) · "
    "[Row 68 → Row 140 Handshake 3 meta prelude capstone reunion index](../appendix/sources.md#row68-row140-handshake3-meta-prelude-capstone-reunion-index-row-160) · "
    "[memory sheet row 160 baby picture](../appendix/memory-sheet.md#row-160-baby-picture-row68-row140-handshake3-meta-prelude-capstone-reunion) · "
    "[prologue row 160 preview row](#prologue-preview-row-160); [prologue row 160 closing stitch](#row-160-closing-stitch); "
    "[epilogue row 160 closing loop](../epilogue/multiscale.md#row-160-closing-loop) — "
    "read row 68 gate + row 159 or row 140 Handshake 3 meta prelude capstone / Handshake 3 meta capstone gate + epilogue α cross-links + row 60 meta aloud "
    "when load cell parses at \\(T_w\\) after verified Handshake 3 meta prelude capstone on the full capstone path but Handshake 3 still feels disconnected from Parts III–VI |\n"
)

PROLOGUE_STITCH = t140_to_160(
    "**Row 140 closing stitch (Row 68 → Row 120 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion).** {#row-140-closing-stitch} "
    "When row 139 closed — Handshake 3 meta prelude capstone verified, row 138 or row 119 recited on the capstone path, and [`parse_alpha.sh`](../../scripts/parse_alpha.sh) archived `alpha_export.yaml` matching [`fixtures/cht_export.yaml`](../../fixtures/cht_export.yaml) at \\(T_w = 311.48\\,\\text{K}\\) after verified DFT workflows meta prelude capstone — "
    "but **row 60 Handshake 3 meta reunion still opens like standalone epilogue coursework after the load-cell chapter hinge on the capstone path** — "
    "read [preface row 140](../preface.md#skill-navigation-row-140), then the "
    "[Row 68 → Row 120 reunion index](../appendix/sources.md#row68-row120-handshake3-meta-prelude-capstone-reunion-index-row-140), then "
    "[epilogue row 140 closing loop](../epilogue/multiscale.md#row-140-closing-loop) before row 141 Handshake 4a meta prelude capstone opens on the capstone path.\n\n"
)

PROLOGUE_PREVIEW = (
    "| <span id=\"prologue-preview-row-160\"></span>Row 160 preview (Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion) | "
    "Explain why midpoint closure (row 68) and Handshake 3 meta (row 60) must be read together with the epilogue α cross-links and ascent chain "
    "after verified Handshake 3 meta prelude capstone on the full capstone path before Act II warming and Act III pulling feel like separate courses | "
    "One sentence: \"read row 68 gate + row 159 or row 140 Handshake 3 meta prelude capstone / Handshake 3 meta capstone gate + epilogue α cross-links + row 60 meta aloud "
    "when load cell parses at \\(T_w\\) after verified Handshake 3 meta prelude capstone on the full capstone path but Handshake 3 still feels disconnected from Parts III–VI\" — "
    "[preface row 160 skill checkpoint](../preface.md#skill-navigation-row-160); [prologue row 160 closing stitch](#row-160-closing-stitch); "
    "[Row 68 → Row 140 reunion index](../appendix/sources.md#row68-row140-handshake3-meta-prelude-capstone-reunion-index-row-160); "
    "[memory sheet row 160 baby picture](../appendix/memory-sheet.md#row-160-baby-picture-row68-row140-handshake3-meta-prelude-capstone-reunion); "
    "[epilogue α cross-links audit](../epilogue/multiscale.md#opening-hinge-ix3-handshake3); "
    "[preface row 60 skill checkpoint](../preface.md#skill-navigation-row-60); "
    "[preface row 159 skill checkpoint](../preface.md#skill-navigation-row-159); "
    "[epilogue row 160 closing loop](../epilogue/multiscale.md#row-160-closing-loop) |\n"
)

_epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
EPILOGUE_LOOP = t140_to_160(
    "### Row 140 closing loop"
    + _epilogue.split("### Row 140 closing loop")[1].split("### Row 141 closing loop")[0]
)
EPILOGUE_LOOP = EPILOGUE_LOOP.replace(
    "Row 160 closes the **Handshake 3 meta prelude capstone",
    "Row 160 closes the **Handshake 3 meta prelude capstone",
    1,
)

SOURCES_TABLE = (
    "| 160 | Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone (midpoint prelude gate ↔ Handshake 3 meta prelude capstone on full capstone path ↔ row 60 meta) | "
    "[Row 68 → Row 140 Handshake 3 meta prelude capstone reunion index](#row68-row140-handshake3-meta-prelude-capstone-reunion-index-row-160) · "
    "[preface row 160](../preface.md#skill-navigation-row-160) · "
    "[prologue row 160 preview](../prologue/00-many-scales.md#prologue-preview-row-160) · "
    "[prologue row 160 closing stitch](../prologue/00-many-scales.md#row-160-closing-stitch) · "
    "[epilogue row 160 closing loop](../epilogue/multiscale.md#row-160-closing-loop) · "
    "[memory sheet row 160 baby picture](memory-sheet.md#row-160-baby-picture-row68-row140-handshake3-meta-prelude-capstone-reunion) | "
    "Row 68 closed but **row 60 Handshake 3 meta reunion still feels disconnected from verified Handshake 3 meta prelude capstone on the full capstone path** — "
    "read row 68 + row 159 or row 140 gate + epilogue α cross-links + row 60; "
    "[preface row 60](../preface.md#skill-navigation-row-60) |\n"
)

SOURCES_INDEX = t140_to_160(
    (ROOT / "writings/appendix/chapters/sources.md")
    .read_text()
    .split("## Row 68 → Row 120 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 140)")[1]
    .split("## Row 68 → Row 121 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 141)")[0]
)
SOURCES_INDEX = (
    "## Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 160)"
    + SOURCES_INDEX
)

MEMORY_TABLE = (
    "| 160 | Meta | [Row 68 → Row 140 Handshake 3 meta prelude capstone reunion index](sources.md#row68-row140-handshake3-meta-prelude-capstone-reunion-index-row-160) · "
    "[preface row 160 skill checkpoint](../preface.md#skill-navigation-row-160) · "
    "[prologue row 160 preview](../prologue/00-many-scales.md#prologue-preview-row-160) · "
    "[prologue row 160 closing stitch](../prologue/00-many-scales.md#row-160-closing-stitch) · "
    "[epilogue row 160 closing loop](../epilogue/multiscale.md#row-160-closing-loop) | "
    "Row 68 closed but row 60 Handshake 3 meta reunion feels disconnected from verified Handshake 3 meta prelude capstone on the full capstone path — "
    "read row 68 + row 159 or row 140 gate + epilogue α cross-links + row 60; "
    "[row 160 baby picture](#row-160-baby-picture-row68-row140-handshake3-meta-prelude-capstone-reunion) |\n"
)

MEMORY_BABY = t140_to_160(
    (ROOT / "writings/appendix/chapters/memory-sheet.md")
    .read_text()
    .split("### Row 140 baby picture")[1]
    .split("### Row 141 baby picture")[0]
)
MEMORY_BABY = "### Row 160 baby picture" + MEMORY_BABY.split(")", 1)[1] if ")" in MEMORY_BABY else "### Row 160 baby picture" + MEMORY_BABY

ROW159_TAIL_OLD = (
    "Read the [memory sheet row 159 baby picture](appendix/memory-sheet.md#row-159-baby-picture-row68-row139-handshake3-meta-prelude-capstone-reunion) when opening [row 140](preface.md#skill-navigation-row-140) before row 59 closes; read the [epilogue row 159 closing loop](epilogue/multiscale.md#row-159-closing-loop) when the competence loop closes. When row 159 is complete, proceed to [row 140](preface.md#skill-navigation-row-140) when load cell parses at \\(T_w\\) but Handshake 3 still feels disconnected from Parts III–VI after verified Handshake 3 meta prelude capstone on the full capstone path, to [row 120](preface.md#skill-navigation-row-120) for the Row 68 ↔ Row 60 Handshake 3 meta audit on the opening-hinge capstone path alone, to [row 100](preface.md#skill-navigation-row-100) when the opening-hinge prelude path (row 99) closed the chapter hinge without row 158 prelude capstone, to [row 139](preface.md#skill-navigation-row-139) for the Row 68 ↔ Row 59 Handshake 3 meta audit on the opening-hinge capstone path alone,"
)
ROW159_TAIL_NEW = (
    "Read the [memory sheet row 159 baby picture](appendix/memory-sheet.md#row-159-baby-picture-row68-row139-handshake3-meta-prelude-capstone-reunion) when opening [row 160](preface.md#skill-navigation-row-160) before row 60 closes on the full capstone path; read the [epilogue row 159 closing loop](epilogue/multiscale.md#row-159-closing-loop) when the competence loop closes. When row 159 is complete, proceed to [row 160](preface.md#skill-navigation-row-160) when load cell parses at \\(T_w\\) but Handshake 3 still feels disconnected from Parts III–VI after verified Handshake 3 meta prelude capstone on the full capstone path, to [row 140](preface.md#skill-navigation-row-140) for the Row 68 ↔ Row 60 Handshake 3 meta audit on the opening-hinge capstone path alone, to [row 120](preface.md#skill-navigation-row-120) for the Row 68 ↔ Row 60 Handshake 3 meta audit on the opening-hinge prelude path alone, to [row 100](preface.md#skill-navigation-row-100) when the opening-hinge prelude path (row 99) closed the chapter hinge without row 159 prelude capstone, to [row 139](preface.md#skill-navigation-row-139) for the Row 68 ↔ Row 59 Handshake 3 meta audit on the opening-hinge capstone path alone,"
)


def main():
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    anchor = "\n## The copper wire through the book"
    if "skill-navigation-row-160" in preface:
        print("preface: row 160 already present")
    else:
        if ROW159_TAIL_OLD not in preface:
            raise SystemExit("preface row 159 tail not found")
        preface = preface.replace(ROW159_TAIL_OLD, ROW159_TAIL_NEW)
        preface = preface.replace(
            anchor,
            ROW160_PREFACE + anchor,
        )
        preface_path.write_text(preface)
        print("preface: added row 160")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-160" not in prologue:
        needle = "| Row 68 → Row 139 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion (row 159) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 159 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + PROLOGUE_COMPASS + prologue[line_end + 1 :]
        prologue = prologue.replace(
            "**Row 159 closing stitch",
            PROLOGUE_STITCH + "**Row 159 closing stitch",
        )
        prologue = prologue.replace(
            '| <span id="prologue-preview-row-159"></span>Row 159 preview',
            PROLOGUE_PREVIEW + '| <span id="prologue-preview-row-159"></span>Row 159 preview',
        )
        prologue_path.write_text(prologue)
        print("prologue: added row 160")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "row-160-closing-loop" not in epilogue:
        epilogue = epilogue.replace(
            "Proceed to [row 140](#row-140-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 159 on the full capstone path, when load cell parses at \\(T_w\\) after verified Handshake 3 meta prelude capstone but Handshake 3 still feels disconnected from Parts III–VI on the full capstone path,",
            "Proceed to [row 160](#row-160-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 159 on the full capstone path, when load cell parses at \\(T_w\\) after verified Handshake 3 meta prelude capstone but Handshake 3 still feels disconnected from Parts III–VI on the full capstone path,",
        )
        epilogue = epilogue.replace(
            "before row 140 Handshake 3 meta prelude capstone opens in workflow time on the full capstone path.",
            "before row 160 Handshake 3 meta prelude capstone reunion on the full capstone path (then row 141 Handshake 4a on the full capstone path).",
        )
        epilogue = epilogue.replace(
            "### Row 135 closing loop (Row 68 → Row 115",
            EPILOGUE_LOOP + "\n\n### Row 135 closing loop (Row 68 → Row 115",
        )
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 160")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row140-handshake3-meta-prelude-capstone-reunion-index-row-160" not in sources:
        sources = sources.replace(
            "| 159 | Row 68 → Row 139 Row 68 → Row 59 Handshake 3 meta prelude capstone",
            SOURCES_TABLE + "| 159 | Row 68 → Row 139 Row 68 → Row 59 Handshake 3 meta prelude capstone",
        )
        sources = sources.replace(
            "## Row 68 → Row 121 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 141)",
            SOURCES_INDEX + "## Row 68 → Row 121 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 141)",
        )
        sources = sources.replace(
            "before row 140 Handshake 3 meta prelude capstone opens.",
            "before row 140 Handshake 3 meta prelude capstone opens on the capstone path; [row 160](#row68-row140-handshake3-meta-prelude-capstone-reunion-index-row-160) reunites **Handshake 3 meta prelude capstone with the Handshake 3 meta boundary on the full capstone path** when row 159 closed DFT workflows meta prelude capstone at verified `alpha_export.yaml` but row 60 Handshake 3 meta still reads like separate courses on the full capstone path;",
        )
        sources_path.write_text(sources)
        print("sources: added row 160")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-160-baby-picture-row68-row140" not in memory:
        memory = memory.replace(
            "| 159 | Meta | [Row 68 → Row 139 Handshake 3 meta prelude capstone reunion index]",
            MEMORY_TABLE + "| 159 | Meta | [Row 68 → Row 139 Handshake 3 meta prelude capstone reunion index]",
        )
        memory = memory.replace(
            "### Row 131 baby picture (Row 68 → Row 111 Row 68 → Row 51 homogenization meta prelude capstone reunion)",
            MEMORY_BABY + "### Row 131 baby picture (Row 68 → Row 111 Row 68 → Row 51 homogenization meta prelude capstone reunion)",
        )
        memory_path.write_text(memory)
        print("memory-sheet: added row 160")


if __name__ == "__main__":
    main()
