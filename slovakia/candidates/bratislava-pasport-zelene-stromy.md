# Bratislava – Zameranie verejnej zelene (302,604 surveyed trees) + Petržalka and Ružinov tree inventories

| Field | Value |
|---|---|
| publisher | Hlavné mesto SR Bratislava (Magistrát, oddelenie tvorby mestskej zelene OTMZ; published on data.bratislava.sk, ArcGIS org `pRlN1m0su5BYaFAS`); district layers: MČ Bratislava-Petržalka (org `gfD2sIpeuhWr0Ulz`), MČ Bratislava-Ružinov (org `9TfFDKe8C35aqkPU`) |
| url | Trees: https://services8.arcgis.com/pRlN1m0su5BYaFAS/arcgis/rest/services/Zameranie_zelene_v_Bratislave_test/FeatureServer/0 (Hub item https://data.bratislava.sk/datasets/c676285f8534424e86495859594f53be_0/about, CSV https://data.bratislava.sk/api/download/v1/items/c676285f8534424e86495859594f53be/csv?layers=0); green areas: same service `/1`; planted trees with species: https://data.bratislava.sk/api/download/v1/items/9d318577711b40f396b662cbb35582cc/geojson?layers=23; Petržalka: https://services-eu1.arcgis.com/gfD2sIpeuhWr0Ulz/arcgis/rest/services/Stromy_read_only/FeatureServer/0; Ružinov: https://services-eu1.arcgis.com/9TfFDKe8C35aqkPU/arcgis/rest/services/Inventarizácia_drevín_Stromy_3D/FeatureServer/0 |
| format | ArcGIS FeatureServer (`f=geojson`, `outSR=4326`, 2,000 per page); Hub CSV (34 MB, X/Y in EPSG:3857), GeoJSON |
| coords | yes (surveyed points; "zameranie" = geodetic survey handed over 2023-10-09 … 2025-07-29) |
| records | Magistrát: 302,604 tree points (`GS_ID` unique 1–302,614, height `vyska_7` on 302,150, district, locality, survey date) and 133,662 green-area polygons (68,095 lawn, 34,672 shrub, 11,654 flower bed, 7,679 hedge, 5,010 tree group, 6,552 other); Výsadba stromov od 2019: 6,651 planted trees with `drevina_lat`/`drevina_sk`, cultivar, planting date, project, donor; Petržalka: 9,268 trees with species, trunk circumference, `id_text`; Ružinov: 36,097 trees with species, height, `ID_S` (inventory 2021) |
| osm_tags | natural=tree + height=*, species=*, genus=*, leaf_type=*, circumference=* (Tag:natural=tree); green polygons: barrier=hedge, natural=shrubbery (not proposed for import) |
| osm_count_sk | natural=tree 99,862 in Slovakia, height 40,557, species 2,154 (taginfo, data until 2026-09-29); inside the Bratislava city relation 1702499: natural=tree 8,459, barrier=hedge 481 (Postpass, 30 Sep 2026) |
| license | CC BY 4.0 (Magistrát Hub items and "Pasport hl. mesta SR Bratislavy" app; Petržalka item: "Podmienky používania sú v súlade s licenciou CC BY 4.0"); Ružinov: none stated (access information "© Mestská časť Bratislava-Ružinov") |
| license_url | https://creativecommons.org/licenses/by/4.0/ ; https://data.bratislava.sk/datasets/c676285f8534424e86495859594f53be_0/about ; https://www.arcgis.com/home/item.html?id=6209f0adfe414998b64ee39854a7e894 |
| license_status | needs_waiver (Magistrát, Petržalka); unclear (Ružinov) |
| update_freq | Magistrát survey: handed over in batches 2023–2025, item modified 2026-05; plantings layer updated each planting season; Petržalka field app (edits 2022–2026) |
| impact | 5 |
| sync_fit | Sync (points; `ref:bratislava:strom=GS_ID`, category → natural=tree 1:1; height as update key; species joined from the plantings/Petržalka/Ružinov layers where they coincide) |
| verified | yes |

## Try it

- **Map preview:** [../samples/bratislava-pasport-zelene-stromy.geojson](../samples/bratislava-pasport-zelene-stromy.geojson) — the 1,608 surveyed trees in Staré Mesto (bbox 17.100,48.140–17.115,48.150) with `natural=tree`, `ref:bratislava:strom`, `height`. OSM has 337 `natural=tree` nodes in the same bbox (Postpass, 30 Sep 2026).
- **QGIS:** *Layer → Add Layer → Add ArcGIS REST Server Layer → New*, URL `https://services8.arcgis.com/pRlN1m0su5BYaFAS/arcgis/rest/services/Zameranie_zelene_v_Bratislave_test/FeatureServer` (layer 0 trees, layer 1 green areas). Or download the CSV `https://data.bratislava.sk/api/download/v1/items/c676285f8534424e86495859594f53be/csv?layers=0` and add it as *Delimited Text*: delimiter comma, X field `X`, Y field `Y`, CRS **EPSG:3857** (the Hub CSV is in Web Mercator, not WGS84). Tested 30 Sep 2026.
- **Web:** "Zameranie verejnej zelene OTMZ HMBA 2023-2025" (ArcGIS Experience, item fb90af4cf0ee47e4ad016c95dced2648).

## Notes

- **Why trees were "blocked" before:** the only Slovak discussion (osm_sk "natural=tree pre každý strom", Feb–Mar 2023, `s-VHFxm8-D4`) was about detecting *every tree including forests* from LiDAR (Martin Ždila, "Dáta máme"); replies suggested deriving forest leaf type instead, and the thread moved to NLC forest maps. Nothing licence-related blocked city trees — nobody had proposed a city register. This source is different in kind: surveyed street and park trees with stable IDs, exactly what `natural=tree` is for in towns.
- **ZBGIS overlap:** KTO type EC030 *Strom* covers only solitary trees, groups under 400 m² and rows with spacing over 10 m, attribute only leaf type; tree rows and park stands go to EA020/EC016. The city survey holds every tree with its own ID and height, so ZBGIS does not substitute for it.
- **Gap:** 800 random surveyed trees matched with Postpass (30 Sep 2026): 20 have a `natural=tree` within 3 m (98 % missing); 221 fall within 3 m of any tree, tree row, wood or forest feature, so about 72 % sit in places where OSM shows no vegetation at all. District layers: Petržalka 496 of 500 sampled missing, Ružinov 497 of 500 missing (3 m). Surveyed trees per district: Ružinov 49,263, Petržalka 44,731, Karlova Ves 34,984, Nové Mesto 30,897, Devín 22,298, Dúbravka 21,114, Záhorská Bystrica 20,477, Rača 18,204, Staré Mesto 17,122 (others below 14,000).
- **Species:** the big survey has no species field. Species come from three smaller layers: plantings since 2019 (6,651, CC BY 4.0), Petržalka (9,268, CC BY 4.0) and Ružinov (36,097, licence unclear). The geoportal also serves a working copy `zp/pasport_STROMY_all_dočasne` (281,887 points) where 7,798 trees already carry species, health, stability and crown width from a dendrologist's assessment — not published as open data, so only a lead for later enrichment.
- **Green polygons (layer 1):** hedges (7,679) and shrub beds (34,672) are geometry, and the community prefers not to import non-ZBGIS geometry directly; use as MapRoulette pointers at most.
- **Suggested ref key:** `ref:bratislava:strom=<GS_ID>` (not in use). For Petržalka/Ružinov records, keep their IDs only if the district layers are synced separately.
- **Tagging checked:** Tag:natural=tree (height, circumference in metres, species/genus, leaf_type). The source height is in metres with two decimals — round to 0.5 m.
- **Contact:** Magistrát hl. m. SR Bratislavy, oddelenie dát a analýz (data.bratislava.sk) for the waiver; OTMZ owns the survey. Petržalka: Oddelenie životného prostredia MČ Petržalka (layer credits). Ružinov: GIS team of MČ Ružinov ("Ruzinov v 3D" hub).

## Wiki entry
```
=== Bratislava – zameranie verejnej zelene (stromy) ===
* dataset: Zameranie verejnej zelene v Bratislave (stromy, plochy); Výsadba stromov v Bratislave od roku 2019; Stromy MČ Petržalka
* správca: [https://data.bratislava.sk/ Hlavné mesto SR Bratislava], [https://mapy-petrzalka.hub.arcgis.com/ MČ Bratislava-Petržalka]
* licencia: CC BY 4.0 [https://creativecommons.org/licenses/by/4.0/]
* dátové primitívy: body (stromy), plochy (živé ploty, kríky, záhony)
* odkaz: https://data.bratislava.sk/api/download/v1/items/c676285f8534424e86495859594f53be/csv?layers=0
* navrhované značky: {{tag|natural|tree}}, {{tag|height|<vyska_7>}}, {{tag|species|<drevina_lat>}}, {{tag|ref:bratislava:strom|<GS_ID>}}
* poznámka: Mesto zameralo 302 604 stromov s výškou a stabilným ID, v OSM je v Bratislave 8 459 stromov a 98 % zameraných stromov v OSM chýba.
```
