#!/usr/bin/env python3
"""Add row 229 meta-stitch (Row 68 → Row 209 ↔ Row 49 taxonomy meta prelude capstone reunion, full capstone path)."""
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


def t209_to_229(text: str) -> str:
    return bump_meta_plus20(text)


def _load_add209():
    spec = importlib.util.spec_from_file_location("add209", ROOT / "scripts/add-row-209.py")
    add209 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add209)
    return add209


def _build_blocks() -> dict[str, str]:
    add209 = _load_add209()
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 209 skill checkpoint")
    end = preface.index("\n\n### Row 210 skill checkpoint", start)
    row229_preface = t209_to_229(preface[start:end]) + "\n\n"

    b209 = add209._build_blocks()
    prologue_stitch = t209_to_229(b209["prologue_stitch"].strip()) + "\n\n"
    prologue_compass = t209_to_229(b209["prologue_compass"])
    prologue_preview = t209_to_229(b209["prologue_preview"])

    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    row209_loop_anchor = (
        "### Row 209 closing loop (Row 68 → Row 189 Row 68 → Row 49 "
        "taxonomy meta prelude capstone reunion) {#row-209-closing-loop}"
    )
    row210_loop_end = (
        "### Row 210 closing loop (Row 68 → Row 190 Row 68 → Row 50 "
        "DDD meta prelude capstone reunion) {#row-210-closing-loop}"
    )
    if row209_loop_anchor not in epilogue:
        row209_loop_anchor = (
            "### Row 189 closing loop (Row 68 → Row 169 Row 68 → Row 49 "
            "taxonomy meta prelude capstone reunion) {#row-209-closing-loop}"
        )
    epilogue_loop = t209_to_229(
        row209_loop_anchor + epilogue.split(row209_loop_anchor, 1)[1].split(row210_loop_end, 1)[0]
    )
    epilogue_loop = epilogue_loop.replace("{#row-209-closing-loop}", "{#row-229-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 209 closing loop (Row 68 → Row 189 Row 68 → Row 49 taxonomy meta prelude capstone reunion)",
        "### Row 229 closing loop (Row 68 → Row 209 Row 68 → Row 49 taxonomy meta prelude capstone reunion)",
        1,
    )

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src209_header = (
        "## Row 68 → Row 189 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 209)"
    )
    next210_header = (
        "## Row 68 → Row 190 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 210)"
    )
    i = sources.index(src209_header)
    j = sources.index(next210_header, i + len(src209_header))
    sources_index = t209_to_229(sources[i:j])

    sources_table = t209_to_229(b209["sources_table"])
    sources_table = sources_table.replace("| 209 | Row 68 → Row 189", "| 229 | Row 68 → Row 209", 1)

    memory_table = t209_to_229(b209["memory_table"])
    memory_table = memory_table.replace("| 209 | Meta |", "| 229 | Meta |", 1)

    memory_baby = t209_to_229(b209["memory_baby"])
    if "{#row-229-baby-picture-row68-row209" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 229 baby picture",
            "### Row 229 baby picture {#row-229-baby-picture-row68-row209-taxonomy-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row229_preface": row229_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW228_TAIL_OLD = (
    "When row 228 is complete, proceed to [row 229](preface.md#skill-navigation-row-209) when midpoint meta prelude capstone is clean but taxonomy meta prelude capstone still lags after verified forest landing on the full capstone path, to [row 189](preface.md#skill-navigation-row-149) when midpoint meta prelude capstone is clean but taxonomy meta prelude capstone still lags after verified forest landing on the opening-hinge capstone path alone, to [row 169](preface.md#skill-navigation-row-129) for the Row 68 ↔ Row 49 meta audit on the opening-hinge prelude path alone, to [row 108](preface.md#skill-navigation-row-108) for the Row 68 ↔ Row 48 meta audit on the opening-hinge prelude path alone, to [row 228](preface.md#skill-navigation-row-228) for the Row 68 ↔ Row 48 meta audit on the opening-hinge capstone path alone, to [row 227](preface.md#skill-navigation-row-207) when part-boundary meta prelude capstone still lags after verified Writings canonical meta prelude capstone on the full capstone path, to [row 88](preface.md#skill-navigation-row-88) for the Row 68 ↔ Row 48 opening prelude audit alone, to [row 48](preface.md#skill-navigation-row-48) for the VI.4 → VII.0 meta audit alone, to [row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, or extend prose only under `writings/` then sync."
)
ROW228_TAIL_NEW = (
    "When row 228 is complete, proceed to [row 229](preface.md#skill-navigation-row-229) when midpoint meta prelude capstone is clean but taxonomy meta prelude capstone still lags after verified forest landing on the full capstone path, to [row 209](preface.md#skill-navigation-row-189) when midpoint meta prelude capstone is clean but taxonomy meta prelude capstone still lags after verified forest landing on the opening-hinge capstone path alone, to [row 189](preface.md#skill-navigation-row-149) for the Row 68 ↔ Row 49 meta audit on the opening-hinge prelude path alone, to [row 108](preface.md#skill-navigation-row-108) for the Row 68 ↔ Row 48 meta audit on the opening-hinge prelude path alone, to [row 228](preface.md#skill-navigation-row-228) for the Row 68 ↔ Row 48 meta audit on the opening-hinge capstone path alone, to [row 227](preface.md#skill-navigation-row-227) when part-boundary meta prelude capstone still lags after verified Writings canonical meta prelude capstone on the full capstone path, to [row 88](preface.md#skill-navigation-row-88) for the Row 68 ↔ Row 48 opening prelude audit alone, to [row 48](preface.md#skill-navigation-row-48) for the VI.4 → VII.0 meta audit alone, to [row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, or extend prose only under `writings/` then sync."
)

ROW228_EPILOGUE_OLD = (
    "Proceed to [row 229](#row-209-closing-loop) when row 68 closed but taxonomy meta prelude capstone still lags after row 228 on the full capstone path,"
)
ROW228_EPILOGUE_NEW = (
    "Proceed to [row 229](#row-229-closing-loop) when row 68 closed but taxonomy meta prelude capstone still lags after row 228 on the full capstone path,"
)

ROW228_STITCH_OLD = (
    "before row 229 taxonomy meta prelude capstone reunion opens on the full capstone path."
)
ROW228_STITCH_NEW = (
    "before row 230 DDD meta prelude capstone reunion opens on the full capstone path."
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 229 skill checkpoint" in preface:
        print("preface: row 229 already present")
    else:
        if "### Row 228 skill checkpoint" not in preface:
            raise SystemExit("row 228 must exist before row 229")
        if ROW228_TAIL_OLD in preface:
            preface = preface.replace(ROW228_TAIL_OLD, ROW228_TAIL_NEW, 1)
        elif "skill-navigation-row-209) when midpoint meta prelude capstone is clean but taxonomy" in preface:
            preface = preface.replace(
                "[row 229](preface.md#skill-navigation-row-209)",
                "[row 229](preface.md#skill-navigation-row-229)",
                1,
            )
        preface = preface.replace(copper, "\n" + b["row229_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 229")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-229" not in prologue:
        needle = (
            "| Row 68 → Row 208 Row 68 → Row 48 midpoint meta prelude capstone reunion (row 208) | "
            "[Preface: row 208 skill checkpoint](../preface.md#skill-navigation-row-228)"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 228 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 229 closing stitch" not in prologue:
            prologue = prologue.replace(
                "**Row 228 closing stitch",
                b["prologue_stitch"] + "**Row 228 closing stitch",
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-209"></span>Row 209 preview'
        if preview_anchor in prologue and '<span id="prologue-preview-row-229">' not in prologue:
            prologue = prologue.replace(preview_anchor, b["prologue_preview"].strip() + "\n" + preview_anchor, 1)
        if ROW228_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW228_STITCH_OLD, ROW228_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 229")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "{#row-229-closing-loop}" not in epilogue or "### Row 229 closing loop" not in epilogue:
        if ROW228_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW228_EPILOGUE_OLD, ROW228_EPILOGUE_NEW, 1)
        marker = (
            "### Row 209 closing loop (Row 68 → Row 189 Row 68 → Row 49 "
            "taxonomy meta prelude capstone reunion) {#row-209-closing-loop}"
        )
        if marker not in epilogue:
            marker = (
                "### Row 189 closing loop (Row 68 → Row 169 Row 68 → Row 49 "
                "taxonomy meta prelude capstone reunion) {#row-209-closing-loop}"
            )
        if marker not in epilogue:
            raise SystemExit("epilogue row 209 insert anchor not found")
        if "### Row 229 closing loop" not in epilogue:
            epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 229")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row209-taxonomy-meta-prelude-capstone-reunion-index-row-229" not in sources:
        sources = sources.replace(
            "| 209 | Row 68 → Row 189 Row 68 → Row 49 taxonomy meta prelude capstone",
            b["sources_table"] + "| 209 | Row 68 → Row 189 Row 68 → Row 49 taxonomy meta prelude capstone",
            1,
        )
        src209_header = (
            "## Row 68 → Row 189 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 209)"
        )
        sources = sources.replace(src209_header, b["sources_index"] + src209_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 229")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-229-baby-picture-row68-row209" not in memory:
        memory = memory.replace(
            "| 209 | Meta | [Row 68 → Row 189 taxonomy meta prelude capstone reunion index]",
            b["memory_table"] + "| 209 | Meta | [Row 68 → Row 189 taxonomy meta prelude capstone reunion index]",
            1,
        )
        inserted = False
        for baby_anchor in (
            "### Row 227 baby picture {#row-227-baby-picture-row68-row207-part-boundary-meta-prelude-capstone-reunion}",
            "### Row 228 baby picture {#row-228-baby-picture-row68-row208-midpoint-meta-prelude-capstone-reunion}",
            "### Row 209 baby picture {#row-209-baby-picture-row68-row189-taxonomy-meta-prelude-capstone-reunion}",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 229")


if __name__ == "__main__":
    main()
