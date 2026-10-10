#!/usr/bin/env python3
"""Add row 233 meta-stitch (Row 68 → Row 213 ↔ Row 53 dynamics meta prelude capstone reunion, full capstone path)."""
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


def t213_to_233(text: str) -> str:
    return bump_meta_plus20(text)


def _load_add213():
    spec = importlib.util.spec_from_file_location("add213", ROOT / "scripts/add-row-213.py")
    add212 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add212)
    return add212


def _build_blocks() -> dict[str, str]:
    add213 = _load_add213()
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 213 skill checkpoint")
    end = preface.index("\n\n### Row 214 skill checkpoint", start)
    row233_preface = t213_to_233(preface[start:end]) + "\n\n"

    b213 = add213._build_blocks()
    prologue_stitch = t213_to_233(b213["prologue_stitch"].strip()) + "\n\n"
    prologue_compass = t213_to_233(b213["prologue_compass"])
    if not prologue_compass.endswith("\n"):
        prologue_compass += "\n"
    prologue_preview = t213_to_233(b213["prologue_preview"])

    epilogue_loop = t213_to_233(b213["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace("{#row-213-closing-loop}", "{#row-233-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 193 closing loop (Row 68 → Row 193 Row 68 → Row 53 dynamics meta prelude capstone reunion)",
        "### Row 233 closing loop (Row 68 → Row 213 Row 68 → Row 53 dynamics meta prelude capstone reunion)",
        1,
    )
    epilogue_loop = epilogue_loop.replace(
        "### Row 213 closing loop (Row 68 → Row 213 Row 68 → Row 53 dynamics meta prelude capstone reunion)",
        "### Row 233 closing loop (Row 68 → Row 213 Row 68 → Row 53 dynamics meta prelude capstone reunion)",
        1,
    )

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src213_header = (
        "## Row 68 → Row 193 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 213)"
    )
    next193_header = (
        "## Row 68 → Row 173 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 193)"
    )
    i = sources.index(src213_header)
    j = sources.index(next193_header, i + len(src213_header))
    sources_index = t213_to_233(sources[i:j])
    if "(row 233) {#row68-row213-dynamics-meta-prelude-capstone-reunion-index-row-233}" not in sources_index:
        sources_index = sources_index.replace(
            "(row 213) {#row68-row193-dynamics-meta-prelude-capstone-reunion-index-row-213}",
            "(row 233) {#row68-row213-dynamics-meta-prelude-capstone-reunion-index-row-233}",
            1,
        )
    sources_index = sources_index.replace(
        "row68-row193-dynamics-meta-prelude-capstone-reunion-index-row-213",
        "row68-row213-dynamics-meta-prelude-capstone-reunion-index-row-233",
    )

    sources_table = t213_to_233(b213["sources_table"])
    sources_table = sources_table.replace("| 213 | Row 68 → Row 193", "| 233 | Row 68 → Row 213", 1)

    memory_table = t213_to_233(b213["memory_table"])
    memory_table = memory_table.replace("| 213 | Meta |", "| 233 | Meta |", 1)

    memory_baby = t213_to_233(b213["memory_baby"])
    if "{#row-233-baby-picture-row68-row213-dynamics-meta-prelude-capstone-reunion}" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 233 baby picture",
            "### Row 233 baby picture {#row-233-baby-picture-row68-row213-dynamics-meta-prelude-capstone-reunion}",
            1,
        )
        memory_baby = memory_baby.replace(
            "### Row 213 baby picture {#row-213-baby-picture-row68-row193-dynamics-meta-prelude-capstone-reunion}",
            "### Row 233 baby picture {#row-233-baby-picture-row68-row213-dynamics-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row233_preface": row233_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW232_EPILOGUE_OLD = (
    "Proceed to [row 213](#row-213-closing-loop) when row 68 closed but dynamics meta prelude capstone still lags after row 212 on the full capstone path,"
)
ROW232_EPILOGUE_NEW = (
    "Proceed to [row 233](#row-233-closing-loop) when row 68 closed but dynamics meta prelude capstone still lags after row 232 on the full capstone path,"
)

ROW232_STITCH_OLD = (
    "before row 213 dynamics meta prelude capstone reunion opens on the full capstone path."
)
ROW232_STITCH_NEW = (
    "before row 234 export meta prelude capstone reunion opens on the full capstone path."
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 233 skill checkpoint" in preface:
        print("preface: row 233 already present")
    else:
        if "### Row 232 skill checkpoint" not in preface:
            raise SystemExit("row 232 must exist before row 233")
        preface = preface.replace(copper, "\n" + b["row233_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 233")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-233" not in prologue:
        needle = (
            "| Row 68 → Row 212 Row 68 → Row 52 atomistic meta prelude capstone reunion (row 232) | "
            "[Preface: row 232 skill checkpoint](../preface.md#skill-navigation-row-232)"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 232 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        stitch_anchors = (
            "**Row 212 closing stitch (Row 68 → Row 212 Row 68 → Row 52 atomistic meta prelude capstone reunion).** {#row-232-closing-stitch}",
            "**Row 211 closing stitch",
        )
        if "{#row-233-closing-stitch}" not in prologue:
            inserted = False
            for anchor in stitch_anchors:
                if anchor in prologue:
                    prologue = prologue.replace(anchor, b["prologue_stitch"] + anchor, 1)
                    inserted = True
                    break
            if not inserted:
                print("prologue: row 233 closing stitch anchor not found (skipped stitch block)")
        preview_anchor = '| <span id="prologue-preview-row-232"></span>Row 212 preview'
        if preview_anchor in prologue and '<span id="prologue-preview-row-233">' not in prologue:
            prologue = prologue.replace(
                preview_anchor, b["prologue_preview"].strip() + "\n" + preview_anchor, 1
            )
        if ROW232_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW232_STITCH_OLD, ROW232_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 233")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "{#row-233-closing-loop}" in epilogue:
        if ROW232_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW232_EPILOGUE_OLD, ROW232_EPILOGUE_NEW, 1)
            epilogue_path.write_text(epilogue)
            print("epilogue: updated row 232 proceed link")
        else:
            print("epilogue: row 233 already present")
    else:
        insert_after = (
            "### Row 212 closing loop (Row 68 → Row 212 Row 68 → Row 52 "
            "atomistic meta prelude capstone reunion) {#row-232-closing-loop}"
        )
        marker = (
            "### Row 210 closing loop (Row 68 → Row 190 Row 68 → Row 50 "
            "DDD meta prelude capstone reunion) {#row-210-closing-loop}"
        )
        if insert_after not in epilogue:
            raise SystemExit("epilogue row 232 insert anchor not found")
        if marker not in epilogue.split(insert_after, 1)[1]:
            raise SystemExit("epilogue row 210 marker not found after row 232")
        head, segment = epilogue.split(insert_after, 1)
        if "### Row 233 closing loop" not in segment.split(marker, 1)[0]:
            if ROW232_EPILOGUE_OLD in epilogue:
                epilogue = epilogue.replace(ROW232_EPILOGUE_OLD, ROW232_EPILOGUE_NEW, 1)
                head, segment = epilogue.split(insert_after, 1)
            segment = segment.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
            epilogue_path.write_text(head + insert_after + segment)
            print("epilogue: added row 233")
        else:
            print("epilogue: row 233 already present")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row213-dynamics-meta-prelude-capstone-reunion-index-row-233" not in sources:
        sources = sources.replace(
            "| 213 | Row 68 → Row 193 Row 68 → Row 53 dynamics meta prelude capstone",
            b["sources_table"] + "| 213 | Row 68 → Row 193 Row 68 → Row 53 dynamics meta prelude capstone",
            1,
        )
        sources = sources.replace(src213_header := (
            "## Row 68 → Row 193 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 213)"
        ), b["sources_index"] + src213_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 233")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-233-baby-picture-row68-row213" not in memory:
        memory = memory.replace(
            "| 232 | Meta | [Row 68 → Row 212 atomistic meta prelude capstone reunion index]",
            b["memory_table"] + "| 232 | Meta | [Row 68 → Row 212 atomistic meta prelude capstone reunion index]",
            1,
        )
        inserted = False
        for baby_anchor in (
            "### Row 232 baby picture {#row-232-baby-picture-row68-row212-atomistic-meta-prelude-capstone-reunion}",
            "### Row 231 baby picture {#row-231-baby-picture-row68-row211-homogenization-meta-prelude-capstone-reunion}",
            "### Row 213 baby picture {#row-213-baby-picture-row68-row193-dynamics-meta-prelude-capstone-reunion}",
            "### Row 193 baby picture",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            table_anchor = "| 232 | Meta | [Row 68 → Row 212 atomistic meta prelude capstone reunion index]"
            if table_anchor in memory:
                line_end = memory.find("\n", memory.find(table_anchor))
                memory = memory[: line_end + 1] + b["memory_table"] + memory[line_end + 1 :]
                print("memory-sheet: added row 233 table (baby section anchor skipped)")
            else:
                raise SystemExit("memory baby picture anchor not found")
        else:
            print("memory-sheet: added row 233 baby block")
        memory_path.write_text(memory)


if __name__ == "__main__":
    main()
