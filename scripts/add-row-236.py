#!/usr/bin/env python3
"""Add row 236 meta-stitch (Row 68 → Row 216 ↔ Row 56 Born–Oppenheimer meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util
import re

ROOT = Path(__file__).resolve().parents[1]


def shift_meta_bump(text: str, delta: int = 20) -> str:
    """Shift capstone-path row references (100–250) by delta for meta-stitch copy."""
    out = text
    for tag in ("__R216__", "__R217__", "__R235__", "__R236__", "__R237__"):
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


def bump216_to_236(text: str) -> str:
    protected = (
        ("row-236-", "__P236__"),
        ("skill-navigation-row-236", "__S236__"),
        ("prologue-preview-row-236", "__PR236__"),
        ("{#row-236-closing-stitch}", "__ST236__"),
        ("{#row-236-closing-loop}", "__LP236__"),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = shift_meta_bump(out, 20)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add216():
    spec = importlib.util.spec_from_file_location("add216", ROOT / "scripts/add-row-216.py")
    add216 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add216)
    return add216


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 216 skill checkpoint")
    end = preface.index("\n\n### Row 217 skill checkpoint", start)
    row236_preface = bump216_to_236(preface[start:end]) + "\n\n"

    b216 = _load_add216()._build_blocks()
    prologue_stitch = bump216_to_236(
        b216["prologue_stitch"]
        .replace("{#row-216-closing-stitch}", "{#row-236-closing-stitch}")
        .replace(
            "**Row 216 closing stitch (Row 68 → Row 196",
            "**Row 236 closing stitch (Row 68 → Row 216",
        )
        .replace(
            "**Row 196 closing stitch (Row 68 → Row 196",
            "**Row 236 closing stitch (Row 68 → Row 216",
        )
    ).replace("**Row 256 closing stitch", "**Row 236 closing stitch", 1)
    prologue_compass = bump216_to_236(b216["prologue_compass"]).replace(
        "Born–Oppenheimer meta prelude capstone reunion (row 216) |",
        "Born–Oppenheimer meta prelude capstone reunion (row 236) |",
        1,
    )
    prologue_preview = bump216_to_236(b216["prologue_preview"]).replace(
        "Row 216 preview", "Row 236 preview", 1
    )

    epilogue_loop = bump216_to_236(b216["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace("{#row-216-closing-loop}", "{#row-236-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 216 closing loop (Row 68 → Row 196",
        "### Row 236 closing loop (Row 68 → Row 216",
        1,
    ).replace(
        "### Row 236 closing loop (Row 68 → Row 196",
        "### Row 236 closing loop (Row 68 → Row 216",
        1,
    )
    for spill in (
        "\n\n\n\n### Row 217 closing loop",
        "\n\n\n\n### Row 197 closing loop",
    ):
        if spill in epilogue_loop:
            epilogue_loop = epilogue_loop.split(spill, 1)[0].rstrip() + "\n\n"
            break
    epilogue_loop = epilogue_loop.rstrip() + "\n\n"

    sources_index = bump216_to_236(b216["sources_index"])
    sources_index = sources_index.replace(
        "## Row 68 → Row 196 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion index (row 216) "
        "{#row68-row196-born-oppenheimer-meta-prelude-capstone-reunion-index-row-216}",
        "## Row 68 → Row 216 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion index (row 236) "
        "{#row68-row216-born-oppenheimer-meta-prelude-capstone-reunion-index-row-236}",
        1,
    )

    sources_table = bump216_to_236(b216["sources_table"])
    sources_table = re.sub(
        r"^\| 216 \| Row 68 → Row 216",
        "| 236 | Row 68 → Row 216",
        sources_table,
        count=1,
        flags=re.MULTILINE,
    )
    if "| 236 | Row 68 → Row 216" not in sources_table:
        sources_table = sources_table.replace(
            "| 216 | Row 68 → Row 196", "| 236 | Row 68 → Row 216", 1
        )

    memory_table = bump216_to_236(b216["memory_table"])
    memory_table = memory_table.replace("| 216 | Meta |", "| 236 | Meta |", 1)

    memory_baby = bump216_to_236(b216["memory_baby"]).rstrip() + "\n\n"
    memory_baby = memory_baby.replace(
        "### Row 236 baby picture {#row-216-baby-picture",
        "### Row 236 baby picture {#row-236-baby-picture-row68-row216-born-oppenheimer-meta-prelude-capstone-reunion} {#row-216-baby-picture",
        1,
    )
    if "{#row-236-baby-picture-row68-row216" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 236 baby picture",
            "### Row 236 baby picture {#row-236-baby-picture-row68-row216-born-oppenheimer-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row236_preface": row236_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW234_STITCH_FIX_OLD = (
    "before row 236 Born–Oppenheimer meta prelude capstone reunion opens on the full capstone path."
)
ROW234_STITCH_FIX_NEW = (
    "before row 235 electronic audit meta prelude capstone reunion opens on the full capstone path."
)

ROW235_EPILOGUE_OLD = (
    "Proceed to [row 216](#row-216-closing-loop) when row 68 closed but Born–Oppenheimer meta prelude capstone still lags after row 215 on the full capstone path,"
)
ROW235_EPILOGUE_NEW = (
    "Proceed to [row 236](#row-236-closing-loop) when row 68 closed but Born–Oppenheimer meta prelude capstone still lags after row 235 on the full capstone path,"
)

ROW235_BABY_OLD = (
    "when opening [row 176](preface.md#skill-navigation-row-176) before row 56 closes on the full capstone path"
)
ROW235_BABY_NEW = (
    "when opening [row 236](preface.md#skill-navigation-row-236) before row 56 closes on the full capstone path"
)

ROW235_STITCH_OLD = (
    "before row 236 Born–Oppenheimer meta prelude capstone reunion opens on the full capstone path."
)
ROW235_STITCH_NEW = (
    "before row 237 Kohn–Sham meta prelude capstone reunion opens on the full capstone path."
)

ROW235_TAIL_OLD = (
    "When row 235 is complete, proceed to [row 236](preface.md#skill-navigation-row-236) when `cu.relax.out` exists on the full capstone path, to [row 216](preface.md#skill-navigation-row-216) when `cu.relax.out` exists but IX.1 still feels disconnected from verified electronic audit meta prelude capstone on the opening-hinge capstone path alone, to [row 196](preface.md#skill-navigation-row-196) for the Row 68 ↔ Row 56 Born–Oppenheimer meta audit on the opening-hinge prelude path alone, to [row 235](preface.md#skill-navigation-row-235) for the Row 68 ↔ Row 55 electronic audit meta audit on the opening-hinge capstone path alone, to [row 234](preface.md#skill-navigation-row-234) when yaml exports still stall after verified export meta prelude capstone on the full capstone path, to [row 56](preface.md#skill-navigation-row-56) when only IX.0 → IX.1 stalls, or extend prose only under `writings/` then sync."
)
ROW235_TAIL_NEW = (
    "When row 235 is complete, proceed to [row 236](preface.md#skill-navigation-row-236) when `cu.relax.out` exists on the full capstone path, to [row 216](preface.md#skill-navigation-row-216) when `cu.relax.out` exists but IX.1 still feels disconnected from verified electronic audit meta prelude capstone on the opening-hinge capstone path alone, to [row 216](preface.md#skill-navigation-row-216) for the Row 68 ↔ Row 56 Born–Oppenheimer meta audit on the opening-hinge prelude path alone, to [row 235](preface.md#skill-navigation-row-235) for the Row 68 ↔ Row 55 electronic audit meta audit on the opening-hinge capstone path alone, to [row 234](preface.md#skill-navigation-row-234) when yaml exports still stall after verified export meta prelude capstone on the full capstone path, to [row 56](preface.md#skill-navigation-row-56) when only IX.0 → IX.1 stalls, or extend prose only under `writings/` then sync."
)

PROLOGUE_STITCH_ANCHOR = (
    "**Row 235 closing stitch (Row 68 → Row 235 Row 68 → Row 55 electronic audit meta prelude capstone reunion).** {#row-235-closing-stitch}"
)

ROW235_INSERT_MARKER = (
    "### Row 235 closing loop (Row 68 → Row 215 Row 68 → Row 55 "
    "electronic audit meta prelude capstone reunion) {#row-235-closing-loop}"
)


def _insert_row236_epilogue(epilogue: str, proper_loop: str) -> str:
    if "### Row 236 closing loop" in epilogue:
        return epilogue
    if ROW235_INSERT_MARKER not in epilogue:
        raise SystemExit("epilogue row 235 insert anchor not found")
    return epilogue.replace(ROW235_INSERT_MARKER, proper_loop + "\n\n" + ROW235_INSERT_MARKER, 1)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 236 skill checkpoint" in preface:
        print("preface: row 236 already present")
    else:
        if "### Row 235 skill checkpoint" not in preface:
            raise SystemExit("row 235 must exist before row 236")
        if ROW235_TAIL_OLD in preface:
            preface = preface.replace(ROW235_TAIL_OLD, ROW235_TAIL_NEW, 1)
        elif ROW235_TAIL_NEW in preface:
            print("preface: row 235 tail already updated")
        else:
            raise SystemExit("row 235 tail proceed string not found")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row236_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 236")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "Born–Oppenheimer meta prelude capstone reunion (row 236) |" not in prologue:
        needle = "| Row 68 → Row 215 Row 68 → Row 55 electronic audit meta prelude capstone reunion (row 235) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 235 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if PROLOGUE_STITCH_ANCHOR in prologue:
            prologue = prologue.replace(
                PROLOGUE_STITCH_ANCHOR,
                b["prologue_stitch"] + PROLOGUE_STITCH_ANCHOR,
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-235"></span>Row 235 preview'
        if preview_anchor not in prologue:
            preview_anchor = '| <span id="prologue-preview-row-234"></span>Row 234 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW235_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW235_STITCH_OLD, ROW235_STITCH_NEW)
        if ROW234_STITCH_FIX_OLD in prologue:
            prologue = prologue.replace(ROW234_STITCH_FIX_OLD, ROW234_STITCH_FIX_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 236")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if ROW235_EPILOGUE_OLD in epilogue:
        epilogue = epilogue.replace(ROW235_EPILOGUE_OLD, ROW235_EPILOGUE_NEW, 1)
    epilogue_new = _insert_row236_epilogue(epilogue, b["epilogue_loop"])
    if epilogue_new != epilogue:
        epilogue_path.write_text(epilogue_new)
        print("epilogue: added row 236")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row216-born-oppenheimer-meta-prelude-capstone-reunion-index-row-236" not in sources:
        sources = sources.replace(
            "| 216 | Row 68 → Row 196 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone",
            b["sources_table"] + "| 216 | Row 68 → Row 196 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone",
            1,
        )
        src216_header = (
            "## Row 68 → Row 196 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion index (row 216) "
            "{#row68-row196-born-oppenheimer-meta-prelude-capstone-reunion-index-row-216}"
        )
        if src216_header not in sources:
            src216_header = (
                "## Row 68 → Row 196 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion index (row 216)"
            )
        sources = sources.replace(
            src216_header,
            b["sources_index"] + src216_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 236")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-236-baby-picture-row68-row216" not in memory:
        memory = memory.replace(
            "| 216 | Meta | [Row 68 → Row 196 Born–Oppenheimer meta prelude capstone reunion index]",
            b["memory_table"] + "| 216 | Meta | [Row 68 → Row 196 Born–Oppenheimer meta prelude capstone reunion index]",
            1,
        )
        baby_anchor = (
            "### Row 216 baby picture {#row-216-baby-picture-row68-row196-born-oppenheimer-meta-prelude-capstone-reunion}"
        )
        if baby_anchor not in memory:
            baby_anchor = "### Row 216 baby picture"
        if baby_anchor in memory:
            memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
        if ROW235_BABY_OLD in memory:
            memory = memory.replace(ROW235_BABY_OLD, ROW235_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 236")


if __name__ == "__main__":
    main()
