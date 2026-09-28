# Akce žába (ČSOP) – road sections with amphibian migration

| Field | Value |
|---|---|
| publisher | Český svaz ochránců přírody (ČSOP), campaign "Akce žába"; Mapotic account "Akce Ž.", map id 13712. Linked with the reporting form from https://biodiverzita.csop.cz/chci-se-zapojit/obojzivelnici/ |
| url | https://www.mapotic.com/api/v1/maps/13712/pois.geojson/ (anonymous); metadata https://www.mapotic.com/api/v1/maps/13712/ ; web map https://www.mapotic.com/akce-zaba |
| format | GeoJSON points with `id`, `name` (village or road section), `category_name`, `last_update`. Crowd-sourcing is off (only the owner adds points) |
| coords | yes (one point per road section; no line geometry) |
| records | 679 (678 in CZ): 609 Rizikové úseky silnic (risk sections), 34 Zajišťované úseky silnic (sections with seasonal barriers and volunteer transfers), 33 Dopravní značení (sections with a warning sign), 2 permanent barriers. last_update: 523 in 2022, 155 in 2024–2026 |
| osm_tags | hazard=animal_crossing + hazard:animal=amphibian + seasonal=spring on the road way or a node on it (wiki Tag:hazard=animal_crossing, status approved; Key:hazard:animal lists `amphibian` with the German "Amphibienwanderung" sign). hazard=animal_crossing is defined as a *signed* place, so only the 33 "Dopravní značení" points fit it without discussion |
| osm_count_cz | hazard=animal_crossing 30, hazard:animal=amphibian 0 (local 2026-09-27 Czechia extract; taginfo Geofabrik CZ data until 2026-09-27: hazard=animal_crossing 25, hazard:animal=amphibian 0) |
| license | none stated; Mapotic terms (https://www.mapotic.com/terms/) give other users no rights to content; biodiverzita.csop.cz footer only "© 2026 Chraňme biodiverzitu" |
| license_url | none |
| license_status | unclear |
| update_freq | yearly (new sections added each spring; 89 points updated in 2026) |
| impact | 2 |
| sync_fit | MapRoulette (needs on-site sign verification; only 33 of 679 clearly qualify) |
| verified | yes |

## Try it
- **Map preview:** none (licence unclear). Publisher's map: https://www.mapotic.com/akce-zaba
- **QGIS:** *Layer → Add Layer → Add Vector Layer*, *Protocol: HTTP(S)*, URI
  `https://www.mapotic.com/api/v1/maps/13712/pois.geojson/` (GeoJSON, EPSG:4326). Tested 2026-09-28: 679 points.

## Notes
- **Gap analysis (local match against the 2026-09-27 Czechia extract, Postpass unavailable):** of 678 points in
  CZ, **673 have no OSM object with any `hazard=*` tag within 500 m**; the 3 matches are unrelated hazards
  (median 241 m). The 31 signed sections ("Dopravní značení") without a match are the clearest gap: the
  sign exists on the ground, and OSM has no amphibian hazard anywhere in Czechia.
- Use for routing and navigation apps: seasonal warnings for drivers and cyclists, and a list of places where
  volunteers put up barriers every spring (these barriers are temporary and should not be mapped as barrier=*).
- Data is a point per section, so an import needs a mapper to split the road way at the section ends
  (or tag a node on the road). The 609 unsigned risk sections need a community decision whether
  hazard=animal_crossing (signed places) or a separate tag fits; the 33 signed ones can go in directly after a
  street-level imagery check.
- Stable ID: Mapotic POI `id`. The `name` is only the nearest village.
- Checked and not known: Cs:Česko/freemap, Cs:Zdroje_v_jednani and Sync config.toml contain no ČSOP,
  obojživelníci or hazard source (2026-09-28).
- Contact: ČSOP, campaign Akce žába, via the reporting page https://biodiverzita.csop.cz/chci-se-zapojit/obojzivelnici/.
- Wiki pages read: Tag:hazard=animal_crossing, Key:hazard:animal (no Cs: variants exist).

## Wiki entry
```
===Akce žába – rizikové úseky migrace obojživelníků===
* dataset: Akce žába (mapa Mapotic č. 13712)
* gestor: [https://biodiverzita.csop.cz/chci-se-zapojit/obojzivelnici/ Český svaz ochránců přírody]
* licence: neuvedena, nutno požádat o souhlas
* datové primitivy: body (jeden bod na úsek silnice)
* odkaz: https://www.mapotic.com/api/v1/maps/13712/pois.geojson/
* navržený tag {{tag|hazard|animal_crossing}} + {{tag|hazard:animal|amphibian}} + {{tag|seasonal|spring}}
* poznámka: 678 úseků (33 se značkou), v OSM není v ČR žádný {{tag|hazard:animal|amphibian}} a u 673 úseků není do 500 m žádný hazard
```
