# Horská služba ČR – stations and mountain webcams (interactive map JSON)

| Field | Value |
|---|---|
| publisher | Horská služba ČR, o.p.s., Špindlerův Mlýn 260 (https://www.horskasluzba.cz/) |
| url | https://www.horskasluzba.cz/data/app/maps-json/hscrmap.json (feed behind https://www.horskasluzba.cz/cz/interaktivni-mapa) |
| format | JSON `{"items":[…]}` with `id`, `category`, `lat`, `lng`, `title`, `htmlContent` (WGS84) |
| coords | yes |
| records | 194 items (2026-09-28): 69 `station` (title with elevation, phone in htmlContent, stable id `station_N`), 83 `webcam` (id `webcam_N`, link to the HS webcam page), 42 `weather` (daily observation reports at stations, not devices) |
| osm_tags | stations: emergency=mountain_rescue + name + operator=Horská služba ČR + phone + ele (wiki Tag:emergency=mountain_rescue); webcams: man_made=surveillance + surveillance:type=camera + contact:webcam (wiki Key:contact:webcam) |
| osm_count_cz | emergency=mountain_rescue 45, contact:webcam 94 distinct values (taginfo 2026-09-28) |
| license | CC BY-SA 4.0 (footer of every horskasluzba.cz page: "This work is licensed under CC BY-SA 4.0") |
| license_url | https://creativecommons.org/licenses/by-sa/4.0/ |
| license_status | needs_waiver |
| update_freq | live (map JSON has a cache-busting version parameter) |
| impact | 2 |
| verified | yes |

## Try it
- **Map preview:** [samples/horska-sluzba-mapa.geojson](../samples/horska-sluzba-mapa.geojson): all 69
  stations (with `in_osm_250m` flag) and 83 webcams, converted to proposed OSM tags.
- **QGIS:** the feed is not GeoJSON. Download it, then in *Plugins → Python Console* run
  `import json,urllib.request;d=json.load(urllib.request.urlopen('https://www.horskasluzba.cz/data/app/maps-json/hscrmap.json'))['items']`
  and write a CSV with `id,category,title,lat,lng`; load it via *Layer → Add Layer → Add Delimited Text
  Layer*, X = `lng`, Y = `lat`, CRS EPSG:4326. Or open the sample GeoJSON above directly.
- **Web:** https://www.horskasluzba.cz/cz/interaktivni-mapa (`?layers=webcam` for webcams).

## Notes
- **Stations gap (local match against the 2026-09-27 Czechia extract, name/operator "Horská služba" or
  emergency=mountain_rescue):** 59 of 69 stations already have an OSM object within 250 m; 10 are
  missing: Český Jiřetín, Vítkovice, Frýdlant nad Ostravicí, Libverda, Bílá, Hynčice pod Sušinou and the
  Krkonoše chalet posts Grohmanova bouda, Černá hora, Labská bouda, Slezský dům. 17 of 78 OSM HS objects
  have no phone. Many OSM names are truncated ("Horská služba Červ.hor.S.", "Rokytnice-Studen."), and
  OSM has HS objects absent from the feed (Stříbrná, Herlíkovice Žalý, Luční bouda, Vysoké nad Jizerou),
  which may be closed stations worth checking.
- **Webcams gap:** 80 of 83 HS webcams have no OSM webcam (contact:webcam or surveillance=webcam) within
  300 m. The GPS in the feed is sometimes the resort, not the exact camera mount; use as a hint layer.
  24 images come from holidayinfo.cz; `contact:webcam` should point to the HS page, not the image.
- **Sync fit:** `station_N` / `webcam_N` ids are stable in the feed; suggested `ref:hscr`. Phones and
  station list change seasonally, which is where sync helps most.
- **Licence:** the site-wide CC BY-SA 4.0 notice covers the page content; ask HS ČR for OSM consent
  (sekretariát, T +420 499 433 230, data box u4zgr6q).
- Wiki pages read: Tag:emergency=mountain_rescue, Key:contact:webcam, Key:surveillance.

## Wiki entry
```
===Horská služba ČR – stanice a webkamery===
* dataset: Interaktivní mapa Horské služby (stanice, webkamery)
* gestor: [https://www.horskasluzba.cz/ Horská služba ČR, o.p.s.]
* licence: CC BY-SA 4.0 [https://creativecommons.org/licenses/by-sa/4.0/]
* datové primitivy: body
* odkaz: https://www.horskasluzba.cz/data/app/maps-json/hscrmap.json
* navržený tag {{tag|emergency|mountain_rescue}} + {{tag|phone}}, {{tag|man_made|surveillance}} + {{tag|surveillance:type|camera}} + {{tag|contact:webcam}}, {{tag|ref:hscr|<id>}}
* poznámka: 10 z 69 stanic HS v OSM chybí a 80 z 83 horských webkamer HS v OSM není; nutný souhlas (CC BY-SA)
```
