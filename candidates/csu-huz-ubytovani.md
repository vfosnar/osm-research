# ČSÚ – Hromadná ubytovací zařízení (adresní body): hotels, guest houses, hostels, campsites

| Field | Value |
|---|---|
| publisher | Český statistický úřad (ČSÚ), IČO 00025593; contact point in NKOD: Ing. Petr Klauda, petr.klauda@czso.cz |
| url | https://geodata.csu.gov.cz/server/rest/services/Hosted/HUZ/FeatureServer/0 (current, 10,454 records, lastEditDate 2026-06-05); snapshot https://geodata.csu.gov.cz/as/data/distribuce/Hosted/HUZ/FeatureServer/0/geojson.zip (HUZ_20250601.geojson, 10,652 records, Last-Modified 2025-07-09; also shp.zip, gpkg.zip, gdb.zip). NKOD record: https://data.gov.cz/zdroj/datové-sady/00025593/33c18c263706082c2f47bc89119260d8 |
| format | ArcGIS FeatureServer (f=geojson, outSR=4326 supported); zipped GeoJSON/SHP/GPKG/GDB |
| coords | yes (point on the RÚIAN address point; median 9 m from the RÚIAN address point, a few points several km off) |
| records | 10,454: Penzion 4,297; Ostatní HUZ 1,575; Hotel \*\*\* 1,556; Hotel \*\*\*\* 890; Turistická ubytovna 712; Kemp 575; Chatová osada 280; Hotel \*\* 208; Hotel garni 167; Hotel \* 117; Hotel \*\*\*\*\* 77. Fields: pagina (ČSÚ establishment id, unique), nazev_uz, kat/kateg, address (obec, část obce, ulice, č.p./č.o., PSČ), idruian (RÚIAN address-point code, 10,085 filled), pocpok (rooms band), pocluz (beds band), pocmis (pitches band), sezona |
| osm_tags | tourism=hotel (+ stars=1–5), tourism=guest_house, tourism=hostel, tourism=camp_site, tourism=chalet; proposed ref:csu:huz=&lt;pagina&gt; |
| osm_count_cz | tourism=hotel 3,478; guest_house 3,654; hostel 476; camp_site 1,160; chalet 762; apartment 715; motel 115; stars 799; ref:csu\* 0 (taginfo 2026-09-27). Local match against the 2026-09-27 Czechia extract (Postpass unavailable): 4,693 of 10,454 establishments (45 %) have no OSM accommodation within 100 m; no OSM accommodation object carries a ČSÚ-like key (csu/czso/huz) or a `ref*` value equal to a `pagina` |
| license | CC0 (NKOD distribution terms); the NKOD terms also state "není autorskoprávně chráněnou databází" and "není chráněna zvláštním právem pořizovatele databáze" |
| license_url | https://data.gov.cz/zdroj/datové-sady/00025593/33c18c263706082c2f47bc89119260d8 ; http://publications.europa.eu/resource/authority/licence/CC0 |
| license_status | ok |
| update_freq | twice a year (NKOD accrualPeriodicity ANNUAL_2) |
| impact | 4 |
| verified | yes |

## Try it
- **Map preview:** [samples/csu-huz-ubytovani.geojson](../samples/csu-huz-ubytovani.geojson): all 171 establishments in Pec pod Sněžkou with the ČSÚ category, the proposed `tourism` value, rooms/beds bands, season and `osm_accommodation_within_100m` (count of OSM `tourism` accommodation objects within 100 m; 0 = likely missing in OSM, absent = not tested).
- **QGIS:** *Layer → Add Layer → Add ArcGIS REST Server Layer… → New*, URL `https://geodata.csu.gov.cz/server/rest/services`, connect, open folder *Hosted* → *HUZ* → layer 0. Alternatively *Layer → Add Layer → Add Vector Layer… → Protocol: HTTP(S)*, URI `https://geodata.csu.gov.cz/server/rest/services/Hosted/HUZ/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=geojson` (the server pages results, so the REST connection is the easier way to get all 10,454). The older snapshot opens directly as `/vsizip/vsicurl/https://geodata.csu.gov.cz/as/data/distribuce/Hosted/HUZ/FeatureServer/0/geojson.zip/HUZ_20250601.geojson` (the server answers range requests).

## Notes
- **What it is:** the register of "collective accommodation establishments" that ČSÚ surveys for its tourism
  statistics (NKOD description: "Definiční body adresních míst hromadných ubytovacích zařízení (HUZ) a jejich
  základní statistické údaje"). It is a national list of hotels, pensions, hostels and campsites with a stable identifier and an official category.
  It is not listed on `Cs:Česko/freemap` (only ČSÚ RSO and UIR-ZSJ are), not in `Cs:Zdroje_v_jednani`,
  not in Sync `config.toml`, and not in ZABAGED (see below).
- **Gap, national (local match against the 2026-09-27 Czechia extract, Postpass unavailable; same rule:
  tourism in hotel/guest_house/hostel/motel/camp_site/caravan_site/chalet/apartment/alpine_hut/wilderness_hut
  within 100 m):** 4,693 of 10,454 (45 %) have nothing within 100 m. Per ČSÚ category (missing / total):

  | ČSÚ kat | total | no OSM accommodation within 100 m | nearest-type check: expected OSM value within 100 m |
  |---|---|---|---|
  | Hotel \* … \*\*\*\*\* | 2,848 | 615 (22 %) | tourism=hotel 2,069 |
  | Hotel garni | 167 | 51 (31 %) | tourism=hotel 97 |
  | Penzion | 4,297 | 2,028 (47 %) | tourism=guest_house 1,672 |
  | Turistická ubytovna | 712 | 449 (63 %) | tourism=hostel 102 |
  | Kemp | 575 | 329 (57 %) | tourism=camp_site/caravan_site 191 |
  | Chatová osada | 280 | 216 (77 %) | tourism=chalet 10 |
  | Ostatní HUZ | 1,575 | 1,005 (64 %) | – |

  Pensions are the largest absolute gap (2,028), hostels/ubytovny and chalet settlements the largest relative
  one; hotels are mostly mapped. The OSM side contains 11,191 accommodation nodes and ways; relations are not
  in the extract, so campsites mapped only as multipolygons count as missing and the Kemp figure is an upper
  bound. Ways are reduced to the mean of their node coordinates. No OSM accommodation object has a key
  containing csu/czso/huz or a `ref*` value equal to any ČSÚ `pagina`, so there is no existing linkage.
- **Earlier sample (Postpass, 2026-09-27, earlier round agent; tourism in hotel/guest_house/hostel/motel/
  camp_site/caravan_site/chalet/apartment/alpine_hut/wilderness_hut within 100 m):**
  random national sample of 1,000 → only 563 have an OSM accommodation object within 100 m, so roughly
  4,500 establishments are missing. Town checks: Třeboň 42 of 74 missing, Pec pod Sněžkou 88 of 170 missing,
  Mikulov 21 of 64 missing. Even where OSM has "something" within 100 m, in dense resorts that is often a
  different establishment, so the real gap is larger.
  (The national figure above, 4,693 missing, confirms this estimate.)
- **ID stability (checked):** the 2025-06-01 snapshot and the 2026 FeatureServer share 10,402 `pagina` values
  (250 closed, 52 new) and 10,309 of those keep the same name, so `pagina` is a stable key and suits Sync.
  Suggested key: `ref:csu:huz=<pagina>` (no `ref:csu*` key exists in CZ yet).
- **Category → tag mapping** (wiki pages read: Tag:tourism=hotel, Tag:tourism=guest_house,
  Cs:Tag:tourism=guest_house, Tag:tourism=hostel, Cs:Tag:tourism=hostel, Tag:tourism=camp_site,
  Tag:tourism=chalet, Key:stars, Key:seasonal):

  | ČSÚ kat | OSM |
  |---|---|
  | Hotel \* … Hotel \*\*\*\*\* | tourism=hotel + stars=1…5 |
  | Hotel garni | tourism=hotel (garni = without restaurant; no star level given) |
  | Penzion | tourism=guest_house |
  | Turistická ubytovna | tourism=hostel (wiki: cheap accommodation with shared dormitory) |
  | Kemp | tourism=camp_site (pocmis gives a pitch band, not a number) |
  | Chatová osada | tourism=chalet (the wiki says the tag is also used for a group of chalets under one operator; tourism=holiday_village is the rarer alternative) |
  | Ostatní HUZ | manual review: names show "apartmány" (221), "chata" (222), "rekreační středisko/zařízení" (221), "ubytovna/ubytování" (101), student dormitories "kolej"/"domov mládeže", children's camps "tábor" |

- **Caveats:**
  - Names are in capitals (10,440 of 10,454), so they need case-fixing before use; do not overwrite
    existing OSM names.
  - Star levels come from the category the establishment reports to ČSÚ, not from an audited
    Hotelstars classification. Key:stars follows the Hotelstars Union levels, so treat stars as a hint.
  - Bands (rooms 1–10, 11–25…, beds, pitches) are not exact values and should not go into `rooms`/`beds`.
  - `sezona` (Celoroční 8,495; Letní 1,565; Smíšený 315; Zimní 79) could map to `seasonal=summer/winter`,
    but Key:seasonal prefers `opening_hours` for amenities; leave it as a review hint.
  - The point sits on the address point, not on the building entrance; `idruian` allows `addr:*` to be filled
    from RÚIAN. 369 records have no `idruian`.
  - The downloadable zip is the 2025-06-01 snapshot; the FeatureServer is the current version.
- **ZABAGED overlap (checked 2026-09-27 on `ags.cuzk.gov.cz/.../ZABAGED_POLOHOPIS/MapServer`):** no layer for
  hotels, pensions or hostels. Layer 114 "Areál účelové zástavby" has 712 areas with `typzast_p='camping'`
  (403 with a `jmeno`, which is often a locality name, not the campsite's name) and 2,807 "chatová kolonie"
  (private cottage colonies, not rentals). So ZABAGED only helps with campsite outlines.
- **Talk-cz archive** was not searched in this round.

## Wiki entry
```
===ČSÚ – Hromadná ubytovací zařízení===
* dataset: Hromadná ubytovací zařízení (adresní body)
* gestor: [https://www.czso.cz/ Český statistický úřad]
* licence: CC0 [https://data.gov.cz/zdroj/datové-sady/00025593/33c18c263706082c2f47bc89119260d8]
* datové primitivy: body
* odkaz: https://geodata.csu.gov.cz/server/rest/services/Hosted/HUZ/FeatureServer/0
* navržený tag {{tag|tourism|hotel}} / {{tag|tourism|guest_house}} / {{tag|tourism|hostel}} / {{tag|tourism|camp_site}} / {{tag|tourism|chalet}}, {{tag|ref:csu:huz|<pagina>}}
* poznámka: 10 454 hotelů, penzionů, ubytoven a kempů se stabilním ID; 4 693 z nich (45 %, z toho 2 028 penzionů) nemá v OSM žádné ubytování do 100 m (Pec pod Sněžkou chybí 88 ze 170)
```
