# Kraje – lékařská pohotovostní služba (out-of-hours GP, paediatric and dental emergency with hours)

| Field | Value |
|---|---|
| publisher | Královéhradecký kraj (IČO 70889546), Karlovarský kraj (70891168), Liberecký kraj (70891508), Olomoucký kraj (60609460) |
| url | KHK: https://www.datakhk.cz/api/download/v1/items/285bc3ecf55b4c718069f05a4471815b/geojson?layers=0 ; KV: https://www.datazapad.cz/api/download/v1/items/72aa9de6abc94f949f3959e70e0d241d/geojson?layers=0 ; LK: https://www.datalk.cz/api/download/v1/items/38d9797b83044ada9c674c08b54f8548/geojson?layers=0 ; OK: https://www.dataok.cz/api/download/v1/items/d32f08a1db4f4ec9bf4ede6e7b0282c1/geojson?layers=0 |
| format | GeoJSON / CSV / ArcGIS FeatureServer (ArcGIS Hub portals of the kraje) |
| coords | yes (WGS84 x/y attributes; OK also carries ID_MISTO_NRPZS) |
| records | KHK 11 (adult 6, child 5); KV 16 (LSPP adult/child 9, surgical 1, dental 4, pharmacy 2, one online service without geometry); LK 13 (adult 6, child 5 of which 1 marked Platnost=0 "zrušeno", dental 2); OK 157 rows = 28 fixed LSPP rows (7 hospitals × adult/child × weekday/weekend) + 120 dated dental-rota rows (2025-01 to 2026-01) + 9 dated pharmacy rows |
| osm_tags | amenity=doctors + healthcare=doctor + healthcare:speciality=emergency (children: emergency;paediatrics); dental: amenity=dentist + healthcare=dentist + healthcare:speciality=emergency; opening_hours; phone; website |
| osm_count_cz | healthcare:speciality=emergency 7, healthcare:speciality=urgent 0 (taginfo 2026-09-27). Postpass 2026-09-28: of the 37 distinct fixed LSPP places, 32 have an amenity=hospital within 300 m but only 5 have an OSM object named "*pohotov*" within 300 m |
| license | NKOD terms of use: no copyright work, not a copyright-protected database, no sui generis right, no personal data (mapped to CC0) — identical for all four datasets |
| license_url | https://data.gov.cz/zdroj/datové-sady/70889546/c2cffa4f63107b7402360343145042b0 ; https://data.gov.cz/zdroj/datové-sady/70891168/13ff2662075c3d7fe6eb8e5f5ec34e6f ; https://data.gov.cz/zdroj/datové-sady/70891508/fea8b687ddcb73389e7f69043fd603b8 ; https://data.gov.cz/zdroj/datové-sady/60609460/5fd37b621ac004ab1690ac3761dbe654 |
| license_status | ok |
| update_freq | KV quarterly; KHK and OK irregular (KHK layer last edited 2025-01-13); LK "other" (layer last edited 2025-12-31) |
| impact | 2 |
| sync_fit | MapRoulette / manual (≈45 points, mostly inside hospital areas; needs placing at the right pavilion and opening_hours review); too small and ID-less for Sync |
| verified | yes |

## Try it
- **Map preview:** [samples/kraje-lspp-pohotovosti.geojson](../samples/kraje-lspp-pohotovosti.geojson): 50 fixed out-of-hours services from all four kraje (KHK 11, KV 13 without the 2 pharmacies and the online service, LK 12 without the cancelled row, OK 14). Each point has `suggested:*` tags; 22 have a ready `suggested:opening_hours` (KV and LK publish per-weekday columns), the rest carry the source hours text in `hours_src`.
- **QGIS:** *Layer → Add Layer → Add Vector Layer*, source type *Protocol: HTTP(S)*, paste any GeoJSON URL from the table (EPSG:4326). Or *Add ArcGIS REST Server Layer* with `https://services6.arcgis.com/ogJAiK65nXL1mXAW/arcgis/rest/services` (KHK, layer "Lékařská pohotovostní služba"), `https://services7.arcgis.com/46Lck1orT7mvuzK5/arcgis/rest/services` (LK, "Pohotovosti_LK") or `https://gispub.kr-olomoucky.cz/pub/rest/services/OpenData` (OK, "pohotovostní služba v Olomouckém kraji"). All three FeatureServer layers answered `?f=json` with esriGeometryPoint.

## Notes
- **Why it matters:** "where is the pohotovost tonight" is one of the most common health searches, and the answer is usually a specific pavilion inside a hospital with evening/weekend hours. OSM has the hospitals (32 of 37 places have an amenity=hospital within 300 m) but almost never the LSPP itself: only 5 of 37 have a nearby object named "pohotovost", and healthcare:speciality=emergency is used 7 times in the whole country.
- **Not in NRPZS/ZABAGED:** the NRPZS extract has no LSPP form of care (0 rows with "pohotov" in druh/forma), and the ZABAGED healthcare layer is at facility level. The kraje organise LSPP under zákon 372/2011 Sb. and these four publish it as open data. NKOD search (title regex pohotovost/LSPP, 2026-09-28) found no other kraj; Praha, JMK, MSK and the rest would have to be asked.
- **Common schema:** KHK, KV and LK use near-identical fields (nazev, cilova_skupina, per-day ordinacni_hodiny_*, kod_obce, cislo_domovni, www, wkt with lat/lon swapped as in NRPZS). KV adds Místo_pohotovostní_služby (pavilion, floor) and Typ (LSPP / zubní / lékárenská). OK uses a different schema with ID_MISTO_NRPZS, which links to NRPZS ZZ_misto_poskytovani_ID.
- **Caveats:**
  - The OK dental rows are a dated rota (one practice per weekend day). They cannot be mapped as permanent POIs; only the 7 hospital LSPP places are usable. The same applies to the pharmacy rows (holiday opening).
  - LK keeps a cancelled service (Turnov children, Platnost=0, all hours "zrušeno"). Filter on Platnost=1.
  - Opening hours change often (services are cut back). The datasets are the only machine-readable source, but a one-off import will go stale; tag `check_date:opening_hours` and consider a periodic MapRoulette re-check.
  - Coordinates are the hospital address point, not the pavilion. Move the node to the correct building using the `location`/`popis_mista` text.
- **Tagging:** Cs:Tag:healthcare:speciality=emergency describes exactly this case ("Lékařská stanice první pomoci … otevřeno mimo ordinační dobu běžných lékařů"). Wiki pages read: Cs:Tag:healthcare:speciality=emergency, Cs:Tag:healthcare:speciality=urgent (urgentní příjem, non-stop, not LSPP), Key:healthcare, Key:emergency. emergency=yes on the hospital is a different thing (emergency department) and is not proposed here.
- **Contacts:** the open-data teams of each kraj (datakhk.cz, datazapad.cz, datalk.cz, dataok.cz). A request to the Asociace krajů to publish all 14 regions in the KHK/LK schema would turn this into a national layer.

## Wiki entry
```
===Kraje – lékařská pohotovostní služba===
* dataset: Lékařská pohotovostní služba (Královéhradecký, Liberecký kraj); Lékařská a lékárenská pohotovostní služba v Karlovarském kraji; Lékařská a lékárenská pohotovostní služba v Olomouckém kraji
* gestor: [https://www.datakhk.cz/ Královéhradecký kraj], [https://www.datazapad.cz/ Karlovarský kraj], [https://www.datalk.cz/ Liberecký kraj], [https://www.dataok.cz/ Olomoucký kraj]
* licence: podmínky užití NKOD – neobsahuje autorská díla, není chráněná databáze (CC0) [https://data.gov.cz/zdroj/datové-sady/70891508/fea8b687ddcb73389e7f69043fd603b8]
* datové primitivy: body
* odkaz: https://www.datalk.cz/api/download/v1/items/38d9797b83044ada9c674c08b54f8548/geojson?layers=0
* navržený tag {{tag|amenity|doctors}} + {{tag|healthcare|doctor}} + {{tag|healthcare:speciality|emergency}} (děti: emergency;paediatrics), {{tag|opening_hours}}
* poznámka: z 37 míst LSPP ve 4 krajích má v OSM do 300 m objekt s názvem „pohotovost“ jen 5; healthcare:speciality=emergency je v ČR použito 7×
```
