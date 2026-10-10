#!/usr/bin/env python3
"""Add row 251 meta-stitch (Row 68 → Row 231 ↔ Row 51 homogenization meta prelude capstone reunion, full capstone path)."""
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


def t231_to_251(text: str) -> str:
    return bump_meta_plus20(text)


def _load_add231():
    spec = importlib.util.spec_from_file_location("add231", ROOT / "scripts/add-row-231.py")
    add231 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add231)
    return add231


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 231 skill checkpoint")
    end = preface.index("\n\n### Row 232 skill checkpoint", start)
    row251_preface = t231_to_251(preface[start:end]) + "\n\n"

    add231 = _load_add231()
    b231 = add231._build_blocks()
    prologue_stitch = t231_to_251(b231["prologue_stitch"].strip()) + "\n\n"
    prologue_compass = t231_to_251(b231["prologue_compass"])
    prologue_preview = t231_to_251(b231["prologue_preview"])

    epilogue_loop = t231_to_251(b231["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace("{#row-231-closing-loop}", "{#row-251-closing-loop}", 1)
    epilogue_loop = re.sub(
        r"### Row 251 closing loop \(Row 68 → Row 251 Row 68 → Row 51 homogenization meta prelude capstone reunion\)",
        "### Row 251 closing loop (Row 68 → Row 231 Row 68 → Row 51 homogenization meta prelude capstone reunion)",
        epilogue_loop,
        count=1,
    )
    epilogue_loop = epilogue_loop.replace(
        "Row 231 closes the **homogenization meta prelude capstone",
        "Row 251 closes the **homogenization meta prelude capstone",
        1,
    )

    sources_index = t231_to_251(b231["sources_index"])
    sources_index = sources_index.replace(
        "(row 231) {#row68-row211-homogenization-meta-prelude-capstone-reunion-index-row-231}",
        "(row 251) {#row68-row251-homogenization-meta-prelude-capstone-reunion-index-row-251}",
        1,
    )
    sources_index = sources_index.replace(
        "row68-row211-homogenization-meta-prelude-capstone-reunion-index-row-231",
        "row68-row251-homogenization-meta-prelude-capstone-reunion-index-row-251",
    )

    sources_table = t231_to_251(b231["sources_table"])
    sources_table = sources_table.replace("| 231 | Row 68 → Row 211", "| 251 | Row 68 → Row 231", 1)

    memory_table = t231_to_251(b231["memory_table"])
    memory_table = memory_table.replace("| 231 | Meta |", "| 251 | Meta |", 1)

    memory_baby = t231_to_251(b231["memory_baby"])
    if "{#row-251-baby-picture-row68-row251" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 251 baby picture",
            "### Row 251 baby picture {#row-251-baby-picture-row68-row251-homogenization-meta-prelude-capstone-reunion}",
            1,
        )
        memory_baby = memory_baby.replace(
            "### Row 231 baby picture {#row-231-baby-picture-row68-row211-homogenization-meta-prelude-capstone-reunion}",
            "### Row 251 baby picture {#row-251-baby-picture-row68-row251-homogenization-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row251_preface": row251_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW231_TAIL_OLD = (
    "When row 231 is complete, proceed to [row 232](preface.md#skill-navigation-row-232) when LAMMPS decks feel like AtomModel homework after verified homogenization meta prelude capstone on the full capstone path,"
)
ROW231_TAIL_NEW = (
    "When row 231 is complete, proceed to [row 271](preface.md#skill-navigation-row-271) when homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the full capstone path, "
    "to [row 251](preface.md#skill-navigation-row-251) when homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the opening-hinge capstone path alone, "
    "to [row 232](preface.md#skill-navigation-row-232) when LAMMPS decks feel like AtomModel homework after verified homogenization meta prelude capstone on the full capstone path,"
)

ROW230_STITCH_OLD = (
    "before row 251 homogenization meta prelude capstone reunion opens on the full capstone path."
)
ROW230_STITCH_NEW = (
    "before row 252 atomistic meta prelude capstone reunion opens on the full capstone path."
)


def main() -> None:
    b = _build_blocks()

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 251 skill checkpoint" in preface:
        print("preface: row 251 already present")
    else:
        if "### Row 231 skill checkpoint" not in preface:
            raise SystemExit("row 231 must exist before row 251")
        if ROW231_TAIL_OLD in preface:
            preface = preface.replace(ROW231_TAIL_OLD, ROW231_TAIL_NEW, 1)
        anchor = "### Row 270 skill checkpoint"
        if anchor not in preface:
            raise SystemExit("row 270 anchor not found for row 251 insert")
        preface = preface.replace(anchor, b["row251_preface"] + anchor, 1)
        preface_path.write_text(preface)
        print("preface: added row 251")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-251" not in prologue:
        needle = (
            "| Row 68 → Row 211 Row 68 → Row 51 homogenization meta prelude capstone reunion (row 231) | "
            "[Preface: row 231 skill checkpoint](../preface.md#skill-navigation-row-231)"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 231 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 251 closing stitch" not in prologue:
            prologue = prologue.replace(
                "**Row 231 closing stitch",
                b["prologue_stitch"] + "**Row 231 closing stitch",
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-231"></span>Row 231 preview'
        if preview_anchor in prologue and '<span id="prologue-preview-row-251">' not in prologue:
            prologue = prologue.replace(
                preview_anchor, b["prologue_preview"].strip() + "\n" + preview_anchor, 1
            )
        if ROW230_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW230_STITCH_OLD, ROW230_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 251")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    insert_after = (
        "### Row 231 closing loop (Row 68 → Row 211 Row 68 → Row 51 "
        "homogenization meta prelude capstone reunion) {#row-231-closing-loop}"
    )
    marker = (
        "### Row 211 closing loop (Row 68 → Row 191 Row 68 → Row 51 "
        "homogenization meta prelude capstone reunion) {#row-211-closing-loop}"
    )
    if insert_after not in epilogue:
        raise SystemExit("epilogue row 231 insert anchor not found")
    head, segment = epilogue.split(insert_after, 1)
    canonical_hdr = (
        "### Row 251 closing loop (Row 68 → Row 251 Row 68 → Row 51 homogenization meta prelude capstone reunion)"
    )
    if canonical_hdr not in segment.split(marker, 1)[0][:8000]:
        if marker not in segment:
            raise SystemExit("epilogue row 211 marker not found after row 231")
        segment = segment.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(head + insert_after + segment)
        print("epilogue: added row 251 at capstone anchor")
    else:
        print("epilogue: row 251 already present at anchor")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row251-homogenization-meta-prelude-capstone-reunion-index-row-251" not in sources:
        table_needle = (
            "| 211 | Row 68 → Row 211 Row 68 → Row 51 homogenization meta prelude capstone "
            "(midpoint prelude gate ↔ DDD meta prelude capstone on full capstone path ↔ row 51 meta) |"
        )
        sources = sources.replace(
            table_needle,
            b["sources_table"] + table_needle,
            1,
        )
        src231_header = (
            "## Row 68 → Row 211 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 231)"
        )
        if src231_header not in sources:
            src231_header = (
                "## Row 68 → Row 211 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 231) "
                "{#row68-row211-homogenization-meta-prelude-capstone-reunion-index-row-231}"
            )
        sources = sources.replace(src231_header, b["sources_index"] + src231_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 251")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-251-baby-picture-row68-row251" not in memory:
        memory = memory.replace(
            "| 231 | Meta | [Row 68 → Row 211 homogenization meta prelude capstone reunion index]",
            b["memory_table"] + "| 231 | Meta | [Row 68 → Row 211 homogenization meta prelude capstone reunion index]",
            1,
        )
        inserted = False
        for baby_anchor in (
            "### Row 231 baby picture (Row 68 → Row 211 Row 68 → Row 51 homogenization meta prelude capstone reunion) {#row-231-baby-picture-row68-row211-homogenization-meta-prelude-capstone-reunion}",
            "{#row-231-baby-picture-row68-row211-homogenization-meta-prelude-capstone-reunion}",
            "### Row 270 baby picture {#row-270-baby-picture-row68-row250-ddd-meta-prelude-capstone-reunion}",
            "### Row 250 baby picture {#row-250-baby-picture-row68-row230-ddd-meta-prelude-capstone-reunion}",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 251")


if __name__ == "__main__":
    main()
