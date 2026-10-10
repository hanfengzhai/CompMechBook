#!/usr/bin/env python3
"""Add row 213 meta-stitch (Row 68 → Row 193 ↔ Row 53 dynamics meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]


def bump193_to_213(text: str) -> str:
    """Transform row-193 capstone-path meta copy to row 213 (173→193 inner, 212 gate)."""
    out = text.replace("row 214", "TEMP_ROW214")
    out = out.replace("row 212", "TEMP_ROW212")
    repl = [
        ("Row 68 → Row 173 Row 68 → Row 53", "Row 68 → Row 193 Row 68 → Row 53"),
        (
            "row68-row173-dynamics-meta-prelude-capstone-reunion-index-row-193",
            "TEMP_ROW213_DYN_INDEX",
        ),
        (
            "row-193-baby-picture-row68-row173-dynamics-meta-prelude-capstone-reunion",
            "row-213-baby-picture-row68-row193-dynamics-meta-prelude-capstone-reunion",
        ),
        ("### Row 193 skill checkpoint", "### Row 213 skill checkpoint"),
        ("skill-navigation-row-193", "skill-navigation-row-213"),
        ("prologue-preview-row-193", "prologue-preview-row-213"),
        ("row-193-closing-stitch", "row-213-closing-stitch"),
        ("row-193-closing-loop", "row-213-closing-loop"),
        ("Row 193 three-way audit", "Row 213 three-way audit"),
        (
            "[row 192](preface.md#skill-navigation-row-192) or [row 173](preface.md#skill-navigation-row-173)",
            "[row 212](preface.md#skill-navigation-row-212) or [row 193](preface.md#skill-navigation-row-193)",
        ),
        (
            "[row 192](preface.md#skill-navigation-row-192) or [Row 68 → Row 173 dynamics meta prelude capstone reunion index (row 173)](appendix/sources.md#row68-row173-dynamics-meta-prelude-capstone-reunion-index-row-193)",
            "[row 212](preface.md#skill-navigation-row-212) or [Row 68 → Row 193 dynamics meta prelude capstone reunion index (row 213)](appendix/sources.md#row68-row193-dynamics-meta-prelude-capstone-reunion-index-row-213)",
        ),
        (
            "verified atomistic meta prelude capstone closure (row 192)",
            "verified atomistic meta prelude capstone closure (row 212)",
        ),
        (
            "before row 194 export meta prelude capstone reunion opens on the full capstone path",
            "before row 214 export meta prelude capstone reunion opens on the full capstone path",
        ),
        (
            "before row 195 export meta prelude opens on the full capstone path",
            "before row 215 export meta prelude opens on the full capstone path",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW213_DYN_INDEX",
        "row68-row193-dynamics-meta-prelude-capstone-reunion-index-row-213",
    )
    out = out.replace("Row 193 does not replace", "Row 213 does not replace")
    out = out.replace("When row 193 is complete", "When row 213 is complete")
    out = out.replace("When row 192 closed", "When row 212 closed")
    out = out.replace("after row 193 alone", "after row 213 alone")
    out = out.replace("Recite [preface row 192]", "Recite [preface row 212]")
    out = out.replace("row 193 or row 173 recited", "row 213 or row 193 recited")
    out = out.replace("row 192 or row 173 recited", "row 212 or row 193 recited")
    out = out.replace("when row 192 closed but row 53", "when row 212 closed but row 53")
    out = out.replace("when row 192 and row 53", "when row 212 and row 53")
    out = out.replace("after row 192 alone", "after row 212 alone")
    out = out.replace("Scene after row 192.", "Scene after row 212.")
    out = out.replace("from row 193's", "from row 212's")
    out = out.replace("row 192's static potential", "row 212's static potential")
    out = out.replace("row 133", "row 153")
    out = out.replace("Row 133", "Row 153")
    out = out.replace("row 113", "row 133")
    out = out.replace("Row 113", "Row 133")
    out = out.replace(
        "row68-row113-dynamics-meta-prelude-capstone-reunion-index-row-133",
        "row68-row133-dynamics-meta-prelude-capstone-reunion-index-row-153",
    )
    out = out.replace("row 153", "row 173")
    out = out.replace("Row 153", "Row 173")
    out = out.replace(
        "row68-row133-dynamics-meta-prelude-capstone-reunion-index-row-153",
        "TEMP_DYN153IDX",
    )
    out = out.replace(
        "row68-row172-atomistic-meta-prelude-capstone-reunion-index-row-192",
        "row68-row192-atomistic-meta-prelude-capstone-reunion-index-row-212",
    )
    out = out.replace("TEMP_DYN153IDX", "row68-row153-dynamics-meta-prelude-capstone-reunion-index-row-173")
    out = out.replace("row 173", "row 193")
    out = out.replace("Row 173", "Row 193")
    out = out.replace(
        "row68-row153-dynamics-meta-prelude-capstone-reunion-index-row-173",
        "TEMP_DYN173IDX",
    )
    out = out.replace("TEMP_DYN173IDX", "row68-row173-dynamics-meta-prelude-capstone-reunion-index-row-193")
    out = out.replace("row 192", "row 212")
    out = out.replace("Row 192", "Row 212")
    out = out.replace("[row 214](preface.md#skill-navigation-row-194)", "[row 214](preface.md#skill-navigation-row-214)")
    out = out.replace("[row 214](preface.md#skill-navigation-row-174)", "[row 214](preface.md#skill-navigation-row-214)")
    out = out.replace("row 213 or row 193", "row 212 or row 193")
    out = out.replace("Row 68 → Row 213 Row 68 → Row 53", "Row 68 → Row 193 Row 68 → Row 53")
    out = out.replace("memory sheet row 193 baby picture", "memory sheet row 213 baby picture")
    out = out.replace("prologue row 193 closing stitch", "prologue row 213 closing stitch")
    out = out.replace("prologue row 193 preview", "prologue row 213 preview")
    out = out.replace("epilogue row 193 closing loop", "epilogue row 213 closing loop")
    out = out.replace(
        "reunion index (row 193)](appendix/sources.md#row68-row173-dynamics-meta-prelude-capstone-reunion-index-row-193)",
        "reunion index (row 213)](appendix/sources.md#row68-row193-dynamics-meta-prelude-capstone-reunion-index-row-213)",
    )
    out = out.replace(
        "Prologue preview ([row 193](prologue/00-many-scales.md#prologue-preview-row-213))",
        "Prologue preview ([row 213](prologue/00-many-scales.md#prologue-preview-row-213))",
    )
    out = out.replace("preface row 193", "preface row 213")
    out = out.replace(
        "[row 194](preface.md#skill-navigation-row-194)",
        "[row 214](preface.md#skill-navigation-row-214)",
    )
    out = out.replace("TEMP_ROW212", "row 212")
    out = out.replace("TEMP_ROW214", "row 214")
    out = out.replace(
        "proceed to [row 194](preface.md#skill-navigation-row-194)",
        "proceed to [row 214](preface.md#skill-navigation-row-214)",
    )
    return out


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 193 skill checkpoint")
    end = preface.index("\n\n### Row 194 skill checkpoint", start)
    row213_preface = bump193_to_213(preface[start:end]) + "\n\n"

    spec193 = importlib.util.spec_from_file_location("add193", ROOT / "scripts/add-row-193.py")
    add193 = importlib.util.module_from_spec(spec193)
    spec193.loader.exec_module(add193)
    prologue_stitch = bump193_to_213(add193.PROLOGUE_STITCH.strip()) + "\n\n"

    prologue_compass = bump193_to_213(add193.PROLOGUE_COMPASS)
    prologue_preview = bump193_to_213(add193.PROLOGUE_PREVIEW)

    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    row193_loop_anchor = (
        "### Row 173 closing loop (Row 68 → Row 173 Row 68 → Row 53 "
        "dynamics meta prelude capstone reunion) {#row-193-closing-loop}"
    )
    row194_loop_end = (
        "### Row 194 closing loop (Row 68 → Row 174 Row 68 → Row 54 "
        "export meta prelude capstone reunion) {#row-194-closing-loop}"
    )
    epilogue_loop = bump193_to_213(
        row193_loop_anchor + epilogue.split(row193_loop_anchor, 1)[1].split(row194_loop_end, 1)[0]
    )

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src193_header = (
        "## Row 68 → Row 173 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 193)"
    )
    next173_header = (
        "## Row 68 → Row 153 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 173)"
    )
    sources_index = bump193_to_213(sources.split(src193_header, 1)[1].split(next173_header, 1)[0])
    sources_index = (
        "## Row 68 → Row 193 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 213) "
        "{#row68-row193-dynamics-meta-prelude-capstone-reunion-index-row-213}"
        + sources_index
    )

    sources_table = bump193_to_213(add193.SOURCES_TABLE)
    sources_table = sources_table.replace("| 193 | Row 68 → Row 193", "| 213 | Row 68 → Row 193", 1)

    memory_table = bump193_to_213(add193.MEMORY_TABLE)
    memory_table = memory_table.replace("| 193 | Meta |", "| 213 | Meta |", 1)

    memory = (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text()
    baby_start = "### Row 193 baby picture"
    if baby_start not in memory:
        baby_start = "### Row 173 baby picture"
    baby_end = "### Row 194 baby picture"
    if baby_end not in memory:
        baby_end = "### Row 174 baby picture"
    if baby_end not in memory:
        baby_end = "### Row 154 baby picture"
    memory_baby = bump193_to_213(baby_start + memory.split(baby_start, 1)[1].split(baby_end, 1)[0])
    memory_baby = memory_baby.replace(
        "### Row 213 baby picture {#row-173-baby-picture",
        "### Row 213 baby picture {#row-213-baby-picture-row68-row193-dynamics-meta-prelude-capstone-reunion} {#row-173-baby-picture",
        1,
    )
    if "{#row-213-baby-picture-row68-row193" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 213 baby picture",
            "### Row 213 baby picture {#row-213-baby-picture-row68-row193-dynamics-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row213_preface": row213_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW212_TAIL_OLD = (
    "When row 212 is complete, proceed to [row 213](preface.md#skill-navigation-row-213) when NVT/NPT still feels like thermostat homework after verified atomistic meta prelude capstone on the full capstone path, to [row 173](preface.md#skill-navigation-row-173) when dynamics meta prelude capstone still lags after verified atomistic meta prelude capstone on the opening-hinge capstone path alone, to [row 153](preface.md#skill-navigation-row-153) for the Row 68 ↔ Row 53 dynamics meta audit on the opening-hinge capstone path alone, to [row 133](preface.md#skill-navigation-row-133) for the Row 68 ↔ Row 53 dynamics meta audit on the opening-hinge prelude path alone, to [row 192](preface.md#skill-navigation-row-172) for the Row 68 ↔ Row 52 atomistic meta audit on the opening-hinge capstone path alone, to [row 192](preface.md#skill-navigation-row-152) for the Row 68 ↔ Row 52 atomistic meta audit on the opening-hinge prelude path alone, to [row 211](preface.md#skill-navigation-row-191) when homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the full capstone path, to [row 52](preface.md#skill-navigation-row-52) when only VII.3 → VIII.1 stalls, to [row 92](preface.md#skill-navigation-row-92) for the Row 68 ↔ Row 52 atomistic opening prelude audit alone, or extend prose only under `writings/` then sync."
)
ROW212_TAIL_NEW = (
    "When row 212 is complete, proceed to [row 213](preface.md#skill-navigation-row-213) when NVT/NPT still feels like thermostat homework after verified atomistic meta prelude capstone on the full capstone path, to [row 193](preface.md#skill-navigation-row-193) when dynamics meta prelude capstone still lags after verified atomistic meta prelude capstone on the opening-hinge capstone path alone, to [row 173](preface.md#skill-navigation-row-173) for the Row 68 ↔ Row 53 dynamics meta audit on the opening-hinge capstone path alone, to [row 153](preface.md#skill-navigation-row-153) for the Row 68 ↔ Row 53 dynamics meta audit on the opening-hinge prelude path alone, to [row 192](preface.md#skill-navigation-row-192) for the Row 68 ↔ Row 52 atomistic meta audit on the opening-hinge capstone path alone, to [row 172](preface.md#skill-navigation-row-172) for the Row 68 ↔ Row 52 atomistic meta audit on the opening-hinge prelude path alone, to [row 211](preface.md#skill-navigation-row-211) when homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the full capstone path, to [row 52](preface.md#skill-navigation-row-52) when only VII.3 → VIII.1 stalls, to [row 92](preface.md#skill-navigation-row-92) for the Row 68 ↔ Row 52 atomistic opening prelude audit alone, or extend prose only under `writings/` then sync."
)

ROW212_EPILOGUE_OLD = (
    "Proceed to [row 193](#row-193-closing-loop) when row 68 closed but dynamics meta prelude capstone still lags after row 192 on the full capstone path,"
)
ROW212_EPILOGUE_NEW = (
    "Proceed to [row 213](#row-213-closing-loop) when row 68 closed but dynamics meta prelude capstone still lags after row 212 on the full capstone path,"
)

ROW212_STITCH_OLD = (
    "before row 213 dynamics meta prelude capstone reunion opens on the full capstone path."
)
ROW212_STITCH_NEW = (
    "before row 214 export meta prelude capstone reunion opens on the full capstone path."
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 213 skill checkpoint" in preface:
        print("preface: row 213 already present")
    else:
        if "### Row 212 skill checkpoint" not in preface:
            raise SystemExit("row 212 must exist before row 213")
        if ROW212_TAIL_OLD in preface:
            preface = preface.replace(ROW212_TAIL_OLD, ROW212_TAIL_NEW, 1)
        elif ROW212_TAIL_NEW in preface:
            print("preface: row 212 tail already updated")
        else:
            raise SystemExit("row 212 tail proceed string not found")
        preface = preface.replace(
            "when opening [row 173](preface.md#skill-navigation-row-173) before row 53 closes on the full capstone path",
            "when opening [row 213](preface.md#skill-navigation-row-213) before row 53 closes on the full capstone path",
            1,
        )
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row213_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 213")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-213" not in prologue:
        needle = "| Row 68 → Row 173 Row 68 → Row 53 dynamics meta prelude capstone reunion (row 193) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 193 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 213 closing stitch" not in prologue:
            for anchor in ("**Row 193 closing stitch", "**Row 173 closing stitch"):
                if anchor in prologue:
                    prologue = prologue.replace(anchor, b["prologue_stitch"] + anchor, 1)
                    break
        preview_anchor = '| <span id="prologue-preview-row-193"></span>Row 193 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview row 193 not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW212_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW212_STITCH_OLD, ROW212_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 213")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "### Row 213 closing loop" not in epilogue:
        if ROW212_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW212_EPILOGUE_OLD, ROW212_EPILOGUE_NEW, 1)
        marker = (
            "### Row 173 closing loop (Row 68 → Row 173 Row 68 → Row 53 "
            "dynamics meta prelude capstone reunion) {#row-193-closing-loop}"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 193 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 213")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row193-dynamics-meta-prelude-capstone-reunion-index-row-213" not in sources:
        sources = sources.replace(
            "| 193 | Row 68 → Row 173 Row 68 → Row 53 dynamics meta prelude capstone",
            b["sources_table"] + "| 193 | Row 68 → Row 173 Row 68 → Row 53 dynamics meta prelude capstone",
            1,
        )
        sources = sources.replace(
            src193_header := (
                "## Row 68 → Row 173 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 193)"
            ),
            b["sources_index"] + src193_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 213")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-213-baby-picture-row68-row193" not in memory:
        memory = memory.replace(
            "| 193 | Meta | [Row 68 → Row 173 dynamics meta prelude capstone reunion index]",
            b["memory_table"] + "| 193 | Meta | [Row 68 → Row 173 dynamics meta prelude capstone reunion index]",
            1,
        )
        inserted = False
        for baby_anchor in ("### Row 193 baby picture", "### Row 173 baby picture"):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 213")


if __name__ == "__main__":
    main()
