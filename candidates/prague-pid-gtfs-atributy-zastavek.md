# PID GTFS – stop attributes (wheelchair_boarding, platform_code, pathways/levels)

| Field | Value |
|---|---|
| publisher | Regionální organizátor pražské integrované dopravy (ROPID), IČO 60437359 |
| url | https://data.pid.cz/PID_GTFS.zip (GTFS, daily); also https://data.pid.cz/stops/json/stops.json (stop groups with wheelchairAccess and lines); catalogue https://pid.cz/opendata/ |
| format | GTFS ZIP (stops.txt with extra columns asw_node_id, asw_stop_id, zone_region_type; plus pathways.txt, levels.txt); JSON |
| coords | yes |
| records | stops.txt 20,166 rows (18,689 location_type=0; 260 stations, 338 entrances, 629 generic nodes, 250 boarding areas); pathways.txt 1,532; levels.txt 170. stops.json: 8,535 groups / 17,212 stops |
| osm_tags | public_transport=platform (+ highway=bus_stop / railway=tram_stop), wheelchair=yes\|no\|limited, local_ref=&lt;platform_code&gt;, ref:PID=&lt;stop_id&gt; |
| osm_count_cz | ref:PID 16,542 (taginfo 2026-09-26); of those, wheelchair on 4,681 and local_ref on 13,924 |
| license | CC BY 4.0 (stated on pid.cz/opendata; NKOD: database as copyrighted work = CC BY, no sui generis right) |
| license_url | https://pid.cz/opendata/ ; https://creativecommons.org/licenses/by/4.0/ |
| license_status | needs_waiver |
| update_freq | daily |
| impact | 2 |
| sync_fit | Sync (points, stable ref:PID, category → platform 1:1) |
| verified | yes |

## Try it

- **Map preview:** [samples/prague-pid-gtfs-atributy-zastavek.geojson](../samples/prague-pid-gtfs-atributy-zastavek.geojson): the 1,132 stop points (`location_type=0`) of `stops.txt` in central Prague (bbox 14.38,50.03–14.50,50.10), with `ref:PID`, `local_ref` and `wheelchair` already mapped (392 yes, 119 no).
- **QGIS:** download `https://data.pid.cz/PID_GTFS.zip` (51 MB) and unzip `stops.txt`, then *Layer → Add Layer → Add Delimited Text Layer…*: file `stops.txt`, format CSV (comma), encoding UTF-8, X field `stop_lon`, Y field `stop_lat`, geometry CRS EPSG:4326.

## Notes
- Stop presence is already covered by vfosnar/jizdni-rady-osm (CIS JŘ). Metro entrances with ref:PID are already in osmcz/sync. This candidate is only about **attributes** on stops that are already mapped.
- **Match (Postpass, Prague + Central Bohemia bbox, 2026-09-27):** 16,110 OSM objects have ref:PID. 14,715 of them match a current GTFS stop_id (format such as U135Z2P). About 1,395 OSM ref:PID values are not in today's GTFS (stale or cancelled stops), which is useful for cleanup.
- **wheelchair:** most accessibility data is already in OSM. There are 3,330 no/2 and 451 yes/1 agreements. The gap:
  - 1,212 OSM stops have no wheelchair tag while GTFS has a value (1,039 not accessible, 173 accessible).
  - About 100 disagree (231 OSM yes vs GTFS 0 "unknown" is not a conflict).
  - 9,270 stops are unknown in both.
- **local_ref vs platform_code:** 1,728 matched OSM stops lack local_ref while GTFS has platform_code, and 216 disagree.
- **pathways.txt/levels.txt:** these give elevator, escalator and stair links (pathway_mode 4 = escalator, 5 = elevator) with signposted_as for metro and train stations. They could support highway=elevator / conveying checks, but that needs manual work.
- Impact is 2 because most attributes were apparently imported earlier. The remaining work is sync and maintenance, which Sync would do well, since ref:PID is stable.
- **Wiki pages read:** Tag:public_transport=platform and Key:local_ref (local_ref = "number or letter of the stop, platform"), plus Key:wheelchair (no default value) and Key:ref:PID ("Reference number in the Prague Integrated Transport system"). The GTFS mapping is 1 → yes, 2 → no, 0 → don't set.
- **Licence:** CC BY 4.0, so an explicit OSM waiver from ROPID is needed. It is not listed on Cs:Česko/freemap (only IDS JMK GTFS is). The ROPID open data contact is on pid.cz/opendata.

## Wiki entry
```
===PID GTFS – atributy zastávek===
* dataset: Jízdní řády PID (GTFS) – stops.txt, pathways.txt
* gestor: [https://pid.cz/opendata/ ROPID]
* licence: CC BY 4.0 [https://creativecommons.org/licenses/by/4.0/]
* datové primitivy: body
* odkaz: https://data.pid.cz/PID_GTFS.zip
* navržený tag {{tag|wheelchair|yes/no}}, {{tag|local_ref|<platform_code>}}, {{tag|ref:PID|<stop_id>}}
* poznámka: ref:PID už má 16,5 tis. objektů; chybí wheelchair u ~1 200 a local_ref u ~1 700 zastávek, ~1 400 ref:PID je zastaralých
```
