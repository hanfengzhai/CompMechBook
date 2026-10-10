#!/usr/bin/env python3
"""Add row 220 meta-stitch (Row 68 → Row 200 ↔ Row 60 Handshake 3 meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]

def bump200_to_220(text: str) -> str:
    """Transform row-180 capstone-path meta copy to row 220 (200→220, 180→200 inner, 219 gate)."""
    out = text.replace("row 221", "TEMP_ROW201")
    out = out.replace("row 220", "TEMP_ROW200")
    out = out.replace("row 219", "TEMP_ROW199")
    repl = [
        ("Row 68 → Row 200 Row 68 → Row 60", "Row 68 → Row 200 Row 68 → Row 60"),
        (
            "row 220_EXP_INDEX",
            "row68-row200-handshake3-meta-prelude-capstone-reunion-index-row-220",
        ),
        (
            "row-220-baby-picture-row68-row200-handshake3-meta-prelude-capstone-reunion",
            "row-220-baby-picture-row68-row200-handshake3-meta-prelude-capstone-reunion",
        ),
        ("skill-navigation-row-220", "skill-navigation-row-220"),
        ("prologue-preview-row-220", "prologue-preview-row-200"),
        ("row-220-closing-stitch", "row-200-closing-stitch"),
        ("row-220-closing-loop", "row-200-closing-loop"),
        ("Row 220 three-way audit", "Row 220 three-way audit"),
        (
            "[row 219](preface.md#skill-navigation-row-219) or [row 200](skill-navigation-row-220)",
            "[row 219](preface.md#skill-navigation-row-199) or [row 200](skill-navigation-row-220)",
        ),
        (
            "[row 219](preface.md#skill-navigation-row-179) or [Row 68 → Row 200 Handshake 3 meta prelude capstone reunion index (row 200)](appendix/sources.md#row 220_EXP_INDEX)",
            "[row 219](preface.md#skill-navigation-row-199) or [Row 68 → Row 200 Handshake 3 meta prelude capstone reunion index (row 220)](appendix/sources.md#row68-row200-handshake3-meta-prelude-capstone-reunion-index-row-220)",
        ),
        (
            "verified Handshake 3 meta prelude capstone closure (row 219)",
            "verified Handshake 3 meta prelude capstone closure (row 219)",
        ),
        (
            "before row 221 Handshake 4a meta prelude capstone opens on the full capstone path",
            "before row 221 Handshake 4a meta prelude capstone opens on the full capstone path",
        ),
        (
            "before row 221 Handshake 4a meta prelude capstone reunion on the full capstone path",
            "before row 221 Handshake 4a meta prelude capstone reunion on the full capstone path",
        ),
        (
            "before row 201 Handshake 4a meta prelude capstone opens on the full capstone path",
            "before row 221 Handshake 4a meta prelude capstone opens on the full capstone path",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "row68-row200-handshake3-meta-prelude-capstone-reunion-index-row-220",
        "row68-row200-handshake3-meta-prelude-capstone-reunion-index-row-220",
    )
    out = out.replace("skill-navigation-row-220", "skill-navigation-row-220")
    out = out.replace("Row 68 → Row 200 Row 68 → Row 60", "Row 68 → Row 200 Row 68 → Row 60")
    out = out.replace("row 200", "row 220")
    out = out.replace("Row 200", "Row 200")
    out = out.replace("Row 68 → Row 200 Row 68 → Row 60", "Row 68 → Row 200 Row 68 → Row 60")
    out = out.replace("skill-navigation-row-220", "skill-navigation-row-200")
    out = out.replace("[row 220](preface.md#skill-navigation-row-199)", "[row 219](preface.md#skill-navigation-row-199)")
    out = out.replace("[row 220](preface.md#skill-navigation-row-200)", "[row 220](preface.md#skill-navigation-row-200)")
    out = out.replace("[row 220](preface.md#skill-navigation-row-220)", "[row 200](preface.md#skill-navigation-row-220)")
    out = out.replace("[row 200](preface.md#skill-navigation-row-200)", "[row 200](preface.md#skill-navigation-row-220)")
    out = out.replace("when row 219 closed but row 60", "when row 219 closed but row 60")
    out = out.replace("[preface row 200](../preface.md#skill-navigation-row-200)", "[preface row 200](../preface.md#skill-navigation-row-220)")
    out = out.replace("row 220 or row 220", "row 219 or row 200")
    out = out.replace("When row 220 closed", "When row 219 closed")
    out = out.replace("after row 220 alone", "after row 219 alone")
    out = out.replace("Recite [preface row 220]", "Recite [preface row 219]")
    out = out.replace("row 220 or row 200 recited", "row 219 or row 200 recited")
    out = out.replace("When row 219 closed — Handshake", "When row 219 closed — Handshake")
    out = out.replace("row 218 or row 199 recited", "row 198 or row 219 recited")
    out = out.replace("row 219 or row 200 recited", "row 219 or row 200 recited")
    out = out.replace("when row 219 closed Handshake", "when row 219 closed Handshake")
    out = out.replace("after row 219 alone", "after row 219 alone")
    out = out.replace("from row 220's", "from row 219's")
    out = out.replace("row 219's foundation", "row 219's foundation")
    out = out.replace("row 219's quasiharmonic", "row 219's quasiharmonic")
    out = out.replace("row 219 and row 60", "row 219 and row 60")
    out = out.replace("Recite [preface row 219]", "Recite [preface row 219]")
    out = out.replace("row 180", "row 200")
    out = out.replace("Row 180", "Row 200")
    out = out.replace("row 160", "row 180")
    out = out.replace("Row 160", "Row 180")
    out = out.replace("row 140", "row 160")
    out = out.replace("Row 140", "Row 160")
    out = out.replace(
        "row68-row180-handshake3-meta-prelude-capstone-reunion-index-row-200",
        "row 220_EXP_INDEX",
    )
    out = out.replace(
        "row 220_EXP_INDEX",
        "row68-row200-handshake3-meta-prelude-capstone-reunion-index-row-220",
    )
    out = out.replace(
        "[row 219](preface.md#skill-navigation-row-179) or [row 200]",
        "[row 219](preface.md#skill-navigation-row-199) or [row 200]",
    )
    out = out.replace("row 219", "row 219")
    out = out.replace("Row 219", "Row 199")
    out = out.replace("[row 219](preface.md#skill-navigation-row-199)", "[row 219](preface.md#skill-navigation-row-199)")
    out = out.replace("[row 219](preface.md#skill-navigation-row-220)", "[row 200](preface.md#skill-navigation-row-220)")
    out = out.replace(
        "Row 68 → Row 200 Handshake 3 meta prelude capstone reunion index",
        "Row 68 → Row 200 Handshake 3 meta prelude capstone reunion index",
    )
    out = out.replace(
        "[row 200](preface.md#skill-navigation-row-160)",
        "[row 200](preface.md#skill-navigation-row-220)",
    )
    out = out.replace("TEMP_ROW201", "row 221")
    out = out.replace("TEMP_ROW200", "row 220")
    out = out.replace("TEMP_ROW199", "row 219")
    return out


def _load_add200():
    spec = importlib.util.spec_from_file_location("add200", ROOT / "scripts/add-row-200.py")
    add200 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add200)
    return add200


def _build_blocks() -> dict[str, str]:
    add200 = _load_add200()
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 200 skill checkpoint")
    end = preface.index("\n\n### Row 201 skill checkpoint", start)
    row220_preface = bump200_to_220(preface[start:end]) + "\n\n"

    row200_stitch = next(
        line
        for line in (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text().splitlines()
        if line.startswith("**Row 200 closing stitch")
    )
    prologue_stitch = bump200_to_220(
        row200_stitch.replace("{#row-200-closing-stitch}", "{#row-220-closing-stitch}").replace(
            "**Row 200 closing stitch (Row 68 → Row 180",
            "**Row 220 closing stitch (Row 68 → Row 200",
        )
    ) + "\n\n"

    b200 = add200._build_blocks()
    prologue_compass = bump200_to_220(b200["prologue_compass"])
    prologue_preview = bump200_to_220(b200["prologue_preview"])

    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    row200_loop_anchor = (
        "### Row 200 closing loop (Row 68 → Row 180 Row 68 → Row 60 "
        "Handshake 3 meta prelude capstone reunion) {#row-200-closing-loop}"
    )
    row201_loop_end = (
        "### Row 201 closing loop (Row 68 → Row 181 Row 68 → Row 61 "
        "Handshake 4a meta prelude capstone reunion) {#row-201-closing-loop}"
    )
    epilogue_loop = bump200_to_220(
        row200_loop_anchor + epilogue.split(row200_loop_anchor, 1)[1].split(row201_loop_end, 1)[0]
    )
    epilogue_loop = epilogue_loop.replace("{#row-200-closing-loop}", "{#row-220-closing-loop}", 1)

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src200_header = (
        "## Row 68 → Row 180 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 200)"
    )
    next201_header = (
        "## Row 68 → Row 181 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 201)"
    )
    sources_index = bump200_to_220(sources.split(src200_header, 1)[1].split(next201_header, 1)[0])
    sources_index = (
        "## Row 68 → Row 200 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 220) "
        "{#row68-row200-handshake3-meta-prelude-capstone-reunion-index-row-220}"
        + sources_index
    )

    sources_table = bump200_to_220(b200["sources_table"])
    sources_table = sources_table.replace("| 200 | Row 68 → Row 180", "| 220 | Row 68 → Row 200", 1)

    memory_table = bump200_to_220(b200["memory_table"])
    memory_table = memory_table.replace("| 200 | Meta |", "| 220 | Meta |", 1)

    memory_baby = bump200_to_220(b200["memory_baby"])
    if "{#row-220-baby-picture-row68-row200" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 220 baby picture (Row 68 → Row 200 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion)",
            "### Row 220 baby picture {#row-220-baby-picture-row68-row200-handshake3-meta-prelude-capstone-reunion} (Row 68 → Row 200 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion)",
            1,
        )

    return {
        "row220_preface": row220_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW219_TAIL_MARKER = (
    "When row 219 is complete, proceed to [row 200](preface.md#skill-navigation-row-220)"
)

ROW219_EPILOGUE_OLD = (
    "Proceed to [row 219](#row-219-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 218 on the full capstone path,"
)
ROW219_EPILOGUE_NEW = (
    "Proceed to [row 220](#row-220-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 219 on the full capstone path,"
)

ROW219_STITCH_OLD = (
    "before row 200 Handshake 3 meta prelude capstone opens on the full capstone path."
)
ROW219_STITCH_NEW = (
    "before row 221 Handshake 4a meta prelude capstone reunion opens on the full capstone path."
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 220 skill checkpoint" in preface:
        print("preface: row 220 already present")
    else:
        if "### Row 219 skill checkpoint" not in preface:
            raise SystemExit("row 219 must exist before row 220")
        if ROW219_TAIL_MARKER not in preface:
            raise SystemExit("row 219 tail proceed marker not found")
        preface = preface.replace(
            ROW219_TAIL_MARKER,
            "When row 219 is complete, proceed to [row 220](preface.md#skill-navigation-row-220)",
            1,
        )
        preface = preface.replace(copper, "\n" + b["row220_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 220")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-220" not in prologue:
        needle = "| Row 68 → Row 180 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion (row 200) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 200 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 220 closing stitch" not in prologue:
            prologue = prologue.replace(
                "**Row 200 closing stitch",
                b["prologue_stitch"] + "**Row 200 closing stitch",
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-200"></span>Row 200 preview'
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW219_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW219_STITCH_OLD, ROW219_STITCH_NEW, 1)
        prologue_path.write_text(prologue)
        print("prologue: added row 220")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "{#row-220-closing-loop}" not in epilogue:
        if ROW219_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW219_EPILOGUE_OLD, ROW219_EPILOGUE_NEW, 1)
        marker = (
            "### Row 200 closing loop (Row 68 → Row 180 Row 68 → Row 60 "
            "Handshake 3 meta prelude capstone reunion) {#row-200-closing-loop}"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 200 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 220")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row200-handshake3-meta-prelude-capstone-reunion-index-row-220" not in sources:
        sources = sources.replace(
            "| 200 | Row 68 → Row 180 Row 68 → Row 60 Handshake 3 meta prelude capstone",
            b["sources_table"] + "| 200 | Row 68 → Row 180 Row 68 → Row 60 Handshake 3 meta prelude capstone",
            1,
        )
        src200_header = (
            "## Row 68 → Row 180 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 200)"
        )
        sources = sources.replace(src200_header, b["sources_index"] + src200_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 220")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-220-baby-picture-row68-row200" not in memory:
        memory = memory.replace(
            "| 200 | Meta | [Row 68 → Row 180 Handshake 3 meta prelude capstone reunion index]",
            b["memory_table"] + "| 200 | Meta | [Row 68 → Row 180 Handshake 3 meta prelude capstone reunion index]",
            1,
        )
        baby_anchor = (
            "### Row 200 baby picture (Row 68 → Row 180 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion)"
        )
        if baby_anchor not in memory:
            raise SystemExit("memory baby picture anchor not found")
        memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
        memory_path.write_text(memory)
        print("memory-sheet: added row 220")


if __name__ == "__main__":
    main()
