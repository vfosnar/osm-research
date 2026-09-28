# CIS JŘ (JDF) – barrier-free stop flag "@" for city and regional operators, plus the DÚK stop register (Ústecký kraj)

| Field | Value |
|---|---|
| publisher | Ministerstvo dopravy / CIS JŘ (IČO 66003008) for JDF; Doprava Ústeckého kraje (DÚK, IČO 70892156) for the stop register |
| url | JDF buses https://portal.cisjr.cz/pub/JDF/JDF.zip (107 MB, NKOD https://data.gov.cz/zdroj/datové-sady/66003008/1463646434); JDF trams and trolleybuses https://portal.cisjr.cz/pub/draha/mestske/JDF.zip (29 MB, NKOD https://data.gov.cz/zdroj/datové-sady/66003008/701563102); DÚK stops https://tabule.portabo.cz/api/v1-tabule/duk/GetStations (NKOD https://data.gov.cz/zdroj/datové-sady/70892156/cc6794f1272c9bcdfc9ac00413ab3250) |
| format | JDF 1.11: one ZIP per line inside the archive, CSV (cp1250, `"…";` rows); `Zastavky.txt` = stop number, obec, část obce, bližší místo, blízká obec, stát, pevný kód 1–6; `Pevnykod.txt` maps the numbers to symbols. DÚK: JSON `ItemList` of Node, Post, Name, Latitude, Longitude, Zone |
| coords | JDF: no (stop names only, stop level, not platform level). DÚK: yes (WGS84, node/post = platform level) |
| records | JDF (archives dated 2026-09-25): 275 carriers, 63,293 carrier/stop pairs, 836 flagged "@" ("zastávka je bezbariérově přístupná"). City operators with the flag: MD Teplice 23 of 137 stops, DPMČB 19 of 209, MDPO Opava 18 of 126, DPO Ostrava 18 of 563 (all suburban bus stops). Regional carriers in Moravskoslezský kraj: Transdev Slezsko 246 of 1,627, Transdev Morava 130 of 1,724, Z-Group bus 113 of 1,614. DÚK: 7,197 node/posts (331 with 0,0 coordinates), `cis/GetStations` 9,047 |
| osm_tags | on the existing public_transport=platform / highway=bus_stop / railway=tram_stop of that stop: wheelchair=yes for "@"; no tag where "@" is missing (absence is not "no") |
| osm_count_cz | public_transport=platform 68,045, ref:CIS_JR 13,302 (taginfo 2026-09-27). Postpass 2026-09-28: MSK bbox 17.1,49.4–18.9,50.35 12,940 OSM stops/platforms, 340 with wheelchair; ÚK bbox 13.3,50.25–14.65,50.95 7,713, 1,368 with wheelchair |
| license | JDF: NKOD terms "neobsahuje autorská díla", "není autorskoprávně chráněnou databází", "není chráněna zvláštním právem pořizovatele databáze" (NKOD maps it to CC0). DÚK stops: the same three terms, also mapped to CC0 |
| license_url | https://data.gov.cz/podmínky-užití/neobsahuje-autorská-díla/ ; https://data.gov.cz/podmínky-užití/není-chráněna-zvláštním-právem-pořizovatele-databáze/ |
| license_status | ok |
| update_freq | JDF archive last-modified 2026-09-25 19:53 GMT (no stated schedule); DÚK API live (NKOD: UPDATE_CONT) |
| impact | 2 |
| sync_fit | MapRoulette for JDF "@" (no coordinates, stop-level flag, needs name matching and a look at each platform); Sync for the DÚK register (points with a stable node/post ID) |
| verified | yes |

## Try it

- **Map preview:** [samples/cisjr-jdf-bezbarierove-zastavky.geojson](../samples/cisjr-jdf-bezbarierove-zastavky.geojson): the 499 OSM stops/platforms whose name matches a JDF stop flagged "@" by DPMČB, MD Teplice, Doprava Teplice, MDPO Opava, DPO and the three MSK regional carriers. JDF has no coordinates, so the points are the OSM positions; `osm_wheelchair` shows the current tag (empty = untagged), `jdf_carrier` and `jdf_stop_name` show where the flag came from.
- **QGIS (JDF):** JDF is not a GIS format. Download `https://portal.cisjr.cz/pub/draha/mestske/JDF.zip`, unzip it, then unzip one line (`1.zip` is DPMÚL line 1). `Zastavky.txt` opens with *Layer → Add Layer → Add Delimited Text Layer…*: custom delimiter `,` and `;`, quote `"`, encoding windows-1250, no header, *No geometry*. Pevný kód columns are field_7–field_12; look up the number in `Pevnykod.txt` of the same line ("@" was code 14 in `1.zip`).
- **QGIS (DÚK):** the API returns plain JSON, not GeoJSON. Save it and convert: `curl -s https://tabule.portabo.cz/api/v1-tabule/duk/GetStations | python3 -c "import json,sys;L=json.load(sys.stdin)['ItemList'];json.dump({'type':'FeatureCollection','features':[{'type':'Feature','geometry':{'type':'Point','coordinates':[s['Longitude'],s['Latitude']]},'properties':s} for s in L if s['Latitude']]},open('duk.geojson','w'))"`, then *Layer → Add Layer → Add Vector Layer…* → `duk.geojson`. Use the URL without a trailing slash: `…/GetStations/` answers 307 to a private IP (172.30.72.19), which is why the earlier try failed. `…/duk/GetStations/dpmul` returns only DPMÚL (Ústí nad Labem) stops.

## Notes
- **Operator survey (2026-09-28): none of the requested city operators publishes a GTFS.** Checked NKOD (titles, descriptions, keywords with GTFS / MHD / jízdní řád), the Mobility Database catalogue (CZ has only PID, IDS JMK, DPMO, DPMLJ, Bean Shuttle and an unofficial national JDF conversion) and each operator homepage for GTFS / open-data links:

  | Operator | GTFS | JDF "@" on stops | Other source |
  |---|---|---|---|
  | DPO Ostrava | no | 18 of 563 (suburban bus stops only, none on trams) | Ostrava "Zastávky MHD" layer with `bezbarier` (below) |
  | DPMHK Hradec Králové | no | 0 of 213 | city accessibility map (see `mesta-mapy-pristupnosti.md`) |
  | DPMP Pardubice | no | 0 of 218 | – |
  | DPMČB České Budějovice | no | 19 of 209 | – |
  | DSZO Zlín | no | 0 of 215 | – |
  | DPMJ Jihlava | no | 0 of 128 | – |
  | DPMÚL Ústí nad Labem | no | 0 of 219 | DÚK stop register (below), coordinates but no accessibility |
  | DPMLJ Liberec | `https://www.dpmlj.cz/gtfs.zip` still listed "active" in the Mobility Database (bbox extracted 2023-03-17), but www.dpmlj.cz could not be reached from here (TLS reset, HTTP 503) | 0 of 253 | – |
  | DPKV Karlovy Vary | no | 0 of 983 | – |
  | DPMMB Mladá Boleslav | site not reachable from here (proxy 502) | 0 of 124 | – |
  | MD Teplice | site answered 403 | 23 of 137 (+12 of 264 Doprava Teplice) | – |
  | MDPO Opava | site certificate failed | 18 of 126 | Opava `info_bezbarierovemhd_V` layer (see `mesta-mapy-pristupnosti.md`) |

  So the PMDP and DPMO feeds remain the only city GTFS with wheelchair_boarding. The one uniform source for everyone else is the CIS JŘ JDF export, and in it only four city operators and three MSK regional carriers use the barrier-free stop flag.
- **What "@" means:** JDF 1.10 spec (https://www.dpmo.cz/doc/cz/jdf-1.10.pdf, pevné kódy): "@" on a stop = "zastávka je bezbariérově přístupná"; on a trip = "spoj s bezbariérově přístupným vozidlem". Only the stop use is taken here. "~" (the most common stop code, 3,732 of 4,076 PMDP stop records) is "možnost přestupu na městskou hromadnou dopravu" and says nothing about access. The flag is per stop name, not per platform, and a stop may carry it in one line's package and not in another; the counts above take the union over all packages.
- **Gap (Postpass 2026-09-28, OSM stop/platform/tram_stop whose normalised name equals the JDF name; for DPMČB, Teplice and Opava also the local part inside the city):** 579 flagged stops, 376 matched to 499 distinct OSM objects. **429 of the 499 have no wheelchair tag**; 30 are wheelchair=yes, 40 limited, none no. By carrier: Transdev Slezsko 345 untagged of 352 matched platforms (Havířov, Třinec, Karviná), Transdev Morava 140/140 (Krnov, Kopřivnice), Z-Group bus 102/102, MDPO Opava 36/36, DPO 33/38. České Budějovice and Teplice are already well tagged (ČB bbox 397 of 640 OSM stops carry wheelchair, Teplice 392 of 609): there the flag conflicts rather than fills — 35 matched ČB platforms are `limited` in OSM where JDF says accessible. 203 flagged stops found no OSM name match, mostly regional stops where OSM abbreviates differently ("Pr. Suchá" vs "Pr.Suchá"); jizdni-rady-osm's name matcher would do better.
- **Why this adds to what exists:** `vfosnar/jizdni-rady-osm` reads the same JDF but does not use pevné kódy for stops (no "@" or wheelchair handling in `src/jdf.rs`, `feed.rs`, `map.rs`, checked 2026-09-28). The CIS NeTEx export (`https://portal.cisjr.cz/pub/netex/NeTEx_DrahyMestske.zip`) has StopPlace names only, no coordinates or accessibility, so it adds nothing.
- **Caveat:** "@" is filled by the carrier when it submits timetables and is rare (836 of 63,293 carrier/stop pairs), so treat it as a hint for a MapRoulette task ("check the platform, add wheelchair=yes"), not as an import. Absence of "@" means nothing.
- **Ostrava "Zastávky MHD" (Statutární město Ostrava, `https://mapy.ostrava.cz/opendata/data/opendata/zastavky_MHD_WGS84_gjson.zip`, NKOD https://data.gov.cz/zdroj/datové-sady/00845451/a6d69626bceefb9c2089445e2034ccc4):** 1,313 platforms with `bezbarier` ANO 160 / NE 1,153, `doprava`, `znameni` (request stop). Of the 153 ANO platforms with an OSM stop within 30 m, 133 have no wheelchair tag. But the file inside the ZIP is dated 2020-02-21, NE is also given where OSM says yes (14 cases), and the terms are CC BY 4.0 for the work and CC BY-SA 4.0 for the database (needs_waiver). Contact: the contact point in the NKOD record (Statutární město Ostrava) about a refresh and an OSM consent.
- **DÚK stop register (retry of the lead in `kraje-zastavky-verejne-dopravy.md`):** reachable now; only the trailing slash was the problem. 5,529 posts with coordinates inside 13.3,50.25–14.65,50.95: 4,063 have an OSM stop within 30 m, 401 within 30–100 m, **1,065 have none within 100 m** (19 %; nearest OSM stop/platform/halt/station, Postpass 2026-09-28). Node is DÚK's own node number, not ref:CIS_JR (0 of 19 matched platforms with ref:CIS_JR agree). No accessibility fields. `ref:DUK=<Node>/<Post>` would need a wiki page first. The full DÚK GTFS exists (`/cis/GetGtfs/gtfs_duk_all`, and `gtfs_google_all` "published to Google") but needs a bearer token (401). Ask DÚK (Doprava Ústeckého kraje, příspěvková organizace) for open access to that GTFS; it would give ÚK what IDS JMK gives JMK.
- **Rejected:** `tangero/jizdni-rady-czech-republic` on GitHub (an aggregated national GTFS) is converted from CHAPS/IDOS `.tt` files and CIS data, CC BY 4.0, and adds no accessibility of its own.
- **Tags:** Key:wheelchair read (no default value; yes/limited/no). Suggest only `wheelchair=yes`.
- **Contacts:** Ministerstvo dopravy (CIS JŘ) on how carriers fill "@"; DÚK for the GTFS token; the carriers themselves (Transdev Slezsko, Transdev Morava) to confirm what they check before setting the flag.

## Wiki entry
```
===CIS JŘ – bezbariérové zastávky (pevný kód @ v JDF)===
* dataset: Jízdní řády veřejné linkové dopravy a Jízdní řády veřejné dopravy na dráhách tramvajových, trolejbusových… (JDF), soubor Zastavky.txt
* gestor: [https://data.gov.cz/zdroj/datové-sady/66003008/1463646434 Ministerstvo dopravy / CIS JŘ]
* licence: neobsahuje autorská díla, není chráněnou databází [https://data.gov.cz/podmínky-užití/neobsahuje-autorská-díla/]
* datové primitivy: bez souřadnic (názvy zastávek), párování podle názvu
* odkaz: https://portal.cisjr.cz/pub/JDF/JDF.zip ; https://portal.cisjr.cz/pub/draha/mestske/JDF.zip
* navržený tag {{tag|wheelchair|yes}} na existující {{tag|public_transport|platform}} (jen kontrolní úloha, ne import)
* poznámka: 429 z 499 nástupišť v OSM, jejichž zastávka má v JDF příznak @, nemá wheelchair (hlavně Havířov, Třinec, Karviná, Krnov, Opava)

===DÚK – seznam zastávek Ústeckého kraje===
* dataset: Seznam zastávek DÚK
* gestor: [https://data.gov.cz/zdroj/datové-sady/70892156/cc6794f1272c9bcdfc9ac00413ab3250 Doprava Ústeckého kraje]
* licence: neobsahuje autorská díla, není chráněnou databází [https://data.gov.cz/podmínky-užití/neobsahuje-autorská-díla/]
* datové primitivy: body
* odkaz: https://tabule.portabo.cz/api/v1-tabule/duk/GetStations
* navržený tag {{tag|public_transport|platform}}, {{tag|highway|bus_stop}}
* poznámka: 1 065 z 5 529 sloupků DÚK nemá v OSM zastávku do 100 m
```
