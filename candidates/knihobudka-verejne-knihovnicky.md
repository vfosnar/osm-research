# KnihoBudka – map of public bookcases (knihobudky a knihovničky)

| Field | Value |
|---|---|
| publisher | KnihoBudka (non-profit project, https://www.knihobudka.cz/), contact knihobudka@gmail.com |
| url | https://www.knihobudka.cz/csvgo.php (JSON array behind the map at https://www.knihobudka.cz/#mapa) |
| format | JSON array of rows `[lat, lon, obec, adresa/popis, skupina]` (header row first) |
| coords | yes (WGS84, 1,523 of 1,538 rows with 7 decimals) |
| records | 1,538 bookcases with coordinates: 129 in group 1 (KnihoBudky built by the project, mostly converted phone booths), 1,409 in group 2 (other bookcases reported to the project); 14 duplicate coordinate pairs |
| osm_tags | amenity=public_bookcase; operator=KnihoBudka for group 1 (wiki Tag:amenity=public_bookcase) |
| osm_count_cz | amenity=public_bookcase 1,072 (taginfo 2026-09-26); 650 of the 1,538 dataset points have one within 50 m, 689 within 150 m (Postpass 2026-09-27) |
| license | none stated (site footer "KnihoBudka©2025") |
| license_url | |
| license_status | unclear |
| update_freq | continuous (crowd-reported, maintained by the project) |
| impact | 3 |
| verified | yes |

## Try it
- **Map preview:** none (licence unclear). The project's own Leaflet map is at https://www.knihobudka.cz/#mapa.
- **QGIS:** the endpoint is a plain JSON array, so convert it first:
  `curl -sS https://www.knihobudka.cz/csvgo.php | jq -r '.[] | select(.[4]=="1" or .[4]=="2") | [.[0],.[1],.[2],.[3],.[4]] | @csv' > knihobudka.csv`
  (tested: 1,540 rows). Then *Layer → Add Layer → Add Delimited Text Layer*, file `knihobudka.csv`, *CSV*, no header, X field = field_2, Y field = field_1, CRS EPSG:4326.

## Notes
- **Gap:** about 850 of 1,538 bookcases (55 %) have no amenity=public_bookcase within 150 m. Prague: 93 of 181 missing (50 m radius). Brno: 23 of 35 missing. Ostrava: 11 of 17 missing. For group 1 (the project's own booths) 33 of 129 are missing.
- The dataset has more bookcases than OSM has in the whole country (1,538 against 1,072).
- There is no ID field. The row index is not stable, so a sync would have to match by position. The text field mixes address and description ("autobusová zastávka Albrechtice nad Vltavou"). Keep it as a hint for mappers (it is not a `name`).
- Positions come from reporters, so some are approximate. Group 2 is best treated as a review list for mappers, and a machine import is not recommended.
- **Licence:** there is no licence or terms of use on the site. Ask the project (knihobudka@gmail.com) for ODbL-compatible consent for the map data, or for permission to use it as a mapping reference.
- Mini.knihovna.cz keeps a smaller Google My Maps layer (28 placemarks, KML via `https://www.google.com/maps/d/kml?mid=1WPEpLJ9tX8weQ1hFYEw8FNcX2tg&forcekml=1`). It is too small to be worth a separate entry.
- Wiki pages read: Tag:amenity=public_bookcase.

## Wiki entry
```
===KnihoBudka – veřejné knihovničky===
* dataset: mapa knihobudek a knihovniček
* gestor: [https://www.knihobudka.cz/ KnihoBudka]
* licence: neuvedena, nutné vyžádat souhlas (knihobudka@gmail.com)
* datové primitivy: body
* odkaz: https://www.knihobudka.cz/csvgo.php
* navržený tag {{tag|amenity|public_bookcase}}, {{tag|operator|KnihoBudka}} (u vlastních budek projektu)
* poznámka: z 1 538 knihovniček v datech jich asi 850 v OSM chybí (v Praze 93 ze 181); data nemají stabilní ID
```
