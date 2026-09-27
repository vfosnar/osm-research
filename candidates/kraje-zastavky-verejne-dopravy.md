# Regional public transport stop registers (Jihočeský, Karlovarský, Královéhradecký, Olomoucký, Moravskoslezský, Liberecký kraj)

| Field | Value |
|---|---|
| publisher | Jihočeský kraj (IČO 70890650); Karlovarský kraj (70891168); Královéhradecký kraj / VDKHK (70889546); Olomoucký kraj (60609460); Moravskoslezský kraj (70890692); Liberecký kraj / KORID (70891508) |
| url | JČK https://geoportal.kraj-jihocesky.gov.cz/portal/media/Soubory/opendata/zastavky_JCK_SHP.zip ; KV https://www.datazapad.cz/api/download/v1/items/979283f4b7ec4b778b8eed7aab6917c3/geojson?layers=0 ; KHK https://www.datakhk.cz/api/download/v1/items/ab928607832141f8bebb36261593107a/csv?layers=0 ; OK https://www.dataok.cz/api/download/v1/items/3e42001252dc42fdbf5f3c8240be779e/geojson?layers=0 ; MSK https://datamsk-mskraj.hub.arcgis.com/api/download/v1/items/0c8d67cd095543adb3ba08d4dc62c0cb/geojson?layers=0 ; IDOL https://dopravnimapy.kraj-lbc.cz/opendata/zastavky_shp_wgs84.zip |
| format | SHP (S-JTSK), GeoJSON, CSV |
| coords | yes |
| records | JČK 7,219 (platform level; 3,683 names; CISLO_NUM = CIS stop number; 6,870 served); KV 1,840 (platform level, Číslo_zastávky + Stanoviště); KHK 4,538 (platform level, Označení + Stanoviště); OK 2,100; MSK 3,270 (ID_ZAS, ODIS); IDOL 2,310 |
| osm_tags | public_transport=platform + highway=bus_stop, name=*, local_ref=&lt;stanoviště&gt;, ref:CIS_JR=&lt;CIS number&gt; |
| osm_count_cz | highway=bus_stop 59,315; public_transport=platform 68,032; ref:CIS_JR 13,300 (taginfo 2026-09-26) |
| license | JČK: no copyright, no DB copyright, sui generis CC0; KV, KHK, OK: NKOD terms "neobsahuje autorská díla / není autorskoprávně chráněnou databází / není chráněna zvláštním právem"; MSK: CC BY 4.0; IDOL: CC BY-SA 4.0 |
| license_url | https://creativecommons.org/publicdomain/zero/1.0/ ; https://data.gov.cz/podmínky-užití/neobsahuje-autorská-díla/ ; https://creativecommons.org/licenses/by/4.0/ ; https://creativecommons.org/licenses/by-sa/4.0/ |
| license_status | ok (JČK, KV, KHK, OK); needs_waiver (MSK, IDOL) |
| update_freq | JČK file dated 2026-01-28; others irregular (ArcGIS hubs, live) |
| impact | 3 |
| verified | yes |

## Try it

- **Map preview:** [samples/kraje-zastavky-verejne-dopravy.geojson](../samples/kraje-zastavky-verejne-dopravy.geojson) has the 1,296 Olomoucký kraj stops south of 49.75° N (Olomouc, Prostějov, Přerov). OK is the region with the biggest gap. 289 of them have no OSM stop, platform or station within 100 m (`osm_stop_distance_m`, Postpass 2026-09-27). The OK `CIS` field is kept as `CIS_ok_internal_id` because it is not `ref:CIS_JR`.
- **QGIS:** *Layer → Add Layer → Add Vector Layer…*. For KV, OK and MSK, choose *Protocol: HTTP(S)* and paste the GeoJSON URL from the table. For JČK, choose *File* and paste `/vsizip/vsicurl/https://geoportal.kraj-jihocesky.gov.cz/portal/media/Soubory/opendata/zastavky_JCK_SHP.zip/zastavky_JcK_20260128_SHP/zastavky_JcK_20260128.shp` (the inner name is dated and changes with each release). For IDOL, paste `/vsizip/vsicurl/https://dopravnimapy.kraj-lbc.cz/opendata/zastavky_shp_wgs84.zip/zastavky_shp_wgs84.shp`.

## Notes
- **How this was found:** following the Google Transit lead. Google credits only PID for CZ transit
  (legal notices). The Mobility Database lists only PID, IDS JMK, DPMO Olomouc, DPMLJ (dead link) and PMDP Plzeň
  feeds for CZ. The regional stop registers turned up in the NKOD while looking for GTFS publishers. Regional
  bus networks outside Prague and Brno have no open GTFS, but their stop positions are published.
- **Why it matters:** CIS JŘ, the national timetable, has stop names but no coordinates.
  `vfosnar/jizdni-rady-osm` (run 2026-09-27) located 37,206 of 43,724 CIS stops. It has 6,025 gaps and
  relies on a geocoder pass. These registers give official coordinates for CIS stop names at platform
  (stanoviště) level:
  - Exact name match against `https://portal.cisjr.cz/pub/seznamy/zastavky.csv` (40,394 names):
    OK 1,967/2,100, KHK 2,187/2,265, JČK 3,044/3,683, MSK 2,586/3,270, IDOL 1,681/2,305.
  - KV writes "Abertamy, Barbora" where CIS writes ",,". After normalising the separator it should match
    too (not tested).
- **OSM coverage** (Postpass, random sample of 300 per region, 2026-09-27; any OSM stop, platform or halt
  within the radius):

  | Region | ≤30 m | ≤100 m | Est. stops missing (>100 m) |
  |---|---|---|---|
  | JČK | 95 % | 96 % | ~290 |
  | KHK | 96 % | 98 % | ~90 |
  | IDOL | 82 % | 93 % | ~160 |
  | MSK | 86 % | 88 % | ~390 |
  | KV | 75 % | 79 % | ~390 |
  | OK | 62 % | 75 % | ~520 |

  KV and OK have the biggest gaps. Part of the 30–100 m band is OSM stops that are offset or sit on the
  wrong side of the road.
- **ref:CIS_JR** (13,300 in CZ, no wiki page yet). JČK `CISLO_NUM` matches 3,309 of 3,494 bus CIS numbers
  already in OSM in that region, so JČK was probably the source earlier. The KV `Číslo_zastávky` and MSK
  `ID_ZAS` values match OSM `ref:CIS_JR` (KV 298 of 383, MSK 412 of 423). OSM has only 383 and 423 refs
  there, so about 600 (KV) and about 2,800 (MSK) stops could get `ref:CIS_JR`. The OK field named `CIS`
  matches only 11 of 200 OSM refs, so it is some other ID. Don't use it as `ref:CIS_JR`.
- Not usable from here: ÚK (DÚK) "CIS zastávky ÚK" API `https://tabule.portabo.cz/api/v1-tabule/cis/GetStations/`
  was refused by this environment's proxy ("private/reserved range"). Its NKOD terms say no rights. Worth
  retrying elsewhere.
- The KHK "Železniční stanice a zastávky VDKHK" layer (185 points) is really the transport information
  offices, not rail stops. Skip it.
- Wiki pages read: Tag:public_transport=platform (ref, local_ref, network). There is no wiki page for
  `ref:CIS_JR`; it should get one before a Sync dataset.
- **Suggested use:** feed the ok-licensed layers into jizdni-rady-osm as a coordinate source for the gap stops,
  and add Sync datasets keyed on `ref:CIS_JR` (JČK, KV) for platform positions. MSK needs a CC BY waiver
  (the Moravskoslezský kraj open data team) and IDOL needs a CC BY-SA waiver (KORID LK).

## Wiki entry
```
===Zastávky veřejné dopravy krajů (JČK, KV, KHK, OK, MSK, IDOL)===
* dataset: Zastávky veřejné dopravy Jihočeského kraje; Autobusové zastávky v Karlovarském kraji; Autobusové zastávky VDKHK; zastávky hromadné dopravy v Olomouckém kraji; Zastávky veřejné hromadné dopravy v Moravskoslezském kraji; Autobusové zastávky IDS IDOL
* gestor: [https://geoportal.kraj-jihocesky.gov.cz Jihočeský kraj], [https://www.datazapad.cz Karlovarský kraj], [https://www.datakhk.cz Královéhradecký kraj], [https://www.dataok.cz Olomoucký kraj], [https://datamsk-mskraj.hub.arcgis.com Moravskoslezský kraj], [https://dopravnimapy.kraj-lbc.cz Liberecký kraj]
* licence: JČK CC0 (zvláštní právo), KV/KHK/OK bez ochrany dle NKOD; MSK CC BY 4.0, IDOL CC BY-SA 4.0 (nutný souhlas) [https://data.gov.cz/podmínky-užití/neobsahuje-autorská-díla/]
* datové primitivy: body (stanoviště)
* odkaz: https://geoportal.kraj-jihocesky.gov.cz/portal/media/Soubory/opendata/zastavky_JCK_SHP.zip, https://www.datazapad.cz/api/download/v1/items/979283f4b7ec4b778b8eed7aab6917c3/geojson?layers=0, https://www.datakhk.cz/api/download/v1/items/ab928607832141f8bebb36261593107a/csv?layers=0, https://www.dataok.cz/api/download/v1/items/3e42001252dc42fdbf5f3c8240be779e/geojson?layers=0
* navržený tag {{tag|public_transport|platform}}, {{tag|highway|bus_stop}}, {{tag|local_ref|<stanoviště>}}, {{tag|ref:CIS_JR|<číslo CIS>}}
* poznámka: souřadnice zastávek s názvy dle CIS JŘ; v OSM chybí ~20–25 % zastávek v KV a OK, ~2 800 zastávek v MSK nemá ref:CIS_JR
```
