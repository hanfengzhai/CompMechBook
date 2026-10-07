#!/usr/bin/env python3
"""Add row 218 meta-stitch (Row 68 → Row 198 ↔ Row 58 DFT workflows meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]


def bump198_to_218(text: str) -> str:
    """Transform row-198 capstone-path meta copy to row 218 (178→198 inner, 217 KS gate)."""
    out = text.replace("row 219", "TEMP_ROW219")
    out = text.replace("row 218", "TEMP_ROW218")
    out = text.replace("row 217", "TEMP_ROW217")
    repl = [
        ("Row 68 → Row 178 Row 68 → Row 58", "Row 68 → Row 198 Row 68 → Row 58"),
        (
            "row68-row178-dft-workflows-meta-prelude-capstone-reunion-index-row-198",
            "TEMP_ROW218_DFT_INDEX",
        ),
        (
            "row-198-baby-picture-row68-row178-dft-workflows-meta-prelude-capstone-reunion",
            "row-218-baby-picture-row68-row198-dft-workflows-meta-prelude-capstone-reunion",
        ),
        ("### Row 198 skill checkpoint", "### Row 218 skill checkpoint"),
        ("skill-navigation-row-198", "skill-navigation-row-218"),
        ("prologue-preview-row-198", "prologue-preview-row-218"),
        ("row-198-closing-stitch", "row-218-closing-stitch"),
        ("row-198-closing-loop", "row-218-closing-loop"),
        ("Row 198 three-way audit", "Row 218 three-way audit"),
        (
            "DFT workflows meta prelude capstone reunion (row 198)",
            "DFT workflows meta prelude capstone reunion (row 218)",
        ),
        (
            "### Row 198 baby picture",
            "### Row 218 baby picture {#row-218-baby-picture-row68-row198-dft-workflows-meta-prelude-capstone-reunion}",
        ),
        ("**Row 198 baby picture:**", "**Row 218 baby picture:**"),
        (
            "[row 217](preface.md#skill-navigation-row-217) or [row 198](preface.md#skill-navigation-row-198)",
            "[row 217](preface.md#skill-navigation-row-217) or [row 198](preface.md#skill-navigation-row-198)",
        ),
        (
            "[row 217](preface.md#skill-navigation-row-217) or [Row 68 → Row 178 DFT workflows meta prelude capstone reunion index (row 198)](appendix/sources.md#row68-row178-dft-workflows-meta-prelude-capstone-reunion-index-row-198)",
            "[row 217](preface.md#skill-navigation-row-217) or [Row 68 → Row 198 DFT workflows meta prelude capstone reunion index (row 218)](appendix/sources.md#row68-row198-dft-workflows-meta-prelude-capstone-reunion-index-row-218)",
        ),
        (
            "verified Kohn–Sham meta prelude capstone closure (row 217)",
            "verified Kohn–Sham meta prelude capstone closure (row 217)",
        ),
        (
            "before row 199 Handshake 3 meta prelude capstone reunion opens on the full capstone path",
            "before row 219 Handshake 3 meta prelude capstone reunion opens on the full capstone path",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW218_DFT_INDEX",
        "row68-row198-dft-workflows-meta-prelude-capstone-reunion-index-row-218",
    )
    out = out.replace("Row 198 does not replace", "Row 218 does not replace")
    out = out.replace("When row 198 is complete", "When row 218 is complete")
    out = out.replace("When row 217 closed", "When row 217 closed")
    out = out.replace("when row 217 closed but row 58", "when row 217 closed but row 58")
    out = out.replace("after row 198 alone", "after row 218 alone")
    out = out.replace("Recite [preface row 217]", "Recite [preface row 217]")
    out = out.replace("row 198 or row 178 recited", "row 218 or row 198 recited")
    out = out.replace("row 217 or row 198 recited", "row 217 or row 198 recited")
    out = out.replace("Row 178", "@@ROW178CAP@@")
    out = out.replace("row 178", "@@row178@@")
    out = out.replace("@@ROW178CAP@@", "Row 198")
    out = out.replace("@@row178@@", "row 198")
    out = out.replace("row 158", "row 178")
    out = out.replace("Row 158", "Row 178")
    out = out.replace("row 138", "row 158")
    out = out.replace("Row 138", "Row 158")
    out = out.replace(
        "row68-row138-dft-workflows-meta-prelude-capstone-reunion-index-row-158",
        "row68-row158-dft-workflows-meta-prelude-capstone-reunion-index-row-178",
    )
    out = out.replace(
        "row68-row177-kohn-sham-meta-prelude-capstone-reunion-index-row-197",
        "row68-row198-dft-workflows-meta-prelude-capstone-reunion-index-row-218",
    )
    out = out.replace("skill-navigation-row-217", "TEMP_SKILL_217")
    out = out.replace("row 217", "row 217")
    out = out.replace("TEMP_SKILL_217", "skill-navigation-row-217")
    out = out.replace("Row 68 → Row 218 Row 68 → Row 58", "Row 68 → Row 198 Row 68 → Row 58")
    out = out.replace("memory sheet row 198 baby picture", "memory sheet row 218 baby picture")
    out = out.replace("prologue row 198 closing stitch", "prologue row 218 closing stitch")
    out = out.replace("prologue row 198 preview", "prologue row 218 preview")
    out = out.replace("epilogue row 198 closing loop", "epilogue row 218 closing loop")
    out = out.replace("opening [row 199]", "opening [row 219]")
    out = out.replace("skill-navigation-row-199", "skill-navigation-row-219")
    out = out.replace(
        "Prologue preview ([row 218](prologue/00-many-scales.md#prologue-preview-row-218))",
        "Prologue preview ([row 218](prologue/00-many-scales.md#prologue-preview-row-218))",
    )
    out = out.replace("preface row 198", "preface row 218")
    out = out.replace(
        "[row 199](preface.md#skill-navigation-row-199)",
        "[row 219](preface.md#skill-navigation-row-219)",
    )
    out = out.replace("TEMP_ROW217", "row 217")
    out = out.replace("TEMP_ROW218", "row 218")
    out = out.replace("TEMP_ROW219", "row 219")
    out = out.replace(
        "proceed to [row 199](preface.md#skill-navigation-row-199)",
        "proceed to [row 219](preface.md#skill-navigation-row-219)",
    )
    return out

    return out


def _load_add198():
    spec = importlib.util.spec_from_file_location("add198", ROOT / "scripts/add-row-198.py")
    add198 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add198)
    return add198


def _build_blocks() -> dict[str, str]:
    add198 = _load_add198()
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 198 skill checkpoint")
    end = preface.index("\n\n### Row 199 skill checkpoint", start)
    row218_preface = bump198_to_218(preface[start:end]) + "\n\n"

    row178_stitch = next(
        line
        for line in (ROOT / "writings/prologue/chapters/00-many-scales.md")
        .read_text()
        .splitlines()
        if line.startswith("**Row 178 closing stitch")
    )
    prologue_stitch = bump198_to_218(
        add198.bump178_to_198(row178_stitch).replace(
            "**Row 198 closing stitch (Row 68 → Row 178",
            "**Row 218 closing stitch (Row 68 → Row 198",
        ).replace("{#row-198-closing-stitch}", "{#row-218-closing-stitch}")
    ) + "\n\n"

    b198 = add198._build_blocks()
    prologue_compass = bump198_to_218(b198["prologue_compass"])
    prologue_preview = bump198_to_218(b198["prologue_preview"])

    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    row198_loop_anchor = (
        "### Row 198 closing loop (Row 68 → Row 178 Row 68 → Row 58 "
        "DFT workflows meta prelude capstone reunion) {#row-198-closing-loop}"
    )
    row199_loop_end = (
        "### Row 199 closing loop (Row 68 → Row 179 Row 68 → Row 59 "
        "Handshake 3 meta prelude capstone reunion) {#row-199-closing-loop}"
    )
    epilogue_loop = bump198_to_218(
        row198_loop_anchor + epilogue.split(row198_loop_anchor, 1)[1].split(row199_loop_end, 1)[0]
    )

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src198_header = (
        "## Row 68 → Row 178 Row 68 → Row 58 DFT workflows meta prelude capstone reunion index (row 198)"
    )
    next178_header = (
        "## Row 68 → Row 158 Row 68 → Row 58 DFT workflows meta prelude capstone reunion index (row 178)"
    )
    sources_index = bump198_to_218(sources.split(src198_header, 1)[1].split(next178_header, 1)[0])
    sources_index = (
        "## Row 68 → Row 198 Row 68 → Row 58 DFT workflows meta prelude capstone reunion index (row 218) "
        "{#row68-row198-dft-workflows-meta-prelude-capstone-reunion-index-row-218}"
        + sources_index
    )

    sources_table = bump198_to_218(b198["sources_table"])
    sources_table = sources_table.replace("| 198 | Row 68 → Row 178", "| 218 | Row 68 → Row 198", 1)

    memory_table = bump198_to_218(b198["memory_table"])
    memory_table = memory_table.replace("| 198 | Meta |", "| 218 | Meta |", 1)

    memory_baby = bump198_to_218(b198["memory_baby"])
    if "{#row-218-baby-picture-row68-row198" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 218 baby picture",
            "### Row 218 baby picture {#row-218-baby-picture-row68-row198-dft-workflows-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row218_preface": row218_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW217_TAIL_OLD = (
    "When row 217 is complete, proceed to [row 198](preface.md#skill-navigation-row-218) when `cutoff_convergence.yaml` exists on the full capstone path, to [row 178](preface.md#skill-navigation-row-178) when `cutoff_convergence.yaml` exists but IX.3 still feels disconnected from verified Kohn–Sham meta prelude capstone on the opening-hinge capstone path alone, to [row 158](preface.md#skill-navigation-row-158) for the Row 68 ↔ Row 58 DFT workflows meta audit on the opening-hinge prelude path alone, to [row 197](preface.md#skill-navigation-row-177) for the Row 68 ↔ Row 57 Kohn–Sham meta audit on the opening-hinge capstone path alone, to [row 216](preface.md#skill-navigation-row-196) when Born–Oppenheimer meta prelude capstone still lags after verified electronic audit meta prelude capstone on the full capstone path, to [row 58](preface.md#skill-navigation-row-58) when only IX.2 → IX.3 stalls, or extend prose only under `writings/` then sync."
)
ROW217_TAIL_NEW = (
    "When row 217 is complete, proceed to [row 218](preface.md#skill-navigation-row-218) when `cutoff_convergence.yaml` exists on the full capstone path, to [row 198](preface.md#skill-navigation-row-198) when `cutoff_convergence.yaml` exists but IX.3 still feels disconnected from verified Kohn–Sham meta prelude capstone on the opening-hinge capstone path alone, to [row 178](preface.md#skill-navigation-row-178) for the Row 68 ↔ Row 58 DFT workflows meta audit on the opening-hinge prelude path alone, to [row 217](preface.md#skill-navigation-row-217) for the Row 68 ↔ Row 57 Kohn–Sham meta audit on the opening-hinge capstone path alone, to [row 216](preface.md#skill-navigation-row-216) when Born–Oppenheimer meta prelude capstone still lags after verified electronic audit meta prelude capstone on the full capstone path, to [row 58](preface.md#skill-navigation-row-58) when only IX.2 → IX.3 stalls, or extend prose only under `writings/` then sync."
)

ROW217_EPILOGUE_OLD = (
    "Proceed to [row 198](#row-198-closing-loop) when row 68 closed but DFT workflows meta prelude capstone still lags after row 197 on the full capstone path,"
)
ROW217_EPILOGUE_NEW = (
    "Proceed to [row 218](#row-218-closing-loop) when row 68 closed but DFT workflows meta prelude capstone still lags after row 217 on the full capstone path,"
)

ROW217_STITCH_OLD = (
    "before row 218 DFT workflows meta prelude capstone reunion opens on the full capstone path."
)
ROW217_STITCH_NEW = (
    "before row 219 Handshake 3 meta prelude capstone reunion opens on the full capstone path."
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 218 skill checkpoint" in preface:
        print("preface: row 218 already present")
    else:
        if "### Row 217 skill checkpoint" not in preface:
            raise SystemExit("row 217 must exist before row 218")
        if ROW217_TAIL_OLD in preface:
            preface = preface.replace(ROW217_TAIL_OLD, ROW217_TAIL_NEW, 1)
        elif ROW217_TAIL_NEW in preface:
            print("preface: row 217 tail already updated")
        else:
            raise SystemExit("row 217 tail proceed string not found")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row218_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 218")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-218" not in prologue:
        needle = "| Row 68 → Row 178 Row 68 → Row 58 DFT workflows meta prelude capstone reunion (row 198) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 198 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 218 closing stitch" not in prologue:
            prologue = prologue.replace(
                "**Row 178 closing stitch",
                b["prologue_stitch"] + "**Row 178 closing stitch",
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-198"></span>Row 198 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview row 198 not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW217_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW217_STITCH_OLD, ROW217_STITCH_NEW, 1)
        prologue_path.write_text(prologue)
        print("prologue: added row 218")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "{#row-218-closing-loop}" not in epilogue:
        if ROW217_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW217_EPILOGUE_OLD, ROW217_EPILOGUE_NEW, 1)
        marker = (
            "### Row 198 closing loop (Row 68 → Row 178 Row 68 → Row 58 "
            "DFT workflows meta prelude capstone reunion) {#row-198-closing-loop}"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 198 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 218")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row198-dft-workflows-meta-prelude-capstone-reunion-index-row-218" not in sources:
        sources = sources.replace(
            "| 198 | Row 68 → Row 178 Row 68 → Row 58 DFT workflows meta prelude capstone",
            b["sources_table"] + "| 198 | Row 68 → Row 178 Row 68 → Row 58 DFT workflows meta prelude capstone",
            1,
        )
        src197_header = (
            "## Row 68 → Row 178 Row 68 → Row 58 DFT workflows meta prelude capstone reunion index (row 198)"
        )
        sources = sources.replace(
            src197_header,
            b["sources_index"] + src197_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 218")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-218-baby-picture-row68-row198" not in memory:
        memory = memory.replace(
            "| 218 | Meta | [Row 68 → Row 177 Kohn–Sham meta prelude capstone reunion index]",
            b["memory_table"] + "| 218 | Meta | [Row 68 → Row 177 Kohn–Sham meta prelude capstone reunion index]",
            1,
        )
        inserted = False
        for baby_anchor in (
            "### Row 198 baby picture (Row 68 → Row 178 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion)",
            "### Row 178 baby picture (Row 68 → Row 158 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion)",
            "### Row 177 baby picture",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 218")


if __name__ == "__main__":
    main()
