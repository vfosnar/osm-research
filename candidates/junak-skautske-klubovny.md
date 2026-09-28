# Junák – český skaut: map of scout troop meeting places (klubovny)

| Field | Value |
|---|---|
| publisher | Junák – český skaut, z. s. (kancelar@skaut.cz, from the site footer) |
| url | https://www.skaut.cz/mapa/ (JavaScript `sections[...] = [lat, lon, water, post_id]` and `units.push([...])` in the page HTML); per place: https://www.skaut.cz/oddil/&lt;post_id&gt;/ and `POST https://www.skaut.cz/wp-admin/admin-ajax.php action=wpj_load_infowindow` |
| format | arrays embedded in HTML (WordPress page with a Google map); address and troop details as HTML per place |
| coords | yes (WGS84, all 592 places) |
| records | 592 meeting places (2026-09-28), 55 of them flagged as water scouting; 1,192 troop/unit entries (age range, boys/girls/mixed); each place page has the address, troop names, meeting day and time |
| osm_tags | `club=scout` (approved, Tag:club=scout: "meeting place of a local scout group", node or area) + `name`, `operator=Junák – český skaut`; the water-scouting flag has no established tag, keep it in `description` |
| osm_count_cz | taginfo 2026-09-28: club=scout 78 (51 nodes, 27 ways), scout=yes 21 |
| license | none stated ("© 2026 – Junák – český skaut, z. s." in the footer only) |
| license_url | – |
| license_status | unclear |
| update_freq | live (troop leaders maintain their entries; the page is generated from the member system) |
| impact | 3 |
| sync_fit | Sync once consent exists (points, stable place id `post_id` as `ref:skaut`, one tag class club=scout) |
| verified | yes |

## Try it
- **Map preview:** none, licence unclear.
- **Browser:** https://www.skaut.cz/mapa/ (filter by age and boys/girls); a place page, for example
  https://www.skaut.cz/oddil/27659/ (Štefánikova 494, Újezd u Brna, troop "Zubři", boys 8–10, Tuesday 16:30–18:00).
- **Extract (tested 2026-09-28, 592 places):**
  `curl -s https://www.skaut.cz/mapa/ | grep -o 'sections\[[0-9]*\] = \[[^]]*\]'` gives
  `sections[27965] = [49.105515833333,16.765300833333,0,27659]` = latitude, longitude, water flag, place id.
- **QGIS:** turn the extract into CSV (`lat,lon,water,post_id`) and load with *Layer → Add Layer → Add
  Delimited Text Layer*, X = `lon`, Y = `lat`, EPSG:4326.

## Notes
- **What it adds:** the clubroom (klubovna) is where children go every week; Junák is the largest
  children's organisation in Czechia. Neither ZABAGED nor any government register has scout clubrooms,
  and nothing Junák-related is on Cs:Česko/freemap, Cs:Zdroje_v_jednani or in Sync's config.toml.
- **Gap, measured (Postpass 2026-09-28, CZ bbox, 150 m radius):** of 592 places, **77** have an OSM object
  tagged club=scout or named "skaut"/"Junák" nearby; 30 more have some other club, community_centre or
  "klubovna" object nearby; **485** have nothing.
- **Caveats:** coordinates were entered by troop leaders; a place can host several troops (one OSM node per
  place, troop names in `description` or separate nodes as the wiki suggests for shared venues). Some places
  are rented rooms inside a school or parish house. The page lists only troops that opted into the
  recruitment map, so it is not the full list of Junák units (about 1,192 unit rows here). Meeting times
  are per troop and change each school year; do not import them as `opening_hours`.
- **Contact:** Junák – český skaut, ústředí, kancelar@skaut.cz. Ask for consent to use the place list
  (coordinates, address, troop name) under ODbL, ideally as a JSON export with the `post_id`.
- Wiki pages read: Tag:club=scout.

## Wiki entry
```
===Junák – český skaut: mapa skautských oddílů===
* dataset: Mapa oddílů (místa schůzek / klubovny)
* gestor: [https://www.skaut.cz/ Junák – český skaut, z. s.]
* licence: neuvedena, nutno vyjednat (kancelar@skaut.cz)
* datové primitivy: body
* odkaz: https://www.skaut.cz/mapa/
* navržený tag {{tag|club|scout}}, {{tag|operator|Junák – český skaut}}
* poznámka: 592 míst schůzek skautských oddílů se souřadnicemi; u 485 z nich není v okruhu 150 m v OSM nic, club=scout je v ČR jen 78×
```
