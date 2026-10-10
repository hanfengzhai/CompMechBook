#!/usr/bin/env python3
"""Add row 235 meta-stitch (Row 68 → Row 215 ↔ Row 55 electronic audit meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util
import re

ROOT = Path(__file__).resolve().parents[1]

PRESERVE_ROW_NUMS = {
    20, 32, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 88, 89, 108,
}


def bump_meta_plus20(text: str) -> str:
    """Shift capstone-path meta row numbers by +20; preserve plot-spine row ids (48, 49, 68, …)."""

    def repl(m: re.Match[str]) -> str:
        n = int(m.group(1))
        if n in PRESERVE_ROW_NUMS:
            return m.group(0)
        return m.group(0).replace(str(n), str(n + 20))

    for pat in (
        r"(?<![0-9])row (\d+)",
        r"(?<![0-9])Row (\d+)",
        r"skill-navigation-row-(\d+)",
        r"prologue-preview-row-(\d+)",
        r"row-(\d+)-closing",
        r"row-(\d+)-baby-picture",
        r"row68-row(\d+)",
        r"reunion-index-row-(\d+)",
    ):
        text = re.sub(pat, repl, text)
    return text


def t215_to_235(text: str) -> str:
    return bump_meta_plus20(text)


def _load_add215():
    spec = importlib.util.spec_from_file_location("add215", ROOT / "scripts/add-row-215.py")
    add215 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add215)
    return add215


def _build_blocks() -> dict[str, str]:
    add215 = _load_add215()
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 215 skill checkpoint")
    end = preface.index("\n\n### Row 216 skill checkpoint", start)
    row235_preface = t215_to_235(preface[start:end]) + "\n\n"

    b215 = add215._build_blocks()
    prologue_stitch = t215_to_235(b215["prologue_stitch"].strip()) + "\n\n"
    prologue_compass = t215_to_235(b215["prologue_compass"])
    if not prologue_compass.endswith("\n"):
        prologue_compass += "\n"
    prologue_preview = t215_to_235(b215["prologue_preview"])

    epilogue_loop = t215_to_235(b215["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace("{#row-215-closing-loop}", "{#row-235-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 195 closing loop (Row 68 → Row 175 Row 68 → Row 55 electronic audit meta prelude capstone reunion)",
        "### Row 235 closing loop (Row 68 → Row 215 Row 68 → Row 55 electronic audit meta prelude capstone reunion)",
        1,
    )
    epilogue_loop = epilogue_loop.replace(
        "### Row 215 closing loop (Row 68 → Row 195 Row 68 → Row 55 electronic audit meta prelude capstone reunion)",
        "### Row 235 closing loop (Row 68 → Row 215 Row 68 → Row 55 electronic audit meta prelude capstone reunion)",
        1,
    )

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src215_header = (
        "## Row 68 → Row 195 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 215)"
    )
    next195_header = (
        "## Row 68 → Row 175 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 195)"
    )
    i = sources.index(src215_header)
    j = sources.index(next195_header, i + len(src215_header))
    sources_index = t215_to_235(sources[i:j])
    if "(row 235) {#row68-row215-electronic-audit-meta-prelude-capstone-reunion-index-row-235}" not in sources_index:
        sources_index = sources_index.replace(
            "(row 215) {#row68-row195-electronic-audit-meta-prelude-capstone-reunion-index-row-215}",
            "(row 235) {#row68-row215-electronic-audit-meta-prelude-capstone-reunion-index-row-235}",
            1,
        )
    sources_index = sources_index.replace(
        "row68-row195-electronic-audit-meta-prelude-capstone-reunion-index-row-215",
        "row68-row215-electronic-audit-meta-prelude-capstone-reunion-index-row-235",
    )

    sources_table = t215_to_235(b215["sources_table"])
    sources_table = sources_table.replace("| 215 | Row 68 → Row 195", "| 235 | Row 68 → Row 215", 1)

    memory_table = t215_to_235(b215["memory_table"])
    memory_table = memory_table.replace("| 215 | Meta |", "| 235 | Meta |", 1)

    memory_baby = t215_to_235(b215["memory_baby"])
    if "{#row-235-baby-picture-row68-row215-electronic-audit-meta-prelude-capstone-reunion}" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 235 baby picture",
            "### Row 235 baby picture {#row-235-baby-picture-row68-row215-electronic-audit-meta-prelude-capstone-reunion}",
            1,
        )
        memory_baby = memory_baby.replace(
            "### Row 215 baby picture {#row-215-baby-picture-row68-row195-electronic-audit-meta-prelude-capstone-reunion}",
            "### Row 235 baby picture {#row-235-baby-picture-row68-row215-electronic-audit-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row235_preface": row235_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW234_STITCH_OLD = (
    "before row 235 electronic audit meta prelude capstone reunion opens on the full capstone path."
)
ROW234_STITCH_NEW = (
    "before row 236 Born–Oppenheimer meta prelude capstone reunion opens on the full capstone path."
)

EPILOGUE_235_PARTIAL_HEAD = (
    "### Row 215 closing loop (Row 68 → Row 215 Row 68 → Row 55 electronic audit meta prelude capstone reunion) {#row-235-closing-loop}"
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 235 skill checkpoint" in preface:
        print("preface: row 235 already present")
    else:
        if "### Row 234 skill checkpoint" not in preface:
            raise SystemExit("row 234 must exist before row 235")
        preface = preface.replace(
            "when opening [row 155](preface.md#skill-navigation-row-155) before row 55 closes on the full capstone path",
            "when opening [row 175](preface.md#skill-navigation-row-175) before row 55 closes on the full capstone path",
            1,
        )
        preface = preface.replace(copper, "\n" + b["row235_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 235")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-235" not in prologue:
        needle = (
            "| Row 68 → Row 214 Row 68 → Row 54 export meta prelude capstone reunion (row 214) | "
            "[Preface: row 214 skill checkpoint](../preface.md#skill-navigation-row-234)"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 234 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        stitch_anchors = (
            "**Row 214 closing stitch (Row 68 → Row 214 Row 68 → Row 54 export meta prelude capstone reunion).** {#row-234-closing-stitch}",
            "**Row 213 closing stitch",
        )
        if "{#row-235-closing-stitch}" not in prologue:
            inserted = False
            for anchor in stitch_anchors:
                if anchor in prologue:
                    prologue = prologue.replace(anchor, b["prologue_stitch"] + anchor, 1)
                    inserted = True
                    break
            if not inserted:
                print("prologue: row 235 closing stitch anchor not found (skipped stitch block)")
        preview_anchor = '| <span id="prologue-preview-row-234"></span>Row 214 preview'
        if preview_anchor in prologue and '<span id="prologue-preview-row-235">' not in prologue:
            prologue = prologue.replace(
                preview_anchor, b["prologue_preview"].strip() + "\n" + preview_anchor, 1
            )
        if ROW234_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW234_STITCH_OLD, ROW234_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 235")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "{#row-235-closing-loop}" in epilogue:
        if EPILOGUE_235_PARTIAL_HEAD in epilogue:
            epilogue = epilogue.replace(EPILOGUE_235_PARTIAL_HEAD, b["epilogue_loop"].split("\n", 1)[0], 1)
            epilogue_path.write_text(epilogue)
            print("epilogue: fixed row 235 closing loop heading")
        elif "### Row 235 closing loop" in epilogue:
            print("epilogue: row 235 already present")
        else:
            print("epilogue: row-235 anchor present (skipped insert)")
    else:
        insert_after = (
            "### Row 234 closing loop (Row 68 → Row 214 Row 68 → Row 54 "
            "export meta prelude capstone reunion) {#row-234-closing-loop}"
        )
        marker = (
            "### Row 210 closing loop (Row 68 → Row 190 Row 68 → Row 50 "
            "DDD meta prelude capstone reunion) {#row-210-closing-loop}"
        )
        if insert_after not in epilogue:
            raise SystemExit("epilogue row 234 insert anchor not found")
        if marker not in epilogue.split(insert_after, 1)[1]:
            raise SystemExit("epilogue row 210 marker not found after row 234")
        head, segment = epilogue.split(insert_after, 1)
        segment = segment.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(head + insert_after + segment)
        print("epilogue: added row 235")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row215-electronic-audit-meta-prelude-capstone-reunion-index-row-235" not in sources:
        src215_header = (
            "## Row 68 → Row 195 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 215)"
        )
        if "| 235 | Row 68 → Row 215" not in sources:
            sources = sources.replace(
                "| 215 | Row 68 → Row 195 Row 68 → Row 55 electronic audit meta prelude capstone",
                b["sources_table"] + "| 215 | Row 68 → Row 195 Row 68 → Row 55 electronic audit meta prelude capstone",
                1,
            )
        if src215_header in sources and b["sources_index"].strip() not in sources:
            sources = sources.replace(src215_header, b["sources_index"] + src215_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 235")
    elif "| 235 | Row 68 → Row 215" not in sources:
        sources = sources.replace(
            "| 215 | Row 68 → Row 215 Row 68 → Row 55 electronic audit meta prelude capstone (midpoint prelude gate ↔ export meta prelude capstone on full capstone path ↔ row 55 meta) | [Row 68 → Row 215 electronic audit meta prelude capstone reunion index](#row68-row215-electronic-audit-meta-prelude-capstone-reunion-index-row-235)",
            "| 235 | Row 68 → Row 215 Row 68 → Row 55 electronic audit meta prelude capstone (midpoint prelude gate ↔ export meta prelude capstone on full capstone path ↔ row 55 meta) | [Row 68 → Row 215 electronic audit meta prelude capstone reunion index](#row68-row215-electronic-audit-meta-prelude-capstone-reunion-index-row-235)",
            1,
        )
        sources_path.write_text(sources)
        print("sources: fixed row 235 table id")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-235-baby-picture-row68-row215" not in memory:
        memory = memory.replace(
            "| 234 | Meta | [Row 68 → Row 214 export meta prelude capstone reunion index]",
            b["memory_table"] + "| 234 | Meta | [Row 68 → Row 214 export meta prelude capstone reunion index]",
            1,
        )
        inserted = False
        for baby_anchor in (
            "### Row 234 baby picture {#row-234-baby-picture-row68-row214-export-meta-prelude-capstone-reunion}",
            "### Row 233 baby picture {#row-233-baby-picture-row68-row213-dynamics-meta-prelude-capstone-reunion}",
            "### Row 215 baby picture {#row-215-baby-picture-row68-row195-electronic-audit-meta-prelude-capstone-reunion}",
            "### Row 195 baby picture",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            table_anchor = "| 234 | Meta | [Row 68 → Row 214 export meta prelude capstone reunion index]"
            if table_anchor in memory:
                line_end = memory.find("\n", memory.find(table_anchor))
                memory = memory[: line_end + 1] + b["memory_table"] + memory[line_end + 1 :]
                print("memory-sheet: added row 235 table (baby section anchor skipped)")
            else:
                raise SystemExit("memory baby picture anchor not found")
        else:
            print("memory-sheet: added row 235 baby block")
        memory_path.write_text(memory)


if __name__ == "__main__":
    main()
