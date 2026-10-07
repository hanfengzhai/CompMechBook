#!/usr/bin/env python3
"""Add row 224 meta-stitch (Row 68 → Row 204 ↔ Row 64 book-loop meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]


def lift204_to_224(text: str) -> str:
    """Lift row-204 capstone meta copy to row 224 (+20: 184→204 index, 204→224 checkpoint)."""
    out = text.replace("row 225", "__R225__")
    out = out.replace("row 224", "__R224__")
    out = out.replace("row 223", "__R223__")
    out = out.replace("row 204", "__R204__")
    repl = [
        ("Row 68 → Row 184 Row 68 → Row 64", "Row 68 → Row 204 Row 68 → Row 64"),
        (
            "row68-row184-book-loop-meta-prelude-capstone-reunion-index-row-204",
            "row68-row204-book-loop-meta-prelude-capstone-reunion-index-row-224",
        ),
        (
            "row-204-baby-picture-row68-row184-book-loop-meta-prelude-capstone-reunion",
            "row-224-baby-picture-row68-row204-book-loop-meta-prelude-capstone-reunion",
        ),
        ("prologue-preview-row-204", "prologue-preview-row-224"),
        ("row-204-closing-stitch", "row-224-closing-stitch"),
        ("row-204-closing-loop", "row-224-closing-loop"),
        ("Row 204 three-way audit", "Row 224 three-way audit"),
        (
            "verified orchestration meta prelude capstone closure (row 203)",
            "verified orchestration meta prelude capstone closure (row 223)",
        ),
        (
            "before row 205 second-pass meta prelude capstone opens on the full capstone path",
            "before row 225 second-pass meta prelude capstone opens on the full capstone path",
        ),
        (
            "before row 205 second-pass meta prelude capstone reunion on the full capstone path",
            "before row 225 second-pass meta prelude capstone reunion on the full capstone path",
        ),
        (
            "Row 68 → Row 184 book-loop meta prelude capstone reunion index (row 204)",
            "Row 68 → Row 204 book-loop meta prelude capstone reunion index (row 224)",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace("skill-navigation-row-204", "skill-navigation-row-224")
    out = out.replace(
        "[row 203](preface.md#skill-navigation-row-203) or [row 183](preface.md#skill-navigation-row-183)",
        "[row 223](preface.md#skill-navigation-row-223) or [row 203](preface.md#skill-navigation-row-203)",
    )
    out = out.replace("row 183](preface.md#skill-navigation-row-183)", "row 203](preface.md#skill-navigation-row-203)")
    out = out.replace("row 164's epilogue book-loop", "row 204's epilogue book-loop")
    out = out.replace("| 204 |", "| 224 |")
    out = out.replace("memory sheet row 204", "memory sheet row 224")
    out = out.replace("prologue row 204", "prologue row 224")
    out = out.replace("epilogue row 204", "epilogue row 224")
    out = out.replace("When row 204 is complete", "When row 224 is complete")
    out = out.replace("when row 203 closed but row 64", "when row 223 closed but row 64")
    out = out.replace("when row 203 and row 64", "when row 223 and row 64")
    out = out.replace("after row 203 on the full capstone path", "after row 223 on the full capstone path")
    out = out.replace("after row 183 on the full capstone path", "after row 203 on the full capstone path")
    out = out.replace("row 203's orchestration meta", "row 223's orchestration meta")
    out = out.replace("Row 204 does not replace", "Row 224 does not replace")
    out = out.replace(
        "Row 68 → Row 164 book-loop meta prelude capstone reunion index (row 204)",
        "Row 68 → Row 204 book-loop meta prelude capstone reunion index (row 224)",
    )
    out = out.replace(
        "Row 68 → Row 184 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 204)",
        "Row 68 → Row 204 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 224)",
    )
    out = out.replace("__R204__", "row 224")
    out = out.replace("__R223__", "row 223")
    out = out.replace("__R224__", "row 224")
    out = out.replace("__R225__", "row 225")
    return out


def _load_add204():
    spec = importlib.util.spec_from_file_location("add204", ROOT / "scripts/add-row-204.py")
    add204 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add204)
    return add204


def _build_blocks() -> dict[str, str]:
    add204 = _load_add204()
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 204 skill checkpoint")
    end = preface.index("\n\n### Row 205 skill checkpoint", start)
    row224_preface = lift204_to_224(preface[start:end]) + "\n\n"
    row224_preface = row224_preface.replace(
        "### Row 204 skill checkpoint",
        "### Row 224 skill checkpoint",
        1,
    ).replace("{#skill-navigation-row-204}", "{#skill-navigation-row-224}", 1)

    b204 = add204._build_blocks()
    prologue_stitch = lift204_to_224(
        b204["prologue_stitch"].replace("{#row-204-closing-stitch}", "{#row-224-closing-stitch}").replace(
            "**Row 204 closing stitch (Row 68 → Row 184",
            "**Row 224 closing stitch (Row 68 → Row 204",
        )
    )
    prologue_compass = lift204_to_224(b204["prologue_compass"])
    prologue_preview = lift204_to_224(b204["prologue_preview"])

    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    ep_loop_start = (
        "### Row 204 closing loop (Row 68 → Row 184 Row 68 → Row 64 "
        "book-loop meta prelude capstone reunion) {#row-204-closing-loop}"
    )
    ep_loop_end = "\n\n### Row 183 closing loop"
    epilogue_loop = lift204_to_224(ep_loop_start + epilogue.split(ep_loop_start, 1)[1].split(ep_loop_end, 1)[0])
    epilogue_loop = epilogue_loop.replace("{#row-204-closing-loop}", "{#row-224-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 204 closing loop (Row 68 → Row 184",
        "### Row 224 closing loop (Row 68 → Row 204",
        1,
    )
    epilogue_loop = epilogue_loop.rstrip() + "\n\n"

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src204_header = (
        "## Row 68 → Row 184 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 204) "
        "{#row68-row184-book-loop-meta-prelude-capstone-reunion-index-row-204}"
    )
    next205_header = (
        "## Row 68 → Row 185 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 205)"
    )
    sources_index = lift204_to_224(sources.split(src204_header, 1)[1].split(next205_header, 1)[0])
    sources_index = (
        "## Row 68 → Row 204 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 224) "
        "{#row68-row204-book-loop-meta-prelude-capstone-reunion-index-row-224}\n"
        + sources_index.lstrip("\n")
    )

    sources_table = lift204_to_224(b204["sources_table"])
    sources_table = sources_table.replace("| 204 | Row 68 → Row 184", "| 224 | Row 68 → Row 204", 1)

    memory_table = lift204_to_224(b204["memory_table"])
    memory_table = memory_table.replace("| 204 | Meta |", "| 224 | Meta |", 1)

    memory = (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text()
    mem_baby_start = (
        "### Row 164 baby picture {#row-204-baby-picture-row68-row184-book-loop-meta-prelude-capstone-reunion}"
    )
    mem_baby_end = "\n\n### Row 183 baby picture"
    memory_baby = lift204_to_224(
        mem_baby_start + memory.split(mem_baby_start, 1)[1].split(mem_baby_end, 1)[0]
    )
    memory_baby = memory_baby.replace(
        "### Row 164 baby picture {#row-204-baby-picture-row68-row184-book-loop-meta-prelude-capstone-reunion}",
        "### Row 224 baby picture {#row-224-baby-picture-row68-row204-book-loop-meta-prelude-capstone-reunion}",
        1,
    ).rstrip() + "\n\n"

    return {
        "row224_preface": row224_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW223_TAIL_MARKER = (
    "proceed to [row 224](preface.md#skill-navigation-row-224)"
)
ROW223_TAIL_OLD = (
    "proceed to [row 224](preface.md#skill-navigation-row-204)"
)

ROW223_EPILOGUE_OLD = (
    "Proceed to [row 184](#row-184-closing-loop) when row 68 closed but book-loop meta still feels disconnected after row 223 on the full capstone path,"
)
ROW223_EPILOGUE_NEW = (
    "Proceed to [row 224](#row-224-closing-loop) when row 68 closed but book-loop meta still feels disconnected after row 223 on the full capstone path,"
)

ROW223_BABY_OLD = (
    "row 223 when **epilogue orchestration cross-links and Row 62 → Row 43 meta must read on the same wire before row 184 book-loop meta prelude capstone reunion opens on the full capstone path**"
)
ROW223_BABY_NEW = (
    "row 223 when **epilogue orchestration cross-links and Row 62 → Row 43 meta must read on the same wire before row 224 book-loop meta prelude capstone reunion opens on the full capstone path**"
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 224 skill checkpoint" in preface:
        print("preface: row 224 already present")
    else:
        if "### Row 223 skill checkpoint" not in preface:
            raise SystemExit("row 223 must exist before row 224")
        if ROW223_TAIL_OLD in preface:
            preface = preface.replace(ROW223_TAIL_OLD, ROW223_TAIL_MARKER, 1)
        preface = preface.replace(copper, "\n" + b["row224_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 224")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-224" not in prologue:
        needle = "| Row 68 → Row 203 Row 68 → Row 63 orchestration meta prelude capstone reunion (row 223) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 223 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 224 closing stitch" not in prologue:
            prologue = prologue.replace(
                "**Row 204 closing stitch",
                b["prologue_stitch"] + "**Row 204 closing stitch",
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-204"></span>Row 204 preview'
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        prologue_path.write_text(prologue)
        print("prologue: added row 224")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "{#row-224-closing-loop}" not in epilogue:
        if ROW223_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW223_EPILOGUE_OLD, ROW223_EPILOGUE_NEW, 1)
        marker = (
            "### Row 186 closing loop (Row 68 → Row 166 Row 68 → Row 66 Writings canonical meta prelude capstone reunion) {#row-186-closing-loop}"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 186 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 224")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row204-book-loop-meta-prelude-capstone-reunion-index-row-224" not in sources:
        sources = sources.replace(
            "| 204 | Row 68 → Row 184 Row 68 → Row 64 book-loop meta prelude capstone",
            b["sources_table"] + "| 204 | Row 68 → Row 184 Row 68 → Row 64 book-loop meta prelude capstone",
            1,
        )
        src204_header = (
            "## Row 68 → Row 184 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 204) "
            "{#row68-row184-book-loop-meta-prelude-capstone-reunion-index-row-204}"
        )
        sources = sources.replace(src204_header, b["sources_index"] + src204_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 224")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-224-baby-picture-row68-row204" not in memory:
        memory = memory.replace(
            "| 204 | Meta | [Row 68 → Row 164 book-loop meta prelude capstone reunion index]",
            b["memory_table"] + "| 204 | Meta | [Row 68 → Row 164 book-loop meta prelude capstone reunion index]",
            1,
        )
        baby_anchor = (
            "### Row 164 baby picture {#row-204-baby-picture-row68-row184-book-loop-meta-prelude-capstone-reunion}"
        )
        if baby_anchor not in memory:
            raise SystemExit("memory baby picture anchor not found")
        memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
        if ROW223_BABY_OLD in memory:
            memory = memory.replace(ROW223_BABY_OLD, ROW223_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 224")


if __name__ == "__main__":
    main()
