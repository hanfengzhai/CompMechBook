#!/usr/bin/env python3
"""Add row 231 meta-stitch (Row 68 → Row 211 ↔ Row 51 homogenization meta prelude capstone reunion, full capstone path)."""
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


def t211_to_231(text: str) -> str:
    return bump_meta_plus20(text)


def _load_add211():
    spec = importlib.util.spec_from_file_location("add211", ROOT / "scripts/add-row-211.py")
    add211 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add211)
    return add211


def _build_blocks() -> dict[str, str]:
    add211 = _load_add211()
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 211 skill checkpoint")
    end = preface.index("\n\n### Row 212 skill checkpoint", start)
    row231_preface = t211_to_231(preface[start:end]) + "\n\n"

    b211 = add211._build_blocks()
    prologue_stitch = t211_to_231(b211["prologue_stitch"].strip()) + "\n\n"
    prologue_compass = (
        "| Row 68 → Row 211 Row 68 → Row 51 homogenization meta prelude capstone reunion (row 231) | "
        "[Preface: row 231 skill checkpoint](../preface.md#skill-navigation-row-231) · "
        "[Row 68 → Row 211 homogenization meta prelude capstone reunion index](../appendix/sources.md#row68-row211-homogenization-meta-prelude-capstone-reunion-index-row-231) · "
        "[memory sheet row 231 baby picture](../appendix/memory-sheet.md#row-231-baby-picture-row68-row211-homogenization-meta-prelude-capstone-reunion) · "
        "[prologue row 231 preview row](#prologue-preview-row-231); [prologue row 231 closing stitch](#row-231-closing-stitch); "
        "[epilogue row 231 closing loop](../epilogue/multiscale.md#row-231-closing-loop) — "
        "read row 68 gate + row 230 or row 211 DDD meta prelude capstone / homogenization meta prelude gate + VII.2 Bridge → opening hinge → VII.3 homogenization + row 51 meta aloud "
        "when Peach–Köhler DDD is clean on the full capstone path but DAMASK decks feel like CP homework after verified DDD meta prelude capstone on the full capstone path |\n"
    )
    prologue_preview = t211_to_231(b211["prologue_preview"])

    epilogue_loop = t211_to_231(b211["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace("{#row-211-closing-loop}", "{#row-231-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 191 closing loop (Row 68 → Row 191 Row 68 → Row 51 homogenization meta prelude capstone reunion)",
        "### Row 231 closing loop (Row 68 → Row 211 Row 68 → Row 51 homogenization meta prelude capstone reunion)",
        1,
    )

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src211_header = (
        "## Row 68 → Row 171 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 191)"
    )
    next171_header = (
        "## Row 68 → Row 151 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 171)"
    )
    i = sources.index(src211_header)
    j = sources.index(next171_header, i + len(src211_header))
    sources_index = t211_to_231(sources[i:j])
    sources_index = sources_index.replace(
        "(row 191) {#row68-row171-homogenization-meta-prelude-capstone-reunion-index-row-191}",
        "(row 231) {#row68-row211-homogenization-meta-prelude-capstone-reunion-index-row-231}",
        1,
    )
    sources_index = sources_index.replace(
        "row68-row171-homogenization-meta-prelude-capstone-reunion-index-row-191",
        "row68-row211-homogenization-meta-prelude-capstone-reunion-index-row-231",
    )

    sources_table = t211_to_231(b211["sources_table"])
    sources_table = sources_table.replace("| 211 | Row 68 → Row 191", "| 231 | Row 68 → Row 211", 1)

    memory_table = t211_to_231(b211["memory_table"])
    memory_table = memory_table.replace("| 211 | Meta |", "| 231 | Meta |", 1)

    memory_baby = t211_to_231(b211["memory_baby"])
    if "{#row-231-baby-picture-row68-row211" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 231 baby picture",
            "### Row 231 baby picture {#row-231-baby-picture-row68-row211-homogenization-meta-prelude-capstone-reunion}",
            1,
        )
        memory_baby = memory_baby.replace(
            "### Row 211 baby picture {#row-211-baby-picture-row68-row191-homogenization-meta-prelude-capstone-reunion}",
            "### Row 231 baby picture {#row-231-baby-picture-row68-row211-homogenization-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row231_preface": row231_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW230_EPILOGUE_OLD = (
    "Proceed to [row 211](#row-211-closing-loop) when row 68 closed but homogenization meta prelude capstone still lags after row 210 on the full capstone path,"
)
ROW230_EPILOGUE_NEW = (
    "Proceed to [row 231](#row-231-closing-loop) when row 68 closed but homogenization meta prelude capstone still lags after row 230 on the full capstone path,"
)

ROW230_STITCH_OLD = (
    "before row 231 homogenization meta prelude capstone reunion opens on the full capstone path."
)
ROW230_STITCH_NEW = (
    "before row 232 atomistic meta prelude capstone reunion opens on the full capstone path."
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 231 skill checkpoint" in preface:
        print("preface: row 231 already present")
    else:
        if "### Row 230 skill checkpoint" not in preface:
            raise SystemExit("row 230 must exist before row 231")
        preface = preface.replace(copper, "\n" + b["row231_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 231")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-231" not in prologue:
        needle = (
            "| Row 68 → Row 210 Row 68 → Row 50 DDD meta prelude capstone reunion (row 230) | "
            "[Preface: row 230 skill checkpoint](../preface.md#skill-navigation-row-230)"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 230 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        stitch_anchors = (
            "**Row 230 closing stitch",
            "**Row 189 closing stitch (Row 68 → Row 209 Row 68 → Row 49 taxonomy meta prelude capstone reunion).** {#row-229-closing-stitch}",
        )
        if "**Row 231 closing stitch" not in prologue:
            inserted = False
            for anchor in stitch_anchors:
                if anchor in prologue:
                    prologue = prologue.replace(anchor, b["prologue_stitch"] + anchor, 1)
                    inserted = True
                    break
            if not inserted:
                print("prologue: row 231 closing stitch anchor not found (skipped stitch block)")
        preview_anchor = '| <span id="prologue-preview-row-230"></span>Row 229 preview'
        if preview_anchor in prologue and '<span id="prologue-preview-row-231">' not in prologue:
            prologue = prologue.replace(
                preview_anchor, b["prologue_preview"].strip() + "\n" + preview_anchor, 1
            )
        if ROW230_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW230_STITCH_OLD, ROW230_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 231")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    insert_after = (
        "### Row 230 closing loop (Row 68 → Row 210 Row 68 → Row 50 "
        "DDD meta prelude capstone reunion) {#row-230-closing-loop}"
    )
    marker = (
        "### Row 210 closing loop (Row 68 → Row 190 Row 68 → Row 50 "
        "DDD meta prelude capstone reunion) {#row-210-closing-loop}"
    )
    if insert_after not in epilogue:
        raise SystemExit("epilogue row 230 insert anchor not found")
    if marker not in epilogue.split(insert_after, 1)[1]:
        raise SystemExit("epilogue row 210 marker not found after row 230")
    head, segment = epilogue.split(insert_after, 1)
    if "### Row 231 closing loop" not in segment.split(marker, 1)[0]:
        if ROW230_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW230_EPILOGUE_OLD, ROW230_EPILOGUE_NEW, 1)
            head, segment = epilogue.split(insert_after, 1)
        segment = segment.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(head + insert_after + segment)
        print("epilogue: added row 231")
    else:
        print("epilogue: row 231 already present")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row211-homogenization-meta-prelude-capstone-reunion-index-row-231" not in sources:
        sources = sources.replace(
            "| 211 | Row 68 → Row 191 Row 68 → Row 51 homogenization meta prelude capstone",
            b["sources_table"] + "| 211 | Row 68 → Row 191 Row 68 → Row 51 homogenization meta prelude capstone",
            1,
        )
        src211_header = (
            "## Row 68 → Row 171 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 191)"
        )
        sources = sources.replace(src211_header, b["sources_index"] + src211_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 231")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-231-baby-picture-row68-row211" not in memory:
        memory = memory.replace(
            "| 230 | Meta | [Row 68 → Row 210 DDD meta prelude capstone reunion index]",
            b["memory_table"] + "| 230 | Meta | [Row 68 → Row 210 DDD meta prelude capstone reunion index]",
            1,
        )
        inserted = False
        for baby_anchor in (
            "### Row 230 baby picture {#row-230-baby-picture-row68-row210-ddd-meta-prelude-capstone-reunion}",
            "### Row 229 baby picture {#row-229-baby-picture-row68-row209-taxonomy-meta-prelude-capstone-reunion}",
            "### Row 211 baby picture {#row-211-baby-picture-row68-row191-homogenization-meta-prelude-capstone-reunion}",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 231")


if __name__ == "__main__":
    main()
