# Kokoza – Mapa komunitních zahrad a kompostérů (Mapko)

| Field | Value |
|---|---|
| publisher | Kokoza, o.p.s. (map "Mapa komunitních zahrad a kompostérů" / Mapko, hosted on Mapotic, map id 61) |
| url | https://www.mapotic.com/api/v1/maps/61/pois.geojson/ (web map https://www.mapotic.com/kokoza, also https://www.mapko.cz/) |
| format | GeoJSON FeatureCollection (Mapotic API, no key needed for this endpoint) |
| coords | yes (WGS84 points) |
| records | 1,593 POIs, 1,562 in the CZ bbox. By category: Komunitní zahrada 224, Komunitní kompostér 97, Vermikompostér 946, Lokální potraviny 88, Zahradní kompostér 87, Balkon a Zahrádka 41, Street gardening 40, Bokashi 21, Udržitelné gastropodniky 21, Zelená střecha 11, Udržitelné školy 9, Záhony pro školky 8 |
| osm_tags | leisure=garden + garden:type=community (wiki Tag:leisure=garden, Key:garden:type) |
| osm_count_cz | garden:type=community 109 (taginfo 2026-09-26). Of 213 Kokoza community gardens in the CZ bbox, 18 have a garden:type=community object within 100 m and 85 have any leisure=garden or landuse=allotments (Postpass 2026-09-27) |
| license | none published for the map data; Mapotic terms (https://www.mapotic.com/terms/) state that users "do not acquire any intellectual rights … to any content entered by other users" |
| license_url | https://www.mapotic.com/terms/ |
| license_status | unclear |
| update_freq | continuous (POI last_update dates range from 2017 to 2025) |
| impact | 2 |
| sync_fit | MapRoulette (12 categories, most without an established OSM tag) |
| verified | yes |

## Try it
- **Map preview:** none (licence unclear). Web map: https://www.mapotic.com/kokoza.
- **QGIS:** *Layer → Add Layer → Add Vector Layer*, source type *Protocol: HTTP(S)*, type *GeoJSON*, URI `https://www.mapotic.com/api/v1/maps/61/pois.geojson/` (tested: returns a FeatureCollection with 1,593 points). Filter with `"category" = 327` (community gardens) or `"category" = 329` (community composters).

## Notes
- **Gap:** OSM marks almost none of these as community gardens. 195 of 213 gardens (92 %) have no garden:type=community within 100 m. 128 have no garden or allotment polygon nearby at all. Prague: 68 of 81 missing as community gardens, and 37 of 81 have no garden polygon at all.
- Community composters (97): only 5 have a compost/organic-recycling object within 60 m.
- Only the Komunitní zahrada and Komunitní kompostér categories are useful for OSM. Vermicomposters are mostly in private flats and must not be imported.
- Fields: Mapotic `id` (stable POI id, usable as a reference), `name`, `slug`, `category`, `last_update`. The per-POI detail endpoint (`/maps/61/pois/<id>/`) needs authentication, so address, opening days and access rules are only visible on the web page.
- Gardens are areas and Kokoza has only points. Mappers would need to draw the outline from imagery, so this suits a MapRoulette-style task and not an import.
- **Licence:** ask Kokoza (https://www.kokoza.cz/) for consent to use the community-garden and composter layers in OSM. Mapotic hosts many other Czech NGO maps (the same `pois.geojson` endpoint works for any public map id), which is an open lead for further niche datasets.
- Wiki pages read: Tag:leisure=garden, Key:garden:type.

## Wiki entry
```
===Kokoza – komunitní zahrady a kompostéry===
* dataset: Mapa komunitních zahrad a kompostérů (Mapko)
* gestor: [https://www.kokoza.cz/ Kokoza, o.p.s.]
* licence: neuvedena, nutné vyžádat souhlas
* datové primitivy: body
* odkaz: https://www.mapotic.com/api/v1/maps/61/pois.geojson/
* navržený tag {{tag|leisure|garden}} + {{tag|garden:type|community}}
* poznámka: z 213 komunitních zahrad v datech jich v OSM 195 není označeno jako komunitní zahrada (v Praze 68 z 81)
```
