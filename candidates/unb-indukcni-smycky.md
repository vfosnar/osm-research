# Unie neslyšících Brno – Indukční smyčky (Mapotic)

| Field | Value |
|---|---|
| publisher | Unie neslyšících Brno (Mapotic map id 13630, owner account "Unie neslyšících Brno") |
| url | https://www.mapotic.com/api/v1/maps/13630/pois.geojson/ (web map https://www.mapotic.com/indukcni-smycky-v-ceske-republice) |
| format | GeoJSON FeatureCollection (Mapotic API, no key needed for this endpoint) |
| coords | yes (WGS84 points) |
| records | 319 POIs (map covers CZ, SK and SI), 161 in the CZ bbox. By type in the CZ bbox: bulkhead (counter) loop 79, spatial (room) loop 57, portable loop 21, uncategorised 4 |
| osm_tags | hearing_loop=yes (Proposal:Hearing loop, status Draft; Key:hearing_loop redirects there), added to the existing amenity/shop/office object |
| osm_count_cz | hearing_loop 1 object, audio_loop 0 (taginfo 2026-09-27; the local 2026-09-27 Czechia extract confirms 1: Kavárna U Žambocha, node 3220984406). Local match against the 2026-09-27 Czechia extract (Postpass unavailable): 85 of 137 loops inside the CZ border have a named or wheelchair-tagged OSM object within 50 m |
| license | none published for the map data; Mapotic terms (https://www.mapotic.com/terms/) give other users no rights to content |
| license_url | https://www.mapotic.com/terms/ |
| license_status | unclear |
| update_freq | irregular (POI last_update: 2023 226, 2024 33, 2025 59, 2026 1) |
| impact | 2 |
| verified | yes |

## Try it
- **Map preview:** none (licence unclear). Web map: https://www.mapotic.com/indukcni-smycky-v-ceske-republice.
- **QGIS:** *Layer → Add Layer → Add Vector Layer*, source type *Protocol: HTTP(S)*, type *GeoJSON*, URI `https://www.mapotic.com/api/v1/maps/13630/pois.geojson/` (tested 2026-09-27: FeatureCollection of 319 points; the category label is in the `category_name` field).

## Notes
- **Gap:** OSM in Czechia has 1 object with hearing_loop and none with audio_loop (taginfo 2026-09-27), so all 161 loops in the CZ bbox are missing. Each point is a building that already exists in OSM (Kaufland and Albert stores, Úřad práce ČR offices, Brno city hall departments, railway stations such as Opava západ and Adamov, churches, Thermal Pasohlávky), so this is a tag-addition task and not new objects.
- **National match (local match against the 2026-09-27 Czechia extract, Postpass unavailable):** 137 of the
  161 bbox points lie inside the CZ border (the other 24 are in Slovakia: 23 in Žilina, 1 near the Austrian border). 85 of
  137 (62 %) have an OSM object within 50 m that carries a name or a wheelchair tag (83 with a named object,
  74 with a wheelchair-tagged one), so the hearing_loop tag can go straight onto an existing, accessibility-
  mapped object. The remaining 52 need a closer look; the extract holds only objects with tourism, wheelchair,
  place-of-worship and similar keys, not every shop or office, so this is a
  lower bound for "existing POI nearby". The only hearing_loop object in OSM Czechia (Kavárna U Žambocha)
  is not in the UNB list.
- The map is multilingual and also lists Slovak (Žilina) and Slovenian loops; filter to the CZ border before use.
- The loop type (bulkhead/spatial/portable) could go into a `hearing_loop:type` subkey, but only hearing_loop=yes is in the draft proposal; don't invent the subkey without community agreement.
- Per-POI details (address, room) sit behind the authenticated detail endpoint; only name, category and position are anonymous. The Mapotic POI `id` is stable.
- Tag status is a caveat: hearing_loop is still a Draft proposal, but it is the key proposed for this exact feature.
- **Licence / contact:** Unie neslyšících Brno, https://www.unb.cz/ (loop project page with contacts: https://ilooptimalforall.unb.cz/kontakt-indukcni-smycka/). Ask them for consent to add hearing_loop=yes from their map; as a disability NGO they benefit from the tag showing up in OSM-based apps.
- Wiki pages read: Proposal:Hearing loop (via Key:hearing_loop redirect).

## Wiki entry
```
===Unie neslyšících Brno – indukční smyčky===
* dataset: Indukční smyčky v České republice (mapa Mapotic)
* gestor: [https://www.unb.cz/ Unie neslyšících Brno]
* licence: neuvedena, nutné vyžádat souhlas
* datové primitivy: body
* odkaz: https://www.mapotic.com/api/v1/maps/13630/pois.geojson/
* navržený tag {{tag|hearing_loop|yes}} na existujících objektech (úřady, obchody, nádraží)
* poznámka: v OSM je v Česku jen 1 objekt s hearing_loop, mapa obsahuje 137 indukčních smyček v Česku (u 85 z nich je do 50 m existující objekt OSM)
```
