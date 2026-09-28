# MPSV – Dětské skupiny (register of children's groups, 2,423 active childcare groups)

| Field | Value |
|---|---|
| publisher | Ministerstvo práce a sociálních věcí (MPSV), IČO 00551023; NKOD record https://data.gov.cz/zdroj/datové-sady/00551023/10990b435fc0b7a04f39582ffe5af9e4 |
| url | https://data.mpsv.cz/portal/api/reports/by-table/detske_skupiny_evid_poskyt_seznam_akt_odata/data/csv?fileName=detske_skupiny_evidendce_poskytovatelu_data (also `/data/json`); documentation https://data.mpsv.cz/web/data/detske-skupiny |
| format | CSV (`;`, UTF-8 with BOM, 1.1 MB) / JSON |
| coords | address-only (`misto_poskytovani_ds` = "street number, town - part, postcode"); geocoded here with the ČÚZK RÚIAN geocoder |
| records | 3,140 rows (2026-09-28): **2,423 Aktivní**, 31 Pozastavené, 686 Zaniklé; stable id `kod_detske_skupiny` (DS00003…), name, capacity (34,335 places in active groups), provider name and IČO, dates of authorisation, suspension and closure |
| osm_tags | `amenity=childcare` (Tag:amenity=childcare: "a place where children are looked after which is not a kindergarten", nursery/daycare for children too young for kindergarten) + `name`, `operator`, `capacity`, `ref:mpsv_ds=DSxxxxx` |
| osm_count_cz | taginfo 2026-09-28: amenity=childcare 141 (88 nodes, 53 ways); amenity=kindergarten 3,238 |
| license | Not a copyright work, not a copyright-protected database, no sui generis database right (NKOD terms of use); NKOD maps the terms to CC0; the file **contains personal data** (per NKOD) |
| license_url | https://data.gov.cz/podmínky-užití/není-chráněna-zvláštním-právem-pořizovatele-databáze/ |
| license_status | ok |
| update_freq | daily (NKOD accrualPeriodicity DAILY) |
| impact | 4 |
| sync_fit | Sync (points after geocoding, stable `kod_detske_skupiny`, one tag class amenity=childcare; closures come as stav Zaniklé) |
| verified | yes |

## Try it
- **Map preview:** [samples/mpsv-detske-skupiny.geojson](../samples/mpsv-detske-skupiny.geojson): 161 of the 165 active
  children's groups in Brno, geocoded to RÚIAN address points; property `osm_2026_09_28` says what OSM has within 100 m.
  105 of them have nothing.
- **QGIS:** *Layer → Add Layer → Add Delimited Text Layer*, file name =
  the CSV URL above, File format *Custom delimiters* → Semicolon, Geometry definition *No geometry*. Filter
  `"stav_opravneni_ds" = 'Aktivní'`. For points, geocode `misto_poskytovani_ds` (the RÚIAN geocoder below worked for 73 %).
- **Geocoder used (tested 2026-09-28):**
  `https://ags.cuzk.gov.cz/arcgis/rest/services/RUIAN/Vyhledavaci_sluzba_nad_daty_RUIAN/MapServer/exts/GeocodeSOE/findAddressCandidates?SingleLine=Komenského 1100 Řevnice&f=json&outSR=4326`
  returns the RÚIAN address point (candidate `Type` = AdresniMisto, score 100). The full string with postcode
  often returns nothing; "street number town" works best.

## Notes
- **What it adds:** children's groups (dětské skupiny, Act 247/2014) are the main childcare for children
  under three in Czechia and a large share of the places for 3–6 year-olds. They are registered at MPSV, not in
  the MŠMT school register (rejstřík škol), so they are not in ZABAGED Škola/Školské zařízení nor in the MŠMT
  school data. Nothing from this register is on Cs:Česko/freemap, Cs:Zdroje_v_jednani or in Sync's config.toml.
- **Gap, measured (Postpass 2026-09-28, 100 m radius around the geocoded address):** 1,773 of 2,423 active
  groups geocoded (score ≥ 90). Of those, **57** have an amenity=childcare or a "Dětská skupina" name nearby,
  243 have a kindergarten nearby (many groups are run by or inside a kindergarten or school), 43 a
  community_centre, and **1,430 have nothing**. Brno: 105 of 161 nothing; Praha: 327 of 428 nothing.
  OSM's 141 childcare objects for the whole country compare with 2,423 registered groups.
- **Caveats:**
  - Address only. 650 addresses did not geocode on the first pass (village addresses written "č. p.",
    town parts, typos); a second pass with RÚIAN address codes or a manual queue is needed.
  - Several groups often share one address (company groups, a provider with two groups in one building):
    one node per group with its own `ref`, or one node with the names joined, is a community decision.
  - Where the group sits inside a mapped kindergarten or school, add a separate node rather than retagging
    the kindergarten.
  - Personal data: providers include natural persons (column `poskytovatel_udaje` holds names of the
    authorised persons). Import only `nazev_ds`, capacity and code; use `operator` only for legal entities
    (the provider IČO distinguishes them).
  - `capacity` is the licensed capacity, not actual enrolment.
- **Suggested ref key:** `ref:mpsv_ds` (not in use in CZ per taginfo; no existing key for this register).
- **Contact:** MPSV, data.mpsv.cz (dataset contact point in NKOD).
- Wiki pages read: Tag:amenity=childcare.

## Wiki entry
```
===Dětské skupiny (MPSV)===
* dataset: Dětské skupiny – evidence poskytovatelů služby péče o dítě v dětské skupině
* gestor: [https://data.mpsv.cz/web/data/detske-skupiny Ministerstvo práce a sociálních věcí]
* licence: není autorské dílo ani chráněná databáze (podmínky užití NKOD, odpovídá CC0) [https://data.gov.cz/zdroj/datové-sady/00551023/10990b435fc0b7a04f39582ffe5af9e4]
* datové primitivy: body (jen adresa, nutné geokódovat přes RÚIAN)
* odkaz: https://data.mpsv.cz/portal/api/reports/by-table/detske_skupiny_evid_poskyt_seznam_akt_odata/data/csv?fileName=detske_skupiny_evidendce_poskytovatelu_data
* navržený tag {{tag|amenity|childcare}}, {{tag|capacity|<kapacita_ds>}}, {{tag|ref:mpsv_ds|<kod_detske_skupiny>}}
* poznámka: 2 423 aktivních dětských skupin s denní aktualizací; v OSM je amenity=childcare v ČR jen 141× a u 1 430 z 1 773 geokódovaných skupin není v okruhu 100 m nic
```
