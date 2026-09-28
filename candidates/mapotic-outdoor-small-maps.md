# Small Mapotic maps: canoe put-ins (Zapádluj), re-use centres, hiking shelters

| Field | Value |
|---|---|
| publisher | three Mapotic maps: Zapádluj (id 9291, account of the Mapotic team, web www.zapadluj.cz); Re-use v ČR (id 18659, private user "Gabriela K.", map labels name "pef čzu"); Bivaky a přístřešky (id 20, private user "Jiri K.") |
| url | https://www.mapotic.com/api/v1/maps/9291/pois.geojson/ ; https://www.mapotic.com/api/v1/maps/18659/pois.geojson/ ; https://www.mapotic.com/api/v1/maps/20/pois.geojson/ (all anonymous) |
| format | GeoJSON points with `id`, `name`, `category_name`, `last_update` |
| coords | yes |
| records | Zapádluj 1,126 (846 in CZ), of them 79 "Nástup / výstup" in CZ (138 in all countries); Re-use 140 (64 re-use centres, 56 re-use points, 10 furniture banks, 10 other); Bivaky 444 (342 in CZ), of them 263 "Turistický přístřešek" in CZ |
| osm_tags | canoe=put_in / canoe=egress / canoe=put_in;egress (wiki Tag:canoe=put_in, de facto); re-use: shop=second_hand (wiki Tag:shop=second_hand, de facto) for re-use centres and furniture banks; there is no documented tag for a re-use corner at a waste collection yard (Key:reuse has no wiki page); shelters: amenity=shelter + shelter_type (wiki Tag:amenity=shelter and Cs:Tag:amenity=shelter) |
| osm_count_cz | taginfo Geofabrik CZ (data until 2026-09-27): canoe=put_in 30, canoe=put_in;egress 70, canoe=egress 11; shop=second_hand 139; amenity=shelter 17,218 |
| license | none stated on any of the three maps; Mapotic terms (https://www.mapotic.com/terms/) give other users no rights to content |
| license_url | none |
| license_status | unclear |
| update_freq | Zapádluj: static (845 of 846 CZ points last updated 2021); Re-use: 2024–2025; Bivaky: crowd-sourced 2017–2026, mostly 2018–2019 |
| impact | 1 |
| verified | yes |

## Try it
- **Map preview:** none (licence unclear).
- **QGIS:** *Layer → Add Layer → Add Vector Layer*, *Protocol: HTTP(S)*, one of the three URIs above
  (GeoJSON, EPSG:4326); filter on `category_name`. Tested 2026-09-28: 1,126 / 140 / 444 features.

## Notes
Gap analysis is a local match against the 2026-09-27 Czechia extract (Postpass unavailable), CZ points only:

- **Zapádluj put-ins:** 70 of 79 put-in/take-out points have no OSM object with a `canoe=*` tag within 150 m
  (9 matched, median 12 m). Names are descriptive ("Nástup pod Římovskou přehradou", "Výstup Toušice",
  "Jindřiš – výstup na autobus"), so each needs a check against imagery. The other layers of the same map
  (weirs, camps, food shops, rentals) are covered better elsewhere: weirs by `mze-isvs-voda-hraze-jezy.md`,
  camps and shops by OSM itself. Vodácká navigace (listed on Cs:Česko/freemap) is a separate, older paddling
  source. Value: a short checklist for paddlers mapping canoe=put_in, nothing to import.
- **Re-use v ČR:** 133 of 140 have no shop=second_hand/charity or `reuse` tag within 100 m. The 56
  "re-use points" (55 missing) are collection spots run by municipalities; 17 of them name a collection yard
  ("(sběrný dvůr …)", "Brno – SSO Hapalova"), which OSM maps as amenity=recycling + recycling_type=centre and
  has no agreed attribute for a re-use corner. The 64 re-use centres and
  10 furniture banks are real shops/depots (74, 69 of them missing) and could be surveyed as shop=second_hand.
  The owner is a private user; the "pef čzu" label points to a Czech University of Life Sciences (PEF ČZU)
  student project, with no contact on the map.
- **Bivaky a přístřešky:** 191 of 263 hiking shelters already have an amenity=shelter or tourism=wilderness_hut
  within 100 m (median 11 m); 72 have none. OSM coverage is good, so the value is a small MapRoulette-style list.
  The 42 rock overhangs/caves and 16 camping spots are not worth adding (natural=cave_entrance and informal
  wild-camping spots).
- All three are one-person or company hobby maps without an organisation to grant a licence; they are
  written up so the open leads from `research/mapotic-maps.md` are closed with numbers.
- Checked and not known: Cs:Česko/freemap, Cs:Zdroje_v_jednani and Sync config.toml contain no Zapádluj,
  re-use or bivak source (2026-09-28).

## Wiki entry
```
===Mapotic – vodácká nástupní místa (Zapádluj)===
* dataset: Zapádluj (mapa Mapotic č. 9291), vrstva „Nástup / výstup“
* gestor: [https://www.zapadluj.cz/ Mapotic]
* licence: neuvedena, nutno požádat o souhlas
* datové primitivy: body
* odkaz: https://www.mapotic.com/api/v1/maps/9291/pois.geojson/
* navržený tag {{tag|canoe|put_in}}, {{tag|canoe|egress}}
* poznámka: 70 ze 79 nástupních a výstupních míst v ČR nemá v OSM do 150 m žádný tag canoe=*; data z roku 2021
```
