# PMDP Plzeň GTFS – stop accessibility (wheelchair_boarding on every platform)

| Field | Value |
|---|---|
| publisher | Plzeňské městské dopravní podniky, a.s. (PMDP), published by Statutární město Plzeň (IČO 00075370) in NKOD as "Jízdní řády PMDP"; secondary: Dopravní podnik města Olomouce, a.s. (DPMO) |
| url | PMDP https://jizdnirady.pmdp.cz/jr/gtfs (GTFS ZIP, served as application/octet-stream); NKOD record https://data.gov.cz/zdroj/datové-sady/00075370/a4d3e3f723eb8f364703e3de464f59c8 ; DPMO https://www.dpmo.cz/doc/dpmo-olomouc-cz.zip (page https://www.dpmo.cz/informace-pro-cestujici/jizdni-rady/jizdni-rady-gtfs/) |
| format | GTFS ZIP; `stops.txt` columns stop_id, stop_code, stop_name, stop_lat, stop_lon, zone_id, location_type, wheelchair_boarding, original_stop_id |
| coords | yes (WGS84, platform level) |
| records | PMDP 719 platforms (all location_type=0), wheelchair_boarding 1 = 494, 2 = 225, none blank; stop_code "&lt;number&gt;/&lt;platform&gt;" (54720/1). DPMO 373 platforms, wheelchair_boarding 1 = 263, blank = 110 |
| osm_tags | on the existing public_transport=platform / highway=bus_stop / railway=tram_stop: wheelchair=yes (1), wheelchair=no (2), nothing for 0/blank; gtfs:stop_id:CZ-PMDP=&lt;stop_id&gt; once the feed code is registered on "List of GTFS feeds" |
| osm_count_cz | public_transport=platform 68,045 (taginfo 2026-09-27). Plzeň bbox 13.2,49.65,13.55,49.82: 1,276 OSM platforms/stops, of them only 119 carry wheelchair (local match against the 2026-09-27 Czechia extract) |
| license | PMDP: NKOD terms "neobsahuje autorská díla", "není autorskoprávně chráněnou databází", "není chráněna zvláštním právem pořizovatele databáze" (NKOD maps this to CC0). DPMO: no licence stated on the download page |
| license_url | https://data.gov.cz/podmínky-užití/neobsahuje-autorská-díla/ ; https://data.gov.cz/podmínky-užití/není-chráněna-zvláštním-právem-pořizovatele-databáze/ |
| license_status | ok (PMDP); unclear (DPMO) |
| update_freq | with each timetable change (DPMO file "od 21.9.2026, aktualizace k 17.9.2026"); PMDP feed is generated live |
| impact | 3 |
| sync_fit | Sync (attribute enrichment of existing platforms; wheelchair 1:1; needs a stable stop_id check first) |
| verified | yes |

## Try it

- **Map preview:** [samples/pmdp-gtfs-pristupnost-zastavek.geojson](../samples/pmdp-gtfs-pristupnost-zastavek.geojson): the 713 PMDP platforms inside Plzeň and its suburbs (bbox 13.2,49.65–13.55,49.82), with `wheelchair` already mapped, `osm_platform_within_30m`, the nearest OSM `osm_id` and its current `osm_wheelchair` (empty = untagged). DPMO is not in the sample because its licence is unclear.
- **QGIS:** download `https://jizdnirady.pmdp.cz/jr/gtfs` and save it as `pmdp.zip` (0.9 MB). QGIS ≥ 3.30 (GDAL GTFS driver): *Layer → Add Layer → Add Vector Layer…* → *File* → `pmdp.zip`, pick the `stops` layer. Older QGIS: unzip `stops.txt`, then *Layer → Add Layer → Add Delimited Text Layer…*: CSV (comma), UTF-8, X field `stop_lon`, Y field `stop_lat`, CRS EPSG:4326; style by `wheelchair_boarding`.

## Notes
- **Gap (local match against the 2026-09-27 Czechia extract, nearest OSM highway=bus_stop / public_transport=platform / railway=tram_stop|platform within 30 m):**
  - PMDP: 680 of 713 platforms have an OSM counterpart within 30 m, 14 are more than 50 m away. Of the 680, **597 have no wheelchair tag** while the feed has a value (419 → yes, 178 → no). OSM and the feed agree on 59 and disagree on 22 (17 OSM yes vs feed 2, 4 limited vs 2, 2 no vs 1). The disagreements need a survey or a question to PMDP. Plzeň platforms have few tags overall: 149 local_ref and 12 ref:CIS_JR in the bbox.
  - DPMO Olomouc: 353 of 373 platforms matched within 30 m; **246 have no wheelchair tag** where the feed says 1 (accessible). OSM has wheelchair on only 5 matched platforms. The 110 blank values mean unknown and give nothing.
- **Why this adds to what exists:** jizdni-rady-osm (CIS JŘ) places stops but carries no accessibility. The PMDP feed is the only city feed outside PID and IDS JMK whose stops.txt is complete for wheelchair_boarding (no 0/blank), and its NKOD terms are CC0-equivalent, so no waiver is needed.
- **IDs:** `stop_id` is a small integer ("27") with an `original_stop_id` column; stability between releases was not tested (only one release fetched, 2026-09-28). `stop_code` "54720/1" looks like a PMDP stop number plus platform. It is not ref:CIS_JR: Nová Ves has stop_code 53190 in the feed and ref:CIS_JR=23656 in OSM (1 of 3 checked codes matched). The `/n` platform suffix agrees with OSM local_ref only partly, so don't import it as local_ref without a check against the physical signs.
- **Tags:** Key:wheelchair (no default; yes/limited/no) and Tag:public_transport=platform read on the wiki. Key:gtfs:stop_id (approved) wants a feed-code suffix from "List of GTFS feeds"; Czechia lists only CZ-IDSJMK there, so a CZ-PMDP code would need to be added first.
- **Contacts:** PMDP (agency_phone +420 378 037 485 in agency.txt, www.pmdp.cz) for the feed; for DPMO, ask Dopravní podnik města Olomouce, a.s. for a licence statement (the GTFS page has none).

## Wiki entry
```
===PMDP Plzeň – GTFS (bezbariérovost zastávek)===
* dataset: Jízdní řády PMDP (GTFS), soubor stops.txt
* gestor: [https://www.pmdp.cz/ Plzeňské městské dopravní podniky, a.s.] / [https://data.gov.cz/zdroj/datové-sady/00075370/a4d3e3f723eb8f364703e3de464f59c8 Statutární město Plzeň]
* licence: neobsahuje autorská díla, není chráněnou databází [https://data.gov.cz/podmínky-užití/neobsahuje-autorská-díla/]
* datové primitivy: body
* odkaz: https://jizdnirady.pmdp.cz/jr/gtfs
* navržený tag {{tag|wheelchair|yes}} / {{tag|wheelchair|no}} na existující {{tag|public_transport|platform}}, {{tag|gtfs:stop_id:CZ-PMDP|<stop_id>}}
* poznámka: 597 ze 680 nástupišť PMDP, která v OSM existují, nemá wheelchair, přestože GTFS hodnotu uvádí u všech 719 zastávek
```
