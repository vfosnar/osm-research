# AGENTS.md

Instructions for AI agents (and humans) continuing this research. The human-readable
results live in `README.md`; this file documents how the research is done.

## Goal

Find open datasets that would have the biggest impact if imported or conflated into
OpenStreetMap in **Czechia**, with a licence compatible with ODbL. "Impact" means data
that map users actually need (POIs, infrastructure, accessibility…), not curiosities.

Never propose anything already known. Known sources are tracked upstream (see below),
not in this repo — check the upstream sources directly at the start of every round.
This repo is only the working memory for new research.

## Repository layout

| Path | Contents |
|---|---|
| `README.md` | Human-readable ranked shortlist and summary. Regenerate after new findings. |
| `AGENTS.md` | This file: method, tools, conventions. |
| `candidates/<slug>.md` | One file per candidate source (format below). Prague sources use `prague-` prefix. |
| `research/` | Human-readable write-ups of broader investigations (e.g. what sources other maps use). |
| `samples/` | Small GeoJSON extracts for previewing candidates on GitHub's map view (see `samples/README.md` for sources and licences). |
| `tools/` | Reusable queries and scripts (e.g. `nkod-queries.md`, `header_to_table.py`). |

## Where known sources are tracked (upstream)

Read these at the start of each round; don't copy them into this repo:

- OSM wiki `Cs:POI_ZABAGED_Import` — ZABAGED POI layers (✅ = imported).
- OSM wiki `Cs:Česko/freemap` — permissions granted, potential sources, finished imports.
- OSM wiki `Cs:Česko/freemap#Potencionální_zdroje` — ideas already listed; not new.
- OSM wiki `Cs:Zdroje_v_jednani` — sources being negotiated.
- OSM wiki pages with prefix `Cs:Import` (list via
  `api.php?action=query&list=allpages&apprefix=Cs:Import`).
- `https://codeberg.org/osmcz/sync/raw/branch/main/backend/config.toml` — every
  `[group.X.dataset.Y]` is a dataset already in the Sync conflation tool.
- Codeberg repos of `osmcz` and `vfosnar` (e.g. `jizdni-rady-osm`, `mcom-contributions`).
- talk-cz archive: `https://osmap.vfosnar.cz/talkcz` (fetch with WebFetch; plain curl
  returns an empty JS shell).

## Tools and endpoints

Overpass is **not** used (blocked/timeouts from this environment, and the user prefers
Postpass).

- **OSM wiki, raw wikitext** — always read the tag page before writing tags; models
  misremember tags and tagging rules:
  `curl -G https://wiki.openstreetmap.org/w/index.php --data-urlencode 'title=Tag:amenity=pharmacy' --data action=raw`
  Also check the `Cs:` variant. Cite the page used.
- **Taginfo for Czechia (Geofabrik)** — country-wide counts and actual usage:
  - `https://taginfo.geofabrik.de/europe:czech-republic/api/4/tag/stats?key=K&value=V`
  - `https://taginfo.geofabrik.de/europe:czech-republic/api/4/key/values?key=brand&query=NAME`
- **Postpass (SQL over OSM)** — bbox counts and sample matching:
  ```
  curl https://postpass.geofabrik.de/api/interpreter \
    --data-urlencode "data=SELECT count(*) AS n FROM postpass_pointpolygon
      WHERE tags->>'amenity'='pharmacy'
      AND geom && ST_MakeEnvelope(minlon,minlat,maxlon,maxlat,4326)" \
    --data-urlencode "options[geojson]=false"
  ```
  - Use `/api/interpreter` (the `/api/0.2/` path redirects).
  - Tables: `postpass_point`, `postpass_line`, `postpass_polygon`, and combined
    `postpass_pointpolygon`, `postpass_pointline`, `postpass_pointlinepolygon`.
    Columns: `tags` (jsonb), `geom` (EPSG:4326), `osm_type`, `osm_id`.
  - Bbox queries are fast. Joining against the CZ border polygon timed out (>120 s).
    The CZ bbox `12.09,48.55,18.86,51.06` includes neighbouring countries, so use
    taginfo for national totals.
  - Non-count queries without `options[geojson]=false` must return a `geom` column.
- **NKOD (national open data catalogue) SPARQL** — `https://data.gov.cz/sparql`
  (DCAT-AP). Saved queries go in `tools/nkod-queries.md`.
- **AllThePlaces** — `alltheplaces.xyz`; spiders already in Sync are the `[group.atp.dataset.*]` entries of Sync's `config.toml`.
- GitHub API is rate-limited/blocked (403) from this environment; Codeberg API works.

## Candidate file format

`candidates/<slug>.md` starts with a title and a two-column table (plain `key: value`
lines collapse into one paragraph on GitHub). Escape `|` as `\|` and `<`/`>` as
`&lt;`/`&gt;` inside the table. `tools/header_to_table.py` converts the old format.

```
# <name>

| Field | Value |
|---|---|
| publisher | |
| url | exact, verified download/API URL |
| format | |
| coords | yes / no / address-only |
| records | |
| osm_tags | checked against the wiki page, cited in notes |
| osm_count_cz | from taginfo or Postpass, with date |
| license | |
| license_url | |
| license_status | ok / needs_waiver / incompatible / unclear |
| update_freq | |
| impact | 1–5 |
| verified | yes / partial |
```

Then a `## Try it` section so a reader can see the data within a minute:

- **Map preview:** link to `samples/<slug>.geojson` — a small WGS84 extract (one town or
  area that shows the OSM gap, ≤ 2,000 features, ≤ 1 MB). GitHub renders `.geojson`
  files as a map. Skip it when the licence is `unclear` or `incompatible`; list the
  source and licence of every sample in `samples/README.md`.
- **QGIS:** exactly what to paste and where (e.g. *Layer → Add Layer → Add Vector
  Layer* with a URL or `/vsizip/vsicurl/…` path, a WFS/ArcGIS REST connection URL, CSV
  delimiter and X/Y columns, CRS). Test it — at least open the URL and check the format.
- Optionally a web viewer the publisher runs.

Followed by notes: gap analysis, caveats, suggested `ref:*` key, contacts.

If the source is already on `Cs:Česko/freemap#Potencionální_zdroje`, name the file
`known-<slug>.md` and start the notes with "Known (listed on Cs:Česko/freemap) — adds: …".

Every file ends with a `## Wiki entry` section: a wikitext block in Czech, ready to paste
into `Cs:Česko/freemap`, following that page's conventions:

```
===<Název>===
* dataset: <název datasetu>
* gestor: [<url> <organizace>]
* licence: <licence> [<licence_url>]
* datové primitivy: body/linie/plochy
* odkaz: <download url>
* navržený tag {{tag|key|value}}, {{tag|ref:…|<id>}}
* poznámka: <one sentence on the OSM gap>
```

The community hand-picks entries from these and appends them to the wiki page.

## Licence rules

- `ok` — CC0, PDDL, ODbL, or explicit consent for OSM (as recorded on `Cs:Česko/freemap`).
- `needs_waiver` — CC BY 4.0 or other attribution licences. The OSM Licensing Working
  Group requires an explicit waiver/consent; ČÚZK is the precedent (CC BY 4.0 + consent).
- Czech *úřední dílo* (§3 of the Copyright Act) is not protected by copyright, but the
  database *sui generis* right may still apply — flag it, don't assume it's fine.
- `incompatible` — non-commercial, no-derivatives, or terms forbidding reuse.
- `unclear` — no licence found; note who to contact.

## Scoring impact (1–5)

Rough product of: number of features missing in OSM × usefulness to map users ×
data quality (coordinates, stable IDs, update frequency). A stable ID is important,
because the community prefers ongoing sync (via Sync) over one-shot imports.

## Working rules

- Verify everything live. Never write a URL, licence or count you did not fetch.
- Research can be fanned out to parallel subagents by theme; each writes its own
  candidate files, so they don't conflict.
- Commit and push directly to `main`; no pull requests needed.
- After a round: regenerate
  the ranked table in `README.md`, commit, push.
