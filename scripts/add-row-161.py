#!/usr/bin/env python3
"""Add row 161 meta-stitch (Row 68 → Row 141 ↔ Row 61 Handshake 4a meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def t141_to_161(text: str) -> str:
    """Transform row-141 capstone-path meta copy to row 161 (141→161, 121→141 inner, 140→160 gate)."""
    repl = [
        ("Row 68 → Row 121 Row 68 → Row 61", "Row 68 → Row 141 Row 68 → Row 61"),
        (
            "row68-row121-handshake4a-meta-prelude-capstone-reunion-index-row-141",
            "row68-row141-handshake4a-meta-prelude-capstone-reunion-index-row-161",
        ),
        (
            "row-141-baby-picture-row68-row121-handshake4a-meta-prelude-capstone-reunion",
            "row-161-baby-picture-row68-row141-handshake4a-meta-prelude-capstone-reunion",
        ),
        ("skill-navigation-row-141", "skill-navigation-row-161"),
        ("prologue-preview-row-141", "prologue-preview-row-161"),
        ("row-141-closing-stitch", "row-161-closing-stitch"),
        ("row-141-closing-loop", "row-161-closing-loop"),
        ("Row 141 three-way audit", "Row 161 three-way audit"),
        (
            "[row 140](preface.md#skill-navigation-row-140) or [row 121](preface.md#skill-navigation-row-121)",
            "[row 160](preface.md#skill-navigation-row-160) or [row 141](preface.md#skill-navigation-row-141)",
        ),
        (
            "[row 140](preface.md#skill-navigation-row-140) or [Row 68 → Row 101",
            "[row 160](preface.md#skill-navigation-row-160) or [Row 68 → Row 121",
        ),
        ("on the capstone path", "on the full capstone path"),
        ("(capstone path)", "(full capstone path)"),
        ("Row 68 ↔ Row 61 reunion (capstone path)", "Row 68 ↔ Row 61 reunion (full capstone path)"),
    ]
    out = text
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace("row 141", "row 161")
    out = out.replace("Row 141", "Row 161")
    out = out.replace("[row 161](preface.md#skill-navigation-row-160)", "[row 160](preface.md#skill-navigation-row-160)")
    out = out.replace("[row 161](preface.md#skill-navigation-row-141)", "[row 141](preface.md#skill-navigation-row-141)")
    out = out.replace("row 1617", "row 157")
    out = out.replace("row 1618", "row 158")
    out = out.replace("row 161 or row 161", "row 160 or row 141")
    out = out.replace("When row 161 closed — Handshake 4a", "When row 160 closed — Handshake 4a")
    out = out.replace("When row 161 closed — Handshake 3", "When row 160 closed — Handshake 3")
    out = out.replace("row 161 closed Handshake 4a", "row 160 closed Handshake 4a")
    out = out.replace("after row 161 alone", "after row 160 alone")
    out = out.replace("Recite [preface row 161]", "Recite [preface row 160]")
    out = out.replace("row 161 or row 141 recited", "row 160 or row 141 recited")
    out = out.replace("from row 161's", "from row 160's")
    out = out.replace(
        "verified Handshake 4a meta prelude capstone closure (row 161)",
        "verified Handshake 4a meta prelude capstone closure (row 160)",
    )
    out = out.replace(
        "verified Handshake 4a meta prelude capstone closure (row 140)",
        "verified Handshake 4a meta prelude capstone closure (row 160)",
    )
    out = out.replace("row 121", "row 141")
    out = out.replace("Row 121", "Row 141")
    out = out.replace("row 140", "row 160")
    out = out.replace("Row 140", "Row 160")
    out = out.replace(
        "before row 162 Handshake 4b meta prelude capstone opens on the full capstone path",
        "before row 142 Handshake 4b meta prelude capstone opens on the full capstone path",
    )
    out = out.replace(
        "Proceed to [row 162]",
        "Proceed to [row 142]",
    )
    out = out.replace(
        "Do not conflate row 161 (row 68 ↔ row 61 reunion on the full capstone path) with row 141",
        "Do not conflate row 161 (row 68 ↔ row 61 reunion on the full capstone path) with row 141",
    )
    out = out.replace(
        "row 141 names **Row 68 → Row 101 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion**",
        "row 141 names **Row 68 → Row 121 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion**",
    )
    out = out.replace(
        "Row 68 → Row 161 Row 68 → Row 61",
        "Row 68 → Row 141 Row 68 → Row 61",
    )
    out = out.replace("#skill-navigation-row-1611", "#skill-navigation-row-142")
    return out


def extract_preface_row141(preface: str) -> str:
    start = preface.index("### Row 141 skill checkpoint")
    end = preface.index("\n\n### Row 142 skill checkpoint")
    return preface[start:end]


ROW161_PREFACE = t141_to_161(
    extract_preface_row141((ROOT / "writings/preface/chapters/preface.md").read_text())
) + "\n\n"

PROLOGUE_COMPASS = (
    "| Row 68 → Row 141 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion (row 161) | "
    "[Preface: row 161 skill checkpoint](../preface.md#skill-navigation-row-161) · "
    "[Row 68 → Row 141 Handshake 4a meta prelude capstone reunion index](../appendix/sources.md#row68-row141-handshake4a-meta-prelude-capstone-reunion-index-row-161) · "
    "[memory sheet row 161 baby picture](../appendix/memory-sheet.md#row-161-baby-picture-row68-row141-handshake4a-meta-prelude-capstone-reunion) · "
    "[prologue row 161 preview row](#prologue-preview-row-161); [prologue row 161 closing stitch](#row-161-closing-stitch); "
    "[epilogue row 161 closing loop](../epilogue/multiscale.md#row-161-closing-loop) — "
    "read row 68 gate + row 160 or row 141 Handshake 4a meta prelude capstone / Handshake 4a meta capstone gate + epilogue rate cross-links + row 61 meta aloud "
    "when bulk hardening parses at lab grip rate after verified Handshake 4a meta prelude capstone on the full capstone path but Handshake 4a still feels disconnected from Part VII |\n"
)

PROLOGUE_STITCH = t141_to_161(
    "**Row 141 closing stitch (Row 68 → Row 121 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion).** {#row-141-closing-stitch} "
    "When row 140 closed — Handshake 3 meta prelude capstone verified, row 139 or row 120 recited on the capstone path, and the [epilogue α(\\(T_w\\)) cross-links audit](../epilogue/multiscale.md#opening-hinge-ix3-handshake3) recited with load-cell thermal pre-stress within handbook tolerance after verified Handshake 3 meta prelude capstone on the capstone path — "
    "but **row 61 Handshake 4a meta reunion still opens like standalone epilogue coursework after verified bulk hardening parsing on the capstone path** — "
    "read [preface row 141](../preface.md#skill-navigation-row-141), then the "
    "[Row 68 → Row 121 reunion index](../appendix/sources.md#row68-row121-handshake4a-meta-prelude-capstone-reunion-index-row-141), then "
    "[epilogue row 141 closing loop](../epilogue/multiscale.md#row-141-closing-loop) before row 142 Handshake 4b meta prelude capstone opens on the capstone path.\n\n"
)

PROLOGUE_PREVIEW = (
    "| <span id=\"prologue-preview-row-161\"></span>Row 161 preview (Row 68 → Row 141 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion) | "
    "Explain why midpoint closure (row 68) and Handshake 4a meta (row 61) must be read together with the epilogue rate cross-links and descent chain "
    "after verified Handshake 4a meta prelude capstone on the full capstone path before Act III pulling and Act IV hardening feel like separate courses | "
    "One sentence: \"read row 68 gate + row 160 or row 141 Handshake 4a meta prelude capstone / Handshake 4a meta capstone gate + epilogue rate cross-links + row 61 meta aloud "
    "when bulk hardening parses at lab grip rate after verified Handshake 4a meta prelude capstone on the full capstone path but OpenDiS exports feed the plasticity deck without power-law extrapolation\" — "
    "[preface row 161 skill checkpoint](../preface.md#skill-navigation-row-161); [prologue row 161 closing stitch](#row-161-closing-stitch); "
    "[Row 68 → Row 141 reunion index](../appendix/sources.md#row68-row141-handshake4a-meta-prelude-capstone-reunion-index-row-161); "
    "[memory sheet row 161 baby picture](../appendix/memory-sheet.md#row-161-baby-picture-row68-row141-handshake4a-meta-prelude-capstone-reunion); "
    "[epilogue rate cross-links audit](../epilogue/multiscale.md#opening-hinge-vii3-handshake4a); "
    "[preface row 61 skill checkpoint](../preface.md#skill-navigation-row-61); "
    "[preface row 160 skill checkpoint](../preface.md#skill-navigation-row-160); "
    "[epilogue row 161 closing loop](../epilogue/multiscale.md#row-161-closing-loop) |\n"
)

_epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
EPILOGUE_LOOP = t141_to_161(
    "### Row 141 closing loop"
    + _epilogue.split("### Row 141 closing loop")[1].split("### Row 142 closing loop")[0]
)

SOURCES_TABLE = (
    "| 161 | Row 68 → Row 141 Row 68 → Row 61 Handshake 4a meta prelude capstone (midpoint prelude gate ↔ Handshake 4a meta prelude capstone on full capstone path ↔ row 61 meta) | "
    "[Row 68 → Row 141 Handshake 4a meta prelude capstone reunion index](#row68-row141-handshake4a-meta-prelude-capstone-reunion-index-row-161) · "
    "[preface row 161](../preface.md#skill-navigation-row-161) · "
    "[prologue row 161 preview](../prologue/00-many-scales.md#prologue-preview-row-161) · "
    "[prologue row 161 closing stitch](../prologue/00-many-scales.md#row-161-closing-stitch) · "
    "[epilogue row 161 closing loop](../epilogue/multiscale.md#row-161-closing-loop) · "
    "[memory sheet row 161 baby picture](memory-sheet.md#row-161-baby-picture-row68-row141-handshake4a-meta-prelude-capstone-reunion) | "
    "Row 68 closed but **row 61 Handshake 4a meta reunion still feels disconnected from verified Handshake 4a meta prelude capstone on the full capstone path** — "
    "read row 68 + row 160 or row 141 gate + epilogue rate cross-links + row 61; "
    "[preface row 61](../preface.md#skill-navigation-row-61) |\n"
)

SOURCES_INDEX = t141_to_161(
    (ROOT / "writings/appendix/chapters/sources.md")
    .read_text()
    .split("## Row 68 → Row 121 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 141)")[1]
    .split("## Row 68 → Row 122 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion index (row 142)")[0]
)
SOURCES_INDEX = (
    "## Row 68 → Row 141 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 161)"
    + SOURCES_INDEX
)

MEMORY_TABLE = (
    "| 161 | Meta | [Row 68 → Row 141 Handshake 4a meta prelude capstone reunion index](sources.md#row68-row141-handshake4a-meta-prelude-capstone-reunion-index-row-161) · "
    "[preface row 161 skill checkpoint](../preface.md#skill-navigation-row-161) · "
    "[prologue row 161 preview](../prologue/00-many-scales.md#prologue-preview-row-161) · "
    "[prologue row 161 closing stitch](../prologue/00-many-scales.md#row-161-closing-stitch) · "
    "[epilogue row 161 closing loop](../epilogue/multiscale.md#row-161-closing-loop) | "
    "Row 68 closed but row 61 Handshake 4a meta reunion feels disconnected from verified Handshake 4a meta prelude capstone on the full capstone path — "
    "read row 68 + row 160 or row 141 gate + epilogue rate cross-links + row 61; "
    "[row 161 baby picture](#row-161-baby-picture-row68-row141-handshake4a-meta-prelude-capstone-reunion) |\n"
)

MEMORY_BABY = t141_to_161(
    (ROOT / "writings/appendix/chapters/memory-sheet.md")
    .read_text()
    .split("### Row 141 baby picture")[1]
    .split("### Row 142 baby picture")[0]
)
MEMORY_BABY = "### Row 161 baby picture" + MEMORY_BABY.split(")", 1)[1] if ")" in MEMORY_BABY else "### Row 161 baby picture" + MEMORY_BABY

ROW160_TAIL_OLD = (
    "Read the [memory sheet row 160 baby picture](appendix/memory-sheet.md#row-160-baby-picture-row68-row140-handshake3-meta-prelude-capstone-reunion) when opening [row 141](preface.md#skill-navigation-row-141) before row 60 closes; read the [epilogue row 160 closing loop](epilogue/multiscale.md#row-160-closing-loop) when the competence loop closes. When row 160 is complete, proceed to [row 141](preface.md#skill-navigation-row-141) when row 68 closed but Handshake 4a meta still feels disconnected after Handshake 3 meta prelude capstone on the full capstone path, to [row 121](preface.md#skill-navigation-row-121) for the Row 68 ↔ Row 61 Handshake 4a meta audit on the opening-hinge capstone path alone, to [row 101](preface.md#skill-navigation-row-101) for the Row 68 ↔ Row 61 meta audit on the opening-hinge prelude path alone, to [row 140](preface.md#skill-navigation-row-120) for the Row 68 ↔ Row 60 meta audit on the opening-hinge capstone path alone, to [row 159](preface.md#skill-navigation-row-139) when Handshake 3 meta prelude capstone still lags after verified DFT workflows meta prelude capstone on the full capstone path, to [row 80](preface.md#skill-navigation-row-80) for the Row 68 ↔ Row 60 meta audit alone, to [row 60](preface.md#skill-navigation-row-60) for the Row 59 ↔ Row 40 meta audit alone, to [row 40](preface.md#skill-navigation-row-40) for the full-book \\(\\alpha(T_w)\\) audit, or extend prose only under `writings/` then sync."
)
ROW160_TAIL_NEW = (
    "Read the [memory sheet row 160 baby picture](appendix/memory-sheet.md#row-160-baby-picture-row68-row140-handshake3-meta-prelude-capstone-reunion) when opening [row 161](preface.md#skill-navigation-row-161) before row 61 closes on the full capstone path; read the [epilogue row 160 closing loop](epilogue/multiscale.md#row-160-closing-loop) when the competence loop closes. When row 160 is complete, proceed to [row 161](preface.md#skill-navigation-row-161) when bulk hardening parses at lab grip rate but Handshake 4a still feels disconnected from Part VII after verified Handshake 4a meta prelude capstone on the full capstone path, to [row 141](preface.md#skill-navigation-row-141) for the Row 68 ↔ Row 61 Handshake 4a meta audit on the opening-hinge capstone path alone, to [row 121](preface.md#skill-navigation-row-121) for the Row 68 ↔ Row 61 meta audit on the opening-hinge prelude path alone, to [row 140](preface.md#skill-navigation-row-140) for the Row 68 ↔ Row 60 meta audit on the opening-hinge capstone path alone, to [row 159](preface.md#skill-navigation-row-159) when Handshake 3 meta prelude capstone still lags after verified DFT workflows meta prelude capstone on the full capstone path, to [row 80](preface.md#skill-navigation-row-80) for the Row 68 ↔ Row 60 meta audit alone, to [row 60](preface.md#skill-navigation-row-60) for the Row 59 ↔ Row 40 meta audit alone, to [row 40](preface.md#skill-navigation-row-40) for the full-book \\(\\alpha(T_w)\\) audit, or extend prose only under `writings/` then sync."
)


def main():
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    anchor = "\n## The copper wire through the book"
    if "skill-navigation-row-161" in preface:
        print("preface: row 161 already present")
    else:
        if ROW160_TAIL_OLD not in preface:
            raise SystemExit("preface row 160 tail not found")
        preface = preface.replace(ROW160_TAIL_OLD, ROW160_TAIL_NEW)
        preface = preface.replace(
            anchor,
            ROW161_PREFACE + anchor,
        )
        preface_path.write_text(preface)
        print("preface: added row 161")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-161" not in prologue:
        needle = "| Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion (row 160) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 160 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + PROLOGUE_COMPASS + prologue[line_end + 1 :]
        prologue = prologue.replace(
            "**Row 160 closing stitch",
            PROLOGUE_STITCH + "**Row 160 closing stitch",
        )
        prologue = prologue.replace(
            '| <span id="prologue-preview-row-160"></span>Row 160 preview',
            PROLOGUE_PREVIEW + '| <span id="prologue-preview-row-160"></span>Row 160 preview',
        )
        prologue_path.write_text(prologue)
        print("prologue: added row 161")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "row-161-closing-loop" not in epilogue:
        epilogue = epilogue.replace(
            "Proceed to [row 141](#row-141-closing-loop) when row 68 closed but Handshake 4a meta still feels disconnected after row 160 on the full capstone path, when load cell parses at \\(T_w\\) after verified Handshake 3 meta prelude capstone but Handshake 4a still feels disconnected from Part VII on the full capstone path,",
            "Proceed to [row 161](#row-161-closing-loop) when row 68 closed but Handshake 4a meta still feels disconnected after row 160 on the full capstone path, when bulk hardening parses at lab grip rate after verified Handshake 4a meta prelude capstone but Handshake 4a still feels disconnected from Part VII on the full capstone path,",
        )
        if "Proceed to [row 141](#row-141-closing-loop) when row 68 closed but Handshake 4a meta still feels disconnected after row 159 on the full capstone path" in epilogue:
            epilogue = epilogue.replace(
                "Proceed to [row 141](#row-141-closing-loop) when row 68 closed but Handshake 4a meta still feels disconnected after row 159 on the full capstone path, when load cell parses at \\(T_w\\) after verified Handshake 3 meta prelude capstone but Handshake 3 still feels disconnected from Parts III–VI on the full capstone path,",
                "Proceed to [row 160](#row-160-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 159 on the full capstone path, when load cell parses at \\(T_w\\) after verified Handshake 3 meta prelude capstone but Handshake 3 still feels disconnected from Parts III–VI on the full capstone path,",
            )
        epilogue = epilogue.replace(
            "before row 141 Handshake 4a meta prelude capstone opens in workflow time on the full capstone path.",
            "before row 161 Handshake 4a meta prelude capstone reunion on the full capstone path (then row 142 Handshake 4b on the full capstone path).",
        )
        epilogue = epilogue.replace(
            "Proceed to [row 141](#row-141-closing-loop) when row 68 closed but Handshake 4a meta still feels disconnected after row 140 on the capstone path,",
            "Proceed to [row 141](#row-141-closing-loop) when row 68 closed but Handshake 4a meta still feels disconnected after row 140 on the capstone path,",
        )
        epilogue = epilogue.replace(
            "### Row 135 closing loop (Row 68 → Row 115",
            EPILOGUE_LOOP + "\n\n### Row 135 closing loop (Row 68 → Row 115",
        )
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 161")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row141-handshake4a-meta-prelude-capstone-reunion-index-row-161" not in sources:
        sources = sources.replace(
            "| 160 | Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone",
            SOURCES_TABLE + "| 160 | Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone",
        )
        sources = sources.replace(
            "## Row 68 → Row 122 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion index (row 142)",
            SOURCES_INDEX + "## Row 68 → Row 122 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion index (row 142)",
        )
        sources = sources.replace(
            "before row 141 Handshake 4a meta prelude capstone opens.",
            "before row 141 Handshake 4a meta prelude capstone opens on the capstone path; [row 161](#row68-row141-handshake4a-meta-prelude-capstone-reunion-index-row-161) reunites **Handshake 4a meta prelude capstone with the Handshake 4a meta boundary on the full capstone path** when row 160 closed Handshake 3 meta prelude capstone at verified bulk hardening pedigree but row 61 Handshake 4a meta still reads like separate courses on the full capstone path;",
        )
        sources_path.write_text(sources)
        print("sources: added row 161")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-161-baby-picture-row68-row141" not in memory:
        memory = memory.replace(
            "| 160 | Meta | [Row 68 → Row 140 Handshake 3 meta prelude capstone reunion index]",
            MEMORY_TABLE + "| 160 | Meta | [Row 68 → Row 140 Handshake 3 meta prelude capstone reunion index]",
        )
        memory = memory.replace(
            "### Row 131 baby picture (Row 68 → Row 111 Row 68 → Row 51 homogenization meta prelude capstone reunion)",
            MEMORY_BABY + "### Row 131 baby picture (Row 68 → Row 111 Row 68 → Row 51 homogenization meta prelude capstone reunion)",
        )
        memory_path.write_text(memory)
        print("memory-sheet: added row 161")


if __name__ == "__main__":
    main()
