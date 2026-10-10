#!/usr/bin/env python3
"""Add row 270 meta-stitch (Row 68 → Row 250 ↔ Row 50 DDD meta prelude capstone reunion, full capstone path)."""
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


def t250_to_270(text: str) -> str:
    return bump_meta_plus20(text)


def _load_add250():
    spec = importlib.util.spec_from_file_location("add250", ROOT / "scripts/add-row-250.py")
    add250 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add250)
    return add250


def _build_blocks() -> dict[str, str]:
    add250 = _load_add250()
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 250 skill checkpoint")
    end = preface.index("\n\n## The copper wire through the book", start)
    row270_preface = t250_to_270(preface[start:end]) + "\n\n"

    b250 = add250._build_blocks()
    prologue_stitch = t250_to_270(b250["prologue_stitch"].strip()) + "\n\n"
    prologue_compass = t250_to_270(b250["prologue_compass"])
    prologue_preview = t250_to_270(b250["prologue_preview"])

    epilogue_loop = t250_to_270(b250["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace("{#row-250-closing-loop}", "{#row-270-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 250 closing loop (Row 68 → Row 230 Row 68 → Row 50 DDD meta prelude capstone reunion)",
        "### Row 270 closing loop (Row 68 → Row 250 Row 68 → Row 50 DDD meta prelude capstone reunion)",
        1,
    )

    sources_index = t250_to_270(b250["sources_index"])
    sources_index = sources_index.replace(
        "(row 250) {#row68-row230-ddd-meta-prelude-capstone-reunion-index-row-250}",
        "(row 270) {#row68-row250-ddd-meta-prelude-capstone-reunion-index-row-270}",
        1,
    )
    sources_index = sources_index.replace(
        "row68-row230-ddd-meta-prelude-capstone-reunion-index-row-250",
        "row68-row250-ddd-meta-prelude-capstone-reunion-index-row-270",
    )

    sources_table = t250_to_270(b250["sources_table"])
    sources_table = sources_table.replace("| 250 | Row 68 → Row 230", "| 270 | Row 68 → Row 250", 1)

    memory_table = t250_to_270(b250["memory_table"])
    memory_table = memory_table.replace("| 250 | Meta |", "| 270 | Meta |", 1)

    memory_baby = t250_to_270(b250["memory_baby"])
    if "{#row-270-baby-picture-row68-row250" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 270 baby picture",
            "### Row 270 baby picture {#row-270-baby-picture-row68-row250-ddd-meta-prelude-capstone-reunion}",
            1,
        )
        memory_baby = memory_baby.replace(
            "### Row 250 baby picture {#row-250-baby-picture-row68-row230-ddd-meta-prelude-capstone-reunion}",
            "### Row 270 baby picture {#row-270-baby-picture-row68-row250-ddd-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row270_preface": row270_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW269_EPILOGUE_OLD = (
    "Proceed to [row 270](#row-250-closing-loop) when row 68 closed but DDD meta prelude capstone still lags after row 269 on the full capstone path,"
)
ROW269_EPILOGUE_NEW = (
    "Proceed to [row 270](#row-270-closing-loop) when row 68 closed but DDD meta prelude capstone still lags after row 269 on the full capstone path,"
)

ROW269_STITCH_OLD = (
    "before row 270 DDD meta prelude capstone reunion opens on the full capstone path."
)
ROW269_STITCH_NEW = (
    "before row 271 homogenization meta prelude capstone reunion opens on the full capstone path."
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 270 skill checkpoint" in preface:
        print("preface: row 270 already present")
    else:
        if "### Row 250 skill checkpoint" not in preface:
            raise SystemExit("row 250 must exist before row 270")
        preface = preface.replace(copper, "\n" + b["row270_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 270")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-270" not in prologue:
        needle = (
            "| Row 68 → Row 249 Row 68 → Row 49 taxonomy meta prelude capstone reunion (row 269) | "
            "[Preface: row 269 skill checkpoint](../preface.md#skill-navigation-row-269)"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 269 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 270 closing stitch" not in prologue:
            prologue = prologue.replace(
                "**Row 269 closing stitch",
                b["prologue_stitch"] + "**Row 269 closing stitch",
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-269"></span>Row 269 preview'
        if preview_anchor in prologue and '<span id="prologue-preview-row-270">' not in prologue:
            prologue = prologue.replace(
                preview_anchor, b["prologue_preview"].strip() + "\n" + preview_anchor, 1
            )
        if ROW269_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW269_STITCH_OLD, ROW269_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 270")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if ROW269_EPILOGUE_OLD in epilogue:
        epilogue = epilogue.replace(ROW269_EPILOGUE_OLD, ROW269_EPILOGUE_NEW, 1)
    marker = (
        "### Row 250 closing loop (Row 68 → Row 230 Row 68 → Row 50 "
        "DDD meta prelude capstone reunion) {#row-250-closing-loop}"
    )
    if marker not in epilogue:
        raise SystemExit("epilogue row 250 insert anchor not found")
    canonical_hdr = "### Row 270 closing loop (Row 68 → Row 250 Row 68 → Row 50 DDD meta prelude capstone reunion)"
    if canonical_hdr not in epilogue.split(marker, 1)[0][-12000:]:
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 270")
    else:
        print("epilogue: row 270 already present at anchor")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row250-ddd-meta-prelude-capstone-reunion-index-row-270" not in sources:
        sources = sources.replace(
            "| 250 | Row 68 → Row 230 Row 68 → Row 50 DDD meta prelude capstone",
            b["sources_table"] + "| 250 | Row 68 → Row 230 Row 68 → Row 50 DDD meta prelude capstone",
            1,
        )
        src250_header = (
            "## Row 68 → Row 230 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 250)"
        )
        if src250_header not in sources:
            src250_header = (
                "## Row 68 → Row 230 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 250) "
                "{#row68-row230-ddd-meta-prelude-capstone-reunion-index-row-250}"
            )
        sources = sources.replace(src250_header, b["sources_index"] + src250_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 270")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-270-baby-picture-row68-row250" not in memory:
        memory = memory.replace(
            "| 250 | Meta | [Row 68 → Row 230 DDD meta prelude capstone reunion index]",
            b["memory_table"] + "| 250 | Meta | [Row 68 → Row 230 DDD meta prelude capstone reunion index]",
            1,
        )
        inserted = False
        for baby_anchor in (
            "### Row 250 baby picture {#row-250-baby-picture-row68-row230-ddd-meta-prelude-capstone-reunion}",
            "### Row 269 baby picture {#row-269-baby-picture-row68-row249-taxonomy-meta-prelude-capstone-reunion}",
            "### Row 230 baby picture {#row-230-baby-picture-row68-row210-ddd-meta-prelude-capstone-reunion}",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 270")


if __name__ == "__main__":
    main()
