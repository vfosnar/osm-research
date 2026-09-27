# ZABAGED 2.36 Zábrana – barriers and gates on roads and forest tracks

| Field | Value |
|---|---|
| publisher | Český úřad zeměměřický a katastrální (ČÚZK), Zeměměřický úřad |
| url | https://ags.cuzk.gov.cz/arcgis/rest/services/ZABAGED_POLOHOPIS/MapServer/54 (ArcGIS REST, layer "Zábrana"); WFS type `ZABAGED_POLOHOPIS:Zábrana` at https://ags.cuzk.gov.cz/arcgis/services/ZABAGED_POLOHOPIS/MapServer/WFSServer; bulk: https://openzu.cuzk.gov.cz/opendata/ZABAGED-GPKG/epsg-5514/ZABAGED-5514-gpkg-20260818.zip (whole ZABAGED, 5.8 GB) |
| format | ArcGIS REST (JSON/GeoJSON, outSR=4326), WFS, GeoPackage |
| coords | yes (points, stated accuracy 5 m) |
| records | 36,809 points: "Závora, brána" (Z) 32,142; "Trvalá zábrana" (T) 4,667. Attributes: typ only. Stable ID `fid_zbg`. |
| osm_tags | Z → barrier=lift_gate / barrier=swing_gate / barrier=gate (type must be checked on imagery or in the field); T → barrier=bar or barrier=bollard/block (fixed, catalogue photo shows a fixed pipe bar). Always as a node on the highway way; ref:zabaged=&lt;fid_zbg&gt; |
| osm_count_cz | taginfo CZ 2026-09-27: barrier=gate 55,617; barrier=lift_gate 9,431; barrier=swing_gate 2,534; barrier=bar 20. No OSM barrier carries ref:zabaged (Postpass 2026-09-27) |
| license | CC BY 4.0 + explicit ČÚZK consent for OSM (Nov 2023) |
| license_url | https://creativecommons.org/licenses/by/4.0/ ; consent recorded on https://wiki.openstreetmap.org/wiki/Cs:%C4%8Cesko/freemap#%C4%8C%C3%9AZK |
| license_status | ok |
| update_freq | ZABAGED is updated continuously; GPKG snapshot 2026-08-18 |
| impact | 3 |
| verified | yes |

## Try it
- **Map preview:** [samples/zabaged-zabrany.geojson](../samples/zabaged-zabrany.geojson): all 375 barriers in Křivoklátsko (bbox 13.75,49.95,14.05,50.10), pre-tagged, with `in_osm_30m` = whether OSM has any point barrier within 30 m. 321 of 375 have none.
- **QGIS:** *Layer → Add Layer → Add ArcGIS REST Server Layer → New*, URL `https://ags.cuzk.gov.cz/arcgis/rest/services/ZABAGED_POLOHOPIS/MapServer`, add *Zábrana* (id 54). Or *Add WFS Layer*, URL `https://ags.cuzk.gov.cz/arcgis/services/ZABAGED_POLOHOPIS/MapServer/WFSServer`, layer `Zábrana`. Native CRS EPSG:5514.

## Notes
- **Why it matters:** a barrier across a forest track decides whether car and bike routing sends people down it. Catalogue definition (2.36, `2_Komunikace/ft_ap041.html`): "Překážka na pozemní komunikaci, určená k zabránění nebo ovládání průjezdu motorových vozidel". Geometry comes from NLI (Národní lesnický institut), IPR Praha, orthophoto and field survey, so it is concentrated on forest roads.
- **Not known:** not in Cs:POI_ZABAGED_Import, not in Sync, not on Cs:Česko/freemap. The known "WMS UHUL – odvozní cesty" entry covers the forest roads, not the barriers on them.
- **Gap (Postpass 2026-09-27, match = any OSM point barrier except linear types):**
  - Křivoklátsko: 375 ZABAGED barriers, OSM 165 point barriers; 329 unmatched at 15 m, 321 at 30 m. Of the 321, every one has an OSM highway within about 25 m (248 within 5 m); the nearest way is highway=track for 212, service 27.
  - Brdy (13.75,49.60,14.05,49.80): 409 in ZABAGED, 608 in OSM, still 283 ZABAGED barriers unmatched at 30 m.
  - Brno centre (16.56,49.17,16.65,49.22): 327 in ZABAGED, 1,713 in OSM, 103 unmatched: the gap is rural.
- **Caveats:** one class "Závora, brána" mixes lift gates, swing gates and gates, so a blind import would give the wrong subtype. Some ZABAGED barriers will have been removed since capture. Best as a Sync/MapRoulette task: snap to the nearest highway node, mapper picks the subtype. Access tags (motor_vehicle=no on the way) must not be derived from the point.
- Wiki pages read: Tag:barrier=lift_gate, Tag:barrier=swing_gate, Tag:barrier=gate, Key:ref:zabaged.

## Wiki entry
```
===ZABAGED – závory a zábrany na cestách===
* dataset: ZABAGED® 2.36 Zábrana (závora, brána; trvalá zábrana)
* gestor: [https://www.cuzk.gov.cz/ ČÚZK]
* licence: CC BY 4.0 + souhlas ČÚZK [https://creativecommons.org/licenses/by/4.0/]
* datové primitivy: body
* odkaz: https://ags.cuzk.gov.cz/arcgis/rest/services/ZABAGED_POLOHOPIS/MapServer/54
* navržený tag {{tag|barrier|lift_gate}} / {{tag|barrier|swing_gate}} / {{tag|barrier|bar}} (podtyp nutno ověřit), {{tag|ref:zabaged|<FID_ZBG>}}
* poznámka: 36 809 zábran hlavně na lesních cestách; na Křivoklátsku chybí v OSM 321 z 375, většinou na highway=track
```
