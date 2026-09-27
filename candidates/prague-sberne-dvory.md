name: Odpadní zařízení pro občany (sběrné dvory, sběrná místa nebezpečného odpadu, re-use centra – Praha)
publisher: IPR Praha (content MHMP-OCP)
url: https://mp.iprpraha.cz/arcgis/rest/services/Hosted/ZPK_CUR_ZPK_O_SBERODPADU_B/FeatureServer/0 ; catalogue https://opendata.geoportalpraha.cz/datasets/iprpraha::odpadní-zařízení-pro-občany-1
format: ArcGIS FeatureServer (JSON/GeoJSON), Hub downloads
coords: yes
records: 42 (typobjektu: SDHMP 23 city collection yards, SSNO 7 hazardous-waste points, SDMC 5 district yards, REUSE-CE 3 re-use centres, SSMBIO 2 bio-waste, SDMC_SSNO 2), 2026-09-27
osm_tags: amenity=recycling + recycling_type=centre + name + operator + opening_hours (converted by hand from `provoznidoba`) + recycling:*=yes from `odpadprijem`
osm_count_cz: recycling_type=centre 902 CZ (taginfo 2026-09-27); 45 amenity=recycling+recycling_type=centre in Prague (Postpass relation 435514)
license: CC BY 4.0 + IPR consent for all open data in OSM (2018)
license_url: https://geoportalpraha.cz/data-a-sluzby/otevrena-data ; https://lists.openstreetmap.org/pipermail/talk-cz/2018-February/018526.html
license_status: ok
update_freq: frequent (dct:modified 2026-09-14)
impact: 2
verified: yes

## Notes

**Fields.** The layer has rich bilingual attributes:
- `nazev`/`name`, e.g. "Sběrný dvůr hlavního města Prahy Generála Šišky".
- `provozovatel`, `adresa`, `kontakt`.
- `provoznidoba`: free text, e.g. "Po - So 8:30 - 18:00 hod. (8:30 - 17:00 hod. v zimním
  období)…".
- Accepted and restricted waste, hazardous waste, take-back, fees.
- `reuse*` fields.
- `mc`, `globalid`.

**OSM gap.** 22 of 42 have no OSM `recycling_type=centre` within 80 m (Postpass, 2026-09-27).
Existing OSM yards often lack opening hours and accepted-waste tags.

**Caveats.**
- The dataset is small, so it is a manual job. `provoznidoba` is free text and needs manual
  `opening_hours` conversion (it has seasonal variants).
- Bulky-waste containers (`ZPK_O_KONT_OBJEMO_B`) are temporary and should not be imported.
  The sorted-waste containers are already in Sync (`prague_recycling`).
- Wiki read: Tag:amenity=recycling and Cs:Tag:amenity=recycling, Tag:recycling_type=centre.

## Wiki entry
```
===Sběrné dvory Prahy===
* dataset: Odpadní zařízení pro občany
* gestor: [https://geoportalpraha.cz IPR Praha] / MHMP
* licence: CC BY 4.0 + souhlas IPR s využitím všech opendat pro OSM (2018) [https://lists.openstreetmap.org/pipermail/talk-cz/2018-February/018526.html]
* datové primitivy: body
* odkaz: https://mp.iprpraha.cz/arcgis/rest/services/Hosted/ZPK_CUR_ZPK_O_SBERODPADU_B/FeatureServer/0
* navržený tag {{tag|amenity|recycling}} + {{tag|recycling_type|centre}}, {{tag|opening_hours}}
* poznámka: 42 sběrných dvorů a míst s otevírací dobou a seznamem přijímaných odpadů, 22 z nich nemá v OSM do 80 m protějšek.
```
