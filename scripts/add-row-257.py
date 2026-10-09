#!/usr/bin/env python3
"""Add row 257 meta-stitch (Row 68 → Row 237 ↔ Row 57 Kohn–Sham meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util
import re

ROOT = Path(__file__).resolve().parents[1]


def shift_meta_bump(text: str, delta: int = 20) -> str:
    """Shift capstone-path row references (100–250) by delta for meta-stitch copy."""
    out = text
    for tag in ("__R237__", "__R238__", "__R256__", "__R257__", "__R258__"):
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


def bump237_to_257(text: str) -> str:
    protected = (
        ("row-257-", "__P257__"),
        ("skill-navigation-row-257", "__S257__"),
        ("prologue-preview-row-257", "__PR257__"),
        ("{#row-257-closing-stitch}", "__ST257__"),
        ("{#row-257-closing-loop}", "__LP257__"),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = shift_meta_bump(out, 20)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add237():
    spec = importlib.util.spec_from_file_location("add237", ROOT / "scripts/add-row-237.py")
    add237 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add237)
    return add237


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 237 skill checkpoint")
    end = preface.index("\n\n### Row 238 skill checkpoint", start)
    row257_preface = bump237_to_257(preface[start:end]) + "\n\n"

    b237 = _load_add237()._build_blocks()
    prologue_stitch = bump237_to_257(
        b237["prologue_stitch"]
        .replace("{#row-237-closing-stitch}", "{#row-257-closing-stitch}")
        .replace(
            "**Row 237 closing stitch (Row 68 → Row 217",
            "**Row 257 closing stitch (Row 68 → Row 237",
        )
        .replace(
            "**Row 217 closing stitch (Row 68 → Row 177",
            "**Row 257 closing stitch (Row 68 → Row 237",
        )
    ).replace("**Row 257 closing stitch", "**Row 257 closing stitch", 1)
    prologue_compass = bump237_to_257(b237["prologue_compass"]).replace(
        "Kohn–Sham meta prelude capstone reunion (row 257) |",
        "Kohn–Sham meta prelude capstone reunion (row 257) |",
        1,
    )
    prologue_preview = bump237_to_257(b237["prologue_preview"]).replace(
        "Row 237 preview", "Row 257 preview", 1
    )

    epilogue_loop = bump237_to_257(b237["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace("{#row-237-closing-loop}", "{#row-257-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 237 closing loop (Row 68 → Row 217",
        "### Row 257 closing loop (Row 68 → Row 237",
        1,
    ).replace(
        "### Row 257 closing loop (Row 68 → Row 217",
        "### Row 257 closing loop (Row 68 → Row 237",
        1,
    )
    for spill in (
        "\n\n\n\n### Row 238 closing loop",
        "\n\n\n\n### Row 198 closing loop",
    ):
        if spill in epilogue_loop:
            epilogue_loop = epilogue_loop.split(spill, 1)[0].rstrip() + "\n\n"
            break
    epilogue_loop = epilogue_loop.rstrip() + "\n\n"

    sources_index = bump237_to_257(b237["sources_index"])
    sources_index = sources_index.replace(
        "## Row 68 → Row 217 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion index (row 237) "
        "{#row68-row197-kohn-sham-meta-prelude-capstone-reunion-index-row-237}",
        "## Row 68 → Row 237 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion index (row 257) "
        "{#row68-row237-kohn-sham-meta-prelude-capstone-reunion-index-row-257}",
        1,
    )

    sources_table = bump237_to_257(b237["sources_table"])
    sources_table = re.sub(
        r"^\| 237 \| Row 68 → Row 237",
        "| 257 | Row 68 → Row 237",
        sources_table,
        count=1,
        flags=re.MULTILINE,
    )
    if "| 257 | Row 68 → Row 237" not in sources_table:
        sources_table = sources_table.replace(
            "| 237 | Row 68 → Row 217", "| 257 | Row 68 → Row 237", 1
        )

    memory_table = bump237_to_257(b237["memory_table"])
    memory_table = memory_table.replace("| 237 | Meta |", "| 257 | Meta |", 1)

    memory_baby = bump237_to_257(b237["memory_baby"]).rstrip() + "\n\n"
    memory_baby = memory_baby.replace(
        "### Row 257 baby picture {#row-237-baby-picture",
        "### Row 257 baby picture {#row-257-baby-picture-row68-row237-kohn-sham-meta-prelude-capstone-reunion} {#row-237-baby-picture",
        1,
    )
    if "{#row-257-baby-picture-row68-row237" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 257 baby picture",
            "### Row 257 baby picture {#row-257-baby-picture-row68-row237-kohn-sham-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row257_preface": row257_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW256_TAIL_OLD = (
    "When row 256 is complete, proceed to [row 257](preface.md#skill-navigation-row-257) when `murnaghan_eos.yaml` exists on the full capstone path, to [row 217](preface.md#skill-navigation-row-197) when `murnaghan_eos.yaml` exists but IX.2 still feels disconnected from verified Born–Oppenheimer meta prelude capstone on the opening-hinge capstone path alone, to [row 177](preface.md#skill-navigation-row-177) for the Row 68 ↔ Row 57 Kohn–Sham meta audit on the opening-hinge prelude path alone, to [row 236](preface.md#skill-navigation-row-236) for the Row 68 ↔ Row 56 Born–Oppenheimer meta audit on the opening-hinge capstone path alone, to [row 214](preface.md#skill-navigation-row-214) when `cu.relax.out` is missing after verified export meta prelude capstone on the full capstone path, to [row 57](preface.md#skill-navigation-row-57) when only IX.1 → IX.2 stalls, or extend prose only under `writings/` then sync."
)
ROW256_TAIL_NEW = (
    "When row 256 is complete, proceed to [row 257](preface.md#skill-navigation-row-257) when `murnaghan_eos.yaml` exists on the full capstone path, to [row 237](preface.md#skill-navigation-row-237) when `murnaghan_eos.yaml` exists but IX.2 still feels disconnected from verified Born–Oppenheimer meta prelude capstone on the opening-hinge capstone path alone, to [row 217](preface.md#skill-navigation-row-197) for the Row 68 ↔ Row 57 Kohn–Sham meta audit on the opening-hinge prelude path alone, to [row 256](preface.md#skill-navigation-row-256) for the Row 68 ↔ Row 56 Born–Oppenheimer meta audit on the opening-hinge capstone path alone, to [row 234](preface.md#skill-navigation-row-234) when `cu.relax.out` is missing after verified export meta prelude capstone on the full capstone path, to [row 57](preface.md#skill-navigation-row-57) when only IX.1 → IX.2 stalls, or extend prose only under `writings/` then sync."
)

ROW256_EPILOGUE_OLD = (
    "Proceed to [row 237](#row-237-closing-loop) when row 68 closed but Kohn–Sham meta prelude capstone still lags after row 256 on the full capstone path,"
)
ROW256_EPILOGUE_NEW = (
    "Proceed to [row 257](#row-257-closing-loop) when row 68 closed but Kohn–Sham meta prelude capstone still lags after row 256 on the full capstone path,"
)

ROW256_STITCH_OLD = (
    "before row 257 Kohn–Sham meta prelude capstone reunion opens on the full capstone path."
)
ROW256_STITCH_NEW = (
    "before row 258 DFT workflows meta prelude capstone reunion opens on the full capstone path."
)

PROLOGUE_STITCH_ANCHOR = (
    "**Row 256 closing stitch (Row 68 → Row 256 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion).** {#row-256-closing-stitch}"
)

ROW256_INSERT_MARKER = (
    "### Row 216 closing loop (Row 68 → Row 216 Row 68 → Row 56 "
    "Born–Oppenheimer meta prelude capstone reunion) {#row-236-closing-loop}"
)


def _insert_row257_epilogue(epilogue: str, proper_loop: str) -> str:
    if "### Row 257 closing loop" in epilogue:
        return epilogue
    if ROW256_INSERT_MARKER not in epilogue:
        raise SystemExit("epilogue row 256 insert anchor not found")
    return epilogue.replace(ROW256_INSERT_MARKER, proper_loop + "\n\n" + ROW256_INSERT_MARKER, 1)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 257 skill checkpoint" in preface:
        print("preface: row 257 already present")
    else:
        if "### Row 256 skill checkpoint" not in preface:
            raise SystemExit("row 256 must exist before row 257")
        if "When row 256 is complete, proceed to [row 257]" in preface:
            print("preface: row 256 tail already has row 257 proceed")
        elif ROW256_TAIL_OLD in preface:
            preface = preface.replace(ROW256_TAIL_OLD, ROW256_TAIL_NEW, 1)
        elif ROW256_TAIL_NEW in preface:
            print("preface: row 256 tail already updated")
        else:
            raise SystemExit("row 256 tail proceed string not found")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row257_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 257")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "Kohn–Sham meta prelude capstone reunion (row 257) |" not in prologue:
        needle = "| Row 68 → Row 216 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion (row 236) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 256 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if PROLOGUE_STITCH_ANCHOR in prologue:
            prologue = prologue.replace(
                PROLOGUE_STITCH_ANCHOR,
                b["prologue_stitch"] + PROLOGUE_STITCH_ANCHOR,
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-256"></span>Row 256 preview'
        if preview_anchor not in prologue:
            preview_anchor = '| <span id="prologue-preview-row-235"></span>Row 235 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW256_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW256_STITCH_OLD, ROW256_STITCH_NEW, 1)
        prologue_path.write_text(prologue)
        print("prologue: added row 257")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if ROW256_EPILOGUE_OLD in epilogue:
        epilogue = epilogue.replace(ROW256_EPILOGUE_OLD, ROW256_EPILOGUE_NEW, 1)
    epilogue_new = _insert_row257_epilogue(epilogue, b["epilogue_loop"])
    if epilogue_new != epilogue:
        epilogue_path.write_text(epilogue_new)
        print("epilogue: added row 257")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row237-kohn-sham-meta-prelude-capstone-reunion-index-row-257" not in sources:
        sources = sources.replace(
            "| 237 | Row 68 → Row 217 Row 68 → Row 57 Kohn–Sham meta prelude capstone",
            b["sources_table"] + "| 237 | Row 68 → Row 217 Row 68 → Row 57 Kohn–Sham meta prelude capstone",
            1,
        )
        src237_header = (
            "## Row 68 → Row 217 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion index (row 237) "
            "{#row68-row197-kohn-sham-meta-prelude-capstone-reunion-index-row-237}"
        )
        if src237_header not in sources:
            src237_header = (
                "## Row 68 → Row 217 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion index (row 237)"
            )
        sources = sources.replace(
            src237_header,
            b["sources_index"] + src237_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 257")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-257-baby-picture-row68-row237" not in memory:
        memory = memory.replace(
            "| 237 | Meta | [Row 68 → Row 217 Kohn–Sham meta prelude capstone reunion index]",
            b["memory_table"] + "| 237 | Meta | [Row 68 → Row 217 Kohn–Sham meta prelude capstone reunion index]",
            1,
        )
        baby_anchor = (
            "### Row 237 baby picture {#row-237-baby-picture-row68-row197-kohn-sham-meta-prelude-capstone-reunion}"
        )
        if baby_anchor not in memory:
            baby_anchor = "### Row 237 baby picture"
        if baby_anchor in memory:
            memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
        memory_path.write_text(memory)
        print("memory-sheet: added row 257")


if __name__ == "__main__":
    main()
