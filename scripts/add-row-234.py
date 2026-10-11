#!/usr/bin/env python3
"""Add row 234 meta-stitch (Row 68 → Row 214 ↔ Row 54 export meta prelude capstone reunion, full capstone path)."""
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


def t214_to_234(text: str) -> str:
    return bump_meta_plus20(text)


def _load_add214():
    spec = importlib.util.spec_from_file_location("add214", ROOT / "scripts/add-row-214.py")
    add214 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add214)
    return add214


def _build_blocks() -> dict[str, str]:
    add214 = _load_add214()
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 214 skill checkpoint")
    end = preface.index("\n\n### Row 215 skill checkpoint", start)
    row234_preface = t214_to_234(preface[start:end]) + "\n\n"

    b214 = add214._build_blocks()
    prologue_stitch = t214_to_234(b214["prologue_stitch"].strip()) + "\n\n"
    prologue_compass = t214_to_234(b214["prologue_compass"])
    if "row 234)" not in prologue_compass:
        prologue_compass = (
            "| Row 68 → Row 214 Row 68 → Row 54 export meta prelude capstone reunion (row 234) | "
            "[Preface: row 234 skill checkpoint](../preface.md#skill-navigation-row-234) · "
            "[Row 68 → Row 214 export meta prelude capstone reunion index](../appendix/sources.md#row68-row214-export-meta-prelude-capstone-reunion-index-row-234) · "
            "[memory sheet row 234 baby picture](../appendix/memory-sheet.md#row-234-baby-picture-row68-row214-export-meta-prelude-capstone-reunion) · "
            "[prologue row 234 preview row](#prologue-preview-row-234); [prologue row 234 closing stitch](#row-234-closing-stitch); "
            "[epilogue row 234 closing loop](../epilogue/multiscale.md#row-234-closing-loop) — "
            "read row 68 gate + row 233 or row 214 dynamics meta prelude capstone / export meta prelude gate + "
            "VIII.2 Bridge → opening hinge → VIII.3 export + row 54 meta aloud when NPT converges on the full "
            "capstone path but foundation manifest feels like AtomModel homework after verified dynamics meta "
            "prelude capstone on the full capstone path |\n"
        )
    prologue_preview = t214_to_234(b214["prologue_preview"])

    epilogue_loop = t214_to_234(b214["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace("{#row-214-closing-loop}", "{#row-234-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 194 closing loop (Row 68 → Row 194 Row 68 → Row 54 export meta prelude capstone reunion)",
        "### Row 234 closing loop (Row 68 → Row 214 Row 68 → Row 54 export meta prelude capstone reunion)",
        1,
    )
    epilogue_loop = epilogue_loop.replace(
        "### Row 214 closing loop (Row 68 → Row 214 Row 68 → Row 54 export meta prelude capstone reunion)",
        "### Row 234 closing loop (Row 68 → Row 214 Row 68 → Row 54 export meta prelude capstone reunion)",
        1,
    )

    sources_index = t214_to_234(b214["sources_index"])
    sources_index = sources_index.replace(
        "(row 214) {#row68-row194-export-meta-prelude-capstone-reunion-index-row-214}",
        "(row 234) {#row68-row214-export-meta-prelude-capstone-reunion-index-row-234}",
        1,
    )
    sources_index = sources_index.replace(
        "row68-row194-export-meta-prelude-capstone-reunion-index-row-214",
        "row68-row214-export-meta-prelude-capstone-reunion-index-row-234",
    )
    if "row 234)" not in sources_index:
        sources_index = sources_index.replace("(row 214)", "(row 234)", 1)

    sources_table = t214_to_234(b214["sources_table"])
    sources_table = sources_table.replace("| 214 | Row 68 → Row 194", "| 234 | Row 68 → Row 214", 1)

    memory_table = t214_to_234(b214["memory_table"])
    memory_table = memory_table.replace("| 214 | Meta |", "| 234 | Meta |", 1)

    memory_baby = t214_to_234(b214["memory_baby"])
    if "{#row-234-baby-picture-row68-row214" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 234 baby picture",
            "### Row 234 baby picture {#row-234-baby-picture-row68-row214-export-meta-prelude-capstone-reunion}",
            1,
        )
        memory_baby = memory_baby.replace(
            "### Row 214 baby picture {#row-214-baby-picture-row68-row194-export-meta-prelude-capstone-reunion}",
            "### Row 234 baby picture {#row-234-baby-picture-row68-row214-export-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row234_preface": row234_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW233_EPILOGUE_OLD = (
    "Proceed to [row 214](#row-214-closing-loop) when row 68 closed but export meta prelude capstone still lags after row 213 on the full capstone path,"
)
ROW233_EPILOGUE_NEW = (
    "Proceed to [row 234](#row-234-closing-loop) when row 68 closed but export meta prelude capstone still lags after row 233 on the full capstone path,"
)

ROW233_STITCH_OLD = (
    "before row 234 export meta prelude capstone reunion opens on the full capstone path."
)
ROW233_STITCH_NEW = (
    "before row 235 electronic audit meta prelude capstone reunion opens on the full capstone path."
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 234 skill checkpoint" in preface:
        print("preface: row 234 already present")
    else:
        if "### Row 233 skill checkpoint" not in preface:
            raise SystemExit("row 233 must exist before row 234")
        preface = preface.replace(copper, "\n" + b["row234_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 234")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-234" not in prologue:
        needle = (
            "| Row 68 → Row 213 Row 68 → Row 53 dynamics meta prelude capstone reunion (row 233) | "
            "[Preface: row 233 skill checkpoint](../preface.md#skill-navigation-row-233)"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 233 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        stitch_anchors = (
            "**Row 213 closing stitch (Row 68 → Row 213 Row 68 → Row 53 dynamics meta prelude capstone reunion).** {#row-233-closing-stitch}",
            "**Row 232 closing stitch",
        )
        if "{#row-234-closing-stitch}" not in prologue:
            inserted = False
            for anchor in stitch_anchors:
                if anchor in prologue:
                    prologue = prologue.replace(anchor, b["prologue_stitch"] + anchor, 1)
                    inserted = True
                    break
            if not inserted:
                print("prologue: row 234 closing stitch anchor not found (skipped stitch block)")
        preview_anchor = '| <span id="prologue-preview-row-233"></span>Row 213 preview'
        if preview_anchor in prologue and '<span id="prologue-preview-row-234">' not in prologue:
            prologue = prologue.replace(
                preview_anchor, b["prologue_preview"].strip() + "\n" + preview_anchor, 1
            )
        if ROW233_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW233_STITCH_OLD, ROW233_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 234")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "{#row-234-closing-loop}" in epilogue:
        changed = False
        if ROW233_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW233_EPILOGUE_OLD, ROW233_EPILOGUE_NEW, 1)
            changed = True
            print("epilogue: updated row 233 proceed link")
        if changed:
            epilogue_path.write_text(epilogue)
        if "### Row 234 skill checkpoint" in preface_path.read_text():
            print("epilogue: row 234 already present")
        elif changed:
            pass
        else:
            print("epilogue: row 234 closing loop present; finishing preface/prologue/memory")
    if "{#row-234-closing-loop}" not in epilogue:
        insert_after = (
            "### Row 213 closing loop (Row 68 → Row 213 Row 68 → Row 53 dynamics meta prelude capstone reunion) "
            "{#row-233-closing-loop}"
        )
        marker = (
            "### Row 210 closing loop (Row 68 → Row 190 Row 68 → Row 50 "
            "DDD meta prelude capstone reunion) {#row-210-closing-loop}"
        )
        if insert_after not in epilogue:
            raise SystemExit("epilogue row 233 insert anchor not found")
        if marker not in epilogue.split(insert_after, 1)[1]:
            raise SystemExit("epilogue row 210 marker not found after row 233")
        head, segment = epilogue.split(insert_after, 1)
        if "### Row 234 closing loop" not in segment.split(marker, 1)[0]:
            if ROW233_EPILOGUE_OLD in epilogue:
                epilogue = epilogue.replace(ROW233_EPILOGUE_OLD, ROW233_EPILOGUE_NEW, 1)
                head, segment = epilogue.split(insert_after, 1)
            segment = segment.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
            epilogue_path.write_text(head + insert_after + segment)
            print("epilogue: added row 234")
        else:
            print("epilogue: row 234 already present")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "| 234 | Row 68 → Row 214" not in sources:
        needle_table = "| 194 | Row 68 → Row 174 Row 68 → Row 54 export meta prelude capstone"
        if needle_table in sources:
            sources = sources.replace(
                needle_table,
                b["sources_table"] + needle_table,
                1,
            )
            print("sources: added row 234 table row")
    src214_header = (
        "## Row 68 → Row 194 Row 68 → Row 54 export meta prelude capstone reunion index (row 214)"
    )
    if "row68-row214-export-meta-prelude-capstone-reunion-index-row-234" not in sources:
        if src214_header in sources and b["sources_index"].strip() not in sources:
            sources = sources.replace(src214_header, b["sources_index"] + src214_header, 1)
            print("sources: added row 234 index")
    sources_path.write_text(sources)

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-234-baby-picture-row68-row214" not in memory:
        memory = memory.replace(
            "| 233 | Meta | [Row 68 → Row 213 dynamics meta prelude capstone reunion index]",
            b["memory_table"] + "| 233 | Meta | [Row 68 → Row 213 dynamics meta prelude capstone reunion index]",
            1,
        )
        inserted = False
        for baby_anchor in (
            "### Row 233 baby picture {#row-233-baby-picture-row68-row213-dynamics-meta-prelude-capstone-reunion}",
            "### Row 232 baby picture {#row-232-baby-picture-row68-row212-atomistic-meta-prelude-capstone-reunion}",
            "### Row 214 baby picture {#row-214-baby-picture-row68-row194-export-meta-prelude-capstone-reunion}",
            "### Row 194 baby picture",
            "### Row 174 baby picture",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 234")


if __name__ == "__main__":
    main()
