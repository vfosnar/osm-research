# Oázy chladu – kašny a fontány, studánky a prameny, pumpy, mlžítka (Praha)

| Field | Value |
|---|---|
| publisher | IPR Praha (content by MHMP) |
| url | https://mp.iprpraha.cz/arcgis/rest/services/Hosted/AGD_CUR_AGD_OCH_FONTANY_B/FeatureServer/0 ; https://mp.iprpraha.cz/arcgis/rest/services/Hosted/AGD_CUR_AGD_OCH_STUDANKYPRAMENY_B/FeatureServer/0 ; https://mp.iprpraha.cz/arcgis/rest/services/Hosted/AGD_CUR_AGD_OCH_PUMPY_B/FeatureServer/0 ; https://mp.iprpraha.cz/arcgis/rest/services/Hosted/AGD_CUR_AGD_OCH_MLZITKA_B/FeatureServer/0 |
| format | ArcGIS FeatureServer (JSON/GeoJSON), Hub downloads |
| coords | yes |
| records | fountains 297 (fontána 197, kašna 86, kaskáda 14); springs/wells 213; hand pumps 94; mist sprayers 52 (2026-09-27) |
| osm_tags | amenity=fountain (+ fountain=decorative, name); natural=spring or man_made=water_well (from `typ`: studánka/pramen/prameniště → natural=spring, studna → man_made=water_well) + drinking_water=yes\|no only when druh_vody=P/U; man_made=water_well + pump=manual for pumps; mist sprayers: amenity=mist_spraying_cooler — not verified on wiki, see notes |
| osm_count_cz | amenity=fountain 2,911 CZ / 435 Prague; natural=spring 4,844 CZ / 78 Prague; man_made=water_well 2,521 CZ / 86 Prague (taginfo Geofabrik and Postpass relation 435514, 2026-09-27) |
| license | CC BY 4.0 + IPR consent for all open data in OSM (2018) |
| license_url | https://geoportalpraha.cz/data-a-sluzby/otevrena-data ; https://lists.openstreetmap.org/pipermail/talk-cz/2018-February/018526.html |
| license_status | ok |
| update_freq | seasonal (dct:modified 2026-07-31) |
| impact | 3 |
| verified | yes |

## Notes

Known (listed on Cs:Česko/freemap, as "Pražské kašny a fontány" (prazskekasny.net,
CC BY-NC-ND 2.5) and "Studánky" (estudanky.eu, CC BY-NC-ND)). This file adds: a
**licence-compatible official source** for the same themes. It is IPR's "Oázy chladu" series,
covered by IPR's 2018 OSM consent. The drinking fountain layer (`AGD_OCH_PITKA_B`) is left out
because Sync already handles Pražská pítka.

**Fields.**
- Fountains: `nazev` (real names, e.g. "Pomník Vítězslava Hálka"), `typ` (1 fontána, 2 kašna,
  3 kaskáda), `pristupnost`, `provoz` (sezónní/celoroční/nefunkční), `provoz_spec`, `spravce`,
  `provozovatel`, `globalid`.
- Springs: `nazev` (e.g. "studánka V Obsinách"), `typ` (studánka, pramen, prameniště, studna,
  jiný), `druh_vody` (P pitná / U užitková / N nezjištěno), `pristupnost`.
- Pumps: `nazev` (street name), `druh_vody`, `provoz`.
- Mist sprayers: `nazev`, `provoz_spec` (e.g. "květen - září").

**OSM gap (Postpass, 2026-09-27).**
- Fountains: 66 of 297 have no OSM fountain or water feature within 30 m.
- Springs and wells: 143 of 213 have no `natural=spring`, `man_made=water_well`, `water_tap` or
  `drinking_water` within 30 m.
- Pumps: 60 of 94 have no matching feature within 20 m.

The main value is springs (estudanky.eu is NC-ND and cannot be used), plus names and
seasonality for fountains.

**Caveats.**
- `druh_vody` is mostly "N" (unknown), so do not add `drinking_water` unless it is P or U.
- Wiki read: Tag:amenity=fountain and Cs:Tag:amenity=fountain (fountain=*, drinking_water),
  Tag:natural=spring and Cs:Tag:natural=spring, Tag:man_made=water_well (pump=*).
- I did not verify mist-sprayer tagging on the wiki. OSM Prague has 25 features tagged
  `man_made`/`amenity=mist_spraying_cooler`. Check the tag page before use, or leave these out.
- Prefer names from this source over prazskekasny.net.

## Wiki entry
```
===Oázy chladu – kašny, fontány, studánky, pumpy (Praha)===
* dataset: Oázy chladu – kašny, fontány; studánky, prameny; pumpy; mlžítka
* gestor: [https://geoportalpraha.cz IPR Praha] / MHMP
* licence: CC BY 4.0 + souhlas IPR s využitím všech opendat pro OSM (2018) [https://lists.openstreetmap.org/pipermail/talk-cz/2018-February/018526.html]
* datové primitivy: body
* odkaz: https://mp.iprpraha.cz/arcgis/rest/services/Hosted/AGD_CUR_AGD_OCH_FONTANY_B/FeatureServer/0 (a vrstvy AGD_OCH_STUDANKYPRAMENY_B, AGD_OCH_PUMPY_B, AGD_OCH_MLZITKA_B)
* navržený tag {{tag|amenity|fountain}}, {{tag|natural|spring}}, {{tag|man_made|water_well}} + {{tag|pump|manual}}
* poznámka: licenčně čistá náhrada za prazskekasny.net a estudanky.eu; 143 z 213 pražských studánek/pramenů a 66 z 297 kašen v OSM chybí.
```
