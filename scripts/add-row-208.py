#!/usr/bin/env python3
"""Add row 208 meta-stitch (Row 68 → Row 188 ↔ Row 48 midpoint meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]


def bump188_to_208(text: str) -> str:
    """Transform row-188 capstone-path meta copy to row 208 (188→208, 168→188 inner, 207 gate)."""
    out = text.replace("row 209", "__R209__")
    out = text.replace("row 208", "__R208__")
    out = text.replace("row 189", "__R189__")
    out = text.replace("row 188", "__R188__")
    repl = [
        ("Row 68 → Row 168 Row 68 → Row 48", "Row 68 → Row 188 Row 68 → Row 48"),
        (
            "row68-row168-midpoint-meta-prelude-capstone-reunion-index-row-188",
            "TEMP208IDX",
        ),
        (
            "row-188-baby-picture-row68-row168-midpoint-meta-prelude-capstone-reunion",
            "row-208-baby-picture-row68-row188-midpoint-meta-prelude-capstone-reunion",
        ),
        ("### Row 188 skill checkpoint", "### Row 208 skill checkpoint"),
        ("skill-navigation-row-188", "skill-navigation-row-208"),
        ("prologue-preview-row-188", "prologue-preview-row-208"),
        ("row-188-closing-stitch", "row-208-closing-stitch"),
        ("row-188-closing-loop", "row-208-closing-loop"),
        ("Row 188 three-way audit", "Row 208 three-way audit"),
        (
            "[row 187](preface.md#skill-navigation-row-187) or [row 168](preface.md#skill-navigation-row-168)",
            "[row 207](preface.md#skill-navigation-row-207) or [row 188](preface.md#skill-navigation-row-188)",
        ),
        (
            "[row 187](preface.md#skill-navigation-row-187) or [Row 68 → Row 168 midpoint meta prelude capstone reunion index (row 188)](appendix/sources.md#row68-row168-midpoint-meta-prelude-capstone-reunion-index-row-188)",
            "[row 207](preface.md#skill-navigation-row-207) or [Row 68 → Row 188 midpoint meta prelude capstone reunion index (row 208)](appendix/sources.md#row68-row188-midpoint-meta-prelude-capstone-reunion-index-row-208)",
        ),
        (
            "verified part-boundary meta prelude capstone on the full capstone path (row 187)",
            "verified part-boundary meta prelude capstone on the full capstone path (row 207)",
        ),
        (
            "verified part-boundary meta prelude capstone via [row 187]",
            "verified part-boundary meta prelude capstone via [row 207]",
        ),
        (
            "before row 189 taxonomy meta prelude capstone reunion opens on the full capstone path",
            "before row 209 taxonomy meta prelude capstone reunion opens on the full capstone path",
        ),
        (
            "before row 169 taxonomy meta prelude capstone opens on the full capstone path",
            "before row 189 taxonomy meta prelude capstone opens on the full capstone path",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace("TEMP208IDX", "row68-row188-midpoint-meta-prelude-capstone-reunion-index-row-208")
    out = out.replace("Row 188 does not replace", "Row 208 does not replace")
    out = out.replace("(row 187) with the full-book", "(row 207) with the full-book")
    out = out.replace("prologue row 188", "prologue row 208")
    out = out.replace("memory sheet row 188", "memory sheet row 208")
    out = out.replace("epilogue row 188", "epilogue row 208")
    out = out.replace("When row 208 is complete", "When row 208 is complete")
    out = out.replace("When row 188 is complete", "When row 208 is complete")
    out = out.replace("When row 187 closed", "When row 207 closed")
    out = out.replace("when row 187 closed", "when row 207 closed")
    out = out.replace("after row 187", "after row 207")
    out = out.replace("after row 187 alone", "after row 207 alone")
    out = out.replace("Recite [preface row 187]", "Recite [preface row 207]")
    out = out.replace("row 187's twin-ladder", "row 207's twin-ladder")
    out = out.replace(
        "[row 189](preface.md#skill-navigation-row-189) before row 49",
        "[row 209](preface.md#skill-navigation-row-209) before row 49",
    )
    out = out.replace(
        "proceed to [row 189](preface.md#skill-navigation-row-189) when midpoint",
        "proceed to [row 209](preface.md#skill-navigation-row-209) when midpoint",
    )
    out = out.replace(
        "[row 168](preface.md#skill-navigation-row-168) for the Row 68 ↔ Row 48 meta audit on the opening-hinge capstone path alone, to [row 187](preface.md#skill-navigation-row-187) when part-boundary",
        "[row 188](preface.md#skill-navigation-row-188) for the Row 68 ↔ Row 48 meta audit on the opening-hinge capstone path alone, to [row 207](preface.md#skill-navigation-row-207) when part-boundary",
    )
    out = out.replace("Row 68 → Row 168 reunion index", "Row 68 → Row 188 reunion index")
    out = out.replace(
        "Row 68 → Row 168 midpoint meta prelude capstone reunion index",
        "Row 68 → Row 188 midpoint meta prelude capstone reunion index",
    )
    out = out.replace("row 168, row 108", "row 188, row 108")
    out = out.replace("row 187, row 168", "row 207, row 188")
    out = out.replace("row 167", "row 187")
    out = out.replace("Row 167", "Row 187")
    out = out.replace(
        "row68-row148-midpoint-meta-prelude-capstone-reunion-index-row-168",
        "row68-row168-midpoint-meta-prelude-capstone-reunion-index-row-188",
    )
    out = out.replace("row 166", "row 206")
    out = out.replace("Row 166", "Row 206")
    out = out.replace("row 148", "row 168")
    out = out.replace("Row 148", "Row 168")
    out = out.replace("row 129", "row 149")
    out = out.replace("Row 129", "Row 149")
    out = out.replace("row 109", "row 129")
    out = out.replace("Row 109", "Row 129")
    out = out.replace("row 127", "row 147")
    out = out.replace("Row 127", "Row 147")
    out = out.replace("__R188__", "row 188")
    out = out.replace("__R189__", "row 189")
    out = out.replace("__R208__", "row 208")
    out = out.replace("__R209__", "row 209")
    out = out.replace("[row 208](preface.md#skill-navigation-row-207)", "[row 207](preface.md#skill-navigation-row-207)")
    out = out.replace("[row 208](preface.md#skill-navigation-row-188)", "[row 188](preface.md#skill-navigation-row-188)")
    out = out.replace("when row 187 and row 48", "when row 207 and row 48")
    out = out.replace("when row 167 and row 48", "when row 187 and row 48")
    out = out.replace("after row 127 alone", "after row 207 alone")
    out = out.replace("row 127 closed", "row 207 closed")
    out = out.replace("skill-navigation-row-128", "skill-navigation-row-208")
    out = out.replace(
        "row 208 names **Row 68 → Row 188 Row 68 → Row 48 midpoint meta prelude capstone reunion**; row 208 names",
        "row 188 names **Row 68 → Row 168 Row 68 → Row 48 midpoint meta prelude capstone reunion**; row 208 names",
    )
    return out


def t188_to_208(text: str) -> str:
    return bump188_to_208(text)


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    memory = (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text()

    start = preface.index("### Row 188 skill checkpoint")
    end = preface.index("\n\n### Row 189 skill checkpoint", start)
    row208_preface = t188_to_208(preface[start:end]) + "\n\n"

    spec188 = importlib.util.spec_from_file_location("add188", ROOT / "scripts/add-row-188.py")
    add188 = importlib.util.module_from_spec(spec188)
    spec188.loader.exec_module(add188)
    prologue_stitch = t188_to_208(add188.PROLOGUE_STITCH.strip()) + "\n\n"

    prologue_compass = (
        "| Row 68 → Row 188 Row 68 → Row 48 midpoint meta prelude capstone reunion (row 208) | "
        "[Preface: row 208 skill checkpoint](../preface.md#skill-navigation-row-208) · "
        "[Row 68 → Row 188 midpoint meta prelude capstone reunion index](../appendix/sources.md#row68-row188-midpoint-meta-prelude-capstone-reunion-index-row-208) · "
        "[memory sheet row 208 baby picture](../appendix/memory-sheet.md#row-208-baby-picture-row68-row188-midpoint-meta-prelude-capstone-reunion) · "
        "[prologue row 208 preview row](#prologue-preview-row-208); [prologue row 208 closing stitch](#row-208-closing-stitch); "
        "[epilogue row 208 closing loop](../epilogue/multiscale.md#row-208-closing-loop) — "
        "read row 68 gate + row 207 or row 188 part-boundary meta prelude capstone / midpoint meta prelude gate + VI.4 intermission → Bridge → VII.0 landing + row 48 meta aloud "
        "when part-boundary meta prelude capstone is clean on the full capstone path but writings/continuum → writings/defects feels like two courses at the knee after verified twin-ladder reunion on the full capstone path |\n"
    )

    prologue_preview = (
        '| <span id="prologue-preview-row-208"></span>Row 208 preview (Row 68 → Row 188 Row 68 → Row 48 midpoint meta prelude capstone reunion) | '
        "Explain why midpoint closure (row 68) and VI.4 → VII.0 meta (row 48) must be read together with the intermission → Bridge chain after verified part-boundary meta prelude capstone on the full capstone path before continuum and defects subtrees feel like separate courses at the knee | "
        'One sentence: "read row 68 gate + row 207 or row 188 part-boundary meta prelude capstone / midpoint meta prelude gate + VI.4 intermission → Bridge → VII.0 landing + row 48 meta aloud when part-boundary meta prelude capstone is clean on the full capstone path but writings/continuum → writings/defects feels like two courses at the knee after verified twin-ladder reunion on the full capstone path" — '
        "[preface row 208 skill checkpoint](../preface.md#skill-navigation-row-208); [prologue row 208 closing stitch](#row-208-closing-stitch); "
        "[Row 68 → Row 188 reunion index](../appendix/sources.md#row68-row188-midpoint-meta-prelude-capstone-reunion-index-row-208); "
        "[memory sheet row 208 baby picture](../appendix/memory-sheet.md#row-208-baby-picture-row68-row188-midpoint-meta-prelude-capstone-reunion); "
        "[VI.4 Writings canonical hinge](../part06-continuum/04-nonlinear-plasticity-preview.md#writings-canonical-hinge-vi4-to-vii0); "
        "[VII.0 descent hinge from VI.4](../part07-defects/00-opening.md#descent-hinge-from-vi4-energy-break-forest-begins); "
        "[preface row 48 skill checkpoint](../preface.md#skill-navigation-row-48); "
        "[preface row 207 skill checkpoint](../preface.md#skill-navigation-row-207); "
        "[epilogue row 208 closing loop](../epilogue/multiscale.md#row-208-closing-loop) |\n"
    )

    row188_loop_anchor = (
        "### Row 188 closing loop (Row 68 → Row 188 Row 68 → Row 48 "
        "midpoint meta prelude capstone reunion) {#row-188-closing-loop}"
    )
    row189_loop_end = (
        "### Row 189 closing loop (Row 68 → Row 169 Row 68 → Row 49 "
        "taxonomy meta prelude capstone reunion) {#row-189-closing-loop}"
    )
    epilogue_loop = t188_to_208(
        row188_loop_anchor
        + epilogue.split(row188_loop_anchor, 1)[1].split(row189_loop_end, 1)[0]
    )

    src188_header = (
        "## Row 68 → Row 168 Row 68 → Row 48 midpoint meta prelude capstone reunion index (row 188)"
    )
    next189_header = (
        "## Row 68 → Row 169 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 189)"
    )
    sources_index = t188_to_208(sources.split(src188_header, 1)[1].split(next189_header, 1)[0])
    sources_index = (
        "## Row 68 → Row 188 Row 68 → Row 48 midpoint meta prelude capstone reunion index (row 208) "
        "{#row68-row188-midpoint-meta-prelude-capstone-reunion-index-row-208}"
        + sources_index
    )

    sources_table = next(
        line for line in sources.splitlines() if line.startswith("| 188 | Row 68 → Row 168")
    )
    sources_table = (
        t188_to_208(sources_table).replace("| 188 | Row 68 → Row 188", "| 208 | Row 68 → Row 188", 1)
        + "\n"
    )

    memory_table = next(
        line for line in memory.splitlines() if line.startswith("| 188 | Meta |")
    )
    memory_table = t188_to_208(memory_table).replace("| 188 | Meta |", "| 208 | Meta |", 1) + "\n"

    baby_start = "### Row 188 baby picture — read"
    baby_end = "### Row 207 baby picture"
    memory_baby = t188_to_208(
        baby_start + memory.split(baby_start, 1)[1].split(baby_end, 1)[0]
    )
    memory_baby = memory_baby.replace(
        "### Row 208 baby picture — read",
        "### Row 208 baby picture {#row-208-baby-picture-row68-row188-midpoint-meta-prelude-capstone-reunion} — read",
        1,
    )

    return {
        "row208_preface": row208_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW207_TAIL_OLD = (
    "When row 207 is complete, proceed to [row 208](preface.md#skill-navigation-row-188) when row 68 closed but midpoint meta prelude capstone still lags after verified part-boundary meta prelude capstone on the full capstone path, to [row 188](preface.md#skill-navigation-row-168) when row 68 closed but midpoint meta prelude capstone still lags after verified part-boundary meta prelude capstone on the opening-hinge capstone path alone, to [row 108](preface.md#skill-navigation-row-108) when twin-ladder reunion is clean but midpoint meta capstone still lags on the opening-hinge path, to [row 207](preface.md#skill-navigation-row-207) for the Row 68 ↔ Row 67 meta audit on the opening-hinge capstone path alone, to [row 206](preface.md#skill-navigation-row-186) when Writings canonical meta prelude capstone still lags after verified second-pass meta prelude capstone on the full capstone path, to [row 87](preface.md#skill-navigation-row-87) for the Row 68 ↔ Row 67 opening prelude audit alone, to [row 67](preface.md#skill-navigation-row-67) for the Row 66 ↔ Row 47 meta audit alone, to [row 47](preface.md#skill-navigation-row-47) for the V.4 → VI.0 meta audit alone, or extend prose only under `writings/` then sync."
)
ROW207_TAIL_NEW = (
    "When row 207 is complete, proceed to [row 208](preface.md#skill-navigation-row-208) when row 68 closed but midpoint meta prelude capstone still lags after verified part-boundary meta prelude capstone on the full capstone path, to [row 188](preface.md#skill-navigation-row-188) when row 68 closed but midpoint meta prelude capstone still lags after verified part-boundary meta prelude capstone on the opening-hinge capstone path alone, to [row 108](preface.md#skill-navigation-row-108) when twin-ladder reunion is clean but midpoint meta capstone still lags on the opening-hinge path, to [row 207](preface.md#skill-navigation-row-207) for the Row 68 ↔ Row 67 meta audit on the opening-hinge capstone path alone, to [row 206](preface.md#skill-navigation-row-206) when Writings canonical meta prelude capstone still lags after verified second-pass meta prelude capstone on the full capstone path, to [row 87](preface.md#skill-navigation-row-87) for the Row 68 ↔ Row 67 opening prelude audit alone, to [row 67](preface.md#skill-navigation-row-67) for the Row 66 ↔ Row 47 meta audit alone, to [row 47](preface.md#skill-navigation-row-47) for the V.4 → VI.0 meta audit alone, or extend prose only under `writings/` then sync."
)

ROW207_EPILOGUE_OLD = (
    "Proceed to [row 208](#row-188-closing-loop) when row 68 closed but midpoint meta prelude capstone still lags after row 207 on the full capstone path,"
)
ROW207_EPILOGUE_NEW = (
    "Proceed to [row 208](#row-208-closing-loop) when row 68 closed but midpoint meta prelude capstone still lags after row 207 on the full capstone path,"
)

ROW207_BABY_OLD = (
    "when opening [row 208](preface.md#skill-navigation-row-188) before row 48 closes on the full capstone path"
)
ROW207_BABY_NEW = (
    "when opening [row 208](preface.md#skill-navigation-row-208) before row 48 closes on the full capstone path"
)

ROW207_STITCH_OLD = (
    "before row 208 midpoint meta prelude capstone reunion opens on the full capstone path."
)
ROW207_STITCH_NEW = (
    "before row 209 midpoint meta prelude capstone reunion opens on the full capstone path."
)


def main() -> None:
    b = _build_blocks()

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "### Row 208 skill checkpoint" in preface:
        print("preface: row 208 already present")
    else:
        if "### Row 207 skill checkpoint" not in preface:
            raise SystemExit("row 207 must exist before row 208")
        if ROW207_TAIL_OLD in preface:
            preface = preface.replace(ROW207_TAIL_OLD, ROW207_TAIL_NEW, 1)
        if ROW207_BABY_OLD in preface:
            preface = preface.replace(ROW207_BABY_OLD, ROW207_BABY_NEW, 1)
        preface = preface.replace(copper, "\n" + b["row208_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 208")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "**Row 208 closing stitch" not in prologue:
        needle = "| Row 68 → Row 187 Row 68 → Row 67 part-boundary meta prelude capstone reunion (row 207) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 207 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 208 closing stitch" not in prologue:
            prologue = prologue.replace(
                "**Row 207 closing stitch",
                b["prologue_stitch"] + "**Row 207 closing stitch",
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-207"></span>Row 207 preview'
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW207_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW207_STITCH_OLD, ROW207_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 208")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "### Row 208 closing loop" not in epilogue:
        if ROW207_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW207_EPILOGUE_OLD, ROW207_EPILOGUE_NEW, 1)
        marker = (
            "### Row 188 closing loop (Row 68 → Row 188 Row 68 → Row 48 "
            "midpoint meta prelude capstone reunion) {#row-188-closing-loop}"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 188 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 208")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row188-midpoint-meta-prelude-capstone-reunion-index-row-208" not in sources:
        sources = sources.replace(
            "| 188 | Row 68 → Row 168 Row 68 → Row 48 midpoint meta prelude capstone",
            b["sources_table"] + "| 188 | Row 68 → Row 168 Row 68 → Row 48 midpoint meta prelude capstone",
            1,
        )
        sources = sources.replace(
            src188_header := (
                "## Row 68 → Row 168 Row 68 → Row 48 midpoint meta prelude capstone reunion index (row 188)"
            ),
            b["sources_index"] + src188_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 208")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-208-baby-picture-row68-row188" not in memory:
        memory = memory.replace(
            "| 188 | Meta | [Row 68 → Row 168 midpoint meta prelude capstone reunion index]",
            b["memory_table"] + "| 188 | Meta | [Row 68 → Row 168 midpoint meta prelude capstone reunion index]",
            1,
        )
        memory = memory.replace(
            baby_insert := "### Row 188 baby picture — read",
            b["memory_baby"] + baby_insert,
            1,
        )
        memory_path.write_text(memory)
        print("memory-sheet: added row 208")


if __name__ == "__main__":
    main()
