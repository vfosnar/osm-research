# RIS: Register škôl a školských zariadení (national register of schools and school facilities, incl. ZUŠ branches, CVČ, internáty)

| Field | Value |
|---|---|
| publisher | Ministerstvo školstva, výskumu, vývoja a mládeže SR; register kept in the rezortný informačný systém RIS (portal crinfo.iedu.sk) |
| url | https://crinfo.iedu.sk/risportal/register/ExportCSV?id=1 (Register ŠaŠZ, 11.8 MB CSV, file name `CIS_Reg_SaSZ_<date>.csv`); list of all registers with update times: https://crinfo.iedu.sk/risportal/register/registre (JSON). Related exports: `?id=2` zriaďovatelia, `?id=4` permitted study fields per school, `?id=5` Register zariadení predprimárneho vzdelávania |
| format | CSV, `;`-separated, UTF-8 with BOM |
| coords | address-only (street, súpisné číslo, orientačné číslo, PSČ, obec); 17,627 of 17,639 active records have a house number |
| records | 22,007 rows; 17,639 "v prevádzke": 4,685 školské jedálne (ŠJ), 3,434 materské školy, 2,168 základné školy, 2,121 ŠKD, 1,656 základné umelecké školy (1,245 of them elokované pracoviská), 1,016 spojené školy, 599 centrá voľného času, 504 SOŠ, 362 special ZŠ, 225 gymnáziá, 173 centrá poradenstva a prevencie, 153 školské internáty, 60 jazykové školy, 21 konzervatóriá, … Register ZPV: 48 active "detské centrá" |
| osm_tags | amenity=school (+ name "Základná umelecká škola …" as is local practice; amenity=music_school is used on 25 SK-named ZUŠ), amenity=kindergarten, amenity=community_centre + community_centre:for=child;juvenile or amenity=school for CVČ (needs a community decision); ref:eduid=&lt;EDUID&gt; proposed; website; operator (zriaďovateľ); language:hu=yes / name:hu for Hungarian-language schools |
| osm_count_sk | amenity=school 2,808; amenity=kindergarten 1,713; amenity=music_school 36; amenity=childcare 37; objects named "…umeleck…" 203, "Centrum voľného času" 55; ref:eduid 0 (taginfo europe:slovakia, 2026-09-30) |
| license | none stated on the RIS portal. The ministry's aggregated catalogue dataset "Register škôl a školských zariadení k 15.9.2025" (counts per district, built from RIS) is CC BY 4.0 |
| license_url | catalogue dataset IRI https://data.gov.sk/set/437907ab-fa48-4a28-a0ba-e8d9df5c4146 (database licence CC BY 4.0 in the SPARQL metadata); RIS portal https://crinfo.iedu.sk/risportal/ (no terms) |
| license_status | unclear |
| update_freq | daily (export timestamp 2026-09-30 07:52 on the day of checking) |
| impact | 4 |
| sync_fit | MapRoulette first (address-only, 1:N tag choice for CVČ/ZUŠ, many facilities share a school building); after geocoding onto OSM addresses, Sync with `ref:eduid` for ongoing updates (stable EDUID, openings and closures) |
| verified | yes (register downloaded and parsed; no sample because the licence is unclear) |

## Try it
- **Map preview:** none (licence unclear).
- **QGIS:** *Layer → Add Layer → Add Delimited Text Layer*, file name `https://crinfo.iedu.sk/risportal/register/ExportCSV?id=1`, custom delimiter `;`, encoding UTF-8, geometry "No geometry (attribute only table)". Join to OSM addresses (`addr:street`, `addr:conscriptionnumber`, `addr:streetnumber`, `addr:city` — present on ~1.49 M objects from MinvSKAddress) to place the records.
- **Web:** the list of registers at https://crinfo.iedu.sk/risportal/register/ (each row has a "Stiahnuť" CSV link).

## Notes
- **Why it matters:** OSM has the main primary schools but little of the rest. Examples (Postpass bbox counts vs active RIS records, 2026-09-30): Žilina — 22 ZUŠ locations in RIS, 3 OSM objects that are music schools or named "umeleck…"; 9 CVČ vs 0 OSM objects named "voľného času"; 42 kindergartens (MŠ + special MŠ) vs 28 `amenity=kindergarten`. Prešov — 28 ZUŠ vs 17, 15 CVČ vs 4. Nationally ~230 OSM objects carry a ZUŠ name against 1,656 ZUŠ locations. The elokované pracoviská of ZUŠ (music lessons held in village schools and culture houses) are the typical invisible POI: each has its own EDUID and address.
- **Stable ID:** `EDUID` (9 digits, 1000xxxxx for schools, 2000xxxxx for founders) plus `KODSKO`; hierarchy via `NadradenaSaSZ_EDUID` / `KmenovaSaSZ_EDUID`, successor chain via `PredchodcaSaSZ_EDUID`, lifecycle dates (`DatumZriadenia`, `DatumZrusenia`, `STAV`). Good for Sync-style ongoing updates.
- **Attributes:** type (`TypSaSZ`), official and short name, teaching language (738 Hungarian, 284 Slovak–Hungarian), ownership (14,566 state, 2,188 private, 885 church), founder, website (11,676 records). `Telefon` is empty in the export. `Riaditel` and `Statutari` are personal names; don't import.
- **Geocoding:** addresses carry both súpisné and orientačné číslo, which match the MinvSKAddress-derived `addr:conscriptionnumber`/`addr:streetnumber` already in OSM, so placement can be done against OSM itself without an external geocoder.
- **What to skip:** ŠKD (after-school clubs inside the school), most ŠJ (canteens inside schools/kindergartens) — useful only as attributes. Map ZUŠ and their branches, CVČ, internáty, MŠ, special schools, poradenské centrá, jazykové školy. The tag for centrá poradenstva a prevencie is an open question.
- **ZBGIS:** only building-use codes in layer *budova* (BFC "Škola" 15, "Univerzita/Fakulta, vysoká škola" 60; the KTO says internát and jedáleň take the BFC of their school). No school types, names or IDs, so RIS adds everything above building level.
- **Licence:** the register is a statutory public list (sieť škôl a školských zariadení, zákon 596/2003), so individual entries are likely "úradný dokument"; the database right of the ministry is not addressed on the portal. The ministry already releases RIS-derived data as CC BY 4.0, so ask MŠVVaM (via its open-data contact) to publish the RIS register in the national catalogue under CC BY 4.0 / CC0 and for OSM consent.
- **Contacts:** RIS / crinfo.iedu.sk operator (CVTI SR, regional-education data department); MŠVVaM open data.
- **Other school datasets seen:** city lists (Snina, Myjava, Svidník, Zlaté Moravce, Prešov, Bratislava ZUŠ 2024, CC BY 4.0) and Prešovský kraj "Školské zariadenia" (PDM, host unreachable on 30 Sep 2026) are subsets of RIS.

## Wiki entry
```
=== RIS – Register škôl a školských zariadení ===
* dataset: Register škôl a školských zariadení (Reg_SaSZ), Register zariadení predprimárneho vzdelávania
* správca: [https://crinfo.iedu.sk/risportal/ MŠVVaM SR – RIS]
* licencia: neuvedená (súhrnný dataset ministerstva z RIS je CC BY 4.0) [https://crinfo.iedu.sk/risportal/register/]
* dátové primitívy: body (len adresy so súpisným a orientačným číslom)
* odkaz: https://crinfo.iedu.sk/risportal/register/ExportCSV?id=1
* navrhované značky: {{tag|amenity|school}}, {{tag|amenity|kindergarten}}, {{tag|amenity|music_school}}, {{tag|ref:eduid|<EDUID>}}, {{tag|website}}
* poznámka: 17 639 škôl a zariadení v prevádzke vrátane 1 656 ZUŠ (1 245 elokovaných pracovísk) a 599 CVČ; v OSM asi 230 ZUŠ, 55 CVČ a 36 amenity=music_school.
```
