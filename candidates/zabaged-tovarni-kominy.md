# ZABAGED 1.10 Tovární komín – industrial chimneys with height

| Field | Value |
|---|---|
| publisher | Český úřad zeměměřický a katastrální (ČÚZK), Zeměměřický úřad |
| url | https://ags.cuzk.gov.cz/arcgis/rest/services/ZABAGED_POLOHOPIS/MapServer/31 (layer "Tovární komín"); WFS type `ZABAGED_POLOHOPIS:Tovární_komín` at https://ags.cuzk.gov.cz/arcgis/services/ZABAGED_POLOHOPIS/MapServer/WFSServer |
| format | ArcGIS REST (JSON/GeoJSON, outSR=4326), WFS |
| coords | yes (points, stated accuracy 2 m) |
| records | 6,117 points; `vyska_obj` (height, m) on 1,997, source `zdrojvys_p` = VGHMÚř (military geographic office) for all 1,997; 3 named. Stable ID `fid_zbg`. |
| osm_tags | man_made=chimney + height=&lt;vyska_obj&gt; (when present) + ref:zabaged=&lt;fid_zbg&gt; |
| osm_count_cz | taginfo CZ (data until 2026-09-27): man_made=chimney 2,733 (2,076 nodes, 655 ways) |
| license | CC BY 4.0 + explicit ČÚZK consent for OSM |
| license_url | https://creativecommons.org/licenses/by/4.0/ ; consent recorded on https://wiki.openstreetmap.org/wiki/Cs:%C4%8Cesko/freemap |
| license_status | ok |
| update_freq | ZABAGED is updated continuously |
| impact | 2 |
| sync_fit | Sync: points, 1:1 (the iD fork file already maps `tovarnikomin` to man_made=chimney), stable `fid_zbg`; height as an update key for existing OSM chimneys. |
| verified | yes |

## Try it
- **Map preview:** [samples/zabaged-tovarni-kominy.geojson](../samples/zabaged-tovarni-kominy.geojson): all 194 chimneys in the bbox 18.10,49.70,18.60,49.95 (Ostrava – Karviná), with height, `osm_dist_m` and `in_osm` (OSM man_made=chimney within 50 m). 132 of 194 have none.
- **QGIS:** *Layer → Add Layer → Add ArcGIS REST Server Layer → New*, URL `https://ags.cuzk.gov.cz/arcgis/rest/services/ZABAGED_POLOHOPIS/MapServer`, add *Tovární komín* (id 31). Or *Add WFS Layer*, URL `https://ags.cuzk.gov.cz/arcgis/services/ZABAGED_POLOHOPIS/MapServer/WFSServer`, layer `Tovární_komín`. Native CRS EPSG:5514.
- One-off GeoJSON: `https://ags.cuzk.gov.cz/arcgis/rest/services/ZABAGED_POLOHOPIS/MapServer/31/query?where=1%3D1&outFields=*&outSR=4326&f=geojson` (2,000 per page, use `resultOffset`).

## Notes
- **Definition** (catalogue 1.10, `1_Sidla/ft_af010.html`): "Výšková stavba (samostatná, příp. nástavba na budově) zpravidla kruhového průřezu. Slouží k odvádění a rozptylování spalin, plynů a výparů do ovzduší." Tag:man_made=chimney asks for industrial chimneys only ("approximate height at least 10 metres"), which matches.
- **Gap (local match against the 2026-09-27 Czechia extract):** 3,650 of 6,117 (60 %) have no OSM man_made=chimney within 50 m. In the Žďár sample (bbox A of the audit) 8 of 25 were missing, so the gap is largest in industrial regions.
- **Heights:** 1,997 heights from VGHMÚř can also fill `height` on chimneys already in OSM (Key:height, metres).
- Chimneys are landmarks on topographic and aviation-obstacle maps; ZABAGED is the only national source found.
- Wiki pages read: Tag:man_made=chimney, Key:height.

## Wiki entry
```
===ZABAGED – tovární komíny===
* dataset: ZABAGED® 1.10 Tovární komín
* gestor: [https://www.cuzk.gov.cz/ ČÚZK]
* licence: CC BY 4.0 + souhlas ČÚZK [https://creativecommons.org/licenses/by/4.0/]
* datové primitivy: body
* odkaz: https://ags.cuzk.gov.cz/arcgis/rest/services/ZABAGED_POLOHOPIS/MapServer/31
* navržený tag {{tag|man_made|chimney}}, {{tag|height|<vyska_obj>}}, {{tag|ref:zabaged|<FID_ZBG>}}
* poznámka: 6 117 komínů (1 997 s výškou), 3 650 (60 %) z nich v OSM chybí
```
