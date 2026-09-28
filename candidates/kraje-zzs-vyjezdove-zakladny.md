# Výjezdové základny zdravotnické záchranné služby (ambulance stations), published by 4 regions

| Field | Value |
|---|---|
| publisher | Královéhradecký kraj (70889546), Moravskoslezský kraj (70890692), Karlovarský kraj (70891168), Liberecký kraj (70891508) |
| url | KHK https://www.datakhk.cz/api/download/v1/items/1c28da5d644445d3a5f4b578ce22ed40/geojson?layers=0 ; MSK https://datamsk-mskraj.hub.arcgis.com/api/download/v1/items/e21ccc36dd404b10b5a9070a2a9a1068/geojson?layers=0 ; KV https://www.datazapad.cz/api/download/v1/items/4d7d80fc1d5f4f6bbb61a10b26d2a2aa/geojson?layers=0 ; LK https://www.datalk.cz/api/download/v1/items/6da21aeaf4844012929017561edb59be/csv?layers=0 |
| format | GeoJSON/CSV/SHP/KML (ArcGIS Hub) |
| coords | yes (x/y or X/Y or n/e WGS84 attributes; GeoJSON geometry in EPSG:3857 for KHK, MSK and LK, WGS84 for KV) |
| records | KHK 16, MSK 33, KV 13, LK 14 (the LK download worked on 2026-09-27). 76 in total. |
| osm_tags | emergency=ambulance_station + name + operator=Zdravotnická záchranná služba &lt;kraje&gt; |
| osm_count_cz | emergency=ambulance_station 138 (Geofabrik taginfo 2026-09-27) |
| license | KHK, KV, LK: NKOD terms, no copyright, no sui generis right (CC0; LK distribution terms checked 2026-09-27). MSK: CC BY 4.0. |
| license_url | https://data.gov.cz/podmínky-užití/neobsahuje-autorská-díla/ ; https://creativecommons.org/licenses/by/4.0/ (MSK) |
| license_status | ok (KHK, KV, LK); needs_waiver (MSK) |
| update_freq | irregular |
| impact | 2 |
| sync_fit | MapRoulette (no stable id field, small dataset needs manual matching) |
| verified | partial |

## Try it

- **Map preview:** [samples/kraje-zzs-vyjezdove-zakladny.geojson](../samples/kraje-zzs-vyjezdove-zakladny.geojson) has all 76 bases from the four regions. Each feature carries its region's `licence`; MSK is CC BY 4.0, © Moravskoslezský kraj. 57 have no OSM `emergency=ambulance_station` within 150 m (Postpass, 2026-09-27). Coordinates come from the WGS84 attribute columns.
- **QGIS:** *Layer → Add Layer → Add Vector Layer…* → *Protocol: HTTP(S)*, and paste any GeoJSON URL from the table. The KHK and MSK files declare EPSG:3857 and KV declares WGS84. QGIS reads either. For LK, use the same Hub item with `geojson?layers=0` in place of `csv?layers=0`.

## Notes
- Postpass check: 16 of 62 stations (26%) have emergency=ambulance_station within 150 m. About 46 are missing in these 3 regions alone. With LK added (2026-09-27), 19 of 76 match and 57 are missing. Nationally there are roughly 300 bases (not verified), but only 4 regions publish open data.
- MSK includes crew counts (RLP/RZP/RV). KHK includes RÚIAN-style address and web link.
- Fire stations (HZS) are covered. Ambulance stations are not, and ÚZIS NRPZS (covered) lists ZZS as a provider, not its individual bases.
- Better national route: ask the ZZS of each region or MZd for a national list. The regional files show that the data is public.
- Wiki page read: Tag:emergency=ambulance_station (de facto; node or area).

## Wiki entry
```
===Výjezdové základny ZZS (kraje)===
* dataset: Výjezdové základny zdravotnické záchranné služby (KHK, MSK, KV, LK)
* gestor: [https://www.datakhk.cz/ Královéhradecký kraj], [https://datamsk-mskraj.hub.arcgis.com/ Moravskoslezský kraj], [https://www.datazapad.cz/ Karlovarský kraj], [https://www.datalk.cz/ Liberecký kraj]
* licence: CC0 (KHK, KV, LK), CC BY 4.0 (MSK) [https://data.gov.cz/zdroj/datové-sady/70889546/696503a9fc4c020b22ebbf9be866f6d0]
* datové primitivy: body
* odkaz: https://www.datakhk.cz/api/download/v1/items/1c28da5d644445d3a5f4b578ce22ed40/geojson?layers=0
* navržený tag {{tag|emergency|ambulance_station}}
* poznámka: ze 76 základen ve 4 krajích je v OSM jen 19 (25 %)
```
