#!/usr/bin/env python3
"""Add row 257 meta-stitch (Row 68 → Row 257 ↔ Row 57 Kohn–Sham meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util
import re

ROOT = Path(__file__).resolve().parents[1]


def shift_meta_bump(text: str, delta: int = 20) -> str:
    """Shift capstone-path row references (100–270) by delta for meta-stitch copy."""
    out = text
    for tag in ("__R237__", "__R238__", "__R256__", "__R257__", "__R258__"):
        out = out.replace(tag, tag)

    def in_band(n: int) -> bool:
        return 100 <= n <= 270

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
            "**Row 217 closing stitch (Row 68 → Row 197",
            "**Row 257 closing stitch (Row 68 → Row 237",
        )
    ).replace("**Row 257 closing stitch", "**Row 257 closing stitch", 1)
    prologue_compass = bump237_to_257(b237["prologue_compass"]).replace(
        "Kohn–Sham meta prelude capstone reunion (row 237) |",
        "Kohn–Sham meta prelude capstone reunion (row 257) |",
        1,
    )
    prologue_preview = bump237_to_257(b237["prologue_preview"]).replace(
        "Row 237 preview", "Row 257 preview", 1
    )

    epilogue_loop = bump237_to_257(b237["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace(
        "### Row 237 closing loop (Row 68 → Row 237",
        "### Row 257 closing loop (Row 68 → Row 237",
        1,
    ).replace(
        "### Row 257 closing loop (Row 68 → Row 217",
        "### Row 257 closing loop (Row 68 → Row 237",
        1,
    )
    for spill in (
        "\n\n\n\n### Row 258 closing loop",
        "\n\n\n\n### Row 238 closing loop",
    ):
        if spill in epilogue_loop:
            epilogue_loop = epilogue_loop.split(spill, 1)[0].rstrip() + "\n\n"
            break
    epilogue_loop = epilogue_loop.rstrip() + "\n\n"

    sources_index = bump237_to_257(b237["sources_index"])
    sources_index = sources_index.replace(
        "## Row 68 → Row 217 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion index (row 237) "
        "{#row68-row217-kohn-sham-meta-prelude-capstone-reunion-index-row-237}",
        "## Row 68 → Row 257 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion index (row 257) "
        "{#row68-row237-kohn-sham-meta-prelude-capstone-reunion-index-row-257}",
        1,
    )

    sources_table = bump237_to_257(b237["sources_table"])
    sources_table = re.sub(
        r"^\| 237 \| Row 68 → Row 257",
        "| 257 | Row 68 → Row 257",
        sources_table,
        count=1,
        flags=re.MULTILINE,
    )
    if "| 257 | Row 68 → Row 257" not in sources_table:
        sources_table = sources_table.replace(
            "| 237 | Row 68 → Row 217", "| 257 | Row 68 → Row 257", 1
        )

    memory_table = bump237_to_257(b237["memory_table"])
    memory_table = memory_table.replace("| 237 | Meta |", "| 257 | Meta |", 1).replace(
        "| 257 | Meta |", "| 257 | Meta |", 1
    )

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


ROW256_STITCH_OLD = (
    "before row 257 Kohn–Sham meta prelude capstone reunion opens on the full capstone path."
)
ROW256_STITCH_NEW = (
    "before row 258 DFT workflows meta prelude capstone reunion opens on the full capstone path."
)

ROW256_LOOP_PROCEED_OLD = (
    "Proceed to [row 237](#row-237-closing-loop) when row 68 closed but Kohn–Sham meta prelude capstone still lags after row 236 on the full capstone path,"
)
ROW256_LOOP_PROCEED_NEW = (
    "Proceed to [row 257](#row-257-closing-loop) when row 68 closed but Kohn–Sham meta prelude capstone still lags after row 256 on the full capstone path,"
)

ROW256_BABY_OLD = (
    "when opening [row 197](preface.md#skill-navigation-row-197) before row 56 closes on the full capstone path"
)
ROW256_BABY_NEW = (
    "when opening [row 257](preface.md#skill-navigation-row-257) before row 57 closes on the full capstone path"
)

PROLOGUE_STITCH_ANCHOR = (
    "**Row 256 closing stitch (Row 68 → Row 256 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion).** {#row-256-closing-stitch}"
)

CAPSTONE_EPILOGUE_AFTER = (
    "### Row 252 closing loop (Row 68 → Row 232 Row 68 → Row 52 atomistic meta prelude capstone reunion) "
    "{#row-252-closing-loop}"
)

CAPSTONE_EPILOGUE_BEFORE = (
    "### Row 227 closing loop (Row 68 → Row 227 Row 68 → Row 67 part-boundary meta prelude capstone reunion) "
    "{#row-247-closing-loop}"
)


def _load_add256():
    spec = importlib.util.spec_from_file_location("add256", ROOT / "scripts/add-row-256.py")
    add256 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add256)
    return add256


def _canonical_capstone_loops(b: dict[str, str]) -> tuple[str, str, str, str, str]:
    add256 = _load_add256()
    bb = add256._build_blocks()
    l253, l254, l255, l256 = add256._canonical_capstone_loops(bb)
    l256 = l256.replace(ROW256_LOOP_PROCEED_OLD, ROW256_LOOP_PROCEED_NEW, 1)
    loop257 = b["epilogue_loop"]
    loop257 = loop257.replace(
        "When row 57 feels like quantum chemistry homework after row 236 alone on the full capstone path",
        "When row 57 feels like quantum chemistry homework after row 256 alone on the full capstone path",
        1,
    ).replace(
        "when row 236 closed Born–Oppenheimer meta prelude capstone",
        "when row 256 closed Born–Oppenheimer meta prelude capstone",
        1,
    ).replace(
        "Recite [preface row 236](../preface.md#skill-navigation-row-196)",
        "Recite [preface row 256](../preface.md#skill-navigation-row-256)",
        1,
    )
    for spill in ("\n\n\n\n### Row 258 closing loop", "\n\n\n\n### Row 238 closing loop"):
        if spill in loop257:
            loop257 = loop257.split(spill, 1)[0].rstrip() + "\n\n"
            break
    return l253, l254, l255, l256, loop257.rstrip() + "\n\n"


def _rebuild_capstone_mid(
    mid: str, l253: str, l254: str, l255: str, l256: str, l257: str
) -> str:
    marker = "### Row 253 closing loop"
    if marker not in mid:
        raise SystemExit("row 253 closing loop header missing in capstone mid")
    start = mid.index(marker)
    return mid[:start] + l253 + l254 + l255 + l256 + l257


def _epilogue_has_row257_in_capstone_chain(text: str) -> bool:
    if CAPSTONE_EPILOGUE_AFTER not in text:
        return False
    idx = text.index(CAPSTONE_EPILOGUE_AFTER)
    window = text[idx : idx + 55000]
    return (
        "{#row-257-closing-loop}" in window
        and "### Row 257 closing loop" in window
        and "after row 256 alone" in window
    )


def _strip_orphan_row257_loops(epilogue: str) -> str:
    """Remove duplicate row-257 loops pasted outside the capstone chain."""
    orphan_header = (
        "### Row 237 closing loop (Row 68 → Row 237 Row 68 → Row 57 "
        "Kohn–Sham meta prelude capstone reunion) {#row-257-closing-loop}"
    )
    while orphan_header in epilogue:
        idx = epilogue.index(orphan_header)
        if CAPSTONE_EPILOGUE_AFTER in epilogue[:idx]:
            cap_idx = epilogue.index(CAPSTONE_EPILOGUE_AFTER)
            cap_end = epilogue.index(CAPSTONE_EPILOGUE_BEFORE, cap_idx)
            if cap_idx < idx < cap_end:
                break
        next_h = epilogue.find("\n\n### Row ", idx + 10)
        if next_h == -1:
            epilogue = epilogue[:idx]
        else:
            epilogue = epilogue[:idx] + epilogue[next_h + 2 :]
    return epilogue


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    before_copper = preface.split(copper, 1)[0]
    if "### Row 257 skill checkpoint" in before_copper:
        print("preface: row 257 capstone already present")
    else:
        if "### Row 256 skill checkpoint" not in before_copper:
            raise SystemExit("row 256 must exist before row 257")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row257_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 257")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    prologue_changed = False
    if "Kohn–Sham meta prelude capstone reunion (row 257) |" not in prologue:
        needle = (
            "| Row 68 → Row 236 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion (row 256) |"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 256 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        prologue_changed = True
    if "**Row 257 closing stitch" not in prologue and PROLOGUE_STITCH_ANCHOR in prologue:
        prologue = prologue.replace(
            PROLOGUE_STITCH_ANCHOR,
            b["prologue_stitch"] + PROLOGUE_STITCH_ANCHOR,
            1,
        )
        prologue_changed = True
    if '<span id="prologue-preview-row-257">' not in prologue:
        preview_anchor = '| <span id="prologue-preview-row-256"></span>Row 256 preview'
        if preview_anchor not in prologue:
            preview_anchor = '| <span id="prologue-preview-row-236"></span>Row 236 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        prologue_changed = True
    if ROW256_STITCH_OLD in prologue:
        prologue = prologue.replace(ROW256_STITCH_OLD, ROW256_STITCH_NEW)
        prologue_changed = True
    if prologue_changed:
        prologue_path.write_text(prologue)
        print("prologue: added row 257")
    else:
        print("prologue: row 257 already present")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    epilogue = _strip_orphan_row257_loops(epilogue)
    force_rebuild = not _epilogue_has_row257_in_capstone_chain(epilogue)
    if force_rebuild:
        if CAPSTONE_EPILOGUE_AFTER not in epilogue:
            raise SystemExit("epilogue row 252 anchor not found")
        if CAPSTONE_EPILOGUE_BEFORE not in epilogue.split(CAPSTONE_EPILOGUE_AFTER, 1)[1]:
            raise SystemExit("epilogue row 247 marker not found after row 252")
        head, tail = epilogue.split(CAPSTONE_EPILOGUE_AFTER, 1)
        mid, rest = tail.split(CAPSTONE_EPILOGUE_BEFORE, 1)
        l253, l254, l255, l256, l257 = _canonical_capstone_loops(b)
        mid = _rebuild_capstone_mid(mid, l253, l254, l255, l256, l257)
        epilogue = head + CAPSTONE_EPILOGUE_AFTER + mid + CAPSTONE_EPILOGUE_BEFORE + rest
        epilogue_path.write_text(epilogue)
        print("epilogue: rebuilt capstone chain through row 257")
    else:
        epilogue_path.write_text(epilogue)
        print("epilogue: row 257 closing loop already present in capstone chain")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row237-kohn-sham-meta-prelude-capstone-reunion-index-row-257" not in sources:
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
        print("sources: added row 257")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-257-baby-picture-row68-row237" not in memory:
        memory = memory.replace(
            "| 217 | Meta | [Row 68 → Row 197 Kohn–Sham meta prelude capstone reunion index]",
            b["memory_table"] + "| 217 | Meta | [Row 68 → Row 197 Kohn–Sham meta prelude capstone reunion index]",
            1,
        )
        baby_anchor = (
            "### Row 237 baby picture {#row-217-baby-picture-row68-row217-kohn-sham-meta-prelude-capstone-reunion}"
        )
        if baby_anchor not in memory:
            baby_anchor = "### Row 237 baby picture"
        if baby_anchor in memory:
            memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
        if ROW256_BABY_OLD in memory:
            memory = memory.replace(ROW256_BABY_OLD, ROW256_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 257")


if __name__ == "__main__":
    main()
