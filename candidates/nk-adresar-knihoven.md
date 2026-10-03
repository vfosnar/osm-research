# Centrální adresář knihoven a informačních institucí v ČR (ADR)

| Field | Value |
|---|---|
| publisher | Národní knihovna České republiky, IČO 00023221 |
| url | https://aleph.nkp.cz/data/adr.xml.gz (NKOD: https://data.gov.cz/zdroj/datové-sady/00023221/1099355216) |
| format | MARCXML (gzip, ~2 MB), custom field tags (SGL, NAZ, ADR, OTD, TYP, EMK, ...) |
| coords | yes (ADR $g in DMS; record STG505 has 49°17'48.84"N, 13°45'25.95"E), present on 6,643 of 8,155 records |
| records | 8,155 total; 6,375 active (no STT "KNIHOVNA ZRUŠENA!/ZRUŠENÁ INSTITUCE!" flag), 6,167 active with coords; 5,163 active public (obecní/městská/krajská) libraries with coords |
| osm_tags | amenity=library, name, opening_hours, website, email, phone, operator, ref:isil=CZ-&lt;sigla&gt; |
| osm_count_cz | amenity=library 1,556; ref:isil 4 (taginfo, 2026-10-04): CZ-NJG512 (node 13957447852), CZ-000002256 (node 2106024220), FMG515 without prefix (way 1430217235), and one German museum; ref:CZ:sigla 0 |
| license | No copyright work, not a copyright-protected database; sui generis right waived under CC0 1.0 (NKOD terms-of-use) |
| license_url | https://data.gov.cz/zdroj/datové-sady/00023221/1099355216 (terms: https://data.gov.cz/podmínky-užití/neobsahuje-autorská-díla/ , .../není-autorskoprávně-chráněnou-databází/ , https://creativecommons.org/publicdomain/zero/1.0/) |
| license_status | ok |
| update_freq | weekly |
| impact | 5 |
| sync_fit | Sync (points, stable ref:isil sigla, category → amenity=library 1:1) |
| verified | yes |

## Try it
- **Map preview:** [samples/nk-adresar-knihoven.geojson](../samples/nk-adresar-knihoven.geojson): all 84 active libraries with coordinates in okres Strakonice, 72 of them obecní. It includes sigla, type, address, website, and `opening_hours` converted from OTD. Librarian names and e-mails are dropped.
- **QGIS:** there is no direct load. The source is gzipped MARCXML with coordinates as DMS text. Use the sample, or convert `https://aleph.nkp.cz/data/adr.xml.gz` with a script.
- **Web:** Aleph search of the directory: https://aleph.nkp.cz/F/?func=file&file_name=find-b&local_base=ADR

## Notes
- Downloaded and parsed the current dump. Type breakdown (TYP $b): obecní knihovna 5,062 (4,842 active); ostatní specializovaná 1,045; městská 521; research institute 375; university 290; medical 228; museum 180; state administration 165; school 141; others. Import the public types (obecní, městská, krajská, národní). Specialised, corporate and ministry libraries are often not publicly accessible and need `access=` or should be skipped.
- Opening hours (OTD) are structured, with subfields 1 to 7 per weekday (record STG505: `1: 8:00-11:00; 13:00-17:30`), which converts well to `opening_hours`. Some records only give a URL in $p ("aktuální otevírací doba: https://..."). Those map to `opening_hours:url`.
- Stable IDs: SGL (sigla; STG505 and STG001 appear in the dump), plus the Aleph doc number in DRL and EMK (the Ministry of Culture registration number under the libraries act 257/2001). The ref is `ref:isil=CZ-<sigla>` (owner decision 2026-10-04), the form `CZ-NJG512` already uses in OSM; whether NK registers exactly this as the Czech ISIL is unconfirmed. On import, `CZ-000002256` (node 2106024220) and the unprefixed `FMG515` (way 1430217235) need fixing to that form.
- Gap: in a Postpass test, only 8 of 50 random active public libraries had an OSM amenity=library within 100 m (16%). That suggests roughly 4,000+ municipal libraries are missing. Many village libraries sit inside the obecní úřad or kulturní dům, so a node inside the building (or `amenity=library` on a POI with `level`) is the usual pattern.
- Personal data: the JMN field (director or librarian name) and some e-mails are personal. Do not import JMN. NKOD flags the dataset as containing personal data.
- Caveats: coordinates are geocoded by NK, often at the address point, and some may be old. The AKT field holds the last update date (many records are from 1990s–2005, but the public-library records are mostly recent). Validate against RÚIAN ADR and the town-hall position.
- Wiki pages read: Tag:amenity=library and Cs:Tag:amenity=library (opening_hours, ref:isil, operator), Key:ref:isil.
- Municipal subsets (Plzeň "Knihovny", Liberecký kraj "Knihovny v Libereckém kraji", Huntířov) are redundant with this national source.
- Contact: Knihovnický institut NK ČR (adresář knihoven), https://www.nkp.cz/ ; Aleph ADR base https://aleph.nkp.cz/F/?func=file&file_name=find-b&local_base=ADR

## Wiki entry
```
===Adresář knihoven NK ČR===
* dataset: Centrální adresář knihoven a informačních institucí v ČR (ADR)
* gestor: [https://www.nkp.cz/ Národní knihovna ČR]
* licence: neobsahuje autorská díla, není chráněnou databází, CC0 [https://data.gov.cz/zdroj/datové-sady/00023221/1099355216]
* datové primitivy: body
* odkaz: https://aleph.nkp.cz/data/adr.xml.gz
* navržený tag {{tag|amenity|library}}, {{tag|ref:isil|CZ-<sigla>}}
* poznámka: ~5 160 veřejných knihoven se souřadnicemi, v OSM 1 556 amenity=library; otevírací doba strukturovaně po dnech
```
