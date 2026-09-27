# Úseky parkování v zónách placeného stání (ZPS Praha)

| Field | Value |
|---|---|
| publisher | IPR Praha (data provider id 38 = TSK hl. m. Prahy) |
| url | https://mp.iprpraha.cz/arcgis/rest/services/Hosted/DOP_CUR_DOP_ZPS_USEKY_P/FeatureServer/0 ; catalogue https://opendata.geoportalpraha.cz/datasets/iprpraha::úseky-parkování-v-zónách-placeného-stání-1 |
| format | ArcGIS FeatureServer (JSON/GeoJSON), Hub downloads |
| coords | yes (polygons of the parking strips) |
| records | 16,876 sections (typzony 1 rezidentní 10,502; 2 smíšený 6,133; 3 návštěvnický 151; 7 jiná regulace 90), 2026-09-27 |
| osm_tags | amenity=parking + parking=street_side + parking:zone=blue\|purple\|orange (existing Prague convention) + capacity=&lt;ps_zps&gt; + fee=yes; alternatively parking:&lt;side&gt;:zone on the street way per the Street parking scheme |
| osm_count_cz | parking:zone=* 647 CZ (taginfo 2026-09-27); in the Prague bbox parking:zone=blue 421, purple 216, orange 9 (Postpass, 2026-09-27); parking:both\|left\|right:zone on Prague streets ≈104 ways |
| license | CC BY 4.0 + IPR consent for all open data in OSM (2018) |
| license_url | https://geoportalpraha.cz/data-a-sluzby/otevrena-data ; https://lists.openstreetmap.org/pipermail/talk-cz/2018-February/018526.html |
| license_status | ok |
| update_freq | weekly or more often (dct:modified 2026-09-21) |
| impact | 3 |
| verified | yes |

## Notes

**Fields.**
- `zps_id`: section id, e.g. "2028", and a good `ref` candidate.
- `typzony`: 1 rezidentní → blue, 2 smíšený → purple, 3 návštěvnický → orange,
  7 jiná regulace. This matches the colours Prague mappers already use in `parking:zone`.
- `tariftab`: tariff code, e.g. "P6-0138".
- `ps_zps`: number of spaces.
- `globalid`.

**OSM gap.** Only about 650 parking areas in Prague carry a zone tag, against 16,876 ZPS
sections. Street-side parking areas (`parking=street_side`) are only partly mapped, and
`parking:both|left|right` appear about 3,400 times on street ways in the Prague bbox (Postpass). Adding zone and capacity is
useful for routing and parking apps.

**Caveats.**
- The polygons are the painted parking strips. Conflating them onto street-side ways or
  `parking=street_side` areas needs spatial logic (side of road). That is more work than a
  point import.
- Zones change often (districts join, tariffs change). A Sync-style ongoing update keyed on
  `zps_id` is better than a one-shot import. The ZPS zones themselves (layers
  `DOP_ZPS_ZONYPARK_P`, `DOP_ZPS_ZM_P`) and the tariff polygons are also available.
- Parking meters from the same system are already in Sync (`prague_parkomaty`), so this is
  a natural extension.
- Wiki read: Street parking ("Residential parking permits, parking zones":
  parking:<side>:zone), Key:parking:zone (requires amenity=parking).

## Wiki entry
```
===Zóny placeného stání Praha – úseky===
* dataset: Úseky parkování v zónách placeného stání
* gestor: [https://geoportalpraha.cz IPR Praha] / TSK hl. m. Prahy
* licence: CC BY 4.0 + souhlas IPR s využitím všech opendat pro OSM (2018) [https://lists.openstreetmap.org/pipermail/talk-cz/2018-February/018526.html]
* datové primitivy: plochy
* odkaz: https://mp.iprpraha.cz/arcgis/rest/services/Hosted/DOP_CUR_DOP_ZPS_USEKY_P/FeatureServer/0
* navržený tag {{tag|amenity|parking}} + {{tag|parking|street_side}}, {{tag|parking:zone|blue/purple/orange}}, {{tag|capacity|<ps_zps>}}, {{tag|ref|<zps_id>}}
* poznámka: 16 876 úseků ZPS s typem a počtem stání, v OSM má zónu jen ~650 parkovacích ploch.
```
