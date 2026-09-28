# Evangnet – schematismus ČCE: all 230 congregations of the Evangelical Church of Czech Brethren with coordinates and Sunday service times

| Field | Value |
|---|---|
| publisher | Evangnet, z. s. (IČO 26610850, spravci@evangnet.cz); records are maintained by the Ústřední církevní kancelář ČCE (each page shows "Aktualizace: &lt;date&gt;, ÚCK &lt;name&gt;") |
| url | https://www.evangnet.cz/cce/sbory/ (list, 230 links); detail https://www.evangnet.cz/cce/sbor/&lt;id&gt;-&lt;slug&gt; (for example https://www.evangnet.cz/cce/sbor/80-jilemnice); summary table of service times https://www.evangnet.cz/cce/casy_bohosluzeb?sen=0&ks=0&bv=0&bv=1&ba=0&ba=1&bz=0&v=1&submit=Filtrovat; preaching stations https://www.evangnet.cz/cce/stanice/ |
| format | HTML (ISO-8859-2); coordinates in the mapy.com link `source=coor&id=&lt;lon&gt;,&lt;lat&gt;` on each detail page |
| coords | yes (WGS84, all 230 congregations; preaching stations have none) |
| records | 230 farní sbory (230 with coordinates and a `bohoslužby` time, 219 with a website, all with address, phone, IČO, 4-digit `kód sboru`); 182 preaching stations (kazatelské stanice) listed inside the congregation pages with their own service times, no coordinates |
| osm_tags | on the existing church: `amenity=place_of_worship`, `religion=christian`, `denomination=protestant` (208 uses in CZ; `czech_brethren` 21 and `evangelical` 136 also used, see notes), `service_times=Su 09:30`, `website`, `phone`, `operator=Farní sbor Českobratrské církve evangelické v …`; suggested `ref:cce=&lt;kód sboru&gt;` (unused) |
| osm_count_cz | taginfo 2026-09-28: service_times 228 (all objects); denomination=czech_brethren 21, protestant 208, evangelical 136, lutheran 120. Local match against the 2026-09-27 Czechia extract (Postpass 503): 150 of 230 congregations have a non-Catholic place of worship within 150 m, of which only 20 have service_times |
| license | none stated on evangnet.cz |
| license_url | – |
| license_status | unclear |
| update_freq | continuous; all 230 pages show an update date in 2026 (fetched 2026-09-28) |
| impact | 3 |
| sync_fit | MapRoulette (attribute enrichment, fuzzy matching, ref:cce unused so far) |
| verified | yes |

## Try it
- **Map preview:** none, licence unclear.
- **Browser:** open https://www.evangnet.cz/cce/sbor/80-jilemnice: address, phone, website, `poloha` (link to mapy.com with `id=15.5071833333,50.6076361111`), `kód sboru: 0604`, `bohoslužby: 10.00`, `kazatelské stanice: Valteřice – 8.30`, `Aktualizace: 18.9.2026`.
- **All times in one table:** the `casy_bohosluzeb` URL above lists every congregation with its seniorát and service time.
- **QGIS:** not a GIS service. Harvest the 230 detail pages (links from `/cce/sbory/`), decode as ISO-8859-2 and take the coordinates from the regex `source=coor&id=([\d.]+),([\d.]+)` (lon, lat); save as CSV and load with *Layer → Add Layer → Add Delimited Text Layer*, X = lon, Y = lat, EPSG:4326. Tested: 230/230 pages parsed, 2026-09-28.

## Notes
- **What it adds:** the only national directory of ČCE (the largest Protestant church in Czechia) with
  coordinates, and a Sunday service time for every congregation. It complements the Catholic source in
  `cirkev-bohosluzby.md`. OSM has the buildings but almost never the times.
- **Gap, measured (local match against the 2026-09-27 Czechia extract, nodes and ways, 150 m radius, Catholic,
  Hussite, Orthodox and Jehovah's Witness places excluded):** 150 of 230 congregations have a candidate
  place of worship in OSM; **20 (13 %)** of those carry service_times. Denominations on the matched objects:
  protestant 62, evangelical 45, lutheran 15, none 14, czech_brethren 11, so the data would also fix
  inconsistent `denomination`: Template:Denominations lists no ČCE value, treats `protestant` as the category and warns that `evangelical` is not the German/Polish "evangelisch/ewangelicki" (the Czech "evangelický" is the same case), so `protestant` + `operator` fits; `czech_brethren` (21 uses, not on the wiki) is for the community to decide. 80 congregations have no match within 150 m (61 have some place of worship
  within 500 m, so the evangnet point is on the parish office or the church is mapped as a relation or not
  at all). Prague: 23 congregations, 15 matched, 5 with service_times.
- **Time format:** 181 of 230 values are a plain Sunday time ("9.30", "10:00", "neděle 9:30") that converts
  directly to `service_times=Su 09:30`; the rest have notes (monthly evening services, summer times, a second
  site) and need a human.
- **Coordinates:** point to the church or the parish house; some congregations list two addresses
  (office and "kostel"). Match to an existing object, never add new points blindly.
- **Stable id:** `kód sboru` (4 digits, the first two are the seniorát), also the IČO of each congregation.
- **Contact:** Evangnet z. s. (spravci@evangnet.cz) runs the site; the data belongs to the ČCE
  (Ústřední církevní kancelář, Jungmannova 9, Praha 1), who would have to give consent.
- **Rejected in the same theme:** Církev československá husitská (https://www.ccsh.cz/adresar-subj.html) lists
  religious communities with a postal address only, no coordinates and no service times.
  Federace židovských obcí (https://www.fzo.cz/zidovske-obce/, checked 2026-09-28) lists 10 Jewish
  communities (Brno, Děčín, Karlovy Vary, Liberec, Olomouc, Ostrava, Plzeň, Praha, Teplice, Ústí nad
  Labem) with office address, phone and web, plus a Shabbat-times calendar per city. No coordinates and no
  synagogue service times, so it is too small for an import (OSM already has 444 `religion=jewish`
  objects, taginfo 2026-09-28; most are cemeteries and former synagogues). The Orthodox church site
  https://www.pravoslavnacirkev.cz/ answers 403 to scripted requests, so its parish list was not read; OSM
  has 61 `denomination=orthodox`. Neither is worth a candidate file.
- Wiki pages read: Key:service_times, Key:denomination, Template:Denominations.

## Wiki entry
```
===Evangnet – sbory ČCE a časy bohoslužeb===
* dataset: Schematismus ČCE – sbory a kazatelské stanice
* gestor: [https://www.evangnet.cz/cce/sbory/ Evangnet, z. s. / Českobratrská církev evangelická]
* licence: neuvedena, nutno vyjednat s ÚCK ČCE a Evangnetem
* datové primitivy: body
* odkaz: https://www.evangnet.cz/cce/sbory/
* navržený tag {{tag|service_times|Su 09:30}}, {{tag|denomination|protestant}}, {{tag|ref:cce|<kód sboru>}}
* poznámka: 230 sborů se souřadnicemi a časem nedělní bohoslužby; v OSM má service_times jen 20 ze 150 dohledaných evangelických kostelů
```
