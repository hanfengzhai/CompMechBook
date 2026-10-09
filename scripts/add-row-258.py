#!/usr/bin/env python3
"""Add row 258 meta-stitch (Row 68 → Row 238 ↔ Row 58 DFT workflows meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util
import re

ROOT = Path(__file__).resolve().parents[1]


def shift_meta_bump(text: str, delta: int = 20) -> str:
    """Shift capstone-path row references (100–250) by delta for meta-stitch copy."""
    out = text
    for tag in ("__R238__", "__R239__", "__R257__", "__R258__", "__R259__"):
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


def bump238_to_258(text: str) -> str:
    protected = (
        ("row-258-", "__P258__"),
        ("skill-navigation-row-258", "__S258__"),
        ("prologue-preview-row-258", "__PR258__"),
        ("{#row-258-closing-stitch}", "__ST258__"),
        ("{#row-258-closing-loop}", "__LP258__"),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = shift_meta_bump(out, 20)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add238():
    spec = importlib.util.spec_from_file_location("add238", ROOT / "scripts/add-row-238.py")
    add238 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add238)
    return add238


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 238 skill checkpoint")
    end = preface.index("\n\n### Row 239 skill checkpoint", start)
    row258_preface = bump238_to_258(preface[start:end]) + "\n\n"

    b238 = _load_add238()._build_blocks()
    prologue_stitch = bump238_to_258(
        b238["prologue_stitch"]
        .replace("{#row-238-closing-stitch}", "{#row-258-closing-stitch}")
        .replace(
            "**Row 238 closing stitch (Row 68 → Row 218",
            "**Row 258 closing stitch (Row 68 → Row 238",
        )
        .replace(
            "**Row 198 closing stitch (Row 68 → Row 178",
            "**Row 258 closing stitch (Row 68 → Row 238",
        )
    ).replace("**Row 277 closing stitch", "**Row 258 closing stitch", 1)
    prologue_compass = bump238_to_258(b238["prologue_compass"]).replace(
        "DFT workflows meta prelude capstone reunion (row 258) |",
        "DFT workflows meta prelude capstone reunion (row 258) |",
        1,
    )
    prologue_preview = bump238_to_258(b238["prologue_preview"]).replace(
        "Row 238 preview", "Row 258 preview", 1
    )

    epilogue_loop = bump238_to_258(b238["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace("{#row-238-closing-loop}", "{#row-258-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 238 closing loop (Row 68 → Row 218",
        "### Row 258 closing loop (Row 68 → Row 238",
        1,
    ).replace(
        "### Row 258 closing loop (Row 68 → Row 218",
        "### Row 258 closing loop (Row 68 → Row 238",
        1,
    )
    for spill in (
        "\n\n\n\n### Row 239 closing loop",
        "\n\n\n\n### Row 199 closing loop",
    ):
        if spill in epilogue_loop:
            epilogue_loop = epilogue_loop.split(spill, 1)[0].rstrip() + "\n\n"
            break
    epilogue_loop = epilogue_loop.rstrip() + "\n\n"

    sources_index = bump238_to_258(b238["sources_index"])
    sources_index = sources_index.replace(
        "## Row 68 → Row 218 Row 68 → Row 58 DFT workflows meta prelude capstone reunion index (row 238) "
        "{#row68-row198-dft-workflows-meta-prelude-capstone-reunion-index-row-238}",
        "## Row 68 → Row 238 Row 68 → Row 58 DFT workflows meta prelude capstone reunion index (row 258) "
        "{#row68-row238-dft-workflows-meta-prelude-capstone-reunion-index-row-258}",
        1,
    )

    sources_table = bump238_to_258(b238["sources_table"])
    sources_table = re.sub(
        r"^\| 238 \| Row 68 → Row 238",
        "| 258 | Row 68 → Row 238",
        sources_table,
        count=1,
        flags=re.MULTILINE,
    )
    if "| 258 | Row 68 → Row 238" not in sources_table:
        sources_table = sources_table.replace(
            "| 238 | Row 68 → Row 218", "| 258 | Row 68 → Row 238", 1
        )

    memory_table = bump238_to_258(b238["memory_table"])
    memory_table = memory_table.replace("| 238 | Meta |", "| 258 | Meta |", 1)

    memory_baby = bump238_to_258(b238["memory_baby"]).rstrip() + "\n\n"
    memory_baby = memory_baby.replace(
        "### Row 258 baby picture {#row-238-baby-picture",
        "### Row 258 baby picture {#row-258-baby-picture-row68-row238-dft-workflows-meta-prelude-capstone-reunion} {#row-237-baby-picture",
        1,
    )
    if "{#row-258-baby-picture-row68-row238" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 258 baby picture",
            "### Row 258 baby picture {#row-258-baby-picture-row68-row238-dft-workflows-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row258_preface": row258_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW257_TAIL_OLD = (
    "When row 257 is complete, proceed to [row 258](preface.md#skill-navigation-row-258) when `cutoff_convergence.yaml` exists on the full capstone path, to [row 238](preface.md#skill-navigation-row-238) when `cutoff_convergence.yaml` exists but IX.3 still feels disconnected from verified Kohn–Sham meta prelude capstone on the opening-hinge capstone path alone, to [row 198](preface.md#skill-navigation-row-198) for the Row 68 ↔ Row 58 DFT workflows meta audit on the opening-hinge prelude path alone, to [row 257](preface.md#skill-navigation-row-257) for the Row 68 ↔ Row 57 Kohn–Sham meta audit on the opening-hinge capstone path alone, to [row 236](preface.md#skill-navigation-row-236) when Born–Oppenheimer meta prelude capstone still lags after verified electronic audit meta prelude capstone on the full capstone path, to [row 58](preface.md#skill-navigation-row-58) when only IX.2 → IX.3 stalls, or extend prose only under `writings/` then sync."
)
ROW257_TAIL_NEW = ROW257_TAIL_OLD

ROW257_EPILOGUE_OLD = (
    "Proceed to [row 238](#row-238-closing-loop) when row 68 closed but DFT workflows meta prelude capstone still lags after row 257 on the full capstone path,"
)
ROW257_EPILOGUE_NEW = (
    "Proceed to [row 258](#row-258-closing-loop) when row 68 closed but DFT workflows meta prelude capstone still lags after row 257 on the full capstone path,"
)

ROW257_STITCH_OLD = (
    "before row 258 DFT workflows meta prelude capstone reunion opens on the full capstone path."
)
ROW257_STITCH_NEW = (
    "before row 259 Handshake 3 meta prelude capstone reunion opens on the full capstone path."
)

PROLOGUE_STITCH_ANCHOR = (
    "**Row 257 closing stitch (Row 68 → Row 257 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion).** {#row-257-closing-stitch}"
)

ROW257_INSERT_MARKER = (
    "### Row 217 closing loop (Row 68 → Row 217 Row 68 → Row 57 "
    "Kohn–Sham meta prelude capstone reunion) {#row-237-closing-loop}"
)


def _insert_row258_epilogue(epilogue: str, proper_loop: str) -> str:
    if "### Row 258 closing loop" in epilogue:
        return epilogue
    if ROW257_INSERT_MARKER not in epilogue:
        raise SystemExit("epilogue row 257 insert anchor not found")
    return epilogue.replace(ROW257_INSERT_MARKER, proper_loop + "\n\n" + ROW257_INSERT_MARKER, 1)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 258 skill checkpoint" in preface:
        print("preface: row 258 already present")
    else:
        if "### Row 257 skill checkpoint" not in preface:
            raise SystemExit("row 257 must exist before row 258")
        if "When row 257 is complete, proceed to [row 258]" in preface:
            print("preface: row 257 tail already has row 258 proceed")
        elif ROW257_TAIL_OLD in preface:
            preface = preface.replace(ROW257_TAIL_OLD, ROW257_TAIL_NEW, 1)
        elif ROW257_TAIL_NEW in preface:
            print("preface: row 257 tail already updated")
        else:
            raise SystemExit("row 257 tail proceed string not found")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row258_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 258")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "DFT workflows meta prelude capstone reunion (row 258) |" not in prologue:
        needle = "| Row 68 → Row 237 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion (row 257) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 257 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if PROLOGUE_STITCH_ANCHOR in prologue:
            prologue = prologue.replace(
                PROLOGUE_STITCH_ANCHOR,
                b["prologue_stitch"] + PROLOGUE_STITCH_ANCHOR,
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-257"></span>Row 257 preview'
        if preview_anchor not in prologue:
            preview_anchor = '| <span id="prologue-preview-row-236"></span>Row 235 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW257_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW257_STITCH_OLD, ROW257_STITCH_NEW, 1)
        prologue_path.write_text(prologue)
        print("prologue: added row 258")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if ROW257_EPILOGUE_OLD in epilogue:
        epilogue = epilogue.replace(ROW257_EPILOGUE_OLD, ROW257_EPILOGUE_NEW, 1)
    epilogue_new = _insert_row258_epilogue(epilogue, b["epilogue_loop"])
    if epilogue_new != epilogue:
        epilogue_path.write_text(epilogue_new)
        print("epilogue: added row 258")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row238-dft-workflows-meta-prelude-capstone-reunion-index-row-258" not in sources:
        sources = sources.replace(
            "| 238 | Row 68 → Row 218 Row 68 → Row 58 DFT workflows meta prelude capstone",
            b["sources_table"] + "| 238 | Row 68 → Row 218 Row 68 → Row 58 DFT workflows meta prelude capstone",
            1,
        )
        src237_header = (
            "## Row 68 → Row 218 Row 68 → Row 58 DFT workflows meta prelude capstone reunion index (row 238) "
            "{#row68-row198-dft-workflows-meta-prelude-capstone-reunion-index-row-238}"
        )
        if src237_header not in sources:
            src237_header = (
                "## Row 68 → Row 218 Row 68 → Row 58 DFT workflows meta prelude capstone reunion index (row 238)"
            )
        sources = sources.replace(
            src237_header,
            b["sources_index"] + src237_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 258")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-258-baby-picture-row68-row238" not in memory:
        memory = memory.replace(
            "| 238 | Meta | [Row 68 → Row 218 DFT workflows meta prelude capstone reunion index]",
            b["memory_table"] + "| 238 | Meta | [Row 68 → Row 218 DFT workflows meta prelude capstone reunion index]",
            1,
        )
        baby_anchor = (
            "### Row 238 baby picture {#row-238-baby-picture-row68-row198-dft-workflows-meta-prelude-capstone-reunion}"
        )
        if baby_anchor not in memory:
            baby_anchor = "### Row 238 baby picture"
        if baby_anchor in memory:
            memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
        memory_path.write_text(memory)
        print("memory-sheet: added row 258")


if __name__ == "__main__":
    main()
