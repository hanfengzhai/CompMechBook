#!/usr/bin/env python3
"""Add row 216 meta-stitch (Row 68 → Row 196 ↔ Row 56 Born–Oppenheimer meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]


def bump196_to_216(text: str) -> str:
    """Transform row-196 capstone-path meta copy to row 216 (176→196 inner, 215 electronic audit gate)."""
    out = text.replace("row 217", "TEMP_ROW217")
    out = text.replace("row 216", "TEMP_ROW216")
    out = text.replace("row 215", "TEMP_ROW215")
    repl = [
        ("Row 68 → Row 176 Row 68 → Row 56", "Row 68 → Row 196 Row 68 → Row 56"),
        (
            "row68-row176-born-oppenheimer-meta-prelude-capstone-reunion-index-row-196",
            "TEMP_ROW216_BO_INDEX",
        ),
        (
            "row-196-baby-picture-row68-row176-born-oppenheimer-meta-prelude-capstone-reunion",
            "row-216-baby-picture-row68-row196-born-oppenheimer-meta-prelude-capstone-reunion",
        ),
        ("### Row 196 skill checkpoint", "### Row 216 skill checkpoint"),
        ("skill-navigation-row-196", "skill-navigation-row-216"),
        ("prologue-preview-row-196", "prologue-preview-row-216"),
        ("row-196-closing-stitch", "row-216-closing-stitch"),
        ("row-196-closing-loop", "row-216-closing-loop"),
        ("Row 196 three-way audit", "Row 216 three-way audit"),
        (
            "[row 195](preface.md#skill-navigation-row-195) or [row 176](preface.md#skill-navigation-row-176)",
            "[row 215](preface.md#skill-navigation-row-215) or [row 196](preface.md#skill-navigation-row-196)",
        ),
        (
            "[row 195](preface.md#skill-navigation-row-175) or [Row 68 → Row 176 Born–Oppenheimer meta prelude capstone reunion index (row 196)](appendix/sources.md#row68-row176-born-oppenheimer-meta-prelude-capstone-reunion-index-row-196)",
            "[row 215](preface.md#skill-navigation-row-215) or [Row 68 → Row 196 Born–Oppenheimer meta prelude capstone reunion index (row 216)](appendix/sources.md#row68-row196-born-oppenheimer-meta-prelude-capstone-reunion-index-row-216)",
        ),
        (
            "verified electronic audit meta prelude capstone closure (row 195)",
            "verified electronic audit meta prelude capstone closure (row 215)",
        ),
        (
            "before row 197 Kohn–Sham meta prelude capstone reunion opens on the full capstone path",
            "before row 217 Kohn–Sham meta prelude capstone reunion opens on the full capstone path",
        ),
        (
            "before row 198 DFT workflows meta prelude capstone reunion opens on the full capstone path",
            "before row 218 DFT workflows meta prelude capstone reunion opens on the full capstone path",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW216_BO_INDEX",
        "row68-row196-born-oppenheimer-meta-prelude-capstone-reunion-index-row-216",
    )
    out = out.replace("Row 196 does not replace", "Row 216 does not replace")
    out = out.replace("When row 196 is complete", "When row 216 is complete")
    out = out.replace("When row 195 closed", "When row 215 closed")
    out = out.replace("when row 195 closed but row 56", "when row 215 closed but row 56")
    out = out.replace("after row 196 alone", "after row 216 alone")
    out = out.replace("Recite [preface row 195]", "Recite [preface row 215]")
    out = out.replace("row 196 or row 176 recited", "row 216 or row 196 recited")
    out = out.replace("row 195 or row 176 recited", "row 215 or row 196 recited")
    out = out.replace("when row 195 and row 56", "when row 215 and row 56")
    out = out.replace("after row 195 alone", "after row 215 alone")
    out = out.replace("skill-navigation-row-176", "TEMP_SKILL_176")
    out = out.replace("row 176", "row 196")
    out = out.replace("Row 176", "Row 196")
    out = out.replace("TEMP_SKILL_176", "skill-navigation-row-176")
    out = out.replace("[row 196](preface.md#skill-navigation-row-195)", "[row 215](preface.md#skill-navigation-row-215)")
    out = out.replace("[row 196](preface.md#skill-navigation-row-176)", "[row 196](preface.md#skill-navigation-row-196)")
    out = out.replace("row 156", "row 176")
    out = out.replace("Row 156", "Row 176")
    out = out.replace("row 136", "row 156")
    out = out.replace("Row 136", "Row 156")
    out = out.replace(
        "row68-row136-born-oppenheimer-meta-prelude-capstone-reunion-index-row-156",
        "row68-row156-born-oppenheimer-meta-prelude-capstone-reunion-index-row-176",
    )
    out = out.replace(
        "row68-row155-electronic-audit-meta-prelude-capstone-reunion-index-row-175",
        "row68-row175-electronic-audit-meta-prelude-capstone-reunion-index-row-195",
    )
    out = out.replace(
        "row68-row175-electronic-audit-meta-prelude-capstone-reunion-index-row-195",
        "row68-row195-electronic-audit-meta-prelude-capstone-reunion-index-row-215",
    )
    out = out.replace("Row 68 → Row 216 Row 68 → Row 56", "Row 68 → Row 196 Row 68 → Row 56")
    out = out.replace("memory sheet row 196 baby picture", "memory sheet row 216 baby picture")
    out = out.replace("prologue row 196 closing stitch", "prologue row 216 closing stitch")
    out = out.replace("prologue row 196 preview", "prologue row 216 preview")
    out = out.replace("epilogue row 196 closing loop", "epilogue row 216 closing loop")
    out = out.replace(
        "reunion index (row 196)](appendix/sources.md#row68-row176-born-oppenheimer-meta-prelude-capstone-reunion-index-row-196)",
        "reunion index (row 216)](appendix/sources.md#row68-row196-born-oppenheimer-meta-prelude-capstone-reunion-index-row-216)",
    )
    out = out.replace(
        "Prologue preview ([row 196](prologue/00-many-scales.md#prologue-preview-row-216))",
        "Prologue preview ([row 216](prologue/00-many-scales.md#prologue-preview-row-216))",
    )
    out = out.replace("preface row 196", "preface row 216")
    out = out.replace(
        "[row 197](preface.md#skill-navigation-row-197)",
        "[row 217](preface.md#skill-navigation-row-217)",
    )
    out = out.replace("TEMP_ROW215", "row 215")
    out = out.replace("TEMP_ROW216", "row 216")
    out = out.replace("TEMP_ROW217", "row 217")
    out = out.replace(
        "proceed to [row 197](preface.md#skill-navigation-row-197)",
        "proceed to [row 217](preface.md#skill-navigation-row-217)",
    )
    return out


def _load_add196():
    spec = importlib.util.spec_from_file_location("add196", ROOT / "scripts/add-row-196.py")
    add196 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add196)
    return add196


def _build_blocks() -> dict[str, str]:
    add196 = _load_add196()
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 196 skill checkpoint")
    end = preface.index("\n\n### Row 197 skill checkpoint", start)
    row216_preface = bump196_to_216(preface[start:end]) + "\n\n"

    b196 = add196._build_blocks()
    prologue_stitch = bump196_to_216(
        add196.bump176_to_196(
            next(
                line
                for line in (ROOT / "writings/prologue/chapters/00-many-scales.md")
                .read_text()
                .splitlines()
                if line.startswith("**Row 176 closing stitch")
            )
        ).replace(
            "**Row 196 closing stitch (Row 68 → Row 176",
            "**Row 216 closing stitch (Row 68 → Row 196",
        ).replace("{#row-196-closing-stitch}", "{#row-216-closing-stitch}")
    ) + "\n\n"
    prologue_compass = bump196_to_216(b196["prologue_compass"])
    prologue_preview = bump196_to_216(b196["prologue_preview"])

    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    row196_loop_anchor = (
        "### Row 196 closing loop (Row 68 → Row 176 Row 68 → Row 56 "
        "Born–Oppenheimer meta prelude capstone reunion) {#row-196-closing-loop}"
    )
    row197_loop_end = (
        "### Row 197 closing loop (Row 68 → Row 177 Row 68 → Row 57 "
        "Kohn–Sham meta prelude capstone reunion) {#row-197-closing-loop}"
    )
    epilogue_loop = bump196_to_216(
        row196_loop_anchor + epilogue.split(row196_loop_anchor, 1)[1].split(row197_loop_end, 1)[0]
    )

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src196_header = (
        "## Row 68 → Row 176 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion index (row 196)"
    )
    next176_header = (
        "## Row 68 → Row 156 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion index (row 176)"
    )
    sources_index = bump196_to_216(sources.split(src196_header, 1)[1].split(next176_header, 1)[0])
    sources_index = (
        "## Row 68 → Row 196 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion index (row 216) "
        "{#row68-row196-born-oppenheimer-meta-prelude-capstone-reunion-index-row-216}"
        + sources_index
    )

    sources_table = bump196_to_216(b196["sources_table"])
    sources_table = sources_table.replace("| 196 | Row 68 → Row 196", "| 216 | Row 68 → Row 196", 1)

    memory_table = bump196_to_216(b196["memory_table"])
    memory_table = memory_table.replace("| 196 | Meta |", "| 216 | Meta |", 1)

    memory = (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text()
    baby_start = "### Row 196 baby picture"
    if baby_start not in memory:
        baby_start = "### Row 176 baby picture"
    baby_end = "### Row 197 baby picture"
    if baby_end not in memory:
        baby_end = "### Row 177 baby picture"
    memory_baby = bump196_to_216(
        add196.bump176_to_196(baby_start + memory.split(baby_start, 1)[1].split(baby_end, 1)[0])
    )
    if "{#row-216-baby-picture-row68-row196" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 216 baby picture",
            "### Row 216 baby picture {#row-216-baby-picture-row68-row196-born-oppenheimer-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row216_preface": row216_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW215_TAIL_OLD = (
    "When row 215 is complete, proceed to [row 216](preface.md#skill-navigation-row-216) when `cu.relax.out` exists on the full capstone path, to [row 176](preface.md#skill-navigation-row-176) when `cu.relax.out` exists but IX.1 still feels disconnected from verified electronic audit meta prelude capstone on the opening-hinge capstone path alone, to [row 156](preface.md#skill-navigation-row-136) for the Row 68 ↔ Row 56 Born–Oppenheimer meta audit on the opening-hinge prelude path alone, to [row 195](preface.md#skill-navigation-row-195) for the Row 68 ↔ Row 55 electronic audit meta audit on the opening-hinge capstone path alone, to [row 194](preface.md#skill-navigation-row-194) when yaml exports still stall after verified export meta prelude capstone on the full capstone path, to [row 56](preface.md#skill-navigation-row-56) when only IX.0 → IX.1 stalls, or extend prose only under `writings/` then sync."
)
ROW215_TAIL_NEW = (
    "When row 215 is complete, proceed to [row 216](preface.md#skill-navigation-row-216) when `cu.relax.out` exists on the full capstone path, to [row 196](preface.md#skill-navigation-row-196) when `cu.relax.out` exists but IX.1 still feels disconnected from verified electronic audit meta prelude capstone on the opening-hinge capstone path alone, to [row 176](preface.md#skill-navigation-row-176) for the Row 68 ↔ Row 56 Born–Oppenheimer meta audit on the opening-hinge prelude path alone, to [row 215](preface.md#skill-navigation-row-215) for the Row 68 ↔ Row 55 electronic audit meta audit on the opening-hinge capstone path alone, to [row 214](preface.md#skill-navigation-row-214) when yaml exports still stall after verified export meta prelude capstone on the full capstone path, to [row 56](preface.md#skill-navigation-row-56) when only IX.0 → IX.1 stalls, or extend prose only under `writings/` then sync."
)

ROW215_EPILOGUE_OLD = (
    "Proceed to [row 196](#row-196-closing-loop) when row 68 closed but Born–Oppenheimer meta prelude capstone still lags after row 195 on the full capstone path,"
)
ROW215_EPILOGUE_NEW = (
    "Proceed to [row 216](#row-216-closing-loop) when row 68 closed but Born–Oppenheimer meta prelude capstone still lags after row 215 on the full capstone path,"
)

ROW215_STITCH_OLD = (
    "before row 216 Born–Oppenheimer meta prelude capstone reunion opens on the full capstone path."
)
ROW215_STITCH_NEW = (
    "before row 217 Kohn–Sham meta prelude capstone reunion opens on the full capstone path."
)

ROW214_STITCH_FIX_OLD = (
    "before row 216 Born–Oppenheimer meta prelude capstone reunion opens on the full capstone path."
)
ROW214_STITCH_FIX_NEW = (
    "before row 215 electronic audit meta prelude capstone reunion opens on the full capstone path."
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 216 skill checkpoint" in preface:
        print("preface: row 216 already present")
    else:
        if "### Row 215 skill checkpoint" not in preface:
            raise SystemExit("row 215 must exist before row 216")
        if ROW215_TAIL_OLD in preface:
            preface = preface.replace(ROW215_TAIL_OLD, ROW215_TAIL_NEW, 1)
        elif ROW215_TAIL_NEW in preface:
            print("preface: row 215 tail already updated")
        else:
            raise SystemExit("row 215 tail proceed string not found")
        preface = preface.replace(
            "when opening [row 156](preface.md#skill-navigation-row-156) before row 56 closes on the full capstone path",
            "when opening [row 216](preface.md#skill-navigation-row-216) before row 56 closes on the full capstone path",
            1,
        )
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row216_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 216")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-216" not in prologue:
        needle = "| Row 68 → Row 176 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion (row 196) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 196 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 216 closing stitch" not in prologue:
            for anchor in ("**Row 196 closing stitch", "**Row 176 closing stitch"):
                if anchor in prologue:
                    prologue = prologue.replace(anchor, b["prologue_stitch"] + anchor, 1)
                    break
        preview_anchor = '| <span id="prologue-preview-row-196"></span>Row 196 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview row 196 not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW215_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW215_STITCH_OLD, ROW215_STITCH_NEW, 1)
        if ROW214_STITCH_FIX_OLD in prologue:
            prologue = prologue.replace(ROW214_STITCH_FIX_OLD, ROW214_STITCH_FIX_NEW, 1)
        prologue_path.write_text(prologue)
        print("prologue: added row 216")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "{#row-216-closing-loop}" not in epilogue:
        if ROW215_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW215_EPILOGUE_OLD, ROW215_EPILOGUE_NEW, 1)
        marker = (
            "### Row 196 closing loop (Row 68 → Row 176 Row 68 → Row 56 "
            "Born–Oppenheimer meta prelude capstone reunion) {#row-196-closing-loop}"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 196 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 216")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row196-born-oppenheimer-meta-prelude-capstone-reunion-index-row-216" not in sources:
        sources = sources.replace(
            "| 196 | Row 68 → Row 176 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone",
            b["sources_table"] + "| 196 | Row 68 → Row 176 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone",
            1,
        )
        src196_header = (
            "## Row 68 → Row 176 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion index (row 196)"
        )
        sources = sources.replace(
            src196_header,
            b["sources_index"] + src196_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 216")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-216-baby-picture-row68-row196" not in memory:
        memory = memory.replace(
            "| 196 | Meta | [Row 68 → Row 176 Born–Oppenheimer meta prelude capstone reunion index]",
            b["memory_table"] + "| 196 | Meta | [Row 68 → Row 176 Born–Oppenheimer meta prelude capstone reunion index]",
            1,
        )
        inserted = False
        for baby_anchor in (
            "### Row 196 baby picture",
            "### Row 176 baby picture (Row 68 → Row 156 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion) {#row-176-baby-picture-row68-row156-born-oppenheimer-meta-prelude-capstone-reunion}",
            "### Row 176 baby picture",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 216")


if __name__ == "__main__":
    main()
