# osm-research

Research into open datasets that could be imported or conflated into OpenStreetMap in
Czechia, excluding what the community already covers (see `covered.md`).

- `covered.md` — sources already imported, in Sync, or in negotiation. Check before proposing.
- `candidates/` — one file per candidate source, with a verified URL, licence, OSM gap and impact.
- `tools/` — reusable queries (NKOD SPARQL, Postpass).

## Method

- Verify everything live. URLs, licences and tags recalled by a model are not trusted.
- Tags: read the OSM wiki page (raw wikitext via `index.php?action=raw`) and confirm usage in
  CZ with Geofabrik taginfo (`https://taginfo.geofabrik.de/europe:czech-republic/api/4/`).
- OSM coverage: taginfo for country-wide totals; Postpass
  (`POST https://postpass.geofabrik.de/api/interpreter`, `data=<SQL>`, `options[geojson]=false`)
  for bbox counts and sample matching. Joining against the CZ boundary polygon times out.
- Licence status: `ok` (CC0/PDDL/ODbL/explicit consent), `needs_waiver` (CC BY 4.0 etc.),
  `incompatible`, `unclear`.
