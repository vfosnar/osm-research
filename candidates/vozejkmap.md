# VozejkMap – bezbariérová místa a vyhrazená parkoviště (CZEPA)

| Field | Value |
|---|---|
| publisher | Česká asociace paraplegiků – CZEPA, z.s. (Mapotic map id 1304, `owner_name` in the map metadata; web https://www.vozejkmap.cz/) |
| url | https://www.mapotic.com/api/v1/maps/1304/pois.geojson/ |
| format | GeoJSON FeatureCollection (Mapotic API, no key needed for this endpoint), 7.5 MB |
| coords | yes (WGS84 points) |
| records | 19,499 POIs, 18,132 in the CZ bbox. In the CZ bbox: Parkoviště (disabled parking) 8,178, Banka/bankomat 1,832, Jídlo a pití 1,210, Obchod 913, Instituce 901, Kultura 847, Ubytování 762, Lékaři/lékárny 740, Doprava 595, Čerpací stanice 593, Veřejné WC 577, Sport 321, other 1,043 |
| osm_tags | parking: amenity=parking_space + parking_space=disabled (wiki Tag:parking_space=disabled), or capacity:disabled on the parent car park; toilets: amenity=toilets + wheelchair=yes (wiki Tag:amenity=toilets, Key:wheelchair); other POIs: wheelchair=yes/limited on the existing object (wiki Key:wheelchair) |
| osm_count_cz | parking_space=disabled 4,940; capacity:disabled 10,551; wheelchair=yes 24,325; amenity=toilets 3,315; toilets:wheelchair=yes 240 (taginfo 2026-09-27). Local match against the 2026-09-27 Czechia extract (Postpass unavailable): 5,537 of 8,157 VozejkMap disabled parking spaces inside the CZ border (68 %) have no disabled-parking object within 30 m; 481 of 567 public toilets lack an accessible OSM toilet within 50 m |
| license | none published for the map data; Mapotic terms (https://www.mapotic.com/terms/) give other users no rights to content |
| license_url | https://www.mapotic.com/terms/ |
| license_status | unclear |
| update_freq | continuous; every entry is checked by an administrator who is a wheelchair user (map homepage text). Parking POI last_update: 2018 3,827, 2024 1,471, 2025 1,770, 2026 1,035 |
| impact | 4 |
| verified | yes |

## Try it
- **Map preview:** none (licence unclear). Web map: https://www.vozejkmap.cz/ or https://www.mapotic.com/vozejkmap.
- **QGIS:** *Layer → Add Layer → Add Vector Layer*, source type *Protocol: HTTP(S)*, type *GeoJSON*, URI `https://www.mapotic.com/api/v1/maps/1304/pois.geojson/` (tested 2026-09-27: FeatureCollection of 19,499 points, 7.5 MB). Filter disabled parking with `"category" = 3928`, public toilets with `"category" = 3931`.

## Notes
- **Gap (Prague centre, bbox 14.41,50.07,14.45,50.11, OSM API data fetched 2026-09-28 because Postpass returned 503 all session):**
  - Disabled parking: VozejkMap has 388 spaces; OSM has 126 objects with parking_space=disabled, capacity:disabled or access:disabled=designated in the whole bbox. Only 46 of the 388 VozejkMap spaces have one of those within 30 m, so **342 (88 %) are missing**.
  - Accessible public toilets: 27 in VozejkMap. 18 have an OSM amenity=toilets within 50 m, but only 8 of those carry wheelchair=yes/designated or toilets:wheelchair=yes. 19 of 27 lack the accessibility information.
  - Other POIs (shops, restaurants, offices, 328 in the bbox): 242 have some wheelchair-tagged OSM object within 30 m. In a dense centre that radius is loose, so this category has a smaller and less certain gap than parking.
- **Gap, national (local match against the 2026-09-27 Czechia extract, Postpass unavailable; same rules as the
  Prague check, 17,950 POIs inside the CZ border):**
  - Disabled parking: 8,157 spaces. 2,620 have an OSM object with parking_space=disabled, capacity:disabled or
    access:disabled=designated within 30 m, so **5,537 (68 %) are missing**. The extract reduces car-park ways
    to the mean of their nodes, so a large car park tagged capacity:disabled can sit more than 30 m from its
    reserved spaces; part of the 5,537 is covered that way and the true gap is somewhat smaller.
  - Public toilets (Veřejné WC): 567. 181 have an OSM amenity=toilets within 50 m, 386 (68 %) have none; of the
    181, only 86 carry wheelchair=yes/designated or toilets:wheelchair=yes. So **481 of 567 (85 %)** lack an
    accessible OSM toilet.
  - All other categories (9,226 POIs: banks, food, offices, culture, shops, accommodation…): 2,809 (30 %) have
    an OSM object with a wheelchair tag within 30 m; the other 6,417 have none (for these the shop or office usually
    exists in OSM but without a wheelchair tag, so this counts missing accessibility information, not missing
    objects; the 30 m radius is loose in town centres).
- **National scale:** 8,178 VozejkMap disabled parking spaces in the CZ bbox against 4,940 parking_space=disabled objects in all of OSM Czechia. This is the most valuable layer: each point is a single reserved space (names such as "Parkovací místo ZTP/P", "Vyhrazené parkoviště"), easy to verify on street-level imagery and to map as amenity=parking_space + parking_space=disabled.
- **Attributes:** the anonymous GeoJSON has only `id`, `name`, `slug`, `category`, `last_update`. The per-POI detail endpoint (`/api/v1/maps/1304/pois/<id>/`) returns 401, so the entrance type, toilet and parking attributes the app shows are not available without an agreement. The Mapotic POI `id` is stable and can serve as `ref:vozejkmap`.
- Being in VozejkMap means a wheelchair user considered the place usable, but the exact level (yes vs limited) is only in the detail attributes. With the point data alone, wheelchair tags on shops and restaurants should not be set blind; use the layer as a MapRoulette-style review list. Disabled parking spaces and toilets are safe to use as positions to check.
- The ATM layer (1,832) and fuel stations (593) could feed wheelchair=yes on atm/fuel objects, but these also need the detail attributes.
- **Not known upstream:** VozejkMap does not appear on Cs:Česko/freemap, Cs:Zdroje_v_jednani or in Sync config.toml (grep 2026-09-27), and the OSM wiki full-text search for "vozejkmap" returns nothing.
- **Licence / contact:** Česká asociace paraplegiků – CZEPA, z.s. (https://www.czepa.cz/) runs VozejkMap. Ask for consent to use positions of disabled parking spaces and accessible toilets in OSM, ideally with the detail attributes. An exchange would help them too: OSM already holds 4,940 disabled spaces they could compare against.
- Wiki pages read: Key:wheelchair, Tag:amenity=toilets, Tag:parking_space=disabled.

## Wiki entry
```
===VozejkMap===
* dataset: VozejkMap – bezbariérová místa (mapa Mapotic)
* gestor: [https://www.czepa.cz/ Česká asociace paraplegiků – CZEPA, z.s.]
* licence: neuvedena, nutné vyžádat souhlas
* datové primitivy: body
* odkaz: https://www.mapotic.com/api/v1/maps/1304/pois.geojson/
* navržený tag {{tag|amenity|parking_space}} + {{tag|parking_space|disabled}}, {{tag|wheelchair|yes}}, {{tag|ref:vozejkmap|<id>}}
* poznámka: 8 178 vyhrazených parkovacích míst pro vozíčkáře v Česku; 5 537 z nich (68 %) nemá v OSM do 30 m žádné vyhrazené parkování (v centru Prahy chybí 342 z 388)
```
