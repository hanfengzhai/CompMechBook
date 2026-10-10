#!/usr/bin/env python3
"""Add row 269 meta-stitch (Row 68 → Row 249 ↔ Row 49 taxonomy meta prelude capstone reunion, full capstone path)."""
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


def t229_to_249(text: str) -> str:
    return bump_meta_plus20(text)


def _load_add229():
    spec = importlib.util.spec_from_file_location("add229", ROOT / "scripts/add-row-229.py")
    add229 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add229)
    return add229


def _build_blocks() -> dict[str, str]:
    add229 = _load_add229()
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 229 skill checkpoint")
    end = preface.index("\n\n### Row 230 skill checkpoint", start)
    row249_preface = t229_to_249(preface[start:end]) + "\n\n"

    b229 = add229._build_blocks()
    prologue_stitch = t229_to_249(b229["prologue_stitch"].strip()) + "\n\n"
    prologue_compass = t229_to_249(b229["prologue_compass"])
    prologue_preview = t229_to_249(b229["prologue_preview"])

    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    row209_loop_anchor = (
        "### Row 229 closing loop (Row 68 → Row 209 Row 68 → Row 49 "
        "taxonomy meta prelude capstone reunion) {#row-229-closing-loop}"
    )
    row210_loop_end = (
        "### Row 230 closing loop (Row 68 → Row 210 Row 68 → Row 50 "
        "DDD meta prelude capstone reunion) {#row-230-closing-loop}"
    )
    if row209_loop_anchor not in epilogue:
        row209_loop_anchor = (
            "### Row 209 closing loop (Row 68 → Row 189 Row 68 → Row 49 "
            "taxonomy meta prelude capstone reunion) {#row-229-closing-loop}"
        )
    epilogue_loop = t229_to_249(
        row209_loop_anchor + epilogue.split(row209_loop_anchor, 1)[1].split(row210_loop_end, 1)[0]
    )
    epilogue_loop = epilogue_loop.replace("{#row-229-closing-loop}", "{#row-249-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 229 closing loop (Row 68 → Row 209 Row 68 → Row 49 taxonomy meta prelude capstone reunion)",
        "### Row 249 closing loop (Row 68 → Row 229 Row 68 → Row 49 taxonomy meta prelude capstone reunion)",
        1,
    )

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src209_header = (
        "## Row 68 → Row 209 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 229)"
    )
    next210_header = (
        "## Row 68 → Row 210 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 230)"
    )
    i = sources.index(src209_header)
    j = sources.index(next210_header, i + len(src209_header))
    sources_index = t229_to_249(sources[i:j])

    sources_table = t229_to_249(b229["sources_table"])
    sources_table = sources_table.replace("| 209 | Row 68 → Row 209", "| 229 | Row 68 → Row 229", 1)

    memory_table = t229_to_249(b229["memory_table"])
    memory_table = memory_table.replace("| 209 | Meta |", "| 229 | Meta |", 1)

    memory_baby = t229_to_249(b229["memory_baby"])
    if "{#row-249-baby-picture-row68-row229" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 249 baby picture",
            "### Row 249 baby picture {#row-249-baby-picture-row68-row229-taxonomy-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row249_preface": row249_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW248_TAIL_OLD = (
    "When row 248 is complete, proceed to [row 249](preface.md#skill-navigation-row-229) when midpoint meta prelude capstone is clean but taxonomy meta prelude capstone still lags after verified forest landing on the full capstone path, to [row 209](preface.md#skill-navigation-row-169) when midpoint meta prelude capstone is clean but taxonomy meta prelude capstone still lags after verified forest landing on the opening-hinge capstone path alone, to [row 189](preface.md#skill-navigation-row-149) for the Row 68 ↔ Row 49 meta audit on the opening-hinge prelude path alone, to [row 108](preface.md#skill-navigation-row-108) for the Row 68 ↔ Row 48 meta audit on the opening-hinge prelude path alone, to [row 248](preface.md#skill-navigation-row-248) for the Row 68 ↔ Row 48 meta audit on the opening-hinge capstone path alone, to [row 247](preface.md#skill-navigation-row-227) when part-boundary meta prelude capstone still lags after verified Writings canonical meta prelude capstone on the full capstone path, to [row 88](preface.md#skill-navigation-row-88) for the Row 68 ↔ Row 48 opening prelude audit alone, to [row 48](preface.md#skill-navigation-row-48) for the VI.4 → VII.0 meta audit alone, to [row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, or extend prose only under `writings/` then sync."
)
ROW248_TAIL_NEW = (
    "When row 248 is complete, proceed to [row 249](preface.md#skill-navigation-row-249) when midpoint meta prelude capstone is clean but taxonomy meta prelude capstone still lags after verified forest landing on the full capstone path, to [row 229](preface.md#skill-navigation-row-209) when midpoint meta prelude capstone is clean but taxonomy meta prelude capstone still lags after verified forest landing on the opening-hinge capstone path alone, to [row 209](preface.md#skill-navigation-row-169) for the Row 68 ↔ Row 49 meta audit on the opening-hinge prelude path alone, to [row 108](preface.md#skill-navigation-row-108) for the Row 68 ↔ Row 48 meta audit on the opening-hinge prelude path alone, to [row 248](preface.md#skill-navigation-row-248) for the Row 68 ↔ Row 48 meta audit on the opening-hinge capstone path alone, to [row 247](preface.md#skill-navigation-row-247) when part-boundary meta prelude capstone still lags after verified Writings canonical meta prelude capstone on the full capstone path, to [row 88](preface.md#skill-navigation-row-88) for the Row 68 ↔ Row 48 opening prelude audit alone, to [row 48](preface.md#skill-navigation-row-48) for the VI.4 → VII.0 meta audit alone, to [row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, or extend prose only under `writings/` then sync."
)

ROW248_EPILOGUE_OLD = (
    "Proceed to [row 249](#row-229-closing-loop) when row 68 closed but taxonomy meta prelude capstone still lags after row 248 on the full capstone path,"
)
ROW248_EPILOGUE_NEW = (
    "Proceed to [row 249](#row-249-closing-loop) when row 68 closed but taxonomy meta prelude capstone still lags after row 248 on the full capstone path,"
)

ROW248_STITCH_OLD = (
    "before row 249 taxonomy meta prelude capstone reunion opens on the full capstone path."
)
ROW248_STITCH_NEW = (
    "before row 250 DDD meta prelude capstone reunion opens on the full capstone path."
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 249 skill checkpoint" in preface:
        print("preface: row 249 already present")
    else:
        if "### Row 248 skill checkpoint" not in preface:
            raise SystemExit("row 248 must exist before row 249")
        if ROW248_TAIL_OLD in preface:
            preface = preface.replace(ROW248_TAIL_OLD, ROW248_TAIL_NEW, 1)
        elif "skill-navigation-row-229) when midpoint meta prelude capstone is clean but taxonomy" in preface:
            preface = preface.replace(
                "[row 249](preface.md#skill-navigation-row-229)",
                "[row 249](preface.md#skill-navigation-row-249)",
                1,
            )
        preface = preface.replace(copper, "\n" + b["row249_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 249")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-249" not in prologue:
        needle = (
            "| Row 68 → Row 228 Row 68 → Row 48 midpoint meta prelude capstone reunion (row 248) | "
            "[Preface: row 248 skill checkpoint](../preface.md#skill-navigation-row-248)"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 248 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 249 closing stitch" not in prologue:
            prologue = prologue.replace(
                "**Row 248 closing stitch",
                b["prologue_stitch"] + "**Row 248 closing stitch",
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-248"></span>Row 248 preview'
        if preview_anchor in prologue and '<span id="prologue-preview-row-249">' not in prologue:
            prologue = prologue.replace(preview_anchor, b["prologue_preview"].strip() + "\n" + preview_anchor, 1)
        if ROW248_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW248_STITCH_OLD, ROW248_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 249")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "{#row-249-closing-loop}" not in epilogue or "### Row 249 closing loop" not in epilogue:
        if ROW248_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW248_EPILOGUE_OLD, ROW248_EPILOGUE_NEW, 1)
        marker = (
            "### Row 229 closing loop (Row 68 → Row 209 Row 68 → Row 49 "
            "taxonomy meta prelude capstone reunion) {#row-229-closing-loop}"
        )
        if marker not in epilogue:
            marker = (
                "### Row 209 closing loop (Row 68 → Row 189 Row 68 → Row 49 "
                "taxonomy meta prelude capstone reunion) {#row-229-closing-loop}"
            )
        if marker not in epilogue:
            raise SystemExit("epilogue row 229 insert anchor not found")
        if "### Row 249 closing loop" not in epilogue:
            epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 249")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row229-taxonomy-meta-prelude-capstone-reunion-index-row-249" not in sources:
        sources = sources.replace(
            "| 229 | Row 68 → Row 209 Row 68 → Row 49 taxonomy meta prelude capstone",
            b["sources_table"] + "| 229 | Row 68 → Row 209 Row 68 → Row 49 taxonomy meta prelude capstone",
            1,
        )
        src229_header = (
            "## Row 68 → Row 209 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 229) "
            "{#row68-row209-taxonomy-meta-prelude-capstone-reunion-index-row-229}"
        )
        if src229_header not in sources:
            src229_header = (
                "## Row 68 → Row 209 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 229)"
            )
        sources = sources.replace(src229_header, b["sources_index"] + src229_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 249")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-249-baby-picture-row68-row229" not in memory:
        memory = memory.replace(
            "| 229 | Meta | [Row 68 → Row 209 taxonomy meta prelude capstone reunion index]",
            b["memory_table"] + "| 229 | Meta | [Row 68 → Row 209 taxonomy meta prelude capstone reunion index]",
            1,
        )
        inserted = False
        for baby_anchor in (
            "### Row 247 baby picture {#row-247-baby-picture-row68-row227-part-boundary-meta-prelude-capstone-reunion}",
            "### Row 248 baby picture {#row-248-baby-picture-row68-row228-midpoint-meta-prelude-capstone-reunion}",
            "### Row 229 baby picture {#row-229-baby-picture-row68-row209-taxonomy-meta-prelude-capstone-reunion}",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 249")


if __name__ == "__main__":
    main()
