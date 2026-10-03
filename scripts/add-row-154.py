#!/usr/bin/env python3
"""Add row 154 (Row 68 → Row 134 ↔ Row 54 export meta prelude capstone on capstone path)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def tx(s: str, pairs: list[tuple[str, str]]) -> str:
    for a, b in pairs:
        s = s.replace(a, b)
    return s


def extract_between(text: str, start: str, end: str) -> str:
    i = text.find(start)
    if i < 0:
        raise SystemExit(f"start marker not found: {start[:80]}")
    j = text.find(end, i + len(start))
    if j < 0:
        raise SystemExit(f"end marker not found after {start[:40]}")
    return text[i:j]


def lift_114_to_134(s: str) -> str:
    p = [
        (
            "Row 68 → Row 94 Row 68 → Row 54 export meta prelude reunion",
            "Row 68 → Row 114 Row 68 → Row 54 export meta prelude capstone reunion",
        ),
        (
            "row68-row94-export-meta-prelude-reunion-index-row-114",
            "row68-row114-export-meta-prelude-capstone-reunion-index-row-134",
        ),
        (
            "row-114-baby-picture-row68-row94-export-meta-prelude-reunion",
            "row-134-baby-picture-row68-row114-export-meta-prelude-capstone-reunion",
        ),
        ("Row 114 names", "Row 134 names"),
        ("(row 114)", "(row 134)"),
        ("skill-navigation-row-114", "skill-navigation-row-134"),
        ("[row 113]", "__R113__"),
        ("row 113", "row 133"),
        ("Row 113", "Row 133"),
        ("__R113__", "[row 133]"),
        ("dynamics meta capstone", "dynamics meta prelude capstone"),
        ("export meta capstone", "export meta prelude capstone"),
        ("Export meta capstone", "Export meta prelude capstone"),
        ("export meta capstone", "export meta prelude capstone"),
        ("dynamics meta capstone", "dynamics meta prelude capstone"),
        ("Preface row 114", "Preface row 134"),
        ("preface row 114", "preface row 134"),
        ("memory sheet row 114", "memory sheet row 134"),
        ("Row 114 baby picture", "Row 134 baby picture"),
    ]
    return tx(s, p)


def lift_134_to_154(s: str) -> str:
    p = [
        ("skill-navigation-row-134", "skill-navigation-row-154"),
        ("### Row 134 skill checkpoint", "### Row 154 skill checkpoint"),
        ("Row 134 does not replace", "Row 154 does not replace"),
        ("Row 134 three-way audit", "Row 154 three-way audit"),
        ("Row 134 closing loop", "Row 154 closing loop"),
        ("row-134-closing-loop", "row-154-closing-loop"),
        ("Row 134 closing stitch", "Row 154 closing stitch"),
        ("row-134-closing-stitch", "row-154-closing-stitch"),
        ("prologue-preview-row-134", "prologue-preview-row-154"),
        ("Row 134 preview", "Row 154 preview"),
        ("Row 134 skill checkpoint", "Row 154 skill checkpoint"),
        ("memory sheet row 134", "memory sheet row 154"),
        ("Row 134 baby picture", "Row 154 baby picture"),
        (
            "Row 68 → Row 114 Row 68 → Row 54 export meta prelude capstone",
            "Row 68 → Row 134 Row 68 → Row 54 export meta prelude capstone",
        ),
        (
            "row68-row114-export-meta-prelude-capstone-reunion-index-row-134",
            "row68-row134-export-meta-prelude-capstone-reunion-index-row-154",
        ),
        (
            "row-134-baby-picture-row68-row114-export-meta-prelude-capstone-reunion",
            "row-154-baby-picture-row68-row134-export-meta-prelude-capstone-reunion",
        ),
        ("[row 135]", "__ROW155__"),
        ("[row 133]", "[row 153]"),
        ("row 133", "row 153"),
        ("Row 133", "Row 153"),
        ("__ROW155__", "[row 155]"),
        (
            "Row 68 → Row 114 export meta prelude capstone reunion index (row 134)",
            "Row 68 → Row 134 export meta prelude capstone reunion index (row 154)",
        ),
        (
            "row68-row94-export-meta-prelude-reunion-index-row-114",
            "row68-row134-export-meta-prelude-capstone-reunion-index-row-154",
        ),
        (
            "verified dynamics meta prelude capstone closure (row 133)",
            "verified dynamics meta prelude capstone closure (row 153)",
        ),
        ("when row 133 closed but row 54", "when row 153 closed but row 54"),
        ("when row 133 and row 54", "when row 153 and row 54"),
        (
            "rear-view mirror of row 133's finite-\\(T\\) dynamics → yaml handoff turn",
            "rear-view mirror of row 153's NPT dynamics → pedigree yaml handoff turn",
        ),
        (
            "when opening [row 115](preface.md#skill-navigation-row-115) before row 55 closes on the capstone path",
            "when opening [row 155](preface.md#skill-navigation-row-155) before row 55 closes on the capstone path",
        ),
        (
            "When row 133 is complete, proceed to [row 134](preface.md#skill-navigation-row-134) when dynamics meta prelude capstone is clean but export meta prelude capstone still lags after verified NPT archive on the capstone path",
            "When row 154 is complete, proceed to [row 155](preface.md#skill-navigation-row-155) when row 68 closed but electronic audit meta prelude capstone still lags after verified export meta prelude capstone on the capstone path",
        ),
        (
            "to [row 114](preface.md#skill-navigation-row-114) when dynamics meta capstone is clean but export meta capstone still lags on the opening-hinge path",
            "to [row 154](preface.md#skill-navigation-row-134) when dynamics meta prelude capstone is clean but export meta prelude still lags on the opening-hinge path",
        ),
        (
            "to [row 133](preface.md#skill-navigation-row-133) when atomistic meta prelude capstone still lags",
            "to [row 153](preface.md#skill-navigation-row-153) when dynamics meta prelude capstone still lags after verified atomistic meta prelude capstone on the capstone path, to [row 133](preface.md#skill-navigation-row-133) when atomistic meta prelude capstone still lags",
        ),
        (
            "before row 55 electronic audit meta prelude opens",
            "before row 55 electronic audit meta prelude capstone opens",
        ),
        (
            "before the electronic audit meta reunion",
            "before the electronic audit meta prelude capstone reunion",
        ),
        (
            "When row 136 is complete, proceed to [row 137]",
            "When row 134 is complete, proceed to [row 135]",
        ),
        ("Row 68 → Row 114 reunion index", "Row 68 → Row 134 reunion index"),
        ("row 134 (row 68 ↔ row 54 reunion", "row 154 (row 68 ↔ row 54 reunion"),
        ("row 114 (opening-hinge prelude stitch alone)", "row 134 (opening-hinge prelude stitch alone)"),
        ("row 114 names", "row 134 names"),
        ("row 134 names **why that reunion must follow verified dynamics meta prelude capstone (row 133)",
         "row 154 names **why that reunion must follow verified dynamics meta prelude capstone (row 153)"),
        ("Recite [preface row 153]", "Recite [preface row 153]"),
        (
            "Proceed to [row 115](#row-115-closing-loop) when row 68 closed but electronic audit meta prelude capstone still lags after row 134",
            "Proceed to [row 155](#row-154-closing-loop) when row 68 closed but electronic audit meta prelude capstone still lags after row 154 on the capstone path",
        ),
        (
            "Proceed to [row 134](#row-134-closing-loop) when row 68 closed but export meta prelude capstone still lags after row 133",
            "Proceed to [row 154](#row-154-closing-loop) when row 68 closed but export meta prelude capstone still lags after row 153 on the capstone path",
        ),
        ("after row 133 alone", "after row 153 alone"),
        ("row 133 closed dynamics", "row 153 closed dynamics"),
        ("| 134 |", "| 154 |"),
        ("preface row 134", "preface row 154"),
        ("prologue row 134", "prologue row 154"),
        ("epilogue row 134", "epilogue row 154"),
    ]
    return tx(s, p)


def dedupe_epilogue_closing_loops(ep: str) -> str:
    """Keep the first closing-loop block for each {#row-NNN-closing-loop} anchor."""
    header = re.compile(
        r"\n### Row \d+ closing loop[^\n]*\{#([^}]+)\}",
    )
    matches = list(header.finditer(ep))
    if not matches:
        return ep
    keep_ranges: list[tuple[int, int]] = []
    seen: set[str] = set()
    for i, m in enumerate(matches):
        anchor = m.group(1)
        if anchor in seen:
            continue
        seen.add(anchor)
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(ep)
        keep_ranges.append((start, end))
    if len(keep_ranges) == len(matches):
        return ep
    out = [ep[: matches[0].start()]]
    for start, end in keep_ranges:
        out.append(ep[start:end])
    return "".join(out)


def fix_row_153_epilogue_block(block: str) -> str:
    """Normalize row 153 closing loop to capstone row 152 wording."""
    p = [
        ("row 151 closed atomistic", "row 152 closed atomistic"),
        ("row 151 alone", "row 152 alone"),
        ("verified atomistic meta prelude capstone closure (row 151)", "verified atomistic meta prelude capstone closure (row 152)"),
        ("Row 68 → Row 53 meta (row 113)", "Row 68 → Row 53 meta (row 133)"),
        ("Do not conflate row 133 (row 68 ↔ row 53 reunion on the capstone path) with row 113",
         "Do not conflate row 153 (row 68 ↔ row 53 reunion on the capstone path) with row 133"),
        ("row 133 names **why that reunion must follow verified atomistic meta prelude capstone (row 151)",
         "row 153 names **why that reunion must follow verified atomistic meta prelude capstone (row 152)"),
        ("Proceed to [row 114](#row-114-closing-loop) when row 68 closed but export meta prelude capstone still lags after row 133",
         "Proceed to [row 154](#row-154-closing-loop) when row 68 closed but export meta prelude capstone still lags after row 153 on the capstone path"),
        ("to [row 151](#row-152-closing-loop)", "to [row 152](#row-152-closing-loop)"),
    ]
    return tx(block, p)


def add_row_154() -> None:
    ep_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep = ep_path.read_text()
    ep = dedupe_epilogue_closing_loops(ep)
    if ep.count("{#row-153-closing-loop}") == 1:
        start = ep.find("### Row 153 closing loop")
        end = ep.find("\n### Row 152 closing loop", start)
        if start >= 0 and end > start:
            ep = ep[:start] + fix_row_153_epilogue_block(ep[start:end]) + ep[end:]
    ep_path.write_text(ep)
    print("epilogue: deduped closing loops; normalized row 153 block")

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "skill-navigation-row-154" not in preface or "### Row 154 skill checkpoint" not in preface:
        m134 = re.search(
            r"(### Row 134 skill checkpoint.*?)(?=\n### Row 135 skill checkpoint)",
            preface,
            re.S,
        )
        if not m134:
            raise SystemExit("row 134 preface checkpoint missing")
        row154 = lift_134_to_154(m134.group(1))
        preface = re.sub(
            r"\n### Row 154 skill checkpoint.*?(?=\n## The copper wire through the book)",
            "",
            preface,
            flags=re.S,
        )
        anchor = "\n## The copper wire through the book"
        idx = preface.find(anchor)
        if idx < 0:
            raise SystemExit("copper wire anchor missing")
        preface = preface[:idx] + "\n" + row154 + preface[idx:]
        preface_path.write_text(preface)
        print("preface: added row 154")
    else:
        print("preface: row 154 already present")

    ep = ep_path.read_text()
    if "row-154-closing-loop" not in ep:
        block134 = extract_between(
            ep,
            "### Row 134 closing loop",
            "### Row 153 closing loop",
        )
        block154 = lift_134_to_154(block134)
        ep = ep.replace(
            "### Row 153 closing loop",
            block154 + "### Row 153 closing loop",
            1,
        )
        ep_path.write_text(ep)
        print("epilogue: added row 154 loop")

    pro_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    pro = pro_path.read_text()
    compass_line = (
        "| Row 68 → Row 134 Row 68 → Row 54 export meta prelude capstone reunion (row 154) |"
    )
    if compass_line not in pro:
        line153 = (
            "| Row 68 → Row 133 Row 68 → Row 53 dynamics meta prelude capstone reunion (row 153) |"
        )
        idx153 = pro.find(line153)
        if idx153 < 0:
            raise SystemExit("prologue compass row 153 not found")
        line_end153 = pro.find("\n", idx153)
        line134 = (
            "| Row 68 → Row 114 Row 68 → Row 54 export meta prelude capstone reunion (row 134) |"
        )
        idx134 = pro.find(line134)
        if idx134 < 0:
            raise SystemExit("prologue compass row 134 not found")
        line_end134 = pro.find("\n", idx134)
        compass154 = lift_134_to_154(pro[idx134:line_end134]) + "\n"
        pro = pro[: line_end153 + 1] + compass154 + pro[line_end153 + 1 :]
        preview134 = extract_between(
            pro,
            '| <span id="prologue-preview-row-134"></span>',
            '\n| <span id="prologue-preview-row-153"></span>',
        )
        preview154 = lift_134_to_154(preview134)
        pro = pro.replace(
            '| <span id="prologue-preview-row-134"></span>',
            preview154 + '| <span id="prologue-preview-row-134"></span>',
            1,
        )
        if "row-154-closing-stitch" not in pro:
            stitch = (
                "**Row 153 closing stitch (Row 68 → Row 133 Row 68 → Row 53 dynamics meta prelude capstone reunion).** {#row-154-closing-stitch} "
                "When row 152 closed — atomistic meta prelude capstone verified, row 151 or row 133 recited on the capstone path, and VIII.1 Bridge → VIII.2 NPT recited with "
                "[NPT Lab act](../part08-md/02-ensembles-integrators.md#lab-act-npt-tension-on-a-copper-nanowire-segment) archived `cu.elastic/` — but **row 54 VIII.2 → VIII.3 opening hinge still opens like standalone export homework after the thermostat Scene on the capstone path** — "
                "the [preface row 154 When-to-pause opening sentence](../preface.md#skill-navigation-row-154) names the dual reunion before the electronic audit meta prelude capstone reunion; "
                "read [preface row 154](../preface.md#skill-navigation-row-154), then the "
                "[Row 68 → Row 134 reunion index](../appendix/sources.md#row68-row134-export-meta-prelude-capstone-reunion-index-row-154), then "
                "[epilogue row 154 closing loop](../epilogue/multiscale.md#row-154-closing-loop) before row 55 electronic audit meta prelude capstone opens on the capstone path.\n\n"
            )
            pro = pro.replace("**Row 153 closing stitch", stitch + "**Row 153 closing stitch", 1)
        pro_path.write_text(pro)
        print("prologue: added row 154 compass/preview/stitch")

    src_path = ROOT / "writings/appendix/chapters/sources.md"
    src = src_path.read_text()
    if "row68-row134-export-meta-prelude-capstone-reunion-index-row-154" not in src:
        block114 = extract_between(
            src,
            "## Row 68 → Row 94 Row 68 → Row 54 export meta prelude reunion index (row 114)",
            "## Row 68 → Row 95 Row 68 → Row 55 electronic audit meta prelude reunion index (row 115)",
        )
        block154 = lift_134_to_154(lift_114_to_134(block114))
        table_row = (
            "| 154 | Row 68 → Row 134 Row 68 → Row 54 export meta prelude capstone (midpoint prelude gate ↔ dynamics meta prelude capstone ↔ row 54 meta) | "
            "[Row 68 → Row 134 export meta prelude capstone reunion index](#row68-row134-export-meta-prelude-capstone-reunion-index-row-154) · "
            "[preface row 154](../preface.md#skill-navigation-row-154) · "
            "[prologue row 154 preview](../prologue/00-many-scales.md#prologue-preview-row-154) · "
            "[prologue row 154 closing stitch](../prologue/00-many-scales.md#row-154-closing-stitch) · "
            "[epilogue row 154 closing loop](../epilogue/multiscale.md#row-154-closing-loop) · "
            "[memory sheet row 154 baby picture](memory-sheet.md#row-154-baby-picture-row68-row134-export-meta-prelude-capstone-reunion) | "
            "Row 68 closed but **row 54 VIII.2 → VIII.3 opening hinge still feels disconnected from verified dynamics meta prelude capstone on the capstone path** — "
            "read row 68 + row 153 or row 134 gate + VIII.2 Bridge → opening hinge → VIII.3 pedigree + row 54; "
            "[preface row 54](../preface.md#skill-navigation-row-54) |\n"
        )
        src = src.replace(
            "| 153 | Row 68 → Row 133 Row 68 → Row 53 dynamics meta prelude capstone",
            table_row + "| 153 | Row 68 → Row 133 Row 68 → Row 53 dynamics meta prelude capstone",
        )
        src = src.replace(
            "## Row 68 → Row 133 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 153)",
            block154 + "## Row 68 → Row 133 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 153)",
        )
        extra = (
            "[row 153](#row68-row134-export-meta-prelude-capstone-reunion-index-row-154) reunites **dynamics meta prelude capstone with the export meta prelude capstone boundary** "
            "when row 153 closed dynamics meta prelude capstone at verified NPT archive on the capstone path but VIII.2 Bridge and row 54 still read like separate courses after verified export meta prelude meta;"
        )
        if extra not in src:
            needle = (
                "[row 152](#row68-row133-dynamics-meta-prelude-capstone-reunion-index-row-153) reunites **atomistic meta prelude capstone with the dynamics meta prelude capstone boundary** "
            )
            if needle in src:
                src = src.replace(needle, needle + " " + extra)
        src_path.write_text(src)
        print("sources: added row 154 index")

    mem_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    mem = mem_path.read_text()
    if "row-154-baby-picture" not in mem:
        baby134 = extract_between(mem, "### Row 134 baby picture", "### Row 135 baby picture")
        baby154 = lift_134_to_154(baby134)
        mem = mem.replace("### Row 133 baby picture", baby154 + "### Row 133 baby picture", 1)
        mem_table = (
            "| 154 | Meta | Row 68 → Row 134 Row 68 → Row 54 export meta prelude capstone reunion | "
            "[Row 68 → Row 134 export meta prelude capstone reunion index](sources.md#row68-row134-export-meta-prelude-capstone-reunion-index-row-154) · "
            "[preface row 154 skill checkpoint](../preface.md#skill-navigation-row-154) · "
            "[prologue row 154 preview](../prologue/00-many-scales.md#prologue-preview-row-154) · "
            "[prologue row 154 closing stitch](../prologue/00-many-scales.md#row-154-closing-stitch) · "
            "[epilogue row 154 closing loop](../epilogue/multiscale.md#row-154-closing-loop) | "
            "Row 68 closed but row 54 VIII.2 → VIII.3 opening hinge feels disconnected from verified dynamics meta prelude capstone on the capstone path — "
            "read row 68 + row 153 or row 134 gate + VIII.2 Bridge → opening hinge → VIII.3 pedigree + row 54; "
            "[row 154 baby picture](#row-154-baby-picture-row68-row134-export-meta-prelude-capstone-reunion) |\n"
        )
        mem = mem.replace(
            "| 153 | Meta | Row 68 → Row 133 Row 68 → Row 53 dynamics meta prelude capstone reunion |",
            mem_table + "| 153 | Meta | Row 68 → Row 133 Row 68 → Row 53 dynamics meta prelude capstone reunion |",
        )
        if "When row 153 closed but export meta reunion still lags" not in mem:
            mem = mem.replace(
                "When row 152 closed but dynamics meta reunion still lags on the capstone path, switch to [row 153](#row-153-baby-picture-row68-row133-dynamics-meta-prelude-capstone-reunion).",
                "When row 152 closed but dynamics meta reunion still lags on the capstone path, switch to [row 153](#row-153-baby-picture-row68-row133-dynamics-meta-prelude-capstone-reunion). "
                "When row 153 closed but export meta reunion still lags on the capstone path, switch to [row 154](#row-154-baby-picture-row68-row134-export-meta-prelude-capstone-reunion).",
            )
        mem_path.write_text(mem)
        print("memory-sheet: added row 154")

    bridge_path = ROOT / "writings/md/chapters/02-ensembles-integrators.md"
    bridge = bridge_path.read_text()
    needle = "Row 68 → Row 133 dynamics meta prelude capstone reunion index"
    cross = (
        "On the capstone path, when row 153 closed dynamics meta prelude but row 54 still reads like coarse-graining homework, the "
        "[Row 68 → Row 134 export meta prelude capstone reunion index](../appendix/sources.md#row68-row134-export-meta-prelude-capstone-reunion-index-row-154) "
        "and [preface row 154 skill checkpoint](../preface.md#skill-navigation-row-154) reunite verified NPT archive with this Bridge before the pedigree checklist opens. "
    )
    if cross not in bridge and needle in bridge:
        bridge = bridge.replace(
            needle,
            cross.strip() + " — see also the " + needle,
            1,
        )
        bridge_path.write_text(bridge)
        print("VIII.2: row 154 cross-link")

    preface = preface_path.read_text()
    preface = preface.replace(
        "when opening [row 154](preface.md#skill-navigation-row-153) before row 54 closes",
        "when opening [row 154](preface.md#skill-navigation-row-154) before row 55 closes",
    )
    preface = preface.replace(
        "When row 153 is complete, proceed to [row 134](preface.md#skill-navigation-row-134) when dynamics meta prelude capstone is clean but export meta prelude capstone still lags after verified NPT archive on the capstone path",
        "When row 153 is complete, proceed to [row 154](preface.md#skill-navigation-row-154) when row 68 closed but export meta prelude capstone still lags after verified dynamics meta prelude capstone on the capstone path",
    )
    preface = preface.replace(
        "after row 133. Return to the [Row 68 → Row 133 reunion index]",
        "after row 152. Return to the [Row 68 → Row 133 reunion index]",
    )
    preface_path.write_text(preface)
    print("preface: row 153 → row 154 pointers")


def main() -> None:
    add_row_154()


if __name__ == "__main__":
    main()
