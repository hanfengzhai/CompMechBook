#!/usr/bin/env python3
"""Add row 219 meta-stitch (Row 68 → Row 199 ↔ Row 59 Handshake 3 meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]


def bump199_to_219(text: str) -> str:
    """Transform row-199 capstone-path meta copy to row 219 (179→199 inner, 218 DFT gate)."""
    out = text.replace("row 220", "TEMP_ROW220")
    out = text.replace("row 219", "TEMP_ROW219")
    out = text.replace("row 218", "TEMP_ROW218")
    repl = [
        ("Row 68 → Row 179 Row 68 → Row 59", "Row 68 → Row 199 Row 68 → Row 59"),
        (
            "row68-row179-handshake3-meta-prelude-capstone-reunion-index-row-199",
            "TEMP_ROW219_HS_INDEX",
        ),
        (
            "row-199-baby-picture-row68-row179-handshake3-meta-prelude-capstone-reunion",
            "row-219-baby-picture-row68-row199-handshake3-meta-prelude-capstone-reunion",
        ),
        ("### Row 199 skill checkpoint", "### Row 219 skill checkpoint"),
        ("skill-navigation-row-199", "skill-navigation-row-219"),
        ("prologue-preview-row-199", "prologue-preview-row-219"),
        ("row-199-closing-stitch", "row-219-closing-stitch"),
        ("row-199-closing-loop", "row-219-closing-loop"),
        ("Row 199 three-way audit", "Row 219 three-way audit"),
        (
            "Handshake 3 meta prelude capstone reunion (row 199)",
            "Handshake 3 meta prelude capstone reunion (row 219)",
        ),
        (
            "### Row 199 baby picture",
            "### Row 219 baby picture {#row-219-baby-picture-row68-row199-handshake3-meta-prelude-capstone-reunion}",
        ),
        ("**Row 199 baby picture:**", "**Row 219 baby picture:**"),
        (
            "[row 218](preface.md#skill-navigation-row-218) or [row 199](preface.md#skill-navigation-row-199)",
            "[row 218](preface.md#skill-navigation-row-218) or [row 199](preface.md#skill-navigation-row-199)",
        ),
        (
            "[row 218](preface.md#skill-navigation-row-218) or [Row 68 → Row 179 Handshake 3 meta prelude capstone reunion index (row 199)](appendix/sources.md#row68-row179-handshake3-meta-prelude-capstone-reunion-index-row-199)",
            "[row 218](preface.md#skill-navigation-row-218) or [Row 68 → Row 199 Handshake 3 meta prelude capstone reunion index (row 219)](appendix/sources.md#row68-row199-handshake3-meta-prelude-capstone-reunion-index-row-219)",
        ),
        (
            "verified DFT workflows meta prelude capstone closure (row 218)",
            "verified DFT workflows meta prelude capstone closure (row 218)",
        ),
        (
            "before row 200 Handshake 3 meta prelude capstone reunion opens on the full capstone path",
            "before row 220 Handshake 3 meta prelude capstone reunion opens on the full capstone path",
        ),
        (
            "before row 200 Handshake 3 meta prelude capstone reunion on the full capstone path",
            "before row 220 Handshake 3 meta prelude capstone reunion on the full capstone path",
        ),
        (
            "before row 180 Handshake 3 meta prelude capstone opens on the full capstone path",
            "before row 200 Handshake 3 meta prelude capstone opens on the full capstone path",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW219_HS_INDEX",
        "row68-row199-handshake3-meta-prelude-capstone-reunion-index-row-219",
    )
    out = out.replace("Row 199 does not replace", "Row 219 does not replace")
    out = out.replace("When row 199 is complete", "When row 219 is complete")
    out = out.replace("When row 218 closed", "When row 218 closed")
    out = out.replace("when row 218 closed but row 59", "when row 218 closed but row 59")
    out = out.replace("after row 199 alone", "after row 219 alone")
    out = out.replace("row 218 or row 199 recited", "row 218 or row 199 recited")
    out = out.replace("row 198 or row 179 recited", "row 218 or row 199 recited")
    out = out.replace("When row 198 closed", "When row 218 closed")
    out = out.replace("when row 198 closed", "when row 218 closed")
    out = out.replace("row 198 or row 199", "row 218 or row 199")
    out = out.replace("When row 218 closed", "When row 218 closed")
    out = out.replace("after row 198 alone", "after row 218 alone")
    out = out.replace("from row 199's", "from row 219's")
    out = out.replace("Recite [preface row 218]", "Recite [preface row 218]")
    out = out.replace("Row 179", "@@ROW179CAP@@")
    out = out.replace("row 179", "@@row179@@")
    out = out.replace("@@ROW179CAP@@", "Row 199")
    out = out.replace("@@row179@@", "row 199")
    out = out.replace("row 159", "row 179")
    out = out.replace("Row 159", "Row 179")
    out = out.replace("row 139", "row 159")
    out = out.replace("Row 139", "Row 159")
    out = out.replace(
        "row68-row119-handshake3-meta-capstone-reunion-index-row-139",
        "row68-row139-handshake3-meta-capstone-reunion-index-row-159",
    )
    out = out.replace(
        "row68-row139-handshake3-meta-prelude-capstone-reunion-index-row-159",
        "row68-row159-handshake3-meta-prelude-capstone-reunion-index-row-179",
    )
    out = out.replace(
        "row68-row198-dft-workflows-meta-prelude-capstone-reunion-index-row-218",
        "row68-row199-handshake3-meta-prelude-capstone-reunion-index-row-219",
    )
    out = out.replace("skill-navigation-row-218", "TEMP_SKILL_218")
    out = out.replace("row 218", "row 218")
    out = out.replace("TEMP_SKILL_218", "skill-navigation-row-218")
    out = out.replace("Row 68 → Row 219 Row 68 → Row 59", "Row 68 → Row 199 Row 68 → Row 59")
    out = out.replace("memory sheet row 199 baby picture", "memory sheet row 219 baby picture")
    out = out.replace("prologue row 199 closing stitch", "prologue row 219 closing stitch")
    out = out.replace("prologue row 199 preview", "prologue row 219 preview")
    out = out.replace("epilogue row 199 closing loop", "epilogue row 219 closing loop")
    out = out.replace("opening [row 200]", "opening [row 220]")
    out = out.replace("skill-navigation-row-200", "skill-navigation-row-220")
    out = out.replace("preface row 199", "preface row 219")
    out = out.replace(
        "[row 200](preface.md#skill-navigation-row-200)",
        "[row 220](preface.md#skill-navigation-row-220)",
    )
    out = out.replace("TEMP_ROW218", "row 218")
    out = out.replace("TEMP_ROW219", "row 219")
    out = out.replace("TEMP_ROW220", "row 220")
    out = out.replace(
        "proceed to [row 200](preface.md#skill-navigation-row-200)",
        "proceed to [row 220](preface.md#skill-navigation-row-220)",
    )
    return out


def _load_add199():
    spec = importlib.util.spec_from_file_location("add199", ROOT / "scripts/add-row-199.py")
    add199 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add199)
    return add199


def _build_blocks() -> dict[str, str]:
    add199 = _load_add199()
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 199 skill checkpoint")
    end = preface.index("\n\n### Row 200 skill checkpoint", start)
    row219_preface = bump199_to_219(preface[start:end]) + "\n\n"

    row179_stitch = next(
        line
        for line in (ROOT / "writings/prologue/chapters/00-many-scales.md")
        .read_text()
        .splitlines()
        if line.startswith("**Row 179 closing stitch")
    )
    prologue_stitch = bump199_to_219(
        add199.bump179_to_199(row179_stitch).replace(
            "**Row 199 closing stitch (Row 68 → Row 179",
            "**Row 219 closing stitch (Row 68 → Row 199",
        ).replace("{#row-199-closing-stitch}", "{#row-219-closing-stitch}")
    ) + "\n\n"

    b199 = add199._build_blocks()
    prologue_compass = bump199_to_219(b199["prologue_compass"])
    prologue_preview = bump199_to_219(b199["prologue_preview"])

    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    row199_loop_anchor = (
        "### Row 199 closing loop (Row 68 → Row 179 Row 68 → Row 59 "
        "Handshake 3 meta prelude capstone reunion) {#row-199-closing-loop}"
    )
    row200_loop_end = (
        "### Row 200 closing loop (Row 68 → Row 180 Row 68 → Row 60 "
        "Handshake 3 meta prelude capstone reunion) {#row-200-closing-loop}"
    )
    epilogue_loop = bump199_to_219(
        row199_loop_anchor + epilogue.split(row199_loop_anchor, 1)[1].split(row200_loop_end, 1)[0]
    )
    epilogue_loop = epilogue_loop.replace(
        "### Row 199 closing loop (Row 68 → Row 199 Row 68 → Row 59 "
        "Handshake 3 meta prelude capstone reunion) {#row-219-closing-loop}",
        "### Row 199 closing loop (Row 68 → Row 199 Row 68 → Row 59 "
        "Handshake 3 meta prelude capstone reunion) {#row-219-closing-loop}",
        1,
    )

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src199_header = (
        "## Row 68 → Row 179 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 199)"
    )
    next179_header = (
        "## Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 160)"
    )
    sources_index = bump199_to_219(sources.split(src199_header, 1)[1].split(next179_header, 1)[0])
    sources_index = (
        "## Row 68 → Row 199 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 219) "
        "{#row68-row199-handshake3-meta-prelude-capstone-reunion-index-row-219}"
        + sources_index
    )

    sources_table = bump199_to_219(b199["sources_table"])
    sources_table = sources_table.replace("| 199 | Row 68 → Row 179", "| 219 | Row 68 → Row 199", 1)

    memory_table = bump199_to_219(b199["memory_table"])
    memory_table = memory_table.replace("| 199 | Meta |", "| 219 | Meta |", 1)

    memory_baby = bump199_to_219(b199["memory_baby"])
    if "{#row-219-baby-picture-row68-row199" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 219 baby picture",
            "### Row 219 baby picture {#row-219-baby-picture-row68-row199-handshake3-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row219_preface": row219_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW218_TAIL_OLD = (
    "When row 218 is complete, proceed to [row 199](preface.md#skill-navigation-row-219) when `foundation_export.yaml` exists but Handshake 3 meta prelude capstone still lags after verified DFT workflows meta prelude capstone on the full capstone path, to [row 159](preface.md#skill-navigation-row-159) for the Row 68 ↔ Row 59 Handshake 3 meta audit on the opening-hinge capstone path alone, to [row 139](preface.md#skill-navigation-row-139) for the Row 68 ↔ Row 59 Handshake 3 meta audit on the opening-hinge capstone path alone, to [row 119](preface.md#skill-navigation-row-119) for the Row 68 ↔ Row 59 Handshake 3 meta audit on the opening-hinge prelude path alone, to [row 198](preface.md#skill-navigation-row-158) for the Row 68 ↔ Row 58 DFT workflows meta audit on the opening-hinge capstone path alone, to [row 178](preface.md#skill-navigation-row-138) for the Row 68 ↔ Row 58 DFT workflows meta audit on the opening-hinge prelude path alone, to [row 99](preface.md#skill-navigation-row-99) for the Row 68 ↔ Row 59 Handshake 3 opening prelude audit alone, to [row 79](preface.md#skill-navigation-row-79) for the Row 68 ↔ Row 59 prelude audit alone, to [row 177](preface.md#skill-navigation-row-157) when Kohn–Sham meta prelude capstone still lags after verified Born–Oppenheimer meta prelude capstone on the full capstone path, to [row 58](preface.md#skill-navigation-row-58) when only IX.2 → IX.3 stalls, or extend prose only under `writings/` then sync."
)
ROW218_TAIL_NEW = (
    "When row 218 is complete, proceed to [row 219](preface.md#skill-navigation-row-219) when `foundation_export.yaml` exists but Handshake 3 meta prelude capstone still lags after verified DFT workflows meta prelude capstone on the full capstone path, to [row 199](preface.md#skill-navigation-row-199) when `foundation_export.yaml` exists but IX.3 → Handshake 3 still feels disconnected from verified DFT workflows meta prelude capstone on the opening-hinge capstone path alone, to [row 179](preface.md#skill-navigation-row-179) for the Row 68 ↔ Row 59 Handshake 3 meta audit on the opening-hinge prelude path alone, to [row 218](preface.md#skill-navigation-row-218) for the Row 68 ↔ Row 58 DFT workflows meta audit on the opening-hinge capstone path alone, to [row 198](preface.md#skill-navigation-row-198) for the Row 68 ↔ Row 58 DFT workflows meta audit on the opening-hinge prelude path alone, to [row 99](preface.md#skill-navigation-row-99) for the Row 68 ↔ Row 59 Handshake 3 opening prelude audit alone, to [row 79](preface.md#skill-navigation-row-79) for the Row 68 ↔ Row 59 prelude audit alone, to [row 217](preface.md#skill-navigation-row-217) when Kohn–Sham meta prelude capstone still lags after verified Born–Oppenheimer meta prelude capstone on the full capstone path, to [row 59](preface.md#skill-navigation-row-59) when only IX.3 → Handshake 3 stalls, or extend prose only under `writings/` then sync."
)

ROW218_EPILOGUE_OLD = (
    "Proceed to [row 199](#row-199-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 198 on the full capstone path,"
)
ROW218_EPILOGUE_NEW = (
    "Proceed to [row 219](#row-219-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 218 on the full capstone path,"
)

ROW218_STITCH_OLD = (
    "before row 179 Handshake 3 meta prelude capstone opens on the full capstone path."
)
ROW218_STITCH_NEW = (
    "before row 220 Handshake 3 meta prelude capstone reunion opens on the full capstone path."
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 219 skill checkpoint" in preface:
        print("preface: row 219 already present")
    else:
        if "### Row 218 skill checkpoint" not in preface:
            raise SystemExit("row 218 must exist before row 219")
        if ROW218_TAIL_OLD in preface:
            preface = preface.replace(ROW218_TAIL_OLD, ROW218_TAIL_NEW, 1)
        elif ROW218_TAIL_NEW in preface:
            print("preface: row 218 tail already updated")
        else:
            raise SystemExit("row 218 tail proceed string not found")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row219_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 219")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-219" not in prologue:
        needle = "| Row 68 → Row 179 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion (row 199) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 199 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 219 closing stitch" not in prologue:
            prologue = prologue.replace(
                "**Row 199 closing stitch",
                b["prologue_stitch"] + "**Row 199 closing stitch",
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-199"></span>Row 199 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview row 199 not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW218_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW218_STITCH_OLD, ROW218_STITCH_NEW, 1)
        prologue_path.write_text(prologue)
        print("prologue: added row 219")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "{#row-219-closing-loop}" not in epilogue:
        if ROW218_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW218_EPILOGUE_OLD, ROW218_EPILOGUE_NEW, 1)
        marker = (
            "### Row 199 closing loop (Row 68 → Row 179 Row 68 → Row 59 "
            "Handshake 3 meta prelude capstone reunion) {#row-199-closing-loop}"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 199 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 219")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row199-handshake3-meta-prelude-capstone-reunion-index-row-219" not in sources:
        sources = sources.replace(
            "| 199 | Row 68 → Row 179 Row 68 → Row 59 Handshake 3 meta prelude capstone",
            b["sources_table"] + "| 199 | Row 68 → Row 179 Row 68 → Row 59 Handshake 3 meta prelude capstone",
            1,
        )
        src199_header = (
            "## Row 68 → Row 179 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 199)"
        )
        sources = sources.replace(
            src199_header,
            b["sources_index"] + src199_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 219")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-219-baby-picture-row68-row199" not in memory:
        memory = memory.replace(
            "| 199 | Meta | [Row 68 → Row 179 Handshake 3 meta prelude capstone reunion index]",
            b["memory_table"] + "| 199 | Meta | [Row 68 → Row 179 Handshake 3 meta prelude capstone reunion index]",
            1,
        )
        inserted = False
        for baby_anchor in (
            "### Row 199 baby picture (Row 68 → Row 179 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion)",
            "### Row 179 baby picture {#row-179-baby-picture-row68-row159-handshake3-meta-prelude-capstone-reunion}",
            "### Row 218 baby picture",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 219")


if __name__ == "__main__":
    main()
