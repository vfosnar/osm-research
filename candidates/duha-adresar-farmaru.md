# Adresář farmářů (Hnutí DUHA) – farms selling direct to consumers

| Field | Value |
|---|---|
| publisher | Hnutí DUHA (Friends of the Earth Czech Republic); the KPZ (community-supported agriculture) and educational-farm entries are maintained by Asociace místních potravinových iniciativ (AMPI), as stated on the map's about page. Hosted on Mapotic, map id 2399, web www.adresarfarmaru.cz |
| url | https://www.mapotic.com/api/v1/maps/2399/pois.geojson/ (all published POIs, anonymous); metadata https://www.mapotic.com/api/v1/maps/2399/ |
| format | GeoJSON points with `id`, `name`, `slug`, `category_name`, `last_update`. The per-POI detail (products, opening hours, contacts) needs a Mapotic login |
| coords | yes (WGS84 points) |
| records | 632 (631 in CZ): 350 Farma, 44 Obchod (farm shop), 30 Vzdělávací farma, 114 Fungující KPZ, 26 KPZ wanted, 16 Bedýnky (box schemes), 4 Farmářský trh, 46 Ostatní, 1 Bioklub. last_update: 529 in 2023, 102 in 2024–2026 |
| osm_tags | shop=farm + name (wiki Tag:shop=farm and Cs:Tag:shop=farm, status de facto); farm without a shop stays landuse=farmyard / place=farm |
| osm_count_cz | shop=farm 89 (taginfo Geofabrik CZ, data until 2026-09-27); 101 nodes/ways in the local 2026-09-27 Czechia extract |
| license | none stated; Mapotic terms (https://www.mapotic.com/terms/) give other users no rights to content |
| license_url | none |
| license_status | unclear |
| update_freq | continuous (farmers and users propose entries; 59 points updated in 2026) |
| impact | 3 |
| verified | yes |

## Try it
- **Map preview:** none (licence unclear). The publisher's map is https://www.adresarfarmaru.cz/.
- **QGIS:** *Layer → Add Layer → Add Vector Layer*, source type *Protocol: HTTP(S)*, URI
  `https://www.mapotic.com/api/v1/maps/2399/pois.geojson/` (GeoJSON, EPSG:4326). Filter with
  `"category_name" LIKE '%Farma%' OR "category_name" LIKE '%Obchod%'`; `category_name` is a JSON object
  `{"cs": …, "en": …}`. Tested 2026-09-28: 632 point features.

## Notes
- **Gap analysis (local match against the 2026-09-27 Czechia extract, Postpass unavailable):** of the 424
  farm, farm-shop and educational-farm points in CZ, **408 have no shop=farm/greengrocer/dairy within 150 m**
  (Farma 341 of 350, Obchod 38 of 44, Vzdělávací farma 29 of 30). With a looser rule (any shop=farm,
  place=farm or landuse=farmyard within 300 m) 388 still have nothing. The 16 matches have a median distance of
  88 m, so points are placed at the farm address, not always the shop door.
- Only 1 of 134 KPZ pick-up points, box schemes and farmers' markets is near a shop=farm; these are mostly
  pick-up addresses, not permanent shops, and are not suitable for OSM.
- OSM has only 89–101 shop=farm in the whole country, so this is the largest list of farm-gate sales found in
  any round. It is a survey/MapRoulette list, not a blind import: many "Farma" entries are sole traders listed
  under a personal name ("Josef Košař", "Malár František") selling from their yard, and the map does not say
  whether a point is a real shop with opening hours (that is in the login-only detail).
- Personal data: the about page says entries are processed "na základě souhlasu jednotlivých osob" and deleted
  4 years after the last contact. A permission request should cover this; entries named after a person should
  get the farm's trading name in OSM.
- Stable ID: Mapotic POI `id` (suggested `ref:mapotic` is not established; use it only in the conflation
  workflow, not as an OSM tag).
- Checked and not known: Cs:Česko/freemap (incl. Potencionální zdroje), Cs:Zdroje_v_jednani and Sync
  config.toml contain no Hnutí DUHA, adresarfarmaru or shop=farm source (2026-09-28).
- Contact: Hnutí DUHA agriculture programme (https://hnutiduha.cz/nase-prace/zemedelstvi); for KPZ entries AMPI.

## Wiki entry
```
===Adresář farmářů Hnutí DUHA===
* dataset: Adresář farmářů (mapa Mapotic č. 2399)
* gestor: [https://www.adresarfarmaru.cz/ Hnutí DUHA] (KPZ a vzdělávací farmy: Asociace místních potravinových iniciativ)
* licence: neuvedena, nutno požádat o souhlas
* datové primitivy: body
* odkaz: https://www.mapotic.com/api/v1/maps/2399/pois.geojson/
* navržený tag {{tag|shop|farm}} + {{tag|name}}
* poznámka: ze 424 farem a farmářských obchodů jich 408 nemá v OSM do 150 m {{tag|shop|farm}} (v celé ČR je jen asi 100 obchodů shop=farm)
```
