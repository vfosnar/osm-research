```
name: ČHMÚ – vodoměrné stanice (surface-water gauging stations with flood-stage thresholds)
publisher: Český hydrometeorologický ústav (ČHMÚ), IČO 00020699
url: https://opendata.chmi.cz/hydrology/now/metadata/meta1.json (545 stations with SPA flood stages); https://opendata.chmi.cz/hydrology/now/metadata/meta3.json (563 stations, full attributes); NKOD: https://data.gov.cz/zdroj/datové-sady/00020699/ecaee834f853b3a92bc304573d8225c0 and GIS layer https://data.gov.cz/zdroj/datové-sady/00020699/7926920934cf3270f9c133b9317a31e6 (https://opendata.chmi.cz/hydrology/product/data/gis_layer/)
format: JSON (header + values arrays)
coords: yes (GEOGR1 lat, GEOGR2 lon, WGS84, 7 decimals)
records: 563 stations in meta3 (categories A 211, B 181, C 169). Operators: ČHMÚ branches 433, Povodí s.p. about 80, municipalities and others.
osm_tags: man_made=monitoring_station + monitoring:water_level=yes (+ monitoring:flow_rate=yes where Q is measured) + name=<STATION_NAME> + operator=<PROVOZOVATEL> + ref=<DBC>; optionally website=<WWW_CHMI>
osm_count_cz: man_made=monitoring_station 1,540 (mostly weather/air); monitoring:water_level=yes 82; operator="Český hydrometeorologický ústav" 96 (Geofabrik taginfo 2026-09-27)
license: CC BY 4.0 (NKOD terms: copyrighted work and database under CC BY 4.0, author ČHMÚ)
license_url: https://creativecommons.org/licenses/by/4.0/
license_status: needs_waiver
update_freq: metadata refreshed daily (file timestamps); network changes rarely
impact: 3
verified: yes
```

## Notes
- Postpass check: of 545 stations in meta1, only 39 have any man_made=monitoring_station within 150 m, and 33 have monitoring:water_level=yes. About 93% are missing.
- Each station has a stable DBC number (e.g. 001000 Špindlerův Mlýn), stream name, elevation, river km, basin area, and three flood-activity thresholds (SPA 1/2/3 in cm and m³/s). These gauges are what "stupeň povodňové aktivity" warnings refer to, so they are highly relevant to users.
- Weather stations (ČHMÚ) are already covered through ZABAGED POI. These hydrological gauges are a separate network. ZABAGED may contain a "vodočet" or "limnigraf" point, but not the IDs or thresholds. Check for overlap with the ZABAGED layer before importing.
- Licence: CC BY 4.0, so a waiver or explicit consent from ČHMÚ is needed (OSM LWG position). ČHMÚ is a state body used to giving consent (ČÚZK precedent).
- Related, not verified in depth: groundwater observation wells (https://opendata.chmi.cz/hydrology/groundwater/now/, CC BY 4.0) could map to man_made=monitoring_station + monitoring:groundwater=yes (not checked on wiki).
- Wiki pages read: Tag:man_made=monitoring_station (lists monitoring:water_level), Key:monitoring:water_level (de facto; combination name, ref, operator; subkey monitoring:water_level:zero).

## Wiki entry
```
===Vodoměrné stanice ČHMÚ===
* dataset: Množství povrchových vod – údaje – now (metadata stanic)
* gestor: [https://www.chmi.cz/ Český hydrometeorologický ústav]
* licence: CC BY 4.0 [https://creativecommons.org/licenses/by/4.0/] – nutný souhlas
* datové primitivy: body
* odkaz: https://opendata.chmi.cz/hydrology/now/metadata/meta3.json
* navržený tag {{tag|man_made|monitoring_station}}, {{tag|monitoring:water_level|yes}}, {{tag|ref|<DBC>}}
* poznámka: 563 vodoměrných stanic se stupni povodňové aktivity, v OSM je v jejich okolí (150 m) jen ~7 %
```
