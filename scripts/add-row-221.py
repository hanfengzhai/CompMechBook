#!/usr/bin/env python3
"""Add row 221 meta-stitch (Row 68 → Row 201 ↔ Row 61 Handshake 4a meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]

def t201_to_221(text: str) -> str:
    """Transform row-181 capstone-path meta copy to row 201 (181→201, 161→181 inner, 200 gate)."""
    out = text.replace("row 202", "row 222")
    out = out.replace("row 201", "row 221")
    out = out.replace("row 200", "row 220")
    repl = [
        ("Row 68 → Row 201 Row 68 → Row 61", "Row 68 → Row 201 Row 68 → Row 61"),
        (
            "row68-row201-handshake4a-meta-prelude-capstone-reunion-index-row-221",
            "row68-row201-handshake4a-meta-prelude-capstone-reunion-index-row-221",
        ),
        (
            "row-221-baby-picture-row68-row201-handshake4a-meta-prelude-capstone-reunion",
            "row-201-baby-picture-row68-row181-handshake4a-meta-prelude-capstone-reunion",
        ),
        ("skill-navigation-row-221", "skill-navigation-row-221"),
        ("prologue-preview-row-221", "prologue-preview-row-201"),
        ("row-221-closing-stitch", "row-201-closing-stitch"),
        ("row-221-closing-loop", "row-201-closing-loop"),
        ("Row 221 three-way audit", "Row 201 three-way audit"),
        (
            "[row 220](preface.md#skill-navigation-row-180) or [row 181](skill-navigation-row-221)",
            "[row 200](preface.md#skill-navigation-row-200) or [row 221](skill-navigation-row-221)",
        ),
        (
            "[row 220](preface.md#skill-navigation-row-180) or [Row 68 → Row 181 Handshake 4a meta prelude capstone reunion index (row 221)](appendix/sources.md#row68-row201-handshake4a-meta-prelude-capstone-reunion-index-row-221)",
            "[row 200](preface.md#skill-navigation-row-200) or [Row 68 → Row 201 Handshake 4a meta prelude capstone reunion index (row 201)](appendix/sources.md#row68-row201-handshake4a-meta-prelude-capstone-reunion-index-row-221)",
        ),
        (
            "verified Handshake 4a meta prelude capstone closure (row 220)",
            "verified Handshake 4a meta prelude capstone closure (row 200)",
        ),
        (
            "before row 202 Handshake 4b meta prelude capstone opens on the full capstone path",
            "before row 202 Handshake 4b meta prelude capstone opens on the full capstone path",
        ),
        (
            "before row 202 Handshake 4b meta prelude capstone reunion on the full capstone path",
            "before row 202 Handshake 4b meta prelude capstone reunion on the full capstone path",
        ),
        (
            "before row 182 Handshake 4b meta prelude capstone opens on the full capstone path",
            "before row 202 Handshake 4b meta prelude capstone opens on the full capstone path",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "row68-row201-handshake4a-meta-prelude-capstone-reunion-index-row-221",
        "row68-row201-handshake4a-meta-prelude-capstone-reunion-index-row-221",
    )
    out = out.replace("skill-navigation-row-221", "skill-navigation-row-221")
    out = out.replace("Row 68 → Row 201 Row 68 → Row 61", "Row 68 → Row 201 Row 68 → Row 61")
    out = out.replace("row 221", "row 201")
    out = out.replace("Row 221", "Row 201")
    out = out.replace("Row 68 → Row 201 Row 68 → Row 61", "Row 68 → Row 201 Row 68 → Row 61")
    out = out.replace("skill-navigation-row-221", "skill-navigation-row-201")
    out = out.replace("[row 201](preface.md#skill-navigation-row-200)", "[row 200](preface.md#skill-navigation-row-200)")
    out = out.replace("[row 201](preface.md#skill-navigation-row-201)", "[row 201](preface.md#skill-navigation-row-201)")
    out = out.replace("[row 201](preface.md#skill-navigation-row-221)", "[row 221](preface.md#skill-navigation-row-221)")
    out = out.replace("[row 221](preface.md#skill-navigation-row-201)", "[row 221](preface.md#skill-navigation-row-221)")
    out = out.replace("when row 220 closed but row 61", "when row 200 closed but row 61")
    out = out.replace("[preface row 221](../preface.md#skill-navigation-row-201)", "[preface row 221](../preface.md#skill-navigation-row-221)")
    out = out.replace("row 201 or row 201", "row 200 or row 221")
    out = out.replace("When row 220 closed", "When row 200 closed")
    out = out.replace("after row 220 alone", "after row 200 alone")
    out = out.replace("Recite [preface row 220]", "Recite [preface row 200]")
    out = out.replace("row 201 or row 221 recited", "row 200 or row 221 recited")
    out = out.replace("When row 220 closed — Handshake 4a", "When row 200 closed — Handshake 4a")
    out = out.replace("row 220 or row 201 recited", "row 200 or row 221 recited")
    out = out.replace("row 220 or row 201 recited", "row 200 or row 221 recited")
    out = out.replace("when row 220 closed Handshake 4a", "when row 200 closed Handshake 4a")
    out = out.replace("after row 220 alone", "after row 200 alone")
    out = out.replace("from row 220's", "from row 200's")
    out = out.replace("row 220's epilogue rate", "row 200's epilogue rate")
    out = out.replace("row 220 and row 61", "row 200 and row 61")
    out = out.replace("Recite [preface row 220]", "Recite [preface row 200]")
    out = out.replace("row 181", "row 221")
    out = out.replace("Row 181", "Row 221")
    out = out.replace("row 161", "row 181")
    out = out.replace("Row 161", "Row 181")
    out = out.replace("row 141", "row 161")
    out = out.replace("Row 141", "Row 161")
    out = out.replace(
        "row68-row201-handshake4a-meta-prelude-capstone-reunion-index-row-221",
        "row68-row201-handshake4a-meta-prelude-capstone-reunion-index-row-221",
    )
    out = out.replace(
        "row68-row201-handshake4a-meta-prelude-capstone-reunion-index-row-221",
        "row68-row201-handshake4a-meta-prelude-capstone-reunion-index-row-221",
    )
    out = out.replace(
        "row68-row201-handshake4a-meta-prelude-capstone-reunion-index-row-221",
        "row68-row201-handshake4a-meta-prelude-capstone-reunion-index-row-221",
    )
    out = out.replace(
        "[row 220](preface.md#skill-navigation-row-180) or [row 221]",
        "[row 200](preface.md#skill-navigation-row-200) or [row 221]",
    )
    out = out.replace("row 220", "row 200")
    out = out.replace("Row 220", "Row 200")
    out = out.replace("[row 200](preface.md#skill-navigation-row-200)", "[row 200](preface.md#skill-navigation-row-200)")
    out = out.replace("[row 200](preface.md#skill-navigation-row-221)", "[row 221](preface.md#skill-navigation-row-221)")
    out = out.replace(
        "Row 68 → Row 201 Handshake 4a meta prelude capstone reunion index",
        "Row 68 → Row 201 Handshake 4a meta prelude capstone reunion index",
    )
    out = out.replace(
        "[row 221](preface.md#skill-navigation-row-161)",
        "[row 221](preface.md#skill-navigation-row-221)",
    )
    out = out.replace("row 222", "row 202")
    out = out.replace("row 221", "row 201")
    out = out.replace("row 220", "row 200")
    return out
    return out


def _load_add201():
    spec = importlib.util.spec_from_file_location("add201", ROOT / "scripts/add-row-201.py")
    add201 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add201)
    return add201


def _build_blocks() -> dict[str, str]:
    add201 = _load_add201()
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 201 skill checkpoint")
    end = preface.index("\n\n### Row 202 skill checkpoint", start)
    row221_preface = t201_to_221(preface[start:end]) + "\n\n"

    row201_stitch = next(
        line
        for line in (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text().splitlines()
        if line.startswith("**Row 201 closing stitch")
    )
    prologue_stitch = t201_to_221(
        row201_stitch.replace("{#row-201-closing-stitch}", "{#row-221-closing-stitch}").replace(
            "**Row 201 closing stitch (Row 68 → Row 181",
            "**Row 221 closing stitch (Row 68 → Row 201",
        )
    ) + "\n\n"

    b201 = add201._build_blocks()
    prologue_compass = t201_to_221(b201["prologue_compass"])
    prologue_preview = t201_to_221(b201["prologue_preview"])

    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    row201_loop_anchor = (
        "### Row 201 closing loop (Row 68 → Row 181 Row 68 → Row 61 "
        "Handshake 4a meta prelude capstone reunion) {#row-201-closing-loop}"
    )
    row202_loop_end = (
        "### Row 202 closing loop (Row 68 → Row 182 Row 68 → Row 62 "
        "Handshake 4b meta prelude capstone reunion) {#row-202-closing-loop}"
    )
    epilogue_loop = t201_to_221(
        row201_loop_anchor + epilogue.split(row201_loop_anchor, 1)[1].split(row202_loop_end, 1)[0]
    )
    epilogue_loop = epilogue_loop.replace("{#row-201-closing-loop}", "{#row-221-closing-loop}", 1)

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src201_header = (
        "## Row 68 → Row 181 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 201)"
    )
    next202_header = (
        "## Row 68 → Row 182 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion index (row 202)"
    )
    sources_index = t201_to_221(sources.split(src201_header, 1)[1].split(next202_header, 1)[0])
    sources_index = (
        "## Row 68 → Row 201 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 221) "
        "{#row68-row201-handshake4a-meta-prelude-capstone-reunion-index-row-221}"
        + sources_index
    )

    sources_table = t201_to_221(b201["sources_table"])
    sources_table = sources_table.replace("| 201 | Row 68 → Row 181", "| 221 | Row 68 → Row 201", 1)

    memory_table = t201_to_221(b201["memory_table"])
    memory_table = memory_table.replace("| 201 | Meta |", "| 221 | Meta |", 1)

    memory_baby = t201_to_221(b201["memory_baby"])
    if "{#row-221-baby-picture-row68-row201" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 221 baby picture (Row 68 → Row 201 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion)",
            "### Row 221 baby picture {#row-221-baby-picture-row68-row201-handshake4a-meta-prelude-capstone-reunion} (Row 68 → Row 201 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion)",
            1,
        )

    return {
        "row221_preface": row221_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW220_TAIL_MARKER = (
    "When row 220 is complete, proceed to [row 221](preface.md#skill-navigation-row-221)"
)

ROW220_EPILOGUE_OLD = (
    "Proceed to [row 201](#row-201-closing-loop) when row 68 closed but Handshake 4a meta still feels disconnected after row 200 on the full capstone path,"
)
ROW220_EPILOGUE_NEW = (
    "Proceed to [row 221](#row-221-closing-loop) when row 68 closed but Handshake 4a meta still feels disconnected after row 220 on the full capstone path,"
)

ROW220_EPILOGUE_BEFORE_OLD = (
    "before row 201 Handshake 4a meta prelude capstone reunion on the full capstone path (then row 181 Handshake 4a on the full capstone path)."
)
ROW220_EPILOGUE_BEFORE_NEW = (
    "before row 222 Handshake 4b meta prelude capstone reunion on the full capstone path (then row 202 Handshake 4b on the full capstone path)."
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 221 skill checkpoint" in preface:
        print("preface: row 221 already present")
    else:
        if ROW220_TAIL_MARKER not in preface:
            # also accept row 220 tail from row 200 section if not yet updated
            alt = "When row 200 is complete, proceed to [row 201](preface.md#skill-navigation-row-201)"
            if alt in preface:
                preface = preface.replace(alt, "When row 200 is complete, proceed to [row 201](preface.md#skill-navigation-row-201)", 1)
            if ROW220_TAIL_MARKER not in preface:
                raise SystemExit("row 220 tail proceed marker not found")
        preface = preface.replace(
            ROW220_TAIL_MARKER,
            "When row 220 is complete, proceed to [row 221](preface.md#skill-navigation-row-221)",
            1,
        )
        preface = preface.replace(copper, "\n" + b["row221_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 221")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-221" not in prologue:
        needle = "| Row 68 → Row 181 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion (row 201) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 201 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 221 closing stitch" not in prologue:
            prologue = prologue.replace(
                "**Row 201 closing stitch",
                b["prologue_stitch"] + "**Row 201 closing stitch",
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-201"></span>Row 201 preview'
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        prologue_path.write_text(prologue)
        print("prologue: added row 221")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "{#row-221-closing-loop}" not in epilogue:
        if ROW220_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW220_EPILOGUE_OLD, ROW220_EPILOGUE_NEW, 1)
        if ROW220_EPILOGUE_BEFORE_OLD in epilogue:
            epilogue = epilogue.replace(ROW220_EPILOGUE_BEFORE_OLD, ROW220_EPILOGUE_BEFORE_NEW, 1)
        marker = (
            "### Row 186 closing loop (Row 68 → Row 166 Row 68 → Row 66 Writings canonical meta prelude capstone reunion)"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 186 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 221")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row201-handshake4a-meta-prelude-capstone-reunion-index-row-221" not in sources:
        sources = sources.replace(
            "| 201 | Row 68 → Row 181 Row 68 → Row 61 Handshake 4a meta prelude capstone",
            b["sources_table"] + "| 201 | Row 68 → Row 181 Row 68 → Row 61 Handshake 4a meta prelude capstone",
            1,
        )
        src201_header = (
            "## Row 68 → Row 181 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 201)"
        )
        sources = sources.replace(src201_header, b["sources_index"] + src201_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 221")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-221-baby-picture-row68-row201" not in memory:
        memory = memory.replace(
            "| 201 | Meta | [Row 68 → Row 181 Handshake 4a meta prelude capstone reunion index]",
            b["memory_table"] + "| 201 | Meta | [Row 68 → Row 181 Handshake 4a meta prelude capstone reunion index]",
            1,
        )
        baby_anchor = (
            "### Row 201 baby picture (Row 68 → Row 181 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion)"
        )
        if baby_anchor not in memory:
            raise SystemExit("memory baby picture anchor not found")
        memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
        memory_path.write_text(memory)
        print("memory-sheet: added row 221")


if __name__ == "__main__":
    main()
