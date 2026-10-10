#!/usr/bin/env python3
"""Add row 209 meta-stitch (Row 68 → Row 189 ↔ Row 49 taxonomy meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]


def bump189_to_209(text: str) -> str:
    """Transform row-189 capstone-path meta copy to row 209 (189→209, 169→189 inner, 208 gate)."""
    out = text.replace("row 210", "__R210__")
    out = text.replace("row 209", "__R209__")
    out = text.replace("row 190", "__R190__")
    out = text.replace("row 189", "__R189__")
    repl = [
        ("Row 68 → Row 169 Row 68 → Row 49", "Row 68 → Row 189 Row 68 → Row 49"),
        (
            "row68-row169-taxonomy-meta-prelude-capstone-reunion-index-row-189",
            "TEMP209IDX",
        ),
        (
            "row-189-baby-picture-row68-row169-taxonomy-meta-prelude-capstone-reunion",
            "row-209-baby-picture-row68-row189-taxonomy-meta-prelude-capstone-reunion",
        ),
        ("### Row 189 skill checkpoint", "### Row 209 skill checkpoint"),
        ("skill-navigation-row-189", "skill-navigation-row-209"),
        ("prologue-preview-row-189", "prologue-preview-row-209"),
        ("row-189-closing-stitch", "row-209-closing-stitch"),
        ("row-189-closing-loop", "row-209-closing-loop"),
        ("Row 189 three-way audit", "Row 209 three-way audit"),
        (
            "[row 188](preface.md#skill-navigation-row-188) or [row 169](preface.md#skill-navigation-row-169)",
            "[row 208](preface.md#skill-navigation-row-208) or [row 189](preface.md#skill-navigation-row-189)",
        ),
        (
            "[row 188](preface.md#skill-navigation-row-188) or [Row 68 → Row 169 taxonomy meta prelude capstone reunion index (row 189)](appendix/sources.md#row68-row169-taxonomy-meta-prelude-capstone-reunion-index-row-189)",
            "[row 208](preface.md#skill-navigation-row-208) or [Row 68 → Row 189 taxonomy meta prelude capstone reunion index (row 209)](appendix/sources.md#row68-row189-taxonomy-meta-prelude-capstone-reunion-index-row-209)",
        ),
        (
            "verified midpoint meta prelude capstone on the full capstone path (row 188)",
            "verified midpoint meta prelude capstone on the full capstone path (row 208)",
        ),
        (
            "verified midpoint meta prelude capstone via [row 187]",
            "verified midpoint meta prelude capstone via [row 207]",
        ),
        (
            "before row 190 DDD meta prelude capstone reunion opens on the full capstone path",
            "before row 210 DDD meta prelude capstone reunion opens on the full capstone path",
        ),
        (
            "before row 170 DDD meta prelude capstone opens on the full capstone path",
            "before row 190 DDD meta prelude capstone opens on the full capstone path",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace("TEMP209IDX", "row68-row189-taxonomy-meta-prelude-capstone-reunion-index-row-209")
    out = out.replace("Row 189 does not replace", "Row 209 does not replace")
    out = out.replace("preface row 189", "preface row 209")
    out = out.replace("prologue row 189", "prologue row 209")
    out = out.replace("memory sheet row 189 baby picture", "memory sheet row 209 baby picture")
    out = out.replace("memory sheet row 189", "memory sheet row 209")
    out = out.replace("epilogue row 189", "epilogue row 209")
    out = out.replace("### Row 169 closing loop", "### Row 209 closing loop")
    out = out.replace("memory sheet row 169", "memory sheet row 209")
    out = out.replace("[Preface row 169]", "[Preface row 209]")
    out = out.replace("Prologue preview ([row 169]", "Prologue preview ([row 209]")
    out = out.replace("Row 169 closes", "Row 209 closes")
    out = out.replace("Row 68 → Row 49 meta (row 169)", "Row 68 → Row 49 meta (row 189)")
    out = out.replace("before row 170 DDD", "before row 190 DDD")
    out = out.replace("skill-navigation-row-168)", "skill-navigation-row-208)")
    out = out.replace("skill-navigation-row-187)", "skill-navigation-row-207)")
    out = out.replace(
        "reunion index (row 189)](appendix/sources.md#row68-row169-taxonomy",
        "reunion index (row 209)](appendix/sources.md#row68-row189-taxonomy",
    )
    out = out.replace(
        "(row 189)](appendix/sources.md#row68-row169-taxonomy-meta-prelude-capstone-reunion-index-row-189)",
        "(row 209)](appendix/sources.md#row68-row189-taxonomy-meta-prelude-capstone-reunion-index-row-209)",
    )
    out = out.replace(
        "[row 188](preface.md#skill-navigation-row-188) or [Row 68 → Row 169 taxonomy meta prelude capstone reunion index (row 189)]",
        "[row 208](preface.md#skill-navigation-row-208) or [Row 68 → Row 189 taxonomy meta prelude capstone reunion index (row 209)]",
    )
    out = out.replace("row 168, row 169", "row 188, row 189")
    out = out.replace("row 149, row 89", "row 169, row 89")
    out = out.replace("When row 209 is complete", "When row 209 is complete")
    out = out.replace("When row 189 is complete", "When row 209 is complete")
    out = out.replace("When row 188 closed", "When row 208 closed")
    out = out.replace("when row 188 closed", "when row 208 closed")
    out = out.replace("after row 188", "after row 208")
    out = out.replace("after row 188 alone", "after row 208 alone")
    out = out.replace("Recite [preface row 188]", "Recite [preface row 208]")
    out = out.replace("row 188's forest", "row 208's forest")
    out = out.replace(
        "[row 190](preface.md#skill-navigation-row-190) before row 50",
        "[row 210](preface.md#skill-navigation-row-210) before row 50",
    )
    out = out.replace(
        "proceed to [row 190](preface.md#skill-navigation-row-190) when taxonomy",
        "proceed to [row 210](preface.md#skill-navigation-row-210) when taxonomy",
    )
    out = out.replace(
        "[row 188](preface.md#skill-navigation-row-188) for the Row 68 ↔ Row 48 meta audit on the opening-hinge capstone path alone, to [row 207]",
        "[row 208](preface.md#skill-navigation-row-208) for the Row 68 ↔ Row 48 meta audit on the opening-hinge capstone path alone, to [row 207]",
    )
    out = out.replace("Row 68 → Row 169 reunion index", "Row 68 → Row 189 reunion index")
    out = out.replace(
        "Row 68 → Row 169 taxonomy meta prelude capstone reunion index",
        "Row 68 → Row 189 taxonomy meta prelude capstone reunion index",
    )
    out = out.replace("row 188, row 169", "row 208, row 189")
    out = out.replace("row 187 or row 169 recited", "row 207 or row 189 recited")
    out = out.replace("row 187", "row 207")
    out = out.replace("Row 187", "Row 207")
    out = out.replace("row 168", "row 188")
    out = out.replace("Row 168", "Row 188")
    out = out.replace("row 167", "row 187")
    out = out.replace("Row 167", "Row 187")
    out = out.replace(
        "row68-row149-taxonomy-meta-prelude-capstone-reunion-index-row-169",
        "row68-row169-taxonomy-meta-prelude-capstone-reunion-index-row-189",
    )
    out = out.replace(
        "row68-row168-midpoint-meta-prelude-capstone-reunion-index-row-188",
        "row68-row188-midpoint-meta-prelude-capstone-reunion-index-row-208",
    )
    out = out.replace("row 149", "row 169")
    out = out.replace("Row 149", "Row 169")
    out = out.replace("row 129", "row 149")
    out = out.replace("Row 129", "Row 149")
    out = out.replace("row 109", "row 129")
    out = out.replace("Row 109", "Row 129")
    out = out.replace("row 170", "row 190")
    out = out.replace("Row 170", "Row 190")
    out = out.replace("row 150", "row 170")
    out = out.replace("Row 150", "Row 170")
    out = out.replace("row 130", "row 150")
    out = out.replace("Row 130", "Row 150")
    out = out.replace("__R189__", "row 189")
    out = out.replace("__R190__", "row 190")
    out = out.replace("__R209__", "row 209")
    out = out.replace("__R210__", "row 210")
    out = out.replace("[row 209](preface.md#skill-navigation-row-208)", "[row 208](preface.md#skill-navigation-row-208)")
    out = out.replace("[row 209](preface.md#skill-navigation-row-189)", "[row 189](preface.md#skill-navigation-row-189)")
    out = out.replace("when row 188 and row 49", "when row 208 and row 49")
    out = out.replace("when row 168 and row 49", "when row 188 and row 49")
    out = out.replace("row 189 or row 170 recited", "row 209 or row 190 recited")
    out = out.replace(
        "Prologue preview ([row 189](prologue/00-many-scales.md#prologue-preview-row-209))",
        "Prologue preview ([row 209](prologue/00-many-scales.md#prologue-preview-row-209))",
    )
    out = out.replace(
        "reunion index (row 189)](appendix/sources.md#row68-row169-taxonomy-meta-prelude-capstone-reunion-index-row-189)",
        "reunion index (row 209)](appendix/sources.md#row68-row189-taxonomy-meta-prelude-capstone-reunion-index-row-209)",
    )
    out = out.replace(
        "verified midpoint meta prelude capstone closure on the full capstone path (row 188)",
        "verified midpoint meta prelude capstone closure on the full capstone path (row 208)",
    )
    out = out.replace("row 208 closed midpoint", "row 208 closed midpoint")
    out = out.replace(
        "row 209 names **Row 68 → Row 189 Row 68 → Row 49 taxonomy meta prelude capstone reunion**; row 209 names",
        "row 189 names **Row 68 → Row 169 Row 68 → Row 49 taxonomy meta prelude capstone reunion**; row 209 names",
    )
    return out


def t189_to_209(text: str) -> str:
    return bump189_to_209(text)


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    memory = (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text()

    start = preface.index("### Row 189 skill checkpoint")
    end = preface.index("\n\n### Row 190 skill checkpoint", start)
    row209_preface = t189_to_209(preface[start:end]) + "\n\n"

    spec189 = importlib.util.spec_from_file_location("add189", ROOT / "scripts/add-row-189.py")
    add189 = importlib.util.module_from_spec(spec189)
    spec189.loader.exec_module(add189)
    prologue_stitch = t189_to_209(add189.PROLOGUE_STITCH.strip()) + "\n\n"

    prologue_compass = (
        "| Row 68 → Row 189 Row 68 → Row 49 taxonomy meta prelude capstone reunion (row 209) | "
        "[Preface: row 209 skill checkpoint](../preface.md#skill-navigation-row-209) · "
        "[Row 68 → Row 189 taxonomy meta prelude capstone reunion index](../appendix/sources.md#row68-row189-taxonomy-meta-prelude-capstone-reunion-index-row-209) · "
        "[memory sheet row 209 baby picture](../appendix/memory-sheet.md#row-209-baby-picture-row68-row189-taxonomy-meta-prelude-capstone-reunion) · "
        "[prologue row 209 preview row](#prologue-preview-row-209); [prologue row 209 closing stitch](#row-209-closing-stitch); "
        "[epilogue row 209 closing loop](../epilogue/multiscale.md#row-209-closing-loop) — "
        "read row 68 gate + row 208 or row 189 midpoint meta prelude capstone / taxonomy meta prelude gate + VII.0 Bridge → opening hinge → VII.1 taxonomy + row 49 meta aloud "
        "when forest landing is clean on the full capstone path but Burgers circuits feel like Defects Notes homework after verified midpoint meta prelude capstone on the full capstone path |\n"
    )

    prologue_preview = (
        '| <span id="prologue-preview-row-209"></span>Row 209 preview (Row 68 → Row 189 Row 68 → Row 49 taxonomy meta prelude capstone reunion) | '
        "Explain why midpoint closure (row 68) and VII.0 → VII.1 meta (row 49) must be read together with the Bridge → Burgers taxonomy chain after verified midpoint meta prelude capstone on the full capstone path before forest landing and dimension tables feel like separate courses | "
        'One sentence: "read row 68 gate + row 208 or row 189 midpoint meta prelude capstone / taxonomy meta prelude gate + VII.0 Bridge → opening hinge → VII.1 taxonomy + row 49 meta aloud when forest landing is clean on the full capstone path but Burgers circuits feel like Defects Notes homework after verified midpoint meta prelude capstone on the full capstone path" — '
        "[preface row 209 skill checkpoint](../preface.md#skill-navigation-row-209); [prologue row 209 closing stitch](#row-209-closing-stitch); "
        "[Row 68 → Row 189 reunion index](../appendix/sources.md#row68-row189-taxonomy-meta-prelude-capstone-reunion-index-row-209); "
        "[memory sheet row 209 baby picture](../appendix/memory-sheet.md#row-209-baby-picture-row68-row189-taxonomy-meta-prelude-capstone-reunion); "
        "[VII.0 Bridge](../part07-defects/00-opening.md#bridge); "
        "[VII.0 opening hinge to VII.1](../part07-defects/00-opening.md#opening-hinge-vii0-to-vii1); "
        "[preface row 49 skill checkpoint](../preface.md#skill-navigation-row-49); "
        "[preface row 208 skill checkpoint](../preface.md#skill-navigation-row-208); "
        "[epilogue row 209 closing loop](../epilogue/multiscale.md#row-209-closing-loop) |\n"
    )

    row189_loop_anchor = (
        "### Row 189 closing loop (Row 68 → Row 189 Row 68 → Row 49 "
        "taxonomy meta prelude capstone reunion) {#row-189-closing-loop}"
    )
    row190_loop_end = (
        "### Row 190 closing loop (Row 68 → Row 170 Row 68 → Row 50 "
        "DDD meta prelude capstone reunion) {#row-190-closing-loop}"
    )
    if row189_loop_anchor not in epilogue:
        row189_loop_anchor = (
            "### Row 169 closing loop (Row 68 → Row 169 Row 68 → Row 49 "
            "taxonomy meta prelude capstone reunion) {#row-189-closing-loop}"
        )
    epilogue_loop = t189_to_209(
        row189_loop_anchor
        + epilogue.split(row189_loop_anchor, 1)[1].split(row190_loop_end, 1)[0]
    )

    src189_header = (
        "## Row 68 → Row 169 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 189)"
    )
    next190_header = (
        "## Row 68 → Row 170 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 190)"
    )
    sources_index = t189_to_209(sources.split(src189_header, 1)[1].split(next190_header, 1)[0])
    sources_index = (
        "## Row 68 → Row 189 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 209) "
        "{#row68-row189-taxonomy-meta-prelude-capstone-reunion-index-row-209}"
        + sources_index
    )

    sources_table = next(
        line for line in sources.splitlines() if line.startswith("| 189 | Row 68 → Row 169")
    )
    sources_table = (
        t189_to_209(sources_table).replace("| 189 | Row 68 → Row 189", "| 209 | Row 68 → Row 189", 1)
        + "\n"
    )

    memory_table = next(
        line for line in memory.splitlines() if line.startswith("| 189 | Meta |")
    )
    memory_table = t189_to_209(memory_table).replace("| 189 | Meta |", "| 209 | Meta |", 1) + "\n"

    baby_start = "### Row 189 baby picture"
    baby_end = "### Row 190 baby picture"
    if baby_start not in memory:
        baby_start = "### Row 169 baby picture"
        baby_end = "### Row 170 baby picture"
    memory_baby = t189_to_209(
        baby_start + memory.split(baby_start, 1)[1].split(baby_end, 1)[0]
    )
    memory_baby = memory_baby.replace(
        "### Row 209 baby picture — read",
        "### Row 209 baby picture {#row-209-baby-picture-row68-row189-taxonomy-meta-prelude-capstone-reunion} — read",
        1,
    )
    if "{#row-209-baby-picture" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 209 baby picture",
            "### Row 209 baby picture {#row-209-baby-picture-row68-row189-taxonomy-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row209_preface": row209_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW208_TAIL_OLD = (
    "When row 188 is complete, proceed to [row 209](preface.md#skill-navigation-row-209) when midpoint meta prelude capstone is clean but taxonomy meta prelude capstone still lags after verified forest landing on the full capstone path, to [row 149](preface.md#skill-navigation-row-129) when midpoint meta prelude capstone is clean but taxonomy meta prelude capstone still lags after verified forest landing on the opening-hinge capstone path alone, to [row 129](preface.md#skill-navigation-row-109) for the Row 68 ↔ Row 49 meta audit on the opening-hinge prelude path alone, to [row 108](preface.md#skill-navigation-row-108) for the Row 68 ↔ Row 48 meta audit on the opening-hinge prelude path alone, to [row 188](preface.md#skill-navigation-row-188) for the Row 68 ↔ Row 48 meta audit on the opening-hinge capstone path alone, to [row 207](preface.md#skill-navigation-row-207) when part-boundary meta prelude capstone still lags after verified Writings canonical meta prelude capstone on the full capstone path, to [row 88](preface.md#skill-navigation-row-88) for the Row 68 ↔ Row 48 opening prelude audit alone, to [row 48](preface.md#skill-navigation-row-48) for the VI.4 → VII.0 meta audit alone, to [row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, or extend prose only under `writings/` then sync."
)
ROW208_TAIL_NEW = (
    "When row 208 is complete, proceed to [row 209](preface.md#skill-navigation-row-209) when midpoint meta prelude capstone is clean but taxonomy meta prelude capstone still lags after verified forest landing on the full capstone path, to [row 169](preface.md#skill-navigation-row-149) when midpoint meta prelude capstone is clean but taxonomy meta prelude capstone still lags after verified forest landing on the opening-hinge capstone path alone, to [row 149](preface.md#skill-navigation-row-129) for the Row 68 ↔ Row 49 meta audit on the opening-hinge prelude path alone, to [row 108](preface.md#skill-navigation-row-108) for the Row 68 ↔ Row 48 meta audit on the opening-hinge prelude path alone, to [row 208](preface.md#skill-navigation-row-208) for the Row 68 ↔ Row 48 meta audit on the opening-hinge capstone path alone, to [row 207](preface.md#skill-navigation-row-207) when part-boundary meta prelude capstone still lags after verified Writings canonical meta prelude capstone on the full capstone path, to [row 88](preface.md#skill-navigation-row-88) for the Row 68 ↔ Row 48 opening prelude audit alone, to [row 48](preface.md#skill-navigation-row-48) for the VI.4 → VII.0 meta audit alone, to [row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, or extend prose only under `writings/` then sync."
)

ROW208_EPILOGUE_OLD = (
    "Proceed to [row 209](#row-189-closing-loop) when row 68 closed but taxonomy meta prelude capstone still lags after row 208 on the full capstone path,"
)
ROW208_EPILOGUE_NEW = (
    "Proceed to [row 209](#row-209-closing-loop) when row 68 closed but taxonomy meta prelude capstone still lags after row 208 on the full capstone path,"
)

ROW208_BABY_OLD = (
    "when opening [row 209](preface.md#skill-navigation-row-209) before row 49 closes on the full capstone path"
)
ROW208_BABY_NEW = (
    "when opening [row 209](preface.md#skill-navigation-row-209) before row 49 closes on the full capstone path"
)

ROW208_STITCH_OLD = (
    "before row 209 taxonomy meta prelude capstone reunion opens on the full capstone path."
)
ROW208_STITCH_NEW = (
    "before row 210 taxonomy meta prelude capstone reunion opens on the full capstone path."
)


def main() -> None:
    b = _build_blocks()

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "### Row 209 skill checkpoint" in preface:
        print("preface: row 209 already present")
    else:
        if "### Row 208 skill checkpoint" not in preface:
            raise SystemExit("row 208 must exist before row 209")
        if ROW208_TAIL_OLD in preface:
            preface = preface.replace(ROW208_TAIL_OLD, ROW208_TAIL_NEW, 1)
        preface = preface.replace(copper, "\n" + b["row209_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 209")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "**Row 209 closing stitch" not in prologue:
        needle = "| Row 68 → Row 188 Row 68 → Row 48 midpoint meta prelude capstone reunion (row 208) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 208 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 209 closing stitch" not in prologue:
            prologue = prologue.replace(
                "**Row 208 closing stitch",
                b["prologue_stitch"] + "**Row 208 closing stitch",
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-208"></span>Row 208 preview'
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW208_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW208_STITCH_OLD, ROW208_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 209")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "### Row 209 closing loop" not in epilogue:
        if ROW208_EPILOGUE_OLD not in epilogue:
            alt_old = (
                "Proceed to [row 189](#row-189-closing-loop) when row 68 closed but taxonomy meta prelude capstone still lags after row 188 on the full capstone path,"
            )
            alt_new = (
                "Proceed to [row 209](#row-209-closing-loop) when row 68 closed but taxonomy meta prelude capstone still lags after row 208 on the full capstone path,"
            )
            if alt_old in epilogue:
                epilogue = epilogue.replace(alt_old, alt_new, 1)
            elif ROW208_EPILOGUE_OLD in epilogue:
                epilogue = epilogue.replace(ROW208_EPILOGUE_OLD, ROW208_EPILOGUE_NEW, 1)
        else:
            epilogue = epilogue.replace(ROW208_EPILOGUE_OLD, ROW208_EPILOGUE_NEW, 1)
        marker = (
            "### Row 189 closing loop (Row 68 → Row 169 Row 68 → Row 49 "
            "taxonomy meta prelude capstone reunion) {#row-189-closing-loop}"
        )
        if marker not in epilogue:
            marker = (
                "### Row 169 closing loop (Row 68 → Row 169 Row 68 → Row 49 "
                "taxonomy meta prelude capstone reunion) {#row-189-closing-loop}"
            )
        if marker not in epilogue:
            raise SystemExit("epilogue row 189 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 209")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row189-taxonomy-meta-prelude-capstone-reunion-index-row-209" not in sources:
        sources = sources.replace(
            "| 189 | Row 68 → Row 169 Row 68 → Row 49 taxonomy meta prelude capstone",
            b["sources_table"] + "| 189 | Row 68 → Row 169 Row 68 → Row 49 taxonomy meta prelude capstone",
            1,
        )
        sources = sources.replace(
            src189_header := (
                "## Row 68 → Row 169 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 189)"
            ),
            b["sources_index"] + src189_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 209")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-209-baby-picture-row68-row189" not in memory:
        memory = memory.replace(
            "| 189 | Meta | [Row 68 → Row 169 taxonomy meta prelude capstone reunion index]",
            b["memory_table"] + "| 189 | Meta | [Row 68 → Row 169 taxonomy meta prelude capstone reunion index]",
            1,
        )
        baby_insert = "### Row 189 baby picture"
        if baby_insert not in memory:
            baby_insert = "### Row 169 baby picture"
        memory = memory.replace(
            baby_insert,
            b["memory_baby"] + baby_insert,
            1,
        )
        memory_path.write_text(memory)
        print("memory-sheet: added row 209")


if __name__ == "__main__":
    main()
