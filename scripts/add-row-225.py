#!/usr/bin/env python3
"""Add row 225 meta-stitch (Row 68 → Row 205 ↔ Row 65 second-pass meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]


def lift205_to_225(text: str) -> str:
    """Lift row-205 capstone meta copy to row 225 (+20: 185→205 index, 205→225 checkpoint)."""
    out = text.replace("row 226", "__R226__")
    out = out.replace("row 225", "__R225__")
    out = out.replace("row 224", "__R224__")
    out = out.replace("row 205", "__R205__")
    repl = [
        ("Row 68 → Row 185 Row 68 → Row 65", "Row 68 → Row 205 Row 68 → Row 65"),
        (
            "row68-row185-second-pass-meta-prelude-capstone-reunion-index-row-205",
            "row68-row205-second-pass-meta-prelude-capstone-reunion-index-row-225",
        ),
        (
            "row-205-baby-picture-row68-row185-second-pass-meta-prelude-capstone-reunion",
            "row-225-baby-picture-row68-row205-second-pass-meta-prelude-capstone-reunion",
        ),
        ("prologue-preview-row-205", "prologue-preview-row-225"),
        ("row-205-closing-stitch", "row-225-closing-stitch"),
        ("row-205-closing-loop", "row-225-closing-loop"),
        ("Row 205 three-way audit", "Row 225 three-way audit"),
        (
            "verified book-loop meta prelude capstone closure (row 204)",
            "verified book-loop meta prelude capstone closure (row 224)",
        ),
        (
            "before row 206 Writings canonical meta prelude capstone opens on the full capstone path",
            "before row 226 Writings canonical meta prelude capstone opens on the full capstone path",
        ),
        (
            "before row 206 Writings canonical meta prelude capstone reunion on the full capstone path",
            "before row 226 Writings canonical meta prelude capstone reunion on the full capstone path",
        ),
        (
            "Row 68 → Row 185 second-pass meta prelude capstone reunion index (row 205)",
            "Row 68 → Row 205 second-pass meta prelude capstone reunion index (row 225)",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace("skill-navigation-row-205", "skill-navigation-row-225")
    out = out.replace(
        "[row 204](preface.md#skill-navigation-row-204) or [row 185](preface.md#skill-navigation-row-185)",
        "[row 224](preface.md#skill-navigation-row-224) or [row 205](preface.md#skill-navigation-row-205)",
    )
    out = out.replace("row 185's epilogue second-pass", "row 205's epilogue second-pass")
    out = out.replace("| 205 |", "| 225 |")
    out = out.replace("memory sheet row 205", "memory sheet row 225")
    out = out.replace("prologue row 205", "prologue row 225")
    out = out.replace("epilogue row 205", "epilogue row 225")
    out = out.replace("When row 205 is complete", "When row 225 is complete")
    out = out.replace("when row 204 closed but row 65", "when row 224 closed but row 65")
    out = out.replace("when row 204 and row 65", "when row 224 and row 65")
    out = out.replace("after row 204 on the full capstone path", "after row 224 on the full capstone path")
    out = out.replace("after row 184 on the full capstone path", "after row 204 on the full capstone path")
    out = out.replace("row 204's book-loop meta", "row 224's book-loop meta")
    out = out.replace("Row 205 does not replace", "Row 225 does not replace")
    out = out.replace(
        "Row 68 → Row 185 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 205)",
        "Row 68 → Row 205 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 225)",
    )
    out = out.replace("__R205__", "row 225")
    out = out.replace("__R224__", "row 224")
    out = out.replace("__R225__", "row 225")
    out = out.replace("__R226__", "row 226")
    return out


def _load_add205():
    spec = importlib.util.spec_from_file_location("add205", ROOT / "scripts/add-row-205.py")
    add205 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add205)
    return add205


def _build_blocks() -> dict[str, str]:
    add205 = _load_add205()
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 205 skill checkpoint")
    end = preface.index("\n\n### Row 206 skill checkpoint", start)
    row225_preface = lift205_to_225(preface[start:end]) + "\n\n"
    row225_preface = row225_preface.replace(
        "### Row 205 skill checkpoint",
        "### Row 225 skill checkpoint",
        1,
    ).replace("{#skill-navigation-row-205}", "{#skill-navigation-row-225}", 1)

    b205 = add205._build_blocks()
    prologue_stitch = lift205_to_225(
        b205["prologue_stitch"].replace("{#row-205-closing-stitch}", "{#row-225-closing-stitch}").replace(
            "**Row 205 closing stitch (Row 68 → Row 185",
            "**Row 225 closing stitch (Row 68 → Row 205",
        )
    )
    prologue_compass = lift205_to_225(b205["prologue_compass"])
    prologue_preview = lift205_to_225(b205["prologue_preview"])

    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    # Compact canonical slice (Row 205 → Row 204); do not split on row 186 (huge span).
    ep_loop_start = (
        "### Row 205 closing loop (Row 68 → Row 205 Row 68 → Row 65 "
        "second-pass meta prelude capstone reunion) {#row-205-closing-loop}"
    )
    ep_loop_end = (
        "\n\n### Row 204 closing loop (Row 68 → Row 184 Row 68 → Row 64 "
        "book-loop meta prelude capstone reunion) {#row-184-closing-loop}"
    )
    epilogue_loop = lift205_to_225(ep_loop_start + epilogue.split(ep_loop_start, 1)[1].split(ep_loop_end, 1)[0])
    epilogue_loop = epilogue_loop.replace("{#row-205-closing-loop}", "{#row-225-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 205 closing loop (Row 68 → Row 205",
        "### Row 225 closing loop (Row 68 → Row 205",
        1,
    )
    epilogue_loop = epilogue_loop.rstrip() + "\n\n"

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src205_header = (
        "## Row 68 → Row 185 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 205) "
        "{#row68-row185-second-pass-meta-prelude-capstone-reunion-index-row-205}"
    )
    next206_header = (
        "## Row 68 → Row 106 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 126)"
    )
    sources_index = lift205_to_225(sources.split(src205_header, 1)[1].split(next206_header, 1)[0])
    sources_index = (
        "## Row 68 → Row 205 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 225) "
        "{#row68-row205-second-pass-meta-prelude-capstone-reunion-index-row-225}\n"
        + sources_index.lstrip("\n")
    )

    sources_table = lift205_to_225(b205["sources_table"])
    sources_table = sources_table.replace("| 205 | Row 68 → Row 185", "| 225 | Row 68 → Row 205", 1)

    memory_table = lift205_to_225(b205["memory_table"])
    memory_table = memory_table.replace("| 205 | Meta |", "| 225 | Meta |", 1)

    memory = (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text()
    mem_baby_start = (
        "### Row 205 baby picture {#row-205-baby-picture-row68-row185-second-pass-meta-prelude-capstone-reunion}"
    )
    mem_baby_end = "\n\n### Row 204 baby picture"
    memory_baby = lift205_to_225(
        mem_baby_start + memory.split(mem_baby_start, 1)[1].split(mem_baby_end, 1)[0]
    )
    memory_baby = memory_baby.replace(
        "### Row 205 baby picture {#row-205-baby-picture-row68-row185-second-pass-meta-prelude-capstone-reunion}",
        "### Row 225 baby picture {#row-225-baby-picture-row68-row205-second-pass-meta-prelude-capstone-reunion}",
        1,
    ).rstrip() + "\n\n"

    return {
        "row225_preface": row225_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW224_TAIL_OLD = (
    "When row 224 is complete, proceed to [row 205](preface.md#skill-navigation-row-205) when row 68 closed but second-pass meta still feels disconnected from novel rhythm after verified book-loop meta prelude capstone on the full capstone path"
)
ROW224_TAIL_NEW = (
    "When row 224 is complete, proceed to [row 225](preface.md#skill-navigation-row-225) when row 68 closed but second-pass meta still feels disconnected from novel rhythm after verified book-loop meta prelude capstone on the full capstone path"
)

ROW224_EPILOGUE_OLD = (
    "Proceed to [row 205](#row-205-closing-loop) when row 68 closed but second-pass meta capstone still lags after row 224 on the full capstone path,"
)
ROW224_EPILOGUE_NEW = (
    "Proceed to [row 225](#row-225-closing-loop) when row 68 closed but second-pass meta capstone still lags after row 224 on the full capstone path,"
)

ROW224_BABY_OLD = (
    "row 204 when **epilogue book-loop cross-links and Row 63 → Row 44 meta must read on the same wire before row 205 second-pass meta prelude capstone reunion opens on the full capstone path**"
)
ROW224_BABY_NEW = (
    "row 204 when **epilogue book-loop cross-links and Row 63 → Row 44 meta must read on the same wire before row 225 second-pass meta prelude capstone reunion opens on the full capstone path**"
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 225 skill checkpoint" in preface:
        print("preface: row 225 already present")
    else:
        if "### Row 224 skill checkpoint" not in preface:
            raise SystemExit("row 224 must exist before row 225")
        if ROW224_TAIL_OLD in preface:
            preface = preface.replace(ROW224_TAIL_OLD, ROW224_TAIL_NEW, 1)
        preface = preface.replace(copper, "\n" + b["row225_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 225")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-225" not in prologue:
        needle = "| Row 68 → Row 204 Row 68 → Row 64 book-loop meta prelude capstone reunion (row 224) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 224 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 225 closing stitch" not in prologue:
            prologue = prologue.replace(
                "**Row 205 closing stitch",
                b["prologue_stitch"] + "**Row 205 closing stitch",
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-205"></span>Row 205 preview'
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        prologue_path.write_text(prologue)
        print("prologue: added row 225")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "{#row-225-closing-loop}" not in epilogue:
        if ROW224_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW224_EPILOGUE_OLD, ROW224_EPILOGUE_NEW, 1)
        marker = (
            "### Row 186 closing loop (Row 68 → Row 166 Row 68 → Row 66 Writings canonical meta prelude capstone reunion) {#row-186-closing-loop}"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 186 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 225")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row205-second-pass-meta-prelude-capstone-reunion-index-row-225" not in sources:
        sources = sources.replace(
            "| 205 | Row 68 → Row 185 Row 68 → Row 65 second-pass meta prelude capstone",
            b["sources_table"] + "| 205 | Row 68 → Row 185 Row 68 → Row 65 second-pass meta prelude capstone",
            1,
        )
        src205_header = (
            "## Row 68 → Row 185 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 205) "
            "{#row68-row185-second-pass-meta-prelude-capstone-reunion-index-row-205}"
        )
        sources = sources.replace(src205_header, b["sources_index"] + src205_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 225")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-225-baby-picture-row68-row205" not in memory:
        memory = memory.replace(
            "| 205 | Meta | [Row 68 → Row 185 second-pass meta prelude capstone reunion index]",
            b["memory_table"] + "| 205 | Meta | [Row 68 → Row 185 second-pass meta prelude capstone reunion index]",
            1,
        )
        baby_anchor = (
            "### Row 205 baby picture {#row-205-baby-picture-row68-row185-second-pass-meta-prelude-capstone-reunion}"
        )
        if baby_anchor not in memory:
            raise SystemExit("memory baby picture anchor not found")
        memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
        if ROW224_BABY_OLD in memory:
            memory = memory.replace(ROW224_BABY_OLD, ROW224_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 225")


if __name__ == "__main__":
    main()
