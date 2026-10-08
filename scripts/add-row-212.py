#!/usr/bin/env python3
"""Add row 212 meta-stitch (Row 68 → Row 192 ↔ Row 52 atomistic meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]


def bump192_to_212(text: str) -> str:
    """Transform row-192 capstone-path meta copy to row 212 (172→192 inner, 211 gate)."""
    out = text.replace("row 213", "TEMP_ROW213")
    repl = [
        ("Row 68 → Row 172 Row 68 → Row 52", "Row 68 → Row 192 Row 68 → Row 52"),
        (
            "row68-row172-atomistic-meta-prelude-capstone-reunion-index-row-192",
            "TEMP_ROW212_ATOM_INDEX",
        ),
        (
            "row-192-baby-picture-row68-row172-atomistic-meta-prelude-capstone-reunion",
            "row-212-baby-picture-row68-row192-atomistic-meta-prelude-capstone-reunion",
        ),
        ("### Row 192 skill checkpoint", "### Row 212 skill checkpoint"),
        ("skill-navigation-row-192", "skill-navigation-row-212"),
        ("prologue-preview-row-192", "prologue-preview-row-212"),
        ("row-192-closing-stitch", "row-212-closing-stitch"),
        ("row-192-closing-loop", "row-212-closing-loop"),
        ("Row 192 three-way audit", "Row 212 three-way audit"),
        (
            "[row 191](preface.md#skill-navigation-row-191) or [row 172](preface.md#skill-navigation-row-172)",
            "[row 211](preface.md#skill-navigation-row-211) or [row 192](preface.md#skill-navigation-row-192)",
        ),
        (
            "[row 191](preface.md#skill-navigation-row-191) or [Row 68 → Row 172 atomistic meta prelude capstone reunion index (row 192)](appendix/sources.md#row68-row172-atomistic-meta-prelude-capstone-reunion-index-row-192)",
            "[row 211](preface.md#skill-navigation-row-211) or [Row 68 → Row 192 atomistic meta prelude capstone reunion index (row 212)](appendix/sources.md#row68-row192-atomistic-meta-prelude-capstone-reunion-index-row-212)",
        ),
        (
            "verified homogenization meta prelude capstone closure on the full capstone path (row 191)",
            "verified homogenization meta prelude capstone closure on the full capstone path (row 211)",
        ),
        (
            "verified homogenization meta prelude capstone closure (row 191)",
            "verified homogenization meta prelude capstone closure (row 211)",
        ),
        (
            "before row 213 dynamics meta prelude capstone reunion opens on the full capstone path",
            "before row 213 dynamics meta prelude capstone reunion opens on the full capstone path",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW212_ATOM_INDEX",
        "row68-row192-atomistic-meta-prelude-capstone-reunion-index-row-212",
    )
    out = out.replace("Row 192 does not replace", "Row 212 does not replace")
    out = out.replace("When row 192 is complete", "When row 212 is complete")
    out = out.replace("When row 191 closed", "When row 211 closed")
    out = out.replace("after row 192 alone", "after row 212 alone")
    out = out.replace("Recite [preface row 191]", "Recite [preface row 211]")
    out = out.replace("row 191 or row 172 recited", "row 211 or row 192 recited")
    out = out.replace("row 191 and row 52", "row 211 and row 52")
    out = out.replace("after row 191", "after row 211")
    out = out.replace("row 191's polycrystal", "row 211's polycrystal")
    out = out.replace("row 132", "row 152")
    out = out.replace("Row 132", "Row 152")
    out = out.replace("row 152", "row 172")
    out = out.replace("Row 152", "Row 172")
    out = out.replace(
        "row68-row132-atomistic-meta-prelude-capstone-reunion-index-row-152",
        "row68-row152-atomistic-meta-prelude-capstone-reunion-index-row-172",
    )
    out = out.replace(
        "row68-row152-atomistic-meta-prelude-capstone-reunion-index-row-172",
        "TEMP_ATOM172IDX",
    )
    out = out.replace("row 172", "row 192")
    out = out.replace("Row 172", "Row 192")
    out = out.replace(
        "TEMP_ATOM172IDX",
        "row68-row172-atomistic-meta-prelude-capstone-reunion-index-row-192",
    )
    out = out.replace("row 151", "row 171")
    out = out.replace("Row 151", "Row 171")
    out = out.replace(
        "row68-row151-homogenization-meta-prelude-capstone-reunion-index-row-171",
        "row68-row171-homogenization-meta-prelude-capstone-reunion-index-row-191",
    )
    out = out.replace("row 171", "row 191")
    out = out.replace("Row 171", "Row 191")
    out = out.replace("row 191", "row 211")
    out = out.replace("Row 191", "Row 211")
    out = out.replace(
        "[row 193](preface.md#skill-navigation-row-193)",
        "[row 213](preface.md#skill-navigation-row-213)",
    )
    out = out.replace("row 212 or row 192", "row 211 or row 192")
    out = out.replace("memory sheet row 192 baby picture", "memory sheet row 212 baby picture")
    out = out.replace("prologue row 192 closing stitch", "prologue row 212 closing stitch")
    out = out.replace("prologue row 192 preview", "prologue row 212 preview")
    out = out.replace("epilogue row 192 closing loop", "epilogue row 212 closing loop")
    out = out.replace("preface row 192", "preface row 212")
    out = out.replace(
        "reunion index (row 192)](appendix/sources.md#row68-row172-atomistic-meta-prelude-capstone-reunion-index-row-192)",
        "reunion index (row 212)](appendix/sources.md#row68-row192-atomistic-meta-prelude-capstone-reunion-index-row-212)",
    )
    out = out.replace(
        "Prologue preview ([row 192](prologue/00-many-scales.md#prologue-preview-row-212))",
        "Prologue preview ([row 212](prologue/00-many-scales.md#prologue-preview-row-212))",
    )
    out = out.replace("TEMP_ROW213", "row 213")
    out = out.replace(
        "proceed to [row 193](preface.md#skill-navigation-row-193)",
        "proceed to [row 213](preface.md#skill-navigation-row-213)",
    )
    return out


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 192 skill checkpoint")
    end = preface.index("\n\n### Row 193 skill checkpoint", start)
    row212_preface = bump192_to_212(preface[start:end]) + "\n\n"

    spec192 = importlib.util.spec_from_file_location("add192", ROOT / "scripts/add-row-192.py")
    add192 = importlib.util.module_from_spec(spec192)
    spec192.loader.exec_module(add192)
    prologue_stitch = bump192_to_212(add192.PROLOGUE_STITCH.strip()) + "\n\n"

    prologue_compass = bump192_to_212(add192.PROLOGUE_COMPASS)
    prologue_preview = bump192_to_212(add192.PROLOGUE_PREVIEW)

    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    row192_loop_anchor = (
        "### Row 172 closing loop (Row 68 → Row 172 Row 68 → Row 52 "
        "atomistic meta prelude capstone reunion) {#row-192-closing-loop}"
    )
    row193_loop_end = (
        "### Row 173 closing loop (Row 68 → Row 173 Row 68 → Row 53 "
        "dynamics meta prelude capstone reunion) {#row-193-closing-loop}"
    )
    epilogue_loop = bump192_to_212(
        row192_loop_anchor + epilogue.split(row192_loop_anchor, 1)[1].split(row193_loop_end, 1)[0]
    )

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src192_header = (
        "## Row 68 → Row 172 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 192)"
    )
    next172_header = (
        "## Row 68 → Row 152 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 172)"
    )
    sources_index = bump192_to_212(sources.split(src192_header, 1)[1].split(next172_header, 1)[0])
    sources_index = (
        "## Row 68 → Row 192 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 212) "
        "{#row68-row192-atomistic-meta-prelude-capstone-reunion-index-row-212}"
        + sources_index
    )

    sources_table = bump192_to_212(add192.SOURCES_TABLE)
    sources_table = sources_table.replace("| 192 | Row 68 → Row 172", "| 212 | Row 68 → Row 192", 1)

    memory_table = bump192_to_212(add192.MEMORY_TABLE)
    memory_table = memory_table.replace("| 192 | Meta |", "| 212 | Meta |", 1)

    memory = (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text()
    baby_start = "### Row 192 baby picture"
    baby_end = "### Row 193 baby picture"
    if baby_end not in memory:
        baby_end = "### Row 173 baby picture"
    memory_baby = bump192_to_212(baby_start + memory.split(baby_start, 1)[1].split(baby_end, 1)[0])
    memory_baby = memory_baby.replace(
        "### Row 212 baby picture {#row-172-baby-picture",
        "### Row 212 baby picture {#row-212-baby-picture-row68-row192-atomistic-meta-prelude-capstone-reunion} {#row-172-baby-picture",
        1,
    )
    if "{#row-212-baby-picture-row68-row192" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 212 baby picture",
            "### Row 212 baby picture {#row-212-baby-picture-row68-row192-atomistic-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row212_preface": row212_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW211_TAIL_OLD = (
    "When row 211 is complete, proceed to [row 192](preface.md#skill-navigation-row-192) when LAMMPS decks feel like AtomModel homework after verified homogenization meta prelude capstone on the full capstone path, to [row 192](preface.md#skill-navigation-row-192) when atomistic meta prelude capstone still lags after verified homogenization meta prelude capstone on the opening-hinge capstone path alone, to [row 172](preface.md#skill-navigation-row-152) for the Row 68 ↔ Row 52 atomistic meta audit on the opening-hinge prelude path alone, to [row 191](preface.md#skill-navigation-row-171) when homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the opening-hinge capstone path alone, to [row 191](preface.md#skill-navigation-row-151) for the Row 68 ↔ Row 51 homogenization meta audit on the opening-hinge prelude path alone, to [row 210](preface.md#skill-navigation-row-190) when DDD meta prelude capstone still lags after verified taxonomy meta prelude capstone on the full capstone path, to [row 52](preface.md#skill-navigation-row-52) when only VII.3 → VIII.1 stalls, or extend prose only under `writings/` then sync."
)
ROW211_TAIL_NEW = (
    "When row 211 is complete, proceed to [row 212](preface.md#skill-navigation-row-212) when LAMMPS decks feel like AtomModel homework after verified homogenization meta prelude capstone on the full capstone path, to [row 192](preface.md#skill-navigation-row-192) when atomistic meta prelude capstone still lags after verified homogenization meta prelude capstone on the opening-hinge capstone path alone, to [row 172](preface.md#skill-navigation-row-172) for the Row 68 ↔ Row 52 atomistic meta audit on the opening-hinge prelude path alone, to [row 191](preface.md#skill-navigation-row-191) when homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the opening-hinge capstone path alone, to [row 171](preface.md#skill-navigation-row-171) for the Row 68 ↔ Row 51 homogenization meta audit on the opening-hinge prelude path alone, to [row 210](preface.md#skill-navigation-row-210) when DDD meta prelude capstone still lags after verified taxonomy meta prelude capstone on the full capstone path, to [row 52](preface.md#skill-navigation-row-52) when only VII.3 → VIII.1 stalls, or extend prose only under `writings/` then sync."
)

ROW211_EPILOGUE_OLD = (
    "Proceed to [row 192](#row-192-closing-loop) when row 68 closed but atomistic meta prelude capstone still lags after row 191 on the full capstone path,"
)
ROW211_EPILOGUE_NEW = (
    "Proceed to [row 212](#row-212-closing-loop) when row 68 closed but atomistic meta prelude capstone still lags after row 211 on the full capstone path,"
)

ROW211_STITCH_OLD = (
    "before row 212 atomistic meta prelude capstone reunion opens on the full capstone path."
)
ROW211_STITCH_NEW = (
    "before row 213 dynamics meta prelude capstone reunion opens on the full capstone path."
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 212 skill checkpoint" in preface:
        print("preface: row 212 already present")
    else:
        if "### Row 211 skill checkpoint" not in preface:
            raise SystemExit("row 211 must exist before row 212")
        if ROW211_TAIL_OLD in preface:
            preface = preface.replace(ROW211_TAIL_OLD, ROW211_TAIL_NEW, 1)
        elif ROW211_TAIL_NEW in preface:
            print("preface: row 211 tail already updated")
        else:
            raise SystemExit("row 211 tail proceed string not found")
        preface = preface.replace(
            "when opening [row 192](preface.md#skill-navigation-row-192) before row 52 closes on the full capstone path",
            "when opening [row 212](preface.md#skill-navigation-row-212) before row 52 closes on the full capstone path",
            1,
        )
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row212_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 212")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-212" not in prologue:
        needle = "| Row 68 → Row 172 Row 68 → Row 52 atomistic meta prelude capstone reunion (row 192) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 192 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 212 closing stitch" not in prologue:
            prologue = prologue.replace(
                "**Row 192 closing stitch",
                b["prologue_stitch"] + "**Row 192 closing stitch",
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-192"></span>Row 192 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview row 192 not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW211_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW211_STITCH_OLD, ROW211_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 212")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "### Row 212 closing loop" not in epilogue:
        if ROW211_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW211_EPILOGUE_OLD, ROW211_EPILOGUE_NEW, 1)
        marker = (
            "### Row 172 closing loop (Row 68 → Row 172 Row 68 → Row 52 "
            "atomistic meta prelude capstone reunion) {#row-192-closing-loop}"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 192 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 212")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row192-atomistic-meta-prelude-capstone-reunion-index-row-212" not in sources:
        sources = sources.replace(
            "| 192 | Row 68 → Row 172 Row 68 → Row 52 atomistic meta prelude capstone",
            b["sources_table"] + "| 192 | Row 68 → Row 172 Row 68 → Row 52 atomistic meta prelude capstone",
            1,
        )
        sources = sources.replace(
            src192_header := (
                "## Row 68 → Row 172 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 192)"
            ),
            b["sources_index"] + src192_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 212")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-212-baby-picture-row68-row192" not in memory:
        memory = memory.replace(
            "| 192 | Meta | [Row 68 → Row 172 atomistic meta prelude capstone reunion index]",
            b["memory_table"] + "| 192 | Meta | [Row 68 → Row 172 atomistic meta prelude capstone reunion index]",
            1,
        )
        memory = memory.replace("### Row 192 baby picture", b["memory_baby"] + "### Row 192 baby picture", 1)
        memory_path.write_text(memory)
        print("memory-sheet: added row 212")


if __name__ == "__main__":
    main()
