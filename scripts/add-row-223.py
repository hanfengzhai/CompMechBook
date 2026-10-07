#!/usr/bin/env python3
"""Add row 223 meta-stitch (Row 68 → Row 203 ↔ Row 63 orchestration meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]


def lift203_to_223(text: str) -> str:
    """Lift row-203 capstone meta copy to row 223 (+20: 183→203 index, 203→223 checkpoint)."""
    out = text.replace("row 224", "__R224__")
    out = out.replace("row 223", "__R223__")
    out = out.replace("row 204", "__R204__")
    out = out.replace("row 203", "__R203__")
    repl = [
        ("Row 68 → Row 183 Row 68 → Row 63", "Row 68 → Row 203 Row 68 → Row 63"),
        (
            "row68-row183-orchestration-meta-prelude-capstone-reunion-index-row-203",
            "row68-row203-orchestration-meta-prelude-capstone-reunion-index-row-223",
        ),
        (
            "row-203-baby-picture-row68-row183-orchestration-meta-prelude-capstone-reunion",
            "row-223-baby-picture-row68-row203-orchestration-meta-prelude-capstone-reunion",
        ),
        ("prologue-preview-row-203", "prologue-preview-row-223"),
        ("row-203-closing-stitch", "row-223-closing-stitch"),
        ("row-203-closing-loop", "row-223-closing-loop"),
        ("Row 203 three-way audit", "Row 223 three-way audit"),
        (
            "verified Handshake 4b meta prelude capstone closure (row 202)",
            "verified Handshake 4b meta prelude capstone closure (row 222)",
        ),
        (
            "before row 204 book-loop meta prelude capstone opens on the full capstone path",
            "before row 224 book-loop meta prelude capstone opens on the full capstone path",
        ),
        (
            "before row 204 book-loop meta prelude capstone reunion on the full capstone path",
            "before row 224 book-loop meta prelude capstone reunion on the full capstone path",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace("skill-navigation-row-203", "skill-navigation-row-223")
    out = out.replace(
        "[row 202](preface.md#skill-navigation-row-202) or [row 183](preface.md#skill-navigation-row-163)",
        "[row 222](preface.md#skill-navigation-row-222) or [row 203](preface.md#skill-navigation-row-203)",
    )
    out = out.replace("row 183](preface.md#skill-navigation-row-163)", "row 203](preface.md#skill-navigation-row-203)")
    out = out.replace("row 183's epilogue orchestration", "row 203's epilogue orchestration")
    out = out.replace("| 203 |", "| 223 |")
    out = out.replace("memory sheet row 203", "memory sheet row 223")
    out = out.replace("prologue row 203", "prologue row 223")
    out = out.replace("epilogue row 203", "epilogue row 223")
    out = out.replace("When row 203 is complete", "When row 223 is complete")
    out = out.replace("row 202 closed but row 63", "row 222 closed but row 63")
    out = out.replace("when row 202 and row 63", "when row 222 and row 63")
    out = out.replace("after row 202 on the full capstone path", "after row 222 on the full capstone path")
    out = out.replace("row 202's Handshake 4b meta", "row 222's Handshake 4b meta")
    out = out.replace("Row 203 does not replace", "Row 223 does not replace")
    out = out.replace(
        "Row 68 → Row 183 orchestration meta prelude capstone reunion index (row 203)",
        "Row 68 → Row 203 orchestration meta prelude capstone reunion index (row 223)",
    )
    out = out.replace("__R203__", "row 223")
    out = out.replace("__R204__", "row 224")
    out = out.replace("__R223__", "row 223")
    out = out.replace("__R224__", "row 224")
    return out


def _load_add203():
    spec = importlib.util.spec_from_file_location("add203", ROOT / "scripts/add-row-203.py")
    add203 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add203)
    return add203


def _build_blocks() -> dict[str, str]:
    add203 = _load_add203()
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 203 skill checkpoint")
    end = preface.index("\n\n### Row 204 skill checkpoint", start)
    row223_preface = lift203_to_223(preface[start:end]) + "\n\n"
    row223_preface = row223_preface.replace(
        "### Row 203 skill checkpoint",
        "### Row 223 skill checkpoint",
        1,
    ).replace("{#skill-navigation-row-203}", "{#skill-navigation-row-223}", 1)

    b203 = add203._build_blocks()
    prologue_stitch = lift203_to_223(
        b203["prologue_stitch"].replace("{#row-203-closing-stitch}", "{#row-223-closing-stitch}").replace(
            "**Row 203 closing stitch (Row 68 → Row 183",
            "**Row 223 closing stitch (Row 68 → Row 203",
        )
    )
    prologue_compass = lift203_to_223(b203["prologue_compass"])
    prologue_preview = lift203_to_223(b203["prologue_preview"])

    epilogue_loop = lift203_to_223(b203["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace("{#row-203-closing-loop}", "{#row-223-closing-loop}", 1)

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src203_header = (
        "## Row 68 → Row 183 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 203)"
    )
    next204_header = (
        "## Row 68 → Row 164 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 204)"
    )
    sources_index = lift203_to_223(sources.split(src203_header, 1)[1].split(next204_header, 1)[0])
    sources_index = (
        "## Row 68 → Row 203 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 223) "
        "{#row68-row203-orchestration-meta-prelude-capstone-reunion-index-row-223}"
        + sources_index
    )

    sources_table = lift203_to_223(b203["sources_table"])
    sources_table = sources_table.replace("| 203 | Row 68 → Row 183", "| 223 | Row 68 → Row 203", 1)

    memory_table = lift203_to_223(b203["memory_table"])
    memory_table = memory_table.replace("| 203 | Meta |", "| 223 | Meta |", 1)

    memory_baby = lift203_to_223(b203["memory_baby"])
    if "{#row-223-baby-picture-row68-row203" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 203 baby picture (Row 68 → Row 183 Row 68 → Row 63 orchestration meta prelude capstone reunion)",
            "### Row 223 baby picture {#row-223-baby-picture-row68-row203-orchestration-meta-prelude-capstone-reunion} (Row 68 → Row 203 Row 68 → Row 63 orchestration meta prelude capstone reunion)",
            1,
        )

    return {
        "row223_preface": row223_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW222_TAIL_MARKER = (
    "When row 222 is complete, proceed to [row 223](preface.md#skill-navigation-row-223)"
)

ROW222_TAIL_ALT = (
    "When row 222 is complete, proceed to [row 203](preface.md#skill-navigation-row-203)"
)

ROW222_EPILOGUE_OLD = (
    "Proceed to [row 203](#row-203-closing-loop) when row 68 closed but orchestration meta still feels disconnected after row 202 on the full capstone path,"
)
ROW222_EPILOGUE_NEW = (
    "Proceed to [row 223](#row-223-closing-loop) when row 68 closed but orchestration meta still feels disconnected after row 222 on the full capstone path,"
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 223 skill checkpoint" in preface:
        print("preface: row 223 already present")
    else:
        if "### Row 222 skill checkpoint" not in preface:
            raise SystemExit("row 222 must exist before row 223")
        # Update row 222 tail if present; else row 203 tail from base path
        if ROW222_TAIL_ALT in preface:
            preface = preface.replace(
                ROW222_TAIL_ALT,
                ROW222_TAIL_MARKER,
                1,
            )
        preface = preface.replace(copper, "\n" + b["row223_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 223")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-223" not in prologue:
        needle = "| Row 68 → Row 183 Row 68 → Row 63 orchestration meta prelude capstone reunion (row 203) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 203 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 223 closing stitch" not in prologue:
            prologue = prologue.replace(
                "**Row 203 closing stitch",
                b["prologue_stitch"] + "**Row 203 closing stitch",
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-203"></span>Row 203 preview'
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        prologue_path.write_text(prologue)
        print("prologue: added row 223")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "{#row-223-closing-loop}" not in epilogue:
        if ROW222_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW222_EPILOGUE_OLD, ROW222_EPILOGUE_NEW, 1)
        marker = (
            "### Row 186 closing loop (Row 68 → Row 166 Row 68 → Row 66 Writings canonical meta prelude capstone reunion)"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 186 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 223")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row203-orchestration-meta-prelude-capstone-reunion-index-row-223" not in sources:
        sources = sources.replace(
            "| 203 | Row 68 → Row 183 Row 68 → Row 63 orchestration meta prelude capstone",
            b["sources_table"] + "| 203 | Row 68 → Row 183 Row 68 → Row 63 orchestration meta prelude capstone",
            1,
        )
        src203_header = (
            "## Row 68 → Row 183 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 203)"
        )
        sources = sources.replace(src203_header, b["sources_index"] + src203_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 223")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-223-baby-picture-row68-row203" not in memory:
        memory = memory.replace(
            "| 203 | Meta | [Row 68 → Row 183 orchestration meta prelude capstone reunion index]",
            b["memory_table"] + "| 203 | Meta | [Row 68 → Row 183 orchestration meta prelude capstone reunion index]",
            1,
        )
        baby_anchor = (
            "### Row 203 baby picture (Row 68 → Row 183 Row 68 → Row 63 orchestration meta prelude capstone reunion)"
        )
        if baby_anchor not in memory:
            raise SystemExit("memory baby picture anchor not found")
        memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
        memory_path.write_text(memory)
        print("memory-sheet: added row 223")


if __name__ == "__main__":
    main()
