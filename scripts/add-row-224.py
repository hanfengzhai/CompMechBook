#!/usr/bin/env python3
"""Add row 224 meta-stitch (Row 68 → Row 204 ↔ Row 64 book-loop meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]


def bump204_to_224(text: str) -> str:
    """Transform row-204 capstone-path meta copy to row 224 (204→224 inner, 223 orchestration gate)."""
    out = text.replace("row 225", "TEMP_ROW225")
    out = out.replace("row 224", "TEMP_ROW224")
    out = out.replace("row 223", "TEMP_ROW223")
    out = out.replace("row 222", "TEMP_ROW222")
    repl = [
        ("Row 68 → Row 184 Row 68 → Row 64", "Row 68 → Row 204 Row 68 → Row 64"),
        (
            "row68-row184-book-loop-meta-prelude-capstone-reunion-index-row-204",
            "TEMP_ROW224_BL_INDEX",
        ),
        (
            "row-204-baby-picture-row68-row184-book-loop-meta-prelude-capstone-reunion",
            "row-224-baby-picture-row68-row204-book-loop-meta-prelude-capstone-reunion",
        ),
        ("### Row 204 skill checkpoint", "### Row 224 skill checkpoint"),
        ("skill-navigation-row-204", "skill-navigation-row-224"),
        ("prologue-preview-row-204", "prologue-preview-row-224"),
        ("row-204-closing-stitch", "row-224-closing-stitch"),
        ("row-204-closing-loop", "row-224-closing-loop"),
        ("Row 204 three-way audit", "Row 224 three-way audit"),
        (
            "[row 203](preface.md#skill-navigation-row-203) or [row 183](preface.md#skill-navigation-row-183)",
            "[row 223](preface.md#skill-navigation-row-223) or [row 203](preface.md#skill-navigation-row-203)",
        ),
        (
            "[row 203](preface.md#skill-navigation-row-203) or [Row 68 → Row 184 book-loop meta prelude capstone reunion index (row 204)](appendix/sources.md#row68-row184-book-loop-meta-prelude-capstone-reunion-index-row-204)",
            "[row 223](preface.md#skill-navigation-row-223) or [Row 68 → Row 204 book-loop meta prelude capstone reunion index (row 224)](appendix/sources.md#row68-row204-book-loop-meta-prelude-capstone-reunion-index-row-224)",
        ),
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
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW224_BL_INDEX",
        "row68-row204-book-loop-meta-prelude-capstone-reunion-index-row-224",
    )
    out = out.replace("Row 204 does not replace", "Row 224 does not replace")
    out = out.replace("When row 204 is complete", "When row 224 is complete")
    out = out.replace("When row 203 closed", "When row 223 closed")
    out = out.replace("when row 203 closed but row 64", "when row 223 closed but row 64")
    out = out.replace("after row 204 alone", "after row 224 alone")
    out = out.replace("Recite [preface row 203]", "Recite [preface row 223]")
    out = out.replace("row 204 or row 183 recited", "row 224 or row 203 recited")
    out = out.replace("row 203 or row 183 recited", "row 223 or row 203 recited")
    out = out.replace("when row 203 and row 64", "when row 223 and row 64")
    out = out.replace("after row 203 alone", "after row 223 alone")
    out = out.replace("after row 203 on the full capstone path", "after row 223 on the full capstone path")
    out = out.replace("skill-navigation-row-183", "TEMP_SKILL_183")
    out = out.replace("row 183", "row 203")
    out = out.replace("Row 183", "Row 203")
    out = out.replace("TEMP_SKILL_183", "skill-navigation-row-183")
    out = out.replace("[row 203](preface.md#skill-navigation-row-203)", "[row 203](preface.md#skill-navigation-row-203)")
    out = out.replace("[row 203](preface.md#skill-navigation-row-163)", "[row 203](preface.md#skill-navigation-row-203)")
    out = out.replace("row 163", "row 183")
    out = out.replace("Row 163", "Row 183")
    out = out.replace("row 164", "row 184")
    out = out.replace("Row 164", "Row 184")
    out = out.replace("row 144", "row 164")
    out = out.replace("Row 144", "Row 164")
    out = out.replace("row 124", "row 144")
    out = out.replace("Row 124", "Row 144")
    out = out.replace(
        "row68-row144-book-loop-meta-prelude-capstone-reunion-index-row-164",
        "row68-row164-book-loop-meta-prelude-capstone-reunion-index-row-184",
    )
    out = out.replace(
        "row68-row184-book-loop-meta-prelude-capstone-reunion-index-row-204",
        "row68-row204-book-loop-meta-prelude-capstone-reunion-index-row-224",
    )
    out = out.replace("Row 68 → Row 224 Row 68 → Row 64", "Row 68 → Row 204 Row 68 → Row 64")
    out = out.replace("memory sheet row 204 baby picture", "memory sheet row 224 baby picture")
    out = out.replace("prologue row 204 closing stitch", "prologue row 224 closing stitch")
    out = out.replace("prologue row 204 preview", "prologue row 224 preview")
    out = out.replace("epilogue row 204 closing loop", "epilogue row 224 closing loop")
    out = out.replace("opening [row 205]", "opening [row 225]")
    out = out.replace("skill-navigation-row-205", "skill-navigation-row-225")
    out = out.replace(
        "Prologue preview ([row 204](prologue/00-many-scales.md#prologue-preview-row-204))",
        "Prologue preview ([row 224](prologue/00-many-scales.md#prologue-preview-row-224))",
    )
    out = out.replace("preface row 204", "preface row 224")
    out = out.replace(
        "[row 205](preface.md#skill-navigation-row-205)",
        "[row 225](preface.md#skill-navigation-row-225)",
    )
    out = out.replace("TEMP_ROW222", "row 222")
    out = out.replace("TEMP_ROW223", "row 223")
    out = out.replace("TEMP_ROW224", "row 224")
    out = out.replace("TEMP_ROW225", "row 225")
    out = out.replace(
        "proceed to [row 205](preface.md#skill-navigation-row-205)",
        "proceed to [row 225](preface.md#skill-navigation-row-225)",
    )
    out = out.replace(
        "Row 68 → Row 164 reunion index](appendix/sources.md#row68-row184-book-loop-meta-prelude-capstone-reunion-index-row-204)",
        "Row 68 → Row 204 reunion index](appendix/sources.md#row68-row204-book-loop-meta-prelude-capstone-reunion-index-row-224)",
    )
    out = out.replace(
        "reunion index (row 204)](appendix/sources.md#row68-row184-book-loop-meta-prelude-capstone-reunion-index-row-204)",
        "reunion index (row 224)](appendix/sources.md#row68-row204-book-loop-meta-prelude-capstone-reunion-index-row-224)",
    )
    out = out.replace("row 203's orchestration meta", "row 223's orchestration meta")
    out = out.replace("row 204's book-loop meta", "row 224's book-loop meta")
    out = out.replace("after row 183 on the full capstone path", "after row 203 on the full capstone path")
    out = out.replace("skill-navigation-row-166", "TEMP_SKILL_166")
    out = out.replace("row 186", "row 206")
    out = out.replace("Row 186", "Row 206")
    out = out.replace("TEMP_SKILL_166", "skill-navigation-row-166")
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
    row224_preface = bump204_to_224(preface[start:end]) + "\n\n"

    row204_stitch = next(
        line
        for line in (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text().splitlines()
        if line.startswith("**Row 204 closing stitch (Row 68 → Row 184")
    )
    prologue_stitch = bump204_to_224(
        row204_stitch.replace("{#row-204-closing-stitch}", "{#row-224-closing-stitch}").replace(
            "**Row 204 closing stitch (Row 68 → Row 184 Row 68 → Row 64 book-loop meta prelude capstone reunion).",
            "**Row 224 closing stitch (Row 68 → Row 204 Row 68 → Row 64 book-loop meta prelude capstone reunion).",
        )
    ) + "\n\n"

    b204 = add204._build_blocks()
    prologue_compass = bump204_to_224(b204["prologue_compass"])
    prologue_preview = bump204_to_224(b204["prologue_preview"])

    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    row204_loop_anchor = (
        "### Row 204 closing loop (Row 68 → Row 184 Row 68 → Row 64 "
        "book-loop meta prelude capstone reunion) {#row-204-closing-loop}"
    )
    row205_loop_end = (
        "### Row 205 closing loop (Row 68 → Row 185 Row 68 → Row 65 "
        "second-pass meta prelude capstone reunion) {#row-205-closing-loop}"
    )
    epilogue_loop = bump204_to_224(
        row204_loop_anchor + epilogue.split(row204_loop_anchor, 1)[1].split(row205_loop_end, 1)[0]
    )
    epilogue_loop = epilogue_loop.replace("{#row-204-closing-loop}", "{#row-224-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 204 closing loop (Row 68 → Row 184 Row 68 → Row 64 book-loop meta prelude capstone reunion)",
        "### Row 224 closing loop (Row 68 → Row 204 Row 68 → Row 64 book-loop meta prelude capstone reunion)",
        1,
    )

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src204_header = (
        "## Row 68 → Row 184 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 204)"
    )
    next205_header = (
        "## Row 68 → Row 185 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 205)"
    )
    sources_index = bump204_to_224(sources.split(src204_header, 1)[1].split(next205_header, 1)[0])
    sources_index = (
        "## Row 68 → Row 204 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 224) "
        "{#row68-row204-book-loop-meta-prelude-capstone-reunion-index-row-224}"
        + sources_index
    )

    sources_table = bump204_to_224(b204["sources_table"])
    sources_table = sources_table.replace("| 204 | Row 68 → Row 184", "| 224 | Row 68 → Row 204", 1)

    memory_table = bump204_to_224(b204["memory_table"])
    memory_table = memory_table.replace("| 204 | Meta |", "| 224 | Meta |", 1)

    memory_baby = bump204_to_224(b204["memory_baby"])
    if "{#row-224-baby-picture-row68-row204" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 224 baby picture (Row 68 → Row 204 Row 68 → Row 64 book-loop meta prelude capstone reunion)",
            "### Row 224 baby picture {#row-224-baby-picture-row68-row204-book-loop-meta-prelude-capstone-reunion} "
            "(Row 68 → Row 204 Row 68 → Row 64 book-loop meta prelude capstone reunion)",
            1,
        )

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


ROW223_TAIL_OLD = (
    "When row 223 is complete, proceed to [row 204](preface.md#skill-navigation-row-224) when orchestration verifies individually but book-loop meta still feels disconnected from next-project restart after verified orchestration meta prelude capstone on the full capstone path,"
)
ROW223_TAIL_NEW = (
    "When row 223 is complete, proceed to [row 224](preface.md#skill-navigation-row-224) when orchestration verifies individually but book-loop meta still feels disconnected from next-project restart after verified orchestration meta prelude capstone on the full capstone path,"
)

ROW223_EPILOGUE_OLD = (
    "Proceed to [row 204](#row-204-closing-loop) when row 68 closed but book-loop meta still feels disconnected after row 203 on the full capstone path,"
)
ROW223_EPILOGUE_NEW = (
    "Proceed to [row 224](#row-224-closing-loop) when row 68 closed but book-loop meta still feels disconnected after row 223 on the full capstone path,"
)

ROW223_EPILOGUE_BEFORE_OLD = (
    "before row 224 book-loop meta prelude capstone reunion on the full capstone path (then row 204 book-loop on the full capstone path)."
)
ROW223_EPILOGUE_BEFORE_NEW = (
    "before row 225 second-pass meta prelude capstone reunion on the full capstone path (then row 205 second-pass on the full capstone path)."
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
        if ROW223_TAIL_OLD not in preface:
            raise SystemExit("row 223 tail proceed string not found")
        preface = preface.replace(ROW223_TAIL_OLD, ROW223_TAIL_NEW, 1)
        preface = preface.replace(
            "when opening [row 184](preface.md#skill-navigation-row-184) before row 64 closes on the full capstone path",
            "when opening [row 224](preface.md#skill-navigation-row-224) before row 64 closes on the full capstone path",
            1,
        )
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row224_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 224")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-224" not in prologue:
        needle = "| Row 68 → Row 203 Row 68 → Row 63 orchestration meta prelude capstone reunion (row 203) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 223 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 224 closing stitch" not in prologue:
            for anchor in ("**Row 204 closing stitch", "**Row 184 closing stitch"):
                if anchor in prologue:
                    prologue = prologue.replace(anchor, b["prologue_stitch"] + anchor, 1)
                    break
            else:
                raise SystemExit("prologue stitch anchor not found")
        preview_anchor = '| <span id="prologue-preview-row-223"></span>Row 203 preview'
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW223_EPILOGUE_BEFORE_OLD in prologue:
            prologue = prologue.replace(ROW223_EPILOGUE_BEFORE_OLD, ROW223_EPILOGUE_BEFORE_NEW, 1)
        prologue_path.write_text(prologue)
        print("prologue: added row 224")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "{#row-224-closing-loop}" not in epilogue:
        if ROW223_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW223_EPILOGUE_OLD, ROW223_EPILOGUE_NEW, 1)
        marker = (
            "### Row 186 closing loop (Row 68 → Row 166 Row 68 → Row 66 Writings canonical meta prelude capstone reunion)"
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
            "## Row 68 → Row 184 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 204)"
        )
        sources = sources.replace(src204_header, b["sources_index"] + src204_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 224")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-224-baby-picture-row68-row204" not in memory:
        memory = memory.replace(
            "| 204 | Meta | [Row 68 → Row 144 book-loop meta prelude capstone reunion index]",
            b["memory_table"] + "| 204 | Meta | [Row 68 → Row 144 book-loop meta prelude capstone reunion index]",
            1,
        )
        inserted = False
        for baby_anchor in (
            "### Row 204 baby picture (Row 68 → Row 184 Row 68 → Row 64 book-loop meta prelude capstone reunion)",
            "### Row 203 baby picture (Row 68 → Row 183 Row 68 → Row 63 orchestration meta prelude capstone reunion)",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 224")


if __name__ == "__main__":
    main()
