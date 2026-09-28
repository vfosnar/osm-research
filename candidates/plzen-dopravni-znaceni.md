# Plzeň – svislé dopravní značení (traffic-sign inventory: stop, give way, speed, weight limits, zones)

| Field | Value |
|---|---|
| publisher | Statutární město Plzeň (IČO 00075370); data from Správa veřejného statku města Plzně (SVSMP), published on https://opendata.plzen.eu/ |
| url | GeoJSON: https://opendata.plzen.eu/public/opendata/download-file/8 (ZIP with `dz_svisle.geojson`, 179 MB, WGS84); SHP: https://opendata.plzen.eu/public/opendata/download-file/10 (ZIP with `dz_svisle_pnt/lin/pol`, EPSG:5514, no .prj); KML …/download-file/9, DXF …/7, DGN …/6. NKOD record https://data.gov.cz/zdroj/datové-sady/00075370/fccdd962dc033441f85e1fbd2e36271f (LKOD id https://opendata.plzen.eu/public/opendata/dataset/6) |
| format | GeoJSON (each sign drawn as a cartographic symbol, GeometryCollection of short lines), SHP (28,364 points + 503 lines + 59 polygons), KML, DXF, DGN |
| coords | yes |
| records | 28,396 sign features, ID_ZNAC unique per feature. Selected codes: P4 give way 1,799; P6 stop 86; P2 main road 1,482; B20a speed limit 187; B13 weight limit 117; B2 no entry 789; IP4b one-way 683; IZ5a/IZ5b living-street zone start/end 490/459; IZ8a/IZ8b zone start/end 295/278; E13 text plates 3,163 |
| osm_tags | highway=stop / highway=give_way + direction=forward\|backward on the approach way; traffic_sign=CZ:&lt;code&gt;[value] (CZ:B20a[50], CZ:B13[3.5]); on ways maxspeed + source:maxspeed=sign, maxweight, oneway=yes, highway=living_street |
| osm_count_cz | taginfo CZ 2026-09-27: highway=give_way 17,317; highway=stop 5,441; traffic_sign=city_limit 8,650, maxspeed 1,164, CZ:P4 19, CZ:P6 7. Plzeň bbox 13.265,49.675,13.48,49.81 (Postpass 2026-09-27): highway=give_way 148, highway=stop 16, 241 nodes with highway=stop/give_way or traffic_sign |
| license | NKOD terms on every distribution: "neobsahuje autorská díla", "není autorskoprávně chráněnou databází", "není chráněna zvláštním právem pořizovatele databáze" (narrowMatch CC0), "neobsahuje osobní údaje" |
| license_url | https://data.gov.cz/podmínky-užití/není-chráněna-zvláštním-právem-pořizovatele-databáze/ |
| license_status | ok |
| update_freq | NKOD accrualPeriodicity CONT; files in the ZIP dated 2026-08-04 |
| impact | 3 |
| sync_fit | MapRoulette (sign code → many different tag schemes, needs per-sign judgement) |
| verified | yes |

## Try it
- **Map preview:** [samples/plzen-dopravni-znaceni.geojson](../samples/plzen-dopravni-znaceni.geojson): 1,726 signs in central Plzeň (bbox 13.34,49.72,13.42,49.77) limited to the codes that map to OSM tags (P4 906, P6 49, B20a 88, B13 65, IZ5a/b 273, IZ8a/b 343). Each point is the centroid of the sign symbol, with a proposed `traffic_sign` value; P4/P6 points carry `osm_node_within_30m` (only 35 of 955 have an OSM give_way/stop node nearby).
- **QGIS:** download https://opendata.plzen.eu/public/opendata/download-file/10 (24 MB ZIP), unzip, *Layer → Add Layer → Add Vector Layer* → `dz_svisle_pnt.shp`. There is no .prj, so set the layer CRS to **EPSG:5514** (S-JTSK / Krovak East North). Filter with `"OZNACENI" IN ('P4','P6','B20a','B13')`. The GeoJSON (download-file/8) is WGS84 but contains unescaped quotes in some `TEXT` values (`ZÓNA {B20a "30"}`), so strict JSON parsers reject it; use the SHP.

## Notes
- **Gap analysis (Plzeň, Postpass 2026-09-27; sign centroid vs OSM):**
  - P6 stop: 86 signs, 5 have an OSM highway=stop node within 30 m → 81 missing.
  - P4 give way: 1,799 signs, 75 have an OSM highway=give_way within 30 m → ~1,720 missing (some P4 are duplicates on both sides of an approach).
  - B13 weight limit: 117 signs, 22 have a road with maxweight within 25 m → ~95 roads lack maxweight.
  - B20a speed limit: 187 signs, 92 have a road with maxspeed within 25 m.
  - IZ8a zone entry (almost all "ZÓNA 30"): 295 signs, 89 have a maxspeed=30 road within 25 m.
  - IZ5a living-street zone: 490 signs, 378 next to highway=living_street; IP4b one-way: 683 signs, 588 next to a oneway road. These two are mostly mapped already, so they are useful as a check.
- **Caveats:**
  - The points are sign positions on the pavement, with no facing direction. P4/P6 must be moved onto the approaching way with `direction=forward/backward`, which needs a human in a review task, not a blind import.
  - The dataset description warns that on class I–III roads (ŘSD and SÚSPK) the inventory may be out of date.
  - `ID_ZNAC` is unique in the current file; whether it stays stable between releases is not verified.
- **ZABAGED overlap:** none. ZABAGED has no traffic signs.
- **Horizontal markings** (Vodorovné DZ, NKOD …/00075370/e833163cef5025528b5ed17d4bc207e0) are only published as DXF with numeric layer names and no sign codes (79k entities). They are hard to use for crossings.
- **Scope:** checked against Cs:Česko/freemap, Cs:Zdroje_v_jednani and Sync config.toml: no traffic-sign source is listed. The existing [plzen-open-data](plzen-open-data.md) candidate does not cover this layer. A search of all NKOD dataset titles and keywords found no other city that publishes a vertical-sign inventory.
- Wiki pages read: Key:traffic_sign, Cs:Key:traffic_sign (a point sign goes on a node of the way, with `traffic_sign:forward`/`traffic_sign:backward` or `direction`; for a section sign also tag maxspeed + source:maxspeed=sign on the way), Tag:highway=stop, Tag:highway=give_way, Key:maxweight.
- Suggested ref: none on the OSM object. Keep ID_ZNAC in a review layer only, because signs are not usually tagged with operator IDs.

## Wiki entry
```
===Plzeň – svislé dopravní značení===
* dataset: Svislé DZ
* gestor: [https://opendata.plzen.eu/ Statutární město Plzeň (SVSMP)]
* licence: neobsahuje autorská díla, není chráněna zvláštním právem pořizovatele databáze (CC0) [https://data.gov.cz/podmínky-užití/není-chráněna-zvláštním-právem-pořizovatele-databáze/]
* datové primitivy: body
* odkaz: https://opendata.plzen.eu/public/opendata/download-file/10
* navržený tag {{tag|highway|stop}}, {{tag|highway|give_way}} + {{tag|direction|forward}}, {{tag|traffic_sign|CZ:B20a[50]}}, na cestách {{tag|maxspeed}}, {{tag|maxweight}}
* poznámka: ve městě je 86 značek P6 a 1 799 značek P4, v OSM jen 16 highway=stop a 148 highway=give_way; body nemají směr, vhodné pro kontrolní úlohy, ne pro slepý import
```
