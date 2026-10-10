#!/usr/bin/env python3
"""Add row 271 meta-stitch (Row 68 → Row 251 ↔ Row 51 homogenization meta prelude capstone reunion, full capstone path)."""
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


def t251_to_271(text: str) -> str:
    return bump_meta_plus20(text)


def _load_add251():
    spec = importlib.util.spec_from_file_location("add251", ROOT / "scripts/add-row-251.py")
    add251 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add251)
    return add251


def _build_blocks() -> dict[str, str]:
    add251 = _load_add251()
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 251 skill checkpoint")
    end = preface.index("\n\n## The copper wire through the book", start)
    row271_preface = t251_to_271(preface[start:end]) + "\n\n"

    b251 = add251._build_blocks()
    prologue_stitch = t251_to_271(b251["prologue_stitch"].strip()) + "\n\n"
    prologue_compass = t251_to_271(b251["prologue_compass"])
    prologue_preview = t251_to_271(b251["prologue_preview"])

    epilogue_loop = t251_to_271(b251["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace("{#row-251-closing-loop}", "{#row-271-closing-loop}", 1)
    epilogue_loop = re.sub(
        r"### Row 271 closing loop \(Row 68 → Row 271 Row 68 → Row 51 homogenization meta prelude capstone reunion\)",
        "### Row 271 closing loop (Row 68 → Row 251 Row 68 → Row 51 homogenization meta prelude capstone reunion)",
        epilogue_loop,
        count=1,
    )
    epilogue_loop = epilogue_loop.replace(
        "Row 251 closes the **homogenization meta prelude capstone",
        "Row 271 closes the **homogenization meta prelude capstone",
        1,
    )
    epilogue_loop = epilogue_loop.replace(
        "[memory sheet row 251]",
        "[memory sheet row 271]",
        1,
    )
    epilogue_loop = epilogue_loop.replace(
        "Prologue preview ([row 251]",
        "Prologue preview ([row 271]",
        1,
    )
    epilogue_loop = epilogue_loop.replace(
        "[Preface row 251]",
        "[Preface row 271]",
        1,
    )
    epilogue_loop = epilogue_loop.replace(
        "skill-navigation-row-210)",
        "skill-navigation-row-270)",
        1,
    )
    epilogue_loop = epilogue_loop.replace(
        "### Row 251 closing loop (Row 68 → Row 251 Row 68 → Row 51 homogenization meta prelude capstone reunion) {#row-271-closing-loop}",
        "### Row 271 closing loop (Row 68 → Row 251 Row 68 → Row 51 homogenization meta prelude capstone reunion) {#row-271-closing-loop}",
        1,
    )

    sources_index = t251_to_271(b251["sources_index"])
    sources_index = sources_index.replace(
        "(row 251) {#row68-row251-homogenization-meta-prelude-capstone-reunion-index-row-251}",
        "(row 271) {#row68-row251-homogenization-meta-prelude-capstone-reunion-index-row-271}",
        1,
    )
    sources_index = sources_index.replace(
        "row68-row251-homogenization-meta-prelude-capstone-reunion-index-row-251",
        "row68-row251-homogenization-meta-prelude-capstone-reunion-index-row-271",
    )

    sources_table = t251_to_271(b251["sources_table"])
    sources_table = sources_table.replace("| 251 | Row 68 → Row 231", "| 271 | Row 68 → Row 251", 1)

    memory_table = t251_to_271(b251["memory_table"])
    memory_table = memory_table.replace("| 251 | Meta |", "| 271 | Meta |", 1)

    memory_baby = t251_to_271(b251["memory_baby"])
    if "{#row-271-baby-picture-row68-row251" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 271 baby picture",
            "### Row 271 baby picture {#row-271-baby-picture-row68-row251-homogenization-meta-prelude-capstone-reunion}",
            1,
        )
        memory_baby = memory_baby.replace(
            "### Row 251 baby picture {#row-251-baby-picture-row68-row251-homogenization-meta-prelude-capstone-reunion}",
            "### Row 271 baby picture {#row-271-baby-picture-row68-row251-homogenization-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row271_preface": row271_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW270_EPILOGUE_OLD = (
    "Proceed to [row 271](#row-251-closing-loop) when row 68 closed but homogenization meta prelude capstone still lags after row 270 on the full capstone path,"
)
ROW270_EPILOGUE_NEW = (
    "Proceed to [row 271](#row-271-closing-loop) when row 68 closed but homogenization meta prelude capstone still lags after row 270 on the full capstone path,"
)

ROW270_STITCH_OLD = (
    "before row 271 homogenization meta prelude capstone reunion opens on the full capstone path."
)
ROW270_STITCH_NEW = (
    "before row 272 atomistic meta prelude capstone reunion opens on the full capstone path."
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 271 skill checkpoint" in preface:
        print("preface: row 271 already present")
    else:
        if "### Row 251 skill checkpoint" not in preface:
            raise SystemExit("row 251 must exist before row 271")
        preface = preface.replace(copper, "\n" + b["row271_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 271")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-271" not in prologue:
        needle = (
            "| Row 68 → Row 250 Row 68 → Row 50 DDD meta prelude capstone reunion (row 270) | "
            "[Preface: row 270 skill checkpoint](../preface.md#skill-navigation-row-270)"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 270 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 271 closing stitch" not in prologue:
            prologue = prologue.replace(
                "**Row 270 closing stitch",
                b["prologue_stitch"] + "**Row 270 closing stitch",
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-270"></span>Row 270 preview'
        if preview_anchor in prologue and '<span id="prologue-preview-row-271">' not in prologue:
            prologue = prologue.replace(
                preview_anchor, b["prologue_preview"].strip() + "\n" + preview_anchor, 1
            )
        if ROW270_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW270_STITCH_OLD, ROW270_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 271")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if ROW270_EPILOGUE_OLD in epilogue:
        epilogue = epilogue.replace(ROW270_EPILOGUE_OLD, ROW270_EPILOGUE_NEW, 1)
    marker = (
        "### Row 251 closing loop (Row 68 → Row 251 Row 68 → Row 51 "
        "homogenization meta prelude capstone reunion) {#row-251-closing-loop}"
    )
    if marker not in epilogue:
        raise SystemExit("epilogue row 251 insert anchor not found")
    canonical_hdr = (
        "### Row 271 closing loop (Row 68 → Row 251 Row 68 → Row 51 homogenization meta prelude capstone reunion)"
    )
    if canonical_hdr not in epilogue.split(marker, 1)[0][-12000:]:
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 271")
    else:
        print("epilogue: row 271 already present at anchor")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row251-homogenization-meta-prelude-capstone-reunion-index-row-271" not in sources:
        table_needle = (
            "| 251 | Row 68 → Row 231 Row 68 → Row 51 homogenization meta prelude capstone "
            "(midpoint prelude gate ↔ DDD meta prelude capstone on full capstone path ↔ row 51 meta) |"
        )
        if table_needle not in sources:
            table_needle = (
                "| 211 | Row 68 → Row 211 Row 68 → Row 51 homogenization meta prelude capstone "
                "(midpoint prelude gate ↔ DDD meta prelude capstone on full capstone path ↔ row 51 meta) |"
            )
        sources = sources.replace(
            table_needle,
            b["sources_table"] + table_needle,
            1,
        )
        src251_header = (
            "## Row 68 → Row 231 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 251)"
        )
        if src251_header not in sources:
            src251_header = (
                "## Row 68 → Row 231 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 251) "
                "{#row68-row251-homogenization-meta-prelude-capstone-reunion-index-row-251}"
            )
        sources = sources.replace(src251_header, b["sources_index"] + src251_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 271")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-271-baby-picture-row68-row251" not in memory:
        memory = memory.replace(
            "| 251 | Meta | [Row 68 → Row 231 homogenization meta prelude capstone reunion index]",
            b["memory_table"] + "| 251 | Meta | [Row 68 → Row 231 homogenization meta prelude capstone reunion index]",
            1,
        )
        inserted = False
        for baby_anchor in (
            "### Row 251 baby picture (Row 68 → Row 251 Row 68 → Row 51 homogenization meta prelude capstone reunion) {#row-251-baby-picture-row68-row251-homogenization-meta-prelude-capstone-reunion}",
            "{#row-251-baby-picture-row68-row251-homogenization-meta-prelude-capstone-reunion}",
            "### Row 231 baby picture (Row 68 → Row 211 Row 68 → Row 51 homogenization meta prelude capstone reunion) {#row-231-baby-picture-row68-row211-homogenization-meta-prelude-capstone-reunion}",
            "### Row 270 baby picture {#row-270-baby-picture-row68-row250-ddd-meta-prelude-capstone-reunion}",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 271")


if __name__ == "__main__":
    main()
