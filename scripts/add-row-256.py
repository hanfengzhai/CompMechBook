#!/usr/bin/env python3
"""Add row 256 meta-stitch (Row 68 → Row 256 ↔ Row 56 Born–Oppenheimer meta prelude capstone reunion, full capstone path)."""
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


def bump236_to_256(text: str) -> str:
    protected = (
        ("row-256-", "__P236__"),
        ("skill-navigation-row-256", "__S236__"),
        ("prologue-preview-row-256", "__PR236__"),
        ("{#row-256-closing-stitch}", "__ST236__"),
        ("{#row-256-closing-loop}", "__LP236__"),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = shift_meta_bump(out, 20)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add236():
    spec = importlib.util.spec_from_file_location("add236", ROOT / "scripts/add-row-236.py")
    add236 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add236)
    return add236


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 236 skill checkpoint")
    end = preface.index("\n\n### Row 237 skill checkpoint", start)
    row256_preface = bump236_to_256(preface[start:end]) + "\n\n"

    b216 = _load_add236()._build_blocks()
    prologue_stitch = bump236_to_256(
        b216["prologue_stitch"]
        .replace("{#row-216-closing-stitch}", "{#row-256-closing-stitch}")
        .replace(
            "**Row 236 closing stitch (Row 68 → Row 196",
            "**Row 256 closing stitch (Row 68 → Row 256",
        )
        .replace(
            "**Row 196 closing stitch (Row 68 → Row 196",
            "**Row 256 closing stitch (Row 68 → Row 256",
        )
    ).replace("**Row 256 closing stitch", "**Row 256 closing stitch", 1)
    prologue_compass = bump236_to_256(b216["prologue_compass"]).replace(
        "Born–Oppenheimer meta prelude capstone reunion (row 236) |",
        "Born–Oppenheimer meta prelude capstone reunion (row 256) |",
        1,
    )
    prologue_preview = bump236_to_256(b216["prologue_preview"]).replace(
        "Row 236 preview", "Row 256 preview", 1
    )

    epilogue_loop = bump236_to_256(b216["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace(
        "### Row 236 closing loop (Row 68 → Row 236",
        "### Row 256 closing loop (Row 68 → Row 236",
        1,
    ).replace(
        "### Row 256 closing loop (Row 68 → Row 196",
        "### Row 256 closing loop (Row 68 → Row 236",
        1,
    )
    for spill in (
        "\n\n\n\n### Row 257 closing loop",
        "\n\n\n\n### Row 197 closing loop",
    ):
        if spill in epilogue_loop:
            epilogue_loop = epilogue_loop.split(spill, 1)[0].rstrip() + "\n\n"
            break
    epilogue_loop = epilogue_loop.rstrip() + "\n\n"

    sources_index = bump236_to_256(b216["sources_index"])
    sources_index = sources_index.replace(
        "## Row 68 → Row 196 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion index (row 236) "
        "{#row68-row196-born-oppenheimer-meta-prelude-capstone-reunion-index-row-216}",
        "## Row 68 → Row 256 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion index (row 256) "
        "{#row68-row236-born-oppenheimer-meta-prelude-capstone-reunion-index-row-256}",
        1,
    )

    sources_table = bump236_to_256(b216["sources_table"])
    sources_table = re.sub(
        r"^\| 216 \| Row 68 → Row 256",
        "| 236 | Row 68 → Row 256",
        sources_table,
        count=1,
        flags=re.MULTILINE,
    )
    if "| 236 | Row 68 → Row 256" not in sources_table:
        sources_table = sources_table.replace(
            "| 216 | Row 68 → Row 196", "| 236 | Row 68 → Row 256", 1
        )

    memory_table = bump236_to_256(b216["memory_table"])
    memory_table = memory_table.replace("| 216 | Meta |", "| 256 | Meta |", 1).replace(
        "| 236 | Meta |", "| 256 | Meta |", 1
    )

    memory_baby = bump236_to_256(b216["memory_baby"]).rstrip() + "\n\n"
    memory_baby = memory_baby.replace(
        "### Row 256 baby picture {#row-216-baby-picture",
        "### Row 256 baby picture {#row-256-baby-picture-row68-row236-born-oppenheimer-meta-prelude-capstone-reunion} {#row-216-baby-picture",
        1,
    )
    if "{#row-256-baby-picture-row68-row236" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 256 baby picture",
            "### Row 256 baby picture {#row-256-baby-picture-row68-row236-born-oppenheimer-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row256_preface": row256_preface,
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
    "before row 256 Born–Oppenheimer meta prelude capstone reunion opens on the full capstone path."
)
ROW234_STITCH_FIX_NEW = (
    "before row 255 electronic audit meta prelude capstone reunion opens on the full capstone path."
)

ROW235_EPILOGUE_OLD = (
    "Proceed to [row 236](#row-256-closing-loop) when row 68 closed but Born–Oppenheimer meta prelude capstone still lags after row 215 on the full capstone path,"
)
ROW235_EPILOGUE_NEW = (
    "Proceed to [row 256](#row-256-closing-loop) when row 68 closed but Born–Oppenheimer meta prelude capstone still lags after row 255 on the full capstone path,"
)

ROW235_BABY_OLD = (
    "when opening [row 176](preface.md#skill-navigation-row-176) before row 56 closes on the full capstone path"
)
ROW235_BABY_NEW = (
    "when opening [row 256](preface.md#skill-navigation-row-256) before row 56 closes on the full capstone path"
)

ROW235_STITCH_OLD = (
    "before row 256 Born–Oppenheimer meta prelude capstone reunion opens on the full capstone path."
)
ROW235_STITCH_NEW = (
    "before row 257 Kohn–Sham meta prelude capstone reunion opens on the full capstone path."
)

ROW235_TAIL_OLD = (
    "When row 255 is complete, proceed to [row 256](preface.md#skill-navigation-row-256) when `cu.relax.out` exists on the full capstone path, to [row 236](preface.md#skill-navigation-row-216) when `cu.relax.out` exists but IX.1 still feels disconnected from verified electronic audit meta prelude capstone on the opening-hinge capstone path alone, to [row 196](preface.md#skill-navigation-row-196) for the Row 68 ↔ Row 56 Born–Oppenheimer meta audit on the opening-hinge prelude path alone, to [row 255](preface.md#skill-navigation-row-235) for the Row 68 ↔ Row 55 electronic audit meta audit on the opening-hinge capstone path alone, to [row 234](preface.md#skill-navigation-row-234) when yaml exports still stall after verified export meta prelude capstone on the full capstone path, to [row 56](preface.md#skill-navigation-row-56) when only IX.0 → IX.1 stalls, or extend prose only under `writings/` then sync."
)
ROW235_TAIL_NEW = (
    "When row 255 is complete, proceed to [row 256](preface.md#skill-navigation-row-256) when `cu.relax.out` exists on the full capstone path, to [row 236](preface.md#skill-navigation-row-216) when `cu.relax.out` exists but IX.1 still feels disconnected from verified electronic audit meta prelude capstone on the opening-hinge capstone path alone, to [row 236](preface.md#skill-navigation-row-216) for the Row 68 ↔ Row 56 Born–Oppenheimer meta audit on the opening-hinge prelude path alone, to [row 255](preface.md#skill-navigation-row-235) for the Row 68 ↔ Row 55 electronic audit meta audit on the opening-hinge capstone path alone, to [row 234](preface.md#skill-navigation-row-234) when yaml exports still stall after verified export meta prelude capstone on the full capstone path, to [row 56](preface.md#skill-navigation-row-56) when only IX.0 → IX.1 stalls, or extend prose only under `writings/` then sync."
)

PROLOGUE_STITCH_ANCHOR = (
    "**Row 255 closing stitch (Row 68 → Row 255 Row 68 → Row 55 electronic audit meta prelude capstone reunion).** {#row-255-closing-stitch}"
)

ROW256_EPILOGUE_AFTER = (
    "### Row 252 closing loop (Row 68 → Row 232 Row 68 → Row 52 atomistic meta prelude capstone reunion) "
    "{#row-252-closing-loop}"
)

ROW256_EPILOGUE_BEFORE = (
    "### Row 227 closing loop (Row 68 → Row 227 Row 68 → Row 67 part-boundary meta prelude capstone reunion) "
    "{#row-247-closing-loop}"
)

ROW255_LOOP_PROCEED_OLD = (
    "Proceed to [row 236](#row-236-closing-loop) when row 68 closed but Born–Oppenheimer meta prelude capstone still lags after row 235 on the full capstone path,"
)
ROW255_LOOP_PROCEED_NEW = (
    "Proceed to [row 256](#row-256-closing-loop) when row 68 closed but Born–Oppenheimer meta prelude capstone still lags after row 255 on the full capstone path,"
)


def _load_add255():
    spec = importlib.util.spec_from_file_location("add255", ROOT / "scripts/add-row-255.py")
    add255 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add255)
    return add255


def _canonical_capstone_loops(b: dict[str, str]) -> tuple[str, str, str, str]:
    add255 = _load_add255()
    bb = add255._build_blocks()
    l253, l254, l255 = add255._canonical_capstone_loops(bb)
    l255 = l255.replace(ROW255_LOOP_PROCEED_OLD, ROW255_LOOP_PROCEED_NEW, 1)
    loop256 = b["epilogue_loop"]
    loop256 = loop256.replace(
        "When row 56 feels like quantum chemistry homework after row 235 alone on the full capstone path",
        "When row 56 feels like quantum chemistry homework after row 255 alone on the full capstone path",
        1,
    ).replace(
        "when row 235 closed electronic audit meta prelude capstone",
        "when row 255 closed electronic audit meta prelude capstone",
        1,
    ).replace(
        "Recite [preface row 235](../preface.md#skill-navigation-row-215)",
        "Recite [preface row 255](../preface.md#skill-navigation-row-255)",
        1,
    )
    for spill in ("\n\n\n\n### Row 257 closing loop", "\n\n\n\n### Row 237 closing loop"):
        if spill in loop256:
            loop256 = loop256.split(spill, 1)[0].rstrip() + "\n\n"
            break
    return l253, l254, l255, loop256.rstrip() + "\n\n"


def _rebuild_capstone_mid(mid: str, l253: str, l254: str, l255: str, l256: str) -> str:
    marker = "### Row 253 closing loop"
    if marker not in mid:
        raise SystemExit("row 253 closing loop header missing in capstone mid")
    start = mid.index(marker)
    return mid[:start] + l253 + l254 + l255 + l256


def _epilogue_has_row256_in_capstone_chain(text: str) -> bool:
    if ROW256_EPILOGUE_AFTER not in text:
        return False
    idx = text.index(ROW256_EPILOGUE_AFTER)
    window = text[idx : idx + 45000]
    return (
        "{#row-256-closing-loop}" in window
        and "### Row 256 closing loop" in window
        and "after row 255 alone" in window
    )


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 256 skill checkpoint" in preface:
        print("preface: row 256 already present")
    else:
        if "### Row 255 skill checkpoint" not in preface:
            raise SystemExit("row 255 must exist before row 256")
        if "When row 255 is complete, proceed to [row 256]" in preface:
            print("preface: row 255 tail already has row 256 proceed")
        elif ROW235_TAIL_OLD in preface:
            preface = preface.replace(ROW235_TAIL_OLD, ROW235_TAIL_NEW, 1)
        elif ROW235_TAIL_NEW in preface:
            print("preface: row 255 tail already updated")
        else:
            raise SystemExit("row 255 tail proceed string not found")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row256_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 256")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    prologue_changed = False
    if "Born–Oppenheimer meta prelude capstone reunion (row 256) |" not in prologue:
        needle = "| Row 68 → Row 235 Row 68 → Row 55 electronic audit meta prelude capstone reunion (row 255) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 255 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        prologue_changed = True
    if "**Row 256 closing stitch" not in prologue and PROLOGUE_STITCH_ANCHOR in prologue:
        prologue = prologue.replace(
            PROLOGUE_STITCH_ANCHOR,
            b["prologue_stitch"] + PROLOGUE_STITCH_ANCHOR,
            1,
        )
        prologue_changed = True
    if '<span id="prologue-preview-row-256">' not in prologue:
        preview_anchor = '| <span id="prologue-preview-row-255"></span>Row 255 preview'
        if preview_anchor not in prologue:
            preview_anchor = '| <span id="prologue-preview-row-235"></span>Row 235 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        prologue_changed = True
    if ROW235_STITCH_OLD in prologue:
        prologue = prologue.replace(ROW235_STITCH_OLD, ROW235_STITCH_NEW)
        prologue_changed = True
    if ROW234_STITCH_FIX_OLD in prologue:
        prologue = prologue.replace(ROW234_STITCH_FIX_OLD, ROW234_STITCH_FIX_NEW)
        prologue_changed = True
    if prologue_changed:
        prologue_path.write_text(prologue)
        print("prologue: added row 256")
    else:
        print("prologue: row 256 already present")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    for old, new in (
        (ROW235_EPILOGUE_OLD, ROW235_EPILOGUE_NEW),
        (ROW255_LOOP_PROCEED_OLD, ROW255_LOOP_PROCEED_NEW),
    ):
        if old in epilogue:
            epilogue = epilogue.replace(old, new, 1)
    force_rebuild = not _epilogue_has_row256_in_capstone_chain(epilogue)
    if force_rebuild:
        if ROW256_EPILOGUE_AFTER not in epilogue:
            raise SystemExit("epilogue row 252 anchor not found")
        if ROW256_EPILOGUE_BEFORE not in epilogue.split(ROW256_EPILOGUE_AFTER, 1)[1]:
            raise SystemExit("epilogue row 247 marker not found after row 252")
        head, tail = epilogue.split(ROW256_EPILOGUE_AFTER, 1)
        mid, rest = tail.split(ROW256_EPILOGUE_BEFORE, 1)
        l253, l254, l255, l256 = _canonical_capstone_loops(b)
        mid = _rebuild_capstone_mid(mid, l253, l254, l255, l256)
        epilogue = head + ROW256_EPILOGUE_AFTER + mid + ROW256_EPILOGUE_BEFORE + rest
        epilogue_path.write_text(epilogue)
        print("epilogue: rebuilt capstone chain through row 256")
    else:
        epilogue_path.write_text(epilogue)
        print("epilogue: row 256 closing loop already present in capstone chain")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row236-born-oppenheimer-meta-prelude-capstone-reunion-index-row-256" not in sources:
        sources = sources.replace(
            "| 216 | Row 68 → Row 196 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone",
            b["sources_table"] + "| 216 | Row 68 → Row 196 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone",
            1,
        )
        src216_header = (
            "## Row 68 → Row 196 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion index (row 236) "
            "{#row68-row196-born-oppenheimer-meta-prelude-capstone-reunion-index-row-216}"
        )
        if src216_header not in sources:
            src216_header = (
                "## Row 68 → Row 196 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion index (row 236)"
            )
        sources = sources.replace(
            src216_header,
            b["sources_index"] + src216_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 256")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-256-baby-picture-row68-row236" not in memory:
        memory = memory.replace(
            "| 216 | Meta | [Row 68 → Row 196 Born–Oppenheimer meta prelude capstone reunion index]",
            b["memory_table"] + "| 216 | Meta | [Row 68 → Row 196 Born–Oppenheimer meta prelude capstone reunion index]",
            1,
        )
        baby_anchor = (
            "### Row 236 baby picture {#row-216-baby-picture-row68-row196-born-oppenheimer-meta-prelude-capstone-reunion}"
        )
        if baby_anchor not in memory:
            baby_anchor = "### Row 236 baby picture"
        if baby_anchor in memory:
            memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
        if ROW235_BABY_OLD in memory:
            memory = memory.replace(ROW235_BABY_OLD, ROW235_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 256")


if __name__ == "__main__":
    main()
