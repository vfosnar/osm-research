# AGENTS.md

Instructions for AI agents (and humans) continuing this research. The human-readable
results live in `README.md`; this file documents how the research is done.

## Goal

Find open datasets that would have the biggest impact if imported or conflated into
OpenStreetMap in **Czechia**, with a licence compatible with ODbL. "Impact" means data
that map users actually need (POIs, infrastructure, accessibility…), not curiosities.

Look for **niche but useful** data. Data that government bodies publish directly as open
data (ministries, IPR Praha, city portals) is probably already being imported by someone, so
don't chase it. Better finds sit behind institutional systems, NGOs, associations and
hobby communities. Masaryk University's room system for indoor mapping
(`candidates/muni-indoor-munimap.md`) is the model example.

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
- Codeberg wiki `vfosnar/osm`, page `Synchronizace` (https://codeberg.org/vfosnar/osm/wiki/Synchronizace)
  — per-layer ZABAGED table with proposed OSM tags and status: 🟢 compared and missing objects
  added (MapRoulette link), 🟡 in progress, ⭐ suited for Sync. Treat 🟢/🟡/⭐ layers as known.
  Also Codeberg `osmcz/planovani` wiki.
- Codeberg `osmcz/iD`, branch `cz-develop` — the community iD fork for ČÚZK data. Read `ZABAGED.md`
  and `CONFLATION.md` there. `data/zabaged_osm_tags.json` is the community's ZABAGED→OSM tag
  mapping (173 tables, `todo` where the OSM idiom is unclear); use it rather than inventing tags.
  `osmcz/zabaged-map` is the supporting server for it (tiles + full-precision features).
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
- **When Postpass is down** (it returned 503 for a whole day on 27–28 September 2026):
  download the Czechia extract from the openstreetmap.fr mirror
  (`https://download.openstreetmap.fr/extracts/europe/czech_republic-latest.osm.pbf`, ~1.1 GB;
  Geofabrik's download server failed through this environment's proxy) and filter it with
  pyosmium (`pip install osmium`) into an NDJSON of the tags you need; match locally.
  Filtering the full extract takes about 25 minutes. The OSM API `map` call works for
  small bboxes.
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
| sync_fit | Sync / iD fork / MapRoulette (see below) |
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

`sync_fit` says which of the community's three routes into OSM fits the data. Read
Sync's `CONFIG.md` and `backend/README.md` (Codeberg `osmcz/sync`) before judging.

- **Sync** — points only. A dataset is a builtin source or an HTTP adapter returning a
  FeatureCollection; any source can be added that way. Auto-matching is by `ref_tag` only;
  everything else is matched by hand with scoring rules (distance, name, `tag_class`,
  `contains`). `create_keys` are the fixed tags written on new nodes, so the source
  category must map 1:1 to OSM tags. `licensed = true` lets only the ref (such as a
  Wikidata QID) flow and shows the rest for verification. Attribute enrichment of
  existing objects works through the update keys and the field-sync worker. A stable
  source ID is needed for ongoing sync.
- **iD fork** (`osmcz/iD` `cz-develop`) — geometry (lines, areas), ZABAGED first. Today the fork
  shows ZABAGED as a background layer and imports one right-clicked feature at a time (tags from
  `data/zabaged_osm_tags.json` plus `ref:zabaged`; waterways conflated onto existing ways), which
  nobody will do for a whole layer. The plan is a Sync-like geometry harness built into the fork:
  a dataset of lines/areas with stable IDs, matched against OSM and worked through as a queue.
  Candidates may assume that harness. What it needs from a source: stable feature IDs, a clear
  tag mapping (tables marked `todo` in the tag file need one first), and geometry good enough
  to conflate onto OSM.
- **MapRoulette** — pointers for a human: 1:N tag choices and lines/areas from sources other
  than ZABAGED. The ZABAGED challenges (pitches, dog-training grounds, cemeteries,
  communication towers) are standard challenges: the source only points to the place, the
  mapper draws the geometry from imagery and picks the tag. Non-ZABAGED geometry is never
  imported directly.

Write the value as the route plus a short reason, and split it per layer when a file
covers several datasets.

## Working rules

- ZABAGED is largely a compilation of data other agencies already publish, and it has far
  more object types than the POI import. For every government source, check the ZABAGED
  object catalogue (`https://geoportal.cuzk.gov.cz/Dokumenty/ZABAGED_katalog/CS/`) and name
  the overlapping type. Propose a primary source only for what ZABAGED lacks: object types,
  stable publisher IDs for Sync, attributes, smaller objects, fresher updates.
- Verify everything live. Never write a URL, licence or count you did not fetch.
- No "e.g." / "např." in candidate files: either a concrete source was investigated
  (name it) or it wasn't (leave it out, or list it as an open lead in `README.md`).
- Never write API keys or tokens into repo files, even public ones embedded in a web page
  (GitHub push protection blocks them). Say where to find the key instead.
- Don't draft emails, letters or consent requests to data holders. Communication is
  the community's job; candidate files only name who to contact.
- Research can be fanned out to parallel subagents by theme; each writes its own
  candidate files, so they don't conflict.
- Commit and push directly to `main`; no pull requests needed.
- After a round: regenerate
  the ranked table in `README.md`, commit, push.
