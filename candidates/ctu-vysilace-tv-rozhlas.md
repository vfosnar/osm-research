# ČTÚ – Přehled televizních a rozhlasových vysílačů (licensed DVB-T2 TV, FM, DAB+ and AM broadcast transmitters)

| Field | Value |
|---|---|
| publisher | Český telekomunikační úřad (ČTÚ), IČO 70106975 |
| url | https://data.ctu.gov.cz/sites/default/files/imports/import_televize/prehled_opravneni_televizni_vysilace.csv ; https://data.ctu.gov.cz/sites/default/files/imports/import_rozhlas/prehled_rozhlasovych_kmitoctu.csv (NKOD: https://data.gov.cz/zdroj/datové-sady/70106975/a6a1de163e0f92a10e91ba9430cf93cb and .../1ae10bf4520f6f96d0c459fed5f0236c) |
| format | CSV (comma, UTF-8); XLSX export also available |
| coords | yes (degrees/minutes/whole seconds plus decimal lon/lat with 4 decimals, about 10–30 m precision) |
| records | TV 470 rows (DVB-T, one per transmitter×multiplex); radio 1,164 rows (FM 995, DAB 165, AM 4). Deduplicated to 796 distinct transmitter sites (rounded to 0.001°). |
| osm_tags | existing man_made=mast\|tower\|communications_tower + tower:type=communication: add communication:television=yes / communication:radio=yes (with ele, name). A new site gets man_made=mast + tower:type=communication. The ANT_ID (antenna ID) could serve as ref:CZ:ctu (new key). |
| osm_count_cz | man_made=mast 2,831; man_made=tower 5,941; tower:type=communication 3,715; communication:television=yes 104; communication:radio=yes 68 (Geofabrik taginfo 2026-09-27) |
| license | NKOD terms: no copyright work, not a protected database, no sui generis right (NKOD maps it to CC0). ČTÚ's own "Podmínky užití otevřených dat" allow copying, distribution and commercial use. |
| license_url | https://data.gov.cz/podmínky-užití/neobsahuje-autorská-díla/ ; http://ctu.gov.cz/o-otevrenych-datech-ctu |
| license_status | ok |
| update_freq | daily (NKOD) |
| impact | 2 |
| verified | yes |

## Try it

- **Map preview:** [samples/ctu-vysilace-tv-rozhlas.geojson](../samples/ctu-vysilace-tv-rozhlas.geojson) has 145 transmitter sites in the central Bohemia bbox 13.4,49.5,15.6,50.6. Each site groups the TV and radio licence rows that share a position rounded to 0.001°, with its services (DVB-T/FM/DAB/AM) and the proposed `communication:*` tags. `osm_mast_or_tower_within_200m` is false for 76 of them (Postpass, 2026-09-27).
- **QGIS:** save both CSVs from the url row, then use *Layer → Add Layer → Add Delimited Text Layer…*: CSV, comma, UTF-8, X = `Zeměpisná délka`, Y = `Zeměpisná šířka`, CRS EPSG:4326.

## Notes
- Postpass check: 376 of the 796 distinct sites (47%) have a man_made=mast/tower/communications_tower or tower:type=communication within 200 m. About 420 broadcasting sites therefore have no mast in OSM at all. Many of the others lack communication:television/radio, which only about 170 objects carry nationwide.
- Attributes include site name (PRAHA and KOMAROV are two rows in the TV file), elevation (Výška nad mořem), ERP, channel/frequency, programme/multiplex, polarisation. Map only site-level facts (mast, ele, communication:*). Frequencies and programmes are not usually mapped in OSM.
- Caveat: licensed coordinates are sometimes rounded to whole seconds, and small gap-filler transmitters are often on existing buildings or chimneys. Use the data as a review layer, not a blind import.
- This is not gsmweb.cz BTS (a known source, mobile cells). It covers broadcast only.
- Wiki pages read: Tag:man_made=mast, Tag:tower:type=communication, Key:communication:television (requires man_made=tower or communications_tower + tower:type=communication).
- The ČTÚ payphone list (Veřejné telefonní automaty) is already on Cs:Česko/freemap and obsolete since 2021, so it is not proposed.

## Wiki entry
```
===Rozhlasové a televizní vysílače (ČTÚ)===
* dataset: Televizní vysílače; Rozhlasové vysílače
* gestor: [https://ctu.gov.cz/ Český telekomunikační úřad]
* licence: neobsahuje autorská díla, není chráněnou databází (CC0) [https://data.gov.cz/zdroj/datové-sady/70106975/a6a1de163e0f92a10e91ba9430cf93cb]
* datové primitivy: body
* odkaz: https://data.ctu.gov.cz/sites/default/files/imports/import_televize/prehled_opravneni_televizni_vysilace.csv
* navržený tag {{tag|man_made|mast}} + {{tag|tower:type|communication}}, {{tag|communication:television|yes}}, {{tag|communication:radio|yes}}
* poznámka: 796 vysílacích stanovišť (DVB-T2, FM, DAB+), u 53 % z nich není v OSM do 200 m žádný stožár ani věž
```
