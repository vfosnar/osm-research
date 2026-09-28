# ZABAGED 4.01 Zdroj podzemních vod – springs, wells, spring basins

| Field | Value |
|---|---|
| publisher | Český úřad zeměměřický a katastrální (ČÚZK), Zeměměřický úřad |
| url | https://ags.cuzk.gov.cz/arcgis/rest/services/ZABAGED_POLOHOPIS/MapServer/19 (ArcGIS REST, layer "Zdroj podzemních vod"); WFS type `ZABAGED_POLOHOPIS:Zdroj_podzemních_vod` at https://ags.cuzk.gov.cz/arcgis/services/ZABAGED_POLOHOPIS/MapServer/WFSServer; bulk: https://openzu.cuzk.gov.cz/opendata/ZABAGED-GPKG/epsg-5514/ZABAGED-5514-gpkg-20260818.zip (whole ZABAGED, 5.8 GB, from the Atom feed https://atom.cuzk.gov.cz/ZABAGED-GPKG/ZABAGED-GPKG.xml) |
| format | ArcGIS REST (JSON/GeoJSON, outSR=4326 works, 2,000 records per page), WFS, GeoPackage |
| coords | yes (points, stated accuracy 2 m) |
| records | 35,224 points: pramen (PS) 11,060; studna, vrt (VR) 21,652; kašna (KA) 2,403; lázeňské zřídlo (LZ) 109. 5,850 have a name (5,370 of the springs). Stable ID `fid_zbg`. |
| osm_tags | PS and LZ → natural=spring (+ name); VR → man_made=water_well; KA → amenity=fountain or natural=spring + refitted=yes after review; ref:zabaged=&lt;fid_zbg&gt; |
| osm_count_cz | taginfo CZ 2026-09-27: natural=spring 4,844; man_made=water_well 2,521; man_made=spring_box 30. Postpass 2026-09-27: only 10 springs and 4 wells in the CZ bbox carry ref:zabaged |
| license | CC BY 4.0 + explicit ČÚZK consent for OSM (Nov 2023) |
| license_url | https://creativecommons.org/licenses/by/4.0/ ; consent recorded on https://wiki.openstreetmap.org/wiki/Cs:%C4%8Cesko/freemap#%C4%8C%C3%9AZK |
| license_status | ok |
| update_freq | ZABAGED is updated continuously; GPKG snapshot 2026-08-18 |
| impact | 4 |
| sync_fit | Sync for PS/LZ/VR (points, stable ref:zabaged fid_zbg, 1:1); MapRoulette for KA (fountain vs spring needs review) |
| verified | yes |

## Try it
- **Map preview:** [samples/zabaged-prameny-studny.geojson](../samples/zabaged-prameny-studny.geojson): all 273 objects in Brdy (bbox 13.75,49.60,14.05,49.80), pre-tagged, with `in_osm_50m` = whether OSM has any spring/well/fountain/drinking_water within 50 m. 219 of 273 have no OSM counterpart.
- **QGIS:** *Layer → Add Layer → Add ArcGIS REST Server Layer → New*, URL `https://ags.cuzk.gov.cz/arcgis/rest/services/ZABAGED_POLOHOPIS/MapServer`, connect and add *Zdroj podzemních vod* (id 19). Or *Add WFS Layer*, URL `https://ags.cuzk.gov.cz/arcgis/services/ZABAGED_POLOHOPIS/MapServer/WFSServer`, layer `Zdroj_podzemních_vod`. Native CRS EPSG:5514. Filter springs with `"typzdroj_k" = 'PS'`.
- **Web:** ČÚZK Geoprohlížeč https://ags.cuzk.gov.cz/geoprohlizec/

## Notes
- **Upstream status:** listed in the ZABAGED table on the Codeberg wiki `vfosnar/osm` page [Synchronizace](https://codeberg.org/vfosnar/osm/wiki/Synchronizace) with no status mark (not compared or imported yet, as of 2026-09-28).
- **Not known:** the ZABAGED POI import (Cs:POI_ZABAGED_Import) covers 13 building/service layers only; Sync has only the ZABAGED fuel, fire station, police, post office, embassy, charging, weather station, hospital, social facility, public office and healthcare datasets. The known "Studánky" entry on Cs:Česko/freemap is a different source (estudanky.eu, CC BY-NC-ND, incompatible). ZABAGED is licence-clean.
- **Gap (Postpass 2026-09-27, 50 m match against natural=spring, man_made=water_well/spring_box, amenity=drinking_water/fountain):**
  - Brdy (13.75,49.60,14.05,49.80): 86 springs in ZABAGED, 47 missing in OSM (55 %); 168 of 177 wells missing.
  - Jeseníky (17.05,50.00,17.35,50.20): 79 springs, 47 missing (59 %); 41 of the 79 are named.
  - Nationally ZABAGED has 11,060 springs against 4,844 natural=spring in OSM.
- **Caveats:** "studna, vrt" mixes public wells, private wells and boreholes, so import those only after review (or skip them). The KA "kašna" photo in the catalogue is a spring basin/trough, not a decorative city fountain, so map it case by case. The spring layer has no drinking-water attribute; never add drinking_water=yes from it. Match radius: ZABAGED states 2 m accuracy, but OSM springs are often placed by hand, so 50 m was used.
- **Suggested workflow:** named springs (5,370) first as a Sync dataset with ref:zabaged; unnamed springs as a MapRoulette challenge, as was done for other ZABAGED layers in Cs:Projekt měsíce.
- Wiki pages read: Tag:natural=spring, Cs:Tag:natural=spring, Tag:man_made=water_well, Tag:amenity=fountain, Key:drinking_water, Key:ref:zabaged. ZABAGED catalogue object 4.01 (`4_Vodstvo/ft_bh170.html`, version 01.07.2026).

## Wiki entry
```
===ZABAGED – prameny a studny===
* dataset: ZABAGED® 4.01 Zdroj podzemních vod (pramen, studna/vrt, kašna, lázeňské zřídlo)
* gestor: [https://www.cuzk.gov.cz/ ČÚZK]
* licence: CC BY 4.0 + souhlas ČÚZK [https://creativecommons.org/licenses/by/4.0/]
* datové primitivy: body
* odkaz: https://ags.cuzk.gov.cz/arcgis/rest/services/ZABAGED_POLOHOPIS/MapServer/19
* navržený tag {{tag|natural|spring}}, {{tag|man_made|water_well}}, {{tag|ref:zabaged|<FID_ZBG>}}
* poznámka: ZABAGED má 11 060 pramenů (5 370 pojmenovaných), OSM 4 844; v Brdech i Jeseníkách chybí v OSM přes polovinu pramenů
```
