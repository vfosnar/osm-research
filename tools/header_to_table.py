"""Convert the `key: value` header of candidate files into a Markdown table.

Idempotent: files whose header is already a table are left alone.
"""
import re, sys, pathlib

KEYS = ["name", "publisher", "url", "format", "coords", "records", "osm_tags",
        "osm_count_cz", "license", "license_url", "license_status", "update_freq",
        "impact", "verified"]
KEY_RE = re.compile(r"^(%s):\s?(.*)$" % "|".join(KEYS))

def convert(text):
    lines = text.split("\n")
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    fenced = lines[i].startswith("```")
    if fenced:
        i += 1
    start = i
    rows = []
    while i < len(lines):
        line = lines[i]
        if fenced and line.startswith("```"):
            i += 1
            break
        if not fenced and not line.strip():
            break
        m = KEY_RE.match(line)
        if m:
            rows.append([m.group(1), m.group(2).strip()])
        elif rows and line.strip():
            rows[-1][1] += " " + line.strip()   # continuation line
        elif line.strip():
            return None                          # not a header we understand
        i += 1
    if not rows or rows[0][0] != "name":
        return None
    title = rows[0][1]
    table = ["# " + title, "", "| Field | Value |", "|---|---|"]
    for k, v in rows[1:]:
        v = v.replace("|", "\\|").replace("<", "&lt;").replace(">", "&gt;")
        table.append(f"| {k} | {v} |")
    rest = "\n".join(lines[i:]).lstrip("\n")
    return "\n".join(table) + "\n\n" + rest

for p in sys.argv[1:]:
    path = pathlib.Path(p)
    new = convert(path.read_text())
    if new is None:
        print("skipped", p)
    else:
        path.write_text(new)
