# e-VÚC: lekárne a výdajne zdravotníckych pomôcok (register of pharmacies of the 8 self-governing regions)

| Field | Value |
|---|---|
| publisher | The 8 samosprávne kraje (VÚC), which license public pharmacies. Portal e-VÚC run for them by CRYSTAL CONSULTING, s.r.o. Open extract: Trnavský samosprávny kraj (TTSK) |
| url | National (HTML only): https://www.e-vuc.sk/ → region → *Lekárne a výdajne ZP* (district list, then one page per pharmacy, e.g. https://www.e-vuc.sk/bsk/zdravotnictvo/lekarne-a-vydajne-zp/malacky/lekaren-pri-stanici.html?page_id=153530). TTSK open extract: https://rss-dcat-opendata-ttsk.hub.arcgis.com/api/download/v1/items/7b5f88d39eb94da292f6e957d8245845/geojson?layers=0 (catalogue: "EVUC Lekárne TTSK (aktualizované)") |
| format | e-VÚC: HTML detail pages with a `maps.google.com/?q=lat,lon` link. TTSK: GeoJSON (EPSG:3857) / CSV from ArcGIS Hub |
| coords | yes (e-VÚC detail page; TTSK fields `F_poloha_šírka_`/`F_poloha_dĺžka_`) |
| records | e-VÚC home page (30 Sep 2026): 2,333 pharmacies and outlets (BBSK 271, BSK 370, KSK 337, NSK 277, PSK 327, TSK 224, TTSK 247, ŽSK 280). TTSK extract: 243 (199 verejná lekáreň, 26 pobočka verejnej lekárne, 3 nemocničná lekáreň s výdajom verejnosti, 11 výdajňa zdravotníckych pomôcok, 4 výdajňa ortopedicko-protetických ZP) |
| osm_tags | amenity=pharmacy + healthcare=pharmacy + dispensing=yes (verejná lekáreň, pobočka); shop=medical_supply (výdajňa ZP); name, operator, opening_hours, website; proposed ref:idzz=&lt;Identifikátor zdravotníckeho zariadenia&gt; |
| osm_count_sk | amenity=pharmacy 1,694; shop=medical_supply not checked; no key for IdZZ exists (taginfo europe:slovakia, 2026-09-30) |
| license | e-VÚC portal: none stated. TTSK extract: CC BY 4.0 (catalogue metadata). Prešovský kraj publishes a comparable health-provider set as PDM (see notes); Nitriansky kraj "Lekárenské zariadenia v Nitrianskom kraji" is CC BY-NC 4.0 |
| license_url | https://creativecommons.org/licenses/by/4.0/ (TTSK); e-VÚC: https://www.e-vuc.sk/e-vuc/pre-poskytovatelov-zdravotnej-starostlivosti/zoznam-zverejnovanych-udajov.html?page_id=66315 (list of published fields, no licence) |
| license_status | needs_waiver (TTSK extract); unclear (national e-VÚC data) |
| update_freq | e-VÚC: live (providers edit hours in the LEKÁREŇ app; the region approves them). TTSK extract: irregular, last catalogue refresh 2024 |
| impact | 4 |
| sync_fit | Sync — points with a stable legal ID (IdZZ), type maps 1:1 (lekáreň → amenity=pharmacy, výdajňa → shop=medical_supply); opening_hours as an update key |
| verified | partial (national data read page by page, not downloaded in bulk; TTSK extract downloaded and matched) |

## Try it
- **Map preview:** [../samples/health-evuc-pharmacies.geojson](../samples/health-evuc-pharmacies.geojson): all 243 TTSK pharmacies and outlets with `opening_hours` converted from the per-day fields (215 converted cleanly) and a flag `osm_pharmacy_within_100m` (154 true, 89 false; Postpass, 2026-09-30).
- **QGIS:** *Layer → Add Layer → Add Vector Layer → Protocol: HTTP(S)*, URI `https://rss-dcat-opendata-ttsk.hub.arcgis.com/api/download/v1/items/7b5f88d39eb94da292f6e957d8245845/geojson?layers=0`. The GeoJSON declares EPSG:3857, which GDAL picks up. (The CSV variant of the same item answered "download file is being generated" on 30 Sep 2026.)
- **Web:** https://www.otvorenalekaren.sk/ (the regions' "nearest open pharmacy" app built on the same data), and the e-VÚC pages above.

## Notes
- **Why this source:** in Slovakia the region (VÚC), not ŠÚKL, issues the permit for a public pharmacy, so e-VÚC is the authoritative, live list. ŠÚKL's open data (https://www.sukl.sk/o-nas/databazy-a-servis/datove-archivy-a-zoznamy) covers medicines only; its "Iné zoznamy" only lists internet pharmacies. AllThePlaces has no Slovak pharmacy spider (no SK split for any brand described as a pharmacy in the 2026-09-26 insights file), so Dr.Max, BENU and independents are not covered by the ATP route.
- **Stable ID:** every detail page shows the *Identifikátor zdravotníckeho zariadenia* (IdZZ), for example `61-36644838-A0001` = issuing authority code (61 = BSK, 62 TTSK … 68 KSK, 51/52 MZ SR) + IČO of the holder + serial number. By law (578/2004 as amended by 77/2015) it stays with the facility for its whole life and is used "vo všetkých informačných systémoch verejnej správy" (https://www.e-vuc.sk/e-vuc/pre-poskytovatelov-zdravotnej-starostlivosti/identifikator-zdravotnickeho-zariadenia.html?page_id=74559). The TTSK extract does not carry the IdZZ, only the e-VÚC internal `F_ID_lekárne_`, so a national export with IdZZ is what to ask for.
- **Tags:** wiki pages read: Tag:amenity=pharmacy (`dispensing=yes/no` for prescription filling), Tag:shop=medical_supply.
- **Attributes:** approved opening hours per weekday with validity date, operator and IČO, type, address with súpisné/orientačné číslo, phone/e-mail, pharmacy duty schedule (lekárenská pohotovosť) on separate pages.
- **Gap:** TTSK, public pharmacies only (228): 139 have an OSM `amenity=pharmacy`/`healthcare=pharmacy` within 100 m, 89 (39 %) do not (Postpass, 2026-09-30). Nationally 2,333 e-VÚC entries against 1,694 OSM pharmacies. Opening hours in OSM could be checked against the approved hours the same way.
- **ZBGIS:** only the building-use attribute BFC of layer *budova* ("Zdravotné zariadenie" 357, "Zdravotné stredisko" 33) in the KTO catalogue; no pharmacy object, no names or IDs. ZBGIS does not cover this.
- **Licence:** the e-VÚC portal publishes no terms. The data is a public register kept by the regions under 578/2004 and 362/2011, so the "úradný dokument" exception (§5 185/2015) may apply to individual records, but the regions' database right is not addressed; flag it. TTSK already publishes its extract as CC BY 4.0, so a waiver/consent from the regions (ideally jointly via the SK8 association, one request for the shared e-VÚC data) is the realistic route.
- **Other regional extracts found:** Prešovský kraj "Poskytovatelia zdravotnej starostlivosti" and "Zariadenia lekárskej služby PP" (`https://opendata.psk.sk/oe/v1/api/oe14/poskytovatel-zdrav-starost?page=0&size=20000&sort=id%2Casc`, licence PDM in the catalogue) could not be read: the host's TLS certificate had expired on 30 Sep 2026. Nitriansky kraj's XLSX (`https://www.unsk.sk/Files/ShowFile/93972`) is CC BY-NC 4.0 → incompatible.
- **Contacts:** info@e-vuc.sk (portal), per-region data errors <kraj>@e-vuc.sk (listed at https://www.e-vuc.sk/e-vuc/kontakty.html?page_id=2295); health departments of the 8 VÚC.

## Wiki entry
```
=== e-VÚC – lekárne a výdajne zdravotníckych pomôcok ===
* dataset: Lekárne a výdajne ZP (e-VÚC, register samosprávnych krajov); otvorený výťah TTSK „EVUC Lekárne TTSK (aktualizované)“
* správca: [https://www.e-vuc.sk/ samosprávne kraje SR (portál e-VÚC)], [https://www.trnava-vuc.sk/ Trnavský samosprávny kraj]
* licencia: e-VÚC bez uvedenej licencie; výťah TTSK CC BY 4.0 [https://creativecommons.org/licenses/by/4.0/]
* dátové primitívy: body
* odkaz: https://rss-dcat-opendata-ttsk.hub.arcgis.com/api/download/v1/items/7b5f88d39eb94da292f6e957d8245845/geojson?layers=0
* navrhované značky: {{tag|amenity|pharmacy}}, {{tag|healthcare|pharmacy}}, {{tag|dispensing|yes}}, {{tag|shop|medical_supply}}, {{tag|opening_hours}}, {{tag|ref:idzz|<identifikátor zdravotníckeho zariadenia>}}
* poznámka: 2 333 lekární a výdajní so schválenými otváracími hodinami a trvalým identifikátorom IdZZ; v OSM 1 694 lekární, v Trnavskom kraji 89 z 228 verejných lekární bez lekárne v OSM do 100 m.
```
