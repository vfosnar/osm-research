# LESY SR: forest-road barriers, fire pits, hunting stands and hunting lodges (CC0)

| Field | Value |
|---|---|
| publisher | LESY Slovenskej republiky, štátny podnik (IČO 36038351), Banská Bystrica |
| url | ArcGIS REST (query with `/<layer>/query?where=1%3D1&outFields=*&outSR=4326&f=geojson`, max 1,000 per page): `https://app.lesy.sk/enterprise/rest/services/LSR_PublicServices/DS_BOZPaPO_LSR_WM/MapServer` (layer 1 `Objekty požiarnej ochrany`, 2 `Objekty prvej pomoci`, 0 `Sídla organizačných jednotiek`); `https://app.lesy.sk/enterprise/rest/services/LSR_PublicServices/DS_Polovnictvo_LSR_WM/MapServer` (layer 0 `Informačné a orientačné prvky`, 1 `Lov a pobyt`, 2 `Ochrana zveri…`); `https://app.lesy.sk/enterprise/rest/services/LSR_PublicServices/LNCH_body/MapServer/0` (forest educational trails); `https://app.lesy.sk/enterprise/rest/services/LSR_PublicServices/DS_Vyznamne_lesnicke_miesto_WM/MapServer/0`. Catalogue entries: https://data.gov.sk/dataset/prva-pomoc-v-lesnych-porastoch ("BOZP a PO"), https://data.gov.sk/dataset/ppo-lsr-protipoziarne-opatrenia , https://data.gov.sk/dataset/polovnictvo-a-ochrana-zveri , https://data.gov.sk/dataset/vyznamne-lesnicke-miesta-podniku-lesy-sr-s-p |
| format | ArcGIS MapServer (REST JSON / GeoJSON, WMS); no WFS (the WFSServer endpoint returns an error) |
| coords | yes (points, WGS84 via `outSR=4326`) |
| records | fetched 30 Sep 2026. Fire-protection layer: 1,528 road barriers (`Typ` 5 "Rampa na ceste"), 397 secured fire pits (11 "Zabezpečené ohnisko"), 263 fire-fighting water sources (7), 185 tool depots (4). Hunting layer: 1,027 covered and 314 open hunting stands (102/103), 168 hunting lodges (101 "Poľovnícka chata"), 18 permanent traps; 241 game fields, wallows and game watering places; 69 information boards. Also 40 forest educational trails (start points with name and URL) and 87 "Významné lesnícke miesta" (named forestry monuments with description, date and URL) |
| osm_tags | barriers: `barrier=lift_gate` (+ `access`/`motor_vehicle` left to the way); fire pits: `leisure=firepit`; hunting stands: `amenity=hunting_stand` + `shelter=yes` (covered, `Typ` 102) / `shelter=no` (open, 103); hunting lodges: `building=cabin` + `name` (no settled SK tag, see notes); information boards: `tourism=information` + `information=board`; water sources: `emergency=suction_point` (low priority). Checked against Tag:barrier=lift_gate, Tag:leisure=firepit, Tag:amenity=hunting_stand (wiki, raw, 30 Sep 2026) |
| osm_count_sk | `barrier=lift_gate` 5,350, `leisure=firepit` 2,982, `amenity=hunting_stand` 11,464, `tourism=wilderness_hut` 281 (taginfo, data until 29 Sep 2026). Local match against all OSM points in the SK bbox (Postpass, 30 Sep 2026): 453 of 1,528 barriers have an OSM barrier node within 50 m; 70 of 397 fire pits have a `leisure=firepit`/`amenity=bbq`/`amenity=shelter` within 50 m; 157 of 1,341 hunting stands have an `amenity=hunting_stand` within 50 m; 21 of 168 hunting lodges have a hut/shelter node within 50 m; 5 of 263 water sources have any water/emergency node within 50 m |
| license | CC0 1.0 for the author's work, the original database and the sui generis database right (terms of use of every distribution listed above in the national catalogue). The map services themselves show the copyright line "© LESY SR š. p., 2023" |
| license_url | https://data.gov.sk/dataset/prva-pomoc-v-lesnych-porastoch ; https://data.gov.sk/dataset/polovnictvo-a-ochrana-zveri ; https://creativecommons.org/publicdomain/zero/1.0/ |
| license_status | ok |
| update_freq | not stated; catalogue records modified 2024-06-04, the services are live (the LNCH layer carries edit dates) |
| impact | 4 |
| sync_fit | barriers and fire pits: Sync (points, category → one fixed tag 1:1; OBJECTID is the only ID, so treat it as a one-off conflation plus manual matching until LESY SR confirms it is stable); hunting stands: Sync with `shelter=yes/no` from `Typ`; hunting lodges, water sources, educational trails and forestry monuments: MapRoulette (tag choice and access need a human) |
| verified | yes |

## Try it

- **Map preview:** [../samples/lesy-sr-lesne-objekty.geojson](../samples/lesy-sr-lesne-objekty.geojson) has every barrier, fire pit and hunting lodge in central Slovakia (bbox 18.6–20.3 E, 48.3–49.1 N): 578 barriers, 245 fire pits, 96 hunting lodges. `osm_match_50m` is false for 418 barriers, 208 fire pits and 85 lodges.
- **QGIS:** *Layer → Data Source Manager → ArcGIS REST Server → New*, URL `https://app.lesy.sk/enterprise/rest/services/LSR_PublicServices/DS_BOZPaPO_LSR_WM/MapServer`, then add `Objekty požiarnej ochrany`; style or filter by `Typ` (5 = rampa, 11 = ohnisko). Do the same with `…/DS_Polovnictvo_LSR_WM/MapServer` for `Lov a pobyt`. Both were queried successfully.
- The coded values of `Typ` are in each layer's `types` list (`…/MapServer/1?f=json`).

## Notes

- **Why it matters.** Forest-road barriers decide whether a car, a cyclist with a trailer or a rescue vehicle can get through, and they are also good landmarks. About 1,075 of the 1,528 barriers on LESY SR roads are missing in OSM. The positions are good: in a random sample of 150 barriers, the median distance to the nearest OSM `highway` way was 2.4 m, and 117 were within 5 m (Postpass, 30 Sep 2026). So the source points sit on the road and can be snapped to the way.
- **Fire pits.** The 397 "zabezpečené ohniská" are the official fire pits where making a fire in the forest is allowed. Names often say which hut or shelter they belong to ("Chata Kuchárová", "prístrešok Koliesko"); 29 have no name. About 327 are missing in OSM.
- **Hunting stands.** OSM already has 11,464 `amenity=hunting_stand` in Slovakia, but only 157 of the 1,341 LESY SR stands match within 50 m. Stands get moved and rebuilt, so this layer suits a check against imagery more than a blind import. `Typ` distinguishes covered from open, which maps to `shelter`.
- **Hunting lodges.** 168 lodges; OSM uses a mix of tags for them (`building=cabin`, `tourism=wilderness_hut`, `tourism=hunting_lodge`, plain `building=yes`, by a Postpass name search). Most are locked and private, so they must not become `tourism=wilderness_hut`. The layer has no names, so this is a pointer layer.
- **Other layers.** "Objekty prvej pomoci" (4,038 points) is mostly volunteer fire-brigade seats (3,027), hospitals and doctors outside the forest; it is a traumatology-plan list, not a forest data set, so leave it out. The line layers "Cesty pre záchranné automobily" and "Cestná sieť" in the same service could help classify forest tracks, but NLC forest roads are already known (known-sources), so they are not proposed here. The 40 educational trails (`LNCH_body`, with name, length, number of stops and URL) and the 87 forestry monuments (`Významné lesnícke miesto`, with description and URL) are small, named, and good for enriching existing trail relations and memorials.
- **ZBGIS overlap.** The ZBGIS catalogue has `AP040 Brána, závora` (point snapped to the road, "Rieši podľa zistení z terénu alebo od správcu") and the building use "Poľovnícka chata" (344). It has no fire pits or hunting stands. ZBGIS gives no LESY SR ID and it is not an open vector download, so the primary source adds value, above all with a clear licence.
- **Licence caveat.** The catalogue declares CC0 on all three rights for these distributions; the service copyright line "© LESY SR" does not contradict CC0 (CC0 waives the rights), but confirm with LESY SR that CC0 also covers the REST query output, not only the WMS listed as the distribution.
- **Stable ID.** Only `OBJECTID` exists. Ask LESY SR whether it survives edits before relying on it as `ref:lesysr`; until then, match by position.
- Contact: LESY Slovenskej republiky, š. p., generálne riaditeľstvo, Námestie SNP 8, Banská Bystrica (GIS department that runs `app.lesy.sk`), https://www.lesy.sk/

## Wiki entry

```
=== LESY SR – rampy, ohniská, posedy a poľovnícke chaty ===
* dataset: BOZP a PO; PPO_LSR – Protipožiarne opatrenia; Poľovníctvo a ochrana zveri; Lesnícke náučné chodníky; Významné lesnícke miesta
* správca: [https://www.lesy.sk/ LESY Slovenskej republiky, š. p.]
* licencia: CC0 1.0 (autorské dielo, databáza aj právo sui generis) [https://data.gov.sk/dataset/prva-pomoc-v-lesnych-porastoch]
* dátové primitívy: body
* odkaz: https://app.lesy.sk/enterprise/rest/services/LSR_PublicServices/DS_BOZPaPO_LSR_WM/MapServer , https://app.lesy.sk/enterprise/rest/services/LSR_PublicServices/DS_Polovnictvo_LSR_WM/MapServer
* navrhované značky: {{tag|barrier|lift_gate}}, {{tag|leisure|firepit}}, {{tag|amenity|hunting_stand}} + {{tag|shelter|yes/no}}
* poznámka: z 1 528 rámp na lesných cestách chýba v OSM asi 1 075 a z 397 povolených ohnísk asi 327; body ležia v priemere 2,4 m od cesty v OSM.
```
