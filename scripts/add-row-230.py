#!/usr/bin/env python3
"""Add row 230 meta-stitch (Row 68 → Row 210 ↔ Row 50 DDD meta prelude capstone reunion, full capstone path)."""
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


def t210_to_230(text: str) -> str:
    return bump_meta_plus20(text)


def _load_add210():
    spec = importlib.util.spec_from_file_location("add210", ROOT / "scripts/add-row-210.py")
    add210 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add210)
    return add210


def _build_blocks() -> dict[str, str]:
    add210 = _load_add210()
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 210 skill checkpoint")
    end = preface.index("\n\n### Row 211 skill checkpoint", start)
    row230_preface = t210_to_230(preface[start:end]) + "\n\n"

    b210 = add210._build_blocks()
    prologue_stitch = t210_to_230(b210["prologue_stitch"].strip()) + "\n\n"
    prologue_compass = (
        "| Row 68 → Row 210 Row 68 → Row 50 DDD meta prelude capstone reunion (row 230) | "
        "[Preface: row 230 skill checkpoint](../preface.md#skill-navigation-row-230) · "
        "[Row 68 → Row 210 DDD meta prelude capstone reunion index](../appendix/sources.md#row68-row210-ddd-meta-prelude-capstone-reunion-index-row-230) · "
        "[memory sheet row 230 baby picture](../appendix/memory-sheet.md#row-230-baby-picture-row68-row210-ddd-meta-prelude-capstone-reunion) · "
        "[prologue row 230 preview row](#prologue-preview-row-230); [prologue row 230 closing stitch](#row-230-closing-stitch); "
        "[epilogue row 230 closing loop](../epilogue/multiscale.md#row-230-closing-loop) — "
        "read row 68 gate + row 229 or row 210 taxonomy meta prelude capstone / DDD meta prelude gate + VII.1 Bridge → opening hinge → VII.2 Peach–Köhler + row 50 meta aloud "
        "when Burgers taxonomy is clean on the full capstone path but OpenDiS exports feel like Defects Notes homework after verified taxonomy meta prelude capstone on the full capstone path |\n"
    )
    prologue_preview = t210_to_230(b210["prologue_preview"])

    epilogue_loop = t210_to_230(b210["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace("{#row-210-closing-loop}", "{#row-230-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 210 closing loop (Row 68 → Row 190 Row 68 → Row 50 DDD meta prelude capstone reunion)",
        "### Row 230 closing loop (Row 68 → Row 210 Row 68 → Row 50 DDD meta prelude capstone reunion)",
        1,
    )

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src210_header = (
        "## Row 68 → Row 190 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 210)"
    )
    next211_header = (
        "## Row 68 → Row 191 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 211)"
    )
    i = sources.index(src210_header)
    j = sources.index(next211_header, i + len(src210_header))
    sources_index = t210_to_230(sources[i:j])
    sources_index = sources_index.replace(
        "(row 210) {#row68-row190-ddd-meta-prelude-capstone-reunion-index-row-210}",
        "(row 230) {#row68-row210-ddd-meta-prelude-capstone-reunion-index-row-230}",
        1,
    )
    sources_index = sources_index.replace(
        "row68-row190-ddd-meta-prelude-capstone-reunion-index-row-210",
        "row68-row210-ddd-meta-prelude-capstone-reunion-index-row-230",
    )

    sources_table = t210_to_230(b210["sources_table"])
    sources_table = sources_table.replace("| 210 | Row 68 → Row 190", "| 230 | Row 68 → Row 210", 1)

    memory_table = t210_to_230(b210["memory_table"])
    memory_table = memory_table.replace("| 210 | Meta |", "| 230 | Meta |", 1)

    memory_baby = t210_to_230(b210["memory_baby"])
    if "{#row-230-baby-picture-row68-row210" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 230 baby picture",
            "### Row 230 baby picture {#row-230-baby-picture-row68-row210-ddd-meta-prelude-capstone-reunion}",
            1,
        )
        memory_baby = memory_baby.replace(
            "### Row 210 baby picture {#row-210-baby-picture-row68-row190-ddd-meta-prelude-capstone-reunion}",
            "### Row 230 baby picture {#row-230-baby-picture-row68-row210-ddd-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row230_preface": row230_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW229_EPILOGUE_OLD = (
    "Proceed to [row 210](#row-210-closing-loop) when row 68 closed but DDD meta prelude capstone still lags after row 209 on the full capstone path,"
)
ROW229_EPILOGUE_NEW = (
    "Proceed to [row 230](#row-230-closing-loop) when row 68 closed but DDD meta prelude capstone still lags after row 229 on the full capstone path,"
)

ROW229_STITCH_OLD = (
    "before row 230 DDD meta prelude capstone reunion opens on the full capstone path."
)
ROW229_STITCH_NEW = (
    "before row 231 homogenization meta prelude capstone reunion opens on the full capstone path."
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 230 skill checkpoint" in preface:
        print("preface: row 230 already present")
    else:
        if "### Row 229 skill checkpoint" not in preface:
            raise SystemExit("row 229 must exist before row 230")
        preface = preface.replace(copper, "\n" + b["row230_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 230")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-230" not in prologue:
        needle = (
            "| Row 68 → Row 209 Row 68 → Row 49 taxonomy meta prelude capstone reunion (row 229) | "
            "[Preface: row 229 skill checkpoint](../preface.md#skill-navigation-row-229)"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 229 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 230 closing stitch" not in prologue:
            prologue = prologue.replace(
                "**Row 229 closing stitch",
                b["prologue_stitch"] + "**Row 229 closing stitch",
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-229"></span>Row 229 preview'
        if preview_anchor in prologue and '<span id="prologue-preview-row-230">' not in prologue:
            prologue = prologue.replace(
                preview_anchor, b["prologue_preview"].strip() + "\n" + preview_anchor, 1
            )
        if ROW229_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW229_STITCH_OLD, ROW229_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 230")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    insert_after = (
        "### Row 229 closing loop (Row 68 → Row 209 Row 68 → Row 49 "
        "taxonomy meta prelude capstone reunion) {#row-229-closing-loop}"
    )
    marker = (
        "### Row 210 closing loop (Row 68 → Row 190 Row 68 → Row 50 "
        "DDD meta prelude capstone reunion) {#row-210-closing-loop}"
    )
    if insert_after not in epilogue or marker not in epilogue.split(insert_after, 1)[1]:
        raise SystemExit("epilogue row 229/210 insert anchors not found")
    head, segment = epilogue.split(insert_after, 1)
    if "### Row 230 closing loop" not in segment.split(marker, 1)[0]:
        if ROW229_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW229_EPILOGUE_OLD, ROW229_EPILOGUE_NEW, 1)
            head, segment = epilogue.split(insert_after, 1)
        segment = segment.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(head + insert_after + segment)
        print("epilogue: added row 230")
    else:
        print("epilogue: row 230 already present")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row210-ddd-meta-prelude-capstone-reunion-index-row-230" not in sources:
        sources = sources.replace(
            "| 210 | Row 68 → Row 190 Row 68 → Row 50 DDD meta prelude capstone",
            b["sources_table"] + "| 210 | Row 68 → Row 190 Row 68 → Row 50 DDD meta prelude capstone",
            1,
        )
        src210_header = (
            "## Row 68 → Row 190 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 210)"
        )
        sources = sources.replace(src210_header, b["sources_index"] + src210_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 230")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-230-baby-picture-row68-row210" not in memory:
        memory = memory.replace(
            "| 229 | Meta | [Row 68 → Row 209 taxonomy meta prelude capstone reunion index]",
            b["memory_table"] + "| 229 | Meta | [Row 68 → Row 209 taxonomy meta prelude capstone reunion index]",
            1,
        )
        inserted = False
        for baby_anchor in (
            "### Row 229 baby picture {#row-229-baby-picture-row68-row209-taxonomy-meta-prelude-capstone-reunion}",
            "### Row 228 baby picture {#row-228-baby-picture-row68-row208-midpoint-meta-prelude-capstone-reunion}",
            "### Row 210 baby picture {#row-210-baby-picture-row68-row190-ddd-meta-prelude-capstone-reunion}",
            "### Row 190 baby picture {#row-210-baby-picture-row68-row190-ddd-meta-prelude-capstone-reunion}",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 230")


if __name__ == "__main__":
    main()
