#!/usr/bin/env python3
"""Add row 214 meta-stitch (Row 68 → Row 194 ↔ Row 54 export meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]


def bump194_to_214(text: str) -> str:
    """Transform row-194 capstone-path meta copy to row 214 (174→194 inner, 213 gate)."""
    out = text.replace("row 215", "TEMP_ROW215")
    out = text.replace("row 214", "TEMP_ROW214")
    out = text.replace("row 213", "TEMP_ROW213")
    repl = [
        ("Row 68 → Row 174 Row 68 → Row 54", "Row 68 → Row 194 Row 68 → Row 54"),
        (
            "row68-row174-export-meta-prelude-capstone-reunion-index-row-194",
            "TEMP_ROW214_EXP_INDEX",
        ),
        (
            "row-194-baby-picture-row68-row174-export-meta-prelude-capstone-reunion",
            "row-214-baby-picture-row68-row194-export-meta-prelude-capstone-reunion",
        ),
        ("### Row 194 skill checkpoint", "### Row 214 skill checkpoint"),
        ("skill-navigation-row-194", "skill-navigation-row-214"),
        ("prologue-preview-row-194", "prologue-preview-row-214"),
        ("row-194-closing-stitch", "row-214-closing-stitch"),
        ("row-194-closing-loop", "row-214-closing-loop"),
        ("Row 194 three-way audit", "Row 214 three-way audit"),
        (
            "[row 193](preface.md#skill-navigation-row-193) or [row 174](preface.md#skill-navigation-row-174)",
            "[row 213](preface.md#skill-navigation-row-213) or [row 194](preface.md#skill-navigation-row-194)",
        ),
        (
            "[row 193](preface.md#skill-navigation-row-193) or [Row 68 → Row 174 export meta prelude capstone reunion index (row 194)](appendix/sources.md#row68-row174-export-meta-prelude-capstone-reunion-index-row-194)",
            "[row 213](preface.md#skill-navigation-row-213) or [Row 68 → Row 194 export meta prelude capstone reunion index (row 214)](appendix/sources.md#row68-row194-export-meta-prelude-capstone-reunion-index-row-214)",
        ),
        (
            "verified dynamics meta prelude capstone closure (row 193)",
            "verified dynamics meta prelude capstone closure (row 213)",
        ),
        (
            "before row 195 electronic audit meta prelude capstone reunion opens on the full capstone path",
            "before row 215 electronic audit meta prelude capstone reunion opens on the full capstone path",
        ),
        (
            "before row 196 Born–Oppenheimer meta prelude capstone reunion opens on the full capstone path",
            "before row 216 Born–Oppenheimer meta prelude capstone reunion opens on the full capstone path",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW214_EXP_INDEX",
        "row68-row194-export-meta-prelude-capstone-reunion-index-row-214",
    )
    out = out.replace("Row 194 does not replace", "Row 214 does not replace")
    out = out.replace("When row 194 is complete", "When row 214 is complete")
    out = out.replace("When row 193 closed", "When row 213 closed")
    out = out.replace("When row 173 closed", "When row 213 closed")
    out = out.replace("when row 173 closed dynamics", "when row 213 closed dynamics")
    out = out.replace("after row 194 alone", "after row 214 alone")
    out = out.replace("Recite [preface row 193]", "Recite [preface row 213]")
    out = out.replace("row 194 or row 174 recited", "row 214 or row 194 recited")
    out = out.replace("row 193 or row 174 recited", "row 213 or row 194 recited")
    out = out.replace("when row 193 closed but row 54", "when row 213 closed but row 54")
    out = out.replace("when row 193 and row 54", "when row 213 and row 54")
    out = out.replace("after row 193 alone", "after row 213 alone")
    out = out.replace("Scene after row 173.", "Scene after row 193.")
    out = out.replace("from row 194's", "from row 213's")
    out = out.replace("row 193's finite-\\(T\\) dynamics", "row 213's finite-\\(T\\) dynamics")
    out = out.replace("row 114", "row 134")
    out = out.replace("Row 114", "Row 134")
    out = out.replace("row 134", "row 154")
    out = out.replace("Row 134", "Row 154")
    out = out.replace(
        "row68-row114-export-meta-prelude-reunion-index-row-134",
        "row68-row134-export-meta-prelude-capstone-reunion-index-row-154",
    )
    out = out.replace("row 154", "row 174")
    out = out.replace("Row 154", "Row 174")
    out = out.replace(
        "row68-row134-export-meta-prelude-capstone-reunion-index-row-154",
        "TEMP_EXP154IDX",
    )
    out = out.replace(
        "row68-row173-dynamics-meta-prelude-capstone-reunion-index-row-193",
        "row68-row193-dynamics-meta-prelude-capstone-reunion-index-row-213",
    )
    out = out.replace("TEMP_EXP154IDX", "row68-row154-export-meta-prelude-capstone-reunion-index-row-174")
    out = out.replace("row 174", "row 194")
    out = out.replace("Row 174", "Row 194")
    out = out.replace(
        "row68-row154-export-meta-prelude-capstone-reunion-index-row-174",
        "TEMP_EXP174IDX",
    )
    out = out.replace("TEMP_EXP174IDX", "row68-row174-export-meta-prelude-capstone-reunion-index-row-194")
    out = out.replace("row 193", "row 213")
    out = out.replace("Row 193", "Row 213")
    out = out.replace("[row 215](preface.md#skill-navigation-row-195)", "[row 215](preface.md#skill-navigation-row-215)")
    out = out.replace("row 214 or row 194", "row 213 or row 194")
    out = out.replace("Row 68 → Row 214 Row 68 → Row 54", "Row 68 → Row 194 Row 68 → Row 54")
    out = out.replace("memory sheet row 194 baby picture", "memory sheet row 214 baby picture")
    out = out.replace("prologue row 194 closing stitch", "prologue row 214 closing stitch")
    out = out.replace("prologue row 194 preview", "prologue row 214 preview")
    out = out.replace("epilogue row 194 closing loop", "epilogue row 214 closing loop")
    out = out.replace(
        "reunion index (row 194)](appendix/sources.md#row68-row174-export-meta-prelude-capstone-reunion-index-row-194)",
        "reunion index (row 214)](appendix/sources.md#row68-row194-export-meta-prelude-capstone-reunion-index-row-214)",
    )
    out = out.replace(
        "Prologue preview ([row 194](prologue/00-many-scales.md#prologue-preview-row-214))",
        "Prologue preview ([row 214](prologue/00-many-scales.md#prologue-preview-row-214))",
    )
    out = out.replace("preface row 194", "preface row 214")
    out = out.replace(
        "[row 195](preface.md#skill-navigation-row-195)",
        "[row 215](preface.md#skill-navigation-row-215)",
    )
    out = out.replace("TEMP_ROW213", "row 213")
    out = out.replace("TEMP_ROW214", "row 214")
    out = out.replace("TEMP_ROW215", "row 215")
    out = out.replace(
        "proceed to [row 195](preface.md#skill-navigation-row-195)",
        "proceed to [row 215](preface.md#skill-navigation-row-215)",
    )
    return out


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 194 skill checkpoint")
    end = preface.index("\n\n### Row 195 skill checkpoint", start)
    row214_preface = bump194_to_214(preface[start:end]) + "\n\n"

    spec194 = importlib.util.spec_from_file_location("add194", ROOT / "scripts/add-row-194.py")
    add194 = importlib.util.module_from_spec(spec194)
    spec194.loader.exec_module(add194)
    prologue_stitch = bump194_to_214(add194.PROLOGUE_STITCH.strip()) + "\n\n"
    prologue_compass = bump194_to_214(add194.PROLOGUE_COMPASS)
    prologue_preview = bump194_to_214(add194.PROLOGUE_PREVIEW)

    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    row194_loop_anchor = (
        "### Row 194 closing loop (Row 68 → Row 174 Row 68 → Row 54 "
        "export meta prelude capstone reunion) {#row-194-closing-loop}"
    )
    row195_loop_end = (
        "### Row 195 closing loop (Row 68 → Row 175 Row 68 → Row 55 "
        "electronic audit meta prelude capstone reunion) {#row-195-closing-loop}"
    )
    epilogue_loop = bump194_to_214(
        row194_loop_anchor + epilogue.split(row194_loop_anchor, 1)[1].split(row195_loop_end, 1)[0]
    )

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src194_header = (
        "## Row 68 → Row 174 Row 68 → Row 54 export meta prelude capstone reunion index (row 194)"
    )
    next174_header = (
        "## Row 68 → Row 154 Row 68 → Row 54 export meta prelude capstone reunion index (row 174)"
    )
    sources_index = bump194_to_214(sources.split(src194_header, 1)[1].split(next174_header, 1)[0])
    sources_index = (
        "## Row 68 → Row 194 Row 68 → Row 54 export meta prelude capstone reunion index (row 214) "
        "{#row68-row194-export-meta-prelude-capstone-reunion-index-row-214}"
        + sources_index
    )

    sources_table = bump194_to_214(add194.SOURCES_TABLE)
    sources_table = sources_table.replace("| 194 | Row 68 → Row 194", "| 214 | Row 68 → Row 194", 1)

    memory_table = bump194_to_214(add194.MEMORY_TABLE)
    memory_table = memory_table.replace("| 194 | Meta |", "| 214 | Meta |", 1)

    memory = (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text()
    baby_start = "### Row 194 baby picture"
    if baby_start not in memory:
        baby_start = "### Row 174 baby picture"
    baby_end = "### Row 195 baby picture"
    if baby_end not in memory:
        baby_end = "### Row 175 baby picture"
    memory_baby = bump194_to_214(baby_start + memory.split(baby_start, 1)[1].split(baby_end, 1)[0])
    if "{#row-214-baby-picture-row68-row194" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 214 baby picture",
            "### Row 214 baby picture {#row-214-baby-picture-row68-row194-export-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row214_preface": row214_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW213_TAIL_OLD = (
    "When row 213 is complete, proceed to [row 214](preface.md#skill-navigation-row-214) when NPT converges but the pedigree checklist still feels disconnected from verified dynamics meta prelude capstone on the full capstone path, to [row 174](preface.md#skill-navigation-row-174) when NPT converges but the pedigree checklist still feels disconnected from verified dynamics meta prelude capstone on the opening-hinge capstone path alone, to [row 193](preface.md#skill-navigation-row-173) when NVT/NPT still feels like thermostat homework after verified atomistic meta prelude capstone on the opening-hinge capstone path alone, to [row 193](preface.md#skill-navigation-row-153) for the Row 68 ↔ Row 53 dynamics meta audit on the opening-hinge capstone path alone, to [row 193](preface.md#skill-navigation-row-133) for the Row 68 ↔ Row 53 dynamics meta audit on the opening-hinge prelude path alone, to [row 172](preface.md#skill-navigation-row-172) for the Row 68 ↔ Row 52 atomistic meta audit on the opening-hinge capstone path alone, to [row 152](preface.md#skill-navigation-row-152) for the Row 68 ↔ Row 52 atomistic meta audit on the opening-hinge prelude path alone, to [row 212](preface.md#skill-navigation-row-192) when atomistic meta prelude capstone still lags after verified homogenization meta prelude capstone on the full capstone path, to [row 53](preface.md#skill-navigation-row-53) when only VIII.1 → VIII.2 stalls, to [row 93](preface.md#skill-navigation-row-93) for the Row 68 ↔ Row 53 dynamics opening prelude audit alone, or extend prose only under `writings/` then sync."
)
ROW213_TAIL_NEW = (
    "When row 213 is complete, proceed to [row 214](preface.md#skill-navigation-row-214) when NPT converges but the pedigree checklist still feels disconnected from verified dynamics meta prelude capstone on the full capstone path, to [row 194](preface.md#skill-navigation-row-194) when NPT converges but the pedigree checklist still feels disconnected from verified dynamics meta prelude capstone on the opening-hinge capstone path alone, to [row 193](preface.md#skill-navigation-row-193) when NVT/NPT still feels like thermostat homework after verified atomistic meta prelude capstone on the opening-hinge capstone path alone, to [row 173](preface.md#skill-navigation-row-173) for the Row 68 ↔ Row 53 dynamics meta audit on the opening-hinge capstone path alone, to [row 153](preface.md#skill-navigation-row-153) for the Row 68 ↔ Row 53 dynamics meta audit on the opening-hinge prelude path alone, to [row 192](preface.md#skill-navigation-row-192) for the Row 68 ↔ Row 52 atomistic meta audit on the opening-hinge capstone path alone, to [row 172](preface.md#skill-navigation-row-172) for the Row 68 ↔ Row 52 atomistic meta audit on the opening-hinge prelude path alone, to [row 212](preface.md#skill-navigation-row-212) when atomistic meta prelude capstone still lags after verified homogenization meta prelude capstone on the full capstone path, to [row 53](preface.md#skill-navigation-row-53) when only VIII.1 → VIII.2 stalls, to [row 93](preface.md#skill-navigation-row-93) for the Row 68 ↔ Row 53 dynamics opening prelude audit alone, or extend prose only under `writings/` then sync."
)

ROW213_EPILOGUE_OLD = (
    "Proceed to [row 194](#row-194-closing-loop) when row 68 closed but export meta prelude capstone still lags after row 193 on the full capstone path,"
)
ROW213_EPILOGUE_NEW = (
    "Proceed to [row 214](#row-214-closing-loop) when row 68 closed but export meta prelude capstone still lags after row 213 on the full capstone path,"
)

ROW213_STITCH_OLD = (
    "before row 214 export meta prelude capstone reunion opens on the full capstone path."
)
ROW213_STITCH_NEW = (
    "before row 215 electronic audit meta prelude capstone reunion opens on the full capstone path."
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 214 skill checkpoint" in preface:
        print("preface: row 214 already present")
    else:
        if "### Row 213 skill checkpoint" not in preface:
            raise SystemExit("row 213 must exist before row 214")
        if ROW213_TAIL_OLD in preface:
            preface = preface.replace(ROW213_TAIL_OLD, ROW213_TAIL_NEW, 1)
        elif ROW213_TAIL_NEW in preface:
            print("preface: row 213 tail already updated")
        else:
            raise SystemExit("row 213 tail proceed string not found")
        preface = preface.replace(
            "when opening [row 174](preface.md#skill-navigation-row-174) before row 54 closes on the full capstone path",
            "when opening [row 214](preface.md#skill-navigation-row-214) before row 54 closes on the full capstone path",
            1,
        )
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row214_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 214")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-214" not in prologue:
        needle = "| Row 68 → Row 174 Row 68 → Row 54 export meta prelude capstone reunion (row 194) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 194 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 214 closing stitch" not in prologue:
            for anchor in ("**Row 194 closing stitch", "**Row 174 closing stitch"):
                if anchor in prologue:
                    prologue = prologue.replace(anchor, b["prologue_stitch"] + anchor, 1)
                    break
        preview_anchor = '| <span id="prologue-preview-row-194"></span>Row 194 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview row 194 not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW213_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW213_STITCH_OLD, ROW213_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 214")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "### Row 214 closing loop" not in epilogue:
        if ROW213_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW213_EPILOGUE_OLD, ROW213_EPILOGUE_NEW, 1)
        marker = (
            "### Row 194 closing loop (Row 68 → Row 174 Row 68 → Row 54 "
            "export meta prelude capstone reunion) {#row-194-closing-loop}"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 194 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 214")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row194-export-meta-prelude-capstone-reunion-index-row-214" not in sources:
        sources = sources.replace(
            "| 194 | Row 68 → Row 174 Row 68 → Row 54 export meta prelude capstone",
            b["sources_table"] + "| 194 | Row 68 → Row 174 Row 68 → Row 54 export meta prelude capstone",
            1,
        )
        src194_header = (
            "## Row 68 → Row 174 Row 68 → Row 54 export meta prelude capstone reunion index (row 194)"
        )
        sources = sources.replace(
            src194_header,
            b["sources_index"] + src194_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 214")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-214-baby-picture-row68-row194" not in memory:
        memory = memory.replace(
            "| 194 | Meta | [Row 68 → Row 174 export meta prelude capstone reunion index]",
            b["memory_table"] + "| 194 | Meta | [Row 68 → Row 174 export meta prelude capstone reunion index]",
            1,
        )
        inserted = False
        for baby_anchor in ("### Row 194 baby picture", "### Row 174 baby picture"):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 214")


if __name__ == "__main__":
    main()
