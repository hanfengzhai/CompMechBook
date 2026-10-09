#!/usr/bin/env python3
"""Add row 211 meta-stitch (Row 68 → Row 191 ↔ Row 51 homogenization meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]


def bump191_to_211(text: str) -> str:
    """Transform row-191 capstone-path meta copy to row 211 (171→191 inner, 210 gate)."""
    out = text.replace("row 212", "TEMP_ROW212")
    out = out.replace("row 192", "TEMP_ROW192")
    repl = [
        ("Row 68 → Row 171 Row 68 → Row 51", "Row 68 → Row 191 Row 68 → Row 51"),
        (
            "row68-row171-homogenization-meta-prelude-capstone-reunion-index-row-191",
            "TEMP_ROW211_HOMOG_INDEX",
        ),
        (
            "row-191-baby-picture-row68-row171-homogenization-meta-prelude-capstone-reunion",
            "row-211-baby-picture-row68-row191-homogenization-meta-prelude-capstone-reunion",
        ),
        ("### Row 191 skill checkpoint", "### Row 211 skill checkpoint"),
        ("skill-navigation-row-191", "skill-navigation-row-211"),
        ("prologue-preview-row-191", "prologue-preview-row-211"),
        ("row-191-closing-stitch", "row-211-closing-stitch"),
        ("row-191-closing-loop", "row-211-closing-loop"),
        ("Row 191 three-way audit", "Row 211 three-way audit"),
        (
            "[row 190](preface.md#skill-navigation-row-190) or [row 171](preface.md#skill-navigation-row-171)",
            "[row 210](preface.md#skill-navigation-row-210) or [row 191](preface.md#skill-navigation-row-191)",
        ),
        (
            "[row 190](preface.md#skill-navigation-row-170) or [Row 68 → Row 171 homogenization meta prelude capstone reunion index (row 171)](appendix/sources.md#row68-row171-homogenization-meta-prelude-capstone-reunion-index-row-191)",
            "[row 210](preface.md#skill-navigation-row-210) or [Row 68 → Row 191 homogenization meta prelude capstone reunion index (row 211)](appendix/sources.md#row68-row191-homogenization-meta-prelude-capstone-reunion-index-row-211)",
        ),
        (
            "verified DDD meta prelude capstone closure on the full capstone path (row 190)",
            "verified DDD meta prelude capstone closure on the full capstone path (row 210)",
        ),
        (
            "before row 212 atomistic meta prelude capstone reunion opens on the full capstone path",
            "before row 212 atomistic meta prelude capstone reunion opens on the full capstone path",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW211_HOMOG_INDEX",
        "row68-row191-homogenization-meta-prelude-capstone-reunion-index-row-211",
    )
    out = out.replace("Row 191 does not replace", "Row 211 does not replace")
    out = out.replace("When row 191 is complete", "When row 211 is complete")
    out = out.replace("When row 190 closed", "When row 210 closed")
    out = out.replace("after row 190 alone", "after row 210 alone")
    out = out.replace("Recite [preface row 190]", "Recite [preface row 210]")
    out = out.replace("row 190 or row 171 recited", "row 210 or row 191 recited")
    out = out.replace("row 190 and row 51", "row 210 and row 51")
    out = out.replace("after row 190", "after row 210")
    out = out.replace("row 190's segment", "row 210's segment")
    out = out.replace("row 190's Peach", "row 210's Peach")
    out = out.replace("row 132", "row 152")
    out = out.replace("Row 132", "Row 152")
    out = out.replace("row 152", "row 172")
    out = out.replace("Row 152", "Row 172")
    out = out.replace("row 131", "row 151")
    out = out.replace("Row 131", "Row 151")
    out = out.replace(
        "row68-row131-homogenization-meta-prelude-capstone-reunion-index-row-151",
        "row68-row151-homogenization-meta-prelude-capstone-reunion-index-row-171",
    )
    out = out.replace("row 151", "row 171")
    out = out.replace("Row 151", "Row 171")
    out = out.replace(
        "row68-row151-homogenization-meta-prelude-capstone-reunion-index-row-171",
        "TEMP_HOMOG171IDX",
    )
    out = out.replace("row 171", "row 191")
    out = out.replace("Row 171", "Row 191")
    out = out.replace(
        "TEMP_HOMOG171IDX",
        "row68-row171-homogenization-meta-prelude-capstone-reunion-index-row-191",
    )
    out = out.replace("row 170", "row 190")
    out = out.replace("Row 170", "Row 190")
    out = out.replace("row 190", "row 210")
    out = out.replace("Row 190", "Row 210")
    out = out.replace("row 191 or row 171", "row 210 or row 191")
    out = out.replace(
        "[row 192](preface.md#skill-navigation-row-192)",
        "[row 212](preface.md#skill-navigation-row-212)",
    )
    out = out.replace(
        "[row 172](preface.md#skill-navigation-row-172)",
        "[row 192](preface.md#skill-navigation-row-192)",
    )
    out = out.replace("memory sheet row 191 baby picture", "memory sheet row 211 baby picture")
    out = out.replace("prologue row 191 closing stitch", "prologue row 211 closing stitch")
    out = out.replace("prologue row 191 preview", "prologue row 211 preview")
    out = out.replace("epilogue row 191 closing loop", "epilogue row 211 closing loop")
    out = out.replace("preface row 191", "preface row 211")
    out = out.replace(
        "reunion index (row 191)](appendix/sources.md#row68-row171-homogenization-meta-prelude-capstone-reunion-index-row-191)",
        "reunion index (row 211)](appendix/sources.md#row68-row191-homogenization-meta-prelude-capstone-reunion-index-row-211)",
    )
    out = out.replace(
        "Prologue preview ([row 191](prologue/00-many-scales.md#prologue-preview-row-211))",
        "Prologue preview ([row 211](prologue/00-many-scales.md#prologue-preview-row-211))",
    )
    out = out.replace("before atomistic meta prelude capstone", "before atomistic meta prelude capstone")
    out = out.replace("TEMP_ROW192", "row 192")
    out = out.replace("TEMP_ROW212", "row 212")
    out = out.replace(
        "proceed to [row 212](preface.md#skill-navigation-row-212)",
        "proceed to [row 212](preface.md#skill-navigation-row-212)",
    )
    return out


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 191 skill checkpoint")
    end = preface.index("\n\n### Row 192 skill checkpoint", start)
    row211_preface = bump191_to_211(preface[start:end]) + "\n\n"

    spec191 = importlib.util.spec_from_file_location("add191", ROOT / "scripts/add-row-191.py")
    add191 = importlib.util.module_from_spec(spec191)
    spec191.loader.exec_module(add191)
    prologue_stitch = bump191_to_211(add191.PROLOGUE_STITCH.strip()) + "\n\n"

    prologue_compass = bump191_to_211(add191.PROLOGUE_COMPASS)
    prologue_preview = bump191_to_211(add191.PROLOGUE_PREVIEW)

    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    row191_loop_anchor = (
        "### Row 171 closing loop (Row 68 → Row 171 Row 68 → Row 51 "
        "homogenization meta prelude capstone reunion) {#row-191-closing-loop}"
    )
    row192_loop_end = (
        "### Row 172 closing loop (Row 68 → Row 172 Row 68 → Row 52 "
        "atomistic meta prelude capstone reunion) {#row-192-closing-loop}"
    )
    epilogue_loop = bump191_to_211(
        row191_loop_anchor + epilogue.split(row191_loop_anchor, 1)[1].split(row192_loop_end, 1)[0]
    )

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src191_header = (
        "## Row 68 → Row 171 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 191)"
    )
    next171_header = (
        "## Row 68 → Row 151 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 171)"
    )
    sources_index = bump191_to_211(sources.split(src191_header, 1)[1].split(next171_header, 1)[0])
    sources_index = (
        "## Row 68 → Row 191 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 211) "
        "{#row68-row191-homogenization-meta-prelude-capstone-reunion-index-row-211}"
        + sources_index
    )

    sources_table = bump191_to_211(add191.SOURCES_TABLE)
    sources_table = sources_table.replace("| 191 | Row 68 → Row 191", "| 211 | Row 68 → Row 191", 1)

    memory_table = bump191_to_211(add191.MEMORY_TABLE)
    memory_table = memory_table.replace("| 191 | Meta |", "| 211 | Meta |", 1)

    memory = (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text()
    baby_start = "### Row 191 baby picture"
    baby_end = "### Row 192 baby picture"
    if baby_end not in memory:
        baby_end = "### Row 172 baby picture"
    memory_baby = bump191_to_211(baby_start + memory.split(baby_start, 1)[1].split(baby_end, 1)[0])
    memory_baby = memory_baby.replace(
        "### Row 211 baby picture {#row-131-baby-picture",
        "### Row 211 baby picture {#row-211-baby-picture-row68-row191-homogenization-meta-prelude-capstone-reunion} {#row-131-baby-picture",
        1,
    )
    if "{#row-211-baby-picture-row68-row191" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 211 baby picture",
            "### Row 211 baby picture {#row-211-baby-picture-row68-row191-homogenization-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row211_preface": row211_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW210_TAIL_OLD = (
    "When row 210 is complete, proceed to [row 211](preface.md#skill-navigation-row-211) when homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the full capstone path, to [row 191](preface.md#skill-navigation-row-191) when homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the opening-hinge capstone path alone, to [row 171](preface.md#skill-navigation-row-171) for the Row 68 ↔ Row 51 homogenization meta audit on the opening-hinge prelude path alone, to [row 190](preface.md#skill-navigation-row-190) when DDD meta prelude capstone still lags after verified taxonomy meta prelude capstone on the opening-hinge capstone path alone, to [row 170](preface.md#skill-navigation-row-170) when DDD meta prelude capstone still lags after verified taxonomy meta prelude capstone on the opening-hinge prelude path alone, to [row 50](preface.md#skill-navigation-row-50) when only VII.1 → VII.2 stalls, to [row 90](preface.md#skill-navigation-row-90) for the Row 68 ↔ Row 50 DDD opening prelude audit alone, or extend prose only under `writings/` then sync."
)
ROW210_TAIL_NEW = (
    "When row 210 is complete, proceed to [row 211](preface.md#skill-navigation-row-211) when homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the full capstone path, to [row 191](preface.md#skill-navigation-row-191) when homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the opening-hinge capstone path alone, to [row 171](preface.md#skill-navigation-row-171) for the Row 68 ↔ Row 51 homogenization meta audit on the opening-hinge prelude path alone, to [row 210](preface.md#skill-navigation-row-210) when DDD meta prelude capstone still lags after verified taxonomy meta prelude capstone on the opening-hinge capstone path alone, to [row 190](preface.md#skill-navigation-row-190) when DDD meta prelude capstone still lags after verified taxonomy meta prelude capstone on the opening-hinge prelude path alone, to [row 50](preface.md#skill-navigation-row-50) when only VII.1 → VII.2 stalls, to [row 90](preface.md#skill-navigation-row-90) for the Row 68 ↔ Row 50 DDD opening prelude audit alone, or extend prose only under `writings/` then sync."
)

ROW210_EPILOGUE_OLD = (
    "Proceed to [row 191](#row-191-closing-loop) when row 68 closed but homogenization meta prelude capstone still lags after row 190 on the full capstone path,"
)
ROW210_EPILOGUE_NEW = (
    "Proceed to [row 211](#row-211-closing-loop) when row 68 closed but homogenization meta prelude capstone still lags after row 210 on the full capstone path,"
)

ROW210_STITCH_OLD = (
    "before row 211 homogenization meta prelude capstone reunion opens on the full capstone path."
)
ROW210_STITCH_NEW = (
    "before row 212 atomistic meta prelude capstone reunion opens on the full capstone path."
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 211 skill checkpoint" in preface:
        print("preface: row 211 already present")
    else:
        if "### Row 210 skill checkpoint" not in preface:
            raise SystemExit("row 210 must exist before row 211")
        if ROW210_TAIL_OLD in preface:
            preface = preface.replace(ROW210_TAIL_OLD, ROW210_TAIL_NEW, 1)
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row211_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 211")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-211" not in prologue:
        needle = "| Row 68 → Row 171 Row 68 → Row 51 homogenization meta prelude capstone reunion (row 191) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 191 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 211 closing stitch" not in prologue:
            prologue = prologue.replace(
                "**Row 191 closing stitch",
                b["prologue_stitch"] + "**Row 191 closing stitch",
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-191"></span>Row 191 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview row 191 not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW210_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW210_STITCH_OLD, ROW210_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 211")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "### Row 211 closing loop" not in epilogue:
        if ROW210_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW210_EPILOGUE_OLD, ROW210_EPILOGUE_NEW, 1)
        marker = (
            "### Row 171 closing loop (Row 68 → Row 171 Row 68 → Row 51 "
            "homogenization meta prelude capstone reunion) {#row-191-closing-loop}"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 191 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 211")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row191-homogenization-meta-prelude-capstone-reunion-index-row-211" not in sources:
        sources = sources.replace(
            "| 191 | Row 68 → Row 171 Row 68 → Row 51 homogenization meta prelude capstone",
            b["sources_table"] + "| 191 | Row 68 → Row 171 Row 68 → Row 51 homogenization meta prelude capstone",
            1,
        )
        sources = sources.replace(
            src191_header := (
                "## Row 68 → Row 171 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 191)"
            ),
            b["sources_index"] + src191_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 211")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-211-baby-picture-row68-row191" not in memory:
        memory = memory.replace(
            "| 191 | Meta | [Row 68 → Row 171 homogenization meta prelude capstone reunion index]",
            b["memory_table"] + "| 191 | Meta | [Row 68 → Row 171 homogenization meta prelude capstone reunion index]",
            1,
        )
        memory = memory.replace("### Row 191 baby picture", b["memory_baby"] + "### Row 191 baby picture", 1)
        memory_path.write_text(memory)
        print("memory-sheet: added row 211")


if __name__ == "__main__":
    main()
