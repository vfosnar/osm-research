# Ostrava – Sportoviště, Cyklistické objekty, Cyklostezky (mapy.ostrava.cz opendata)

| Field | Value |
|---|---|
| publisher | Statutární město Ostrava (Magistrát, odbor útvaru hlavního architekta a GIS) |
| url | https://mapy.ostrava.cz/opendata/data/opendata/ (listed in NKOD under publisher 00845451) |
| format | zipped GeoJSON / SHP / GML / DXF in S-JTSK and WGS84; downloaded: https://mapy.ostrava.cz/opendata/data/opendata/sportoviste_WGS84_gjson.zip, cyklo_bod_WGS84_gjson.zip, cyklo_WGS84_gjson.zip |
| coords | yes |
| records | sportoviště 263 points; cyklistické objekty 798 points (103 uzamykatelný stojan, 49 stojan na kola, 2 přístřešky, 2 cyklopumpy, 2 úschovny, 16 odpočívek, 69 orientačních plánů, 26 cyklo-semaforů, 338 virtual bike-share stations); cyklostezky 1,066 line segments (incl. ~130 "projekt" = planned) |
| osm_tags | leisure=pitch / leisure=sports_centre / leisure=playground / leisure=fitness_station; amenity=bicycle_parking (+bicycle_parking, covered); amenity=bicycle_repair_station; highway=cycleway / cycleway=lane / bicycle=designated + foot=designated (+segregated) |
| osm_count_cz | leisure=pitch 33,252; amenity=bicycle_parking 13,650; highway=cycleway 21,260 (taginfo CZ 2026-09-26) |
| license | GIS layers: author work CC BY 4.0 ("SMO"), database as author work CC BY 4.0, sui-generis database right CC BY-SA 4.0 (NKOD terms of use). CSV lists from opendata.ostrava.cz ("Veřejná hřiště", "Hřiště otevřená veřejnosti 20xx") are marked no copyright / no DB protection. |
| license_url | https://creativecommons.org/licenses/by/4.0/ ; https://creativecommons.org/licenses/by-sa/4.0/deed.cs |
| license_status | needs_waiver |
| update_freq | IRREG (sportoviště attributes mention 2019 → stale) |
| impact | 3 |
| sync_fit | Sync for point objects (categories 1:1); MapRoulette for cycle-path lines |
| verified | yes |

## Try it

- **Map preview:** [samples/ostrava-gis-opendata-stojany.geojson](../samples/ostrava-gis-opendata-stojany.geojson): the 154 bike stands from `cyklo_bod` (BOD 11 lockable 103, 16 plain 49, 17 covered 2), pre-tagged `amenity=bicycle_parking`.
- **QGIS:** *Layer → Add Layer → Add Vector Layer… → Source type: File*, paste `/vsizip/vsicurl/https://mapy.ostrava.cz/opendata/data/opendata/cyklo_bod_WGS84_gjson.zip/cyklo_bod_WGS84_gjson.geojson` (the ZIP holds one WGS84 GeoJSON). Sports grounds: the same pattern with `sportoviste_WGS84_gjson`.

## Notes
- OSM in Ostrava bbox (18.10,49.72,18.40,49.90, Postpass 2026-09-27): leisure=pitch 657, leisure=playground 255, amenity=bicycle_parking 283, drinking_water 19, benches 995, street lamps 391 — Ostrava is sparsely mapped for street furniture, but the city does NOT publish benches/trees/lamps; only the three layers above have map value.
- Bike stands (152 points) are the most importable part; bike-share stations (BOD=100, "sdílení kol – …") are virtual zones → skip (operator data belongs to amenity=bicycle_rental only if physical).
- Cyklostezky: POPIS gives type (samostatná cyklostezka, společná stezka pro pěší a cyklisty, cyklistický pruh, protisměr…) + surface quality; useful as a QA layer against OSM highway=cycleway / cycleway=* rather than import (line geometry won't match OSM ways). Drop "- projekt" rows. Text encoding in the cyklostezky WGS84 GeoJSON is mojibake (cp1250 bytes as UTF-8) — needs re-decoding.
- Sportoviště: 263 with NAZEV, ADRESA, TYP, POVRCH, DRUH_SPORT, KOD_POPIS (školní hřiště 49, tělocvična/hala 45, workout 14, discgolf 2…). Attributes last updated ~2019.
- CSV "Veřejná hřiště" (45 rows) and "Hřiště otevřená veřejnosti 2025" (50 rows) are address-only lists of school playgrounds open to the public with opening hours — could add opening_hours/access to existing leisure=pitch, license ok (no copyright).
- BY-SA on the sui-generis right makes a waiver mandatory before any use in OSM.
- Suggested ref: none (OBJECTID not stable).
- Wiki pages read: Tag:leisure=pitch, Tag:amenity=bicycle_parking, Tag:highway=cycleway, Tag:leisure=fitness_station.

## Wiki entry
```
===Ostrava – sportoviště a cyklistická infrastruktura===
* dataset: Sportoviště; Cyklistické objekty; Cyklostezky
* gestor: [https://mapy.ostrava.cz/opendata/ Statutární město Ostrava]
* licence: CC BY 4.0, databáze CC BY-SA 4.0 [https://creativecommons.org/licenses/by-sa/4.0/deed.cs] – nutný souhlas
* datové primitivy: body (sportoviště, stojany), linie (cyklostezky)
* odkaz: https://mapy.ostrava.cz/opendata/data/opendata/cyklo_bod_WGS84_gjson.zip
* navržený tag {{tag|amenity|bicycle_parking}}, {{tag|leisure|pitch}}, {{tag|highway|cycleway}}
* poznámka: Ostrava má v OSM jen ~280 stojanů na kola a málo mobiliáře; město ale mobiliář (lavičky, stromy, lampy) nepublikuje.
```
