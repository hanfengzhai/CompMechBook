#!/usr/bin/env python3
"""Add row 250 meta-stitch (Row 68 → Row 230 ↔ Row 50 DDD meta prelude capstone reunion, full capstone path)."""
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


def t230_to_250(text: str) -> str:
    return bump_meta_plus20(text)


def _load_add230():
    spec = importlib.util.spec_from_file_location("add230", ROOT / "scripts/add-row-230.py")
    add230 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add230)
    return add230


def _build_blocks() -> dict[str, str]:
    add230 = _load_add230()
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 230 skill checkpoint")
    end = preface.index("\n\n### Row 231 skill checkpoint", start)
    row250_preface = t230_to_250(preface[start:end]) + "\n\n"

    b230 = add230._build_blocks()
    prologue_stitch = t230_to_250(b230["prologue_stitch"].strip()) + "\n\n"
    prologue_compass = t230_to_250(b230["prologue_compass"])
    prologue_preview = t230_to_250(b230["prologue_preview"])

    epilogue_loop = t230_to_250(b230["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace("{#row-230-closing-loop}", "{#row-250-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 230 closing loop (Row 68 → Row 210 Row 68 → Row 50 DDD meta prelude capstone reunion)",
        "### Row 250 closing loop (Row 68 → Row 230 Row 68 → Row 50 DDD meta prelude capstone reunion)",
        1,
    )

    sources_index = t230_to_250(b230["sources_index"])
    sources_index = sources_index.replace(
        "(row 230) {#row68-row210-ddd-meta-prelude-capstone-reunion-index-row-230}",
        "(row 250) {#row68-row230-ddd-meta-prelude-capstone-reunion-index-row-250}",
        1,
    )
    sources_index = sources_index.replace(
        "row68-row210-ddd-meta-prelude-capstone-reunion-index-row-230",
        "row68-row230-ddd-meta-prelude-capstone-reunion-index-row-250",
    )

    sources_table = t230_to_250(b230["sources_table"])
    sources_table = sources_table.replace("| 230 | Row 68 → Row 210", "| 250 | Row 68 → Row 230", 1)

    memory_table = t230_to_250(b230["memory_table"])
    memory_table = memory_table.replace("| 230 | Meta |", "| 250 | Meta |", 1)

    memory_baby = t230_to_250(b230["memory_baby"])
    if "{#row-250-baby-picture-row68-row230" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 250 baby picture",
            "### Row 250 baby picture {#row-250-baby-picture-row68-row230-ddd-meta-prelude-capstone-reunion}",
            1,
        )
        memory_baby = memory_baby.replace(
            "### Row 230 baby picture {#row-230-baby-picture-row68-row210-ddd-meta-prelude-capstone-reunion}",
            "### Row 250 baby picture {#row-250-baby-picture-row68-row230-ddd-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row250_preface": row250_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW249_TAIL_OLD = (
    "When row 249 is complete, proceed to [row 250](preface.md#skill-navigation-row-230) when taxonomy meta prelude capstone is clean but DDD meta prelude capstone still lags after verified Burgers closure on the full capstone path,"
)
ROW249_TAIL_NEW = (
    "When row 249 is complete, proceed to [row 270](preface.md#skill-navigation-row-270) when taxonomy meta prelude capstone is clean but DDD meta prelude capstone still lags after verified Burgers closure on the full capstone path, to [row 250](preface.md#skill-navigation-row-250) when taxonomy meta prelude capstone is clean but DDD meta prelude capstone still lags after verified Burgers closure on the opening-hinge capstone path alone,"
)

ROW229_STITCH_OLD = (
    "before row 250 DDD meta prelude capstone reunion opens on the full capstone path."
)
ROW229_STITCH_NEW = (
    "before row 251 homogenization meta prelude capstone reunion opens on the full capstone path."
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 250 skill checkpoint" in preface:
        print("preface: row 250 already present")
    else:
        if "### Row 230 skill checkpoint" not in preface:
            raise SystemExit("row 230 must exist before row 250")
        if ROW249_TAIL_OLD in preface:
            preface = preface.replace(ROW249_TAIL_OLD, ROW249_TAIL_NEW, 1)
        preface = preface.replace(copper, "\n" + b["row250_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 250")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-250" not in prologue:
        needle = (
            "| Row 68 → Row 210 Row 68 → Row 50 DDD meta prelude capstone reunion (row 230) | "
            "[Preface: row 230 skill checkpoint](../preface.md#skill-navigation-row-230)"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 230 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 250 closing stitch" not in prologue:
            prologue = prologue.replace(
                "**Row 230 closing stitch",
                b["prologue_stitch"] + "**Row 230 closing stitch",
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-230"></span>Row 230 preview'
        if preview_anchor in prologue and '<span id="prologue-preview-row-250">' not in prologue:
            prologue = prologue.replace(
                preview_anchor, b["prologue_preview"].strip() + "\n" + preview_anchor, 1
            )
        if ROW229_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW229_STITCH_OLD, ROW229_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 250")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    marker = (
        "### Row 230 closing loop (Row 68 → Row 210 Row 68 → Row 50 "
        "DDD meta prelude capstone reunion) {#row-230-closing-loop}"
    )
    if marker not in epilogue:
        raise SystemExit("epilogue row 230 insert anchor not found")
    if "### Row 250 closing loop (Row 68 → Row 230" not in epilogue.split(marker, 1)[0][-8000:]:
        if marker in epilogue and epilogue.count("{#row-250-closing-loop}") < 2:
            epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
            epilogue_path.write_text(epilogue)
            print("epilogue: added row 250")
    else:
        print("epilogue: row 250 already present")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row230-ddd-meta-prelude-capstone-reunion-index-row-250" not in sources:
        sources = sources.replace(
            "| 230 | Row 68 → Row 210 Row 68 → Row 50 DDD meta prelude capstone",
            b["sources_table"] + "| 230 | Row 68 → Row 210 Row 68 → Row 50 DDD meta prelude capstone",
            1,
        )
        src230_header = (
            "## Row 68 → Row 210 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 230)"
        )
        sources = sources.replace(src230_header, b["sources_index"] + src230_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 250")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-250-baby-picture-row68-row230" not in memory:
        memory = memory.replace(
            "| 230 | Meta | [Row 68 → Row 210 DDD meta prelude capstone reunion index]",
            b["memory_table"] + "| 230 | Meta | [Row 68 → Row 210 DDD meta prelude capstone reunion index]",
            1,
        )
        inserted = False
        for baby_anchor in (
            "### Row 230 baby picture {#row-230-baby-picture-row68-row210-ddd-meta-prelude-capstone-reunion}",
            "### Row 249 baby picture {#row-249-baby-picture-row68-row229-taxonomy-meta-prelude-capstone-reunion}",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 250")


if __name__ == "__main__":
    main()
