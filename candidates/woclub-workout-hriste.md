# WOclub / WOblog – map of street workout parks (workout hřiště)

| Field | Value |
|---|---|
| publisher | WOclub (manufacturer of workout equipment; sites woblog.cz and streetworkout.cz, footer "© WOclub", contact info@workoutclub.cz) |
| url | https://www.woblog.cz/hriste (data embedded in the page as the JS array `var wbParks = [...]`); detail pages https://www.woblog.cz/hriste/&lt;slug&gt;; smaller JSON variant on https://streetworkout.cz/hriste (`wbParks = {...}`) |
| format | JavaScript object literal inside HTML (woblog.cz); JSON object inside HTML (streetworkout.cz) |
| coords | yes (lat/lng WGS84 per park) |
| records | woblog.cz 707 parks (7 marked INDOOR in the title; 392 flagged `woclub: "1"` = built by WOclub, 315 by others), fields id, lat, lng, title, street, city, woclub, imageUrl, detailUrl. streetworkout.cz 540 records (527 share the woblog id) with extra fields type OUTDOOR/SCHOOL/INDOOR (435/100/5), year built (`rok`, 183 filled, 2013–2019), manufacturer |
| osm_tags | leisure=fitness_station (+ sport=calisthenics or sport=fitness) as an area or node (wiki Tag:leisure=fitness_station, Key:fitness_station, Cs:Tag:leisure=fitness_station) |
| osm_count_cz | leisure=fitness_station 1,917 (1,000 nodes, 913 ways) (taginfo CZ, data until 2026-09-26) |
| license | none stated ("2026 © WOclub - Made in Czech Republic") |
| license_url | n/a |
| license_status | unclear |
| update_freq | irregular (user and manufacturer submissions; streetworkout.cz years end 2019, woblog.cz has 180 parks not on streetworkout.cz) |
| impact | 3 |
| verified | yes |

## Try it
- **Map preview:** no sample, because the licence is `unclear`.
- **QGIS:** extract the array to CSV (tested: 707 rows):
  ```
  python3 - <<'E'
  import re,csv,urllib.request
  s=urllib.request.urlopen('https://www.woblog.cz/hriste').read().decode()
  b=s[s.find('var wbParks = ['):]; b=b[:b.find('];')]
  w=csv.writer(open('workout.csv','w',newline='')); w.writerow(['id','lat','lng','title','street','city','woclub','url'])
  for m in re.finditer(r'\{\s*id: "(\d+)",\s*position: \{\s*lat: ([-0-9.]+),\s*lng: ([-0-9.]+)\s*\},(.*?)detailUrl: "([^"]*)"',b,re.S):
      f=dict(re.findall(r'(\w+): "([^"]*)"',m.group(4)))
      w.writerow([m.group(1),m.group(2),m.group(3),f.get('title'),f.get('street'),f.get('city'),f.get('woclub'),m.group(5)])
  E
  ```
  then *Layer → Add Layer → Add Delimited Text Layer*, `workout.csv`, delimiter comma, X `lng`, Y `lat`,
  CRS EPSG:4326.
- **Web viewer:** https://www.woblog.cz/hriste (map and list).

## Notes
- **Gap (Postpass, 2026-09-27):** 660 non-indoor parks fall inside the CZ bbox. Only 193 have a
  `leisure=fitness_station` / `sport=fitness|calisthenics|gymnastics` / `fitness_station=*` object within
  100 m, and 249 within 300 m. **467 parks (71 %) have nothing in OSM within 100 m** (297 of them WOclub-built,
  170 by others). Prague alone: 68 parks, 37 missing. Missing examples: Služovice 175, Štěpánovice (Nová 34),
  Příbram (Drásov 11), Miroslav (ul. Komenského), Hrobčice – Červený Újezd, Hrobčice – Mukov.
- **Why it is niche but useful:** outdoor workout parks are free, open 24/7 and sought by runners and
  calisthenics athletes. They are small and hidden in housing estates and school grounds, so OSM misses them.
  The manufacturer's reference list is the most complete national inventory found. Other lists are smaller:
  RVL13's map of built parks (https://www.rvl13.com/mapa-realizovanych-workoutovych-parku-hrist) and
  turistickyatlas.cz (not evaluated).
- **Caveats:**
  - About 100 records (streetworkout.cz type SCHOOL) are on school grounds with limited access; the
    detail text says so ("Přístupnost si musíte ověřit se správou školy"). Map them with `access=customers`
    or `access=private`, or skip them.
  - "Soukromé hřiště" (private) appears in some descriptions.
  - 35 streetworkout.cz records have lat=0.
  - Coordinates are hand-placed pins, so check them against the orthophoto.
  - Equipment lists are only in free text on the detail pages.
- **Suggested ID:** `ref:woblog=<id>` (numeric ids are shared by woblog.cz and streetworkout.cz, so they look
  stable).
- **ZABAGED overlap:** none. ZABAGED_POLOHOPIS (149 layers) has no sports-equipment layer. City open data
  (the Opava and Břeclav ArcGIS layers seen during this round) cover single towns only.
- **Not on the known lists:** not on Cs:Česko/freemap (including Potencionální zdroje), Cs:Zdroje_v_jednani or
  in Sync's config.toml.
- **Licence / contact:** no licence is stated. Ask WOclub (info@workoutclub.cz; editorial address of
  streetworkout.cz redakce@streetworkout.cz) for consent. A manufacturer may welcome OSM presence, and each
  record already links a photo that helps verification.
- Wiki pages read: Tag:leisure=fitness_station, Key:fitness_station, Cs:Tag:leisure=fitness_station.

## Wiki entry
```
===Workoutová hřiště (WOclub / WOblog)===
* dataset: Mapa workoutových hřišť
* gestor: [https://www.woblog.cz/hriste WOclub]
* licence: neuvedena – nutno požádat o souhlas (info@workoutclub.cz)
* datové primitivy: body
* odkaz: https://www.woblog.cz/hriste
* navržený tag {{tag|leisure|fitness_station}} + {{tag|sport|calisthenics}}, {{tag|ref:woblog|<id>}}
* poznámka: ze 660 venkovních hřišť v ČR jich 467 nemá v OSM do 100 m žádné fitness_station; část je ve školních areálech s omezeným přístupem
```
