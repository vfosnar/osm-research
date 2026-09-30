# MV SR – sirény a úkryty civilnej ochrany v Bratislave (ArcGIS)

| Field | Value |
|---|---|
| publisher | Ministerstvo vnútra SR (ArcGIS Online organisation `minv`, owner `minv_publisher`) |
| url | sirens: https://services-eu1.arcgis.com/WVOWAPkFgYuaZiF5/arcgis/rest/services/sireny_bratislava/FeatureServer/0 ; shelters: https://services-eu1.arcgis.com/WVOWAPkFgYuaZiF5/arcgis/rest/services/ukryty_bratislava/FeatureServer/0 (items e5fd946e3d834693aca9cdd52a20766b, 44105af9aa61402a85f0ac9a8873bd91, web map c41c874556404c29ab84b4911a10d0e7) |
| format | ArcGIS FeatureServer (query with `f=geojson`, `outSR=4326`) |
| coords | yes, but geocoded from addresses (every siren flagged `orientačná`; 122 of 186 shelters `orientačné`, 38 `exact_OMA`) |
| records | 104 sirens, 186 public shelters with total capacity 30,180, in four boroughs: Ružinov, Staré Mesto, Nové Mesto, Rača (published 10 Jul 2026) |
| osm_tags | sirens: emergency=siren, siren:model, operator; shelters: amenity=shelter, shelter_type=bomb_shelter, capacity, operator (checked on Tag:emergency=siren and Key:shelter_type) |
| osm_count_sk | emergency=siren 79 in Slovakia (taginfo, data until 2026-09-29), 7 in the Bratislava bbox 16.95,48.05,17.35,48.27 (Postpass 30 Sep 2026); bunker_type=bomb_shelter 2 in Slovakia |
| license | none stated (item `licenseInfo` empty; credits only "spracovala: Alexandra Bánovská, publikoval: Mgr. Miloslav Ofúkaný") |
| license_url | https://www.arcgis.com/home/item.html?id=c41c874556404c29ab84b4911a10d0e7 |
| license_status | unclear |
| update_freq | one-off (all items created and last modified 10 Jul 2026) |
| impact | 2 |
| sync_fit | Sync (points; sirens keyed by `sirena_c`, shelters by `evidencne_cislo`; category 1:1 per layer), with manual placement because the coordinates are geocoded |
| verified | yes |

## Try it
- **Map preview:** no sample, because no licence is stated (`unclear`).
- **QGIS:** *Layer → Add Layer → Add ArcGIS REST Server Layer → New*, URL `https://services-eu1.arcgis.com/WVOWAPkFgYuaZiF5/arcgis/rest/services/sireny_bratislava/FeatureServer` (and `…/ukryty_bratislava/FeatureServer`). Or as GeoJSON in *Add Vector Layer*: `https://services-eu1.arcgis.com/WVOWAPkFgYuaZiF5/arcgis/rest/services/ukryty_bratislava/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=geojson`. Tested 30 Sep 2026.
- **Web:** web map "Sirény a úkryty v Bratislave" (item c41c874556404c29ab84b4911a10d0e7).

## Notes
- Sirens: fields `sirena_c` (siren code such as `BAIII-001`), `typ` (600T 46, 1200T 21, ES1200 13, EC1200 10, 300T 4, others), `rok_zast` (installation year), `ovladanie` (95 radio-controlled RO/RDS, 6 local MO), `majitel` (SKMCO MV SR 67, Duslo 16, Slovnaft 12, MO SR, ŽSR…), `pocet_obyv` (population covered), `adresa`. `typ` goes to `siren:model`; derive `siren:type` only after checking the model codes with the owner.
- Shelters: `evidencne_cislo` (registration number such as `01 03 001`), `druh` (133 OÚ odolný úkryt = blast-resistant, 53 PÚ plynotesný úkryt = gas-tight), `kapacita`, `spravca` (borough offices, housing co-operatives, Istrochem), `vlastnik`, `ulica_cislo`.
- Gap (Postpass, 30 Sep 2026): 0 of 104 sirens have an OSM `emergency=siren` within 100 m, and 3 of 186 shelters have any bunker or bomb-shelter tag within 60 m. Part of the siren miss is geocoding: the 7 OSM sirens in Bratislava sit on rooftops the address points do not hit. Treat the layer as pointers.
- Coverage is partial: four of the city's 17 boroughs. The okresné úrady keep shelter records; municipal shelter lists (JÚBS) are only in municipal protection plans.
- Shelter tagging: `amenity=shelter` + `shelter_type=bomb_shelter` is the documented value (Key:shelter_type); use `bunker_type=bomb_shelter` only for stand-alone bunkers. Most of these shelters are basements of residential blocks, so map them as a node with `access`/`capacity`, not as a building.
- Licence: public ArcGIS items of a ministry without terms; the data is a civil-protection register (úradný dokument status is doubtful, database right may apply). Ask MV SR, Sekcia krízového riadenia / civil-protection office, for consent, and ask whether the rest of Bratislava and other cities are planned.
- ZBGIS: no siren or civil-defence shelter type in the ZBGIS catalogue (KTO mentions "úkryt" only for huts, checked 30 Sep 2026).
- Wiki pages read: Tag:emergency=siren, Key:shelter_type.

## Wiki entry
```
=== MV SR – sirény a úkryty v Bratislave ===
* dataset: Sirény v Bratislave; Úkryty v Bratislave
* správca: [https://www.minv.sk/ Ministerstvo vnútra SR]
* licencia: neuvedená – potrebný súhlas [https://www.arcgis.com/home/item.html?id=c41c874556404c29ab84b4911a10d0e7]
* dátové primitívy: body
* odkaz: https://services-eu1.arcgis.com/WVOWAPkFgYuaZiF5/arcgis/rest/services/sireny_bratislava/FeatureServer/0
* navrhované značky: {{tag|emergency|siren}}, {{tag|siren:model|<typ>}}, {{tag|amenity|shelter}}, {{tag|shelter_type|bomb_shelter}}, {{tag|capacity|<kapacita>}}
* poznámka: 104 sirén a 186 úkrytov v štyroch mestských častiach Bratislavy; v OSM má náprotivok 0 sirén a 3 úkryty.
```
