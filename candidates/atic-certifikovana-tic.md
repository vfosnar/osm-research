# A.T.I.C. ČR – certifikovaná turistická informační centra (Jednotná klasifikace TIC)

| Field | Value |
|---|---|
| publisher | Asociace turistických informačních center ČR (A.T.I.C. ČR), IČO 62930460, Na Pankráci 332/14, Praha 4; office@aticcr.cz, tel. 799 561 441 |
| url | https://www.aticcr.cz/assets/File.ashx?id_org=200039&id_dokumenty=3930 ("Všechna certifikovaná TIC k 10.8.2026", XLSX, 95 kB); list of all versions: https://www.aticcr.cz/certifikovana%2Dtic/ds-1113/p1=3110 |
| format | XLSX (one sheet `atic_10-08-26`) |
| coords | address-only (street + house number + PSČ + town); 510 of 546 geocode to a RÚIAN address point with a simple street/number/PSČ match |
| records | 546 certified TICs (members and non-members). Class (`trida`): A 27, B 257, C 261. Columns: trida, clen (member), tic (name), mesto, ulice, psc, pravni forma, e-mail, telefon, IC (operator IČO), certifikace (date), prubezna cert., kraj, krajské / oblastní / lokální DMO, q (Značka Q), www |
| osm_tags | tourism=information + information=office (wiki Tag:information=office, status de facto); name, phone, email, website (contact data) |
| osm_count_cz | information=office 723 (taginfo 2026-09-27). Local match against the 2026-09-27 Czechia extract (Postpass unavailable): 740 information=office objects, of which 238 have `website`, 190 `phone`, 130 `email` |
| license | none stated (no licence or terms on aticcr.cz; the file is published for download without conditions) |
| license_url | |
| license_status | unclear |
| update_freq | several times a year (versions dated 2023-10, 2024-02, 2024-04, 2024-06, 2024-11, 2025-01, 2025-09, 2026-01, 2026-05, 2026-08) |
| impact | 3 |
| sync_fit | MapRoulette (address-only geocoding, attribute enrichment, no stable id) |
| verified | yes |

## Try it
- **Map preview:** none, because the licence is unclear.
- **QGIS:** download the XLSX from the URL above, then *Layer → Add Layer → Add Vector Layer…*, source type *File*, pick the `.xlsx`; it loads as a table without geometry (546 rows, header in row 1). To place it on a map, join on address with RÚIAN address points or geocode it.
- **Web:** the association's per-region lists: https://www.aticcr.cz/informacni%2Dcentra%2Ddle%2Dkraju%2Dcr/os-1353/p1=2293

## Notes
- **What it is:** A.T.I.C. ČR certifies tourist information centres under the "Jednotná klasifikace turistických informačních center ČR" (classes A, B, C, with a re-certification cycle) and publishes the full list of certified offices several times a year. It is a curated national list of real, staffed information offices with verified contact data. It is not on `Cs:Česko/freemap` (including Potencionální zdroje), `Cs:Zdroje_v_jednani` or the Sync `config.toml`, and ZABAGED has no information-office layer. `regional-tourism-hubs.md` covers kraj-level infocentrum layers (small, one kraj each); this list is national and maintained by the certifying body.
- **Gap (local match against the 2026-09-27 Czechia extract; Postpass returned 503):** 510 of 546 TICs were geocoded to a RÚIAN address point (street + number + PSČ, then house number + PSČ). Against the 740 OSM `tourism=information` + `information=office` objects:
  - 226 of 510 (44 %) certified TICs have **no information office within 150 m** of their address. For 99 of them the nearest `tourism=information` object within 150 m is a guidepost, board or map, not an office. Missing offices by kraj: Středočeský 29, Jihomoravský 26, Královéhradecký 24, Vysočina 24, Plzeňský 22, Olomoucký 20, Pardubický 16, Ústecký 15, Jihočeský 12, Moravskoslezský 12, Zlínský 9, Liberecký 8, Karlovarský 7, Praha 2.
  - 284 matched an OSM office within 150 m; of these 165 have no website, 187 no phone, 216 no e-mail. The list fills those.
- **Caveats:** no stable record id (the `c.r.` column is only a row number); key on the operator IČO + town, or on the OSM id after a first match. Addresses are typed by hand (non-breaking spaces, "nám.", notes in brackets), so 36 rows did not geocode automatically. A class (A/B/C) has no established OSM key; do not invent one.
- **Licence:** nothing is stated. The list is a simple compilation of facts (names, addresses, contacts), but the association may hold the database right. Ask A.T.I.C. ČR (office@aticcr.cz, sekretariát Ing. Barbora Hodačová) for consent for OSM use.
- Wiki pages read: Tag:information=office.

## Wiki entry
```
===A.T.I.C. ČR – certifikovaná turistická informační centra===
* dataset: Všechna certifikovaná TIC (Jednotná klasifikace TIC v ČR)
* gestor: [https://www.aticcr.cz/ Asociace turistických informačních center ČR]
* licence: neuvedena – nutno požádat o souhlas
* datové primitivy: body (pouze adresy)
* odkaz: https://www.aticcr.cz/certifikovana%2Dtic/ds-1113/p1=3110
* navržený tag {{tag|tourism|information}} + {{tag|information|office}}, {{tag|phone}}, {{tag|email}}, {{tag|website}}
* poznámka: 226 z 510 certifikovaných TIC nemá v OSM do 150 m od adresy žádné infocentrum; u 165 nalezených chybí web
```
