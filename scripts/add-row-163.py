#!/usr/bin/env python3
"""Add row 163 meta-stitch (Row 68 → Row 143 ↔ Row 63 orchestration meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def t143_to_163(text: str) -> str:
    """Transform row-143 capstone-path meta copy to row 163 (143→163, 123→143 inner, 142→162 gate)."""
    repl = [
        ("Row 68 → Row 123 Row 68 → Row 63", "Row 68 → Row 143 Row 68 → Row 63"),
        (
            "row68-row123-orchestration-meta-prelude-capstone-reunion-index-row-143",
            "row68-row143-orchestration-meta-prelude-capstone-reunion-index-row-163",
        ),
        (
            "row-143-baby-picture-row68-row123-orchestration-meta-prelude-capstone-reunion",
            "row-163-baby-picture-row68-row143-orchestration-meta-prelude-capstone-reunion",
        ),
        ("skill-navigation-row-143", "skill-navigation-row-163"),
        ("prologue-preview-row-143", "prologue-preview-row-163"),
        ("row-143-closing-stitch", "row-163-closing-stitch"),
        ("row-143-closing-loop", "row-163-closing-loop"),
        ("Row 143 three-way audit", "Row 163 three-way audit"),
        (
            "[row 142](preface.md#skill-navigation-row-142) or [row 123](preface.md#skill-navigation-row-123)",
            "[row 162](preface.md#skill-navigation-row-162) or [row 143](preface.md#skill-navigation-row-143)",
        ),
        (
            "[row 142](preface.md#skill-navigation-row-142) or [Row 68 → Row 103",
            "[row 162](preface.md#skill-navigation-row-162) or [Row 68 → Row 123",
        ),
        ("on the capstone path", "on the full capstone path"),
        ("(capstone path)", "(full capstone path)"),
        ("Row 68 ↔ Row 63 reunion (capstone path)", "Row 68 ↔ Row 63 reunion (full capstone path)"),
    ]
    out = text
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace("row 143", "row 163")
    out = out.replace("Row 143", "Row 163")
    out = out.replace("[row 163](preface.md#skill-navigation-row-162)", "[row 162](preface.md#skill-navigation-row-162)")
    out = out.replace("[row 163](preface.md#skill-navigation-row-143)", "[row 143](preface.md#skill-navigation-row-143)")
    out = out.replace("row 1634", "row 164")
    out = out.replace("row 1635", "row 165")
    out = out.replace("row 163 or row 163", "row 162 or row 143")
    out = out.replace("When row 163 closed — orchestration", "When row 162 closed — orchestration")
    out = out.replace("When row 163 closed — Handshake 4b", "When row 162 closed — Handshake 4b")
    out = out.replace("row 163 closed orchestration", "row 162 closed orchestration")
    out = out.replace("after row 163 alone", "after row 162 alone")
    out = out.replace("Recite [preface row 163]", "Recite [preface row 162]")
    out = out.replace("row 163 or row 143 recited", "row 162 or row 143 recited")
    out = out.replace("from row 163's", "from row 162's")
    out = out.replace(
        "verified orchestration meta prelude capstone closure (row 163)",
        "verified orchestration meta prelude capstone closure (row 162)",
    )
    out = out.replace(
        "verified Handshake 4b meta prelude capstone closure (row 163)",
        "verified Handshake 4b meta prelude capstone closure (row 162)",
    )
    out = out.replace(
        "verified Handshake 4b meta prelude capstone closure (row 142)",
        "verified Handshake 4b meta prelude capstone closure (row 162)",
    )
    out = out.replace("row 123", "row 143")
    out = out.replace("Row 123", "Row 143")
    out = out.replace("row 142", "row 162")
    out = out.replace("Row 142", "Row 162")
    out = out.replace(
        "before row 164 book-loop meta prelude capstone opens on the full capstone path",
        "before row 144 book-loop meta prelude capstone opens on the full capstone path",
    )
    out = out.replace(
        "Proceed to [row 164]",
        "Proceed to [row 144]",
    )
    out = out.replace(
        "Do not conflate row 163 (row 68 ↔ row 63 reunion on the full capstone path) with row 143",
        "Do not conflate row 163 (row 68 ↔ row 63 reunion on the full capstone path) with row 143",
    )
    out = out.replace(
        "row 143 names **Row 68 → Row 103 Row 68 → Row 63 orchestration meta prelude capstone reunion**",
        "row 143 names **Row 68 → Row 123 Row 68 → Row 63 orchestration meta prelude capstone reunion**",
    )
    out = out.replace(
        "Row 68 → Row 163 Row 68 → Row 63",
        "Row 68 → Row 143 Row 68 → Row 63",
    )
    out = out.replace("#skill-navigation-row-1634", "#skill-navigation-row-144")
    out = out.replace("#skill-navigation-row-142)", "#skill-navigation-row-162)")
    out = out.replace("#skill-navigation-row-123)", "#skill-navigation-row-143)")
    out = out.replace(
        "row68-row103-orchestration-meta-prelude-capstone-reunion-index-row-123",
        "row68-row143-orchestration-meta-prelude-capstone-reunion-index-row-143",
    )
    out = out.replace(
        "row68-row122-handshake4b-meta-prelude-capstone-reunion-index-row-142",
        "row68-row142-handshake4b-meta-prelude-capstone-reunion-index-row-162",
    )
    out = out.replace("#row-123-closing-loop)", "#row-143-closing-loop)")
    out = out.replace("#row-142-closing-loop)", "#row-162-closing-loop)")
    out = out.replace(
        "Row 143 names **Row 68 → Row 103 Row 68 → Row 63 orchestration meta prelude reunion**",
        "Row 143 names **Row 68 → Row 123 Row 68 → Row 63 orchestration meta prelude reunion**",
    )
    out = out.replace(
        "row 162 names **Row 68 → Row 122 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion**",
        "row 162 names **Row 68 → Row 142 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion**",
    )
    return out


def extract_preface_row143(preface: str) -> str:
    start = preface.index("### Row 143 skill checkpoint")
    end = preface.index("\n\n### Row 144 skill checkpoint")
    return preface[start:end]


ROW163_PREFACE = t143_to_163(
    extract_preface_row143((ROOT / "writings/preface/chapters/preface.md").read_text())
) + "\n\n"

PROLOGUE_COMPASS = (
    "| Row 68 → Row 143 Row 68 → Row 63 orchestration meta prelude capstone reunion (row 163) | "
    "[Preface: row 163 skill checkpoint](../preface.md#skill-navigation-row-163) · "
    "[Row 68 → Row 143 orchestration meta prelude capstone reunion index](../appendix/sources.md#row68-row143-orchestration-meta-prelude-capstone-reunion-index-row-163) · "
    "[memory sheet row 163 baby picture](../appendix/memory-sheet.md#row-163-baby-picture-row68-row143-orchestration-meta-prelude-capstone-reunion) · "
    "[prologue row 163 preview row](#prologue-preview-row-163); [prologue row 163 closing stitch](#row-163-closing-stitch); "
    "[epilogue row 163 closing loop](../epilogue/multiscale.md#row-163-closing-loop) — "
    "read row 68 gate + row 162 or row 143 Handshake 4b meta prelude capstone / orchestration meta capstone gate + epilogue orchestration cross-links + row 63 meta aloud "
    "when Handshakes 1–4b verify individually after Handshake 4b meta prelude capstone on the full capstone path but Act V notch and Act VI foundation still feel like separate afternoons without orchestrated `multiscale_export.yaml` |\n"
)

PROLOGUE_STITCH = t143_to_163(
    "**Row 143 closing stitch (Row 68 → Row 123 Row 68 → Row 63 orchestration meta prelude capstone reunion).** {#row-143-closing-stitch} "
    "When row 142 closed — Handshake 4b meta prelude capstone verified, row 141 or row 122 recited on the capstone path, and [`parse_fe2.sh`](../../scripts/parse_fe2.sh) archived `fe2_export.yaml` with enrichment when uplift exceeds 10% after verified Handshake 4a meta prelude capstone on the capstone path — "
    "but **row 63 orchestration meta reunion still opens like standalone epilogue coursework after verified notch-root parsing on the capstone path** — "
    "read [preface row 143](../preface.md#skill-navigation-row-143), then the "
    "[Row 68 → Row 123 reunion index](../appendix/sources.md#row68-row123-orchestration-meta-prelude-capstone-reunion-index-row-143), then "
    "[epilogue row 143 closing loop](../epilogue/multiscale.md#row-143-closing-loop) before row 144 book-loop meta prelude capstone opens on the capstone path.\n\n"
)

PROLOGUE_PREVIEW = (
    "| <span id=\"prologue-preview-row-163\"></span>Row 163 preview (Row 68 → Row 143 Row 68 → Row 63 orchestration meta prelude capstone reunion) | "
    "Explain why midpoint closure (row 68) and orchestration meta (row 63) must be read together with the epilogue orchestration cross-links and H1→OUT chain "
    "after verified Handshake 4b meta prelude capstone on the full capstone path before Act V notch and Act VI foundation feel like separate courses | "
    "One sentence: \"read row 68 gate + row 162 or row 143 Handshake 4b meta prelude capstone / orchestration meta capstone gate + epilogue orchestration cross-links + row 63 meta aloud "
    "when Handshakes 1–4b verify individually after Handshake 4b meta prelude capstone on the full capstone path but Act V notch and Act VI foundation still feel like separate afternoons without orchestrated `multiscale_export.yaml`\" — "
    "[preface row 163 skill checkpoint](../preface.md#skill-navigation-row-163); [prologue row 163 closing stitch](#row-163-closing-stitch); "
    "[Row 68 → Row 143 reunion index](../appendix/sources.md#row68-row143-orchestration-meta-prelude-capstone-reunion-index-row-163); "
    "[memory sheet row 163 baby picture](../appendix/memory-sheet.md#row-163-baby-picture-row68-row143-orchestration-meta-prelude-capstone-reunion); "
    "[epilogue orchestration cross-links audit](../epilogue/multiscale.md#opening-hinge-rows17-42-row16); "
    "[preface row 63 skill checkpoint](../preface.md#skill-navigation-row-63); "
    "[preface row 162 skill checkpoint](../preface.md#skill-navigation-row-162); "
    "[epilogue row 163 closing loop](../epilogue/multiscale.md#row-163-closing-loop) |\n"
)

_epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
EPILOGUE_LOOP = t143_to_163(
    "### Row 143 closing loop"
    + _epilogue.split("### Row 143 closing loop")[1].split("### Row 144 closing loop")[0]
)

SOURCES_TABLE = (
    "| 163 | Row 68 → Row 143 Row 68 → Row 63 orchestration meta prelude capstone (midpoint prelude gate ↔ orchestration meta prelude capstone on full capstone path ↔ row 63 meta) | "
    "[Row 68 → Row 143 orchestration meta prelude capstone reunion index](#row68-row143-orchestration-meta-prelude-capstone-reunion-index-row-163) · "
    "[preface row 163](../preface.md#skill-navigation-row-163) · "
    "[prologue row 163 preview](../prologue/00-many-scales.md#prologue-preview-row-163) · "
    "[prologue row 163 closing stitch](../prologue/00-many-scales.md#row-163-closing-stitch) · "
    "[epilogue row 163 closing loop](../epilogue/multiscale.md#row-163-closing-loop) · "
    "[memory sheet row 163 baby picture](memory-sheet.md#row-163-baby-picture-row68-row143-orchestration-meta-prelude-capstone-reunion) | "
    "Row 68 closed but **row 63 orchestration meta reunion still feels disconnected from verified Handshake 4b meta prelude capstone on the full capstone path** — "
    "read row 68 + row 162 or row 143 gate + epilogue orchestration cross-links + row 63; "
    "[preface row 63](../preface.md#skill-navigation-row-63) |\n"
)

SOURCES_INDEX = t143_to_163(
    (ROOT / "writings/appendix/chapters/sources.md")
    .read_text()
    .split("## Row 68 → Row 123 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 143)")[1]
    .split("## Row 68 → Row 100 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 120)")[0]
)
SOURCES_INDEX = (
    "## Row 68 → Row 143 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 163)"
    + SOURCES_INDEX
)

MEMORY_TABLE = (
    "| 163 | Meta | [Row 68 → Row 143 orchestration meta prelude capstone reunion index](sources.md#row68-row143-orchestration-meta-prelude-capstone-reunion-index-row-163) · "
    "[preface row 163 skill checkpoint](../preface.md#skill-navigation-row-163) · "
    "[prologue row 163 preview](../prologue/00-many-scales.md#prologue-preview-row-163) · "
    "[prologue row 163 closing stitch](../prologue/00-many-scales.md#row-163-closing-stitch) · "
    "[epilogue row 163 closing loop](../epilogue/multiscale.md#row-163-closing-loop) | "
    "Row 68 closed but row 63 orchestration meta reunion feels disconnected from verified Handshake 4b meta prelude capstone on the full capstone path — "
    "read row 68 + row 162 or row 143 gate + epilogue orchestration cross-links + row 63; "
    "[row 163 baby picture](#row-163-baby-picture-row68-row143-orchestration-meta-prelude-capstone-reunion) |\n"
)

MEMORY_BABY = t143_to_163(
    (ROOT / "writings/appendix/chapters/memory-sheet.md")
    .read_text()
    .split("### Row 143 baby picture")[1]
    .split("### Row 144 baby picture")[0]
)
MEMORY_BABY = "### Row 163 baby picture" + MEMORY_BABY.split(")", 1)[1] if ")" in MEMORY_BABY else "### Row 163 baby picture" + MEMORY_BABY

ROW162_TAIL_OLD = (
    "Read the [memory sheet row 162 baby picture](appendix/memory-sheet.md#row-162-baby-picture-row68-row142-handshake4b-meta-prelude-capstone-reunion) when opening [row 143](preface.md#skill-navigation-row-143) before row 62 closes; read the [epilogue row 162 closing loop](epilogue/multiscale.md#row-162-closing-loop) when the competence loop closes. When row 162 is complete, proceed to [row 143](preface.md#skill-navigation-row-143) when row 68 closed but orchestration meta still feels disconnected after Handshake 4b meta prelude capstone on the full capstone path, to [row 123](preface.md#skill-navigation-row-123) for the Row 68 ↔ Row 63 meta audit on the opening-hinge capstone path alone, to [row 103](preface.md#skill-navigation-row-103) for the Row 68 ↔ Row 63 meta audit on the opening-hinge prelude path alone, to [row 142](preface.md#skill-navigation-row-142) for the Row 68 ↔ Row 62 Handshake 4b meta audit on the opening-hinge capstone path alone, to [row 122](preface.md#skill-navigation-row-122) for the Row 68 ↔ Row 62 meta audit on the opening-hinge capstone path alone, to [row 102](preface.md#skill-navigation-row-102) for the Row 68 ↔ Row 62 meta audit on the opening-hinge prelude path alone, to [row 161](preface.md#skill-navigation-row-161) when Handshake 4a meta prelude capstone still lags after verified Handshake 4a meta prelude capstone on the full capstone path, to [row 82](preface.md#skill-navigation-row-82) for the Row 68 ↔ Row 62 opening prelude audit alone, to [row 62](preface.md#skill-navigation-row-62) for the Row 61 ↔ Row 42 meta audit alone, to [row 42](preface.md#skill-navigation-row-42) for the full VII.3 → Handshake 4b meta audit, or extend prose only under `writings/` then sync."
)
ROW162_TAIL_NEW = (
    "Read the [memory sheet row 162 baby picture](appendix/memory-sheet.md#row-162-baby-picture-row68-row142-handshake4b-meta-prelude-capstone-reunion) when opening [row 163](preface.md#skill-navigation-row-163) before row 63 closes on the full capstone path; read the [epilogue row 162 closing loop](epilogue/multiscale.md#row-162-closing-loop) when the competence loop closes. When row 162 is complete, proceed to [row 163](preface.md#skill-navigation-row-163) when Handshakes 1–4b verify individually but orchestration meta still feels disconnected from Act VI foundation after verified Handshake 4b meta prelude capstone on the full capstone path, to [row 143](preface.md#skill-navigation-row-143) for the Row 68 ↔ Row 63 orchestration meta audit on the opening-hinge capstone path alone, to [row 123](preface.md#skill-navigation-row-123) for the Row 68 ↔ Row 63 meta audit on the opening-hinge capstone path alone, to [row 103](preface.md#skill-navigation-row-103) for the Row 68 ↔ Row 63 meta audit on the opening-hinge prelude path alone, to [row 142](preface.md#skill-navigation-row-142) for the Row 68 ↔ Row 62 Handshake 4b meta audit on the opening-hinge capstone path alone, to [row 122](preface.md#skill-navigation-row-122) for the Row 68 ↔ Row 62 meta audit on the opening-hinge capstone path alone, to [row 102](preface.md#skill-navigation-row-102) for the Row 68 ↔ Row 62 meta audit on the opening-hinge prelude path alone, to [row 161](preface.md#skill-navigation-row-161) when Handshake 4a meta prelude capstone still lags after verified Handshake 4a meta prelude capstone on the full capstone path, to [row 83](preface.md#skill-navigation-row-83) for the Row 68 ↔ Row 63 opening prelude audit alone, to [row 63](preface.md#skill-navigation-row-63) for the Row 62 ↔ Row 43 meta audit alone, to [row 43](preface.md#skill-navigation-row-43) for the full Rows 17–42 → row 16 meta audit, or extend prose only under `writings/` then sync."
)

ROW162_STITCH_OLD = "before row 143 orchestration meta prelude capstone opens on the full capstone path"
ROW162_STITCH_NEW = (
    "before row 163 orchestration meta prelude capstone reunion on the full capstone path "
    "(then row 144 book-loop meta prelude capstone on the full capstone path)"
)

ROW162_EPILOGUE_PROCEED_OLD = (
    "Proceed to [row 143](#row-143-closing-loop) when row 68 closed but orchestration meta still feels disconnected after row 162 on the full capstone path,"
)
ROW162_EPILOGUE_PROCEED_NEW = (
    "Proceed to [row 163](#row-163-closing-loop) when row 68 closed but orchestration meta still feels disconnected after row 162 on the full capstone path,"
)

ROW162_BABY_OLD = (
    "row 162 when **epilogue FE² cross-links and Row 61 → Row 42 Handshake 4b meta must read on the same wire before row 143 orchestration meta prelude capstone reunion opens on the full capstone path**"
)
ROW162_BABY_NEW = (
    "row 162 when **epilogue FE² cross-links and Row 61 → Row 42 Handshake 4b meta must read on the same wire before row 163 orchestration meta prelude capstone reunion opens on the full capstone path**"
)


def main():
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    anchor = "\n## The copper wire through the book"
    if "skill-navigation-row-163" in preface:
        print("preface: row 163 already present")
    else:
        if ROW162_TAIL_OLD not in preface:
            raise SystemExit("preface row 162 tail not found")
        preface = preface.replace(ROW162_TAIL_OLD, ROW162_TAIL_NEW)
        preface = preface.replace(
            anchor,
            ROW163_PREFACE + anchor,
        )
        preface_path.write_text(preface)
        print("preface: added row 163")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-163" not in prologue:
        needle = "| Row 68 → Row 142 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion (row 162) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 162 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + PROLOGUE_COMPASS + prologue[line_end + 1 :]
        prologue = prologue.replace(
            "**Row 162 closing stitch",
            PROLOGUE_STITCH + "**Row 162 closing stitch",
        )
        prologue = prologue.replace(
            '| <span id="prologue-preview-row-162"></span>Row 162 preview',
            PROLOGUE_PREVIEW + '| <span id="prologue-preview-row-162"></span>Row 162 preview',
        )
        prologue = prologue.replace(ROW162_STITCH_OLD, ROW162_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 163")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "row-163-closing-loop" not in epilogue:
        if ROW162_EPILOGUE_PROCEED_OLD in epilogue:
            epilogue = epilogue.replace(ROW162_EPILOGUE_PROCEED_OLD, ROW162_EPILOGUE_PROCEED_NEW)
        marker = (
            "to [row 62](#row-62-closing-loop) when only Handshake 4b meta stalls, or extend prose only under `writings/` then sync.\n\n\n\n\n### Row 135 closing loop"
        )
        replacement = (
            "to [row 62](#row-62-closing-loop) when only Handshake 4b meta stalls, or extend prose only under `writings/` then sync.\n\n\n"
            + EPILOGUE_LOOP
            + "\n\n### Row 135 closing loop"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 162 end marker not found")
        epilogue = epilogue.replace(marker, replacement, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 163")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row143-orchestration-meta-prelude-capstone-reunion-index-row-163" not in sources:
        sources = sources.replace(
            "| 162 | Row 68 → Row 142 Row 68 → Row 62 Handshake 4b meta prelude capstone",
            SOURCES_TABLE + "| 162 | Row 68 → Row 142 Row 68 → Row 62 Handshake 4b meta prelude capstone",
        )
        sources = sources.replace(
            "## Row 68 → Row 123 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 143)",
            SOURCES_INDEX + "## Row 68 → Row 123 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 143)",
        )
        sources = sources.replace(
            "before row 143 orchestration meta prelude capstone reunion opens on the capstone path;",
            "before row 143 orchestration meta prelude capstone reunion opens on the capstone path; [row 163](#row68-row143-orchestration-meta-prelude-capstone-reunion-index-row-163) reunites **orchestration meta prelude capstone with the orchestration meta boundary on the full capstone path** when row 162 closed Handshake 4b meta prelude capstone at verified notch pedigree but row 63 orchestration meta still reads like separate courses on the full capstone path;",
        )
        sources_path.write_text(sources)
        print("sources: added row 163")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-163-baby-picture-row68-row143" not in memory:
        memory = memory.replace(
            "| 162 | Meta | [Row 68 → Row 142 Handshake 4b meta prelude capstone reunion index]",
            MEMORY_TABLE + "| 162 | Meta | [Row 68 → Row 142 Handshake 4b meta prelude capstone reunion index]",
        )
        memory = memory.replace(
            "### Row 162 baby picture {#row-162-baby-picture-row68-row142-handshake4b-meta-prelude-capstone-reunion}",
            MEMORY_BABY + "### Row 162 baby picture {#row-162-baby-picture-row68-row142-handshake4b-meta-prelude-capstone-reunion}",
        )
        memory = memory.replace(ROW162_BABY_OLD, ROW162_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 163")


if __name__ == "__main__":
    main()
