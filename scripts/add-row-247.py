#!/usr/bin/env python3
"""Add row 247 meta-stitch (Row 68 → Row 227 ↔ Row 67 part-boundary meta prelude capstone reunion, full capstone path)."""
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


def bump227_to_247(text: str) -> str:
    protected = (
        ("row-247-", "__P247__"),
        ("skill-navigation-row-247", "__S247__"),
        ("prologue-preview-row-247", "__prologue-preview-row-247__"),
        ("{#row-247-closing-stitch}", "__{#row-247-closing-stitch}__"),
        ("{#row-247-closing-loop}", "__{#row-247-closing-loop}__"),
        (
            "row68-row227-part-boundary-meta-prelude-capstone-reunion-index-row-247",
            "__row68-row227-part-boundary-meta-prelude-capstone-reunion-index-row-247__",
        ),
        (
            "row-247-baby-picture-row68-row227-part-boundary-meta-prelude-capstone-reunion",
            "__row-247-baby-picture-row68-row227-part-boundary-meta-prelude-capstone-reunion__",
        ),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = shift_meta_bump(out, 20)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add227():
    spec = importlib.util.spec_from_file_location("add227", ROOT / "scripts/add-row-227.py")
    add227 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add227)
    return add227


def _row247_sources_index() -> str:
    """Single row-247 reunion index block (avoid duplicating legacy row-227 index trees)."""
    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    header = (
        "## Row 68 → Row 227 Row 68 → Row 67 part-boundary meta prelude capstone reunion index (row 247) "
        "{#row68-row227-part-boundary-meta-prelude-capstone-reunion-index-row-247}"
    )
    if header in sources:
        start = sources.index(header)
        end = sources.find(
            "\n\n## Row 68 → Row 226 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 246)",
            start,
        )
        if end != -1:
            return sources[start:end].strip() + "\n\n"
    preface = bump227_to_247(
        (ROOT / "writings/preface/chapters/preface.md")
        .read_text()
        .split("### Row 227 skill checkpoint", 1)[1]
        .split("### Row 228 skill checkpoint", 1)[0]
    )
    return (
        header
        + "\n\n"
        + "Row 247 closes the **part-boundary meta prelude capstone** on the full capstone path — "
        + "see [preface row 247](../preface.md#skill-navigation-row-247) and the five-step audit in:\n\n"
        + preface[:800]
        + "…\n\n"
    )


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 227 skill checkpoint")
    end = preface.index("\n\n### Row 228 skill checkpoint", start)
    row247_preface = bump227_to_247(preface[start:end]).strip() + "\n\n"

    b227 = _load_add227()._build_blocks()
    out = {
        "row247_preface": row247_preface,
        "prologue_compass": bump227_to_247(b227["prologue_compass"]),
        "prologue_stitch": bump227_to_247(b227["prologue_stitch"]),
        "prologue_preview": bump227_to_247(b227["prologue_preview"]),
        "epilogue_loop": bump227_to_247(b227["epilogue_loop"]),
        "sources_table": bump227_to_247(b227["sources_table"]).replace(
            "| 227 | Row 68 → Row 227", "| 247 | Row 68 → Row 227", 1
        ),
        "memory_table": (
            "| 247 | Meta | [Row 68 → Row 227 part-boundary meta prelude capstone reunion index]"
            "(sources.md#row68-row227-part-boundary-meta-prelude-capstone-reunion-index-row-247) · "
            "[preface row 247 skill checkpoint](../preface.md#skill-navigation-row-247) · "
            "[prologue row 247 preview](../prologue/00-many-scales.md#prologue-preview-row-247) · "
            "[prologue row 247 closing stitch](../prologue/00-many-scales.md#row-247-closing-stitch) · "
            "[epilogue row 247 closing loop](../epilogue/multiscale.md#row-247-closing-loop) | "
            "Row 68 closed but row 67 part-boundary meta reunion feels disconnected from verified "
            "Writings canonical meta prelude capstone on the full capstone path — read row 68 + row 246 or "
            "row 227 gate + V.4 Bridge → VI.0 twin-ladder + row 67; confirm `cht_export.yaml` beside both decks; "
            "[row 247 baby picture](#row-247-baby-picture-row68-row227-part-boundary-meta-prelude-capstone-reunion) |\n"
        ),
        "sources_index": _row247_sources_index(),
        "memory_baby": (
            "### Row 247 baby picture {#row-247-baby-picture-row68-row227-part-boundary-meta-prelude-capstone-reunion}\n\n"
            "**Row 247 baby picture:** when row 68 closed the midpoint prelude and row 246 or row 227 "
            "closed Writings canonical meta prelude capstone / part-boundary meta prelude on the full capstone path "
            "but **row 67's V.4 → VI.0 twin-ladder Bridge or `writings/fvm` → `writings/continuum` handoff still "
            "feel like separate checklists on the full capstone path**, open the "
            "[Row 68 → Row 227 part-boundary meta prelude capstone reunion index]"
            "(sources.md#row68-row227-part-boundary-meta-prelude-capstone-reunion-index-row-247) — read "
            "[preface row 68](../preface.md#skill-navigation-row-68) gate → "
            "[preface row 246](../preface.md#skill-navigation-row-246) or "
            "[preface row 227](../preface.md#skill-navigation-row-227) Writings canonical meta prelude capstone / "
            "part-boundary meta prelude gate → [V.4 Bridge](../part05-fvm/04-navier-stokes-cfd.md#bridge-to-part-vi) "
            "through [VI.0 twin ladders reunite](../part06-continuum/00-opening.md#the-twin-ladders-reunite-galerkin-and-conservation) "
            "aloud → [preface row 67](../preface.md#skill-navigation-row-67) five-step audit → confirm "
            "`cht_export.yaml` beside both decks before row 248 midpoint meta prelude capstone opens on the full capstone path.\n\n"
            "```mermaid\nflowchart LR\n  MP[Midpoint row 68]\n  WM[Writings meta prelude capstone row 246]\n"
            "  BR[Twin-ladder Bridge V.4 to VI.0]\n  R67[row 67 meta gate]\n  MP --> WM --> BR --> R67\n```\n\n"
            "When row 247 feels disconnected from row 246, read them as **Writings meta prelude capstone "
            "vs part-boundary meta prelude capstones on the full capstone path**: row 246 when "
            "**epilogue writings cross-links must reunite on verified second-pass meta prelude capstone "
            "before any fvm → continuum Bridge on the full capstone path**; row 247 when "
            "**V.4 → VI.0 twin-ladder reunion and Row 66 → Row 47 meta must read on the same wire before "
            "row 248 midpoint meta prelude capstone opens on the full capstone path** — "
            "same copper wire, same Functional Analysis Notes layout, one continuous single-manuscript-tree → "
            "Cauchy stress afternoon after verified Writings canonical meta prelude capstone on the full capstone path. "
            "When row 246 closed but twin-ladder reunion still lags on the full capstone path, switch to [row 247]"
            "(#row-247-baby-picture-row68-row227-part-boundary-meta-prelude-capstone-reunion).\n\n\n"
        ),
    }
    loop = out["epilogue_loop"]
    loop = loop.replace(
        "### Row 247 closing loop (Row 68 → Row 227",
        "### Row 227 closing loop (Row 68 → Row 227",
        1,
    )
    for spill in ("\n\n\n\n### Row 246 closing loop", "\n\n\n\n### Row 247 closing loop"):
        if spill in loop:
            loop = loop.split(spill, 1)[0].rstrip() + "\n\n"
            break
    out["epilogue_loop"] = loop.rstrip() + "\n\n"
    return out


PROLOGUE_STITCH_ANCHOR = (
    "**Row 246 closing stitch (Row 68 → Row 226 Row 68 → Row 66 Writings canonical meta prelude capstone reunion).** {#row-246-closing-stitch}"
)

ROW247_INSERT_MARKER = (
    "### Row 226 closing loop (Row 68 → Row 226 Row 68 → Row 66 Writings canonical meta prelude capstone reunion) {#row-246-closing-loop}"
)

ROW246_EPILOGUE_OLD = (
    "Proceed to [row 227](#row-227-closing-loop) when row 68 closed but part-boundary meta prelude capstone still lags after row 246 on the full capstone path,"
)
ROW246_EPILOGUE_NEW = (
    "Proceed to [row 247](#row-247-closing-loop) when row 68 closed but part-boundary meta prelude capstone still lags after row 246 on the full capstone path,"
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 247 skill checkpoint" in preface:
        print("preface: row 247 already present")
    else:
        if "### Row 246 skill checkpoint" not in preface:
            raise SystemExit("row 246 must exist before row 247")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row247_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 247")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "part-boundary meta prelude capstone reunion (row 247) |" not in prologue:
        needle = (
            "| Row 68 → Row 226 Row 68 → Row 66 Writings canonical meta prelude capstone reunion (row 246) |"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 246 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if PROLOGUE_STITCH_ANCHOR in prologue:
            prologue = prologue.replace(
                PROLOGUE_STITCH_ANCHOR,
                b["prologue_stitch"] + PROLOGUE_STITCH_ANCHOR,
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-246"></span>Row 246 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        prologue_path.write_text(prologue)
        print("prologue: added row 247")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "{#row-247-closing-loop}" not in epilogue:
        if ROW246_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW246_EPILOGUE_OLD, ROW246_EPILOGUE_NEW, 1)
        marker = ROW247_INSERT_MARKER
        if marker not in epilogue:
            raise SystemExit("epilogue row 246 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 247")
    else:
        print("epilogue: row 247 closing loop already present")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row227-part-boundary-meta-prelude-capstone-reunion-index-row-247" not in sources:
        sources = sources.replace(
            "| 246 | Row 68 → Row 226 Row 68 → Row 66 Writings canonical meta prelude capstone",
            b["sources_table"] + "| 246 | Row 68 → Row 226 Row 68 → Row 66 Writings canonical meta prelude capstone",
            1,
        )
        src_header = (
            "## Row 68 → Row 226 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 246) "
            "{#row68-row226-writings-meta-prelude-capstone-reunion-index-row-246}"
        )
        if src_header in sources and b["sources_index"].strip() not in sources:
            sources = sources.replace(src_header, b["sources_index"] + src_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 247")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "### Row 247 baby picture {#row-247-baby-picture-row68-row227" not in memory:
        memory = memory.replace(
            "| 246 | Meta | [Row 68 → Row 226 Writings canonical meta prelude capstone reunion index](sources.md#row68-row226-writings-meta-prelude-capstone-reunion-index-row-246)",
            b["memory_table"]
            + "| 246 | Meta | [Row 68 → Row 226 Writings canonical meta prelude capstone reunion index](sources.md#row68-row226-writings-meta-prelude-capstone-reunion-index-row-246)",
            1,
        )
        inserted = False
        for baby_anchor in (
            "### Row 246 baby picture {#row-246-baby-picture-row68-row226-writings-meta-prelude-capstone-reunion}",
            "### Row 226 baby picture {#row-226-baby-picture-row68-row206-writings-meta-prelude-capstone-reunion}",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 247")
    else:
        memory_path.write_text(memory)
        print("memory-sheet: row 247 baby already present (orphans stripped)")


if __name__ == "__main__":
    main()
