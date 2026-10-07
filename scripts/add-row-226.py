#!/usr/bin/env python3
"""Add row 226 meta-stitch (Row 68 → Row 206 ↔ Row 66 Writings canonical meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]


def lift206_to_226(text: str) -> str:
    """Lift row-206 capstone meta copy to row 226 (+20: 186→206 index, 206→226 checkpoint)."""
    out = text.replace("row 227", "__R227__")
    out = text.replace("row 226", "__R226__")
    out = text.replace("row 225", "__R225__")
    out = text.replace("row 206", "__R206__")
    repl = [
        ("Row 68 → Row 186 Row 68 → Row 66", "Row 68 → Row 206 Row 68 → Row 66"),
        (
            "row68-row186-writings-meta-prelude-capstone-reunion-index-row-206",
            "row68-row206-writings-meta-prelude-capstone-reunion-index-row-226",
        ),
        (
            "row-206-baby-picture-row68-row186-writings-meta-prelude-capstone-reunion",
            "row-226-baby-picture-row68-row206-writings-meta-prelude-capstone-reunion",
        ),
        ("prologue-preview-row-206", "prologue-preview-row-226"),
        ("row-206-closing-stitch", "row-226-closing-stitch"),
        ("row-206-closing-loop", "row-226-closing-loop"),
        ("Row 206 three-way audit", "Row 226 three-way audit"),
        (
            "verified second-pass meta prelude capstone closure on the full capstone path (row 205)",
            "verified second-pass meta prelude capstone closure on the full capstone path (row 225)",
        ),
        (
            "before row 207 part-boundary meta prelude capstone reunion opens on the full capstone path",
            "before row 227 part-boundary meta prelude capstone reunion opens on the full capstone path",
        ),
        (
            "before row 207 part-boundary meta prelude capstone reunion opens on the opening-hinge capstone path alone",
            "before row 227 part-boundary meta prelude capstone reunion opens on the opening-hinge capstone path alone",
        ),
        (
            "Row 68 → Row 186 Writings canonical meta prelude capstone reunion index (row 206)",
            "Row 68 → Row 206 Writings canonical meta prelude capstone reunion index (row 226)",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace("skill-navigation-row-206", "skill-navigation-row-226")
    out = out.replace(
        "[row 205](preface.md#skill-navigation-row-205) or [Row 68 → Row 186 Writings canonical meta prelude capstone reunion index (row 206)](appendix/sources.md#row68-row186-writings-meta-prelude-capstone-reunion-index-row-206)",
        "[row 225](preface.md#skill-navigation-row-225) or [Row 68 → Row 206 Writings canonical meta prelude capstone reunion index (row 226)](appendix/sources.md#row68-row206-writings-meta-prelude-capstone-reunion-index-row-226)",
    )
    out = out.replace("row 186's epilogue writings", "row 206's epilogue writings")
    out = out.replace("| 206 |", "| 226 |")
    out = out.replace("memory sheet row 206", "memory sheet row 226")
    out = out.replace("prologue row 206", "prologue row 226")
    out = out.replace("epilogue row 206", "epilogue row 226")
    out = out.replace("When row 206 is complete", "When row 226 is complete")
    out = out.replace("when row 205 closed but row 66", "when row 225 closed but row 66")
    out = out.replace("when row 205 and row 66", "when row 225 and row 66")
    out = out.replace("after row 205 on the full capstone path", "after row 225 on the full capstone path")
    out = out.replace("after row 205 alone", "after row 225 alone")
    out = out.replace("row 205 closed", "row 225 closed")
    out = out.replace("When row 205 closed", "When row 225 closed")
    out = out.replace("Row 206 does not replace", "Row 226 does not replace")
    out = out.replace("row 205's second-pass", "row 225's second-pass")
    out = out.replace("row 205 (second-pass meta prelude capstone on full path)", "row 225 (second-pass meta prelude capstone on full path)")
    out = out.replace("closure (row 205)", "closure (row 225)")
    out = out.replace("row 205 or row 186", "row 225 or row 206")
    out = out.replace("Recite [preface row 205]", "Recite [preface row 225]")
    out = out.replace(
        "Row 68 → Row 186 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 206)",
        "Row 68 → Row 206 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 226)",
    )
    out = out.replace("__R206__", "row 226")
    out = out.replace("__R225__", "row 225")
    out = out.replace("__R226__", "row 226")
    out = out.replace("__R227__", "row 227")
    return out


def _load_add206():
    spec = importlib.util.spec_from_file_location("add206", ROOT / "scripts/add-row-206.py")
    add206 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add206)
    return add206


def _build_blocks() -> dict[str, str]:
    add206 = _load_add206()
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 206 skill checkpoint")
    end = preface.index("\n\n### Row 207 skill checkpoint", start)
    row226_preface = lift206_to_226(preface[start:end]) + "\n\n"
    row226_preface = row226_preface.replace(
        "### Row 206 skill checkpoint",
        "### Row 226 skill checkpoint",
        1,
    ).replace("{#skill-navigation-row-206}", "{#skill-navigation-row-226}", 1)

    b206 = add206._build_blocks()
    prologue_stitch = lift206_to_226(
        b206["prologue_stitch"].replace("{#row-206-closing-stitch}", "{#row-226-closing-stitch}").replace(
            "**Row 206 closing stitch (Row 68 → Row 186",
            "**Row 226 closing stitch (Row 68 → Row 206",
        )
    )
    prologue_compass = lift206_to_226(b206["prologue_compass"])
    prologue_preview = lift206_to_226(b206["prologue_preview"])

    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    ep_loop_start = (
        "### Row 206 closing loop (Row 68 → Row 186 Row 68 → Row 66 "
        "Writings canonical meta prelude capstone reunion) {#row-206-closing-loop}"
    )
    ep_loop_end = (
        "\n\n### Row 205 closing loop (Row 68 → Row 185 Row 68 → Row 65 "
        "second-pass meta prelude capstone reunion) {#row-185-closing-loop}"
    )
    epilogue_loop = lift206_to_226(ep_loop_start + epilogue.split(ep_loop_start, 1)[1].split(ep_loop_end, 1)[0])
    epilogue_loop = epilogue_loop.replace("{#row-206-closing-loop}", "{#row-226-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 206 closing loop (Row 68 → Row 206",
        "### Row 226 closing loop (Row 68 → Row 206",
        1,
    )
    epilogue_loop = epilogue_loop.rstrip() + "\n\n"

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src206_header = (
        "## Row 68 → Row 186 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 206) "
        "{#row68-row186-writings-meta-prelude-capstone-reunion-index-row-206}"
    )
    next186_header = (
        "## Row 68 → Row 126 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 186)"
    )
    sources_index = lift206_to_226(sources.split(src206_header, 1)[1].split(next186_header, 1)[0])
    sources_index = (
        "## Row 68 → Row 206 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 226) "
        "{#row68-row206-writings-meta-prelude-capstone-reunion-index-row-226}\n"
        + sources_index.lstrip("\n")
    )

    sources_table = lift206_to_226(b206["sources_table"])
    sources_table = sources_table.replace("| 206 | Row 68 → Row 186", "| 226 | Row 68 → Row 206", 1)

    memory_table = lift206_to_226(b206["memory_table"])
    memory_table = memory_table.replace("| 206 | Meta |", "| 226 | Meta |", 1)

    memory = (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text()
    mem_baby_start = (
        "### Row 205 baby picture {#row-205-baby-picture-row68-row185-second-pass-meta-prelude-capstone-reunion}"
    )
    mem_baby_end = "\n\n### Row 204 baby picture"
    memory_baby = lift206_to_226(
        mem_baby_start + memory.split(mem_baby_start, 1)[1].split(mem_baby_end, 1)[0]
    )
    memory_baby = memory_baby.replace(
        "### Row 205 baby picture {#row-205-baby-picture-row68-row185-second-pass-meta-prelude-capstone-reunion}",
        "### Row 226 baby picture {#row-226-baby-picture-row68-row206-writings-meta-prelude-capstone-reunion}",
        1,
    ).rstrip() + "\n\n"

    return {
        "row226_preface": row226_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW225_TAIL_OLD = (
    "When row 225 is complete, proceed to [row 206](preface.md#skill-navigation-row-206) when row 68 closed but Writings canonical meta prelude capstone still lags after second-pass meta prelude capstone on the full capstone path"
)
ROW225_TAIL_NEW = (
    "When row 225 is complete, proceed to [row 226](preface.md#skill-navigation-row-226) when row 68 closed but Writings canonical meta prelude capstone still lags after second-pass meta prelude capstone on the full capstone path"
)

ROW225_EPILOGUE_OLD = (
    "Proceed to [row 206](#row-206-closing-loop) when row 68 closed but Writings canonical meta prelude capstone still lags after row 225 on the full capstone path"
)
ROW225_EPILOGUE_NEW = (
    "Proceed to [row 226](#row-226-closing-loop) when row 68 closed but Writings canonical meta prelude capstone still lags after row 225 on the full capstone path"
)

ROW225_BABY_OLD = (
    "row 206 Writings canonical meta prelude capstone reunion opens on the full capstone path**"
)
ROW225_BABY_NEW = (
    "row 226 Writings canonical meta prelude capstone reunion opens on the full capstone path**"
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 226 skill checkpoint" in preface:
        print("preface: row 226 already present")
    else:
        if "### Row 225 skill checkpoint" not in preface:
            raise SystemExit("row 225 must exist before row 226")
        if ROW225_TAIL_OLD in preface:
            preface = preface.replace(ROW225_TAIL_OLD, ROW225_TAIL_NEW, 1)
        preface = preface.replace(copper, "\n" + b["row226_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 226")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-226" not in prologue:
        needle = "| Row 68 → Row 205 Row 68 → Row 65 second-pass meta prelude capstone reunion (row 225) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 225 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 226 closing stitch" not in prologue:
            prologue = prologue.replace(
                "**Row 206 closing stitch",
                b["prologue_stitch"] + "**Row 206 closing stitch",
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-206"></span>Row 206 preview'
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        prologue_path.write_text(prologue)
        print("prologue: added row 226")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "{#row-226-closing-loop}" not in epilogue:
        if ROW225_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW225_EPILOGUE_OLD, ROW225_EPILOGUE_NEW, 1)
        marker = (
            "### Row 186 closing loop (Row 68 → Row 166 Row 68 → Row 66 Writings canonical meta prelude capstone reunion) {#row-186-closing-loop}"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 186 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 226")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row206-writings-meta-prelude-capstone-reunion-index-row-226" not in sources:
        sources = sources.replace(
            "| 206 | Row 68 → Row 186 Row 68 → Row 66 Writings canonical meta prelude capstone",
            b["sources_table"] + "| 206 | Row 68 → Row 186 Row 68 → Row 66 Writings canonical meta prelude capstone",
            1,
        )
        src206_header = (
            "## Row 68 → Row 186 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 206) "
            "{#row68-row186-writings-meta-prelude-capstone-reunion-index-row-206}"
        )
        sources = sources.replace(src206_header, b["sources_index"] + src206_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 226")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-226-baby-picture-row68-row206" not in memory:
        memory = memory.replace(
            "| 206 | Meta | [Row 68 → Row 184 book-loop meta prelude capstone reunion index]",
            b["memory_table"] + "| 206 | Meta | [Row 68 → Row 184 book-loop meta prelude capstone reunion index]",
            1,
        )
        baby_anchor = (
            "### Row 205 baby picture {#row-205-baby-picture-row68-row185-second-pass-meta-prelude-capstone-reunion}"
        )
        if baby_anchor not in memory:
            raise SystemExit("memory baby picture anchor not found")
        memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
        if ROW225_BABY_OLD in memory:
            memory = memory.replace(ROW225_BABY_OLD, ROW225_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 226")


if __name__ == "__main__":
    main()
