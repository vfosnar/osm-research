# Slovenská pošta – zoznam poštových schránok

| Field | Value |
|---|---|
| publisher | Slovenská pošta, a.s. (state-owned) |
| url | https://www.posta.sk/files/6811e10225b182cd7cd9e3b9/zoznam-postovych-schranok.xlsx (linked from the "Súbory na stiahnutie" block of https://www.posta.sk/pobocky-a-balikoboxy) |
| format | XLSX, one sheet "Zoznam PS" (237 kB) |
| coords | yes (`Zem.šírka` / `Zem.dĺžka`, WGS84 decimal degrees, on all 3,006 rows) |
| records | 3,006 post boxes (30 Sep 2026): 1,631 "ostatné" (street locations), 1,256 on or next to a post office, 102 at a BalíkoBOX, 17 inside a post office |
| osm_tags | amenity=post_box, operator=Slovenská pošta, collection_times, ref (checked on Tag:amenity=post_box) |
| osm_count_sk | amenity=post_box 1,086 (taginfo europe:slovakia, data until 2026-09-29) |
| license | none stated on the file or page |
| license_url | https://www.posta.sk/pobocky-a-balikoboxy |
| license_status | unclear |
| update_freq | irregular (no date in the file; its storage id encodes 30 Apr 2025, so it may be that old; changes in the network are also published as `zmeny-v-postovej-sieti.xlsx` on the same page) |
| impact | 4 |
| sync_fit | Sync (points, category 1:1 to amenity=post_box; composite ref from post name + box number; collection_times as an update key) |
| verified | yes |

## Try it
- **Map preview:** no sample, because no licence is stated (`unclear`).
- **QGIS:** download the XLSX and open it with *Layer → Add Layer → Add Vector Layer* (GDAL reads XLSX). Then *Processing → Create points layer from table*, X field `Zem.dĺžka`, Y field `Zem.šírka`, CRS EPSG:4326. Tested 30 Sep 2026.
- **Web:** branch finder https://www.posta.sk/pobocky-a-balikoboxy (does not show the boxes on the map).

## Notes
- Known (`WikiProject Slovakia/Sources`, section "Slovenská pošta - pobočky": phone consent and 2021 import of post offices by Dodko) — adds: a new object type from the same holder. The consent covers post office data only; post boxes were raised in the 2021 import thread (`afglwDyRtBM`) but not imported. AllThePlaces `slovenska_posta_sk` (1,596 features) has offices and BalíkoBOX lockers, not post boxes.
- Columns: `Číslo PS` (box number within the post), `Schránku prevádzkuje` (the post office that empties it), `Umiestnenie` (location class), `Adresa`, `Zem.šírka`, `Zem.dĺžka`, `Čas vyberania schránok/Zaradenie do výpravy`, `Služby` (`PS-L` stamped letters; `PS-LePH` also letters paid with the online ePodací hárok). 1,598 boxes are PS-L only, 1,408 also PS-LePH.
- Collection times: 2,807 rows are a single weekday time (`po-pi:13:30/dnes` → `collection_times=Mo-Fr 13:30`), 199 list each weekday (`po:12:00/dnes ut:12:00/dnes st:11:00/dnes …`), which converts to `Mo,Tu,Th,Fr 12:00; We 11:00`. The suffix `dnes` (2,881) / `zmeškané` (125) says whether the collection still makes the same day's dispatch; it has no OSM equivalent and can go to a note.
- Stable ID: no single ID column. `Schránku prevádzkuje` + `Číslo PS` is unique for all but 30 pairs; propose `ref=<Číslo PS>` with `operator`, or a combined `ref:posta_sk=<post>/<n>` for Sync (agree in osm_sk).
- Gap (Postpass, 30 Sep 2026): 50 of 400 randomly sampled boxes have an OSM `amenity=post_box` within 50 m (12.5 %). That puts roughly 2,600 post boxes missing, which would more than triple the OSM count.
- Caveats: coordinates of "na budove pošty" boxes likely repeat the post office position (fine for OSM, since the box is on the building). For "ostatné" boxes the address and coordinates come from the post; spot-check against imagery before bulk use.
- Licence: the file carries no terms. Slovenská pošta already agreed by phone (2021) to OSM use of its branch data and GPS positions; ask the same department (Odbor podpory a rozvoja pobočkovej siete, named on the Sources page) to extend the consent to the post-box list.
- Same page, not proposed: `zoznam-post-s-hodinami-pre-verejnost.xls` (offices, already imported), `zoznam-pojazdnych-post-s-otvaracimi-hodinami.xls` (mobile post stops), `stanovistia-motorizovanych-dorucovatelov.xls`, `prehlad-poskytovanych-sluzieb-na-postach.xlsx` (services per office; could enrich the imported offices).
- ZBGIS: no post-box type in the ZBGIS catalogue (KTO checked 30 Sep 2026).
- Wiki pages read: Tag:amenity=post_box.

## Wiki entry
```
=== Slovenská pošta – poštové schránky ===
* dataset: Zoznam poštových schránok
* správca: [https://www.posta.sk/ Slovenská pošta, a.s.]
* licencia: neuvedená – rozšíriť súhlas pre pobočky z roku 2021 [https://www.posta.sk/pobocky-a-balikoboxy]
* dátové primitívy: body
* odkaz: https://www.posta.sk/files/6811e10225b182cd7cd9e3b9/zoznam-postovych-schranok.xlsx
* navrhované značky: {{tag|amenity|post_box}}, {{tag|operator|Slovenská pošta}}, {{tag|collection_times|Mo-Fr 13:30}}, {{tag|ref|<číslo PS>}}
* poznámka: Zoznam má 3 006 schránok so súradnicami a časom výberu, v OSM je 1 086 schránok a v náhodnej vzorke má náprotivok v OSM len 12,5 %.
```
