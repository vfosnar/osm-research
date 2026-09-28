# Asociace provozovatelů kin (APK / kinari.cz) – member cinemas map

| Field | Value |
|---|---|
| publisher | Asociace provozovatelů kin, z.s. (https://www.kinari.cz/o-nas/) |
| url | https://www.kinari.cz/clenove/ (section "Mapa členských kin"; markers inline as `cspm_new_pin_object(map_id, {...})` JSON); detail pages https://www.kinari.cz/pobocka/&lt;slug&gt;/ |
| format | HTML with embedded JSON (WordPress "Progress Map" plugin) |
| coords | yes (WGS84) |
| records | 233 member cinemas (233 distinct WordPress post_id), 10 of them summer cinemas (slug `letni-kino-*`); fields: post_id, lat, lng, address, detail link |
| osm_tags | amenity=cinema + name; open_air=yes for summer cinemas; screen=&lt;n&gt; only if known (Tag:amenity=cinema, Key:screen – the key is `screen`, not `screens`) |
| osm_count_cz | amenity=cinema 414 (taginfo CZ, data until 2026-09-27); screen 44; cinema:type=open_air 1 |
| license | none stated |
| license_url | – |
| license_status | unclear |
| update_freq | when membership changes (detail pages dated 2024) |
| impact | 2 |
| sync_fit | Sync (points, 1:1 to amenity=cinema, post_id as ref) |
| verified | yes |

## Try it
- **Map preview:** none (licence unclear).
- **QGIS:** no direct service. Save https://www.kinari.cz/clenove/, extract the JSON objects passed to
  `cspm_new_pin_object(map_id, …)` (keys `post_id`, `coordinates.lat`, `coordinates.lng`,
  `coordinates.address`, `media.link`) into CSV, then *Layer → Add Layer → Add Delimited Text Layer*,
  X = lng, Y = lat, CRS EPSG:4326.
- **Web:** https://www.kinari.cz/clenove/#mapa-clenskych-kin

## Notes
- **Gap (Postpass, 2026-09-28):** 586 amenity=cinema / cinema:type objects in the CZ bbox. 176 of the 233
  APK cinemas have an OSM cinema within 200 m; **57 have none** (nearest OSM cinema 0.26–19 km away).
  Most are small-town single-screen cinemas: Rumburk, Šternberk, Králíky (Klub Na Střelnici), Trhové Sviny,
  Protivín, Vítkov, Moravský Beroun, Staré Město (Kino Sněžník), Kuřim, Měnín, Krumsín, KD Liteň. A few are
  city cinemas whose OSM node is further than 200 m or missing (Kino Varšava Liberec, CineStar Mladá
  Boleslav, Kino Jednička Ostrava). Spot-check needed; some APK points are geocoded addresses.
- The APK list is members only, so it is not a full cinema register. It is the best freely viewable list
  of small and municipal cinemas, which are the ones missing in OSM. Screens and seat counts are not in
  the data.
- **Suggested ref:** `ref:kinari=<post_id>` (WordPress post id, stable while the page exists), or keep only
  `website`.
- **Rejected alternatives checked in this round:** Institut umění – Divadelní ústav open data
  (`https://opendata.idu.cz/data/adresare.csv`, CC BY 4.0): 1,004 SCENA records but only 119 current Czech
  ones with any address, no coordinates, stale phone numbers; adresar.divadlo.cz (688 theatres and
  ensembles, address only, "Všechna práva vyhrazena"). Unie filmových distributorů has only a multiplex
  overview. The AMG museum directory (https://www.cz-museums.cz/adresar/) states the sui generis database
  right and forbids copying.
- **Known check:** not on Cs:Česko/freemap, Cs:Zdroje_v_jednani or in Sync config.toml.
- **Contact:** Asociace provozovatelů kin, z.s. (board listed on https://www.kinari.cz/o-nas/, chairman Dan
  Krátký, Hodonín).
- Wiki pages read: Tag:amenity=cinema, Key:screen.

## Wiki entry
```
===Asociace provozovatelů kin – mapa členských kin===
* dataset: Mapa členských kin
* gestor: [https://www.kinari.cz/ Asociace provozovatelů kin, z.s.]
* licence: neuvedena, nutné vyjednat souhlas
* datové primitivy: body
* odkaz: https://www.kinari.cz/clenove/
* navržený tag {{tag|amenity|cinema}}, {{tag|open_air|yes}} (letní kina), {{tag|ref:kinari|<post_id>}}
* poznámka: 57 z 233 členských kin (hlavně malá městská kina) nemá v OSM do 200 m žádné amenity=cinema
```
