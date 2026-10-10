#!/usr/bin/env python3
"""Add row 245 meta-stitch (Row 68 → Row 225 ↔ Row 65 second-pass meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util
import re

ROOT = Path(__file__).resolve().parents[1]


def shift_meta_bump(text: str, delta: int = 20) -> str:
    """Shift capstone-path row references (100–250) by delta for meta-stitch copy."""

    def in_band(n: int) -> bool:
        return 100 <= n <= 250

    def repl_row(m: re.Match[str]) -> str:
        n = int(m.group(1))
        return f"row {n + delta}" if in_band(n) else m.group(0)

    def repl_Row(m: re.Match[str]) -> str:
        n = int(m.group(1))
        return f"Row {n + delta}" if in_band(n) else m.group(0)

    out = text
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


def bump225_to_245(text: str) -> str:
    protected = (
        ("row-245-", "__P245__"),
        ("skill-navigation-row-245", "__S245__"),
        ("prologue-preview-row-245", "__prologue-preview-row-245__"),
        ("{#row-245-closing-stitch}", "__{#row-245-closing-stitch}__"),
        ("{#row-245-closing-loop}", "__{#row-245-closing-loop}__"),
        (
            "row68-row225-second-pass-meta-prelude-capstone-reunion-index-row-245",
            "__row68-row225-second-pass-meta-prelude-capstone-reunion-index-row-245__",
        ),
        (
            "row-245-baby-picture-row68-row225-second-pass-meta-prelude-capstone-reunion",
            "__row-245-baby-picture-row68-row225-second-pass-meta-prelude-capstone-reunion__",
        ),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = shift_meta_bump(out, 20)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add225():
    spec = importlib.util.spec_from_file_location("add225", ROOT / "scripts/add-row-225.py")
    add225 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add225)
    return add225


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 225 skill checkpoint")
    end = preface.index("\n\n### Row 226 skill checkpoint", start)
    row245_preface = bump225_to_245(preface[start:end]).strip() + "\n\n"

    b225 = _load_add225()._build_blocks()
    out = {
        "row245_preface": row245_preface,
        "prologue_compass": bump225_to_245(b225["prologue_compass"]),
        "prologue_stitch": bump225_to_245(b225["prologue_stitch"]),
        "prologue_preview": bump225_to_245(b225["prologue_preview"]),
        "epilogue_loop": bump225_to_245(b225["epilogue_loop"]),
        "sources_table": bump225_to_245(b225["sources_table"]).replace(
            "| 225 | Row 68 → Row 225", "| 245 | Row 68 → Row 225", 1
        ),
        "memory_table": (
            "| 245 | Meta | [Row 68 → Row 225 second-pass meta prelude capstone reunion index]"
            "(sources.md#row68-row225-second-pass-meta-prelude-capstone-reunion-index-row-245) · "
            "[preface row 245 skill checkpoint](../preface.md#skill-navigation-row-245) · "
            "[prologue row 245 preview](../prologue/00-many-scales.md#prologue-preview-row-245) · "
            "[prologue row 245 closing stitch](../prologue/00-many-scales.md#row-245-closing-stitch) · "
            "[epilogue row 245 closing loop](../epilogue/multiscale.md#row-245-closing-loop) | "
            "Row 68 closed but row 65 second-pass meta reunion feels disconnected from verified "
            "book-loop meta prelude capstone on the full capstone path — read row 68 + row 244 or "
            "row 225 gate + epilogue second-pass cross-links + row 65; "
            "[row 245 baby picture](#row-245-baby-picture-row68-row225-second-pass-meta-prelude-capstone-reunion) |\n"
        ),
        "sources_index": bump225_to_245(b225["sources_index"]).replace(
            "## Row 68 → Row 205 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 225) "
            "{#row68-row205-second-pass-meta-prelude-capstone-reunion-index-row-225}",
            "## Row 68 → Row 225 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 245) "
            "{#row68-row225-second-pass-meta-prelude-capstone-reunion-index-row-245}",
            1,
        ),
        "memory_baby": (
            "### Row 245 baby picture {#row-245-baby-picture-row68-row225-second-pass-meta-prelude-capstone-reunion}\n\n"
            "**Row 245 baby picture:** when row 68 closed the midpoint prelude and row 244 or row 225 "
            "closed book-loop meta prelude capstone / second-pass meta prelude on the full capstone path "
            "but **row 65's epilogue second-pass cross-links audit or the continuous read-through guide "
            "still feel like separate checklists on the full capstone path**, open the "
            "[Row 68 → Row 225 second-pass meta prelude capstone reunion index]"
            "(sources.md#row68-row225-second-pass-meta-prelude-capstone-reunion-index-row-245) — read "
            "[preface row 68](../preface.md#skill-navigation-row-68) gate → "
            "[preface row 244](../preface.md#skill-navigation-row-244) or "
            "[preface row 225](../preface.md#skill-navigation-row-225) book-loop meta prelude capstone / "
            "second-pass meta prelude gate → [epilogue second-pass cross-links audit]"
            "(../epilogue/multiscale.md#opening-hinge-rows17-44-row17) aloud → "
            "[preface row 65](../preface.md#skill-navigation-row-65) five-step audit → recite "
            "[continuous read-through guide](sources.md#continuous-read-through-guide) before row 66 "
            "Writings canonical reunion opens on the full capstone path.\n\n"
            "```mermaid\nflowchart LR\n  MP[Midpoint row 68]\n  BL[Book-loop meta prelude capstone row 244]\n"
            "  XL[Second-pass cross-links]\n  R65[row 65 meta gate]\n  MP --> BL --> XL --> R65\n```\n\n"
            "When row 245 feels disconnected from row 244, read them as **book-loop meta prelude capstone "
            "vs second-pass meta prelude capstones on the full capstone path**: row 244 when "
            "**epilogue book-loop cross-links must reunite on verified orchestration meta prelude capstone "
            "before any second-pass table on the full capstone path**; row 245 when "
            "**epilogue second-pass cross-links and Row 64 → Row 65 meta must read on the same wire before "
            "row 246 Writings canonical meta prelude capstone reunion opens on the full capstone path** — "
            "same copper wire, same Functional Analysis Notes layout, one continuous next-project → "
            "novel-rhythm afternoon after verified book-loop meta prelude capstone. When row 244 closed but "
            "novel second pass still lags on the full capstone path, switch to [row 245]"
            "(#row-245-baby-picture-row68-row225-second-pass-meta-prelude-capstone-reunion).\n\n\n"
        ),
    }
    loop = out["epilogue_loop"]
    loop = loop.replace(
        "### Row 245 closing loop (Row 68 → Row 225",
        "### Row 225 closing loop (Row 68 → Row 225",
        1,
    )
    for spill in ("\n\n\n\n### Row 244 closing loop", "\n\n\n\n### Row 245 closing loop"):
        if spill in loop:
            loop = loop.split(spill, 1)[0].rstrip() + "\n\n"
            break
    out["epilogue_loop"] = loop.rstrip() + "\n\n"
    if "{#row-245-baby-picture-row68-row225" not in out["memory_baby"]:
        out["memory_baby"] = out["memory_baby"].replace(
            "### Row 245 baby picture",
            "### Row 245 baby picture {#row-245-baby-picture-row68-row225-second-pass-meta-prelude-capstone-reunion}",
            1,
        )
    return out


PROLOGUE_STITCH_ANCHOR = (
    "**Row 244 closing stitch (Row 68 → Row 224 Row 68 → Row 64 book-loop meta prelude capstone reunion).** {#row-244-closing-stitch}"
)

ROW245_INSERT_MARKER = (
    "### Row 224 closing loop (Row 68 → Row 224 Row 68 → Row 64 book-loop meta prelude capstone reunion) {#row-244-closing-loop}"
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 245 skill checkpoint" in preface:
        print("preface: row 245 already present")
    else:
        if "### Row 244 skill checkpoint" not in preface:
            raise SystemExit("row 244 must exist before row 245")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row245_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 245")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "second-pass meta prelude capstone reunion (row 245) |" not in prologue:
        needle = (
            "| Row 68 → Row 224 Row 68 → Row 64 book-loop meta prelude capstone reunion (row 224) |"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 244 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if PROLOGUE_STITCH_ANCHOR in prologue:
            prologue = prologue.replace(
                PROLOGUE_STITCH_ANCHOR,
                b["prologue_stitch"] + PROLOGUE_STITCH_ANCHOR,
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-244"></span>Row 224 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        prologue_path.write_text(prologue)
        print("prologue: added row 245")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "{#row-245-closing-loop}" not in epilogue:
        marker = ROW245_INSERT_MARKER
        if marker not in epilogue:
            raise SystemExit("epilogue row 244 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 245")
    else:
        print("epilogue: row 245 closing loop already present")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row225-second-pass-meta-prelude-capstone-reunion-index-row-245" not in sources:
        sources = sources.replace(
            "| 225 | Row 68 → Row 205 Row 68 → Row 65 second-pass meta prelude capstone",
            b["sources_table"] + "| 225 | Row 68 → Row 205 Row 68 → Row 65 second-pass meta prelude capstone",
            1,
        )
        src_header = (
            "## Row 68 → Row 205 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 225) "
            "{#row68-row205-second-pass-meta-prelude-capstone-reunion-index-row-225}"
        )
        if src_header in sources and b["sources_index"].strip() not in sources:
            sources = sources.replace(src_header, b["sources_index"] + src_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 245")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-245-baby-picture-row68-row225" not in memory:
        memory = memory.replace(
            "| 244 | Meta | [Row 68 → Row 204 book-loop meta prelude capstone reunion index](sources.md#row68-row224-book-loop-meta-prelude-capstone-reunion-index-row-244)",
            b["memory_table"]
            + "| 244 | Meta | [Row 68 → Row 204 book-loop meta prelude capstone reunion index](sources.md#row68-row224-book-loop-meta-prelude-capstone-reunion-index-row-244)",
            1,
        )
        inserted = False
        for baby_anchor in (
            "### Row 225 baby picture {#row-225-baby-picture-row68-row205-second-pass-meta-prelude-capstone-reunion}",
            "### Row 204 baby picture {#row-244-baby-picture-row68-row224-book-loop-meta-prelude-capstone-reunion}",
            "### Row 224 baby picture {#row-224-baby-picture-row68-row204-book-loop-meta-prelude-capstone-reunion}",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 245")


if __name__ == "__main__":
    main()
