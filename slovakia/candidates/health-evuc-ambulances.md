# e-VÚC: ambulantné zdravotnícke zariadenia, ambulantná pohotovosť a ZZS (doctors, dentists, specialists, out-of-hours and ambulance stations)

| Field | Value |
|---|---|
| publisher | The 8 samosprávne kraje (VÚC) as licensing authority for outpatient care (plus MZ SR / ÚDZS for some permits, visible in the IdZZ prefix). Portal e-VÚC operated by CRYSTAL CONSULTING, s.r.o. Open extract: Trnavský samosprávny kraj |
| url | National (HTML only): https://www.e-vuc.sk/ → region → *Ambulantné zdravotnícke zariadenia* / *Ambulantná pohotovosť* (e.g. https://www.e-vuc.sk/bsk/zdravotnictvo/ambulantne-zdravotnicke-zariadenia.html?page_id=60142); ZZS list per region https://www.e-vuc.sk/e-vuc/pre-poskytovatelov-zdravotnej-starostlivosti/ambulancie-zachrannej-zdravotnej-sluzby.html?page_id=153843. TTSK open extract "Ambulancie TTSK": https://rss-dcat-opendata-ttsk.hub.arcgis.com/api/download/v1/items/4bc784dd08b644c1ac82c685e76d6954/geojson?layers=0 |
| format | e-VÚC: HTML detail pages with a `maps.google.com/?q=lat,lon` link. TTSK: GeoJSON (declares WGS84 coordinates in the geometry) and CSV (`X`,`Y`, `F_Zemepisná_šírka_`, `F_Zemepisná_dĺžka_`) |
| coords | yes |
| records | e-VÚC home page (30 Sep 2026): 24,199 outpatient facilities (BBSK 2,529, BSK 5,567, KSK 3,468, NSK 2,547, PSK 3,129, TSK 2,084, TTSK 1,998, ŽSK 2,877); ambulantná pohotovosť BSK 75 (other regions not counted); ZZS: 474 distinct IdZZ across the 8 regional ZZS lists. TTSK extract: 1,921 facilities, all `F_Dátum_aktualizácie_` 2023-06 |
| osm_tags | amenity=doctors + healthcare=doctor + healthcare:speciality=* (general, gynaecology, paediatrics, …); amenity=dentist + healthcare=dentist; healthcare=sample_collection (mobilné odberové miesto); healthcare=nurse (ADOS); emergency=ambulance_station (ZZS stanovište); opening_hours; proposed ref:idzz |
| osm_count_sk | amenity=doctors 1,015; healthcare=doctor 754; amenity=dentist 580; amenity=clinic 384; healthcare:speciality 870; emergency=ambulance_station 34 (taginfo europe:slovakia, 2026-09-30) |
| license | e-VÚC: none stated. TTSK extract: CC BY 4.0 (catalogue) |
| license_url | https://creativecommons.org/licenses/by/4.0/ ; published-fields statement https://www.e-vuc.sk/e-vuc/pre-poskytovatelov-zdravotnej-starostlivosti/zoznam-zverejnovanych-udajov.html?page_id=66315 |
| license_status | needs_waiver (TTSK extract); unclear (national e-VÚC data) |
| update_freq | e-VÚC: live (providers edit in the AMBULANCIA app, regions approve opening hours). TTSK extract: frozen at June 2023 |
| impact | 5 |
| sync_fit | Sync for doctors and dentists (points, IdZZ, facility type → tags 1:1 via a lookup table of ~60 druhy); MapRoulette for ZZS stations (the list gives the stanovište name, not a position) and for clustered polyclinics where one OSM building holds dozens of ambulances |
| verified | partial (national pages read, not bulk-downloaded; TTSK extract downloaded and matched) |

## Try it
- **Map preview:** [../samples/health-evuc-ambulances.geojson](../samples/health-evuc-ambulances.geojson): the 475 TTSK facilities of okres Trnava (80 general practice, 77 dentists, 39 SVaLZ labs, 20 one-day surgery, 18 gynaecology, …) with `opening_hours` converted from the per-day fields and `osm_healthcare_within_50m` (306 true, 169 false; Postpass, 2026-09-30). The responsible-person field (`F_Odborný_zástupca_`) is dropped.
- **QGIS:** *Layer → Add Layer → Add Vector Layer → Protocol: HTTP(S)*, URI `https://rss-dcat-opendata-ttsk.hub.arcgis.com/api/download/v1/items/4bc784dd08b644c1ac82c685e76d6954/geojson?layers=0`; or the CSV variant (`…/csv?layers=0`, delimiter comma, X = `F_Zemepisná_dĺžka_`, Y = `F_Zemepisná_šírka_`, EPSG:4326).
- **Web:** e-VÚC pages above; "nearest out-of-hours service/hospital" at https://www.otvorenalekaren.sk/.

## Notes
- **What a record holds** (BSK detail page read 30 Sep 2026, `…/algeziologicka-ambulancia-bratislava-stare-mesto-cliniq-s.-r.-o..html?page_id=150738`): druh zariadenia, IdZZ `61-51179458-A0052`, odborné zameranie, place of operation including floor and room ("1. NP - m.č. 1.50 … prístup z ul. Gajova 2") — useful for `level`/indoor in polyclinics, insurers accepted (VšZP, Dôvera, Union), provider and IČO, approved ordinačné hodiny with validity date (split sessions such as `7:00-12:00 || 12:30-16:00`), coordinates. Absences/holidays are published too.
- **Stable ID:** IdZZ, see [health-evuc-pharmacies.md](health-evuc-pharmacies.md). The ZZS list shows that IdZZ also covers each ambulance crew (`51-17336210-A0093` …), so a ZZS stanovište may carry several IdZZ (RZP, RLP, "S" crews).
- **Gap:** TTSK extract matched with Postpass (2026-09-30): general practice 194 of 346 have any `amenity=doctors|clinic` / `healthcare=doctor|clinic|centre` within 100 m; dentists only 68 of 274 have `amenity=dentist`/`healthcare=dentist` within 100 m (206 missing, 75 %). In okres Trnava 169 of 475 facilities have no healthcare object at all within 50 m. The "within 100 m" hits are generous because one polyclinic node satisfies every ambulance inside it. ZZS: 474 ambulance IdZZ against 34 `emergency=ambulance_station` in OSM.
- **Personal data:** facility names often contain physicians' names ("Algeziologická ambulancia, MUDr. …"). e-VÚC publishes them deliberately (their statement: patients identify ambulances by the doctor's name), but OSM should keep `name` to the facility name and not import the doctor/nurse lists.
- **Tag mapping:** the ~60 `druh zariadenia` values map to `amenity=doctors` + `healthcare:speciality` (per Key:healthcare:speciality), `amenity=dentist`, `healthcare=laboratory` (spoločné vyšetrovacie a liečebné zložky), `healthcare=sample_collection` (mobilné odberové miesto, per Tag:healthcare=sample_collection), `healthcare=nurse` (ADOS). Wiki pages read: Tag:amenity=doctors, Key:healthcare:speciality, Tag:healthcare=sample_collection, Tag:healthcare=laboratory, Tag:healthcare=nurse, Tag:emergency=ambulance_station.
- **ZBGIS:** only building-use codes in layer *budova* (BFC "Zdravotné stredisko (súbor ambulancií)" 33, "Zdravotné zariadenie (samostatná ambulancia)" 357, "Nemocničná budova" 6). No facility-level objects, types, IDs or hours.
- **Rejected alternative:** NCZI "Sieť poskytovateľov zdravotnej starostlivosti SR" is CC BY-NC 4.0 in the catalogue and statistical → incompatible. The NCZI "Ročný výkaz …" datasets are statistics, not locations.
- **Licence and contacts:** as for pharmacies — one consent request covering the shared e-VÚC data (all 8 regions) would unlock pharmacies, ambulances, out-of-hours services and the social-services pages that some regions also keep on e-VÚC. Contacts: info@e-vuc.sk and the per-region addresses on https://www.e-vuc.sk/e-vuc/kontakty.html?page_id=2295.

## Wiki entry
```
=== e-VÚC – ambulancie, ambulantná pohotovosť a ZZS ===
* dataset: Ambulantné zdravotnícke zariadenia, Ambulantná pohotovosť, Ambulancie ZZS (e-VÚC); otvorený výťah TTSK „Ambulancie TTSK“
* správca: [https://www.e-vuc.sk/ samosprávne kraje SR (portál e-VÚC)], [https://www.trnava-vuc.sk/ Trnavský samosprávny kraj]
* licencia: e-VÚC bez uvedenej licencie; výťah TTSK CC BY 4.0 [https://creativecommons.org/licenses/by/4.0/]
* dátové primitívy: body
* odkaz: https://rss-dcat-opendata-ttsk.hub.arcgis.com/api/download/v1/items/4bc784dd08b644c1ac82c685e76d6954/geojson?layers=0
* navrhované značky: {{tag|amenity|doctors}} + {{tag|healthcare:speciality}}, {{tag|amenity|dentist}}, {{tag|healthcare|sample_collection}}, {{tag|emergency|ambulance_station}}, {{tag|opening_hours}}, {{tag|ref:idzz|<identifikátor zdravotníckeho zariadenia>}}
* poznámka: 24 199 ambulancií so schválenými ordinačnými hodinami a IdZZ; v Trnavskom kraji má zubnú ambulanciu v OSM do 100 m len 68 z 274 zubných ambulancií, ZZS 474 posádok oproti 34 staniciam v OSM.
```
