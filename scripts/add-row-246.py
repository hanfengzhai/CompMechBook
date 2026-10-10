#!/usr/bin/env python3
"""Add row 246 meta-stitch (Row 68 → Row 226 ↔ Row 66 Writings canonical meta prelude capstone reunion, full capstone path)."""
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


def bump226_to_246(text: str) -> str:
    protected = (
        ("row-246-", "__P246__"),
        ("skill-navigation-row-246", "__S246__"),
        ("prologue-preview-row-246", "__prologue-preview-row-246__"),
        ("{#row-246-closing-stitch}", "__{#row-246-closing-stitch}__"),
        ("{#row-246-closing-loop}", "__{#row-246-closing-loop}__"),
        (
            "row68-row226-writings-meta-prelude-capstone-reunion-index-row-246",
            "__row68-row226-writings-meta-prelude-capstone-reunion-index-row-246__",
        ),
        (
            "row-246-baby-picture-row68-row226-writings-meta-prelude-capstone-reunion",
            "__row-246-baby-picture-row68-row226-writings-meta-prelude-capstone-reunion__",
        ),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = shift_meta_bump(out, 20)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add226():
    spec = importlib.util.spec_from_file_location("add226", ROOT / "scripts/add-row-226.py")
    add226 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add226)
    return add226


def _row246_sources_index() -> str:
    """Single row-246 reunion index block (avoid duplicating legacy row-226 index trees)."""
    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    header = (
        "## Row 68 → Row 226 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 246) "
        "{#row68-row226-writings-meta-prelude-capstone-reunion-index-row-246}"
    )
    if header in sources:
        start = sources.index(header)
        end = sources.find(
            "\n\n## Row 68 → Row 225 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 245)",
            start,
        )
        if end != -1:
            return sources[start:end].strip() + "\n\n"
    preface = bump226_to_246(
        (ROOT / "writings/preface/chapters/preface.md")
        .read_text()
        .split("### Row 226 skill checkpoint", 1)[1]
        .split("### Row 227 skill checkpoint", 1)[0]
    )
    return (
        header
        + "\n\n"
        + "Row 246 closes the **Writings canonical meta prelude capstone** on the full capstone path — "
        + "see [preface row 246](../preface.md#skill-navigation-row-246) and the five-step audit in:\n\n"
        + preface[:800]
        + "…\n\n"
    )


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 226 skill checkpoint")
    end = preface.index("\n\n### Row 227 skill checkpoint", start)
    row246_preface = bump226_to_246(preface[start:end]).strip() + "\n\n"

    b226 = _load_add226()._build_blocks()
    out = {
        "row246_preface": row246_preface,
        "prologue_compass": bump226_to_246(b226["prologue_compass"]),
        "prologue_stitch": bump226_to_246(b226["prologue_stitch"]),
        "prologue_preview": bump226_to_246(b226["prologue_preview"]),
        "epilogue_loop": bump226_to_246(b226["epilogue_loop"]),
        "sources_table": bump226_to_246(b226["sources_table"]).replace(
            "| 226 | Row 68 → Row 226", "| 246 | Row 68 → Row 226", 1
        ),
        "memory_table": (
            "| 246 | Meta | [Row 68 → Row 226 Writings canonical meta prelude capstone reunion index]"
            "(sources.md#row68-row226-writings-meta-prelude-capstone-reunion-index-row-246) · "
            "[preface row 246 skill checkpoint](../preface.md#skill-navigation-row-246) · "
            "[prologue row 246 preview](../prologue/00-many-scales.md#prologue-preview-row-246) · "
            "[prologue row 246 closing stitch](../prologue/00-many-scales.md#row-246-closing-stitch) · "
            "[epilogue row 246 closing loop](../epilogue/multiscale.md#row-246-closing-loop) | "
            "Row 68 closed but row 66 Writings canonical meta reunion feels disconnected from verified "
            "second-pass meta prelude capstone on the full capstone path — read row 68 + row 245 or "
            "row 226 gate + epilogue writings cross-links + row 66; run `./scripts/sync-writings.sh --check`; "
            "[row 246 baby picture](#row-246-baby-picture-row68-row226-writings-meta-prelude-capstone-reunion) |\n"
        ),
        "sources_index": _row246_sources_index(),
        "memory_baby": (
            "### Row 246 baby picture {#row-246-baby-picture-row68-row226-writings-meta-prelude-capstone-reunion}\n\n"
            "**Row 246 baby picture:** when row 68 closed the midpoint prelude and row 245 or row 226 "
            "closed second-pass meta prelude capstone / Writings canonical meta prelude on the full capstone path "
            "but **row 66's epilogue writings cross-links audit or `./scripts/sync-writings.sh --check` still "
            "feel like separate checklists on the full capstone path**, open the "
            "[Row 68 → Row 226 Writings canonical meta prelude capstone reunion index]"
            "(sources.md#row68-row226-writings-meta-prelude-capstone-reunion-index-row-246) — read "
            "[preface row 68](../preface.md#skill-navigation-row-68) gate → "
            "[preface row 245](../preface.md#skill-navigation-row-245) or "
            "[preface row 226](../preface.md#skill-navigation-row-226) second-pass meta prelude capstone / "
            "Writings canonical meta prelude gate → [epilogue Writings canonical cross-links audit]"
            "(../epilogue/multiscale.md#opening-hinge-rows17-45-writings) aloud → "
            "[preface row 66](../preface.md#skill-navigation-row-66) five-step audit → run "
            "`./scripts/sync-writings.sh --check` before row 67 part-boundary prelude opens on the full capstone path.\n\n"
            "```mermaid\nflowchart LR\n  MP[Midpoint row 68]\n  SP[Second-pass meta prelude capstone row 245]\n"
            "  XL[Writings cross-links]\n  R66[row 66 meta gate]\n  MP --> SP --> XL --> R66\n```\n\n"
            "When row 246 feels disconnected from row 245, read them as **second-pass meta prelude capstone "
            "vs Writings canonical meta prelude capstones on the full capstone path**: row 245 when "
            "**epilogue second-pass cross-links must reunite on verified book-loop meta prelude capstone "
            "before any writings table on the full capstone path**; row 246 when "
            "**epilogue writings cross-links and Row 65 → Row 46 meta must read on the same wire before "
            "row 247 part-boundary meta prelude capstone reunion opens on the full capstone path** — "
            "same copper wire, same Functional Analysis Notes layout, one continuous novel-rhythm → "
            "canonical-tree afternoon after verified second-pass meta prelude capstone. When row 245 closed but "
            "sync discipline still lags on the full capstone path, switch to [row 246]"
            "(#row-246-baby-picture-row68-row226-writings-meta-prelude-capstone-reunion).\n\n\n"
        ),
    }
    loop = out["epilogue_loop"]
    loop = loop.replace(
        "### Row 246 closing loop (Row 68 → Row 226",
        "### Row 226 closing loop (Row 68 → Row 226",
        1,
    )
    for spill in ("\n\n\n\n### Row 245 closing loop", "\n\n\n\n### Row 246 closing loop"):
        if spill in loop:
            loop = loop.split(spill, 1)[0].rstrip() + "\n\n"
            break
    out["epilogue_loop"] = loop.rstrip() + "\n\n"
    return out


PROLOGUE_STITCH_ANCHOR = (
    "**Row 245 closing stitch (Row 68 → Row 225 Row 68 → Row 65 second-pass meta prelude capstone reunion).** {#row-245-closing-stitch}"
)

ROW246_INSERT_MARKER = (
    "### Row 225 closing loop (Row 68 → Row 225 Row 68 → Row 65 second-pass meta prelude capstone reunion) {#row-245-closing-loop}"
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 246 skill checkpoint" in preface:
        print("preface: row 246 already present")
    else:
        if "### Row 245 skill checkpoint" not in preface:
            raise SystemExit("row 245 must exist before row 246")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row246_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 246")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "Writings canonical meta prelude capstone reunion (row 246) |" not in prologue:
        needle = (
            "| Row 68 → Row 225 Row 68 → Row 65 second-pass meta prelude capstone reunion (row 245) |"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 245 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if PROLOGUE_STITCH_ANCHOR in prologue:
            prologue = prologue.replace(
                PROLOGUE_STITCH_ANCHOR,
                b["prologue_stitch"] + PROLOGUE_STITCH_ANCHOR,
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-245"></span>Row 245 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        prologue_path.write_text(prologue)
        print("prologue: added row 246")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "{#row-246-closing-loop}" not in epilogue:
        marker = ROW246_INSERT_MARKER
        if marker not in epilogue:
            raise SystemExit("epilogue row 245 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 246")
    else:
        print("epilogue: row 246 closing loop already present")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row226-writings-meta-prelude-capstone-reunion-index-row-246" not in sources:
        sources = sources.replace(
            "| 245 | Row 68 → Row 225 Row 68 → Row 65 second-pass meta prelude capstone",
            b["sources_table"] + "| 245 | Row 68 → Row 225 Row 68 → Row 65 second-pass meta prelude capstone",
            1,
        )
        src_header = (
            "## Row 68 → Row 225 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 245) "
            "{#row68-row225-second-pass-meta-prelude-capstone-reunion-index-row-245}"
        )
        if src_header in sources and b["sources_index"].strip() not in sources:
            sources = sources.replace(src_header, b["sources_index"] + src_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 246")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-246-baby-picture-row68-row226" not in memory:
        memory = memory.replace(
            "| 245 | Meta | [Row 68 → Row 225 second-pass meta prelude capstone reunion index](sources.md#row68-row225-second-pass-meta-prelude-capstone-reunion-index-row-245)",
            b["memory_table"]
            + "| 245 | Meta | [Row 68 → Row 225 second-pass meta prelude capstone reunion index](sources.md#row68-row225-second-pass-meta-prelude-capstone-reunion-index-row-245)",
            1,
        )
        inserted = False
        for baby_anchor in (
            "### Row 245 baby picture {#row-245-baby-picture-row68-row225-second-pass-meta-prelude-capstone-reunion}",
            "### Row 225 baby picture {#row-225-baby-picture-row68-row205-second-pass-meta-prelude-capstone-reunion}",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 246")


if __name__ == "__main__":
    main()
