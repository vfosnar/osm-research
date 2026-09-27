# Památné stromy (memorial trees) – AOPK ČR / ÚSOP

| Field | Value |
|---|---|
| publisher | Agentura ochrany přírody a krajiny ČR (AOPK ČR), IČO 62933591 |
| url | https://data.nature.cz/ds/56/download , https://data.nature.cz/ds/57/download , https://data.nature.cz/ds/58/download (SHP, S-JTSK); GeoJSON WGS84 https://hub.arcgis.com/api/v3/datasets/362de39fceee4a9e9ba1f795bd9bffc6_0/downloads/data?format=geojson&spatialRefId=4326&where=1%3D1 ; ArcGIS REST https://gis.nature.cz/arcgis/rest/services/PamatneStromy/PamatneStromy/MapServer (layers 0 objekty, 1 jedinci, 2 linie, 3 polygony, 6 centroidy); WFS .../PamatneStromy/MapServer/WFSServer |
| format | SHP, GeoJSON, CSV, KML, WFS, ArcGIS REST JSON |
| coords | yes |
| records | 5,359 protected objects (layer 0, multipoint: solitary trees, alleys, groups), 16,972 individual trees (layer 1), 80 alleys without individual positions (lines), 39 groups without positions (polygons), 5,478 centroids (checked 2026-09-27); last update 10.09.2026 |
| osm_tags | natural=tree (or natural=tree_row for alleys) + denotation=natural_monument, name, species/genus; suggested ref:drusop=&lt;KOD&gt; |
| osm_count_cz | denotation=natural_monument 1,343 (1,315 on natural=tree); ref:drusop 3, ref:DRUSOP 4, ref:drusop:tree 1, ref:aopk 3 (taginfo 2026-09-26) |
| license | CC BY 4.0, attribution "(c) AOPK ČR" (stated on data.nature.cz dataset page; NKOD entry has no terms-of-use spec) |
| license_url | https://data.nature.cz/ds/58 ; https://creativecommons.org/licenses/by/4.0/deed.cs |
| license_status | needs_waiver |
| update_freq | irregular (NKOD "OTHER"); data dated 10.09.2026 |
| impact | 4 |
| verified | yes |

## Notes
Known (listed on Cs:Česko/freemap, "Památné stromy", licence given there as "neznámá") — adds: verified download URLs, REST/WFS endpoints, the licence (CC BY 4.0, so an OSM waiver is needed) and record counts.

- **Gap.** OSM has 1,343 `denotation=natural_monument` in CZ. AOPK lists 5,359 objects / 16,972 individual trees. In the South Moravia bbox 16.0,48.6,17.2,49.3, Postpass counts 120 `denotation=natural_monument` against 247 AOPK objects. So roughly 60-75 % are missing, and existing ones lack a stable ID.
- **Attributes.** Layer 0: `KOD` (ÚSOP code, e.g. 100002; stable), `NAZEV`, `TYP`, `POCET` (tree count), `OP_TYP`, `ID_ISOP`, `URL_USOP` (link to drusop.aopk.gov.cz detail). Species is not in the geometry layer; it is on the ÚSOP detail page.
- **Tagging.** Tag:natural=tree and Key:denotation wiki pages (raw, read 2026-09-27) define `denotation=natural_monument` for "an especially old tree … protected for its uniqueness". Alleys map to `natural=tree_row` or individual trees from layer 1. There is no documented ref key: suggest `ref:drusop=<KOD>` (small de facto use exists) and document it on the Cs wiki.
- **Wikidata.** Czech memorial trees are also on Wikidata (~335 OSM trees already carry `wikidata`), which helps with linking.
- **Caveats.** Positions of individuals are GPS/orthophoto based and generally good. Declared-but-dead trees disappear from the register with a delay (`ZMENA_G`/`ZMENA_T` dates help). The cities of Brno, Ostrava and Plzeň publish their own memorial-tree sets in NKOD, which duplicate this one.
- Contact: Jan Votrubec, jan.votrubec@aopk.gov.cz (data steward named on data.nature.cz).

## Wiki entry
```
===Památné stromy (AOPK ČR)===
* dataset: Památné stromy (objekty, jedinci, linie, polygony)
* gestor: [https://www.nature.cz/ Agentura ochrany přírody a krajiny ČR]
* licence: CC BY 4.0, uvádět „(c) AOPK ČR“ [https://data.nature.cz/ds/58] – nutný souhlas pro OSM
* datové primitivy: body, linie, plochy
* odkaz: https://data.nature.cz/ds/56/download , https://gis.nature.cz/arcgis/rest/services/PamatneStromy/PamatneStromy/MapServer
* navržený tag {{tag|natural|tree}} + {{tag|denotation|natural_monument}}, {{tag|ref:drusop|<KOD>}}
* poznámka: v OSM 1 343 památných stromů z 5 359 objektů / 16 972 jedinců v registru
```
