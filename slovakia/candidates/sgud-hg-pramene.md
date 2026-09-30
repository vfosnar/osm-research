# Hydrogeological map 1:50,000 – springs, wells and karst points (ŠGÚDŠ "HG objekty")

| Field | Value |
|---|---|
| publisher | Štátny geologický ústav Dionýza Štúra (ŠGÚDŠ) |
| url | ArcGIS REST: `https://ags.geology.sk/arcgis/rest/services/WebServices/HG50/MapServer/0` ("HG objekty, vrty, pramene, krasové javy"; query `/query?where=1%3D1&outFields=*&outSR=4326&f=json&orderByFields=objectid&resultOffset=N&resultRecordCount=1000`); WFS: `https://ags.geology.sk/arcgis/services/WebServices/HG50/MapServer/WFSServer?request=GetCapabilities&service=WFS` (feature type `WebServices_HG50:HG_objekty__vrty__pramene__krasové_javy`); catalogue https://data.gov.sk/set/2367dbf95ebe323e94ab581ffd3ba82a , metadata https://rpi.gov.sk/metadata/d58d10d2-9363-489c-901f-8dfdbaf9683e |
| format | ArcGIS REST JSON/GeoJSON, WFS, WMS |
| coords | yes (points) |
| records | 29,462 points in 35 hydrogeological map regions (downloaded 30 Sep 2026): 19,151 groundwater outflows (16,602 `prameň`, 1,059 spring lines, 737 springs used for water supply, 249 supply + monitored, 241 yield-monitored, 115 spring groups, 64 mineral, 40 carbonated "kyselka", 22 sulphurous), 8,885 boreholes, 878 artificial objects (354 dug wells used for water supply, 235 river gauging stations, 135 rain gauges), 548 karst points (227 sinkholes, 210 caves, 73 ponors, 31 abysses). 18,584 springs carry a yield `q_p` in l/s |
| osm_tags | spring: `natural=spring` (+ `water_characteristic=mineral` for mineral springs, as the SAŽP mineral-spring import did); karst: `natural=cave_entrance`, `natural=sinkhole`; dug well: `man_made=water_well`. There is no established key for spring yield; `ref` stays empty (see notes). Checked against Tag:natural=spring (wiki, raw, 30 Sep 2026) |
| osm_count_sk | `natural=spring` 12,125; `natural=cave_entrance` 2,609; `natural=sinkhole` 10,923 (taginfo, data until 29 Sep 2026). Match against all OSM springs/wells/drinking water in the SK bbox (Postpass, 30 Sep 2026): only 1,669 of the 19,151 outflows have an OSM spring or water point within 100 m (1,077 within 50 m). Coverage differs by region: Veľká Fatra east 831 of 2,331 matched, Spišsko-gemerské rudohorie north 103 of 3,253, Čergov 34 of 1,620, Žiar 25 of 1,214 |
| license | CC BY 4.0 for author's work, database and sui generis right (national catalogue terms of use); service note "copyright ŠGÚDŠ" |
| license_url | https://data.gov.sk/set/2367dbf95ebe323e94ab581ffd3ba82a ; https://creativecommons.org/licenses/by/4.0/ |
| license_status | needs_waiver |
| update_freq | static map product (regional maps compiled over decades); no update cycle stated |
| impact | 3 |
| sync_fit | MapRoulette (no stable national ID, map-scale positions and unknown current state; a mapper confirms each spring with DMR 5.0 and the stream network) |
| verified | yes |

## Try it

- **Map preview:** [../samples/sgud-hg-pramene.geojson](../samples/sgud-hg-pramene.geojson) has the 1,067 springs in the eastern Veľká Fatra (bbox 19.10–19.26 E, 48.92–49.05 N), with yield and use. Even in this well-mapped range, `osm_spring_or_water_100m` is false for 659 of them.
- **QGIS:** *Layer → Add Layer → Add WFS Layer…*, new connection `https://ags.geology.sk/arcgis/services/WebServices/HG50/MapServer/WFSServer`, add `HG_objekty__vrty__pramene__krasové_javy`, filter `"bod_typ" = 'Vývery podzemnej vody'`. Or *ArcGIS REST Server* with `https://ags.geology.sk/arcgis/rest/services/WebServices/HG50/MapServer`. Both answered on 30 Sep 2026.
- **Web:** ŠGÚDŠ map portal https://apl.geology.sk/mapportal/

## Notes

- **Why it matters.** Springs are one of the most used features on Slovak hiking maps (Freemap renders them prominently, and the `osm_sk` list has many threads about spring mapping, `drinking_water` and `refitted`). OSM already has 12,125 springs, largely surveyed by hand (3,256 carry exactly `source=survey, GPS`). This layer adds roughly 17,500 springs with no OSM point within 100 m, plus a yield value for nearly all of them, which tells a hiker whether a spring is worth the detour.
- **Positional quality.** For the 1,610 register springs that have an OSM `natural=spring` within 100 m, the distance is 18 m (25th percentile), 35 m (median), 63 m (75th percentile). The points are 1:50,000 map positions, good enough to send a mapper to the right valley, not for a blind import.
- **Currency.** The maps were compiled over several decades; some springs have dried up or been captured. That is why the route is MapRoulette and not Sync.
- **IDs.** `cislo_b` is the number on the map sheet (missing on 1,065 records) and is not unique nationally; only `objectid` is unique inside the service. Don't write a `ref`.
- **Other point types.** The 235 river gauging stations and 135 rain gauges duplicate SHMÚ networks (`shmu-meteo-stanice.md` covers the meteorological ones). The 8,885 boreholes are mostly exploration wells and have no place in OSM. The 210 caves and 31 abysses are few; OSM already has 2,609 cave entrances, 103 of the 541 karst points match within 100 m.
- **Known overlap.** Mineral springs: Martin Ždila imported the SAŽP mineral-spring list by hand between 2011 and 2015 (`import_ref=mp2002`, 704 objects: 387 springs, 258 wells, 45 drinking water, 9 hot springs; `osm_sk` thread "Fwd: min. pramene", `YVuOIWygMjk`). Leave the 126 springs typed as mineral, carbonated or sulphurous in this layer to that data.
- **ZBGIS overlap.** ZBGIS has `BH170 Prameň` (point, type by mineralisation, name) with the note "Údaj od správcu … Trieda nie je predmetom aktualizácie", so ZBGIS springs are taken from a data holder and not updated. OSM has consent for ZBGIS map services (known-sources), but ZBGIS has no yield and no water-supply use. Comparing ZBGIS springs with this layer would show whether they come from the same maps; the ZBGIS WMS was unreachable from here on 30 Sep 2026.
- Contact: ŠGÚDŠ, oddelenie hydrogeológie / Geofond, Mlynská dolina 1, Bratislava, https://www.geology.sk/

## Wiki entry

```
=== Pramene z hydrogeologických máp 1 : 50 000 (ŠGÚDŠ) ===
* dataset: Hydrogeologická mapa SR M 1:50 000 – HG objekty
* správca: [https://www.geology.sk/ Štátny geologický ústav Dionýza Štúra]
* licencia: CC BY 4.0 [https://data.gov.sk/set/2367dbf95ebe323e94ab581ffd3ba82a]
* dátové primitívy: body
* odkaz: https://ags.geology.sk/arcgis/services/WebServices/HG50/MapServer/WFSServer?request=GetCapabilities&service=WFS
* navrhované značky: {{tag|natural|spring}}, {{tag|natural|cave_entrance}}, {{tag|natural|sinkhole}}, {{tag|man_made|water_well}}
* poznámka: 19 151 prameňov s výdatnosťou v 35 regiónoch, z ktorých asi 17 500 nemá v OSM do 100 m žiadny prameň; polohy sú v mierke 1 : 50 000, vhodné pre MapRoulette.
```
