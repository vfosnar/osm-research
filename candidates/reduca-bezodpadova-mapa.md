# Reduca – Bezodpadová mapa (bulk shops, milk vending machines, charity shops)

| Field | Value |
|---|---|
| publisher | Reduca.cz (zero-waste blog and crowd-sourced map founded by Martina Sumbalová; web https://www.reduca.cz/, map https://mapa.reduca.cz/) |
| url | https://api.reduca.cz/v1/map/load (anonymous JSON, whole map in one response, 1.4 MB) |
| format | JSON: `data.places[]` with `id`, `slug`, `name`, `description`, `address` (street, city, country), `location` (lat, lng), `type`, `groceries` (ids of products sold unpackaged), `date_added`, `rating`; lookup lists `types`, `categories`, `groceries` |
| coords | yes (WGS84) |
| records | 1,760 places, of them 1,334 in CZ: 479 shops ("Obchod", mostly bulk/zero-waste), 199 "Azylový dům", 186 farms, 144 milk vending machines ("Mlékomat"), 88 "Krabice", 72 e-shops, 52 bazaars/charity shops, 32 rental/library/repair places, 32 restaurants, 24 farmers' markets, 20 florists |
| osm_tags | bulk shops: existing shop=* + bulk_purchase=only / bulk_purchase=yes (wiki Key:bulk_purchase, in use); milk machines: amenity=vending_machine + vending=milk (wiki Key:vending, value list); charity shops: shop=charity (wiki Tag:shop=charity, de facto) or shop=second_hand |
| osm_count_cz | taginfo Geofabrik CZ (2026-09-28): bulk_purchase=only 4, bulk_purchase=yes 12, vending=milk 41, shop=second_hand 139, shop=charity 29 |
| license | none stated on the map, API or blog |
| license_url | none |
| license_status | unclear |
| update_freq | crowd-sourced, now mostly dormant: CZ records added 2017: 658, 2018: 205, 2019: 196, 2020: 171, 2021: 66, 2022–2024: 27 |
| impact | 2 |
| sync_fit | MapRoulette (attribute enrichment of existing shops with bulk_purchase; many records need a survey because the data is 4–9 years old) |
| verified | yes |

## Try it
- **Map preview:** none (licence unclear).
- **Web viewer:** https://mapa.reduca.cz/ (Leaflet, filter by type and by product sold unpackaged).
- **QGIS:** the API returns nested JSON, not GeoJSON (tested 2026-09-28: 1,760 places). Flatten it to CSV with
  `curl -s https://api.reduca.cz/v1/map/load | python3 -c "import json,csv,sys;w=csv.writer(sys.stdout);[w.writerow([p['id'],p['name'],p['type']['name'],p['location']['lng'],p['location']['lat']]) for p in json.load(sys.stdin)['data']['places']]" > reduca.csv`,
  then *Layer → Add Layer → Add Delimited Text Layer*, delimiter comma, X = column 4, Y = column 5, EPSG:4326.

## Notes
Gap analysis with Postpass (2026-09-28), Prague bbox 14.22,49.94,14.71,50.18 and Brno bbox 16.48,49.12,16.73,49.29;
a Reduca shop counts as matched when an OSM shop/craft/amenity within 80 m shares a name word:

- **Bulk shops ("Obchod"):** Prague 46 matched / 70 not found, Brno 43 / 40. The 89 matched shops are the useful
  part: they exist in OSM and only lack `bulk_purchase` (16 objects in all of Czechia carry it). Many of the
  110 unmatched shops are probably closed (the not-found list mixes chain health-food shops such as
  "Country life" with small shops that no longer exist), so they need a survey, not an import.
- **Milk vending machines:** 144 CZ records, of which 15 have an OSM vending=milk or shop=dairy within 60 m
  (CZ bbox, Postpass). 129 of the 144 were added in 2017, and many farm milk machines have closed since, so this is
  a survey list only.
- **Charity shops/bazaars:** Prague 7 matched / 16 not found, Brno 1 / 4.
- The "Azylový dům" (199) and "Krabice" (88) layers are outside the circular-economy scope and were not analysed.
- Place `id` is a stable integer, `slug` a URL-friendly name; a `ref:reduca` key is not worth it for a dormant
  source. The practical use is a one-off MapRoulette challenge "add bulk_purchase to these shops".
- Not listed on Cs:Česko/freemap, Cs:Zdroje_v_jednani or in Sync config.toml (checked 2026-09-28).
- Contact: via https://www.reduca.cz/ (blog author, map admin user id 1).

## Wiki entry
```
===Reduca – Bezodpadová mapa===
* dataset: Bezodpadová mapa (bezobalové obchody, mlékomaty, bazary a dobročinné obchody)
* gestor: [https://www.reduca.cz/ Reduca.cz]
* licence: neuvedena, nutno požádat o souhlas
* datové primitivy: body
* odkaz: https://api.reduca.cz/v1/map/load
* navržený tag {{tag|bulk_purchase|only}}, {{tag|bulk_purchase|yes}}, {{tag|vending|milk}}, {{tag|shop|charity}}
* poznámka: 89 bezobalových obchodů v Praze a Brně je v OSM bez tagu bulk_purchase (v celé ČR ho má 16 objektů); data jsou z let 2017–2021
```
