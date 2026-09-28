# IDS JMK GTFS – stop attributes for Brno (wheelchair, gtfs:stop_id, platform codes)

| Field | Value |
|---|---|
| publisher | KORDIS JMK, a.s. (feed operator), published on data.Brno (Statutární město Brno) |
| url | https://kordis-jmk.cz/gtfs/gtfs.zip (9.3 MB, stops.txt dated 2026-09-25); catalogue https://data.brno.cz/datasets/379d2e9a7907460c8ca7fda1f3e84328 |
| format | GTFS ZIP; `stops.txt` columns stop_id, stop_name, stop_lat, stop_lon, zone_id, location_type, parent_station, wheelchair_boarding, platform_code |
| coords | yes (WGS84, platform level) |
| records | 10,949 rows: 7,689 platforms (location_type 0) with stop_id U&lt;node&gt;Z&lt;n&gt; (U1146Z11), 3,260 parent stations (U&lt;node&gt;N&lt;n&gt;). Brno bbox 16.48,49.13–16.72,49.28: 1,567 platforms, wheelchair_boarding 1 = 894, 2 = 673; platform_code filled on 510 platforms network-wide |
| osm_tags | on the existing public_transport=platform / highway=bus_stop / railway=tram_stop: wheelchair=yes (1) / no (2), gtfs:stop_id:CZ-IDSJMK=&lt;stop_id&gt;, local_ref=&lt;platform_code&gt; |
| osm_count_cz | gtfs:stop_id:CZ-IDSJMK 2 objects, gtfs:route_id:CZ-IDSJMK 48 relations (taginfo 2026-09-27). Brno bbox: 2,053 OSM platforms/stops, 165 with wheelchair, 163 with local_ref (local match against the 2026-09-27 Czechia extract) |
| license | explicit consent for use in OSM from 2024-11-18 (recorded on Cs:Česko/freemap, request closed on Cs:Zdroje_v_jednani) |
| license_url | https://wiki.openstreetmap.org/wiki/Cs:%C4%8Cesko/freemap |
| license_status | ok |
| update_freq | daily (files regenerated around 03:50) |
| impact | 3 |
| sync_fit | Sync (attribute enrichment of existing platforms; stable ref gtfs:stop_id:CZ-IDSJMK, wheelchair 1:1) |
| verified | yes |

## Try it

- **Map preview:** [samples/known-idsjmk-gtfs-atributy-zastavek.geojson](../samples/known-idsjmk-gtfs-atributy-zastavek.geojson): the 1,567 IDS JMK platforms in Brno, with `wheelchair` mapped, `gtfs:stop_id`, `platform_code`, `osm_platform_within_30m`, the nearest `osm_id` and its current `osm_wheelchair` (empty = untagged).
- **QGIS:** download `https://kordis-jmk.cz/gtfs/gtfs.zip`. QGIS ≥ 3.30 (GDAL GTFS driver): *Layer → Add Layer → Add Vector Layer…* → *File* → `gtfs.zip`, pick the `stops` layer. Older QGIS: unzip `stops.txt`, then *Layer → Add Layer → Add Delimited Text Layer…*: CSV (comma), UTF-8, X field `stop_lon`, Y field `stop_lat`, CRS EPSG:4326; filter `"location_type" = 0`.

## Notes
- Known (listed on Cs:Česko/freemap as "Jízdní řád IDS JMK GTFS", consent since 2024-11-18) — adds: nobody has used its stop attributes yet. Only 2 OSM objects carry `gtfs:stop_id:CZ-IDSJMK`, although CZ-IDSJMK is already the registered feed code on the wiki "List of GTFS feeds" and 48 route relations use `gtfs:route_id:CZ-IDSJMK`.
- **Gap in Brno (local match against the 2026-09-27 Czechia extract, nearest OSM stop/platform within 30 m):** 1,488 of 1,567 feed platforms have an OSM counterpart; 44 are more than 50 m away. Of the 1,488, **1,368 have no wheelchair tag** while the feed has a value (800 → yes, 568 → no). OSM and the feed agree on 77 and disagree on 43 (33 OSM yes vs feed 2, 7 no vs 1, 3 limited vs 1).
- **platform_code:** of 106 matched Brno platforms with a platform_code, 83 have OSM local_ref and 61 agree. Nearest-neighbour matching at big interchanges picks the wrong platform sometimes, so match by ID after the first pass.
- **Regional values are a default, not data:** outside Brno, 6,108 of 6,120 platforms have wheelchair_boarding=2, and 205 of the matched ones are wheelchair=yes in OSM. Use wheelchair only for Brno city (DPMB) stops, or only value 1, until KORDIS confirms what 2 means for regional stops.
- **Stable ID:** stop_id follows the KORDIS node/platform scheme (U1146 = Hlavní nádraží, Z11 = platform), the same pattern PID uses for ref:PID. That makes `gtfs:stop_id:CZ-IDSJMK` a good Sync ref and would also let the 1,180 JMK feed platforms with no OSM stop within 50 m be checked against jizdni-rady-osm.
- **Wiki pages read:** Key:wheelchair (no default; yes/limited/no), Key:local_ref, Tag:public_transport=platform, Key:gtfs:stop_id (approved; "the exact value of the stop_id column", needs the feed-code suffix), List of GTFS feeds (Czechia: only CZ-IDSJMK).
- **Contact:** KORDIS JMK, a.s. (phone +420 543 174 317 listed on mapa.idsjmk.cz) about the meaning of wheelchair_boarding=2 on regional stops.

## Wiki entry
```
===IDS JMK GTFS – atributy zastávek (Brno)===
* dataset: Jízdní řád IDS JMK ve formátu GTFS, soubor stops.txt
* gestor: [https://data.brno.cz/datasets/379d2e9a7907460c8ca7fda1f3e84328 KORDIS JMK, a.s. / data.Brno]
* licence: výslovný souhlas s použitím v OSM (od 18. 11. 2024) [https://wiki.openstreetmap.org/w/images/5/5f/OSMCZ_%C5%BE%C3%A1dost_o_data.pdf]
* datové primitivy: body
* odkaz: https://kordis-jmk.cz/gtfs/gtfs.zip
* navržený tag {{tag|gtfs:stop_id:CZ-IDSJMK|<stop_id>}}, {{tag|wheelchair|yes}} / {{tag|wheelchair|no}}, {{tag|local_ref|<platform_code>}}
* poznámka: v Brně 1 368 z 1 488 nástupišť v OSM nemá wheelchair, přestože GTFS hodnotu má; gtfs:stop_id:CZ-IDSJMK je v OSM jen na 2 objektech (mimo Brno je wheelchair_boarding=2 výchozí hodnota, nepoužívat)
```
