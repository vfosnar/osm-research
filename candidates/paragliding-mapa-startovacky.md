# Paragliding Mapa – paragliding launch sites (startovačky), landings and parking

| Field | Value |
|---|---|
| publisher | Paragliding Mapa (paragliding-mapa.cz, community site run by ifire.cz; footer "© ifire 2026", contact info@paragliding-mapa.cz) |
| url | https://www.paragliding-mapa.cz/api/v0.1/launch?country=cz&locale=cs (JSON API, documented at https://www.paragliding-mapa.cz/api/help); web list https://www.paragliding-mapa.cz/startovacky |
| format | JSON (`{status, data:[…]}`), no auth |
| coords | yes (WGS84 lat/lon per launch, landing and parking) |
| records | 234 launch sites in CZ (fetched 2026-09-28): flying_status 1 official paid 38, 2 official free 22, 3 tolerated 99, 4 forbidden 19, 5 not stated 56; `active` true 195. Nested: 67 landing fields (`landings`), 49 parking places (`parkings`). Per launch: stable numeric `id`, name, altitude, superelevation, wind_usable_from/to and wind_optimal_from/to (degrees), ramp, windsock, toilet, restaurant, water, taxes (fee text), management (operator URL, 53 filled), rules (link to site rules, 49), air_traffic, access, limitations |
| osm_tags | sport=free_flying + free_flying:takeoff=yes (landings: free_flying:landing=yes), free_flying:paragliding=yes, free_flying:official=yes/no, direction=&lt;from&gt;-&lt;to&gt; (degree range), direction:ideal, ele, fee, website, name (wiki Tag:sport=free_flying; free_flying:site=* is marked deprecated there). Parking: amenity=parking |
| osm_count_cz | sport=free_flying 43, free_flying:site=takeoff 14, free_flying:site=landing 4, free_flying:takeoff 0 (taginfo CZ 2026-09-28). Local match against the 2026-09-27 Czechia extract: 24 of 234 launch sites have any free_flying feature within 500 m; 63 of 67 landings have none |
| license | none stated ("© ifire 2026") |
| license_url | n/a |
| license_status | unclear |
| update_freq | continuous (user-edited site; API marked beta; pages show latest XContest launch date) |
| impact | 4 |
| verified | yes |

## Try it
- **Map preview:** no sample, because the licence is `unclear`. The licensed alternative
  [paraglidingearth-cz](paraglidingearth-cz.md) has a sample covering the same sites.
- **QGIS:** the API returns plain JSON, not GeoJSON. Convert it to CSV (tested: 234 rows), then
  *Layer → Add Layer → Add Delimited Text Layer*, delimiter comma, X field `longitude`, Y field
  `latitude`, CRS EPSG:4326:
  ```
  python3 - <<'E'
  import json,csv,urllib.request
  d=json.load(urllib.request.urlopen('https://www.paragliding-mapa.cz/api/v0.1/launch?country=cz&locale=cs'))['data']
  w=csv.writer(open('startovacky.csv','w',newline=''))
  w.writerow(['id','name','latitude','longitude','altitude','flying_status','active','wind_from','wind_to','windsock','url'])
  for p in d: w.writerow([p['id'],p['name'],p['latitude'],p['longitude'],p['altitude'],p['flying_status'],p['active'],p['wind_usable_from'],p['wind_usable_to'],p['windsock'],p['url']])
  E
  ```
- **Web:** map https://www.paragliding-mapa.cz/mapa, list https://www.paragliding-mapa.cz/startovacky

## Notes
- **Gap:** OSM in Czechia has 43 `sport=free_flying` objects in total. In the local match against the
  2026-09-27 Czechia extract, only 24 of the 234 launch sites and 4 of the 67 landing fields have any
  free-flying feature within 500 m. Of the 144 active sites that are official or tolerated
  (status 1–3), 22 are in OSM. In Krkonoše (bbox 15.4,50.55,16.0,50.8), 1 of 9 launch sites is mapped.
- **Why it matters:** launch and landing fields are small meadows or ridge clearings that are hard to
  identify from imagery. Hikers and outdoor apps (OsmAnd, OpenTopoMap) show `sport=free_flying`.
  The status field says which sites are forbidden (Všetaty/Cecemín carries a municipal ban). Those sites
  should be skipped, or mapped as `free_flying:takeoff=no` only where that helps.
- **Attributes that map directly to wiki tags:** wind_usable_from/to becomes `direction=205-245`
  (Key:direction allows degree ranges; Tag:sport=free_flying says `direction` is the usable wind
  direction). wind_optimal becomes `direction:ideal`. altitude becomes `ele`. flying_status 1/2 becomes
  `free_flying:official=yes`, and taxes becomes `fee`. management becomes `website`/`operator`.
- **Suggested ID:** `ref:paragliding-mapa=<id>` (not in use yet; the community should decide). The
  numeric id is stable and appears in the page URLs.
- **Overlap:** 117 of the 234 sites have a paraglidingearth.com site within 500 m. Paragliding Mapa has
  more CZ sites, plus official/tolerated/forbidden status, landings and parking.
- **Licence:** no licence or terms on the site. It is a single-maintainer hobby project that credits OSM
  as a basemap. Contact info@paragliding-mapa.cz (ifire.cz) and ask for ODbL/CC0 or an OSM consent. The
  LAA ČR Svaz paraglidingu (https://www.laacr.cz/svazy/svaz-pg/), which runs the Fond podpory
  startovišť, is a possible co-signatory for the "official" list.
- **LAA ČR Svaz PG list (checked 2026-09-28):** the page
  https://www.laacr.cz/svazy/svaz-pg/podpora/fond-podpory-startovist/seznam-startovist/ is not a full
  register. It names the 13 launch sites supported by the Fond podpory startovišť (Černá hora, Kozákov,
  Javorový [sjezdovka], Krupka, Raná, Skalka, Svatobor, Doubrava, Zvičina, Javorový [západ], Velký
  Javorník, Kamenec, Jeviněves) with the club contact for each, and 19 LAA wind stations ("sondy") with
  their operator and live-data URL. It has no coordinates and no licence. A supported site must have a
  windsock and an information board, so the 13 names can confirm `free_flying:official=yes` and
  `operator=<club>` on the matching Paragliding Mapa points. The wind stations could become
  `man_made=monitoring_station` + `monitoring:weather=yes` + `website`, positioned by survey or from the
  station pages. Nothing here needs an import; facts like these (names, operators) can be used as a
  cross-check.
- Wiki pages read: Tag:sport=free_flying, Key:direction, Tag:man_made=monitoring_station.

## Wiki entry
```
===Paragliding Mapa – startoviště a přistávací plochy===
* dataset: Startovačky, přistávačky, parkování (API v0.1)
* gestor: [https://www.paragliding-mapa.cz/ Paragliding Mapa (ifire.cz)]
* licence: neuvedena (© ifire), nutný souhlas – info@paragliding-mapa.cz
* datové primitivy: body
* odkaz: https://www.paragliding-mapa.cz/api/v0.1/launch?country=cz&locale=cs
* navržený tag {{tag|sport|free_flying}} + {{tag|free_flying:takeoff|yes}} / {{tag|free_flying:landing|yes}}, {{tag|direction|<od>-<do>}}, {{tag|free_flying:official|yes}}, {{tag|ref:paragliding-mapa|<id>}}
* poznámka: z 234 startovišť v ČR je v OSM (do 500 m) jen 24 a z 67 přistávacích ploch 4; data mají i stav (oficiální/tolerované/zakázané) a směry větru
```
