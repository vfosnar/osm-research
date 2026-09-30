# Road structures from the SSC road databank: bridges, underpass clearances, tunnels, level crossings

| Field | Value |
|---|---|
| publisher | Slovenská správa ciest (SSC), Cestná databanka (CDB), IČO 00003328 |
| url | ArcGIS REST: `https://ismcs.cdb.sk/inspire/rest/services/FREE/WFS_CestneObjekty/MapServer` (layers 1 `DilatacnyCelokMosta`, 2 `Most`, 3 `Podjazd`, 4 `Tunel`, 5 `ZeleznicnePriecestie`, 6 `Priepust`; query with `/<layer>/query?where=1%3D1&outFields=*&outSR=4326&f=geojson`); WFS 2.0: `https://ismcs.cdb.sk/inspire/services/FREE/WFS_CestneObjekty/MapServer/WFSServer`; CSV reports without geometry: `https://www.cdb.sk/files/documents/cestna-databanka/vystupy-cdb/2026/csv/sr_co_report_mostypk_2026-01-01.csv`, `…/sr_co_podjazd_2026-01-01.csv`, `…/sr_co_tunel_2026-01-01.csv`, `…/sr_co_zeleznicnepriecestie_2026-01-01.csv` |
| format | ArcGIS REST GeoJSON (lines), WFS 2.0 GML, CSV (cp1250, `;`) |
| coords | yes (line geometry of each structure along the road axis) |
| records | bridges 8,815 (8,880 bridge segments); underpasses 1,276 (968 under a road bridge, 201 under a railway bridge, 47 footbridges, 29 pipelines, 13 ecoducts); tunnels 25; level crossings 590 (fetched 30 Sep 2026, state 1 Jan 2026) |
| osm_tags | underpasses: `maxheight:physical=<minVyska>` on the road way under the structure; bridges: `bridge:ref=<SSC bridge ID>`, `start_date=<rokPostavenia>`; level crossings: `ref=<ŽSR ID>` (tag choice for the ref key to be agreed), `crossing:barrier`, `crossing:light`; tunnels: `tunnel:name`, `maxheight:physical` |
| osm_count_sk | `maxheight:physical` 4, `bridge:ref` 737, `bridge:name` 147, `railway=level_crossing` 5,409 (taginfo, 29 Sep 2026). Postpass sample (30 Sep 2026): 104 of 300 road/railway underpasses have a `highway` way tagged `maxheight` within 30 m; 19 of 300 SSC bridges have an OSM bridge with `bridge:name`/`bridge:ref` within 25 m; 578 of 590 level crossings have an OSM `railway=level_crossing` within 40 m, 562 with `crossing:barrier` |
| license | CC BY 4.0 ("Autor: Slovenská správa ciest. Licencia: CC-BY 4.0" on the CDB map-services page; the national catalogue lists the same for each CSV) |
| license_url | https://www.cdb.sk/sk/poskytovanie-udajov/poskytovanie-vektorovych-udajov-CTEPK/mapove-sluzby.alej |
| license_status | needs_waiver |
| update_freq | yearly (state on 1 January) |
| impact | 3 |
| sync_fit | underpass clearances: MapRoulette (the value belongs on the road way under the structure, which a human has to pick); bridges: iD fork harness (line geometry with a stable ID `identifikacneCisloMosta`, matched onto existing `bridge=*` ways for attributes, never imported as geometry); level crossings: Sync attribute enrichment (points, ŽSR ID as ref, existing OSM nodes already cover 98 %) |
| verified | yes |

## Try it

- **Map preview:** [../samples/transport-ssc-cestne-objekty.geojson](../samples/transport-ssc-cestne-objekty.geojson) has every structure around Žilina (bbox 18.55–19.10 E, 48.95–49.30 N): 468 bridges, 102 underpasses with clearance, 16 level crossings, 10 tunnel tubes. The `layer` property says which is which.
- **QGIS:** *Layer → Data Source Manager → ArcGIS REST Server → New*, URL `https://ismcs.cdb.sk/inspire/rest/services/FREE/WFS_CestneObjekty/MapServer`, then add `Podjazd` or `Most`. Alternatively *Add WFS Layer* with `https://ismcs.cdb.sk/inspire/services/FREE/WFS_CestneObjekty/MapServer/WFSServer`. Both were tested and return features.
- **Web:** CDB map viewer https://ismcs.cdb.sk/portal/mapviewer

## Notes

- **Underpass clearance (most useful part).** `Podjazd.minVyska` is the measured minimum clearance under a structure. Only 4 objects in all of Slovakia carry `maxheight:physical` (taginfo). In the Postpass sample, about a third of the underpasses already have a road with `maxheight` nearby. That `maxheight` may be the signed legal limit or may sit on the wrong way (the road on the bridge instead of the road under it), so a human should check each task. That is about 750 underpasses to review, which matters for lorry and camper routing. The wiki (Key:maxheight:physical) defines it as the physical height of the passage. The value is not the signed limit and must not go into `maxheight`.
- **Bridges.** Each bridge has a unique `identifikacneCisloMosta` (`M1` … `M10102`, 8,815 distinct values). There is also an evidenčné číslo (`D4-031.1`, `50-071`, often just `001` per road) plus a descriptive name like "Most cez potok Pereň v meste Humenné", year built, span length, widths, material and construction type. OSM `bridge:ref` already has both forms (`M158`, `M1701`, `D3-071`, `R1-114` among the top values). The community should agree on one form; the M-number is unique, so it is the better key. The `nazovMosta` strings are descriptions, not names, so don't put them in `bridge:name`. The load capacities in `DilatacnyCelokMosta` (`zatazitelnostNormalnaText` and others) are design capacities, not signed restrictions, so they must not become `maxweight`. 242 of 300 sampled bridges already have an OSM `bridge=*` way within 25 m; the other ~19 % are mostly small bridges on minor roads where the way isn't split. Those make MapRoulette pointers, not geometry.
- **Level crossings.** 590 crossings of roads I.–III. class. 532 of them carry the ŽSR crossing ID `JIC_ZSR` (such as `SP1792`), and each has the protection type: 272 lights + barriers, 161 lights, 31 barriers, 83 unprotected, 39 siding-unprotected. OSM already has nearly all of them with `crossing:barrier`, so the only addition is the ŽSR ID. For a ref key, `railway:ref` is taken by stations, so this needs a community decision. A TomTom MapRoulette challenge on missing level crossings is already known (known-sources).
- **Tunnels.** 25 tunnel tubes with name, category (`kategoriaTunela` A–D, relevant to `hazmat`) and clearance. All are motorway or I-class tunnels, most likely mapped already; attributes only.
- **ZBGIS overlap:** the ZBGIS object catalogue has `AQ040 Most` (with span length LOB and passable width, but no SSC ID, year or clearance) and `AQ063 Železničné priecestie`. Underpass clearance (`Podjazd`) and the SSC/ŽSR identifiers are not in ZBGIS.
- Licence: CC BY 4.0, so a waiver is needed. SSC gave a consent for road refs in 2007 (known-sources). One request could cover both CDB files (`transport-ssc-kilometrovniky.md`).
- Contact: Slovenská správa ciest, Cestná databanka, https://www.cdb.sk/

## Wiki entry

```
=== Cestné objekty zo SSC Cestnej databanky (mosty, podjazdy, tunely, priecestia) ===
* dataset: Údaje centrálnej technickej evidencie ciest – WFS cestných objektov
* správca: [https://www.cdb.sk/ Slovenská správa ciest – Cestná databanka]
* licencia: CC BY 4.0 [https://www.cdb.sk/sk/poskytovanie-udajov/poskytovanie-vektorovych-udajov-CTEPK/mapove-sluzby.alej]
* dátové primitívy: línie
* odkaz: https://ismcs.cdb.sk/inspire/services/FREE/WFS_CestneObjekty/MapServer/WFSServer
* navrhované značky: {{tag|maxheight:physical|<minVyska>}}, {{tag|bridge:ref|<identifikačné číslo mosta>}}, {{tag|start_date|<rok postavenia>}}, {{tag|crossing:barrier}}
* poznámka: 1 276 podjazdov s nameranou podjazdnou výškou (v OSM má maxheight:physical len 4 objekty) a 8 815 mostov s jednoznačným ID SSC.
```
