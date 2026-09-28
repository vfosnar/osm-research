# WC kompas – veřejné toalety a toalety na Euroklíč (Pacienti IBD)

| Field | Value |
|---|---|
| publisher | Pacienti IBD z.s. (Mapotic map id 10, owner account "Pacienti IBD"; web https://www.wckompas.cz/) |
| url | https://www.mapotic.com/api/v1/maps/10/pois.geojson/ |
| format | GeoJSON FeatureCollection (Mapotic API, no key needed for this endpoint), 5.3 MB |
| coords | yes (WGS84 points) |
| records | 14,479 POIs, 13,943 in the CZ bbox. In the CZ bbox: Veřejné WC 1,339, Euroklíč 415, Ostatní 11,453, Restaurace 308, Policie ČR 210, Úřad 140, Zdravotnické zařízení 78 |
| osm_tags | amenity=toilets (wiki Tag:amenity=toilets); Euroklíč toilets add centralkey=eurokey (wiki Key:centralkey) and usually wheelchair=yes |
| osm_count_cz | amenity=toilets 3,315; centralkey=eurokey 25 (taginfo 2026-09-27) |
| license | none published for the map data; Mapotic terms (https://www.mapotic.com/terms/) give other users no rights to content |
| license_url | https://www.mapotic.com/terms/ |
| license_status | unclear |
| update_freq | crowdsourced, anyone can add and rate toilets (map homepage). POI last_update: 2021 622, 2024 156, 2025 114, 2026 187 (most records are older) |
| impact | 3 |
| verified | yes |

## Try it
- **Map preview:** none (licence unclear). Web map: https://www.wckompas.cz/ or https://www.mapotic.com/wckompas.
- **QGIS:** *Layer → Add Layer → Add Vector Layer*, source type *Protocol: HTTP(S)*, type *GeoJSON*, URI `https://www.mapotic.com/api/v1/maps/10/pois.geojson/` (tested 2026-09-27: FeatureCollection of 14,479 points). Filter with `"category" IN (115, 116)` for public and Euroklíč toilets.

## Notes
- **Which records are useful:** only *Veřejné WC* (category 115) and *Euroklíč* (116). *Ostatní* (11,453) and the Restaurace/Úřad/Policie categories are places that let holders of the IBD patients' "WC karta" use a staff toilet (sampled names: municipal offices such as "Břežany – obecní úřad", tennis halls, vehicle inspection stations). They are not public toilets and must not become amenity=toilets; at most toilets=customers on the existing object after checking.
- **Gap (Prague centre, bbox 14.41,50.07,14.45,50.11, OSM API data fetched 2026-09-28; Postpass returned 503 all session):** 97 WC kompas public + Euroklíč toilets. 52 have an OSM amenity=toilets within 50 m, **45 (46 %) have none**. Of 6 Euroklíč toilets, 2 have any OSM toilet nearby and none has centralkey.
- **Eurokey is the clearest gap:** 415 Euroklíč toilets in the CZ bbox against 25 centralkey=eurokey objects in OSM Czechia. A second Mapotic map, "Euroklíč" (id 3964, 316 toilets and 19 platforms, static since 2019, private owner), covers the same topic and can be used for cross-checking.
- National: 1,339 + 415 = 1,754 toilets in the CZ bbox vs 3,315 amenity=toilets in OSM Czechia. Many will already be mapped (the Prague sample suggests about half), so this is a conflation list, not an import.
- Positions are crowdsourced and many records have not been touched since 2021; closed toilets are likely. The Mapotic POI `id` is stable; the per-POI detail endpoint returns 401, so opening hours and fees are not anonymous.
- **Not known upstream:** not on Cs:Česko/freemap, Cs:Zdroje_v_jednani or in Sync config.toml (grep 2026-09-27); OSM wiki full-text search for "wc kompas" returns nothing. Prague public toilets from Golemio are a separate candidate (`prague-verejne-toalety.md`); WC kompas adds the rest of the country and the Euroklíč layer.
- **Licence / contact:** Pacienti IBD z.s. (the IBD patients' association that issues the WC karta). Ask for consent for the Veřejné WC and Euroklíč layers only.
- Wiki pages read: Tag:amenity=toilets, Key:centralkey, Key:wheelchair.

## Wiki entry
```
===WC kompas===
* dataset: WC kompas – online mapa veřejných toalet (mapa Mapotic)
* gestor: [https://www.wckompas.cz/ Pacienti IBD z.s.]
* licence: neuvedena, nutné vyžádat souhlas
* datové primitivy: body
* odkaz: https://www.mapotic.com/api/v1/maps/10/pois.geojson/
* navržený tag {{tag|amenity|toilets}}, u toalet na Euroklíč {{tag|centralkey|eurokey}}
* poznámka: 415 toalet na Euroklíč v Česku proti 25 objektům s centralkey=eurokey v OSM; v centru Prahy chybí 45 z 97 veřejných toalet
```
