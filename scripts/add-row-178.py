#!/usr/bin/env python3
"""Add row 178 meta-stitch (Row 68 → Row 158 ↔ Row 58 DFT workflows meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def t158_to_178(text: str) -> str:
    """Transform row-158 capstone-path meta copy to row 178 (158→178, 138→158 inner, 177 gate)."""
    repl = [
        ("Row 68 → Row 138 Row 68 → Row 58", "Row 68 → Row 158 Row 68 → Row 58"),
        (
            "row68-row138-dft-workflows-meta-prelude-capstone-reunion-index-row-158",
            "TEMP_ROW178_EXP_INDEX",
        ),
        (
            "row-158-baby-picture-row68-row138-dft-workflows-meta-prelude-capstone-reunion",
            "row-178-baby-picture-row68-row158-dft-workflows-meta-prelude-capstone-reunion",
        ),
        ("skill-navigation-row-158", "TEMP_SKILL_NAV_158"),
        ("prologue-preview-row-158", "prologue-preview-row-178"),
        ("row-158-closing-stitch", "row-178-closing-stitch"),
        ("row-158-closing-loop", "row-178-closing-loop"),
        ("Row 158 three-way audit", "Row 178 three-way audit"),
        (
            "[row 157](preface.md#skill-navigation-row-157) or [row 138](TEMP_SKILL_NAV_158)",
            "[row 177](preface.md#skill-navigation-row-177) or [row 158](TEMP_SKILL_NAV_158)",
        ),
        (
            "[row 157](preface.md#skill-navigation-row-157) or [Row 68 → Row 118 DFT workflows meta prelude capstone reunion index (row 138)](appendix/sources.md#row68-row118-dft-workflows-meta-prelude-capstone-reunion-index-row-138)",
            "[row 177](preface.md#skill-navigation-row-177) or [Row 68 → Row 158 DFT workflows meta prelude capstone reunion index (row 178)](appendix/sources.md#row68-row158-dft-workflows-meta-prelude-capstone-reunion-index-row-178)",
        ),
        (
            "[row 157](preface.md#skill-navigation-row-157) or [Row 68 → Row 138 DFT workflows meta prelude capstone reunion index (row 158)](appendix/sources.md#row68-row138-dft-workflows-meta-prelude-capstone-reunion-index-row-158)",
            "[row 177](preface.md#skill-navigation-row-177) or [Row 68 → Row 158 DFT workflows meta prelude capstone reunion index (row 178)](appendix/sources.md#row68-row158-dft-workflows-meta-prelude-capstone-reunion-index-row-178)",
        ),
        (
            "verified Kohn–Sham meta prelude capstone closure (row 157)",
            "verified Kohn–Sham meta prelude capstone closure (row 177)",
        ),
        (
            "before row 159 Handshake 3 meta prelude capstone reunion opens on the full capstone path",
            "before row 179 Handshake 3 meta prelude capstone reunion opens on the full capstone path",
        ),
        (
            "before row 159 Handshake 3 meta prelude capstone reunion on the full capstone path",
            "before row 179 Handshake 3 meta prelude capstone reunion on the full capstone path",
        ),
        (
            "before row 139 Handshake 3 meta prelude capstone opens on the full capstone path",
            "before row 179 Handshake 3 meta prelude capstone opens on the full capstone path",
        ),
    ]
    out = text
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW178_EXP_INDEX",
        "row68-row158-dft-workflows-meta-prelude-capstone-reunion-index-row-178",
    )
    out = out.replace("TEMP_SKILL_NAV_158", "skill-navigation-row-158")
    out = out.replace("row 158", "row 178")
    out = out.replace("Row 158", "Row 178")
    out = out.replace("skill-navigation-row-158", "skill-navigation-row-178")
    out = out.replace("[row 178](preface.md#skill-navigation-row-177)", "[row 177](preface.md#skill-navigation-row-177)")
    out = out.replace("[row 178](preface.md#skill-navigation-row-178)", "[row 178](preface.md#skill-navigation-row-178)")
    out = out.replace("[row 178](preface.md#skill-navigation-row-158)", "[row 158](preface.md#skill-navigation-row-158)")
    out = out.replace("[row 158](preface.md#skill-navigation-row-178)", "[row 158](preface.md#skill-navigation-row-158)")
    out = out.replace("when row 157 closed but row 58", "when row 177 closed but row 58")
    out = out.replace("[preface row 158](../preface.md#skill-navigation-row-178)", "[preface row 158](../preface.md#skill-navigation-row-158)")
    out = out.replace("row 1587", "row 179")
    out = out.replace("row 1588", "row 180")
    out = out.replace("row 178 or row 178", "row 177 or row 158")
    out = out.replace("When row 178 closed", "When row 177 closed")
    out = out.replace("after row 178 alone", "after row 177 alone")
    out = out.replace("Recite [preface row 178]", "Recite [preface row 177]")
    out = out.replace("row 178 or row 158 recited", "row 177 or row 158 recited")
    out = out.replace("When row 178 closed — Kohn", "When row 177 closed — Kohn")
    out = out.replace("When row 157 closed — Kohn", "When row 177 closed — Kohn")
    out = out.replace("row 157 or row 138 recited", "row 177 or row 158 recited")
    out = out.replace("row 156 or row 117 recited", "row 176 or row 157 recited")
    out = out.replace("row 157 or row 58 recited", "row 177 or row 58 recited")
    out = out.replace("when row 157 closed Kohn", "when row 177 closed Kohn")
    out = out.replace("(preface.md#skill-navigation-row-138)", "(preface.md#skill-navigation-row-158)")
    out = out.replace(
        "Row 68 → Row 178 DFT workflows meta prelude capstone reunion index",
        "Row 68 → Row 158 DFT workflows meta prelude capstone reunion index",
    )
    out = out.replace("row 156 or row 117 recited", "row 176 or row 157 recited")
    out = out.replace("row 138", "row 158")
    out = out.replace("Row 138", "Row 158")
    out = out.replace("row 118", "row 138")
    out = out.replace("Row 118", "Row 138")
    out = out.replace(
        "row68-row118-dft-workflows-meta-prelude-capstone-reunion-index-row-138",
        "row68-row138-dft-workflows-meta-prelude-capstone-reunion-index-row-158",
    )
    out = out.replace(
        "row68-row117-kohn-sham-meta-prelude-capstone-reunion-index-row-137",
        "row68-row157-kohn-sham-meta-prelude-capstone-reunion-index-row-177",
    )
    out = out.replace("Row 68 → Row 178 Row 68 → Row 58", "Row 68 → Row 158 Row 68 → Row 58")
    out = out.replace(
        "[preface row 158](../preface.md#skill-navigation-row-138)",
        "[preface row 158](../preface.md#skill-navigation-row-158)",
    )
    out = out.replace(
        "Confirm [row 157](preface.md#skill-navigation-row-157) or [Row 68 → Row 158",
        "Confirm [row 177](preface.md#skill-navigation-row-177) or [Row 68 → Row 158",
    )
    out = out.replace(
        "and [row 157](preface.md#skill-navigation-row-157) or [row 158]",
        "and [row 177](preface.md#skill-navigation-row-177) or [row 158]",
    )
    out = out.replace("[row 138](preface.md#skill-navigation-row-118)", "[row 138](preface.md#skill-navigation-row-138)")
    out = out.replace(
        "(preface.md#skill-navigation-row-178) when `cutoff",
        "(preface.md#skill-navigation-row-158) when `cutoff",
    )
    out = out.replace("when row 157 and row 58", "when row 177 and row 58")
    out = out.replace("after row 157 alone", "after row 177 alone")
    out = out.replace("Scene after row 157.", "Scene after row 177.")
    out = out.replace("from row 178's", "from row 177's")
    out = out.replace("row 157's SCF fixed-point", "row 177's SCF fixed-point")
    out = out.replace("row 157 tells you", "row 177 tells you")
    out = out.replace(
        "[IX.2 Bridge](part09-dft/02-kohn-sham.md#bridge)",
        "[IX.2 Bridge → opening hinge → IX.3 calculation ladder](part09-dft/02-kohn-sham.md#bridge)",
    )
    out = out.replace("row 157", "row 177")
    out = out.replace("Row 157", "Row 177")
    out = out.replace("[row 177](preface.md#skill-navigation-row-177)", "[row 177](preface.md#skill-navigation-row-177)")
    out = out.replace("[row 177](preface.md#skill-navigation-row-158)", "[row 158](preface.md#skill-navigation-row-158)")
    return out


def extract_preface_row158(preface: str) -> str:
    start = preface.index("### Row 158 skill checkpoint")
    end = preface.index("\n\n### Row 159 skill checkpoint")
    return preface[start:end]


ROW178_PREFACE = t158_to_178(extract_preface_row158((ROOT / "writings/preface/chapters/preface.md").read_text())) + "\n\n"

_prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
_row158_compass = next(
    line for line in _prologue.splitlines() if "(row 158) |" in line and "Row 68 → Row 138" in line
)
PROLOGUE_COMPASS = t158_to_178(_row158_compass) + "\n"

_row158_stitch_body = (
    _prologue.split("**Row 158 closing stitch")[1].split("**Row 177 closing stitch")[0].lstrip().split("\n\n")[0]
)
PROLOGUE_STITCH = t158_to_178(
    "**Row 158 closing stitch (Row 68 → Row 138 Row 68 → Row 58 DFT workflows meta prelude capstone reunion).** {#row-158-closing-stitch} "
    + _row158_stitch_body.split(".** {#row-158-closing-stitch} ", 1)[-1]
) + "\n\n"

_row158_preview = next(line for line in _prologue.splitlines() if 'id="prologue-preview-row-158"' in line)
PROLOGUE_PREVIEW = t158_to_178(_row158_preview) + "\n"

_epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
EPILOGUE_LOOP = t158_to_178(
    "### Row 158 closing loop"
    + _epilogue.split("### Row 158 closing loop")[1].split("### Row 159 closing loop")[0]
)

_src158_header = "## Row 68 → Row 138 Row 68 → Row 58 DFT workflows meta prelude capstone reunion index (row 158)"
_next158_header = "## Continuous read-through guide"
_sources_blob = (ROOT / "writings/appendix/chapters/sources.md").read_text()
_src158_body = _sources_blob.split(_src158_header, 1)[1].split(_next158_header, 1)[0]
SOURCES_INDEX = (
    "## Row 68 → Row 158 Row 68 → Row 58 DFT workflows meta prelude capstone reunion index (row 178)"
    + t158_to_178(_src158_body)
)

_row158_table = next(
    line for line in _sources_blob.splitlines() if line.startswith("| 158 | Row 68 → Row 138")
)
SOURCES_TABLE = t158_to_178(_row158_table).replace("| 158 | Row 68 → Row 158", "| 178 | Row 68 → Row 158", 1) + "\n"

_row158_mem_table = next(
    line for line in (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text().splitlines()
    if line.startswith("| 158 | Meta |")
)
MEMORY_TABLE = t158_to_178(_row158_mem_table).replace("| 158 | Meta |", "| 178 | Meta |", 1) + "\n"

_baby_anchor = "### Row 158 baby picture (Row 68 → Row 158 Row 68 → Row 58 DFT workflows meta prelude capstone reunion) {#row-158-baby-picture-row68-row138-dft-workflows-meta-prelude-capstone-reunion}"
MEMORY_BABY = t158_to_178(
    (ROOT / "writings/appendix/chapters/memory-sheet.md")
    .read_text()
    .split(_baby_anchor)[1]
    .split("### Row 159 baby picture")[0]
)
MEMORY_BABY = (
    "### Row 178 baby picture (Row 68 → Row 158 Row 68 → Row 58 DFT workflows meta prelude capstone reunion)"
    + MEMORY_BABY.split(")", 1)[1]
    if ")" in MEMORY_BABY
    else "### Row 178 baby picture" + MEMORY_BABY
)

ROW177_BABY_OLD = (
    "row 177 when **IX.1 Bridge and Row 68 → Row 57 meta must read on the same wire before row 158 DFT workflows meta prelude capstone opens on the full capstone path**"
)
ROW177_BABY_NEW = (
    "row 177 when **IX.2 Bridge and Row 68 → Row 58 meta must read on the same wire before row 178 DFT workflows meta prelude capstone opens on the full capstone path**"
)


def main():
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "skill-navigation-row-178" in preface and preface.index("skill-navigation-row-178") < preface.index(copper):
        print("preface: row 178 already present")
    elif "skill-navigation-row-178" in preface:
        raise SystemExit("preface row 178 exists but not at copper wire insert point")
    else:
        if "skill-navigation-row-177" not in preface:
            raise SystemExit("preface row 177 must exist before row 178")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + ROW178_PREFACE + copper)
        preface_path.write_text(preface)
        print("preface: added row 178")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-178" not in prologue:
        needle = "| Row 68 → Row 157 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion (row 177) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 177 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + PROLOGUE_COMPASS + prologue[line_end + 1 :]
        prologue = prologue.replace(
            "**Row 177 closing stitch",
            PROLOGUE_STITCH + "**Row 177 closing stitch",
        )
        prologue = prologue.replace(
            '| <span id="prologue-preview-row-177"></span>Row 177 preview',
            PROLOGUE_PREVIEW + '| <span id="prologue-preview-row-177"></span>Row 177 preview',
        )
        prologue_path.write_text(prologue)
        print("prologue: added row 178")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "row-178-closing-loop" not in epilogue:
        marker = (
            "Proceed to [row 158](#row-158-closing-loop) when row 68 closed but DFT workflows meta prelude capstone still lags after row 177 on the full capstone path, to [row 138](#row-138-closing-loop) when row 68 closed but DFT workflows meta prelude capstone still lags after row 157 on the opening-hinge capstone path alone, to [row 157](#row-137-closing-loop) when row 68 closed but Kohn–Sham meta prelude capstone still lags after row 136 on the opening-hinge capstone path alone, to [row 118](#row-118-closing-loop) for the Row 68 ↔ Row 58 DFT workflows meta audit on the opening-hinge prelude path alone, to [row 137](#row-117-closing-loop) for the Row 68 ↔ Row 57 Kohn–Sham meta audit on the opening-hinge capstone path alone, to [row 97](#row-97-closing-loop) for the Row 68 ↔ Row 57 Kohn–Sham opening prelude audit alone, to [row 77](#row-77-closing-loop) for the Row 68 ↔ Row 57 prelude audit alone, to [row 176](#row-156-closing-loop) when `murnaghan_eos.yaml` is missing after verified Born–Oppenheimer meta prelude capstone on the full capstone path, to [row 57](#row-57-closing-loop) when only IX.1 → IX.2 stalls, or extend prose only under `writings/` then sync.\n\n\n\n\n\n"
        )
        replacement = (
            "Proceed to [row 178](#row-178-closing-loop) when row 68 closed but DFT workflows meta prelude capstone still lags after row 177 on the full capstone path, to [row 158](#row-158-closing-loop) when DFT workflows meta prelude capstone still lags after verified Kohn–Sham meta prelude capstone on the opening-hinge capstone path alone, to [row 138](#row-138-closing-loop) when row 68 closed but DFT workflows meta prelude capstone still lags after row 157 on the opening-hinge capstone path alone, to [row 118](#row-118-closing-loop) for the Row 68 ↔ Row 58 DFT workflows meta audit on the opening-hinge prelude path alone, to [row 137](#row-117-closing-loop) for the Row 68 ↔ Row 57 Kohn–Sham meta audit on the opening-hinge capstone path alone, to [row 97](#row-97-closing-loop) for the Row 68 ↔ Row 57 Kohn–Sham opening prelude audit alone, to [row 177](#row-177-closing-loop) when `cutoff_convergence.yaml` is missing after verified Kohn–Sham meta prelude capstone on the full capstone path, to [row 157](#row-157-closing-loop) when `cutoff_convergence.yaml` is missing on the opening-hinge capstone path alone, to [row 58](#row-58-closing-loop) when only IX.2 → IX.3 stalls, or extend prose only under `writings/` then sync.\n\n\n"
            + EPILOGUE_LOOP
            + "\n\n\n\n\n"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 177 end marker not found")
        epilogue = epilogue.replace(marker, replacement, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 178")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row158-dft-workflows-meta-prelude-capstone-reunion-index-row-178" not in sources:
        sources = sources.replace(
            "| 158 | Row 68 → Row 138 Row 68 → Row 58 DFT workflows meta prelude capstone",
            SOURCES_TABLE + "| 158 | Row 68 → Row 138 Row 68 → Row 58 DFT workflows meta prelude capstone",
        )
        sources = sources.replace(
            _src158_header,
            SOURCES_INDEX + _src158_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 178")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-178-baby-picture-row68-row158" not in memory:
        memory = memory.replace(
            "| 177 | Meta | [Row 68 → Row 157 Kohn–Sham meta prelude capstone reunion index]",
            MEMORY_TABLE + "| 177 | Meta | [Row 68 → Row 157 Kohn–Sham meta prelude capstone reunion index]",
        )
        memory = memory.replace(
            _baby_anchor,
            MEMORY_BABY + _baby_anchor,
            1,
        )
        if ROW177_BABY_OLD in memory:
            memory = memory.replace(ROW177_BABY_OLD, ROW177_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 178")


if __name__ == "__main__":
    main()
