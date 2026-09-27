# Letiště Praha – terminal services directory (shops, food, ATMs, fountains, lounges, info desks with terminal and floor)

| Field | Value |
|---|---|
| publisher | Letiště Praha, a. s. (Václav Havel Airport Prague), web www.prg.aero |
| url | https://www.prg.aero/mapa-letiste – the full list is embedded in the page as JSON (`<script data-drupal-selector="drupal-settings-json">` → `services`); detail pages `https://www.prg.aero/<url>` (for example https://www.prg.aero/lekarna-benu) |
| format | JSON inside HTML (Drupal settings); detail pages HTML |
| coords | yes (WGS84 lat/lon, 5–15 decimals, placed inside the terminal on the right spot) |
| records | 249 map points (2026-09-27): terminal 1 = 106, terminal 2 = 130, terminal 3 = 3, landside/none = 10; floor 0 = 12, 1 = 162, 2 = 68, 3 = 6. Top-level categories: Restaurace (4) 60, Obchody (10) 45, Služby (17) 90, Relax (23) 39, Zábava (1455) 40 |
| osm_tags | shop=* / amenity=cafe\|restaurant\|fast_food\|bar\|atm\|bureau_de_change\|pharmacy\|car_rental\|drinking_water\|vending_machine\|lounge\|place_of_worship (+ religion=multifaith)\|luggage_locker, amenity=information → tourism=information + information=office, + level=&lt;floor&gt;, name, opening_hours from the detail page |
| osm_count_cz | airport terminal bbox 14.258,50.097,14.290,50.114 (Postpass 2026-09-27): 313 shop/amenity/tourism features, 92 of them with level; amenity=drinking_water 6, vending_machine 25, atm 18, toilets 12 |
| license | none stated; page footer "© Letiště Praha, a. s." |
| license_url | n/a |
| license_status | unclear |
| update_freq | continuous (web CMS; the list also carries live open/closed status) |
| impact | 2 |
| verified | partial |

## Try it
- **Map preview:** no sample, because no licence is stated (`unclear`).
- **Raw data:** open https://www.prg.aero/mapa-letiste, view the source, find `drupal-settings-json` and read the `services` array. One-liner:
  `curl -sL https://www.prg.aero/mapa-letiste | python3 -c "import re,sys,json;print(json.dumps(json.loads(re.search(r'drupal-settings-json\">(.*?)</script>',sys.stdin.read(),re.S).group(1))['services'],ensure_ascii=False))" > prg.json`
  Each item: `label`, `latitude`, `longitude`, `floor`, `terminal` (25 = T1, 26 = T2, 131 = T3), `categories`, `url`, `open_status`.
- **QGIS:** save the output above as JSON, convert to CSV (or load with *Layer → Add Layer → Add Delimited Text Layer* after flattening), X = `longitude`, Y = `latitude`, CRS EPSG:4326.
- **Web viewer:** https://www.prg.aero/mapa-letiste (Google Maps with terminal/category filters).

## Notes
- **Gap (Postpass 2026-09-27):** the terminals are already reasonably mapped (313 POIs), so this is not a blank area. By name, only 45 of the 165 distinct service names in the airport list have a similarly named OSM feature in the bbox. Missing names include Lékárna BENU, Costa Coffee, Longchamp, Erste Premier Lounge, VISA Lounge, the two prayer rooms (Modlitebna T1/T2), 6 information desks, luggage storage (Úschovna zavazadel), lost and found (Ztráty a nálezy), and several car-rental desks (Avis, Hertz, Czechocar, Rent plus). The airport lists 13 drinking fountains (OSM has 6) and 20 vending machines (OSM 25, placement unknown).
- **What it adds:** a `level` for every point, the terminal, and airside/landside ("Veřejná část") plus opening hours and phone on the detail pages. Only 92 of 313 OSM POIs at the airport have `level`.
- **Level mapping:** `floor` is already zero-based (0 = přízemí prstů B/C, 1 = arrivals/transfer, 2 = T2 departure hall). This matches the OSM convention (Key:level) and the levels already used in OSM there (0/1/2), but check it per terminal before any edit.
- **Noise:** about 40 points cannot be mapped or are art (QR codes, sculptures such as "Pegas" and "Letící muž", piano, Lego model, anamorphic portrait). Filter them out by category 1455 (Zábava) and by name.
- **ZABAGED overlap:** none. ZABAGED has only the airport area (Letiště, Obvod letištní dráhy), not terminal POIs.
- **Stable ID:** none is exposed. `url` (slug) repeats for chains (Relay ×8), so matching would use name + level + position. That fits a one-shot, manually reviewed import better than Sync.
- **Licence / who to ask:** the site has no terms-of-use page (/podminky-uzivani and similar return 404). Ask Letiště Praha, a. s. for permission: https://www.prg.aero/kontakt redirects to the media contacts page https://www.prg.aero/kontakt-pro-media; the site also lists the nonstop info line +420 220 111 888.
- Wiki pages read: Key:level, Tag:amenity=lounge, Tag:amenity=vending_machine, Tag:amenity=drinking_water, Tag:amenity=place_of_worship, Key:changing_table.

## Wiki entry
```
===Letiště Praha – služby v terminálech===
* dataset: Mapa letiště – obchody, restaurace, služby (JSON ve stránce)
* gestor: [https://www.prg.aero/ Letiště Praha, a. s.]
* licence: neuvedena – nutný souhlas [https://www.prg.aero/mapa-letiste]
* datové primitivy: body
* odkaz: https://www.prg.aero/mapa-letiste
* navržený tag {{tag|amenity|drinking_water}}, {{tag|amenity|lounge}}, {{tag|amenity|place_of_worship}} + {{tag|religion|multifaith}}, {{tag|shop|*}} + {{tag|level|<patro>}}
* poznámka: 249 bodů s terminálem a patrem; v OSM chybí asi 120 ze 165 názvů (lékárna, salonky, modlitebny, informace) a jen 92 z 313 POI má level
```
