#!/usr/bin/env python3
"""Add row 234 meta-stitch (Row 68 → Row 214 ↔ Row 54 export meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util
import re

ROOT = Path(__file__).resolve().parents[1]


def shift_meta_bump(text: str, delta: int = 20) -> str:
    """Shift capstone-path row references (100–250) by delta for meta-stitch copy."""
    out = text
    for tag in ("__R214__", "__R215__", "__R233__", "__R234__", "__R235__"):
        out = out.replace(tag, tag)

    def in_band(n: int) -> bool:
        return 100 <= n <= 250

    def repl_row(m: re.Match[str]) -> str:
        n = int(m.group(1))
        return f"row {n + delta}" if in_band(n) else m.group(0)

    def repl_Row(m: re.Match[str]) -> str:
        n = int(m.group(1))
        return f"Row {n + delta}" if in_band(n) else m.group(0)

    out = re.sub(
        r"row68-row(\d{3})",
        lambda m: f"row68-row{int(m.group(1)) + delta}" if in_band(int(m.group(1))) else m.group(0),
        out,
    )
    out = re.sub(
        r"index-row-(\d{3})",
        lambda m: f"index-row-{int(m.group(1)) + delta}" if in_band(int(m.group(1))) else m.group(0),
        out,
    )
    out = re.sub(
        r"skill-navigation-row-(\d{3})",
        lambda m: f"skill-navigation-row-{int(m.group(1)) + delta}" if in_band(int(m.group(1))) else m.group(0),
        out,
    )
    out = re.sub(
        r"prologue-preview-row-(\d{3})",
        lambda m: f"prologue-preview-row-{int(m.group(1)) + delta}" if in_band(int(m.group(1))) else m.group(0),
        out,
    )
    out = re.sub(
        r"row-(\d{3})-(closing-stitch|closing-loop|baby-picture)",
        lambda m: f"row-{int(m.group(1)) + delta}-{m.group(2)}" if in_band(int(m.group(1))) else m.group(0),
        out,
    )
    out = re.sub(r"\brow (\d{3})\b", repl_row, out)
    out = re.sub(r"\bRow (\d{3})\b", repl_Row, out)
    return out


def bump214_to_234(text: str) -> str:
    protected = (
        ("row-234-", "__P234__"),
        ("skill-navigation-row-234", "__S234__"),
        ("prologue-preview-row-234", "__PR234__"),
        ("{#row-234-closing-stitch}", "__ST234__"),
        ("{#row-234-closing-loop}", "__LP234__"),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = shift_meta_bump(out, 20)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add214():
    spec = importlib.util.spec_from_file_location("add214", ROOT / "scripts/add-row-214.py")
    add214 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add214)
    return add214


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 214 skill checkpoint")
    end = preface.index("\n\n### Row 215 skill checkpoint", start)
    row234_preface = bump214_to_234(preface[start:end]) + "\n\n"

    b214 = _load_add214()._build_blocks()
    prologue_stitch = bump214_to_234(
        b214["prologue_stitch"]
        .replace("{#row-214-closing-stitch}", "{#row-234-closing-stitch}")
        .replace(
            "**Row 214 closing stitch (Row 68 → Row 194",
            "**Row 234 closing stitch (Row 68 → Row 214",
        )
        .replace(
            "**Row 194 closing stitch (Row 68 → Row 194",
            "**Row 234 closing stitch (Row 68 → Row 214",
        )
    ).replace("**Row 254 closing stitch", "**Row 234 closing stitch", 1)
    prologue_compass = bump214_to_234(b214["prologue_compass"]).replace(
        "export meta prelude capstone reunion (row 214) |",
        "export meta prelude capstone reunion (row 234) |",
        1,
    )
    prologue_preview = bump214_to_234(b214["prologue_preview"]).replace(
        "Row 214 preview", "Row 234 preview", 1
    )

    # Use add-row-214 blocks only — live epilogue slice pulls duplicate export loops.
    epilogue_loop = bump214_to_234(b214["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace("{#row-214-closing-loop}", "{#row-234-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 214 closing loop (Row 68 → Row 214",
        "### Row 234 closing loop (Row 68 → Row 214",
        1,
    ).replace(
        "### Row 234 closing loop (Row 68 → Row 194",
        "### Row 234 closing loop (Row 68 → Row 214",
        1,
    )
    for spill in (
        "\n\n\n\n### Row 215 closing loop",
        "\n\n\n\n### Row 195 closing loop",
    ):
        if spill in epilogue_loop:
            epilogue_loop = epilogue_loop.split(spill, 1)[0].rstrip() + "\n\n"
            break
    epilogue_loop = epilogue_loop.rstrip() + "\n\n"

    sources_index = bump214_to_234(b214["sources_index"])
    sources_index = sources_index.replace(
        "## Row 68 → Row 194 Row 68 → Row 54 export meta prelude capstone reunion index (row 214) "
        "{#row68-row194-export-meta-prelude-capstone-reunion-index-row-214}",
        "## Row 68 → Row 214 Row 68 → Row 54 export meta prelude capstone reunion index (row 234) "
        "{#row68-row214-export-meta-prelude-capstone-reunion-index-row-234}",
        1,
    )

    sources_table = bump214_to_234(b214["sources_table"])
    sources_table = re.sub(
        r"^\| 214 \| Row 68 → Row 214",
        "| 234 | Row 68 → Row 214",
        sources_table,
        count=1,
        flags=re.MULTILINE,
    )
    if "| 234 | Row 68 → Row 214" not in sources_table:
        sources_table = sources_table.replace("| 214 | Row 68 → Row 194", "| 234 | Row 68 → Row 214", 1)

    memory_table = bump214_to_234(b214["memory_table"])
    memory_table = memory_table.replace("| 214 | Meta |", "| 234 | Meta |", 1)

    memory_baby = bump214_to_234(b214["memory_baby"]).rstrip() + "\n\n"
    memory_baby = memory_baby.replace(
        "### Row 234 baby picture {#row-214-baby-picture",
        "### Row 234 baby picture {#row-234-baby-picture-row68-row214-export-meta-prelude-capstone-reunion} {#row-214-baby-picture",
        1,
    )
    if "{#row-234-baby-picture-row68-row214" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 234 baby picture",
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


ROW232_STITCH_FIX_OLD = (
    "before row 234 export meta prelude capstone reunion opens on the full capstone path."
)
ROW232_STITCH_FIX_NEW = (
    "before row 233 dynamics meta prelude capstone reunion opens on the full capstone path."
)

ROW233_EPILOGUE_OLD = (
    "Proceed to [row 213](#row-213-closing-loop) when row 68 closed but dynamics meta prelude capstone still lags after row 212 on the full capstone path,"
)
ROW233_EPILOGUE_NEW = (
    "Proceed to [row 233](#row-233-closing-loop) when row 68 closed but dynamics meta prelude capstone still lags after row 232 on the full capstone path,"
)

ROW233_BABY_OLD = (
    "when opening [row 194](preface.md#skill-navigation-row-194) before row 54 closes on the full capstone path"
)
ROW233_BABY_NEW = (
    "when opening [row 214](preface.md#skill-navigation-row-214) before row 54 closes on the full capstone path"
)

ROW233_STITCH_OLD = (
    "before row 234 export meta prelude capstone reunion opens on the full capstone path."
)
ROW233_STITCH_NEW = (
    "before row 235 electronic audit meta prelude capstone reunion opens on the full capstone path."
)

PROLOGUE_STITCH_ANCHOR = (
    "**Row 233 closing stitch (Row 68 → Row 233 Row 68 → Row 53 dynamics meta prelude capstone reunion).** {#row-233-closing-stitch}"
)

ROW233_INSERT_MARKER = (
    "### Row 233 closing loop (Row 68 → Row 213 Row 68 → Row 53 "
    "dynamics meta prelude capstone reunion) {#row-233-closing-loop}"
)


def _insert_row234_epilogue(epilogue: str, proper_loop: str) -> str:
    if "### Row 234 closing loop" in epilogue:
        return epilogue
    if ROW233_INSERT_MARKER not in epilogue:
        raise SystemExit("epilogue row 233 insert anchor not found")
    return epilogue.replace(ROW233_INSERT_MARKER, proper_loop + "\n\n" + ROW233_INSERT_MARKER, 1)


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
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row234_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 234")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "export meta prelude capstone reunion (row 234) |" not in prologue:
        needle = "| Row 68 → Row 213 Row 68 → Row 53 dynamics meta prelude capstone reunion (row 233) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 233 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if PROLOGUE_STITCH_ANCHOR in prologue:
            prologue = prologue.replace(
                PROLOGUE_STITCH_ANCHOR,
                b["prologue_stitch"] + PROLOGUE_STITCH_ANCHOR,
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-233"></span>Row 233 preview'
        if preview_anchor not in prologue:
            preview_anchor = '| <span id="prologue-preview-row-232"></span>Row 232 preview'
        if preview_anchor not in prologue:
            preview_anchor = '| <span id="prologue-preview-row-214"></span>Row 194 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW233_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW233_STITCH_OLD, ROW233_STITCH_NEW)
        if ROW232_STITCH_FIX_OLD in prologue:
            prologue = prologue.replace(ROW232_STITCH_FIX_OLD, ROW232_STITCH_FIX_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 234")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if ROW233_EPILOGUE_OLD in epilogue:
        epilogue = epilogue.replace(ROW233_EPILOGUE_OLD, ROW233_EPILOGUE_NEW, 1)
    epilogue_new = _insert_row234_epilogue(epilogue, b["epilogue_loop"])
    if epilogue_new != epilogue:
        epilogue_path.write_text(epilogue_new)
        print("epilogue: added row 234")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row214-export-meta-prelude-capstone-reunion-index-row-234" not in sources:
        sources = sources.replace(
            "| 214 | Row 68 → Row 194 Row 68 → Row 54 export meta prelude capstone",
            b["sources_table"] + "| 214 | Row 68 → Row 194 Row 68 → Row 54 export meta prelude capstone",
            1,
        )
        src214_header = (
            "## Row 68 → Row 194 Row 68 → Row 54 export meta prelude capstone reunion index (row 214) "
            "{#row68-row194-export-meta-prelude-capstone-reunion-index-row-214}"
        )
        if src214_header not in sources:
            src214_header = (
                "## Row 68 → Row 194 Row 68 → Row 54 export meta prelude capstone reunion index (row 214)"
            )
        sources = sources.replace(
            src214_header,
            b["sources_index"] + src214_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 234")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-234-baby-picture-row68-row214" not in memory:
        memory = memory.replace(
            "| 214 | Meta | [Row 68 → Row 194 export meta prelude capstone reunion index]",
            b["memory_table"] + "| 214 | Meta | [Row 68 → Row 194 export meta prelude capstone reunion index]",
            1,
        )
        baby_anchor = (
            "### Row 214 baby picture {#row-214-baby-picture-row68-row194-export-meta-prelude-capstone-reunion}"
        )
        if baby_anchor not in memory:
            baby_anchor = "### Row 214 baby picture"
        if baby_anchor in memory:
            memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
        if ROW233_BABY_OLD in memory:
            memory = memory.replace(ROW233_BABY_OLD, ROW233_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 234")


if __name__ == "__main__":
    main()
