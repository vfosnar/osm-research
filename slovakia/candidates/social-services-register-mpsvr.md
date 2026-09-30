# Centrálny register poskytovateľov sociálnych služieb (MPSVR SR) and the ISP map of social services

| Field | Value |
|---|---|
| publisher | Ministerstvo práce, sociálnych vecí a rodiny SR (register entries are made by the 8 VÚC as registrars); map by its Inštitút sociálnej politiky (ISP) |
| url | Register (XML): https://data.slovensko.sk/download?id=a49d8bd0-279a-4f69-aba0-f1798429b727 (file `RSS20250116052147.xml`, 10.5 MB; catalogue landing page https://data.gov.sk/dataset/centralny-register-poskytovatelov-socialnych-sluzieb). ISP map "Poskytovatelia sociálnych služieb v SR k 31.05.2026" as KML: https://www.google.com/maps/d/kml?mid=1yr_EusLdf6t3zw48E3PjDI-TDT4BS0Y&forcekml=1 (16 MB), linked from https://www.employment.gov.sk/sk/ministerstvo/vyskum-oblasti-prace-socialnych-veci-institut-socialnej-politiky/mapa-socialnych-sluzieb-3.html |
| format | XML (namespace `http://data.gov.sk/set/data/mpsvr.sd.rpss.csru/v1`: provider → providedService); KML with ExtendedData (30 fields) |
| coords | register: address-only (street, súpisné/orientačné číslo, PSČ, obec); ISP map: yes (`Zemepisná šírka`/`Zemepisná dĺžka`, origin of the geocoding not stated) |
| records | Register (state 2025-01-16): 8,839 services, 5,554 not erased; 5,350 carry a place-of-provision address. Forms: ambulatory 1,970, field (terénna) 1,768, residential year-round 1,598, weekly 71, other 147. ISP map (May 2026): 3,405 places — odkázanostné služby 1,954, krízová intervencia 518 (257 komunitné centrá, 109 útulky, 55 nocľahárne, 42 nízkoprahové služby pre deti a rodinu, 22 nízkoprahové denné centrá, 21 domovy na polceste, 11 integračné centrá, 1 zariadenie núdzového bývania), podporné služby 439, podpora rodiny s deťmi 275 (incl. jasle), poradenstvo 219 |
| osm_tags | amenity=social_facility + social_facility=nursing_home / group_home / assisted_living / day_care / shelter / outreach / soup_kitchen + social_facility:for=senior / disabled / homeless / child / drug_addicted; amenity=community_centre (komunitné centrum); amenity=childcare (jasle, zariadenie starostlivosti o deti do 3 rokov); capacity; operator; proposed ref:sk:rpss=&lt;service identifier&gt; |
| osm_count_sk | amenity=social_facility 514; social_facility=* 450; amenity=childcare 37 (taginfo europe:slovakia, 2026-09-30) |
| license | Register: CC BY-SA 4.0 (catalogue terms of use of the distribution). ISP map: no licence stated |
| license_url | https://creativecommons.org/licenses/by-sa/4.0/ ; https://data.gov.sk/dataset/centralny-register-poskytovatelov-socialnych-sluzieb |
| license_status | needs_waiver (CC BY-SA 4.0 is not ODbL-compatible without consent; the map's coordinates are unclear) |
| update_freq | catalogue XML last refreshed 2025-01-16 (stale); ISP map every few months (previous layer: September 2024, current May 2026); live register in IS SoS |
| impact | 4 |
| sync_fit | MapRoulette — tag choice is 1:N per service type (a "zariadenie pre seniorov" can be nursing_home or group_home) and several services often share one building; Sync is possible later for residential facilities once a type→tag table is agreed, keyed on the register's service identifier |
| verified | yes (both files downloaded and parsed) |

## Try it
- **Map preview:** none for this dataset (licence of the coordinate layer unclear). For a CC BY 4.0 slice see [social-bratislava-homeless-services.md](social-bratislava-homeless-services.md).
- **QGIS:** *Layer → Add Layer → Add Vector Layer → Protocol: HTTP(S)*, URI `https://www.google.com/maps/d/kml?mid=1yr_EusLdf6t3zw48E3PjDI-TDT4BS0Y&forcekml=1` (KML, EPSG:4326; one layer per service group; attributes in ExtendedData). The register XML has no geometry; open it in a script.
- **Web:** the embedded Google My Map on the ISP page above; public register search in IS SoS (linked from the same page).

## Notes
- **Gap:** random sample of 700 of the 3,405 ISP map points matched with Postpass (2026-09-30) against any `amenity=social_facility|social_centre|nursing_home|shelter`, `social_facility=*` or `healthcare=nursing_home` within 100 m: only 187 (27 %) have one. By group: odkázanostné 125 of 384 (33 %), krízová intervencia 17 of 110 (15 %), podpora rodiny 5 of 53, poradenstvo 10 of 49, podporné 23 of 85. Roughly 2,500 service places are missing, including most shelters (útulky, nocľahárne) and daycare for small children.
- **Stable ID:** each `providedService` has an `identifier` (7 digits, `6222809`) and a `dateOfRegistration`/`dateOfErasure`; providers have IČO. The ISP map has no service ID, only IČO + address, which let 1,391 of 3,405 map points be joined back to a single register record by IČO + obec + ulica + súpisné číslo. A current register export with IDs and place addresses is the thing to ask MPSVR for.
- **Type codes:** the register uses codes (`A0023`, `C0015` …) whose codebook is not in the catalogue. From the join above: A0023 = komunitné centrum (177 joined), A0024 = nocľaháreň, A0025 = útulok, A0026 = domov na polceste, A0021 = nízkoprahové denné centrum, A0022 = integračné centrum, A0030 = nízkoprahová sociálna služba pre deti a rodinu; C00xx are odkázanostné services, E00xx podporné, B00xx family support. Get the official codebook from MPSVR before mapping.
- **Attributes:** capacity (`currentCapacity`, KML `Kapacita`), occupancy, target group, form (ambulatory/residential), provider type (obec, n.o., cirkev, …), website (1,918 map points). Responsible persons, statutory bodies and their phones/e-mails are personal data — don't import.
- **Coordinates caveat:** the ISP map points have 7-decimal coordinates whose source is not stated (possibly a commercial geocoder). Prefer placing records on OSM addresses (MinvSKAddress, `addr:conscriptionnumber`) and use the map only as a pointer.
- **Field services:** 1,768 services are terénne (home care, streetwork) with no place; skip them.
- **Regional duplicates:** TTSK "Zariadenia sociálnych služieb TTSK" (3,183 rows, CC BY 4.0, https://rss-dcat-opendata-ttsk.hub.arcgis.com/api/download/v1/items/c8dc09d8d8704a9780c3472e71c65178/geojson?layers=0), Košice "Zoznam poskytovateľov sociálnych služieb v meste Košice" (CC BY 4.0), Nitriansky kraj "Sociálne zariadenia" (CC BY-NC 4.0 → incompatible) and Prešovský kraj "Poskytovatelia sociálnych služieb" (PDM; host unreachable, expired TLS certificate on 30 Sep 2026) are regional cuts of the same register. e-VÚC also lists social services for BBSK (758), NSK (664), PSK (1,034), TSK (560), ŽSK (724).
- **ZBGIS:** building-use code BFC "Sociálne zariadenie" 356 in layer *budova* only; no service types, names or IDs.
- **Contacts:** ISP, isp@employment.gov.sk (named on the map page); MPSVR open data; the social-affairs departments of the VÚC as registrars.

## Wiki entry
```
=== Register poskytovateľov sociálnych služieb (MPSVR SR) ===
* dataset: Centrálny register poskytovateľov sociálnych služieb; Mapa sociálnych služieb ISP (05/2026)
* správca: [https://www.employment.gov.sk/ Ministerstvo práce, sociálnych vecí a rodiny SR]
* licencia: register CC BY-SA 4.0 [https://creativecommons.org/licenses/by-sa/4.0/]; mapa ISP bez uvedenej licencie
* dátové primitívy: body
* odkaz: https://data.slovensko.sk/download?id=a49d8bd0-279a-4f69-aba0-f1798429b727
* navrhované značky: {{tag|amenity|social_facility}} + {{tag|social_facility}} + {{tag|social_facility:for}}, {{tag|amenity|community_centre}}, {{tag|amenity|childcare}}, {{tag|capacity}}, {{tag|ref:sk:rpss|<identifikátor služby>}}
* poznámka: 3 405 miest poskytovania ambulantných a pobytových sociálnych služieb; v OSM má sociálne zariadenie do 100 m len 27 % z nich (útulky a nocľahárne 15 %).
```
