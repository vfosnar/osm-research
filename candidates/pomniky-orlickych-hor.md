# Pomníky Orlických hor – field database of memorials (diploma thesis, 2023–2025)

| Field | Value |
|---|---|
| publisher | Author of the diploma thesis "Pomníky jako součást paměti krajiny Orlických hor" (ArcGIS Online account `slanina_spszem`); item https://www.arcgis.com/home/item.html?id=fa652229875a48028adb42f9582c91c9 , web map https://www.arcgis.com/home/item.html?id=9a88f432d46649aebb679e38c245dcea |
| url | https://services6.arcgis.com/MBLxaIHHJFo8VA1y/arcgis/rest/services/Pomníky_Orlických_hor___databáze_WFL1/FeatureServer/0 |
| format | ArcGIS FeatureServer (JSON/GeoJSON, `outSR=4326` works) |
| coords | yes (points, field survey) |
| records | 161 memorials (pietní 57, válečné 47, oslavné 38, pietní/válečné 12, osobnosti 4, oslavné/osobnosti 3); stav: úplný 117, neúplný 34, zaniklý 10; fields: name, category, date of origin (`vznik`), author, maintenance state (`pece`), symbolism flags, description, survey date, ZSJ code, link to Mapy.cz for 99 |
| osm_tags | historic=memorial + memorial=war_memorial / stone / plaque / cross, name, start_date, inscription (wiki Tag:historic=memorial, Key:memorial) |
| osm_count_cz | historic=memorial 30,273; memorial=war_memorial 2,899; memorial=stone 1,088; memorial=plaque 5,954 (taginfo CZ 2026-09-28) |
| license | none stated (item licenseInfo empty) |
| license_url | n/a |
| license_status | unclear |
| update_freq | one-off (survey 2023–2025, published 2026-01) |
| impact | 1 |
| sync_fit | MapRoulette (mixed/ambiguous categories, memorial subtype judgement) |
| verified | partial |

## Try it
- **Map preview:** none (licence unclear).
- **QGIS:** *Layer → Add Layer → Add ArcGIS REST Server Layer → New*, URL `https://services6.arcgis.com/MBLxaIHHJFo8VA1y/arcgis/rest/services/Pomníky_Orlických_hor___databáze_WFL1/FeatureServer`, connect, add layer *pomníky Orlických hor*. Or *Add Vector Layer* with `…/FeatureServer/0/query?where=1=1&outFields=*&outSR=4326&f=geojson`.
- **Web:** the ArcGIS web map linked above.

## Notes
- **Found by:** ArcGIS Online anonymous search sweep, keyword "pomníky" in the CZ bbox (see `research/platform-sweeps.md`).
- **What it is:** a systematic field and archive survey of every memorial in the Orlické hory (bbox 16.31,49.95,16.83,50.38) for a diploma thesis. It describes each object in detail, including memorials of the 1866 war, personal memorial stones, plaques and destroyed monuments.
- **Gap (local match against the 2026-09-27 Czechia extract, any historic=*, tourism=artwork, amenity=place_of_worship, man_made=cross within 75 m):** of the 151 existing (not zaniklý) memorials, 109 have an OSM object within 30 m, 17 within 30–75 m and **25 have nothing within 75 m**. The missing ones include the pomník obětem války 1866 and the hrob vojáka Rudé armády in Rokytnice v Orlických horách, the pomník řeckým občanům in Těchonín and the smírčí kříž in Pěčín. For matched objects the database adds `start_date`, the author and a description.
- **Caveat:** 99 records link to a Mapy.cz POI (`Odkaz_MAPY_CZ`). The coordinates are the author's own survey (Y_ZS/X_ZD fields), but ask the author whether any position was copied from Mapy.cz before use.
- Suggested ref: none needed for a one-off import (`ID_pom` is only the thesis number).
- **Licence / contact:** no licence. Ask the author via the ArcGIS account `slanina_spszem`. The thesis title above identifies the work. A CC0 or ODbL release from the author would be enough.

## Wiki entry
```
===Pomníky Orlických hor===
* dataset: Pomníky Orlických hor – databáze (diplomová práce „Pomníky jako součást paměti krajiny Orlických hor“)
* gestor: [https://www.arcgis.com/home/item.html?id=fa652229875a48028adb42f9582c91c9 autor diplomové práce (ArcGIS účet slanina_spszem)]
* licence: neuvedena – nutno požádat autora
* datové primitivy: body
* odkaz: https://services6.arcgis.com/MBLxaIHHJFo8VA1y/arcgis/rest/services/Pomníky_Orlických_hor___databáze_WFL1/FeatureServer/0
* navržený tag {{tag|historic|memorial}} + {{tag|memorial|war_memorial}} / {{tag|memorial|stone}}, {{tag|start_date}}
* poznámka: 161 pomníků z terénního průzkumu 2023–2025; 25 dochovaných v OSM do 75 m nic nemá, u ostatních doplní datum vzniku a popis
```
