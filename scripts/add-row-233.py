#!/usr/bin/env python3
"""Add row 233 meta-stitch (Row 68 → Row 213 ↔ Row 53 dynamics meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util
import re

ROOT = Path(__file__).resolve().parents[1]


def shift_meta_bump(text: str, delta: int = 20) -> str:
    """Shift capstone-path row references (100–250) by delta for meta-stitch copy."""
    out = text
    for tag in ("__R213__", "__R214__", "__R232__", "__R233__", "__R234__"):
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


def bump213_to_233(text: str) -> str:
    protected = (
        ("row-233-", "__P233__"),
        ("skill-navigation-row-233", "__S233__"),
        ("prologue-preview-row-233", "__PR233__"),
        ("{#row-233-closing-stitch}", "__ST233__"),
        ("{#row-233-closing-loop}", "__LP233__"),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = shift_meta_bump(out, 20)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add213():
    spec = importlib.util.spec_from_file_location("add213", ROOT / "scripts/add-row-213.py")
    add213 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add213)
    return add213


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 213 skill checkpoint")
    end = preface.index("\n\n### Row 214 skill checkpoint", start)
    row233_preface = bump213_to_233(preface[start:end]) + "\n\n"

    b213 = _load_add213()._build_blocks()
    prologue_stitch = bump213_to_233(
        b213["prologue_stitch"]
        .replace("{#row-213-closing-stitch}", "{#row-233-closing-stitch}")
        .replace(
            "**Row 213 closing stitch (Row 68 → Row 193",
            "**Row 233 closing stitch (Row 68 → Row 213",
        )
        .replace(
            "**Row 193 closing stitch (Row 68 → Row 193",
            "**Row 233 closing stitch (Row 68 → Row 213",
        )
    ).replace("**Row 253 closing stitch", "**Row 233 closing stitch", 1)
    prologue_compass = bump213_to_233(b213["prologue_compass"]).replace(
        "dynamics meta prelude capstone reunion (row 213) |",
        "dynamics meta prelude capstone reunion (row 233) |",
        1,
    )
    prologue_preview = bump213_to_233(b213["prologue_preview"]).replace(
        "Row 213 preview", "Row 233 preview", 1
    )

    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    row213_loop_anchor = (
        "### Row 193 closing loop (Row 68 → Row 193 Row 68 → Row 53 "
        "dynamics meta prelude capstone reunion) {#row-213-closing-loop}"
    )
    row214_loop_end = (
        "### Row 194 closing loop (Row 68 → Row 194 Row 68 → Row 54 "
        "export meta prelude capstone reunion) {#row-214-closing-loop}"
    )
    if row213_loop_anchor in epilogue and row214_loop_end in epilogue.split(row213_loop_anchor, 1)[1]:
        ep_slice = row213_loop_anchor + epilogue.split(row213_loop_anchor, 1)[1].split(row214_loop_end, 1)[0]
    else:
        ep_slice = b213["epilogue_loop"]
    epilogue_loop = bump213_to_233(ep_slice)
    epilogue_loop = epilogue_loop.replace("{#row-213-closing-loop}", "{#row-233-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 213 closing loop (Row 68 → Row 213",
        "### Row 233 closing loop (Row 68 → Row 213",
        1,
    ).replace(
        "### Row 233 closing loop (Row 68 → Row 193",
        "### Row 233 closing loop (Row 68 → Row 213",
        1,
    )
    epilogue_loop = epilogue_loop.rstrip() + "\n\n"

    sources_index = bump213_to_233(b213["sources_index"])
    sources_index = sources_index.replace(
        "## Row 68 → Row 193 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 213) "
        "{#row68-row193-dynamics-meta-prelude-capstone-reunion-index-row-213}",
        "## Row 68 → Row 213 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 233) "
        "{#row68-row213-dynamics-meta-prelude-capstone-reunion-index-row-233}",
        1,
    )

    sources_table = bump213_to_233(b213["sources_table"])
    sources_table = sources_table.replace("| 213 | Row 68 → Row 213", "| 233 | Row 68 → Row 213", 1)
    if "| 233 | Row 68 → Row 213" not in sources_table:
        sources_table = sources_table.replace("| 213 | Row 68 → Row 193", "| 233 | Row 68 → Row 213", 1)

    memory_table = bump213_to_233(b213["memory_table"])
    memory_table = memory_table.replace("| 213 | Meta |", "| 233 | Meta |", 1)

    memory_baby = bump213_to_233(b213["memory_baby"]).rstrip() + "\n\n"
    memory_baby = memory_baby.replace(
        "### Row 233 baby picture {#row-213-baby-picture",
        "### Row 233 baby picture {#row-233-baby-picture-row68-row213-dynamics-meta-prelude-capstone-reunion} {#row-213-baby-picture",
        1,
    )
    if "{#row-233-baby-picture-row68-row213" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 233 baby picture",
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

ROW232_BABY_OLD = (
    "when opening [row 233](preface.md#skill-navigation-row-233) before row 52 closes on the full capstone path"
)
ROW232_BABY_NEW = (
    "when opening [row 234](preface.md#skill-navigation-row-234) before row 54 closes on the full capstone path"
)

ROW232_STITCH_OLD = (
    "before row 213 dynamics meta prelude capstone reunion opens on the full capstone path."
)
ROW232_STITCH_NEW = (
    "before row 234 export meta prelude capstone reunion opens on the full capstone path."
)

PROLOGUE_STITCH_ANCHOR = (
    "**Row 232 closing stitch (Row 68 → Row 212 Row 68 → Row 52 atomistic meta prelude capstone reunion).** {#row-232-closing-stitch}"
)

ROW232_INSERT_MARKER = (
    "### Row 232 closing loop (Row 68 → Row 212 Row 68 → Row 52 "
    "atomistic meta prelude capstone reunion) {#row-232-closing-loop}"
)


def _insert_row233_epilogue(epilogue: str, proper_loop: str) -> str:
    if "### Row 233 closing loop" in epilogue:
        return epilogue
    if ROW232_INSERT_MARKER not in epilogue:
        raise SystemExit("epilogue row 232 insert anchor not found")
    return epilogue.replace(ROW232_INSERT_MARKER, proper_loop + "\n\n" + ROW232_INSERT_MARKER, 1)


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
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row233_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 233")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "dynamics meta prelude capstone reunion (row 233) |" not in prologue:
        needle = "| Row 68 → Row 212 Row 68 → Row 52 atomistic meta prelude capstone reunion (row 232) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 232 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if PROLOGUE_STITCH_ANCHOR in prologue:
            prologue = prologue.replace(
                PROLOGUE_STITCH_ANCHOR,
                b["prologue_stitch"] + PROLOGUE_STITCH_ANCHOR,
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-232"></span>Row 232 preview'
        if preview_anchor not in prologue:
            preview_anchor = '| <span id="prologue-preview-row-231"></span>Row 231 preview'
        if preview_anchor not in prologue:
            preview_anchor = '| <span id="prologue-preview-row-213"></span>Row 193 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW232_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW232_STITCH_OLD, ROW232_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 233")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if ROW232_EPILOGUE_OLD in epilogue:
        epilogue = epilogue.replace(ROW232_EPILOGUE_OLD, ROW232_EPILOGUE_NEW, 1)
    epilogue_new = _insert_row233_epilogue(epilogue, b["epilogue_loop"])
    if epilogue_new != epilogue:
        epilogue_path.write_text(epilogue_new)
        print("epilogue: added row 233")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row213-dynamics-meta-prelude-capstone-reunion-index-row-233" not in sources:
        sources = sources.replace(
            "| 213 | Row 68 → Row 193 Row 68 → Row 53 dynamics meta prelude capstone",
            b["sources_table"] + "| 213 | Row 68 → Row 193 Row 68 → Row 53 dynamics meta prelude capstone",
            1,
        )
        src213_header = (
            "## Row 68 → Row 193 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 213) "
            "{#row68-row193-dynamics-meta-prelude-capstone-reunion-index-row-213}"
        )
        sources = sources.replace(
            src213_header,
            b["sources_index"] + src213_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 233")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-233-baby-picture-row68-row213" not in memory:
        memory = memory.replace(
            "| 213 | Meta | [Row 68 → Row 193 dynamics meta prelude capstone reunion index]",
            b["memory_table"] + "| 213 | Meta | [Row 68 → Row 193 dynamics meta prelude capstone reunion index]",
            1,
        )
        baby_anchor = (
            "### Row 213 baby picture {#row-213-baby-picture-row68-row193-dynamics-meta-prelude-capstone-reunion}"
        )
        if baby_anchor not in memory:
            baby_anchor = "### Row 213 baby picture"
        memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
        if ROW232_BABY_OLD in memory:
            memory = memory.replace(ROW232_BABY_OLD, ROW232_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 233")


if __name__ == "__main__":
    main()
