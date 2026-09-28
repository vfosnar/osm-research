# Umístění a vlastnosti stanovišť pro plavidla (berths: kotviště, překladiště, přístaviště, vývaziště, přístavní polohy)

| Field | Value |
|---|---|
| publisher | Státní plavební správa (SPS), IČO 00003352; served through EuRIS (European River Information Services portal) |
| url | NKOD https://data.gov.cz/zdroj/datové-sady/00003352/1467543610 → API https://www.eurisportal.eu/doc/api/?urls.primaryName=Berth_v2 ; geometry: https://www.eurisportal.eu/api/arcgis/rest/services/berths/0/query?where=LOCODE+LIKE+%27CZ%25%27&outSR=4326&outFields=*&returnGeometry=true&f=json (the earlier bbox query ignored the envelope and returned all 5,841 European berths; fixed 2026-09-27) ; attributes: https://www.eurisportal.eu/visuris/api/Berths_v2/GetCompactBerths?$filter=startswith(locode,'CZ') (paged, $top ≤ 100) and .../Berths_v2/GetBerth?isrs=&lt;ISRS&gt; |
| format | JSON (ArcGIS REST FeatureServer-like, polyline); REST JSON |
| coords | yes (polylines along the bank, WGS84) |
| records | 317 CZ berths in the Berth API, 280 with geometry in the ArcGIS layer (Elbe 194, Vltava 97, Morava 20, Berounka 6). By function: 202 berths without transhipment (přístavní polohy / vývaziště), 49 ferry/passenger berths (přístaviště), 29 transhipment berths (překladiště) |
| osm_tags | mooring=yes\|ferry\|commercial (on ways along the bank), amenity=ferry_terminal for passenger landings, ref:isrs=&lt;ISRS code&gt; (proposed) |
| osm_count_cz | mooring=* 175 (taginfo 2026-09-26), leisure=marina 166, waterway=milestone 1 |
| license | NKOD terms: no copyrighted work, not a copyright-protected database, no sui generis right. SPS also calls it open data per §3(5) InfZ and lists it as a High-Value Dataset. The EuRIS portal's own terms (eurisportal.eu/disclaimer) are rendered by JS and could not be read |
| license_url | https://data.gov.cz/zdroj/datové-sady/00003352/1467543610 ; https://sps.gov.cz/organizace/opendata |
| license_status | ok (per NKOD); confirm that the EuRIS General Terms do not add restrictions |
| update_freq | as needed (NKOD: AS_NEEDED) |
| impact | 2 |
| sync_fit | iD fork (berth lines, stable ref:isrs; function → mooring subtype) |
| verified | yes |

## Try it
- **Map preview:** [samples/sps-euris-stanoviste-plavidel.geojson](../samples/sps-euris-stanoviste-plavidel.geojson): all 280 CZ berth lines with `ref:isrs`, function code (berths_3 = 202, berths_9 = 49, berths_1 = 29), bank and owner.
- **QGIS:** *Layer → Add Layer → Add Vector Layer*, source type *Protocol: HTTP(S)*, URI `https://www.eurisportal.eu/api/arcgis/rest/services/berths/0/query?where=LOCODE+LIKE+%27CZ%25%27&outSR=4326&outFields=*&returnGeometry=true&f=json`. GDAL reads the response as ESRI JSON; `f=geojson` also returns ESRI JSON here. The services root is not listable, so an ArcGIS REST connection does not work.
- **Web viewer:** https://www.eurisportal.eu/visuris

## Notes
- **Stable ID:** the ISRS location code; CZBAB07008BER1100414 is one of the CZ berths. It encodes country, UN/LOCODE, fairway section, object type and hectometre (river km × 10). Suggested key: `ref:isrs`. There is no such key on the wiki yet, so propose it on talk-cz.
- **Gap (Postpass, 100 m buffer around berth centroids against OSM mooring/pier/quay/ferry_terminal/marina):**
  - 60 of 202 non-transhipment berths have an OSM feature nearby.
  - 32 of 49 passenger berths have one.
  - 4 of 29 transhipment berths have one.
  - That leaves about 180 berths with nothing mapped. Mooring=* currently has only 175 objects in CZ.
- **Detail attributes (GetBerth):** owner, refFunctionMessage, bank (LB/RB), berthLength, draught. Many are null. In the ArcGIS layer, OWN_NAME is Povodí Labe for 54 berths, Povodí Vltavy 22, Ředitelství vodních cest 12, Povodí Moravy 8, and empty for 138.
- **Wiki pages read:** Key:mooring. It applies to ways, not nodes, which suits the EuRIS polylines. Values: yes, ferry, cruise, guest, commercial, declaration.
- **Related SPS HVD datasets:**
  - Locks: /Locks_v2/GetCompactLocks has 56 CZ lock chambers with sub-lock dimensions (length, width, draught, clearance), but the ArcGIS `locks` layer returned 0 CZ features, so there is no geometry. It is useful only to enrich the 44 lock=yes / 175 lock_gate objects already mapped. I did not create a separate candidate for it.
  - IENC charts: the /api/v3/ienc/compact listing had no identifiable CZ cells. IENC would be the source for hectometre marks (waterway=milestone, only 1 in OSM), but I could not locate CZ cells, so this is not verified.
- Contact: Státní plavební správa, ředitelství Praha (sps.gov.cz).

## Wiki entry
```
===Stanoviště pro plavidla (SPS / EuRIS)===
* dataset: Umístění a vlastnosti stanovišť pro plavidla (kotviště, překladiště, přístaviště, vývaziště, přístavní polohy)
* gestor: [https://sps.gov.cz/ Státní plavební správa]
* licence: neobsahuje autorská díla, není chráněnou databází (NKOD, HVD) [https://data.gov.cz/zdroj/datové-sady/00003352/1467543610]
* datové primitivy: linie
* odkaz: https://www.eurisportal.eu/api/arcgis/rest/services/berths/0/query
* navržený tag {{tag|mooring|yes}}, {{tag|mooring|ferry}}, {{tag|amenity|ferry_terminal}}, {{tag|ref:isrs|<ISRS>}}
* poznámka: z 280 stanovišť na Labi, Vltavě a Moravě má v OSM protějšek do 100 m jen ~100; mooring=* je v ČR jen 175×
```
