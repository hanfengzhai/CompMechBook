#!/usr/bin/env python3
"""Add row 215 meta-stitch (Row 68 → Row 195 ↔ Row 55 electronic audit meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]


def bump195_to_215(text: str) -> str:
    """Transform row-195 capstone-path meta copy to row 215 (175→195 inner, 214 export gate)."""
    out = text.replace("row 216", "TEMP_ROW216")
    out = text.replace("row 215", "TEMP_ROW215")
    out = text.replace("row 214", "TEMP_ROW214")
    repl = [
        ("Row 68 → Row 175 Row 68 → Row 55", "Row 68 → Row 195 Row 68 → Row 55"),
        (
            "row68-row175-electronic-audit-meta-prelude-capstone-reunion-index-row-195",
            "TEMP_ROW215_EA_INDEX",
        ),
        (
            "row-195-baby-picture-row68-row175-electronic-audit-meta-prelude-capstone-reunion",
            "row-215-baby-picture-row68-row195-electronic-audit-meta-prelude-capstone-reunion",
        ),
        ("### Row 195 skill checkpoint", "### Row 215 skill checkpoint"),
        ("skill-navigation-row-195", "skill-navigation-row-215"),
        ("prologue-preview-row-195", "prologue-preview-row-215"),
        ("row-195-closing-stitch", "row-215-closing-stitch"),
        ("row-195-closing-loop", "row-215-closing-loop"),
        ("Row 195 three-way audit", "Row 215 three-way audit"),
        (
            "[row 194](preface.md#skill-navigation-row-194) or [row 175](preface.md#skill-navigation-row-175)",
            "[row 214](preface.md#skill-navigation-row-214) or [row 195](preface.md#skill-navigation-row-195)",
        ),
        (
            "[row 174](preface.md#skill-navigation-row-174) or [Row 68 → Row 175 electronic audit meta prelude capstone reunion index (row 195)](appendix/sources.md#row68-row175-electronic-audit-meta-prelude-capstone-reunion-index-row-195)",
            "[row 214](preface.md#skill-navigation-row-214) or [Row 68 → Row 195 electronic audit meta prelude capstone reunion index (row 215)](appendix/sources.md#row68-row195-electronic-audit-meta-prelude-capstone-reunion-index-row-215)",
        ),
        (
            "verified export meta prelude capstone closure (row 194)",
            "verified export meta prelude capstone closure (row 214)",
        ),
        (
            "before row 196 Born–Oppenheimer meta prelude capstone reunion opens on the full capstone path",
            "before row 216 Born–Oppenheimer meta prelude capstone reunion opens on the full capstone path",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW215_EA_INDEX",
        "row68-row195-electronic-audit-meta-prelude-capstone-reunion-index-row-215",
    )
    out = out.replace("Row 195 does not replace", "Row 215 does not replace")
    out = out.replace("When row 195 is complete", "When row 215 is complete")
    out = out.replace("When row 194 closed", "When row 214 closed")
    out = out.replace("when row 194 closed but row 55", "when row 214 closed but row 55")
    out = out.replace("after row 195 alone", "after row 215 alone")
    out = out.replace("Recite [preface row 194]", "Recite [preface row 214]")
    out = out.replace("row 195 or row 175 recited", "row 215 or row 195 recited")
    out = out.replace("row 194 or row 175 recited", "row 214 or row 195 recited")
    out = out.replace("when row 194 and row 55", "when row 214 and row 55")
    out = out.replace("after row 194 alone", "after row 214 alone")
    out = out.replace("from row 195's", "from row 214's")
    out = out.replace("row 174's yaml pedigree", "row 214's yaml pedigree")
    out = out.replace("row 155", "row 175")
    out = out.replace("Row 155", "Row 175")
    out = out.replace("row 135", "row 155")
    out = out.replace("Row 135", "Row 155")
    out = out.replace(
        "row68-row135-electronic-audit-meta-prelude-capstone-reunion-index-row-155",
        "row68-row155-electronic-audit-meta-prelude-capstone-reunion-index-row-175",
    )
    out = out.replace(
        "row68-row174-export-meta-prelude-capstone-reunion-index-row-194",
        "row68-row194-export-meta-prelude-capstone-reunion-index-row-214",
    )
    out = out.replace("skill-navigation-row-175", "TEMP_SKILL_175")
    out = out.replace("row 175", "row 195")
    out = out.replace("Row 175", "Row 195")
    out = out.replace("TEMP_SKILL_175", "skill-navigation-row-175")
    out = out.replace("[row 195](preface.md#skill-navigation-row-194)", "[row 214](preface.md#skill-navigation-row-214)")
    out = out.replace("[row 195](preface.md#skill-navigation-row-175)", "[row 195](preface.md#skill-navigation-row-195)")
    out = out.replace("Row 68 → Row 215 Row 68 → Row 55", "Row 68 → Row 195 Row 68 → Row 55")
    out = out.replace("memory sheet row 195 baby picture", "memory sheet row 215 baby picture")
    out = out.replace("prologue row 195 closing stitch", "prologue row 215 closing stitch")
    out = out.replace("prologue row 195 preview", "prologue row 215 preview")
    out = out.replace("epilogue row 195 closing loop", "epilogue row 215 closing loop")
    out = out.replace(
        "reunion index (row 195)](appendix/sources.md#row68-row175-electronic-audit-meta-prelude-capstone-reunion-index-row-195)",
        "reunion index (row 215)](appendix/sources.md#row68-row195-electronic-audit-meta-prelude-capstone-reunion-index-row-215)",
    )
    out = out.replace(
        "Prologue preview ([row 195](prologue/00-many-scales.md#prologue-preview-row-215))",
        "Prologue preview ([row 215](prologue/00-many-scales.md#prologue-preview-row-215))",
    )
    out = out.replace("preface row 195", "preface row 215")
    out = out.replace(
        "[row 196](preface.md#skill-navigation-row-196)",
        "[row 216](preface.md#skill-navigation-row-216)",
    )
    out = out.replace("TEMP_ROW214", "row 214")
    out = out.replace("TEMP_ROW215", "row 215")
    out = out.replace("TEMP_ROW216", "row 216")
    out = out.replace(
        "proceed to [row 196](preface.md#skill-navigation-row-196)",
        "proceed to [row 216](preface.md#skill-navigation-row-216)",
    )
    return out


def _load_add195():
    spec = importlib.util.spec_from_file_location("add195", ROOT / "scripts/add-row-195.py")
    add195 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add195)
    return add195


def _build_blocks() -> dict[str, str]:
    add195 = _load_add195()
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 195 skill checkpoint")
    end = preface.index("\n\n### Row 196 skill checkpoint", start)
    row215_preface = bump195_to_215(preface[start:end]) + "\n\n"

    b195 = add195._build_blocks()
    prologue_stitch = bump195_to_215(
        add195.bump175_to_195(
            next(
                line
                for line in (ROOT / "writings/prologue/chapters/00-many-scales.md")
                .read_text()
                .splitlines()
                if line.startswith("**Row 175 closing stitch")
            )
        ).replace(
            "**Row 195 closing stitch (Row 68 → Row 175",
            "**Row 215 closing stitch (Row 68 → Row 195",
        ).replace("{#row-195-closing-stitch}", "{#row-215-closing-stitch}")
    ) + "\n\n"
    prologue_compass = bump195_to_215(b195["prologue_compass"])
    prologue_preview = bump195_to_215(b195["prologue_preview"])

    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    row195_loop_anchor = (
        "### Row 195 closing loop (Row 68 → Row 175 Row 68 → Row 55 "
        "electronic audit meta prelude capstone reunion) {#row-195-closing-loop}"
    )
    row196_loop_end = (
        "### Row 196 closing loop (Row 68 → Row 176 Row 68 → Row 56 "
        "Born–Oppenheimer meta prelude capstone reunion) {#row-196-closing-loop}"
    )
    epilogue_loop = bump195_to_215(
        row195_loop_anchor + epilogue.split(row195_loop_anchor, 1)[1].split(row196_loop_end, 1)[0]
    )

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src195_header = (
        "## Row 68 → Row 175 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 195)"
    )
    next175_header = (
        "## Row 68 → Row 155 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 175)"
    )
    sources_index = bump195_to_215(sources.split(src195_header, 1)[1].split(next175_header, 1)[0])
    sources_index = (
        "## Row 68 → Row 195 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 215) "
        "{#row68-row195-electronic-audit-meta-prelude-capstone-reunion-index-row-215}"
        + sources_index
    )

    sources_table = bump195_to_215(b195["sources_table"])
    sources_table = sources_table.replace("| 195 | Row 68 → Row 195", "| 215 | Row 68 → Row 195", 1)

    memory_table = bump195_to_215(b195["memory_table"])
    memory_table = memory_table.replace("| 195 | Meta |", "| 215 | Meta |", 1)

    memory = (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text()
    baby_start = "### Row 195 baby picture"
    if baby_start not in memory:
        baby_start = "### Row 175 baby picture"
    baby_end = "### Row 196 baby picture"
    if baby_end not in memory:
        baby_end = "### Row 176 baby picture"
    memory_baby = bump195_to_215(
        add195.bump175_to_195(baby_start + memory.split(baby_start, 1)[1].split(baby_end, 1)[0])
    )
    if "{#row-215-baby-picture-row68-row195" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 215 baby picture",
            "### Row 215 baby picture {#row-215-baby-picture-row68-row195-electronic-audit-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row215_preface": row215_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW214_TAIL_OLD = (
    "When row 214 is complete, proceed to [row 215](preface.md#skill-navigation-row-215) when the pedigree checklist is filled but Part IX still feels disconnected from verified export meta prelude capstone on the full capstone path, to [row 175](preface.md#skill-navigation-row-175) when the pedigree checklist is filled but Part IX still feels disconnected from verified export meta prelude capstone on the opening-hinge capstone path alone, to [row 155](preface.md#skill-navigation-row-155) for the Row 68 ↔ Row 55 electronic audit meta audit on the opening-hinge prelude path alone, to [row 194](preface.md#skill-navigation-row-174) for the Row 68 ↔ Row 54 export meta audit on the opening-hinge capstone path alone, to [row 213](preface.md#skill-navigation-row-193) when NVT/NPT still stalls after verified atomistic meta prelude capstone on the full capstone path, to [row 55](preface.md#skill-navigation-row-55) when only VIII.3 → IX.0 stalls, or extend prose only under `writings/` then sync."
)
ROW214_TAIL_NEW = (
    "When row 214 is complete, proceed to [row 215](preface.md#skill-navigation-row-215) when the pedigree checklist is filled but Part IX still feels disconnected from verified export meta prelude capstone on the full capstone path, to [row 195](preface.md#skill-navigation-row-195) when the pedigree checklist is filled but Part IX still feels disconnected from verified export meta prelude capstone on the opening-hinge capstone path alone, to [row 175](preface.md#skill-navigation-row-175) for the Row 68 ↔ Row 55 electronic audit meta audit on the opening-hinge prelude path alone, to [row 214](preface.md#skill-navigation-row-214) for the Row 68 ↔ Row 54 export meta audit on the opening-hinge capstone path alone, to [row 213](preface.md#skill-navigation-row-213) when NVT/NPT still stalls after verified atomistic meta prelude capstone on the full capstone path, to [row 55](preface.md#skill-navigation-row-55) when only VIII.3 → IX.0 stalls, or extend prose only under `writings/` then sync."
)

ROW214_EPILOGUE_OLD = (
    "Proceed to [row 175](#row-175-closing-loop) when row 68 closed but electronic audit meta prelude capstone still lags after row 194 on the full capstone path,"
)
ROW214_EPILOGUE_NEW = (
    "Proceed to [row 215](#row-215-closing-loop) when row 68 closed but electronic audit meta prelude capstone still lags after row 214 on the full capstone path,"
)

ROW214_STITCH_OLD = (
    "before row 215 electronic audit meta prelude capstone reunion opens on the full capstone path."
)
ROW214_STITCH_NEW = (
    "before row 216 Born–Oppenheimer meta prelude capstone reunion opens on the full capstone path."
)

ROW213_STITCH_FIX_OLD = (
    "before row 215 electronic audit meta prelude capstone reunion opens on the full capstone path."
)
ROW213_STITCH_FIX_NEW = (
    "before row 214 export meta prelude capstone reunion opens on the full capstone path."
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 215 skill checkpoint" in preface:
        print("preface: row 215 already present")
    else:
        if "### Row 214 skill checkpoint" not in preface:
            raise SystemExit("row 214 must exist before row 215")
        if ROW214_TAIL_OLD in preface:
            preface = preface.replace(ROW214_TAIL_OLD, ROW214_TAIL_NEW, 1)
        elif ROW214_TAIL_NEW in preface:
            print("preface: row 214 tail already updated")
        else:
            raise SystemExit("row 214 tail proceed string not found")
        preface = preface.replace(
            "when opening [row 135](preface.md#skill-navigation-row-135) before row 55 closes on the full capstone path",
            "when opening [row 215](preface.md#skill-navigation-row-215) before row 55 closes on the full capstone path",
            1,
        )
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row215_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 215")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-215" not in prologue:
        needle = "| Row 68 → Row 175 Row 68 → Row 55 electronic audit meta prelude capstone reunion (row 195) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 195 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 215 closing stitch" not in prologue:
            for anchor in ("**Row 195 closing stitch", "**Row 175 closing stitch"):
                if anchor in prologue:
                    prologue = prologue.replace(anchor, b["prologue_stitch"] + anchor, 1)
                    break
        preview_anchor = '| <span id="prologue-preview-row-195"></span>Row 195 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview row 195 not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW214_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW214_STITCH_OLD, ROW214_STITCH_NEW, 1)
        if ROW213_STITCH_FIX_OLD in prologue:
            prologue = prologue.replace(ROW213_STITCH_FIX_OLD, ROW213_STITCH_FIX_NEW, 1)
        prologue_path.write_text(prologue)
        print("prologue: added row 215")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "{#row-215-closing-loop}" not in epilogue:
        if ROW214_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW214_EPILOGUE_OLD, ROW214_EPILOGUE_NEW, 1)
        marker = (
            "### Row 195 closing loop (Row 68 → Row 175 Row 68 → Row 55 "
            "electronic audit meta prelude capstone reunion) {#row-195-closing-loop}"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 195 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 215")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row195-electronic-audit-meta-prelude-capstone-reunion-index-row-215" not in sources:
        sources = sources.replace(
            "| 195 | Row 68 → Row 175 Row 68 → Row 55 electronic audit meta prelude capstone",
            b["sources_table"] + "| 195 | Row 68 → Row 175 Row 68 → Row 55 electronic audit meta prelude capstone",
            1,
        )
        src195_header = (
            "## Row 68 → Row 175 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 195)"
        )
        sources = sources.replace(
            src195_header,
            b["sources_index"] + src195_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 215")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-215-baby-picture-row68-row195" not in memory:
        memory = memory.replace(
            "| 195 | Meta | [Row 68 → Row 175 electronic audit meta prelude capstone reunion index]",
            b["memory_table"] + "| 195 | Meta | [Row 68 → Row 175 electronic audit meta prelude capstone reunion index]",
            1,
        )
        inserted = False
        for baby_anchor in (
            "### Row 195 baby picture",
            "### Row 175 baby picture (Row 68 → Row 155 Row 68 → Row 55 electronic audit meta prelude capstone reunion) {#row-175-baby-picture-row68-row155-electronic-audit-meta-prelude-capstone-reunion}",
            "### Row 175 baby picture",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 215")


if __name__ == "__main__":
    main()
