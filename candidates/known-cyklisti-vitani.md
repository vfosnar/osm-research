# Cyklisté vítáni – certifikovaná zařízení vstřícná k cyklistům (ubytování, gastronomie, výletní cíle)

| Field | Value |
|---|---|
| publisher | Partnerství, o.p.s., IČO 45773521, Údolní 33, Brno (operator of the brand since the split from Nadace Partnerství); cv@partnerstvi-ops.cz, +420 604 423 771 |
| url | https://www.cyklistevitani.cz/mapa (all POIs are embedded in the page's `<script data-drupal-selector="drupal-settings-json">` under `mapyComRoutes.<id>.pois`); detail pages https://www.cyklistevitani.cz/sluzba/&lt;slug&gt; |
| format | JSON inside HTML (Drupal settings) |
| coords | yes (WGS84, 7 decimals) |
| records | 853 certified places: Ubytování 437, Gastronomie 206, Výletní cíl 181, Za vínem 21, mixed/untyped 8; 609 flagged `hasCharging` (e-bike charging). Fields: nid (Drupal node id, unique), title, lat, lon, nodeUrl, types, hasCharging, routeIds. Detail pages list the certified services (bike storage, tools, washing, drying, first aid, trip tips) and contact data |
| osm_tags | bike_friend=yes (wiki Key:bike_friend: "a certified bicycle friendly place", status in use, only where a certificate is visible on site) on the existing tourism=* / amenity=* object; proposed ref:cyklistevitani=&lt;nid&gt;. Key:bettundbike is the German ADFC equivalent and is scheme-specific, so not reused |
| osm_count_cz | bike_friend 0; bettundbike 1; no value containing "cyklistevitani" apart from 2 source/note values (taginfo 2026-09-27). Worldwide bike_friend 302 (taginfo.openstreetmap.org) |
| license | consent for OSM ("získán souhlas"), Nadace Partnerství, 26.01.2022, recorded on Cs:Zdroje_v_jednani ("Databáze POI z projektů Cyklisté vítáni, Moravské vinařské stezky a cyklotrasy") |
| license_url | https://wiki.openstreetmap.org/wiki/Cs:Zdroje_v_jednani |
| license_status | ok |
| update_freq | continuous (certifications added and renewed through the year) |
| impact | 3 |
| verified | yes |

## Try it
- **Map preview:** [samples/known-cyklisti-vitani.geojson](../samples/known-cyklisti-vitani.geojson): all 853 places with `ref:cyklistevitani`, name, type, `has_charging`, detail URL and `osm_match_100m` (the nearest OSM object of the expected kind within 100 m, `null` = nothing found).
- **QGIS:** *Layer → Add Layer → Add Vector Layer…*, source type *File*, open the sample GeoJSON (EPSG:4326). The live list has no separate endpoint: save https://www.cyklistevitani.cz/mapa and read the JSON from the `drupal-settings-json` script (`mapyComRoutes` → first key → `pois`).
- **Web:** https://www.cyklistevitani.cz/mapa

## Notes
- Known (listed on Cs:Zdroje_v_jednani as consent obtained in 2022) — adds: the current data access path (the Drupal map page with 853 POIs and stable node ids), a measured gap and a tagging proposal. Nothing from it has been imported: no OSM object in Czechia carries a Cyklisté vítáni tag or ref four years after the consent.
- **Gap (local match against the 2026-09-27 Czechia extract; Postpass returned 503):** OSM object of the expected kind within 100 m (accommodation → tourism=hotel/guest_house/camp_site/chalet/apartment/hostel/motel/alpine_hut; gastronomy → amenity=restaurant/cafe/pub/bar/fast_food/biergarten; wine → craft=winery/shop=wine or gastronomy):
  - Ubytování: 125 of 437 (29 %) have no OSM accommodation within 100 m; of the 312 matches, 255 share a name prefix with the OSM object.
  - Gastronomie: 65 of 207 (31 %) have no OSM restaurant/café/pub within 100 m.
  - Za vínem: 7 of 21 without a match. Výletní cíl: nearly all lie next to some named OSM object (these are museums, castles and information centres, already mapped).
  - All 853 lack the certification attribute in OSM.
- **Use:** add `bike_friend=yes` + `ref:cyklistevitani` to matched objects (good fit for Sync with the nid as key); list the 190 unmatched accommodation and gastronomy places for survey or careful import. The certification is shown on site by a sticker, which satisfies the wiki condition for bike_friend.
- **Caveats:** the 2022 consent came from Nadace Partnerství; the web now names Partnerství, o.p.s. as operator, so confirm the consent still covers the current data (cv@partnerstvi-ops.cz). Coordinates are the brand's own pins, not surveyed entrances.
- Wiki pages read: Key:bike_friend, Key:bettundbike.

## Wiki entry
```
===Cyklisté vítáni – certifikovaná zařízení===
* dataset: mapa certifikovaných zařízení Cyklisté vítáni
* gestor: [https://www.cyklistevitani.cz/ Partnerství, o.p.s.]
* licence: souhlas pro OSM (Nadace Partnerství, 26.01.2022, viz Cs:Zdroje_v_jednani)
* datové primitivy: body
* odkaz: https://www.cyklistevitani.cz/mapa
* navržený tag {{tag|bike_friend|yes}}, {{tag|ref:cyklistevitani|<nid>}}
* poznámka: 853 certifikovaných míst, v OSM žádné nemá značku; 125 ubytování a 65 restaurací v OSM do 100 m chybí
```
