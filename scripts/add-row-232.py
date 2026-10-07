#!/usr/bin/env python3
"""Add row 232 meta-stitch (Row 68 → Row 212 ↔ Row 52 atomistic meta prelude capstone reunion, full capstone path)."""
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


def t212_to_232(text: str) -> str:
    return bump_meta_plus20(text)


def _load_add212():
    spec = importlib.util.spec_from_file_location("add212", ROOT / "scripts/add-row-212.py")
    add212 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add212)
    return add212


def _build_blocks() -> dict[str, str]:
    add212 = _load_add212()
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 212 skill checkpoint")
    end = preface.index("\n\n### Row 213 skill checkpoint", start)
    row232_preface = t212_to_232(preface[start:end]) + "\n\n"

    b212 = add212._build_blocks()
    prologue_stitch = t212_to_232(b212["prologue_stitch"].strip()) + "\n\n"
    prologue_compass = (
        "| Row 68 → Row 212 Row 68 → Row 52 atomistic meta prelude capstone reunion (row 232) | "
        "[Preface: row 232 skill checkpoint](../preface.md#skill-navigation-row-232) · "
        "[Row 68 → Row 212 atomistic meta prelude capstone reunion index](../appendix/sources.md#row68-row212-atomistic-meta-prelude-capstone-reunion-index-row-232) · "
        "[memory sheet row 232 baby picture](../appendix/memory-sheet.md#row-232-baby-picture-row68-row212-atomistic-meta-prelude-capstone-reunion) · "
        "[prologue row 232 preview row](#prologue-preview-row-232); [prologue row 232 closing stitch](#row-232-closing-stitch); "
        "[epilogue row 232 closing loop](../epilogue/multiscale.md#row-232-closing-loop) — "
        "read row 68 gate + row 231 or row 212 homogenization meta prelude capstone / atomistic meta prelude gate + VII.3 Bridge → opening hinge → VIII.1 phase space + row 52 meta aloud "
        "when polycrystal handoff is clean on the full capstone path but LAMMPS decks feel like AtomModel homework after verified homogenization meta prelude capstone on the full capstone path |\n"
    )
    prologue_preview = t212_to_232(b212["prologue_preview"])

    epilogue_loop = t212_to_232(b212["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace("{#row-212-closing-loop}", "{#row-232-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 192 closing loop (Row 68 → Row 192 Row 68 → Row 52 atomistic meta prelude capstone reunion)",
        "### Row 232 closing loop (Row 68 → Row 212 Row 68 → Row 52 atomistic meta prelude capstone reunion)",
        1,
    )
    epilogue_loop = epilogue_loop.replace(
        "### Row 212 closing loop (Row 68 → Row 212 Row 68 → Row 52 atomistic meta prelude capstone reunion)",
        "### Row 232 closing loop (Row 68 → Row 212 Row 68 → Row 52 atomistic meta prelude capstone reunion)",
        1,
    )

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src212_header = (
        "## Row 68 → Row 192 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 212)"
    )
    next192_header = (
        "## Row 68 → Row 172 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 192)"
    )
    i = sources.index(src212_header)
    j = sources.index(next192_header, i + len(src212_header))
    sources_index = t212_to_232(sources[i:j])
    sources_index = sources_index.replace(
        "(row 212) {#row68-row192-atomistic-meta-prelude-capstone-reunion-index-row-212}",
        "(row 232) {#row68-row212-atomistic-meta-prelude-capstone-reunion-index-row-232}",
        1,
    )
    sources_index = sources_index.replace(
        "row68-row192-atomistic-meta-prelude-capstone-reunion-index-row-212",
        "row68-row212-atomistic-meta-prelude-capstone-reunion-index-row-232",
    )

    sources_table = t212_to_232(b212["sources_table"])
    sources_table = sources_table.replace("| 212 | Row 68 → Row 192", "| 232 | Row 68 → Row 212", 1)

    memory_table = t212_to_232(b212["memory_table"])
    memory_table = memory_table.replace("| 212 | Meta |", "| 232 | Meta |", 1)

    memory_baby = t212_to_232(b212["memory_baby"])
    if "{#row-232-baby-picture-row68-row212" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 232 baby picture",
            "### Row 232 baby picture {#row-232-baby-picture-row68-row212-atomistic-meta-prelude-capstone-reunion}",
            1,
        )
        memory_baby = memory_baby.replace(
            "### Row 212 baby picture {#row-212-baby-picture-row68-row192-atomistic-meta-prelude-capstone-reunion}",
            "### Row 232 baby picture {#row-232-baby-picture-row68-row212-atomistic-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row232_preface": row232_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW231_EPILOGUE_OLD = (
    "Proceed to [row 212](#row-212-closing-loop) when row 68 closed but atomistic meta prelude capstone still lags after row 211 on the full capstone path,"
)
ROW231_EPILOGUE_NEW = (
    "Proceed to [row 232](#row-232-closing-loop) when row 68 closed but atomistic meta prelude capstone still lags after row 231 on the full capstone path,"
)

ROW231_STITCH_OLD = (
    "before row 232 atomistic meta prelude capstone reunion opens on the full capstone path."
)
ROW231_STITCH_NEW = (
    "before row 233 dynamics meta prelude capstone reunion opens on the full capstone path."
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 232 skill checkpoint" in preface:
        print("preface: row 232 already present")
    else:
        if "### Row 231 skill checkpoint" not in preface:
            raise SystemExit("row 231 must exist before row 232")
        preface = preface.replace(copper, "\n" + b["row232_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 232")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-232" not in prologue:
        needle = (
            "| Row 68 → Row 211 Row 68 → Row 51 homogenization meta prelude capstone reunion (row 231) | "
            "[Preface: row 231 skill checkpoint](../preface.md#skill-navigation-row-231)"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 231 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        stitch_anchors = (
            "**Row 211 closing stitch (Row 68 → Row 211 Row 68 → Row 51 homogenization meta prelude capstone reunion).** {#row-231-closing-stitch}",
            "**Row 230 closing stitch",
        )
        if "{#row-232-closing-stitch}" not in prologue:
            inserted = False
            for anchor in stitch_anchors:
                if anchor in prologue:
                    prologue = prologue.replace(anchor, b["prologue_stitch"] + anchor, 1)
                    inserted = True
                    break
            if not inserted:
                print("prologue: row 232 closing stitch anchor not found (skipped stitch block)")
        preview_anchor = '| <span id="prologue-preview-row-231"></span>Row 211 preview'
        if preview_anchor in prologue and '<span id="prologue-preview-row-232">' not in prologue:
            prologue = prologue.replace(
                preview_anchor, b["prologue_preview"].strip() + "\n" + preview_anchor, 1
            )
        if ROW231_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW231_STITCH_OLD, ROW231_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 232")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "{#row-232-closing-loop}" in epilogue:
        if ROW231_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW231_EPILOGUE_OLD, ROW231_EPILOGUE_NEW, 1)
            epilogue_path.write_text(epilogue)
            print("epilogue: updated row 231 proceed link")
        else:
            print("epilogue: row 232 already present")
    else:
        insert_after = (
            "### Row 211 closing loop (Row 68 → Row 211 Row 68 → Row 51 "
            "homogenization meta prelude capstone reunion) {#row-231-closing-loop}"
        )
        marker = (
            "### Row 210 closing loop (Row 68 → Row 190 Row 68 → Row 50 "
            "DDD meta prelude capstone reunion) {#row-210-closing-loop}"
        )
        if insert_after not in epilogue:
            raise SystemExit("epilogue row 231 insert anchor not found")
        if marker not in epilogue.split(insert_after, 1)[1]:
            raise SystemExit("epilogue row 210 marker not found after row 231")
        head, segment = epilogue.split(insert_after, 1)
        if "### Row 232 closing loop" not in segment.split(marker, 1)[0]:
            if ROW231_EPILOGUE_OLD in epilogue:
                epilogue = epilogue.replace(ROW231_EPILOGUE_OLD, ROW231_EPILOGUE_NEW, 1)
                head, segment = epilogue.split(insert_after, 1)
            segment = segment.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
            epilogue_path.write_text(head + insert_after + segment)
            print("epilogue: added row 232")
        else:
            print("epilogue: row 232 already present")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row212-atomistic-meta-prelude-capstone-reunion-index-row-232" not in sources:
        sources = sources.replace(
            "| 192 | Row 68 → Row 192 Row 68 → Row 52 atomistic meta prelude capstone",
            b["sources_table"] + "| 192 | Row 68 → Row 192 Row 68 → Row 52 atomistic meta prelude capstone",
            1,
        )
        sources = sources.replace(src212_header := (
            "## Row 68 → Row 192 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 212)"
        ), b["sources_index"] + src212_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 232")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-232-baby-picture-row68-row212" not in memory:
        memory = memory.replace(
            "| 231 | Meta | [Row 68 → Row 211 homogenization meta prelude capstone reunion index]",
            b["memory_table"] + "| 231 | Meta | [Row 68 → Row 211 homogenization meta prelude capstone reunion index]",
            1,
        )
        inserted = False
        for baby_anchor in (
            "### Row 231 baby picture {#row-231-baby-picture-row68-row211-homogenization-meta-prelude-capstone-reunion}",
            "### Row 230 baby picture {#row-230-baby-picture-row68-row210-ddd-meta-prelude-capstone-reunion}",
            "### Row 212 baby picture {#row-212-baby-picture-row68-row192-atomistic-meta-prelude-capstone-reunion}",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 232")


if __name__ == "__main__":
    main()
