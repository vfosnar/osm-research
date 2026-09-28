# AI road detections: Meta MapWithAI Czechia export and Microsoft Road Detections (review layers)

| Field | Value |
|---|---|
| publisher | Meta (Facebook) Open Mapping / Rapid; Microsoft Bing Maps (github.com/microsoft/RoadDetections) |
| url | Meta: https://rapideditor.org/country_exports/CZ_mapwithai_road_data.gpkg.tar.gz (44 MB, Last-Modified 2020-01-09). Microsoft: https://usaminedroads.z19.web.core.windows.net/drops/2025.04.28/Eastern_Europe.zip (1.4 GB, TSV of country code + GeoJSON; filter rows starting `CZE`) |
| format | Meta: GeoPackage (EPSG:4326, fields way_fbid, highway_tag, wkt). Microsoft: zipped TSV, one GeoJSON LineString per row with WidthMeters |
| coords | yes (lines) |
| records | Meta: 251,530 lines predicted as missing from OSM (Rapid country table date 2019-12-30, imagery Maxar Premium) (residential 145,256; track 80,319; service 14,535; unclassified 6,406; path 3,709). Microsoft: 1,208,394 CZE lines, 194,771 km. These are all detected roads, not only the ones missing from OSM |
| osm_tags | highway=track / service / unclassified / residential after manual review; Meta's highway_tag guess is unreliable (25 of 76 unmatched forest lines in the sample are "residential") |
| osm_count_cz | highway=track 426,022 ways (Geofabrik taginfo CZ, 2026-09-28) |
| license | Meta: MIT (repository LICENSE.md), published for use in OSM through Rapid and the JOSM MapWithAI plugin. Microsoft: ODbL |
| license_url | https://github.com/facebookmicrosites/Open-Mapping-At-Facebook/blob/main/LICENSE.md ; https://github.com/microsoft/RoadDetections (README: "Open Data Commons Open Database License (ODbL)") |
| license_status | ok (Microsoft ODbL; Meta data is offered for OSM editing in Rapid, the practice documented on wiki page Rapid) |
| update_freq | Meta CZ export: one-off 2020-01. Microsoft: drops, latest 2025-04-28 |
| impact | 1 |
| verified | yes |

## Try it
- **Map preview:** [samples/meta-mapwithai-roads.geojson](../samples/meta-mapwithai-roads.geojson), Brdy
  (bbox 13.75,49.70,13.85,49.75): 76 Meta lines (13.8 km) and 8 Microsoft lines (1.2 km) that have no OSM
  highway within 20 m. Each keeps `dataset`, `length_m`, and for Meta `ai_highway` and `fbid`.
- **QGIS (Meta):** download and unpack the tar.gz, then *Layer → Add Layer → Add Vector Layer*, file
  `CZ_mapwithai_road_data.gpkg` (EPSG:4326).
- **QGIS (Microsoft):** the zip is 1.4 GB for all of Eastern Europe. Extract the rows starting with `CZE`,
  drop the first column, then *Add Vector Layer* on the resulting newline-delimited GeoJSON.
- **Editor:** both datasets appear in Rapid (rapideditor.org) as AI layers.

## Notes
- **Measured gap** (local match; OSM highways from the OSM API map call on each bbox, 2026-09-28,
  20 m buffer, detections densified to 10 m):

  | Area (bbox) | Microsoft detected / not in OSM | Meta 2019 "missing" / still not in OSM |
  |---|---|---|
  | Brdy forest (13.75,49.70,13.85,49.75) | 88.2 km / 2.2 km (2.5%) | 26.9 km / 15.8 km |
  | Vsetín hills (17.97,49.31,18.01,49.34) | 62.4 km / 2.1 km (3.4%) | 6.9 km / 2.7 km |
  | Říčany suburb (14.63,49.985,14.66,50.005) | 43.9 km / 2.4 km (5.5%) | 2.1 km / 0.6 km |

- **Microsoft:** Czechia is covered, but the OSM road and track network already contains 94–97% of what
  the model finds. OSM has far more forest tracks than the model detects under canopy (29 km of
  track matched against 224 track ways in the Brdy bbox). The leftovers are short pieces, 8–10 runs of 50 m
  or more per sample bbox.
- **Meta:** the 2019 "missing" roads still have about 14 km unmatched in Brdy. Only 0.2 km of those
  13.8 km coincides with a Microsoft 2025 detection within 20 m, so most are overgrown rides,
  skid trails or false positives. Useful only as a hint layer for forest tracks in the former Brdy military
  area.
- **Community position:** the OSM wiki page Rapid says Meta's AI roads are conflated against OSM and "only
  generates missing roads"; for the Microsoft building layer in Rapid it says the data "requires reviewing every single building". No talk-cz thread on
  Rapid/MapWithAI was found (talk-cz archive at osmap.vfosnar.cz, 2026-09 listing). The OSMF LWG has not
  ruled on either dataset. Microsoft's is ODbL, so no waiver question.
- **Verdict:** keep as a review layer for mappers using Rapid, not a Sync dataset. Neither has a stable,
  meaningful ID for ongoing sync (Meta has way_fbid, Microsoft has none).

## Wiki entry
```
===AI detekce cest (Meta MapWithAI, Microsoft Road Detections)===
* dataset: CZ_mapwithai_road_data (Meta, 2019); Road Detections Eastern Europe (Microsoft, 2025-04)
* gestor: [https://github.com/facebookmicrosites/Open-Mapping-At-Facebook Meta]; [https://github.com/microsoft/RoadDetections Microsoft]
* licence: MIT (Meta) [https://github.com/facebookmicrosites/Open-Mapping-At-Facebook/blob/main/LICENSE.md]; ODbL (Microsoft) [https://opendatacommons.org/licenses/odbl/]
* datové primitivy: linie
* odkaz: https://rapideditor.org/country_exports/CZ_mapwithai_road_data.gpkg.tar.gz
* navržený tag {{tag|highway|track}} po ruční kontrole
* poznámka: Microsoft detekce jsou v OSM z 94–97 % už zmapované; Meta 2019 má v Brdech 14 km neshod, ale z velké části jde o zarostlé průseky – jen jako podklad pro kontrolu
```
