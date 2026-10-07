#!/usr/bin/env python3
"""Add row 206 meta-stitch (Row 68 → Row 186 ↔ Row 66 Writings canonical meta prelude capstone reunion, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def t186_to_206(text: str) -> str:
    """Transform row-186 capstone-path meta copy to row 206 (186→206, 166→186 inner, 205 gate)."""
    out = text.replace("row 207", "__R207__")
    out = text.replace("row 206", "__R206__")
    repl = [
        ("Row 68 → Row 166 Row 68 → Row 66", "TEMP206TITLE"),
        (
            "row68-row166-writings-meta-prelude-capstone-reunion-index-row-186",
            "TEMP206IDX",
        ),
        (
            "row-186-baby-picture-row68-row166-writings-meta-prelude-capstone-reunion",
            "row-206-baby-picture-row68-row186-writings-meta-prelude-capstone-reunion",
        ),
        ("skill-navigation-row-186", "TEMP206NAV"),
        ("prologue-preview-row-186", "prologue-preview-row-206"),
        ("row-186-closing-stitch", "row-206-closing-stitch"),
        ("row-186-closing-loop", "row-206-closing-loop"),
        ("Row 186 three-way audit", "Row 206 three-way audit"),
        (
            "[row 185](preface.md#skill-navigation-row-185) or [row 186](skill-navigation-row-186)",
            "[row 205](preface.md#skill-navigation-row-205) or [row 206](TEMP206NAV)",
        ),
        (
            "[row 185](preface.md#skill-navigation-row-145) or [Row 68 → Row 166 Writings canonical meta prelude capstone reunion index (row 186)](appendix/sources.md#row68-row166-writings-meta-prelude-capstone-reunion-index-row-186)",
            "[row 205](preface.md#skill-navigation-row-205) or [Row 68 → Row 186 Writings canonical meta prelude capstone reunion index (row 206)](appendix/sources.md#row68-row186-writings-meta-prelude-capstone-reunion-index-row-206)",
        ),
        (
            "verified second-pass meta prelude capstone closure on the full capstone path (row 185)",
            "verified second-pass meta prelude capstone closure on the full capstone path (row 205)",
        ),
        (
            "before row 187 part-boundary meta prelude capstone reunion opens on the full capstone path",
            "before row 207 part-boundary meta prelude capstone reunion opens on the full capstone path",
        ),
        (
            "before row 187 part-boundary meta prelude capstone reunion opens on the full capstone path",
            "before row 207 part-boundary meta prelude capstone reunion opens on the full capstone path",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace("TEMP206IDX", "row68-row186-writings-meta-prelude-capstone-reunion-index-row-206")
    out = out.replace("TEMP206NAV", "skill-navigation-row-206")
    out = out.replace("row 186", "row 206")
    out = out.replace("Row 186", "Row 206")
    out = out.replace("TEMP206TITLE", "Row 68 → Row 186 Row 68 → Row 66")
    out = out.replace("skill-navigation-row-186", "skill-navigation-row-206")
    out = out.replace(
        "[row 206](preface.md#skill-navigation-row-205)",
        "[row 205](preface.md#skill-navigation-row-205)",
    )
    out = out.replace(
        "[row 206](preface.md#skill-navigation-row-186)",
        "[row 186](preface.md#skill-navigation-row-186)",
    )
    out = out.replace("when row 185 closed", "when row 205 closed")
    out = out.replace("When row 185 closed", "When row 205 closed")
    out = out.replace("row 185 closed", "row 205 closed")
    out = out.replace("after row 185 alone", "after row 205 alone")
    out = out.replace("Recite [preface row 185]", "Recite [preface row 205]")
    out = out.replace("from row 185's", "from row 205's")
    out = out.replace("row 185 and row 66", "row 205 and row 66")
    out = out.replace("row 185 or row 166", "row 205 or row 186")
    out = out.replace("row 166", "row 186")
    out = out.replace("Row 166", "Row 186")
    out = out.replace(
        "row68-row146-writings-meta-prelude-capstone-reunion-index-row-166",
        "row68-row166-writings-meta-prelude-capstone-reunion-index-row-186",
    )
    out = out.replace(
        "row68-row166-writings-meta-prelude-capstone-reunion-index-row-186",
        "row68-row186-writings-meta-prelude-capstone-reunion-index-row-206",
    )
    out = out.replace("row 185", "row 205")
    out = out.replace("Row 185", "Row 205")
    out = out.replace("row 165", "row 185")
    out = out.replace("Row 165", "Row 185")
    out = out.replace("row 164", "row 184")
    out = out.replace("Row 164", "Row 184")
    out = out.replace(
        "row 186 names **Row 68 → Row 146 Row 68 → Row 66 Writings canonical meta prelude capstone reunion**",
        "row 186 names **Row 68 → Row 166 Row 68 → Row 66 Writings canonical meta prelude capstone reunion**",
    )
    out = out.replace("__R206__", "row 206")
    out = out.replace("__R207__", "row 207")
    return out


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    memory = (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text()

    start = preface.index("### Row 186 skill checkpoint")
    end = preface.index("\n\n### Row 187 skill checkpoint", start)
    row206_preface = t186_to_206(preface[start:end]) + "\n\n"

    row166_stitch = next(
        line
        for line in prologue.splitlines()
        if line.startswith("**Row 166 closing stitch") and "Writings canonical meta prelude capstone" in line
    )
    # Compose 166→186→206 so stitch title/anchor match row 206 (not a partial 186 lift).
    import importlib.util

    spec186 = importlib.util.spec_from_file_location("add186", ROOT / "scripts/add-row-186.py")
    add186 = importlib.util.module_from_spec(spec186)
    spec186.loader.exec_module(add186)
    row166_stitch = add186.t166_to_186(row166_stitch)

    prologue_compass = (
        "| Row 68 → Row 186 Row 68 → Row 66 Writings canonical meta prelude capstone reunion (row 206) | "
        "[Preface: row 206 skill checkpoint](../preface.md#skill-navigation-row-206) · "
        "[Row 68 → Row 186 Writings canonical meta prelude capstone reunion index](../appendix/sources.md#row68-row186-writings-meta-prelude-capstone-reunion-index-row-206) · "
        "[memory sheet row 206 baby picture](../appendix/memory-sheet.md#row-206-baby-picture-row68-row186-writings-meta-prelude-capstone-reunion) · "
        "[prologue row 206 preview row](#prologue-preview-row-206); [prologue row 206 closing stitch](#row-206-closing-stitch); "
        "[epilogue row 206 closing loop](../epilogue/multiscale.md#row-206-closing-loop) — "
        "read row 68 gate + row 205 or row 186 second-pass meta prelude capstone / Writings canonical meta prelude gate + epilogue writings cross-links + row 66 meta aloud "
        "when second pass reads as a novel on the full capstone path after verified book-loop meta prelude capstone but the next edit opens src/part* instead of writings/ |\n"
    )

    prologue_preview = (
        '| <span id="prologue-preview-row-206"></span>Row 206 preview (Row 68 → Row 186 Row 68 → Row 66 Writings canonical meta prelude capstone reunion) | '
        "Explain why midpoint closure (row 68) and Writings canonical meta (row 66) must be read together with the epilogue writings cross-links and sync discipline "
        "after verified second-pass meta prelude capstone on the full capstone path before novel rhythm and canonical source tree feel like separate courses | "
        'One sentence: "read row 68 gate + row 205 or row 186 second-pass meta prelude capstone / Writings canonical meta prelude gate + epilogue writings cross-links + row 66 meta aloud '
        "when second pass reads as a novel on the full capstone path after verified book-loop meta prelude capstone but the next edit opens src/part* instead of writings/\" — "
        "[preface row 206 skill checkpoint](../preface.md#skill-navigation-row-206); [prologue row 206 closing stitch](#row-206-closing-stitch); "
        "[Row 68 → Row 186 reunion index](../appendix/sources.md#row68-row186-writings-meta-prelude-capstone-reunion-index-row-206); "
        "[memory sheet row 206 baby picture](../appendix/memory-sheet.md#row-206-baby-picture-row68-row186-writings-meta-prelude-capstone-reunion); "
        "[epilogue Writings canonical cross-links audit](../epilogue/multiscale.md#opening-hinge-rows17-45-writings); "
        "[preface row 66 skill checkpoint](../preface.md#skill-navigation-row-66); "
        "[preface row 205 skill checkpoint](../preface.md#skill-navigation-row-205); "
        "[epilogue row 206 closing loop](../epilogue/multiscale.md#row-206-closing-loop) |\n"
    )

    row186_loop_anchor = (
        "### Row 186 closing loop (Row 68 → Row 166 Row 68 → Row 66 "
        "Writings canonical meta prelude capstone reunion) {#row-186-closing-loop}"
    )
    row187_loop_end = (
        "### Row 187 closing loop (Row 68 → Row 167 Row 68 → Row 67 "
        "part-boundary meta prelude capstone reunion) {#row-187-closing-loop}"
    )
    epilogue_loop = t186_to_206(
        row186_loop_anchor
        + epilogue.split(row186_loop_anchor, 1)[1].split(row187_loop_end, 1)[0]
    )

    src186_header = (
        "## Row 68 → Row 166 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 186)"
    )
    next187_header = (
        "## Row 68 → Row 127 Row 68 → Row 67 part-boundary meta prelude capstone reunion index (row 167)"
    )
    sources_index = t186_to_206(sources.split(src186_header, 1)[1].split(next187_header, 1)[0])
    sources_index = (
        "## Row 68 → Row 186 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 206) "
        "{#row68-row186-writings-meta-prelude-capstone-reunion-index-row-206}"
        + sources_index
    )

    sources_table = next(
        line for line in sources.splitlines() if line.startswith("| 186 | Row 68 → Row 166")
    )
    sources_table = (
        t186_to_206(sources_table).replace("| 186 | Row 68 → Row 186", "| 206 | Row 68 → Row 186", 1)
        + "\n"
    )

    memory_table = next(
        line for line in memory.splitlines() if line.startswith("| 205 | Meta |")
    )
    memory_table = t186_to_206(memory_table).replace("| 205 | Meta |", "| 206 | Meta |", 1) + "\n"

    baby_anchor = "### Row 185 baby picture {#row-205-baby-picture-row68-row185-second-pass-meta-prelude-capstone-reunion}"
    baby_end = "### Row 204 baby picture"
    memory_baby = t186_to_206(
        baby_anchor + memory.split(baby_anchor, 1)[1].split(baby_end, 1)[0]
    )
    memory_baby = memory_baby.replace(
        "### Row 205 baby picture {#row-206-baby-picture-row68-row186-writings-meta-prelude-capstone-reunion}",
        "### Row 206 baby picture {#row-206-baby-picture-row68-row186-writings-meta-prelude-capstone-reunion}",
        1,
    )

    return {
        "row206_preface": row206_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": t186_to_206(row166_stitch) + "\n\n",
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW205_TAIL_OLD = (
    "When row 205 is complete, proceed to [row 186](preface.md#skill-navigation-row-186) when row 68 closed but Writings canonical meta prelude capstone still lags after second-pass meta prelude capstone on the full capstone path"
)
ROW205_TAIL_NEW = (
    "When row 205 is complete, proceed to [row 206](preface.md#skill-navigation-row-206) when row 68 closed but Writings canonical meta prelude capstone still lags after second-pass meta prelude capstone on the full capstone path"
)

ROW205_EPILOGUE_OLD = (
    "Proceed to [row 186](#row-186-closing-loop) when row 68 closed but Writings canonical meta prelude capstone still lags after row 205 on the full capstone path,"
)
ROW205_EPILOGUE_NEW = (
    "Proceed to [row 206](#row-206-closing-loop) when row 68 closed but Writings canonical meta prelude capstone still lags after row 205 on the full capstone path,"
)

ROW205_BABY_OLD = (
    "row 205 when **epilogue second-pass cross-links and Row 64 → Row 45 meta must read on the same wire before row 146 Writings canonical meta prelude capstone reunion opens on the full capstone path**"
)
ROW205_BABY_NEW = (
    "row 205 when **epilogue second-pass cross-links and Row 64 → Row 45 meta must read on the same wire before row 206 Writings canonical meta prelude capstone reunion opens on the full capstone path**"
)


def main() -> None:
    b = _build_blocks()

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "### Row 206 skill checkpoint" in preface:
        print("preface: row 206 already present")
    else:
        if ROW205_TAIL_OLD not in preface:
            raise SystemExit("row 205 tail proceed marker not found")
        preface = preface.replace(ROW205_TAIL_OLD, ROW205_TAIL_NEW, 1)
        if "### Row 205 skill checkpoint" not in preface:
            raise SystemExit("row 205 must exist before row 206")
        preface = preface.replace(copper, "\n" + b["row206_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 206")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "**Row 206 closing stitch" not in prologue:
        needle = "| Row 68 → Row 185 Row 68 → Row 65 second-pass meta prelude capstone reunion (row 205) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 205 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 206 closing stitch" not in prologue:
            prologue = prologue.replace(
                "**Row 205 closing stitch",
                b["prologue_stitch"] + "**Row 205 closing stitch",
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-205"></span>Row 205 preview'
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        prologue_path.write_text(prologue)
        print("prologue: added row 206")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "### Row 206 closing loop" not in epilogue:
        if ROW205_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW205_EPILOGUE_OLD, ROW205_EPILOGUE_NEW, 1)
        marker = "### Row 187 closing loop (Row 68 → Row 167 Row 68 → Row 67 part-boundary meta prelude capstone reunion)"
        if marker not in epilogue:
            raise SystemExit("epilogue row 187 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 206")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row186-writings-meta-prelude-capstone-reunion-index-row-206" not in sources:
        sources = sources.replace(
            "| 186 | Row 68 → Row 166 Row 68 → Row 66 Writings canonical meta prelude capstone",
            b["sources_table"] + "| 186 | Row 68 → Row 166 Row 68 → Row 66 Writings canonical meta prelude capstone",
            1,
        )
        sources = sources.replace(
            src186_header := (
                "## Row 68 → Row 166 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 186)"
            ),
            b["sources_index"] + src186_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 206")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-206-baby-picture-row68-row186" not in memory:
        memory = memory.replace(
            "| 205 | Meta | [Row 68 → Row 184 book-loop meta prelude capstone reunion index]",
            b["memory_table"] + "| 205 | Meta | [Row 68 → Row 184 book-loop meta prelude capstone reunion index]",
            1,
        )
        memory = memory.replace(
            baby_anchor := (
                "### Row 185 baby picture {#row-205-baby-picture-row68-row185-second-pass-meta-prelude-capstone-reunion}"
            ),
            b["memory_baby"] + baby_anchor,
            1,
        )
        if ROW205_BABY_OLD in memory:
            memory = memory.replace(ROW205_BABY_OLD, ROW205_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 206")


if __name__ == "__main__":
    main()
