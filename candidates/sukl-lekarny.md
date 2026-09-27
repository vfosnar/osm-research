# SÚKL Seznam lékáren (list of pharmacies incl. opening hours)

| Field | Value |
|---|---|
| publisher | Státní ústav pro kontrolu léčiv (SÚKL), IČO 00023817 |
| url | https://opendata.sukl.cz/?q=katalog/seznam-lekaren (monthly ZIP; current file https://opendata.sukl.cz/soubory/SOD20260925/LEKARNY20260925.zip, verified 2026-09-27); NKOD distribution https://opendata.sukl.cz/soubory/NKOD/LEKARNY/nkod_lekarny_seznam.csv |
| format | ZIP of 3 CSV files (';'-separated, cp1250): lekarny_seznam.csv, lekarny_prac_doba.csv, lekarny_typ.csv |
| coords | address-only (text address: MESTO, ULICE "street č.p./č.o.", PSC; no RÚIAN code) |
| records | 2,689 (2026-09-25 file); 2,673 have opening-hours rows |
| osm_tags | amenity=pharmacy + healthcare=pharmacy, dispensing=yes, name, opening_hours, phone, email, website, ref:SUKL=&lt;KOD_PRACOVISTE&gt; |
| osm_count_cz | amenity=pharmacy 2,557; ref:SUKL 1,142 objects / 1,106 distinct values (of which 805 match the current SÚKL file, 301 are stale/invalid); opening_hours on 2,286 pharmacies |
| license | No copyright work, not a copyright-protected database, no sui generis database right (NKOD terms-of-use); NKOD also maps it to CC0 |
| license_url | https://data.gov.cz/zdroj/datové-sady/00023817/ee950579137405421560185466ffb5be (terms: https://data.gov.cz/podmínky-užití/neobsahuje-autorská-díla/ , .../není-autorskoprávně-chráněnou-databází/ , .../není-chráněna-zvláštním-právem-pořizovatele-databáze/) |
| license_status | ok |
| update_freq | monthly |
| impact | 3 |
| verified | yes |

## Try it
- **Map preview:** [samples/sukl-lekarny.geojson](../samples/sukl-lekarny.geojson): all 39 pharmacies in Olomouc, geocoded against the RÚIAN address points of obec 500496 (`https://vdp.cuzk.gov.cz/vymenny_format/csv/20260831_OB_ADR_csv.zip`, file `20260831_OB_500496_ADR.csv`, S-JTSK converted with pyproj). All 39 matched on street + č.p./č.o. The sample carries `ref:SUKL` and `opening_hours`. OSM has 42 pharmacies in the Olomouc bbox, 14 of them with ref:SUKL (Postpass 2026-09-27).
- **QGIS:** this is an attribute table only (no coordinates). Use *Layer → Add Layer → Add Vector Layer*, source type *Protocol: HTTP(S)*, URI `https://opendata.sukl.cz/soubory/NKOD/LEKARNY/nkod_lekarny_seznam.csv` (UTF-8 with BOM, comma). The CSVs inside the monthly ZIP are cp1250 with ';'.

## Notes
- Downloaded and parsed the 2026-09-25 ZIP. Columns: NAZEV, KOD_PRACOVISTE (11-digit, used as ref:SUKL in OSM already), KOD_LEKARNY, ICZ, ICO, MESTO, ULICE, PSC, head pharmacist (name, i.e. personal data: do not import), WWW, EMAIL, TELEFON, ERP, TYP_LEKARNY, ZASILKOVY_PRODEJ (mail order, 227), POHOTOVOST (emergency service, 16).
- Opening hours come as one row per day (PO, UT, ST, CT, PA, SO, NE, SVATEK) with OD/DO times. 69 pharmacy-days have several intervals (lunch breaks). They convert cleanly to `opening_hours`, and SVATEK maps to `PH`.
- Types (TYP_LEKARNY): Z 2,073; OOVL 205 (separate dispensing branch, "odloučené oddělení výdeje"); Z/OOVL 172; hospital pharmacies (NO/NZ/L/LO) about 200; A (military) 5. Map OOVL as a pharmacy too, but check how it is tagged locally.
- Gap: in a Postpass test, 44 of 50 randomly sampled pharmacies (NRPZS coordinates) already had an OSM pharmacy within 75 m, so about 88% are present. Most of the value is therefore maintenance, not new features:
  (a) 1,884 current SÚKL pharmacies carry no ref:SUKL in OSM, so adding refs would enable ongoing sync;
  (b) 301 ref:SUKL values in OSM no longer exist in SÚKL, which points to closed or renamed pharmacies. One value (00213576554) sits on 34 objects, which is clearly wrong;
  (c) opening_hours and contact details can be checked and updated;
  (d) roughly 300 to 350 pharmacies are missing.
- No coordinates are provided. Match on ref:SUKL where it exists. Otherwise geocode the address against RÚIAN (the ULICE field is "street č.p./č.o.", which parses well) or match by name/address to OSM. NRPZS (ÚZIS) also lists 2,515 "Lékárna" places with GPS, but it is CC BY 4.0 (see uzis-nrpzs-ambulantni.md), so do not use it for positions without a waiver.
- ref:SUKL has no OSM wiki page (Key:ref:SUKL does not exist). It is used de facto with the KOD_PRACOVISTE value. Document it on the Cs wiki before any sync.
- Wiki pages read: Tag:amenity=pharmacy and Cs:Tag:amenity=pharmacy (dispensing=yes/no, healthcare=pharmacy, opening_hours).
- Dr.Max is already covered by the AllThePlaces sync. Do not duplicate it; use SÚKL only to add ref:SUKL to those objects.
- Contact: SÚKL open data, opendata.sukl.cz (the "Podmínky užití otevřených dat" page on the portal).

## Wiki entry
```
===Seznam lékáren SÚKL===
* dataset: Seznam lékáren
* gestor: [https://www.sukl.cz/ Státní ústav pro kontrolu léčiv]
* licence: neobsahuje autorská díla, není chráněnou databází, CC0 [https://data.gov.cz/zdroj/datové-sady/00023817/ee950579137405421560185466ffb5be]
* datové primitivy: body (pouze adresy)
* odkaz: https://opendata.sukl.cz/?q=katalog/seznam-lekaren
* navržený tag {{tag|amenity|pharmacy}}, {{tag|ref:SUKL|<KOD_PRACOVISTE>}}
* poznámka: v OSM 2 557 lékáren, ale 1 884 bez ref:SUKL a 301 neplatných ref:SUKL; vhodné hlavně pro údržbu a otevírací doby
```
