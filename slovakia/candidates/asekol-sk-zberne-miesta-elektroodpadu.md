# ASEKOL SK – collection points for e-waste (street containers, collection yards, shop take-back)

| Field | Value |
|---|---|
| publisher | ASEKOL SK s.r.o. (producer-responsibility organisation for electrical equipment) |
| url | https://us-central1-asekol-ef453.cloudfunctions.net/getCachedPlacesSK (JSON behind the map at https://asekol.sk/zberne-miesta) |
| format | JSON array |
| coords | yes (`lat`, `long`, WGS84, Google-geocoded precision) |
| records | 3,151 rows = 3,003 unique `internalNumber` (2026-09-30; 148 rows are exact duplicates). Unique by type: PS (shop take-back) 1,918; KSM (municipal collection point) 618; **STK (stationary street containers) 270**; **SD (collection yard, zberný dvor) 115**; SMFI (company or institution) 82 |
| osm_tags | STK: amenity=recycling, recycling_type=container, recycling:small_electrical_appliances=yes, operator=&lt;municipality&gt;; SD: amenity=recycling, recycling_type=centre, recycling:electrical_appliances=yes, recycling:small_electrical_appliances=yes, operator=&lt;proName&gt; |
| osm_count_sk | recycling:small_electrical_appliances 9, recycling:small_appliances 37, recycling:electrical_appliances 113, recycling:electrical_items 22, recycling:batteries 135, recycling_type=centre 390 (taginfo SK, 2026-09-30). The same keys in CZ: 1,079 / 722 / 1,079 / 208 / 1,455 |
| license | none stated |
| license_url | https://asekol.sk/zberne-miesta |
| license_status | unclear |
| update_freq | cached cloud function behind the live map; no date field |
| impact | 3 |
| sync_fit | STK: Sync (points with a stable `internalNumber`, fixed tags); SD: Sync field enrichment of existing recycling centres, else MapRoulette (area drawn from imagery); PS/KSM/SMFI: not for OSM (see notes) |
| verified | yes |

## Try it

- **Map preview:** none, because the licence is unclear, so no extract is redistributed here.
- **QGIS:** convert to CSV (tested 2026-09-30, 3,151 rows):
  ```
  curl -s https://us-central1-asekol-ef453.cloudfunctions.net/getCachedPlacesSK | python3 -c "import json,csv,sys;w=csv.writer(open('asekol_sk.csv','w'));w.writerow(['id','type','name','street','no','postcode','operator','access','lat','lon']);w.writerows([[p['internalNumber'],p['type'],p['name'],p['street'],p['houseNumber'],p['postCode'],p['proName'],p['siteAccess'],p['lat'],p['long']] for p in json.load(sys.stdin)])"
  ```
  Then *Layer → Add Layer → Add Delimited Text Layer…*: `asekol_sk.csv`, CSV, UTF-8, X = `lon`, Y = `lat`, EPSG:4326. Filter `"type" IN ('STK','SD')`.
- **Web viewer:** https://asekol.sk/zberne-miesta

## Notes

- **Gap (Postpass, 2026-09-30):**
  - **STK containers:** 31 of 270 have an OSM `amenity=recycling` with an electrical-waste key within 75 m (11 %), and 73 have any recycling object within 75 m. So **about 240 e-waste containers are missing**, and at the rest the OSM object lacks the electro key.
  - **SD collection yards:** 8 of 115 have an OSM `recycling_type=centre` within 150 m (7 %), and 14 have one within 500 m. So **about 100 municipal collection yards are missing** or not tagged as centres. The yards at Brezno (31 m) and Michalovce (22 m) are examples that do match.
  - Slovakia is far behind Czechia on e-waste keys: 9 vs 1,079 objects with `recycling:small_electrical_appliances`.
- **Fields:** `internalNumber` (stable id; its prefix is the IČO of the municipality or company, then a sequence: `00312983/3`), `type`, `name` ("Smolenice - STK_1", "Zberný dvor - Brezno"), `street`, `houseNumber`, `postCode`, `municipality` (`SK.<code of the municipality>`), `siteAccess` (`public` 306 / `closed_estate` 2,845), `openMonday`…`openSunday` (filled on 982 rows), `proName` (the operating municipality, technical services or company), `tel`. `wasteTypes`, `takebackType` and `binTypes` are empty.
- **What not to import:**
  - PS rows are shops obliged to take back an old appliance when selling a new one. That is a retail duty, not a map feature.
  - Some PS names are natural persons (sole traders), so do not copy names.
  - KSM (municipal collection point, often the municipal office yard, used on collection days) and SMFI (company premises) are mostly not public.
- **siteAccess caveat:** the STK containers are mostly marked `closed_estate` although they are street containers. Treat the field as unreliable, and check a few on imagery before trusting it.
- **Tagging:**
  - Tag:amenity=recycling (wiki, raw, read 2026-09-30) lists `recycling:small_appliances` as a possible synonym, with the advice "Consider to use recycling:small_electrical_appliances instead". Use `recycling:small_electrical_appliances`.
  - Tag:recycling_type=centre is the tag for collection yards.
  - Whether the containers also take batteries and bulbs is not stated in the feed. Add `recycling:batteries` only after checking the container label.
- **ZBGIS:** the catalogue has no waste-collection object types. The closest is AM032 "Skládka materiálu" (material or waste heaps). Collection yards are not a ZBGIS type.
- **Related open source:** MŽP SR's CC0 "Register zberných dvorov" (ISOH, catalogue dataset `https://data.gov.sk/dataset/register-zbernych-dvorov`, download `https://data.isoh.gov.sk/set/collection-yard`) would be the licence-clean national list of collection yards. On 2026-09-30 every `data.isoh.gov.sk` path returned HTTP 500 ("opendata-app: Name or service not known"), and the catalogue's own availability check from 2026-09-29 also recorded 500. Its content could not be verified, so it is only an open lead.
- **Other e-waste PROs checked:** no machine-readable collection-point feed was found on the home pages of SEWA, ENVIDOM and EKOLAMP SK or on the ELEKOS page https://elekos.sk/zberne-miesta/ (read 2026-09-30).
- **Contact:** ASEKOL SK s.r.o., https://asekol.sk/

## Wiki entry

```
=== Zberné miesta elektroodpadu ASEKOL SK ===
* dataset: zberné miesta elektroodpadu (stacionárne kontajnery, zberné dvory)
* správca: [https://asekol.sk/ ASEKOL SK s.r.o.]
* licencia: neuvedená – potrebný súhlas [https://asekol.sk/zberne-miesta]
* dátové primitívy: body
* odkaz: https://us-central1-asekol-ef453.cloudfunctions.net/getCachedPlacesSK
* navrhované značky: {{tag|amenity|recycling}}, {{tag|recycling_type|container}}, {{tag|recycling:small_electrical_appliances|yes}}
* poznámka: 270 stacionárnych kontajnerov na drobný elektroodpad a 115 zberných dvorov; v OSM má elektro kľúč 11 % kontajnerov a zberný dvor 7 % dvorov (9/2026).
```
