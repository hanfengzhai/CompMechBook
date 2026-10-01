#!/usr/bin/env python3
"""Add row 162 meta-stitch (Row 68 → Row 142 ↔ Row 62 Handshake 4b meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def t142_to_162(text: str) -> str:
    """Transform row-142 capstone-path meta copy to row 162 (142→162, 122→142 inner, 141→161 gate)."""
    repl = [
        ("Row 68 → Row 122 Row 68 → Row 62", "Row 68 → Row 142 Row 68 → Row 62"),
        (
            "row68-row122-handshake4b-meta-prelude-capstone-reunion-index-row-142",
            "row68-row142-handshake4b-meta-prelude-capstone-reunion-index-row-162",
        ),
        (
            "row-142-baby-picture-row68-row122-handshake4b-meta-prelude-capstone-reunion",
            "row-162-baby-picture-row68-row142-handshake4b-meta-prelude-capstone-reunion",
        ),
        ("skill-navigation-row-142", "skill-navigation-row-162"),
        ("prologue-preview-row-142", "prologue-preview-row-162"),
        ("row-142-closing-stitch", "row-162-closing-stitch"),
        ("row-142-closing-loop", "row-162-closing-loop"),
        ("Row 142 three-way audit", "Row 162 three-way audit"),
        (
            "[row 141](preface.md#skill-navigation-row-141) or [row 122](preface.md#skill-navigation-row-122)",
            "[row 161](preface.md#skill-navigation-row-161) or [row 142](preface.md#skill-navigation-row-142)",
        ),
        (
            "[row 141](preface.md#skill-navigation-row-141) or [Row 68 → Row 102",
            "[row 161](preface.md#skill-navigation-row-161) or [Row 68 → Row 122",
        ),
        ("on the capstone path", "on the full capstone path"),
        ("(capstone path)", "(full capstone path)"),
        ("Row 68 ↔ Row 62 reunion (capstone path)", "Row 68 ↔ Row 62 reunion (full capstone path)"),
    ]
    out = text
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace("row 142", "row 162")
    out = out.replace("Row 142", "Row 162")
    out = out.replace("[row 162](preface.md#skill-navigation-row-161)", "[row 161](preface.md#skill-navigation-row-161)")
    out = out.replace("[row 162](preface.md#skill-navigation-row-142)", "[row 142](preface.md#skill-navigation-row-142)")
    out = out.replace("row 1623", "row 143")
    out = out.replace("row 1624", "row 144")
    out = out.replace("row 162 or row 162", "row 161 or row 142")
    out = out.replace("When row 162 closed — Handshake 4a", "When row 161 closed — Handshake 4a")
    out = out.replace("When row 162 closed — Handshake 4b", "When row 161 closed — Handshake 4b")
    out = out.replace("row 162 closed Handshake 4a", "row 161 closed Handshake 4a")
    out = out.replace("after row 162 alone", "after row 161 alone")
    out = out.replace("Recite [preface row 162]", "Recite [preface row 161]")
    out = out.replace("row 162 or row 142 recited", "row 161 or row 142 recited")
    out = out.replace("from row 162's", "from row 161's")
    out = out.replace(
        "verified Handshake 4a meta prelude capstone closure (row 162)",
        "verified Handshake 4a meta prelude capstone closure (row 161)",
    )
    out = out.replace(
        "verified Handshake 4a meta prelude capstone closure (row 141)",
        "verified Handshake 4a meta prelude capstone closure (row 161)",
    )
    out = out.replace("row 122", "row 142")
    out = out.replace("Row 122", "Row 142")
    out = out.replace("row 141", "row 161")
    out = out.replace("Row 141", "Row 161")
    out = out.replace(
        "before row 163 orchestration meta prelude capstone opens on the full capstone path",
        "before row 143 orchestration meta prelude capstone opens on the full capstone path",
    )
    out = out.replace(
        "Proceed to [row 163]",
        "Proceed to [row 143]",
    )
    out = out.replace(
        "Do not conflate row 162 (row 68 ↔ row 62 reunion on the full capstone path) with row 142",
        "Do not conflate row 162 (row 68 ↔ row 62 reunion on the full capstone path) with row 142",
    )
    out = out.replace(
        "row 142 names **Row 68 → Row 102 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion**",
        "row 142 names **Row 68 → Row 122 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion**",
    )
    out = out.replace(
        "Row 68 → Row 162 Row 68 → Row 62",
        "Row 68 → Row 142 Row 68 → Row 62",
    )
    out = out.replace("#skill-navigation-row-1623", "#skill-navigation-row-143")
    return out


def extract_preface_row142(preface: str) -> str:
    start = preface.index("### Row 142 skill checkpoint")
    end = preface.index("\n\n### Row 143 skill checkpoint")
    return preface[start:end]


ROW162_PREFACE = t142_to_162(
    extract_preface_row142((ROOT / "writings/preface/chapters/preface.md").read_text())
) + "\n\n"

PROLOGUE_COMPASS = (
    "| Row 68 → Row 142 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion (row 162) | "
    "[Preface: row 162 skill checkpoint](../preface.md#skill-navigation-row-162) · "
    "[Row 68 → Row 142 Handshake 4b meta prelude capstone reunion index](../appendix/sources.md#row68-row142-handshake4b-meta-prelude-capstone-reunion-index-row-162) · "
    "[memory sheet row 162 baby picture](../appendix/memory-sheet.md#row-162-baby-picture-row68-row142-handshake4b-meta-prelude-capstone-reunion) · "
    "[prologue row 162 preview row](#prologue-preview-row-162); [prologue row 162 closing stitch](#row-162-closing-stitch); "
    "[epilogue row 162 closing loop](../epilogue/multiscale.md#row-162-closing-loop) — "
    "read row 68 gate + row 161 or row 142 Handshake 4a meta prelude capstone / Handshake 4b meta capstone gate + epilogue FE² cross-links + row 62 meta aloud "
    "when bulk hardening matches flow stress after verified Handshake 4a meta prelude capstone on the full capstone path but the notch root under-predicts peak stress without FE² audit |\n"
)

PROLOGUE_STITCH = t142_to_162(
    "**Row 142 closing stitch (Row 68 → Row 122 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion).** {#row-142-closing-stitch} "
    "When row 141 closed — Handshake 4a meta prelude capstone verified, row 140 or row 121 recited on the capstone path, and [`parse_rate.sh`](../../scripts/parse_rate.sh) archived `rate_export.yaml` with lab grip rate matching [`fixtures/cht_export.yaml`](../../fixtures/cht_export.yaml) at \\(T_w\\) after verified Handshake 4a meta prelude capstone on the capstone path — "
    "but **row 62 Handshake 4b meta reunion still opens like standalone epilogue coursework after verified bulk hardening parsing on the capstone path** — "
    "read [preface row 142](../preface.md#skill-navigation-row-142), then the "
    "[Row 68 → Row 122 reunion index](../appendix/sources.md#row68-row122-handshake4b-meta-prelude-capstone-reunion-index-row-142), then "
    "[epilogue row 142 closing loop](../epilogue/multiscale.md#row-142-closing-loop) before row 143 orchestration meta prelude capstone opens on the capstone path.\n\n"
)

PROLOGUE_PREVIEW = (
    "| <span id=\"prologue-preview-row-162\"></span>Row 162 preview (Row 68 → Row 142 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion) | "
    "Explain why midpoint closure (row 68) and Handshake 4b meta (row 62) must be read together with the epilogue FE² cross-links and discretization chain "
    "after verified Handshake 4a meta prelude capstone on the full capstone path before Act IV hardening and Act V notch localization feel like separate courses | "
    "One sentence: \"read row 68 gate + row 161 or row 142 Handshake 4a meta prelude capstone / Handshake 4b meta capstone gate + epilogue FE² cross-links + row 62 meta aloud "
    "when bulk hardening matches flow stress after verified Handshake 4a meta prelude capstone on the full capstone path but the notch root under-predicts peak stress without FE² audit\" — "
    "[preface row 162 skill checkpoint](../preface.md#skill-navigation-row-162); [prologue row 162 closing stitch](#row-162-closing-stitch); "
    "[Row 68 → Row 142 reunion index](../appendix/sources.md#row68-row142-handshake4b-meta-prelude-capstone-reunion-index-row-162); "
    "[memory sheet row 162 baby picture](../appendix/memory-sheet.md#row-162-baby-picture-row68-row142-handshake4b-meta-prelude-capstone-reunion); "
    "[epilogue FE² cross-links audit](../epilogue/multiscale.md#opening-hinge-vii3-handshake4b); "
    "[preface row 62 skill checkpoint](../preface.md#skill-navigation-row-62); "
    "[preface row 161 skill checkpoint](../preface.md#skill-navigation-row-161); "
    "[epilogue row 162 closing loop](../epilogue/multiscale.md#row-162-closing-loop) |\n"
)

_epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
EPILOGUE_LOOP = t142_to_162(
    "### Row 142 closing loop"
    + _epilogue.split("### Row 142 closing loop")[1].split("### Row 143 closing loop")[0]
)

SOURCES_TABLE = (
    "| 162 | Row 68 → Row 142 Row 68 → Row 62 Handshake 4b meta prelude capstone (midpoint prelude gate ↔ Handshake 4b meta prelude capstone on full capstone path ↔ row 62 meta) | "
    "[Row 68 → Row 142 Handshake 4b meta prelude capstone reunion index](#row68-row142-handshake4b-meta-prelude-capstone-reunion-index-row-162) · "
    "[preface row 162](../preface.md#skill-navigation-row-162) · "
    "[prologue row 162 preview](../prologue/00-many-scales.md#prologue-preview-row-162) · "
    "[prologue row 162 closing stitch](../prologue/00-many-scales.md#row-162-closing-stitch) · "
    "[epilogue row 162 closing loop](../epilogue/multiscale.md#row-162-closing-loop) · "
    "[memory sheet row 162 baby picture](memory-sheet.md#row-162-baby-picture-row68-row142-handshake4b-meta-prelude-capstone-reunion) | "
    "Row 68 closed but **row 62 Handshake 4b meta reunion still feels disconnected from verified Handshake 4a meta prelude capstone on the full capstone path** — "
    "read row 68 + row 161 or row 142 gate + epilogue FE² cross-links + row 62; "
    "[preface row 62](../preface.md#skill-navigation-row-62) |\n"
)

SOURCES_INDEX = t142_to_162(
    (ROOT / "writings/appendix/chapters/sources.md")
    .read_text()
    .split("## Row 68 → Row 122 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion index (row 142)")[1]
    .split("## Row 68 → Row 123 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 143)")[0]
)
SOURCES_INDEX = (
    "## Row 68 → Row 142 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion index (row 162)"
    + SOURCES_INDEX
)

MEMORY_TABLE = (
    "| 162 | Meta | [Row 68 → Row 142 Handshake 4b meta prelude capstone reunion index](sources.md#row68-row142-handshake4b-meta-prelude-capstone-reunion-index-row-162) · "
    "[preface row 162 skill checkpoint](../preface.md#skill-navigation-row-162) · "
    "[prologue row 162 preview](../prologue/00-many-scales.md#prologue-preview-row-162) · "
    "[prologue row 162 closing stitch](../prologue/00-many-scales.md#row-162-closing-stitch) · "
    "[epilogue row 162 closing loop](../epilogue/multiscale.md#row-162-closing-loop) | "
    "Row 68 closed but row 62 Handshake 4b meta reunion feels disconnected from verified Handshake 4a meta prelude capstone on the full capstone path — "
    "read row 68 + row 161 or row 142 gate + epilogue FE² cross-links + row 62; "
    "[row 162 baby picture](#row-162-baby-picture-row68-row142-handshake4b-meta-prelude-capstone-reunion) |\n"
)

MEMORY_BABY = t142_to_162(
    (ROOT / "writings/appendix/chapters/memory-sheet.md")
    .read_text()
    .split("### Row 142 baby picture")[1]
    .split("### Row 143 baby picture")[0]
)
MEMORY_BABY = "### Row 162 baby picture" + MEMORY_BABY.split(")", 1)[1] if ")" in MEMORY_BABY else "### Row 162 baby picture" + MEMORY_BABY

ROW161_TAIL_OLD = (
    "Read the [memory sheet row 161 baby picture](appendix/memory-sheet.md#row-161-baby-picture-row68-row141-handshake4a-meta-prelude-capstone-reunion) when opening [row 142](preface.md#skill-navigation-row-142) before row 61 closes; read the [epilogue row 161 closing loop](epilogue/multiscale.md#row-161-closing-loop) when the competence loop closes. When row 161 is complete, proceed to [row 142](preface.md#skill-navigation-row-142) when row 68 closed but Handshake 4b meta still feels disconnected after Handshake 4a meta prelude capstone on the full capstone path, to [row 122](preface.md#skill-navigation-row-122) for the Row 68 ↔ Row 62 meta audit on the opening-hinge capstone path alone, to [row 102](preface.md#skill-navigation-row-102) for the Row 68 ↔ Row 62 meta audit on the opening-hinge prelude path alone, to [row 141](preface.md#skill-navigation-row-141) for the Row 68 ↔ Row 61 meta audit on the opening-hinge capstone path alone, to [row 160](preface.md#skill-navigation-row-160) when Handshake 3 meta prelude capstone still lags after verified Handshake 3 meta prelude capstone on the full capstone path, to [row 81](preface.md#skill-navigation-row-81) for the Row 68 ↔ Row 61 opening prelude audit alone, to [row 61](preface.md#skill-navigation-row-61) for the Row 60 ↔ Row 41 meta audit alone, to [row 41](preface.md#skill-navigation-row-41) for the full VII.3 → Handshake 4a meta audit, or extend prose only under `writings/` then sync."
)
ROW161_TAIL_NEW = (
    "Read the [memory sheet row 161 baby picture](appendix/memory-sheet.md#row-161-baby-picture-row68-row141-handshake4a-meta-prelude-capstone-reunion) when opening [row 162](preface.md#skill-navigation-row-162) before row 62 closes on the full capstone path; read the [epilogue row 161 closing loop](epilogue/multiscale.md#row-161-closing-loop) when the competence loop closes. When row 161 is complete, proceed to [row 162](preface.md#skill-navigation-row-162) when bulk hardening matches flow stress but Handshake 4b still feels disconnected from Part VII Step 4 after verified Handshake 4a meta prelude capstone on the full capstone path, to [row 142](preface.md#skill-navigation-row-142) for the Row 68 ↔ Row 62 Handshake 4b meta audit on the opening-hinge capstone path alone, to [row 122](preface.md#skill-navigation-row-122) for the Row 68 ↔ Row 62 meta audit on the opening-hinge capstone path alone, to [row 102](preface.md#skill-navigation-row-102) for the Row 68 ↔ Row 62 meta audit on the opening-hinge prelude path alone, to [row 141](preface.md#skill-navigation-row-141) for the Row 68 ↔ Row 61 meta audit on the opening-hinge capstone path alone, to [row 160](preface.md#skill-navigation-row-160) when Handshake 3 meta prelude capstone still lags after verified Handshake 3 meta prelude capstone on the full capstone path, to [row 82](preface.md#skill-navigation-row-82) for the Row 68 ↔ Row 62 opening prelude audit alone, to [row 62](preface.md#skill-navigation-row-62) for the Row 61 ↔ Row 42 meta audit alone, to [row 42](preface.md#skill-navigation-row-42) for the full VII.3 → Handshake 4b meta audit, or extend prose only under `writings/` then sync."
)

ROW161_STITCH_OLD = "before row 142 Handshake 4b meta prelude capstone opens on the full capstone path"
ROW161_STITCH_NEW = "before row 162 Handshake 4b meta prelude capstone reunion on the full capstone path (then row 143 orchestration meta prelude capstone on the full capstone path)"

ROW161_EPILOGUE_PROCEED_OLD = (
    "Proceed to [row 142](#row-142-closing-loop) when row 68 closed but Handshake 4b meta still feels disconnected after row 161 on the full capstone path,"
)
ROW161_EPILOGUE_PROCEED_NEW = (
    "Proceed to [row 162](#row-162-closing-loop) when row 68 closed but Handshake 4b meta still feels disconnected after row 161 on the full capstone path,"
)

ROW161_BABY_OLD = (
    "row 161 when **epilogue rate cross-links and Row 60 → Row 41 Handshake 4a meta must read on the same wire before row 142 Handshake 4b meta prelude capstone opens on the full capstone path**"
)
ROW161_BABY_NEW = (
    "row 161 when **epilogue rate cross-links and Row 60 → Row 41 Handshake 4a meta must read on the same wire before row 162 Handshake 4b meta prelude capstone reunion opens on the full capstone path**"
)


def main():
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    anchor = "\n## The copper wire through the book"
    if "skill-navigation-row-162" in preface:
        print("preface: row 162 already present")
    else:
        if ROW161_TAIL_OLD not in preface:
            raise SystemExit("preface row 161 tail not found")
        preface = preface.replace(ROW161_TAIL_OLD, ROW161_TAIL_NEW)
        preface = preface.replace(
            anchor,
            ROW162_PREFACE + anchor,
        )
        preface_path.write_text(preface)
        print("preface: added row 162")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-162" not in prologue:
        needle = "| Row 68 → Row 141 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion (row 161) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 161 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + PROLOGUE_COMPASS + prologue[line_end + 1 :]
        prologue = prologue.replace(
            "**Row 161 closing stitch",
            PROLOGUE_STITCH + "**Row 161 closing stitch",
        )
        prologue = prologue.replace(
            '| <span id="prologue-preview-row-161"></span>Row 161 preview',
            PROLOGUE_PREVIEW + '| <span id="prologue-preview-row-161"></span>Row 161 preview',
        )
        prologue = prologue.replace(ROW161_STITCH_OLD, ROW161_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 162")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "row-162-closing-loop" not in epilogue:
        if ROW161_EPILOGUE_PROCEED_OLD in epilogue:
            epilogue = epilogue.replace(ROW161_EPILOGUE_PROCEED_OLD, ROW161_EPILOGUE_PROCEED_NEW)
        epilogue = epilogue.replace(
            "or extend prose only under `writings/` then sync.\n\n\n\n\n### Row 135 closing loop (Row 68 → Row 115",
            "or extend prose only under `writings/` then sync.\n\n\n" + EPILOGUE_LOOP + "\n\n### Row 135 closing loop (Row 68 → Row 115",
            1,
        )
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 162")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row142-handshake4b-meta-prelude-capstone-reunion-index-row-162" not in sources:
        sources = sources.replace(
            "| 161 | Row 68 → Row 141 Row 68 → Row 61 Handshake 4a meta prelude capstone",
            SOURCES_TABLE + "| 161 | Row 68 → Row 141 Row 68 → Row 61 Handshake 4a meta prelude capstone",
        )
        sources = sources.replace(
            "## Row 68 → Row 123 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 143)",
            SOURCES_INDEX + "## Row 68 → Row 123 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 143)",
        )
        sources = sources.replace(
            "before row 142 Handshake 4b meta prelude capstone opens on the full capstone path;",
            "before row 142 Handshake 4b meta prelude capstone opens on the capstone path; [row 162](#row68-row142-handshake4b-meta-prelude-capstone-reunion-index-row-162) reunites **Handshake 4b meta prelude capstone with the Handshake 4b meta boundary on the full capstone path** when row 161 closed Handshake 4a meta prelude capstone at verified bulk hardening pedigree but row 62 Handshake 4b meta still reads like separate courses on the full capstone path;",
        )
        sources_path.write_text(sources)
        print("sources: added row 162")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-162-baby-picture-row68-row142" not in memory:
        memory = memory.replace(
            "| 161 | Meta | [Row 68 → Row 141 Handshake 4a meta prelude capstone reunion index]",
            MEMORY_TABLE + "| 161 | Meta | [Row 68 → Row 141 Handshake 4a meta prelude capstone reunion index]",
        )
        memory = memory.replace(
            "### Row 131 baby picture (Row 68 → Row 111 Row 68 → Row 51 homogenization meta prelude capstone reunion)",
            MEMORY_BABY + "### Row 131 baby picture (Row 68 → Row 111 Row 68 → Row 51 homogenization meta prelude capstone reunion)",
        )
        memory = memory.replace(ROW161_BABY_OLD, ROW161_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 162")


if __name__ == "__main__":
    main()
