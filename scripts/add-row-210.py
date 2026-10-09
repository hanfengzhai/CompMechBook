#!/usr/bin/env python3
"""Add row 210 meta-stitch (Row 68 → Row 190 ↔ Row 50 DDD meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]


def bump190_to_210(text: str) -> str:
    """Transform row-190 capstone-path meta copy to row 210 (190→210, 170→190 inner, 209 gate)."""
    out = text.replace("row 210", "row 210")
    out = text.replace("row 209", "row 209")
    out = text.replace("row 190", "row 190")
    out = text.replace("row 189", "row 189")
    repl = [
        ("Row 68 → Row 170 Row 68 → Row 50", "Row 68 → Row 190 Row 68 → Row 50"),
        (
            "row68-row170-ddd-meta-prelude-capstone-reunion-index-row-190",
            "TEMP210IDX",
        ),
        (
            "row-190-baby-picture-row68-row170-ddd-meta-prelude-capstone-reunion",
            "row-210-baby-picture-row68-row190-ddd-meta-prelude-capstone-reunion",
        ),
        ("### Row 190 skill checkpoint", "### Row 210 skill checkpoint"),
        ("skill-navigation-row-190", "skill-navigation-row-210"),
        ("prologue-preview-row-190", "prologue-preview-row-210"),
        ("row-190-closing-stitch", "row-210-closing-stitch"),
        ("row-190-closing-loop", "row-210-closing-loop"),
        ("Row 190 three-way audit", "Row 210 three-way audit"),
        (
            "[row 189](preface.md#skill-navigation-row-189) or [row 170](preface.md#skill-navigation-row-170)",
            "[row 208](preface.md#skill-navigation-row-208) or [row 189](preface.md#skill-navigation-row-190)",
        ),
        (
            "[row 188](preface.md#skill-navigation-row-188) or [Row 68 → Row 169 DDD meta prelude capstone reunion index (row 190)](appendix/sources.md#row68-row169-ddd-meta-prelude-capstone-reunion-index-row-190)",
            "[row 208](preface.md#skill-navigation-row-208) or [Row 68 → Row 189 DDD meta prelude capstone reunion index (row 210)](appendix/sources.md#row68-row190-ddd-meta-prelude-capstone-reunion-index-row-209)",
        ),
        (
            "verified taxonomy meta prelude capstone on the full capstone path (row 169)",
            "verified taxonomy meta prelude capstone on the full capstone path (row 189)",
        ),
        (
            "verified taxonomy meta prelude capstone via [row 189]",
            "verified taxonomy meta prelude capstone via [row 209]",
        ),
        (
            "before row 210 DDD meta prelude capstone reunion opens on the full capstone path",
            "before row 211 homogenization meta prelude capstone reunion opens on the full capstone path",
        ),
        (
            "before row 190 DDD meta prelude capstone opens on the full capstone path",
            "before row 190 DDD meta prelude capstone opens on the full capstone path",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace("TEMP210IDX", "row68-row190-ddd-meta-prelude-capstone-reunion-index-row-210")
    out = out.replace("Row 190 does not replace", "Row 210 does not replace")
    out = out.replace("preface row 190", "preface row 210")
    out = out.replace("prologue row 190", "prologue row 210")
    out = out.replace("memory sheet row 190 baby picture", "memory sheet row 210 baby picture")
    out = out.replace("memory sheet row 190", "memory sheet row 210")
    out = out.replace("epilogue row 190", "epilogue row 210")
    out = out.replace("### Row 190 closing loop", "### Row 210 closing loop")
    out = out.replace("memory sheet row 169", "memory sheet row 210")
    out = out.replace("[Preface row 169]", "[Preface row 209]")
    out = out.replace("Prologue preview ([row 169]", "Prologue preview ([row 209]")
    out = out.replace("Row 169 closes", "Row 209 closes")
    out = out.replace("Row 68 → Row 50 meta (row 170)", "Row 68 → Row 50 meta (row 190)")
    out = out.replace("before row 170 DDD", "before row 190 DDD")
    out = out.replace("skill-navigation-row-168)", "skill-navigation-row-208)")
    out = out.replace("skill-navigation-row-187)", "skill-navigation-row-207)")
    out = out.replace(
        "reunion index (row 189)](appendix/sources.md#row68-row169-taxonomy",
        "reunion index (row 209)](appendix/sources.md#row68-row190-ddd",
    )
    out = out.replace(
        "(row 189)](appendix/sources.md#row68-row169-ddd-meta-prelude-capstone-reunion-index-row-190)",
        "(row 209)](appendix/sources.md#row68-row190-ddd-meta-prelude-capstone-reunion-index-row-209)",
    )
    out = out.replace(
        "[row 188](preface.md#skill-navigation-row-188) or [Row 68 → Row 169 DDD meta prelude capstone reunion index (row 190)]",
        "[row 208](preface.md#skill-navigation-row-208) or [Row 68 → Row 189 DDD meta prelude capstone reunion index (row 210)]",
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
        "[row 211](preface.md#skill-navigation-row-211) before row 51",
        "[row 211](preface.md#skill-navigation-row-211) before row 51",
    )
    out = out.replace(
        "proceed to [row 211](preface.md#skill-navigation-row-211) when homogenization",
        "proceed to [row 211](preface.md#skill-navigation-row-211) when homogenization",
    )
    out = out.replace(
        "[row 188](preface.md#skill-navigation-row-188) for the Row 68 ↔ Row 48 meta audit on the opening-hinge capstone path alone, to [row 207]",
        "[row 208](preface.md#skill-navigation-row-208) for the Row 68 ↔ Row 48 meta audit on the opening-hinge capstone path alone, to [row 207]",
    )
    out = out.replace("Row 68 → Row 170 reunion index", "Row 68 → Row 190 reunion index")
    out = out.replace(
        "Row 68 → Row 170 DDD meta prelude capstone reunion index",
        "Row 68 → Row 190 DDD meta prelude capstone reunion index",
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
        "row68-row170-ddd-meta-prelude-capstone-reunion-index-row-190",
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
    out = out.replace("row 189", "row 189")
    out = out.replace("row 190", "row 190")
    out = out.replace("row 209", "row 209")
    out = out.replace("row 210", "row 210")
    out = out.replace("[row 209](preface.md#skill-navigation-row-208)", "[row 208](preface.md#skill-navigation-row-208)")
    out = out.replace("[row 209](preface.md#skill-navigation-row-190)", "[row 189](preface.md#skill-navigation-row-190)")
    out = out.replace("when row 188 and row 49", "when row 208 and row 49")
    out = out.replace("when row 168 and row 49", "when row 188 and row 49")
    out = out.replace("row 209 or row 190 recited", "row 209 or row 190 recited")
    out = out.replace(
        "Prologue preview ([row 189](prologue/00-many-scales.md#prologue-preview-row-210))",
        "Prologue preview ([row 209](prologue/00-many-scales.md#prologue-preview-row-210))",
    )
    out = out.replace(
        "reunion index (row 189)](appendix/sources.md#row68-row169-ddd-meta-prelude-capstone-reunion-index-row-190)",
        "reunion index (row 209)](appendix/sources.md#row68-row190-ddd-meta-prelude-capstone-reunion-index-row-209)",
    )
    out = out.replace(
        "verified midpoint meta prelude capstone closure on the full capstone path (row 188)",
        "verified midpoint meta prelude capstone closure on the full capstone path (row 208)",
    )
    out = out.replace("row 208 closed midpoint", "row 208 closed midpoint")
    out = out.replace(
        "row 190 names **Row 68 → Row 170 Row 68 → Row 50 DDD meta prelude capstone reunion**; row 210 names",
        "row 189 names **Row 68 → Row 169 Row 68 → Row 49 taxonomy meta prelude capstone reunion**; row 209 names",
    )
    return out


def t190_to_210(text: str) -> str:
    return bump190_to_210(text)


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    memory = (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text()

    start = preface.index("### Row 190 skill checkpoint")
    end = preface.index("\n\n### Row 191 skill checkpoint", start)
    row210_preface = t190_to_210(preface[start:end]) + "\n\n"

    spec190 = importlib.util.spec_from_file_location("add190", ROOT / "scripts/add-row-190.py")
    add190 = importlib.util.module_from_spec(spec190)
    spec190.loader.exec_module(add190)
    prologue_stitch = t190_to_210(add190.PROLOGUE_STITCH.strip()) + "\n\n"

    prologue_compass = (
        "| Row 68 → Row 189 Row 68 → Row 49 taxonomy meta prelude capstone reunion (row 209) | "
        "[Preface: row 209 skill checkpoint](../preface.md#skill-navigation-row-210) · "
        "[Row 68 → Row 190 DDD meta prelude capstone reunion index](../appendix/sources.md#row68-row190-ddd-meta-prelude-capstone-reunion-index-row-209) · "
        "[memory sheet row 210 baby picture](../appendix/memory-sheet.md#row-210-baby-picture-row68-row190-ddd-meta-prelude-capstone-reunion) · "
        "[prologue row 210 preview row](#prologue-preview-row-210); [prologue row 210 closing stitch](#row-210-closing-stitch); "
        "[epilogue row 210 closing loop](../epilogue/multiscale.md#row-210-closing-loop) — "
        "read row 68 gate + row 208 or row 189 midpoint meta prelude capstone / taxonomy meta prelude gate + VII.0 Bridge → opening hinge → VII.1 taxonomy + row 49 meta aloud "
        "when forest landing is clean on the full capstone path but Burgers circuits feel like Defects Notes homework after verified midpoint meta prelude capstone on the full capstone path |\n"
    )

    prologue_preview = (
        '| <span id="prologue-preview-row-210"></span>Row 209 preview (Row 68 → Row 189 Row 68 → Row 49 taxonomy meta prelude capstone reunion) | '
        "Explain why midpoint closure (row 68) and VII.0 → VII.1 meta (row 49) must be read together with the Bridge → Burgers taxonomy chain after verified midpoint meta prelude capstone on the full capstone path before forest landing and dimension tables feel like separate courses | "
        'One sentence: "read row 68 gate + row 208 or row 189 midpoint meta prelude capstone / taxonomy meta prelude gate + VII.0 Bridge → opening hinge → VII.1 taxonomy + row 49 meta aloud when forest landing is clean on the full capstone path but Burgers circuits feel like Defects Notes homework after verified midpoint meta prelude capstone on the full capstone path" — '
        "[preface row 210 skill checkpoint](../preface.md#skill-navigation-row-210); [prologue row 210 closing stitch](#row-210-closing-stitch); "
        "[Row 68 → Row 190 reunion index](../appendix/sources.md#row68-row190-ddd-meta-prelude-capstone-reunion-index-row-209); "
        "[memory sheet row 210 baby picture](../appendix/memory-sheet.md#row-210-baby-picture-row68-row190-ddd-meta-prelude-capstone-reunion); "
        "[VII.0 Bridge](../part07-defects/00-opening.md#bridge); "
        "[VII.0 opening hinge to VII.1](../part07-defects/00-opening.md#opening-hinge-vii0-to-vii1); "
        "[preface row 49 skill checkpoint](../preface.md#skill-navigation-row-49); "
        "[preface row 208 skill checkpoint](../preface.md#skill-navigation-row-208); "
        "[epilogue row 210 closing loop](../epilogue/multiscale.md#row-210-closing-loop) |\n"
    )

    row190_loop_anchor = (
        "### Row 190 closing loop (Row 68 → Row 190 Row 68 → Row 50 "
        "DDD meta prelude capstone reunion) {#row-190-closing-loop}"
    )
    row191_loop_end = (
        "### Row 171 closing loop (Row 68 → Row 171 Row 68 → Row 51 "
        "homogenization meta prelude capstone reunion) {#row-191-closing-loop}"
    )
    if row190_loop_anchor not in epilogue:
        row190_loop_anchor = (
            "### Row 190 closing loop (Row 68 → Row 170 Row 68 → Row 50 "
            "DDD meta prelude capstone reunion) {#row-190-closing-loop}"
        )
    epilogue_loop = t190_to_210(
        row190_loop_anchor
        + epilogue.split(row190_loop_anchor, 1)[1].split(row191_loop_end, 1)[0]
    )

    src190_header = (
        "## Row 68 → Row 170 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 190)"
    )
    next191_header = (
        "## Row 68 → Row 171 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 191)"
    )
    sources_index = t190_to_210(sources.split(src190_header, 1)[1].split(next191_header, 1)[0])
    sources_index = (
        "## Row 68 → Row 190 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 210) "
        "{#row68-row190-ddd-meta-prelude-capstone-reunion-index-row-210}"
        + sources_index
    )

    sources_table = next(
        line for line in sources.splitlines() if line.startswith("| 190 | Row 68 → Row 170")
    )
    sources_table = (
        t190_to_210(sources_table).replace("| 190 | Row 68 → Row 190", "| 210 | Row 68 → Row 190", 1)
        + "\n"
    )

    memory_table = next(
        line for line in memory.splitlines() if line.startswith("| 190 | Meta |")
    )
    memory_table = t190_to_210(memory_table).replace("| 190 | Meta |", "| 210 | Meta |", 1) + "\n"

    baby_start = "### Row 190 baby picture"
    baby_end = "### Row 191 baby picture"
    if baby_start not in memory:
        baby_start = "### Row 170 baby picture"
        baby_end = "### Row 171 baby picture"
    memory_baby = t190_to_210(
        baby_start + memory.split(baby_start, 1)[1].split(baby_end, 1)[0]
    )
    memory_baby = memory_baby.replace(
        "### Row 210 baby picture — read",
        "### Row 210 baby picture {#row-210-baby-picture-row68-row190-ddd-meta-prelude-capstone-reunion} — read",
        1,
    )
    if "{#row-210-baby-picture" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 210 baby picture",
            "### Row 210 baby picture {#row-210-baby-picture-row68-row190-ddd-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row210_preface": row210_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW209_TAIL_OLD = (
    "When row 209 is complete, proceed to [row 210](preface.md#skill-navigation-row-210) when taxonomy meta prelude capstone is clean but DDD meta prelude capstone still lags after verified Burgers closure on the full capstone path, to [row 190](preface.md#skill-navigation-row-170) when taxonomy meta prelude capstone is clean but DDD meta prelude capstone still lags after verified Burgers closure on the opening-hinge capstone path alone, to [row 170](preface.md#skill-navigation-row-150) for the Row 68 ↔ Row 50 DDD meta audit on the opening-hinge prelude path alone, to [row 169](preface.md#skill-navigation-row-169) for the Row 68 ↔ Row 49 meta audit on the opening-hinge prelude path alone, to [row 189](preface.md#skill-navigation-row-209) when taxonomy meta prelude capstone still lags after verified midpoint meta prelude capstone on the opening-hinge capstone path alone, to [row 208](preface.md#skill-navigation-row-208) when midpoint meta prelude capstone still lags after verified part-boundary meta prelude capstone on the full capstone path, to [row 89](preface.md#skill-navigation-row-89) for the Row 68 ↔ Row 49 taxonomy opening prelude audit alone, to [row 49](preface.md#skill-navigation-row-49) for the VII.0 → VII.1 meta audit alone, to [row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, or extend prose only under `writings/` then sync."
)
ROW209_TAIL_NEW = (
    "When row 209 is complete, proceed to [row 210](preface.md#skill-navigation-row-210) when taxonomy meta prelude capstone is clean but DDD meta prelude capstone still lags after verified Burgers closure on the full capstone path, to [row 190](preface.md#skill-navigation-row-190) when taxonomy meta prelude capstone is clean but DDD meta prelude capstone still lags after verified Burgers closure on the opening-hinge capstone path alone, to [row 170](preface.md#skill-navigation-row-170) for the Row 68 ↔ Row 50 DDD meta audit on the opening-hinge prelude path alone, to [row 169](preface.md#skill-navigation-row-169) for the Row 68 ↔ Row 49 meta audit on the opening-hinge prelude path alone, to [row 189](preface.md#skill-navigation-row-189) when taxonomy meta prelude capstone still lags after verified midpoint meta prelude capstone on the opening-hinge capstone path alone, to [row 208](preface.md#skill-navigation-row-208) when midpoint meta prelude capstone still lags after verified part-boundary meta prelude capstone on the full capstone path, to [row 89](preface.md#skill-navigation-row-89) for the Row 68 ↔ Row 49 taxonomy opening prelude audit alone, to [row 49](preface.md#skill-navigation-row-49) for the VII.0 → VII.1 meta audit alone, to [row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, or extend prose only under `writings/` then sync."
)

ROW209_EPILOGUE_OLD = (
    "Proceed to [row 190](#row-190-closing-loop) when row 68 closed but DDD meta prelude capstone still lags after row 189 on the full capstone path,"
)
ROW209_EPILOGUE_NEW = (
    "Proceed to [row 210](#row-210-closing-loop) when row 68 closed but DDD meta prelude capstone still lags after row 209 on the full capstone path,"
)

ROW209_BABY_OLD = (
    "when opening [row 209](preface.md#skill-navigation-row-210) before row 49 closes on the full capstone path"
)
ROW209_BABY_NEW = (
    "when opening [row 209](preface.md#skill-navigation-row-210) before row 49 closes on the full capstone path"
)

ROW209_STITCH_OLD = (
    "before row 209 taxonomy meta prelude capstone reunion opens on the full capstone path."
)
ROW209_STITCH_NEW = (
    "before row 211 homogenization meta prelude capstone reunion opens on the full capstone path."
)


def main() -> None:
    b = _build_blocks()

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "### Row 210 skill checkpoint" in preface:
        print("preface: row 210 already present")
    else:
        if "### Row 209 skill checkpoint" not in preface:
            raise SystemExit("row 209 must exist before row 210")
        if ROW209_TAIL_OLD in preface:
            preface = preface.replace(ROW209_TAIL_OLD, ROW209_TAIL_NEW, 1)
        preface = preface.replace(copper, "\n" + b["row210_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 210")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "**Row 210 closing stitch" not in prologue:
        needle = "| Row 68 → Row 189 Row 68 → Row 49 taxonomy meta prelude capstone reunion (row 209) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 209 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 210 closing stitch" not in prologue:
            prologue = prologue.replace(
                "**Row 209 closing stitch",
                b["prologue_stitch"] + "**Row 209 closing stitch",
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-209"></span>Row 209 preview'
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW209_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW209_STITCH_OLD, ROW209_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 210")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "### Row 210 closing loop" not in epilogue:
        if ROW209_EPILOGUE_OLD not in epilogue:
            alt_old = (
                "Proceed to [row 189](#row-190-closing-loop) when row 68 closed but taxonomy meta prelude capstone still lags after row 188 on the full capstone path,"
            )
            alt_new = (
                "Proceed to [row 209](#row-210-closing-loop) when row 68 closed but taxonomy meta prelude capstone still lags after row 208 on the full capstone path,"
            )
            if alt_old in epilogue:
                epilogue = epilogue.replace(alt_old, alt_new, 1)
            elif ROW209_EPILOGUE_OLD in epilogue:
                epilogue = epilogue.replace(ROW209_EPILOGUE_OLD, ROW209_EPILOGUE_NEW, 1)
        else:
            epilogue = epilogue.replace(ROW209_EPILOGUE_OLD, ROW209_EPILOGUE_NEW, 1)
        marker = (
            "### Row 190 closing loop (Row 68 → Row 190 Row 68 → Row 50 "
            "DDD meta prelude capstone reunion) {#row-190-closing-loop}"
        )
        if marker not in epilogue:
            marker = (
                "### Row 190 closing loop (Row 68 → Row 170 Row 68 → Row 50 "
                "DDD meta prelude capstone reunion) {#row-190-closing-loop}"
            )
        if marker not in epilogue:
            raise SystemExit("epilogue row 190 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 210")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row190-ddd-meta-prelude-capstone-reunion-index-row-210" not in sources:
        sources = sources.replace(
            "| 190 | Row 68 → Row 170 Row 68 → Row 50 DDD meta prelude capstone",
            b["sources_table"] + "| 190 | Row 68 → Row 170 Row 68 → Row 50 DDD meta prelude capstone",
            1,
        )
        sources = sources.replace(
            src190_header := (
                "## Row 68 → Row 170 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 190)"
            ),
            b["sources_index"] + src190_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 210")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-210-baby-picture-row68-row190" not in memory:
        memory = memory.replace(
            "| 189 | Meta | [Row 68 → Row 170 DDD meta prelude capstone reunion index]",
            b["memory_table"] + "| 189 | Meta | [Row 68 → Row 170 DDD meta prelude capstone reunion index]",
            1,
        )
        baby_insert = "### Row 190 baby picture"
        if baby_insert not in memory:
            baby_insert = "### Row 170 baby picture"
        memory = memory.replace(
            baby_insert,
            b["memory_baby"] + baby_insert,
            1,
        )
        memory_path.write_text(memory)
        print("memory-sheet: added row 210")


if __name__ == "__main__":
    main()
