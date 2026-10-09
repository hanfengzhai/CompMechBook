#!/usr/bin/env python3
"""Add row 217 meta-stitch (Row 68 → Row 197 ↔ Row 57 Kohn–Sham meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]


def bump197_to_217(text: str) -> str:
    """Transform row-197 capstone-path meta copy to row 217 (177→197 inner, 216 BO gate)."""
    out = text.replace("row 218", "TEMP_ROW218")
    out = text.replace("row 217", "TEMP_ROW217")
    out = text.replace("row 216", "TEMP_ROW216")
    repl = [
        ("Row 68 → Row 177 Row 68 → Row 57", "Row 68 → Row 197 Row 68 → Row 57"),
        (
            "row68-row177-kohn-sham-meta-prelude-capstone-reunion-index-row-197",
            "TEMP_ROW217_KS_INDEX",
        ),
        (
            "row-197-baby-picture-row68-row177-kohn-sham-meta-prelude-capstone-reunion",
            "row-217-baby-picture-row68-row197-kohn-sham-meta-prelude-capstone-reunion",
        ),
        ("### Row 197 skill checkpoint", "### Row 217 skill checkpoint"),
        ("skill-navigation-row-197", "skill-navigation-row-217"),
        ("prologue-preview-row-197", "prologue-preview-row-217"),
        ("row-197-closing-stitch", "row-217-closing-stitch"),
        ("row-197-closing-loop", "row-217-closing-loop"),
        ("Row 197 three-way audit", "Row 217 three-way audit"),
        (
            "Kohn–Sham meta prelude capstone reunion (row 197)",
            "Kohn–Sham meta prelude capstone reunion (row 217)",
        ),
        (
            "### Row 197 baby picture",
            "### Row 217 baby picture {#row-217-baby-picture-row68-row197-kohn-sham-meta-prelude-capstone-reunion}",
        ),
        ("**Row 197 baby picture:**", "**Row 217 baby picture:**"),
        (
            "[row 196](preface.md#skill-navigation-row-196) or [row 177](preface.md#skill-navigation-row-177)",
            "[row 216](preface.md#skill-navigation-row-216) or [row 197](preface.md#skill-navigation-row-197)",
        ),
        (
            "[row 196](preface.md#skill-navigation-row-176) or [row 177](preface.md#skill-navigation-row-157)",
            "[row 216](preface.md#skill-navigation-row-216) or [row 197](preface.md#skill-navigation-row-197)",
        ),
        (
            "[row 196](preface.md#skill-navigation-row-196) or [Row 68 → Row 177 Kohn–Sham meta prelude capstone reunion index (row 197)](appendix/sources.md#row68-row177-kohn-sham-meta-prelude-capstone-reunion-index-row-197)",
            "[row 216](preface.md#skill-navigation-row-216) or [Row 68 → Row 197 Kohn–Sham meta prelude capstone reunion index (row 217)](appendix/sources.md#row68-row197-kohn-sham-meta-prelude-capstone-reunion-index-row-217)",
        ),
        (
            "verified Born–Oppenheimer meta prelude capstone closure (row 196)",
            "verified Born–Oppenheimer meta prelude capstone closure (row 216)",
        ),
        (
            "before row 198 DFT workflows meta prelude capstone reunion opens on the full capstone path",
            "before row 218 DFT workflows meta prelude capstone reunion opens on the full capstone path",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW217_KS_INDEX",
        "row68-row197-kohn-sham-meta-prelude-capstone-reunion-index-row-217",
    )
    out = out.replace("Row 197 does not replace", "Row 217 does not replace")
    out = out.replace("When row 197 is complete", "When row 217 is complete")
    out = out.replace("When row 196 closed", "When row 216 closed")
    out = out.replace("when row 196 closed but row 57", "when row 216 closed but row 57")
    out = out.replace("after row 197 alone", "after row 216 alone")
    out = out.replace("Recite [preface row 196]", "Recite [preface row 216]")
    out = out.replace("row 197 or row 177 recited", "row 217 or row 197 recited")
    out = out.replace("row 196 or row 177 recited", "row 216 or row 197 recited")
    out = out.replace("Row 177", "@@ROW177CAP@@")
    out = out.replace("row 177", "@@row177@@")
    out = out.replace("@@ROW177CAP@@", "Row 197")
    out = out.replace("@@row177@@", "row 197")
    out = out.replace("row 157", "row 177")
    out = out.replace("Row 157", "Row 177")
    out = out.replace("row 137", "row 157")
    out = out.replace("Row 137", "Row 157")
    out = out.replace(
        "row68-row157-kohn-sham-meta-prelude-capstone-reunion-index-row-177",
        "row68-row177-kohn-sham-meta-prelude-capstone-reunion-index-row-197",
    )
    out = out.replace(
        "row68-row176-born-oppenheimer-meta-prelude-capstone-reunion-index-row-196",
        "row68-row196-born-oppenheimer-meta-prelude-capstone-reunion-index-row-216",
    )
    out = out.replace("skill-navigation-row-196", "TEMP_SKILL_196")
    out = out.replace("row 196", "row 216")
    out = out.replace("Row 196", "Row 216")
    out = out.replace("TEMP_SKILL_196", "skill-navigation-row-196")
    out = out.replace("Row 68 → Row 217 Row 68 → Row 57", "Row 68 → Row 197 Row 68 → Row 57")
    out = out.replace("memory sheet row 197 baby picture", "memory sheet row 217 baby picture")
    out = out.replace("prologue row 197 closing stitch", "prologue row 217 closing stitch")
    out = out.replace("prologue row 197 preview", "prologue row 217 preview")
    out = out.replace("epilogue row 197 closing loop", "epilogue row 217 closing loop")
    out = out.replace("opening [row 198]", "opening [row 218]")
    out = out.replace("skill-navigation-row-198", "skill-navigation-row-218")
    out = out.replace(
        "Prologue preview ([row 217](prologue/00-many-scales.md#prologue-preview-row-217))",
        "Prologue preview ([row 217](prologue/00-many-scales.md#prologue-preview-row-217))",
    )
    out = out.replace("preface row 197", "preface row 217")
    out = out.replace(
        "[row 198](preface.md#skill-navigation-row-198)",
        "[row 218](preface.md#skill-navigation-row-218)",
    )
    out = out.replace("TEMP_ROW216", "row 216")
    out = out.replace("TEMP_ROW217", "row 217")
    out = out.replace("TEMP_ROW218", "row 218")
    out = out.replace(
        "proceed to [row 198](preface.md#skill-navigation-row-198)",
        "proceed to [row 218](preface.md#skill-navigation-row-218)",
    )
    return out


def _load_add197():
    spec = importlib.util.spec_from_file_location("add197", ROOT / "scripts/add-row-197.py")
    add197 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add197)
    return add197


def _build_blocks() -> dict[str, str]:
    add197 = _load_add197()
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 197 skill checkpoint")
    end = preface.index("\n\n### Row 198 skill checkpoint", start)
    row217_preface = bump197_to_217(preface[start:end]) + "\n\n"

    row177_stitch = next(
        line
        for line in (ROOT / "writings/prologue/chapters/00-many-scales.md")
        .read_text()
        .splitlines()
        if line.startswith("**Row 177 closing stitch")
    )
    prologue_stitch = bump197_to_217(
        add197.bump177_to_197(row177_stitch).replace(
            "**Row 197 closing stitch (Row 68 → Row 177",
            "**Row 217 closing stitch (Row 68 → Row 197",
        ).replace("{#row-197-closing-stitch}", "{#row-217-closing-stitch}")
    ) + "\n\n"

    b197 = add197._build_blocks()
    prologue_compass = bump197_to_217(b197["prologue_compass"])
    prologue_preview = bump197_to_217(b197["prologue_preview"])

    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    row197_loop_anchor = (
        "### Row 197 closing loop (Row 68 → Row 177 Row 68 → Row 57 "
        "Kohn–Sham meta prelude capstone reunion) {#row-197-closing-loop}"
    )
    row198_loop_end = (
        "### Row 198 closing loop (Row 68 → Row 178 Row 68 → Row 58 "
        "DFT workflows meta prelude capstone reunion) {#row-198-closing-loop}"
    )
    epilogue_loop = bump197_to_217(
        row197_loop_anchor + epilogue.split(row197_loop_anchor, 1)[1].split(row198_loop_end, 1)[0]
    )

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src197_header = (
        "## Row 68 → Row 177 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion index (row 197)"
    )
    next177_header = (
        "## Row 68 → Row 157 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion index (row 177)"
    )
    sources_index = bump197_to_217(sources.split(src197_header, 1)[1].split(next177_header, 1)[0])
    sources_index = (
        "## Row 68 → Row 197 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion index (row 217) "
        "{#row68-row197-kohn-sham-meta-prelude-capstone-reunion-index-row-217}"
        + sources_index
    )

    sources_table = bump197_to_217(b197["sources_table"])
    sources_table = sources_table.replace("| 197 | Row 68 → Row 197", "| 217 | Row 68 → Row 197", 1)

    memory_table = bump197_to_217(b197["memory_table"])
    memory_table = memory_table.replace("| 197 | Meta |", "| 217 | Meta |", 1)

    memory_baby = bump197_to_217(b197["memory_baby"])
    if "{#row-217-baby-picture-row68-row197" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 217 baby picture",
            "### Row 217 baby picture {#row-217-baby-picture-row68-row197-kohn-sham-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row217_preface": row217_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW216_TAIL_OLD = (
    "When row 216 is complete, proceed to [row 197](preface.md#skill-navigation-row-197) when `murnaghan_eos.yaml` exists on the full capstone path, to [row 177](preface.md#skill-navigation-row-177) when `murnaghan_eos.yaml` exists but IX.2 still feels disconnected from verified Born–Oppenheimer meta prelude capstone on the opening-hinge capstone path alone, to [row 157](preface.md#skill-navigation-row-157) for the Row 68 ↔ Row 57 Kohn–Sham meta audit on the opening-hinge prelude path alone, to [row 176](preface.md#skill-navigation-row-176) for the Row 68 ↔ Row 56 Born–Oppenheimer meta audit on the opening-hinge capstone path alone, to [row 194](preface.md#skill-navigation-row-194) when `cu.relax.out` is missing after verified export meta prelude capstone on the full capstone path, to [row 57](preface.md#skill-navigation-row-57) when only IX.1 → IX.2 stalls, or extend prose only under `writings/` then sync."
)
ROW216_TAIL_NEW = (
    "When row 216 is complete, proceed to [row 217](preface.md#skill-navigation-row-217) when `murnaghan_eos.yaml` exists on the full capstone path, to [row 197](preface.md#skill-navigation-row-197) when `murnaghan_eos.yaml` exists but IX.2 still feels disconnected from verified Born–Oppenheimer meta prelude capstone on the opening-hinge capstone path alone, to [row 177](preface.md#skill-navigation-row-177) for the Row 68 ↔ Row 57 Kohn–Sham meta audit on the opening-hinge prelude path alone, to [row 196](preface.md#skill-navigation-row-196) for the Row 68 ↔ Row 56 Born–Oppenheimer meta audit on the opening-hinge capstone path alone, to [row 214](preface.md#skill-navigation-row-214) when `cu.relax.out` is missing after verified export meta prelude capstone on the full capstone path, to [row 57](preface.md#skill-navigation-row-57) when only IX.1 → IX.2 stalls, or extend prose only under `writings/` then sync."
)

ROW216_EPILOGUE_PROCEED_OLD = (
    "Proceed to [row 197](#row-197-closing-loop) when row 68 closed but Kohn–Sham meta prelude capstone still lags after row 196 on the full capstone path,"
)
ROW216_EPILOGUE_PROCEED_NEW = (
    "Proceed to [row 217](#row-217-closing-loop) when row 68 closed but Kohn–Sham meta prelude capstone still lags after row 216 on the full capstone path,"
)

ROW216_STITCH_OLD = (
    "before row 197 Kohn–Sham meta prelude capstone reunion opens on the full capstone path."
)
ROW216_STITCH_NEW = (
    "before row 217 Kohn–Sham meta prelude capstone reunion opens on the full capstone path."
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 217 skill checkpoint" in preface:
        print("preface: row 217 already present")
    else:
        if "### Row 216 skill checkpoint" not in preface:
            raise SystemExit("row 216 must exist before row 217")
        if ROW216_TAIL_OLD in preface:
            preface = preface.replace(ROW216_TAIL_OLD, ROW216_TAIL_NEW, 1)
        elif ROW216_TAIL_NEW in preface or "proceed to [row 217](preface.md#skill-navigation-row-217)" in preface:
            print("preface: row 216 tail already updated")
        else:
            raise SystemExit("row 216 tail proceed string not found")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row217_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 217")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-217" not in prologue:
        needle = "| Row 68 → Row 177 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion (row 197) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 197 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 217 closing stitch" not in prologue:
            prologue = prologue.replace(
                "**Row 177 closing stitch",
                b["prologue_stitch"] + "**Row 177 closing stitch",
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-197"></span>Row 197 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview row 197 not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW216_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW216_STITCH_OLD, ROW216_STITCH_NEW, 1)
        prologue_path.write_text(prologue)
        print("prologue: added row 217")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "{#row-217-closing-loop}" not in epilogue:
        if ROW216_EPILOGUE_PROCEED_OLD in epilogue:
            epilogue = epilogue.replace(ROW216_EPILOGUE_PROCEED_OLD, ROW216_EPILOGUE_PROCEED_NEW, 1)
        marker = (
            "### Row 197 closing loop (Row 68 → Row 177 Row 68 → Row 57 "
            "Kohn–Sham meta prelude capstone reunion) {#row-197-closing-loop}"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 197 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 217")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row197-kohn-sham-meta-prelude-capstone-reunion-index-row-217" not in sources:
        sources = sources.replace(
            "| 197 | Row 68 → Row 177 Row 68 → Row 57 Kohn–Sham meta prelude capstone",
            b["sources_table"] + "| 197 | Row 68 → Row 177 Row 68 → Row 57 Kohn–Sham meta prelude capstone",
            1,
        )
        src197_header = (
            "## Row 68 → Row 177 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion index (row 197)"
        )
        sources = sources.replace(
            src197_header,
            b["sources_index"] + src197_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 217")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-217-baby-picture-row68-row197" not in memory:
        memory = memory.replace(
            "| 197 | Meta | [Row 68 → Row 177 Kohn–Sham meta prelude capstone reunion index]",
            b["memory_table"] + "| 197 | Meta | [Row 68 → Row 177 Kohn–Sham meta prelude capstone reunion index]",
            1,
        )
        inserted = False
        for baby_anchor in (
            "### Row 197 baby picture (Row 68 → Row 177 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion)",
            "### Row 177 baby picture (Row 68 → Row 157 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion)",
            "### Row 177 baby picture",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 217")


if __name__ == "__main__":
    main()
