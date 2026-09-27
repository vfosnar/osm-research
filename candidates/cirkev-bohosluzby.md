# Katolické bohoslužby v ČR (bohosluzby.cirkev.cz) – mass times, accessibility and contacts for Catholic churches

| Field | Value |
|---|---|
| publisher | Česká biskupská konference (portal cirkev.cz), data entered by all Czech dioceses; contact bohosluzby@cirkev.cz |
| url | https://bohosluzby.cirkev.cz/apiWeb/detail?id=&lt;church id&gt; (JSON detail); https://bohosluzby.cirkev.cz/apiWeb/getChurches?church_id=false&offset=0&latitude=&lt;lat&gt;&longitude=&lt;lon&gt; (nearest churches with upcoming services, 5 per call) |
| format | undocumented JSON API behind the web app (jQuery endpoints `apiWeb/*`) |
| coords | yes (WGS84 `latitude`/`longitude`; some records 0,0) |
| records | not measured: IDs are non-sequential per diocese (10009, 7000995485767, 50001914111036) and there is no list endpoint; `apiWeb/markers` (bbox) returns "SQL template 'markers' not found" and `apiWeb/allData` returns only 3 records without coordinates (2026-09-27) |
| osm_tags | on the existing `amenity=place_of_worship` object: `service_times=*` (from `regular`), `wheelchair=yes` (from `barrier_free=1`), `website`, `phone`, `email`; suggested `ref:bohosluzby=<id>` (unused in CZ) |
| osm_count_cz | taginfo 2026-09-27: amenity=place_of_worship 11,484; denomination=roman_catholic 5,750; service_times 228; ref:bohosluzby 0 |
| license | none stated on bohosluzby.cirkev.cz or cirkev.cz |
| license_url | – |
| license_status | unclear |
| update_freq | continuous (records `updated_at` 2026-06 and 2026-08 in Olomouc sample) |
| impact | 3 |
| verified | partial |

## Try it
- **Map preview:** none, licence unclear.
- **Browser / curl:** open `https://bohosluzby.cirkev.cz/apiWeb/detail?id=7000995485767` (farní kostel sv. Mořice, Olomouc). The JSON has `institution` (name, dedication, coordinates, `barrier_free`, phone, email, www, parish, `mapycz_id`, `updated_at`) and `regular` (one row per recurring service: `den` weekdays, `cas` time, language, `poznamka` note such as "školní rok, kromě července a srpna"), plus `extra` (one-off services).
- **Nearby search:** `https://bohosluzby.cirkev.cz/apiWeb/getChurches?church_id=false&offset=0&latitude=49.5946&longitude=17.2508` returns `church_ids` of the 5 nearest churches with upcoming services.
- **QGIS:** not a GIS service; convert the detail JSON with a script first.
- **Web viewer:** https://bohosluzby.cirkev.cz/ (also the mobile app Bohoslužby.Církev.cz).

## Notes
- **What it adds:** OSM has almost all Catholic churches already; what is missing is `service_times`
  (228 objects in CZ against 5,750 roman_catholic places of worship). This is the only national
  source of mass times, kept up to date by the dioceses themselves, with a stable numeric id per church.
- **Gap, measured (Olomouc old town, bbox 17.248,49.592,17.264,49.600, OSM API 2026-09-27):** 16
  `amenity=place_of_worship` objects, only 1 with `service_times`. The 5 churches returned by the
  API for that spot (Neposkvrněné Početí P. M. – Dominikáni, sv. Anna, sv. Mořic, P. M. Sněžná,
  sv. Michal) all exist in OSM; 4 of 5 have no `service_times`.
- **Quality check:** for the Dominican church OSM has `Su 09:30, 18:00; Mo-Fr 06:00, 18:00; Sa 18:00`;
  the API has ne 09:30, po–ne 18:00, po–pá 06:00 ("školní rok, kromě července a srpna") and čt 18:00
  latinsky. The data match and the API is more detailed (seasonal note, language).
- **Do not take the coordinates.** Records carry a `mapycz_id`, so positions were probably picked on
  Mapy.com (proprietary). Use the data only to add attributes to existing OSM churches, matching by
  name + distance, and store the id in `ref:bohosluzby`.
- **Conversion:** `regular.den` is Czech weekday abbreviations (po út st čt pá so ne) and `cas` HH:MM;
  it maps directly to the `service_times` syntax, which follows `opening_hours`. Seasonal notes need
  manual review.
- **Access:** there is no list endpoint; a full harvest needs the ids. The `getChurches` nearest-search
  over a grid of points would enumerate them, or ask the operator for an export (Matěj Cepl received a
  full list with coordinates and ids from the same server in 2016, talk-cz 2016-11-21, "Seznam všech
  katolických kostelů s bohoslužbami s UUIDs"; the linked file is now 404 and nothing was imported).
- **Licence:** no terms found on bohosluzby.cirkev.cz or cirkev.cz. Service times are facts, but the
  database right applies; ask Česká biskupská konference (bohosluzby@cirkev.cz) for consent covering
  `service_times`, `wheelchair` and contact tags.
- Wiki pages read: Tag:amenity=place_of_worship (lists `service_times`), Key:service_times,
  Cs:Tag:amenity=place_of_worship.

## Wiki entry
```
===Katolické bohoslužby v ČR===
* dataset: Katolické bohoslužby v České republice (bohosluzby.cirkev.cz)
* gestor: [https://www.cirkev.cz Česká biskupská konference]
* licence: neuvedena, nutno požádat o souhlas (bohosluzby@cirkev.cz)
* datové primitivy: body
* odkaz: https://bohosluzby.cirkev.cz/apiWeb/detail?id=7000995485767
* navržený tag {{tag|service_times|<časy bohoslužeb>}}, {{tag|wheelchair|yes}}, {{tag|ref:bohosluzby|<id>}}
* poznámka: v OSM má service_times jen 228 míst ze 5 750 katolických kostelů; data diecézí jsou aktuální, souřadnice nepřebírat (Mapy.com)
```
