# Vetřelci a volavky – art in public space 1945–1989 (sculptures, reliefs, mosaics)

| Field | Value |
|---|---|
| publisher | Vetřelci a volavky, volunteer project led by sculptor Pavel Karous (https://vetrelciavolavky.cz/kontakt) |
| url | https://vetrelciavolavky.cz/mapa (Drupal gmap page, all markers inline as JSON); https://vetrelciavolavky.cz/kml (KML, coordinates only, empty names); detail pages https://vetrelciavolavky.cz/sochy/&lt;slug&gt; |
| format | HTML with embedded JSON markers; KML |
| coords | yes (WGS84, 5–6 decimals) |
| records | 2,970 markers (2,946 distinct slugs); 2,689 inside the CZ bbox, the rest mostly Slovakia. Each marker: slug, "artist, title, year, material, location" text. 49 texts say "odstraněno"/"zničen" |
| osm_tags | tourism=artwork + artwork_type=sculpture/statue/relief/mosaic + name + artist_name + start_date + material (Tag:tourism=artwork lists artwork_type, artist_name, start_date, material, name) |
| osm_count_cz | tourism=artwork 12,104; artist_name 1,466; artwork_type 9,829 (taginfo CZ, data until 2026-09-27) |
| license | none stated; site text is plain copyright, no terms for the data |
| license_url | – |
| license_status | unclear |
| update_freq | irregular, crowd-submitted ("vložte sochu" form) |
| impact | 3 |
| sync_fit | Sync (points; slug as ref, `create_keys` tourism=artwork; artist_name/start_date as update keys for enrichment) |
| verified | yes |

## Try it
- **Map preview:** none (licence unclear).
- **QGIS:** *Layer → Add Layer → Add Vector Layer*, source type *Protocol: HTTP(S)*, URI `https://vetrelciavolavky.cz/kml` (KML, EPSG:4326). It only has points without names; the attributes are in the `markers` array of https://vetrelciavolavky.cz/mapa (parse `latitude`, `longitude`, `text` → `href="/sochy/<slug>"` and the "artist, title, year, material, place" string).
- **Web:** https://vetrelciavolavky.cz/mapa

## Notes
- **What it is:** a curated inventory of "four-percent art" (the 1–4 % of state construction budgets spent on
  decoration) of the socialist era: sculptures, fountains, reliefs and mosaics on housing estates, schools,
  polyclinics. It is the best-known list of this kind in Czechia. Artists and years are researched by art
  historians, which OSM almost never has.
- **Gap (Postpass, 2026-09-28):** the 2,689 CZ-bbox points were matched against all
  tourism=artwork, historic=memorial and amenity=fountain objects (59,619 in the CZ bbox). 945 points have
  nothing within 75 m, and 1,266 have nothing within 30 m. Memorials inflate the matches, so the true gap is
  larger. By town (no OSM object within 75 m): Praha 213/833, Ostrava 45/75, Brno 41/141, Kladno 13/34,
  Plzeň 10/33, Most 7/47.
- **Enrichment:** of the 1,744 points with an OSM object within 75 m, the nearest object has `artist_name`
  in only 286 cases. Artist, title and year could be added to about 1,450 existing objects.
- **Caveats:** removed works stay in the database (49 texts flag "odstraněno"/"zničen", more are removed
  without a flag), some works are inside buildings or metro vestibules, and positions are hand-placed on
  Google Maps. A survey step (MapRoulette-style check, or Sync manual review) is needed; don't bulk-import.
  The text field must be split (artist, title, year, material, location); it is comma-separated but the
  location part contains commas.
- **Suggested ref:** `ref:vetrelciavolavky=<slug>` (slug from `/sochy/<slug>`, stable Drupal path).
- **Known check:** not on Cs:Česko/freemap, Cs:Zdroje_v_jednani or in Sync config.toml. The related
  `sochyamesta.cz` is already listed on Cs:Česko/freemap.
- **Contact:** Pavel Karous (project author, contact listed on https://vetrelciavolavky.cz/kontakt); ask for
  consent to use the coordinates and attribute text under ODbL.
- Wiki pages read: Tag:tourism=artwork, Key:artist_name.

## Wiki entry
```
===Vetřelci a volavky – výtvarné umění ve veřejném prostoru 1945–1989===
* dataset: mapa děl projektu Vetřelci a volavky
* gestor: [https://vetrelciavolavky.cz/ Vetřelci a volavky (Pavel Karous)]
* licence: neuvedena, nutné vyjednat souhlas
* datové primitivy: body
* odkaz: https://vetrelciavolavky.cz/mapa ; https://vetrelciavolavky.cz/kml
* navržený tag {{tag|tourism|artwork}} + {{tag|artwork_type|sculpture}}, {{tag|artist_name}}, {{tag|start_date}}, {{tag|ref:vetrelciavolavky|<slug>}}
* poznámka: z 2 689 děl v ČR nemá 945 v okolí 75 m žádný objekt tourism=artwork/historic=memorial/amenity=fountain a u spárovaných v OSM většinou chybí autor a rok
```
