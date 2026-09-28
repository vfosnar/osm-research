# ParaglidingEarth – free-flying sites in Czechia

| Field | Value |
|---|---|
| publisher | paraglidingearth.com (collaborative worldwide free-flying site database, maintained by Raphaël, raphael /at/ disroot /dot/ org; source at https://framagit.org/raph-tr/paraglidingearth) |
| url | http://www.paraglidingearth.com/api/geojson/getCountrySites.php?iso=cz&style=detailled (API docs http://www.paraglidingearth.com/api/) |
| format | GeoJSON (also XML variant under /api/) |
| coords | yes (takeoff point; landing_lat/landing_lng and takeoff/landing parking as properties) |
| records | 159 CZ sites (fetched 2026-09-28): 106 with a landing point; paragliding=1 on all, hanggliding=1 on 22; per-direction wind suitability (N…NW, 0/1/2), takeoff_altitude, takeoff_description, flight_rules, thermals/soaring/winch/xc/flatland flags, stable `pge_site_id`; 28 with a last_edit date (12 edited on or after 2024-12-10) |
| osm_tags | sport=free_flying + free_flying:takeoff=yes (landing: free_flying:landing=yes), free_flying:paragliding=yes, free_flying:hanggliding=yes, direction=N;NE…, ele, name (wiki Tag:sport=free_flying) |
| osm_count_cz | sport=free_flying 43, free_flying:site=takeoff 14, free_flying:site=landing 4 (taginfo CZ 2026-09-28). Local match against the 2026-09-27 Czechia extract: 16 of 159 takeoffs and 7 of 106 landings have a free_flying feature within 500 m |
| license | CC BY-SA 3.0 Unported for the database; contributions made since 2024-12-10 are also added to a separate database under ODbL 1.0 |
| license_url | https://creativecommons.org/licenses/by-sa/3.0/ ; https://opendatacommons.org/licenses/odbl/summary/ |
| license_status | needs_waiver |
| update_freq | continuous (user-contributed) |
| impact | 3 |
| sync_fit | Sync (points, stable pge_site_id, category → sport=free_flying 1:1) |
| verified | yes |

## Try it
- **Map preview:** [samples/paraglidingearth-cz.geojson](../samples/paraglidingearth-cz.geojson): all 159
  CZ takeoffs and 106 landings. `in_osm_500m` marks the 16 takeoffs and 7 landings that already have a
  free-flying feature nearby.
- **QGIS:** *Layer → Add Layer → Add Vector Layer*, source type *Protocol: HTTP(S)*, type *GeoJSON*, URI
  `http://www.paraglidingearth.com/api/geojson/getCountrySites.php?iso=cz&style=detailled` (tested with
  curl: 159 features, 165 kB). Use `http://`, because HTTPS to this host was unreliable from here.
- **Web:** http://www.paraglidingearth.com/ (site pages `?site=<pge_site_id>`)

## Notes
- **Gap:** OSM has 43 `sport=free_flying` objects in Czechia. In the local match against the 2026-09-27
  extract, 143 of 159 takeoffs and 99 of 106 landing fields have nothing within 500 m.
- **Licence:** this is the only CZ free-flying dataset with an explicit open licence. CC BY-SA 3.0 is not
  accepted into OSM without a waiver, but the maintainer already publishes an ODbL database of new
  contributions. That suggests he would give consent for OSM, or put the older data under ODbL, if asked
  (contact above). Check the provenance of legacy entries before any import: the sites are user-submitted,
  and the licence does not say whether any were copied from other databases.
- **Versus Paragliding Mapa:** [paragliding-mapa-startovacky](paragliding-mapa-startovacky.md) has
  234 CZ sites with official/tolerated/forbidden status, but no licence. 117 of its sites have a PGE site
  within 500 m. PGE is the licensable subset. Descriptions are in mixed languages, and some sites are
  closed without being flagged (PGE has no status field), so a human should review each one. It is a
  good fit for a MapRoulette-style challenge rather than a blind import.
- **Mapping:** convert the direction flags (value 1 or 2) to `direction=S;SW;W`. takeoff_altitude
  becomes `ele`. Suggested ID `ref:paraglidingearth=<pge_site_id>` (not in use yet).
- Wiki pages read: Tag:sport=free_flying (free_flying:site marked deprecated in favour of
  free_flying:takeoff/landing), Key:direction. The OSM wiki has no page mentioning paraglidingearth
  (wiki search 2026-09-28).

## Wiki entry
```
===ParaglidingEarth – startoviště a přistávací plochy===
* dataset: getCountrySites (iso=cz)
* gestor: [http://www.paraglidingearth.com/ ParaglidingEarth]
* licence: CC BY-SA 3.0 [https://creativecommons.org/licenses/by-sa/3.0/]; příspěvky od 10. 12. 2024 i ODbL 1.0 [https://opendatacommons.org/licenses/odbl/summary/]
* datové primitivy: body
* odkaz: http://www.paraglidingearth.com/api/geojson/getCountrySites.php?iso=cz&style=detailled
* navržený tag {{tag|sport|free_flying}} + {{tag|free_flying:takeoff|yes}} / {{tag|free_flying:landing|yes}}, {{tag|direction|<směry>}}, {{tag|ref:paraglidingearth|<pge_site_id>}}
* poznámka: 143 ze 159 startovišť a 99 ze 106 přistávacích ploch v ČR v OSM chybí; pro starší data (CC BY-SA) je nutný souhlas správce
```
