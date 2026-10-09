#!/usr/bin/env python3
"""Add row 248 meta-stitch (Row 68 → Row 228 ↔ Row 48 midpoint meta prelude capstone reunion, full capstone path)."""
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


def bump228_to_248(text: str) -> str:
    protected = (
        ("row-248-", "__P248__"),
        ("skill-navigation-row-248", "__S248__"),
        ("prologue-preview-row-248", "__prologue-preview-row-248__"),
        ("{#row-248-closing-stitch}", "__{#row-248-closing-stitch}__"),
        ("{#row-248-closing-loop}", "__{#row-248-closing-loop}__"),
        (
            "row68-row228-midpoint-meta-prelude-capstone-reunion-index-row-248",
            "__row68-row228-midpoint-meta-prelude-capstone-reunion-index-row-248__",
        ),
        (
            "row-248-baby-picture-row68-row228-midpoint-meta-prelude-capstone-reunion",
            "__row-248-baby-picture-row68-row228-midpoint-meta-prelude-capstone-reunion__",
        ),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = shift_meta_bump(out, 20)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add228():
    spec = importlib.util.spec_from_file_location("add228", ROOT / "scripts/add-row-228.py")
    add228 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add228)
    return add228


def _row248_sources_index() -> str:
    """Single row-248 reunion index block (avoid duplicating legacy row-228 index trees)."""
    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    header = (
        "## Row 68 → Row 228 Row 68 → Row 48 midpoint meta prelude capstone reunion index (row 248) "
        "{#row68-row228-midpoint-meta-prelude-capstone-reunion-index-row-248}"
    )
    if header in sources:
        start = sources.index(header)
        end = sources.find(
            "\n\n## Row 68 → Row 227 Row 68 → Row 67 part-boundary meta prelude capstone reunion index (row 247)",
            start,
        )
        if end != -1:
            return sources[start:end].strip() + "\n\n"
    preface = bump228_to_248(
        (ROOT / "writings/preface/chapters/preface.md")
        .read_text()
        .split("### Row 228 skill checkpoint", 1)[1]
        .split("### Row 229 skill checkpoint", 1)[0]
    )
    return (
        header
        + "\n\n"
        + "Row 248 closes the **midpoint meta prelude capstone** on the full capstone path — "
        + "see [preface row 248](../preface.md#skill-navigation-row-248) and the five-step audit in:\n\n"
        + preface[:800]
        + "…\n\n"
    )


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 228 skill checkpoint")
    end = preface.index("\n\n### Row 229 skill checkpoint", start)
    row248_preface = bump228_to_248(preface[start:end]).strip() + "\n\n"

    b228 = _load_add228()._build_blocks()
    out = {
        "row248_preface": row248_preface,
        "prologue_compass": bump228_to_248(b228["prologue_compass"]),
        "prologue_stitch": bump228_to_248(b228["prologue_stitch"]),
        "prologue_preview": bump228_to_248(b228["prologue_preview"]),
        "epilogue_loop": bump228_to_248(b228["epilogue_loop"]),
        "sources_table": bump228_to_248(b228["sources_table"]).replace(
            "| 228 | Row 68 → Row 208", "| 248 | Row 68 → Row 228", 1
        ),
        "memory_table": (
            "| 248 | Meta | [Row 68 → Row 228 midpoint meta prelude capstone reunion index]"
            "(sources.md#row68-row228-midpoint-meta-prelude-capstone-reunion-index-row-248) · "
            "[preface row 248 skill checkpoint](../preface.md#skill-navigation-row-248) · "
            "[prologue row 248 preview](../prologue/00-many-scales.md#prologue-preview-row-248) · "
            "[prologue row 248 closing stitch](../prologue/00-many-scales.md#row-248-closing-stitch) · "
            "[epilogue row 248 closing loop](../epilogue/multiscale.md#row-248-closing-loop) | "
            "Row 68 closed but row 48 midpoint meta reunion feels disconnected from verified "
            "part-boundary meta prelude capstone on the full capstone path — read row 68 + row 247 or "
            "row 228 gate + VI.4 intermission → VII.0 Bridge + row 48; confirm `hardening.yaml` beside Act IV; "
            "[row 248 baby picture](#row-248-baby-picture-row68-row228-midpoint-meta-prelude-capstone-reunion) |\n"
        ),
        "sources_index": _row248_sources_index(),
        "memory_baby": (
            "### Row 248 baby picture {#row-248-baby-picture-row68-row228-midpoint-meta-prelude-capstone-reunion}\n\n"
            "**Row 248 baby picture:** when row 68 closed the midpoint prelude and row 247 or row 228 "
            "closed part-boundary meta prelude capstone / midpoint meta prelude on the full capstone path "
            "but **row 48's VI.4 intermission → Bridge or `writings/continuum` → `writings/defects` handoff still "
            "feel like separate checklists on the full capstone path**, open the "
            "[Row 68 → Row 228 midpoint meta prelude capstone reunion index]"
            "(sources.md#row68-row228-midpoint-meta-prelude-capstone-reunion-index-row-248) — read "
            "[preface row 68](../preface.md#skill-navigation-row-68) gate → "
            "[preface row 247](../preface.md#skill-navigation-row-247) or "
            "[preface row 228](../preface.md#skill-navigation-row-228) part-boundary meta prelude capstone / "
            "midpoint meta prelude gate → [VI.4 intermission](../part06-continuum/04-nonlinear-plasticity-preview.md#intermission-ascent-ends-descent-begins) "
            "through [VII.0 descent hinge from VI.4](../part07-defects/00-opening.md#descent-hinge-from-vi4-energy-break-forest-begins) "
            "aloud → [preface row 48](../preface.md#skill-navigation-row-48) five-step audit → confirm "
            "`hardening.yaml` beside Act IV before row 249 taxonomy meta prelude capstone opens on the full capstone path.\n\n"
            "```mermaid\nflowchart LR\n  MP[Midpoint row 68]\n  PB[Part-boundary meta row 247]\n"
            "  BR[Intermission Bridge VI.4 to VII.0]\n  R48[row 48 meta gate]\n  MP --> PB --> BR --> R48\n```\n\n"
            "When row 248 feels disconnected from row 247, read them as **part-boundary meta prelude capstone "
            "vs midpoint meta prelude capstones on the full capstone path**: row 247 when "
            "**V.4 → VI.0 twin-ladder reunion must read on the same wire before any continuum → defects audit "
            "on the full capstone path**; row 248 when "
            "**VI.4 intermission and Row 67 → Row 48 meta must read on the same wire before "
            "row 249 taxonomy meta prelude capstone opens on the full capstone path** — "
            "same copper wire, same Functional Analysis Notes layout, one continuous twin-ladder → forest "
            "afternoon after verified part-boundary meta prelude capstone on the full capstone path. "
            "When row 247 closed but midpoint meta reunion still lags on the full capstone path, switch to [row 248]"
            "(#row-248-baby-picture-row68-row228-midpoint-meta-prelude-capstone-reunion).\n\n\n"
        ),
    }
    loop = out["epilogue_loop"]
    loop = loop.replace(
        "### Row 248 closing loop (Row 68 → Row 228",
        "### Row 228 closing loop (Row 68 → Row 228",
        1,
    )
    for spill in ("\n\n\n\n### Row 247 closing loop", "\n\n\n\n### Row 248 closing loop"):
        if spill in loop:
            loop = loop.split(spill, 1)[0].rstrip() + "\n\n"
            break
    out["epilogue_loop"] = loop.rstrip() + "\n\n"
    return out


PROLOGUE_STITCH_ANCHOR = (
    "**Row 247 closing stitch (Row 68 → Row 227 Row 68 → Row 67 part-boundary meta prelude capstone reunion).** {#row-247-closing-stitch}"
)

ROW248_INSERT_MARKER = (
    "### Row 227 closing loop (Row 68 → Row 227 Row 68 → Row 67 part-boundary meta prelude capstone reunion) {#row-247-closing-loop}"
)

ROW247_EPILOGUE_OLD = (
    "Proceed to [row 248](#row-228-closing-loop) when row 68 closed but midpoint meta prelude capstone still lags after row 247 on the full capstone path,"
)
ROW247_EPILOGUE_NEW = (
    "Proceed to [row 248](#row-248-closing-loop) when row 68 closed but midpoint meta prelude capstone still lags after row 247 on the full capstone path,"
)


def _strip_orphan_row248_epilogue(text: str) -> str:
    """Remove row-248 closing loops (partial bumps or misplaced duplicates)."""
    pattern = (
        r"\n\n### Row 228 closing loop \(Row 68 → Row 228 Row 68 → Row 48 "
        r"midpoint meta prelude capstone reunion\) \{#row-248-closing-loop\}.*?"
        r"(?=\n\n### Row \d+ closing loop)"
    )
    return re.sub(pattern, "", text, flags=re.DOTALL)


def _epilogue_has_row248_at_capstone(text: str) -> bool:
    marker = ROW248_INSERT_MARKER
    if marker not in text:
        return False
    idx = text.index(marker)
    window = text[max(0, idx - 12000) : idx]
    return "{#row-248-closing-loop}" in window and "memory sheet row 248" in window


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 248 skill checkpoint" in preface:
        print("preface: row 248 already present")
    else:
        if "### Row 247 skill checkpoint" not in preface:
            raise SystemExit("row 247 must exist before row 248")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row248_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 248")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "midpoint meta prelude capstone reunion (row 248) |" not in prologue and (
        "prologue-preview-row-248" not in prologue
    ):
        needle = (
            "| Row 68 → Row 227 Row 68 → Row 67 part-boundary meta prelude capstone reunion (row 247) |"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 247 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if PROLOGUE_STITCH_ANCHOR in prologue:
            prologue = prologue.replace(
                PROLOGUE_STITCH_ANCHOR,
                b["prologue_stitch"] + PROLOGUE_STITCH_ANCHOR,
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-247"></span>Row 247 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        prologue_path.write_text(prologue)
        print("prologue: added row 248")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    epilogue = _strip_orphan_row248_epilogue(epilogue)
    epilogue = epilogue.replace(ROW247_EPILOGUE_OLD, ROW247_EPILOGUE_NEW)
    if not _epilogue_has_row248_at_capstone(epilogue):
        marker = ROW248_INSERT_MARKER
        if marker not in epilogue:
            raise SystemExit("epilogue row 247 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 248")
    else:
        epilogue_path.write_text(epilogue)
        print("epilogue: row 248 closing loop already present at capstone anchor")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row228-midpoint-meta-prelude-capstone-reunion-index-row-248" not in sources:
        sources = sources.replace(
            "| 247 | Row 68 → Row 227 Row 68 → Row 67 part-boundary meta prelude capstone",
            b["sources_table"] + "| 247 | Row 68 → Row 227 Row 68 → Row 67 part-boundary meta prelude capstone",
            1,
        )
        src_header = (
            "## Row 68 → Row 227 Row 68 → Row 67 part-boundary meta prelude capstone reunion index (row 247) "
            "{#row68-row227-part-boundary-meta-prelude-capstone-reunion-index-row-247}"
        )
        if src_header in sources and b["sources_index"].strip() not in sources:
            sources = sources.replace(src_header, b["sources_index"] + src_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 248")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "### Row 248 baby picture {#row-248-baby-picture-row68-row228" not in memory:
        memory = memory.replace(
            "| 247 | Meta | [Row 68 → Row 227 part-boundary meta prelude capstone reunion index](sources.md#row68-row227-part-boundary-meta-prelude-capstone-reunion-index-row-247)",
            b["memory_table"]
            + "| 247 | Meta | [Row 68 → Row 227 part-boundary meta prelude capstone reunion index](sources.md#row68-row227-part-boundary-meta-prelude-capstone-reunion-index-row-247)",
            1,
        )
        inserted = False
        for baby_anchor in (
            "### Row 247 baby picture {#row-247-baby-picture-row68-row227-part-boundary-meta-prelude-capstone-reunion}",
            "### Row 227 baby picture {#row-227-baby-picture-row68-row207-part-boundary-meta-prelude-capstone-reunion}",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 248")
    else:
        memory_path.write_text(memory)
        print("memory-sheet: row 248 baby already present")


if __name__ == "__main__":
    main()
