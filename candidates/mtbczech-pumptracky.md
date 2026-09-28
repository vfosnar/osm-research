# MTBczech.cz – pumptracky (pump tracks) of Czechia

| Field | Value |
|---|---|
| publisher | project "Trailcentra a bikeparky České republiky" (www.mtbczech.cz), contact info@mtbczech.cz |
| url | list: https://www.mtbczech.cz/pumptracky ; detail pages https://www.mtbczech.cz/pumptrack/&lt;slug&gt; (146 links on the list page) |
| format | HTML only. Each detail page has `var lat=…; var lon=…;` (WGS84) plus Lokalita, GPS (DMS), Kraj, Web, Další info (surface) |
| coords | yes (145 of 146; Pumptrack-Karlovy-Vary-Bohatice has none) |
| records | 146 pump tracks, 145 with coordinates; surface: 83 dirt (hliněný), 51 asphalt, 8 modular, 2 mixed, 1 under construction |
| osm_tags | site: leisure=pitch + sport=cycling (or bmx/skateboard) + cycling=pump_track + surface; the ridden line: leisure=track + cycling=pump_track (wiki Tag:cycling=pump_track) |
| osm_count_cz | cycling=pump_track 151, cycling=pumptrack 3, sport=pumptrack 11, leisure=pumptrack 1 (taginfo Geofabrik CZ, 2026-09-27). Local match against the 2026-09-27 Czechia extract (Postpass unavailable): 336 OSM nodes/ways with a pump-track tag or name; of the 145 listed tracks 60 matched, 24 only a bike/skate feature, 61 nothing (OSM API check: 64 / 24 / 57) |
| license | none stated; footer "Copyright © 2019, Trailcentra a bikeparky České republiky" |
| license_url | none |
| license_status | unclear |
| update_freq | irregular (entries added as tracks open) |
| impact | 2 |
| sync_fit | MapRoulette (no stable id for the site; track line drawn from imagery) |
| verified | yes |

## Try it
- **Map preview:** none (licence unclear). The publisher's own map is the list page https://www.mtbczech.cz/pumptracky.
- **QGIS:** there is no machine-readable endpoint. Scrape the coordinates into CSV, then load it with
  *Layer → Add Layer → Add Delimited Text Layer*, delimiter `;`, X field `lon`, Y field `lat`, CRS EPSG:4326:
  ```
  curl -s https://www.mtbczech.cz/pumptracky | grep -o 'https://www.mtbczech.cz/pumptrack/[^"]*' | sort -u |
  while read u; do curl -s "$u" | tr -d '\n' | sed -n "s|.*var lat=\([0-9.]*\);.*var lon=\([0-9.]*\);.*|$u;\1;\2|p"; done > pumptracky.csv
  ```
  Add the header line `url;lat;lon` before loading. (Tested 2026-09-27: 145 rows.)

## Notes
- **Gap analysis (2026-09-27/28):** Postpass returned 503 for the whole session, so each of the 145 points was
  checked against the OSM API (`/api/0.6/map`, bbox ±~330 m around the point). A track counts as mapped when any
  node or way within 300 m has cycling=pump_track/pumptrack, "pump" in sport/leisure, or "pump" in its name.
  - 64 are in OSM. Many have no pump-track tag, only leisure=track + sport=cycling with "pumptrack" in the name
    (only 20 of the 64 have cycling=pump_track within 300 m).
  - 24 have only a generic bike/BMX/skate feature (sport=bmx/cycling/mtb/skateboard) within 200 m. This may be an
    untagged pump track or a nearby skatepark.
  - **57 have nothing** within 300 m. They are in every region: Jihomoravský 9, Středočeský 8, Jihočeský 7,
    Liberecký 6, Zlínský 5, Královéhradecký 5, Praha 4 and 13 more. Examples: Pumptrack Brno Lesná (Dusíkova
    795/7, asphalt), Pumptrack Brumov-Bylnice, Pumptrack Blatná, Pumptrack Boskovice (Sportpark), Pumpline Nad
    Voleškou in Kladno, Pumptrack Chrastava. 14 of the 57 are asphalt tracks, which are permanent public sports
    facilities (usually municipal).
- **Cross-check against the national extract (local match against the 2026-09-27 Czechia extract, Postpass
  unavailable; same rule and radii):** 60 in OSM (20 of them with cycling=pump_track within 300 m; median
  distance 11 m), 24 with only a bike/skate feature, 61 with nothing (Jihomoravský 10, Středočeský 8,
  Jihočeský 7, Zlínský 6, Liberecký 6, Královéhradecký 5, Praha 4 and 15 more; 17 of the 61 are asphalt).
  140 of 145 tracks get the same status as in the OSM API check. The 5 that differ lose their match because the
  matching OSM way (Pumptrack Drnovice, Hošťálkovice, Vysočina Arena among them) carries "pumptrack" only in its
  name and none of the keys the extract was filtered on, so it is not in the extract; the OSM API figure
  (57 missing) sees all objects and remains the headline.
- The earlier note "OSM has only ~12 pump tracks" was wrong. It counted sport=pumptrack and leisure=pumptrack.
  The documented tag is cycling=pump_track (151 objects in CZ, often several ways per site).
- The community could also use the list to fix tagging: 44 of the 64 matched tracks lack cycling=pump_track.
- **Quality:** coordinates are hand-placed by the site editors. For the 64 matched tracks the median distance to the OSM feature is 9 m (58 within 50 m, 63 within 100 m).
  There is no stable ID; the URL slug (Pumptrack-Blatna) is the only key. The surface is free text in "Další info".
- **Licence:** there is no open licence, and the site is a hand-compiled list. Treat it as a checklist for
  surveying/aerial-imagery mapping, not an import, unless the operator gives explicit OSM consent. Ask
  info@mtbczech.cz. For single tracks, the municipality that built them (the "Web" field often links to it) is
  the primary source.
- The same site also lists trail centres and bike parks (https://www.mtbczech.cz/trailcentra,
  https://www.mtbczech.cz/bikeparky; 55 markers on the list-page map). These were not evaluated.
- Checked and not known: none of Cs:Česko/freemap, Cs:Zdroje_v_jednani or the Sync config.toml mention
  pumptracks or mtbczech (2026-09-27).
- Wiki pages read: Tag:cycling=pump_track (status in use; sport=pumptrack and leisure=pumptrack have no wiki page).

## Wiki entry
```
===MTBczech – pumptracky===
* dataset: Pumptracky (seznam na www.mtbczech.cz)
* gestor: [https://www.mtbczech.cz/ Trailcentra a bikeparky České republiky] (info@mtbczech.cz)
* licence: neuvedena (© 2019 Trailcentra a bikeparky ČR), nutno požádat o souhlas
* datové primitivy: body
* odkaz: https://www.mtbczech.cz/pumptracky
* navržený tag {{tag|leisure|pitch}} + {{tag|sport|cycling}} + {{tag|cycling|pump_track}} + {{tag|surface}}
* poznámka: ze 145 pumptracků s GPS jich 57 v OSM zcela chybí a 44 z 64 zmapovaných nemá {{tag|cycling|pump_track}}
```
