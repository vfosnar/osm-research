#!/usr/bin/env python3
"""Add a Route column to the README shortlist tables and regenerate the "By route" section.

Route comes from each candidate's `sync_fit` row (Sync / iD fork / MapRoulette, in the order
they appear). Idempotent: rerun after adding candidates or changing sync_fit values.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ROUTES = ["Sync", "iD fork", "MapRoulette"]


def field(text, name):
    m = re.search(rf"^\| {re.escape(name)} \| (.*) \|$", text, re.M)
    return m.group(1).strip() if m else ""


def candidates():
    out = {}
    for p in sorted((ROOT / "candidates").glob("*.md")):
        t = p.read_text()
        sf = field(t, "sync_fit")
        found = sorted({r for r in ROUTES if r in sf}, key=sf.index)
        title = t.splitlines()[0].lstrip("# ").strip()
        imp = field(t, "impact")
        out[p.name] = {
            "routes": found,
            "title": title,
            "impact": int(imp[0]) if imp[:1].isdigit() else 0,
            "licence": field(t, "license_status").split()[0] if field(t, "license_status") else "",
        }
    return out


def route_label(c):
    return " + ".join(c["routes"]) if c["routes"] else "–"


def add_route_column(lines, cands):
    out, in_table = [], False
    for line in lines:
        if line.startswith("| Source |"):
            in_table = True
            if "| Route |" not in line:
                line = line.rstrip() + " Route |"
        elif in_table and line.startswith("|---"):
            if line.count("|") == out[-1].count("|") - 1:
                line = line.rstrip() + "---|"
        elif in_table and line.startswith("|"):
            m = re.search(r"\(candidates/([^)]+\.md)\)", line)
            cells = line.rstrip().rstrip("|").split(" | ")
            label = route_label(cands[m.group(1)]) if m and m.group(1) in cands else "–"
            ncols = next(l for l in reversed(out) if l.startswith("| Source |")).count("|") - 1
            if line.count("|") - 1 < ncols:
                line = line.rstrip() + f" {label} |"
            else:  # refresh existing value
                parts = line.rstrip().split("|")
                parts[-2] = f" {label} "
                line = "|".join(parts)
        else:
            in_table = False
        out.append(line)
    return out


def by_route_section(cands):
    lic = {"ok": "✅", "needs_waiver": "✍️", "unclear": "❓", "incompatible": "❌"}
    s = ["## By route", "",
         "Which of the community's routes into OSM fits each candidate (the `sync_fit` row; see",
         "[AGENTS.md](AGENTS.md#scoring-impact-15)). Sorted by impact; the icon is the licence status.",
         "A candidate with several layers can appear under more than one route.", ""]
    for r, blurb in [("Sync", "points with a stable ID and a 1:1 tag mapping"),
                     ("iD fork", "lines and areas for the planned geometry harness in the osmcz iD fork"),
                     ("MapRoulette", "pointers for a human: tag choices, no stable ID, or needs a look")]:
        items = sorted(((n, c) for n, c in cands.items() if r in c["routes"]),
                       key=lambda x: (-x[1]["impact"], x[1]["title"]))
        s.append(f"### {r} — {blurb} ({len(items)})")
        s.append("")
        s.extend(
            f"- {lic.get(c['licence'], '')} [{c['title'].split(' – ')[0].split(' (')[0]}](candidates/{n}) — impact {c['impact']}"
            for n, c in items)
        s.append("")
    return s


def main():
    p = ROOT / "README.md"
    lines = p.read_text().splitlines()
    cands = candidates()
    lines = add_route_column(lines, cands)
    text = "\n".join(lines) + "\n"
    section = "\n".join(by_route_section(cands)) + "\n"
    if "\n## By route\n" in text:
        text = re.sub(r"\n## By route\n.*?(?=\n## )", "\n" + section.rstrip("\n") + "\n", text, flags=re.S)
    else:
        text = text.replace("\n## What's already covered\n", "\n" + section + "\n## What's already covered\n")
    p.write_text(text)


if __name__ == "__main__":
    main()
