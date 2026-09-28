# MZe ISVS-VODA – Hráze, Jezy, Objekty v korytě (dams incl. pond dams, weirs, drops/chutes in watercourses)

| Field | Value |
|---|---|
| publisher | Ministerstvo zemědělství (MZe), IČO 00020478 (data from the Povodí s.p. companies) |
| url | https://voda.gov.cz/data/ISVSVoda_Hraze.zip ; https://voda.gov.cz/data/ISVSVoda_Jezy.zip ; https://voda.gov.cz/data/ISVSVoda_Objektyvkoryte.zip (NKOD: https://data.gov.cz/zdroj/datové-sady/00020478/e250b943c7a19487974381d408584d21 , .../5bc201cfaeb94e49eabbc18df2e14677) |
| format | SHP points, S-JTSK Křovák East-North (EPSG:5514) |
| coords | yes (the X_JTSK/Y_JTSK attributes are 0, but the geometry is present) |
| records | Hráze 32,701 (17,533 "bezejmenná"; PVL basin 21,729); Jezy 2,353; Objekty v korytě 1,883 (stupně, skluzy) |
| osm_tags | Hráze -&gt; waterway=dam (normally a way across the dam crest; a node is acceptable for small dams per the wiki); Jezy -&gt; waterway=weir (node on the waterway); stupně/skluzy -&gt; waterway=weir? (check; possibly waterway=rapids or ford-like drops; no clear tag); ref:CZ:isvs=&lt;JEV_ID&gt; (new key) |
| osm_count_cz | waterway=dam 1,164; waterway=weir 6,872; man_made=dyke 306 (Geofabrik taginfo 2026-09-27) |
| license | NKOD terms: no copyright work, not a protected database, no sui generis right (NKOD maps it to CC0) |
| license_url | https://data.gov.cz/podmínky-užití/neobsahuje-autorská-díla/ |
| license_status | ok |
| update_freq | continuous (NKOD UPDATE_CONT) |
| impact | 2 |
| sync_fit | Sync for weirs (points, stable ref:CZ:isvs, waterway=weir 1:1); iD fork for dams (lines, stable ref:CZ:isvs); MapRoulette for stupně/skluzy (unclear tag) |
| verified | yes |

## Try it
- **Map preview:** [samples/mze-isvs-voda-hraze-jezy.geojson](../samples/mze-isvs-voda-hraze-jezy.geojson): Třeboňsko (bbox 14.62,48.93,14.92,49.12) with 600 dams (Hráze), 10 weirs and 8 objekty v korytě. Most of these ponds are drawn in OSM, but their dams are not.
- **QGIS:** *Layer → Add Layer → Add Vector Layer*, source type *File*, paste `/vsizip/vsicurl/https://voda.gov.cz/data/ISVSVoda_Hraze.zip/Hraze.shp`. For the other layers use `/vsizip/vsicurl/https://voda.gov.cz/data/ISVSVoda_Jezy.zip/Jezy.shp` and `/vsizip/vsicurl/https://voda.gov.cz/data/ISVSVoda_Objektyvkoryte.zip/Objekty_v_koryte.shp`. The .prj is ESRI "S-JTSK_Krovak_East_North"; pick EPSG:5514 if QGIS asks.

## Notes
- Possible overlap: the waterways theme is handled by another agent, and DIBAVOD (covered) contains some water structures. This MZe/Povodí ISVS-VODA layer is a different, continuously updated register with river km (LOKAL_OD) and watercourse ID (IDVT) per object.
- Postpass checks (random 200-point samples):
  - Jezy: 139/200 (70%) have waterway=weir/dam/lock_gate/sluice_gate within 60 m. The gap is about 700 weirs, and many named ones lack names.
  - Hráze: only 5/200 (2.5%) have waterway=dam or man_made=dyke/embankment within 150 m, although 186/200 sit on an OSM water polygon. These are almost all pond and reservoir dams (rybniční hráze): the ponds exist in OSM, but their dams are unmapped. Tagging 30k point dams is questionable, so this works better as a MapRoulette-style review layer (draw the dam way) than as an import.
  - Objekty v korytě: 58/200 matched any non-channel waterway=* feature.
- Other MZe ISVS-VODA sets exist under the same CC0-like terms and were not verified: Vodní nádrže (ISVSVoda_Vodninadrze.zip), HOZ drainage (ISVSVoda_HOZ.zip), and Zdroje pitné vody (XLSX; content is a 2020 water-works table, "VÚME ÚV 2020 A.xlsx").
- Wiki pages read: Tag:waterway=weir (node on waterway for small weirs), Tag:waterway=dam (way; small dam as node allowed), Tag:man_made=dyke.

## Wiki entry
```
===Hráze a jezy (ISVS-VODA)===
* dataset: Hráze; Jezy; Objekty v korytě
* gestor: [https://voda.gov.cz/ Ministerstvo zemědělství]
* licence: neobsahuje autorská díla, není chráněnou databází (CC0) [https://data.gov.cz/zdroj/datové-sady/00020478/e250b943c7a19487974381d408584d21]
* datové primitivy: body
* odkaz: https://voda.gov.cz/data/ISVSVoda_Hraze.zip
* navržený tag {{tag|waterway|dam}}, {{tag|waterway|weir}}, {{tag|ref:CZ:isvs|<JEV_ID>}}
* poznámka: 32 701 hrází (hlavně rybničních), v OSM je u nich zakreslena hráz jen ve ~2,5 % případů; u jezů chybí ~30 %
```
