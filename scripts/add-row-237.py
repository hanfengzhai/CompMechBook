#!/usr/bin/env python3
"""Add row 237 meta-stitch (Row 68 → Row 217 ↔ Row 57 Kohn–Sham meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util
import re

ROOT = Path(__file__).resolve().parents[1]


def shift_meta_bump(text: str, delta: int = 20) -> str:
    """Shift capstone-path row references (100–250) by delta for meta-stitch copy."""
    out = text
    for tag in ("__R217__", "__R218__", "__R236__", "__R237__", "__R238__"):
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


def bump217_to_237(text: str) -> str:
    protected = (
        ("row-237-", "__P237__"),
        ("skill-navigation-row-237", "__S237__"),
        ("prologue-preview-row-237", "__PR237__"),
        ("{#row-237-closing-stitch}", "__ST237__"),
        ("{#row-237-closing-loop}", "__LP237__"),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = shift_meta_bump(out, 20)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add217():
    spec = importlib.util.spec_from_file_location("add217", ROOT / "scripts/add-row-217.py")
    add217 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add217)
    return add217


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 217 skill checkpoint")
    end = preface.index("\n\n### Row 218 skill checkpoint", start)
    row237_preface = bump217_to_237(preface[start:end]) + "\n\n"

    b217 = _load_add217()._build_blocks()
    prologue_stitch = bump217_to_237(
        b217["prologue_stitch"]
        .replace("{#row-217-closing-stitch}", "{#row-237-closing-stitch}")
        .replace(
            "**Row 217 closing stitch (Row 68 → Row 197",
            "**Row 237 closing stitch (Row 68 → Row 217",
        )
        .replace(
            "**Row 197 closing stitch (Row 68 → Row 177",
            "**Row 237 closing stitch (Row 68 → Row 217",
        )
    ).replace("**Row 257 closing stitch", "**Row 237 closing stitch", 1)
    prologue_compass = bump217_to_237(b217["prologue_compass"]).replace(
        "Kohn–Sham meta prelude capstone reunion (row 217) |",
        "Kohn–Sham meta prelude capstone reunion (row 237) |",
        1,
    )
    prologue_preview = bump217_to_237(b217["prologue_preview"]).replace(
        "Row 217 preview", "Row 237 preview", 1
    )

    epilogue_loop = bump217_to_237(b217["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace("{#row-217-closing-loop}", "{#row-237-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 217 closing loop (Row 68 → Row 197",
        "### Row 237 closing loop (Row 68 → Row 217",
        1,
    ).replace(
        "### Row 237 closing loop (Row 68 → Row 197",
        "### Row 237 closing loop (Row 68 → Row 217",
        1,
    )
    for spill in (
        "\n\n\n\n### Row 218 closing loop",
        "\n\n\n\n### Row 198 closing loop",
    ):
        if spill in epilogue_loop:
            epilogue_loop = epilogue_loop.split(spill, 1)[0].rstrip() + "\n\n"
            break
    epilogue_loop = epilogue_loop.rstrip() + "\n\n"

    sources_index = bump217_to_237(b217["sources_index"])
    sources_index = sources_index.replace(
        "## Row 68 → Row 197 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion index (row 217) "
        "{#row68-row197-kohn-sham-meta-prelude-capstone-reunion-index-row-217}",
        "## Row 68 → Row 217 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion index (row 237) "
        "{#row68-row217-kohn-sham-meta-prelude-capstone-reunion-index-row-237}",
        1,
    )

    sources_table = bump217_to_237(b217["sources_table"])
    sources_table = re.sub(
        r"^\| 217 \| Row 68 → Row 217",
        "| 237 | Row 68 → Row 217",
        sources_table,
        count=1,
        flags=re.MULTILINE,
    )
    if "| 237 | Row 68 → Row 217" not in sources_table:
        sources_table = sources_table.replace(
            "| 217 | Row 68 → Row 197", "| 237 | Row 68 → Row 217", 1
        )

    memory_table = bump217_to_237(b217["memory_table"])
    memory_table = memory_table.replace("| 217 | Meta |", "| 237 | Meta |", 1)

    memory_baby = bump217_to_237(b217["memory_baby"]).rstrip() + "\n\n"
    memory_baby = memory_baby.replace(
        "### Row 237 baby picture {#row-217-baby-picture",
        "### Row 237 baby picture {#row-237-baby-picture-row68-row217-kohn-sham-meta-prelude-capstone-reunion} {#row-217-baby-picture",
        1,
    )
    if "{#row-237-baby-picture-row68-row217" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 237 baby picture",
            "### Row 237 baby picture {#row-237-baby-picture-row68-row217-kohn-sham-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row237_preface": row237_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW236_TAIL_OLD = (
    "When row 236 is complete, proceed to [row 237](preface.md#skill-navigation-row-237) when `murnaghan_eos.yaml` exists on the full capstone path, to [row 197](preface.md#skill-navigation-row-197) when `murnaghan_eos.yaml` exists but IX.2 still feels disconnected from verified Born–Oppenheimer meta prelude capstone on the opening-hinge capstone path alone, to [row 177](preface.md#skill-navigation-row-177) for the Row 68 ↔ Row 57 Kohn–Sham meta audit on the opening-hinge prelude path alone, to [row 216](preface.md#skill-navigation-row-216) for the Row 68 ↔ Row 56 Born–Oppenheimer meta audit on the opening-hinge capstone path alone, to [row 214](preface.md#skill-navigation-row-214) when `cu.relax.out` is missing after verified export meta prelude capstone on the full capstone path, to [row 57](preface.md#skill-navigation-row-57) when only IX.1 → IX.2 stalls, or extend prose only under `writings/` then sync."
)
ROW236_TAIL_NEW = (
    "When row 236 is complete, proceed to [row 237](preface.md#skill-navigation-row-237) when `murnaghan_eos.yaml` exists on the full capstone path, to [row 217](preface.md#skill-navigation-row-217) when `murnaghan_eos.yaml` exists but IX.2 still feels disconnected from verified Born–Oppenheimer meta prelude capstone on the opening-hinge capstone path alone, to [row 197](preface.md#skill-navigation-row-197) for the Row 68 ↔ Row 57 Kohn–Sham meta audit on the opening-hinge prelude path alone, to [row 236](preface.md#skill-navigation-row-236) for the Row 68 ↔ Row 56 Born–Oppenheimer meta audit on the opening-hinge capstone path alone, to [row 234](preface.md#skill-navigation-row-234) when `cu.relax.out` is missing after verified export meta prelude capstone on the full capstone path, to [row 57](preface.md#skill-navigation-row-57) when only IX.1 → IX.2 stalls, or extend prose only under `writings/` then sync."
)

ROW236_EPILOGUE_OLD = (
    "Proceed to [row 217](#row-217-closing-loop) when row 68 closed but Kohn–Sham meta prelude capstone still lags after row 216 on the full capstone path,"
)
ROW236_EPILOGUE_NEW = (
    "Proceed to [row 237](#row-237-closing-loop) when row 68 closed but Kohn–Sham meta prelude capstone still lags after row 236 on the full capstone path,"
)

ROW236_STITCH_OLD = (
    "before row 237 Kohn–Sham meta prelude capstone reunion opens on the full capstone path."
)
ROW236_STITCH_NEW = (
    "before row 238 DFT workflows meta prelude capstone reunion opens on the full capstone path."
)

PROLOGUE_STITCH_ANCHOR = (
    "**Row 236 closing stitch (Row 68 → Row 236 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion).** {#row-236-closing-stitch}"
)

ROW236_INSERT_MARKER = (
    "### Row 216 closing loop (Row 68 → Row 216 Row 68 → Row 56 "
    "Born–Oppenheimer meta prelude capstone reunion) {#row-236-closing-loop}"
)


def _insert_row237_epilogue(epilogue: str, proper_loop: str) -> str:
    if "### Row 237 closing loop" in epilogue:
        return epilogue
    if ROW236_INSERT_MARKER not in epilogue:
        raise SystemExit("epilogue row 236 insert anchor not found")
    return epilogue.replace(ROW236_INSERT_MARKER, proper_loop + "\n\n" + ROW236_INSERT_MARKER, 1)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 237 skill checkpoint" in preface:
        print("preface: row 237 already present")
    else:
        if "### Row 236 skill checkpoint" not in preface:
            raise SystemExit("row 236 must exist before row 237")
        if ROW236_TAIL_OLD in preface:
            preface = preface.replace(ROW236_TAIL_OLD, ROW236_TAIL_NEW, 1)
        elif ROW236_TAIL_NEW in preface:
            print("preface: row 236 tail already updated")
        else:
            raise SystemExit("row 236 tail proceed string not found")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row237_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 237")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "Kohn–Sham meta prelude capstone reunion (row 237) |" not in prologue:
        needle = "| Row 68 → Row 216 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion (row 236) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 236 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if PROLOGUE_STITCH_ANCHOR in prologue:
            prologue = prologue.replace(
                PROLOGUE_STITCH_ANCHOR,
                b["prologue_stitch"] + PROLOGUE_STITCH_ANCHOR,
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-236"></span>Row 236 preview'
        if preview_anchor not in prologue:
            preview_anchor = '| <span id="prologue-preview-row-235"></span>Row 235 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW236_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW236_STITCH_OLD, ROW236_STITCH_NEW, 1)
        prologue_path.write_text(prologue)
        print("prologue: added row 237")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if ROW236_EPILOGUE_OLD in epilogue:
        epilogue = epilogue.replace(ROW236_EPILOGUE_OLD, ROW236_EPILOGUE_NEW, 1)
    epilogue_new = _insert_row237_epilogue(epilogue, b["epilogue_loop"])
    if epilogue_new != epilogue:
        epilogue_path.write_text(epilogue_new)
        print("epilogue: added row 237")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row217-kohn-sham-meta-prelude-capstone-reunion-index-row-237" not in sources:
        sources = sources.replace(
            "| 217 | Row 68 → Row 197 Row 68 → Row 57 Kohn–Sham meta prelude capstone",
            b["sources_table"] + "| 217 | Row 68 → Row 197 Row 68 → Row 57 Kohn–Sham meta prelude capstone",
            1,
        )
        src217_header = (
            "## Row 68 → Row 197 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion index (row 217) "
            "{#row68-row197-kohn-sham-meta-prelude-capstone-reunion-index-row-217}"
        )
        if src217_header not in sources:
            src217_header = (
                "## Row 68 → Row 197 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion index (row 217)"
            )
        sources = sources.replace(
            src217_header,
            b["sources_index"] + src217_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 237")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-237-baby-picture-row68-row217" not in memory:
        memory = memory.replace(
            "| 217 | Meta | [Row 68 → Row 197 Kohn–Sham meta prelude capstone reunion index]",
            b["memory_table"] + "| 217 | Meta | [Row 68 → Row 197 Kohn–Sham meta prelude capstone reunion index]",
            1,
        )
        baby_anchor = (
            "### Row 217 baby picture {#row-217-baby-picture-row68-row197-kohn-sham-meta-prelude-capstone-reunion}"
        )
        if baby_anchor not in memory:
            baby_anchor = "### Row 217 baby picture"
        if baby_anchor in memory:
            memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
        memory_path.write_text(memory)
        print("memory-sheet: added row 237")


if __name__ == "__main__":
    main()
