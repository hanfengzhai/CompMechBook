#!/usr/bin/env python3
"""Add row 159 meta-stitch (Row 68 → Row 139 ↔ Row 59 Handshake 3 meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def t139_to_159(text: str) -> str:
    """Transform row-139 capstone-path meta copy to row 159 (139→159, 119→139 inner, 138→158 gate)."""
    repl = [
        ("Row 68 → Row 119 Row 68 → Row 59", "Row 68 → Row 139 Row 68 → Row 59"),
        (
            "row68-row119-handshake3-meta-prelude-capstone-reunion-index-row-139",
            "row68-row139-handshake3-meta-prelude-capstone-reunion-index-row-159",
        ),
        (
            "row-139-baby-picture-row68-row119-handshake3-meta-prelude-capstone-reunion",
            "row-159-baby-picture-row68-row139-handshake3-meta-prelude-capstone-reunion",
        ),
        ("skill-navigation-row-139", "skill-navigation-row-159"),
        ("prologue-preview-row-139", "prologue-preview-row-159"),
        ("row-139-closing-stitch", "row-159-closing-stitch"),
        ("row-139-closing-loop", "row-159-closing-loop"),
        ("Row 139 three-way audit", "Row 159 three-way audit"),
        (
            "[row 138](preface.md#skill-navigation-row-138) or [row 119](preface.md#skill-navigation-row-119)",
            "[row 158](preface.md#skill-navigation-row-158) or [row 139](preface.md#skill-navigation-row-139)",
        ),
        (
            "[row 138](preface.md#skill-navigation-row-138) or [Row 68 → Row 99",
            "[row 158](preface.md#skill-navigation-row-158) or [Row 68 → Row 119",
        ),
        ("on the capstone path", "on the full capstone path"),
        ("(capstone path)", "(full capstone path)"),
        ("Row 68 ↔ Row 59 reunion (capstone path)", "Row 68 ↔ Row 59 reunion (full capstone path)"),
    ]
    out = text
    for old, new in repl:
        out = out.replace(old, new)
    # Meta row number bumps (after targeted gate replacements)
    out = out.replace("row 139", "row 159")
    out = out.replace("Row 139", "Row 159")
    # Restore inner gate and upstream row numbers
    out = out.replace("[row 159](preface.md#skill-navigation-row-158)", "[row 158](preface.md#skill-navigation-row-158)")
    out = out.replace("[row 159](preface.md#skill-navigation-row-139)", "[row 139](preface.md#skill-navigation-row-139)")
    out = out.replace("skill-navigation-row-159)", "skill-navigation-row-139)", 1)  # no-op safety
    out = out.replace("row 1597", "row 157")
    out = out.replace("row 1598", "row 158")
    out = out.replace("row 159 or row 159", "row 158 or row 139")
    out = out.replace("When row 159 closed — DFT", "When row 158 closed — DFT")
    out = out.replace("row 159 closed DFT", "row 158 closed DFT")
    out = out.replace("after row 159 alone", "after row 158 alone")
    out = out.replace("Recite [preface row 159]", "Recite [preface row 158]")
    out = out.replace("row 159 or row 139 recited", "row 158 or row 139 recited")
    out = out.replace("from row 159's", "from row 158's")
    out = out.replace("verified DFT workflows meta prelude capstone (row 159)", "verified DFT workflows meta prelude capstone (row 158)")
    out = out.replace("verified DFT workflows meta prelude capstone closure (row 159)", "verified DFT workflows meta prelude capstone closure (row 158)")
    out = out.replace("row 119", "row 139")
    out = out.replace("Row 119", "Row 139")
    out = out.replace("row 138", "row 158")
    out = out.replace("Row 138", "Row 158")
    out = out.replace("row 137", "row 157")
    out = out.replace("row 118", "row 138")
    out = out.replace(
        "before row 160 Handshake 3 meta prelude capstone opens on the full capstone path",
        "before row 140 Handshake 3 meta prelude capstone opens on the full capstone path",
    )
    out = out.replace(
        "before row 140 Handshake 3 meta prelude capstone opens in workflow time on the full capstone path",
        "before row 140 Handshake 3 meta prelude capstone opens in workflow time on the full capstone path",
    )
    out = out.replace(
        "Row 68 → Row 59 meta (row 139)",
        "Row 68 → Row 59 meta (row 59)",
    )
    out = out.replace(
        "with row 159 (opening-hinge capstone stitch alone)",
        "with row 139 (opening-hinge capstone stitch alone)",
    )
    out = out.replace(
        "row 139 names **Row 68 → Row 99 Row 68 → Row 59 Handshake 3 meta capstone reunion**",
        "row 139 names **Row 68 → Row 119 Row 68 → Row 59 Handshake 3 meta capstone reunion**",
    )
    out = out.replace(
        "row 159 names **why that reunion must follow verified DFT workflows meta prelude capstone (row 158)",
        "row 159 names **why that reunion must follow verified DFT workflows meta prelude capstone (row 158)",
    )
    out = out.replace(
        "Proceed to [row 160]",
        "Proceed to [row 140]",
    )
    out = out.replace("row 120 Handshake 3 meta prelude capstone opens", "row 140 Handshake 3 meta prelude capstone opens")
    out = out.replace(
        "Do not conflate row 159 (row 68 ↔ row 59 reunion on the full capstone path) with row 139",
        "Do not conflate row 159 (row 68 ↔ row 59 reunion on the full capstone path) with row 139",
    )
    # Fix over-replaced skill anchors in gate links
    out = out.replace("#skill-navigation-row-1588", "#skill-navigation-row-158")
    out = out.replace("preface row 159 skill checkpoint", "preface row 159 skill checkpoint")
    out = out.replace(
        "[Preface row 159](../preface.md#skill-navigation-row-159)",
        "[Preface row 159](../preface.md#skill-navigation-row-159)",
    )
    return out


def extract_preface_row139(preface: str) -> str:
    start = preface.index("### Row 139 skill checkpoint")
    end = preface.index("\n\n\n### Row 140 skill checkpoint")
    return preface[start:end]


ROW159_PREFACE = t139_to_159(
    extract_preface_row139((ROOT / "writings/preface/chapters/preface.md").read_text())
) + "\n\n"

PROLOGUE_COMPASS = (
    "| Row 68 → Row 139 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion (row 159) | "
    "[Preface: row 159 skill checkpoint](../preface.md#skill-navigation-row-159) · "
    "[Row 68 → Row 139 Handshake 3 meta prelude capstone reunion index](../appendix/sources.md#row68-row139-handshake3-meta-prelude-capstone-reunion-index-row-159) · "
    "[memory sheet row 159 baby picture](../appendix/memory-sheet.md#row-159-baby-picture-row68-row139-handshake3-meta-prelude-capstone-reunion) · "
    "[prologue row 159 preview row](#prologue-preview-row-159); [prologue row 159 closing stitch](#row-159-closing-stitch); "
    "[epilogue row 159 closing loop](../epilogue/multiscale.md#row-159-closing-loop) — "
    "read row 68 gate + row 158 or row 139 DFT workflows meta prelude capstone / Handshake 3 meta capstone gate + IX.3 Bridge → opening hinge to Handshake 3 + row 59 meta aloud "
    "when foundation archive is clean on the full capstone path but handbook \\(\\alpha(300\\,\\text{K})\\) persists at the load cell after verified DFT workflows meta prelude capstone |\n"
)

PROLOGUE_STITCH = t139_to_159(
    "**Row 139 closing stitch (Row 68 → Row 119 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion).** {#row-139-closing-stitch} "
    "When row 138 closed — DFT workflows meta prelude capstone verified, row 137 or row 118 recited on the capstone path, and IX.2 Bridge → IX.3 calculation ladder recited with "
    "[foundation archive Lab act](../part09-dft/03-dft-workflows.md#lab-act-archive-the-foundation-run-before-the-wire-scale-solve-act-vi--foundation) archived `foundation_export.yaml` "
    "— but **row 59 IX.3 → Handshake 3 opening hinge still opens like standalone epilogue homework after the workflow archive Scene on the capstone path** — "
    "read [preface row 139](../preface.md#skill-navigation-row-139), then the "
    "[Row 68 → Row 119 reunion index](../appendix/sources.md#row68-row119-handshake3-meta-prelude-capstone-reunion-index-row-139), then "
    "[epilogue row 139 closing loop](../epilogue/multiscale.md#row-139-closing-loop) before row 140 Handshake 3 meta prelude capstone opens on the capstone path.\n\n"
)

PROLOGUE_PREVIEW = (
    "| <span id=\"prologue-preview-row-159\"></span>Row 159 preview (Row 68 → Row 139 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion) | "
    "Explain why midpoint closure (row 68) and IX.3 → Handshake 3 meta (row 59) must be read together with the Bridge → quasiharmonic \\(\\alpha(T_w)\\) chain "
    "after verified DFT workflows meta prelude capstone on the full capstone path before foundation archive and load-cell thermal stress feel like separate courses | "
    "One sentence: \"read row 68 gate + row 158 or row 139 DFT workflows meta prelude capstone / Handshake 3 meta capstone gate + IX.3 Bridge → opening hinge to Handshake 3 + row 59 meta aloud "
    "when foundation archive is clean on the full capstone path but handbook \\(\\alpha(300\\,\\text{K})\\) persists at the load cell after verified DFT workflows meta prelude capstone\" — "
    "[preface row 159 skill checkpoint](../preface.md#skill-navigation-row-159); [prologue row 159 closing stitch](#row-159-closing-stitch); "
    "[Row 68 → Row 139 reunion index](../appendix/sources.md#row68-row139-handshake3-meta-prelude-capstone-reunion-index-row-159); "
    "[memory sheet row 159 baby picture](../appendix/memory-sheet.md#row-159-baby-picture-row68-row139-handshake3-meta-prelude-capstone-reunion); "
    "[IX.3 Bridge to the epilogue](../part09-dft/03-dft-workflows.md#bridge-to-the-epilogue); "
    "[opening hinge to Handshake 3](../part09-dft/03-dft-workflows.md#opening-hinge-ix3-to-handshake3); "
    "[preface row 59 skill checkpoint](../preface.md#skill-navigation-row-59); "
    "[preface row 158 skill checkpoint](../preface.md#skill-navigation-row-158); "
    "[epilogue row 159 closing loop](../epilogue/multiscale.md#row-159-closing-loop) |\n"
)

_epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
EPILOGUE_LOOP = t139_to_159(
    "### Row 139 closing loop"
    + _epilogue.split("### Row 139 closing loop")[1].split("### Row 140 closing loop")[0]
)
EPILOGUE_LOOP = EPILOGUE_LOOP.replace(
    "Row 139 closes the **Handshake 3 meta prelude capstone",
    "Row 159 closes the **Handshake 3 meta prelude capstone",
    1,
)

SOURCES_TABLE = (
    "| 159 | Row 68 → Row 139 Row 68 → Row 59 Handshake 3 meta prelude capstone (midpoint prelude gate ↔ DFT workflows meta prelude capstone on full capstone path ↔ row 59 meta) | "
    "[Row 68 → Row 139 Handshake 3 meta prelude capstone reunion index](#row68-row139-handshake3-meta-prelude-capstone-reunion-index-row-159) · "
    "[preface row 159](../preface.md#skill-navigation-row-159) · "
    "[prologue row 159 preview](../prologue/00-many-scales.md#prologue-preview-row-159) · "
    "[prologue row 159 closing stitch](../prologue/00-many-scales.md#row-159-closing-stitch) · "
    "[epilogue row 159 closing loop](../epilogue/multiscale.md#row-159-closing-loop) · "
    "[memory sheet row 159 baby picture](memory-sheet.md#row-159-baby-picture-row68-row139-handshake3-meta-prelude-capstone-reunion) | "
    "Row 68 closed but **row 59 IX.3 → Handshake 3 opening hinge still feels disconnected from verified DFT workflows meta prelude capstone on the full capstone path** — "
    "read row 68 + row 158 or row 139 gate + IX.3 Bridge → opening hinge to Handshake 3 + row 59; "
    "[preface row 59](../preface.md#skill-navigation-row-59) |\n"
)

SOURCES_INDEX = t139_to_159(
    (ROOT / "writings/appendix/chapters/sources.md")
    .read_text()
    .split("## Row 68 → Row 119 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 139)")[1]
    .split("## Row 68 → Row 120 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 140)")[0]
)
SOURCES_INDEX = (
    "## Row 68 → Row 139 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 159)"
    + SOURCES_INDEX
)
SOURCES_INDEX = SOURCES_INDEX.replace(
    "| [Row 158 reunion (DFT workflows meta prelude capstone)](#row68-row138-dft-workflows-meta-prelude-capstone-reunion-index-row-158) | DFT workflows meta prelude capstone | \"Row 158 or row 139 gate before IX.3 Bridge\" | Foundation yaml clean but Handshake 3 opens early |",
    "| [Row 158 reunion (DFT workflows meta prelude capstone)](#row68-row138-dft-workflows-meta-prelude-capstone-reunion-index-row-158) | DFT workflows meta prelude capstone | \"Row 158 or row 139 gate before IX.3 Bridge\" | Foundation yaml clean but Handshake 3 opens early |",
)
SOURCES_INDEX = SOURCES_INDEX.replace(
    "| [Row 139 reunion (Handshake 3 meta capstone)](#row68-row119-handshake3-meta-capstone-reunion-index-row-139) | Handshake 3 opening | \"Row 68 gate + DFT workflows meta prelude capstone before row 59 on capstone path\" | Row 158 only; IX.3 Bridge chain skipped |",
    "| [Row 139 reunion (Handshake 3 meta capstone)](#row68-row119-handshake3-meta-prelude-capstone-reunion-index-row-139) | Handshake 3 opening | \"Row 68 gate + DFT workflows meta prelude capstone before row 59 on full capstone path\" | Row 158 only; IX.3 Bridge chain skipped |",
)
SOURCES_INDEX = SOURCES_INDEX.replace(
    "| [Row 59 reunion (meta)](#ix3-handshake3-opening-hinge-reunion-index-row-59) | Handshake 3 prelude meta | \"Row 159 gate + Bridge before quasiharmonic \\(\\alpha\\)\" | Row 139 only; row 59 meta skipped |",
    "| [Row 59 reunion (meta)](#ix3-handshake3-opening-hinge-reunion-index-row-59) | Handshake 3 prelude meta | \"Row 159 gate + Bridge before quasiharmonic \\(\\alpha\\)\" | Row 139 only; row 59 meta skipped |",
)

MEMORY_TABLE = (
    "| 159 | Meta | [Row 68 → Row 139 Handshake 3 meta prelude capstone reunion index](sources.md#row68-row139-handshake3-meta-prelude-capstone-reunion-index-row-159) · "
    "[preface row 159 skill checkpoint](../preface.md#skill-navigation-row-159) · "
    "[prologue row 159 preview](../prologue/00-many-scales.md#prologue-preview-row-159) · "
    "[prologue row 159 closing stitch](../prologue/00-many-scales.md#row-159-closing-stitch) · "
    "[epilogue row 159 closing loop](../epilogue/multiscale.md#row-159-closing-loop) | "
    "Row 68 closed but row 59 IX.3 → Handshake 3 opening hinge feels disconnected from verified DFT workflows meta prelude capstone on the full capstone path — "
    "read row 68 + row 158 or row 139 gate + IX.3 Bridge → opening hinge to Handshake 3 + row 59; "
    "[row 159 baby picture](#row-159-baby-picture-row68-row139-handshake3-meta-prelude-capstone-reunion) |\n"
)

MEMORY_BABY = t139_to_159(
    (ROOT / "writings/appendix/chapters/memory-sheet.md")
    .read_text()
    .split("### Row 139 baby picture")[1]
    .split("### Row 140 baby picture")[0]
)
MEMORY_BABY = "### Row 159 baby picture" + MEMORY_BABY.split(")", 1)[1] if ")" in MEMORY_BABY else "### Row 159 baby picture" + MEMORY_BABY

ROW158_TAIL_OLD = (
    "Read the [memory sheet row 158 baby picture](appendix/memory-sheet.md#row-158-baby-picture-row68-row138-dft-workflows-meta-prelude-capstone-reunion) when opening [row 139](preface.md#skill-navigation-row-139) before row 59 closes; read the [epilogue row 158 closing loop](epilogue/multiscale.md#row-158-closing-loop) when the competence loop closes. When row 158 is complete, proceed to [row 139](preface.md#skill-navigation-row-139) when `foundation_export.yaml` exists but Handshake 3 meta prelude capstone still lags after verified DFT workflows meta prelude capstone on the full capstone path, to [row 119](preface.md#skill-navigation-row-119) for the Row 68 ↔ Row 59 Handshake 3 meta audit on the opening-hinge prelude path alone, to [row 138](preface.md#skill-navigation-row-138) for the Row 68 ↔ Row 58 DFT workflows meta audit on the opening-hinge capstone path alone,"
)
ROW158_TAIL_NEW = (
    "Read the [memory sheet row 158 baby picture](appendix/memory-sheet.md#row-158-baby-picture-row68-row138-dft-workflows-meta-prelude-capstone-reunion) when opening [row 159](preface.md#skill-navigation-row-159) before row 59 closes on the full capstone path; read the [epilogue row 158 closing loop](epilogue/multiscale.md#row-158-closing-loop) when the competence loop closes. When row 158 is complete, proceed to [row 159](preface.md#skill-navigation-row-159) when `foundation_export.yaml` exists but Handshake 3 meta prelude capstone still lags after verified DFT workflows meta prelude capstone on the full capstone path, to [row 139](preface.md#skill-navigation-row-139) for the Row 68 ↔ Row 59 Handshake 3 meta audit on the opening-hinge capstone path alone, to [row 119](preface.md#skill-navigation-row-119) for the Row 68 ↔ Row 59 Handshake 3 meta audit on the opening-hinge prelude path alone, to [row 138](preface.md#skill-navigation-row-138) for the Row 68 ↔ Row 58 DFT workflows meta audit on the opening-hinge capstone path alone,"
)


def main():
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    anchor = "\n## The copper wire through the book"
    if "skill-navigation-row-159" in preface:
        print("preface: row 159 already present")
    else:
        if ROW158_TAIL_OLD not in preface:
            raise SystemExit("preface row 158 tail not found")
        preface = preface.replace(ROW158_TAIL_OLD, ROW158_TAIL_NEW)
        preface = preface.replace(
            anchor,
            ROW159_PREFACE + anchor,
        )
        preface_path.write_text(preface)
        print("preface: added row 159")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-159" not in prologue:
        needle = "| Row 68 → Row 138 Row 68 → Row 58 DFT workflows meta prelude capstone reunion (row 158) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 158 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + PROLOGUE_COMPASS + prologue[line_end + 1 :]
        prologue = prologue.replace(
            "**Row 158 closing stitch",
            PROLOGUE_STITCH + "**Row 158 closing stitch",
        )
        prologue = prologue.replace(
            '| <span id="prologue-preview-row-158"></span>Row 158 preview',
            PROLOGUE_PREVIEW + '| <span id="prologue-preview-row-158"></span>Row 158 preview',
        )
        prologue_path.write_text(prologue)
        print("prologue: added row 159")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "row-159-closing-loop" not in epilogue:
        epilogue = epilogue.replace(
            "Proceed to [row 139](#row-139-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 158 on the full capstone path, to [row 138](#row-138-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 138 on the opening-hinge capstone path alone,",
            "Proceed to [row 159](#row-159-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 158 on the full capstone path, to [row 139](#row-139-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 138 on the opening-hinge capstone path alone,",
        )
        epilogue = epilogue.replace(
            "before row 139 Handshake 3 meta prelude capstone opens in workflow time on the full capstone path.",
            "before row 159 Handshake 3 meta prelude capstone reunion on the full capstone path (then row 140 on the capstone path).",
        )
        epilogue = epilogue.replace(
            "### Row 135 closing loop (Row 68 → Row 115",
            EPILOGUE_LOOP + "\n\n### Row 135 closing loop (Row 68 → Row 115",
        )
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 159")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row139-handshake3-meta-prelude-capstone-reunion-index-row-159" not in sources:
        sources = sources.replace(
            "| 158 | Row 68 → Row 138 Row 68 → Row 58 DFT workflows meta prelude capstone",
            SOURCES_TABLE + "| 158 | Row 68 → Row 138 Row 68 → Row 58 DFT workflows meta prelude capstone",
        )
        sources = sources.replace(
            "## Row 68 → Row 120 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 140)",
            SOURCES_INDEX + "## Row 68 → Row 120 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 140)",
        )
        sources = sources.replace(
            "[row 158](#row68-row138-dft-workflows-meta-prelude-capstone-reunion-index-row-158) reunites **Kohn–Sham meta prelude capstone with the DFT workflows meta boundary on the full capstone path** when row 157 closed Kohn–Sham meta prelude capstone at verified `cutoff_convergence.yaml` but IX.2 → IX.3 opening hinge still reads like separate courses on the full capstone path;",
            "[row 158](#row68-row138-dft-workflows-meta-prelude-capstone-reunion-index-row-158) reunites **Kohn–Sham meta prelude capstone with the DFT workflows meta boundary on the full capstone path** when row 157 closed Kohn–Sham meta prelude capstone at verified `cutoff_convergence.yaml` but IX.2 → IX.3 opening hinge still reads like separate courses on the full capstone path; [row 159](#row68-row139-handshake3-meta-prelude-capstone-reunion-index-row-159) reunites **DFT workflows meta prelude capstone with the Handshake 3 meta boundary on the full capstone path** when row 158 closed DFT workflows meta prelude capstone at verified `foundation_export.yaml` but IX.3 → Handshake 3 opening hinge still reads like separate courses on the full capstone path;",
        )
        sources_path.write_text(sources)
        print("sources: added row 159")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-159-baby-picture-row68-row139" not in memory:
        memory = memory.replace(
            "| 158 | Meta | [Row 68 → Row 138 DFT workflows meta prelude capstone reunion index]",
            MEMORY_TABLE + "| 158 | Meta | [Row 68 → Row 138 DFT workflows meta prelude capstone reunion index]",
        )
        memory = memory.replace(
            "### Row 131 baby picture (Row 68 → Row 111 Row 68 → Row 51 homogenization meta prelude capstone reunion)",
            MEMORY_BABY + "### Row 131 baby picture (Row 68 → Row 111 Row 68 → Row 51 homogenization meta prelude capstone reunion)",
        )
        memory_path.write_text(memory)
        print("memory-sheet: added row 159")


if __name__ == "__main__":
    main()
