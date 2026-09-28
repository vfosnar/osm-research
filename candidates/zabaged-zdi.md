# ZABAGED 1.23 Zeď – walls, retaining walls, noise barriers (and the fence question)

| Field | Value |
|---|---|
| publisher | Český úřad zeměměřický a katastrální (ČÚZK), Zeměměřický úřad |
| url | https://ags.cuzk.gov.cz/arcgis/rest/services/ZABAGED_POLOHOPIS/MapServer/39 (ArcGIS REST, layer "Zeď"); WFS type `ZABAGED_POLOHOPIS:Zeď` at https://ags.cuzk.gov.cz/arcgis/services/ZABAGED_POLOHOPIS/MapServer/WFSServer; bulk: https://openzu.cuzk.gov.cz/opendata/ZABAGED-GPKG/epsg-5514/ZABAGED-5514-gpkg-20260818.zip (whole ZABAGED, 5.8 GB) |
| format | ArcGIS REST (JSON/GeoJSON, outSR=4326), WFS, GeoPackage |
| coords | yes (lines, stated accuracy 1 m) |
| records | 83,833 lines: zeď opěrná (ZOP) 56,474; no type 20,818; protihluková stěna (PHS) 4,106; zeď vodního díla (ZVD) 1,501; zeď ostatní (ZOS) 934. Attributes: typ, jmeno, length. Stable ID `fid_zbg`. |
| osm_tags | ZOP → barrier=retaining_wall; PHS → barrier=wall + wall=noise_barrier; ZOS / no type → barrier=wall; ZVD → barrier=wall or man_made=embankment/dam context, review; ref:zabaged=&lt;fid_zbg&gt; |
| osm_count_cz | taginfo CZ 2026-09-27: barrier=wall 26,568; barrier=retaining_wall 10,325; barrier=city_wall 1,787; wall=noise_barrier 2,089 |
| license | CC BY 4.0 + explicit ČÚZK consent for OSM (Nov 2023) |
| license_url | https://creativecommons.org/licenses/by/4.0/ ; consent recorded on https://wiki.openstreetmap.org/wiki/Cs:%C4%8Cesko/freemap#%C4%8C%C3%9AZK |
| license_status | ok |
| update_freq | ZABAGED is updated continuously; GPKG snapshot 2026-08-18 |
| impact | 2 |
| sync_fit | iD fork (wall lines, stable ref:zabaged fid_zbg; ZVD subtype needs review) |
| verified | yes |

## Try it
- **Map preview:** [samples/zabaged-zdi.geojson](../samples/zabaged-zdi.geojson): all 247 wall lines in Kutná Hora (bbox 15.24,49.93,15.30,49.96), pre-tagged, with `in_osm_8m` = whether an OSM wall/retaining_wall/city_wall/fence lies within 8 m of the segment midpoint. 155 of 247 (10.5 km) have none.
- **QGIS:** *Layer → Add Layer → Add ArcGIS REST Server Layer → New*, URL `https://ags.cuzk.gov.cz/arcgis/rest/services/ZABAGED_POLOHOPIS/MapServer`, add *Zeď* (id 39). Or *Add WFS Layer*, URL `https://ags.cuzk.gov.cz/arcgis/services/ZABAGED_POLOHOPIS/MapServer/WFSServer`, layer `Zeď`. Native CRS EPSG:5514.

## Notes
- **Upstream status:** listed in the ZABAGED table on the Codeberg wiki `vfosnar/osm` page [Synchronizace](https://codeberg.org/vfosnar/osm/wiki/Synchronizace) with no status mark (not compared or imported yet, as of 2026-09-28).
- **Does ZABAGED have fences? No.** Checked 2026-09-27 against every object page of the current web catalogue ("Katalog objektů ZABAGED®", version 4.7, "Rozšířená webová verze aktuální k: 01.07.2026", https://geoportal.cuzk.gov.cz/Dokumenty/ZABAGED_katalog/CS/index.html, 145 object types; plain curl needs a cookie jar or it redirects to Podminky.pdf) and against the 149 layers of the ArcGIS service ZABAGED_POLOHOPIS. No type or attribute value is a fence (plot, oplocení, ohrazení). The only fence-related items are:
  - 1.23 ZEĎ (`1_Sidla/ft_al260.html`): "Samostatný stavební objekt z pevného materiálu … Zahrnuje hřbitovní zdi, opěrné zdi, mohutnější zdi, které mají funkci plotu, a protihlukové stěny". Solid walls only.
  - 2.36 ZÁBRANA (`2_Komunikace/ft_ap041.html`): barrier points on roads (see [zabaged-zabrany](zabaged-zabrany.md)).
  - 6.12 LINIOVÁ VEGETACE (`6_Vegetace_a_povrch/ft_ec035.html`): tree rows, which by definition include "jednoduchý plot sestavený ze stříhaných křovin" (a clipped hedge).
  - 6.01 HRANICE UŽÍVÁNÍ PŮDY (`ft_ex100.html`): land-use boundary lines with no attributes; fences often follow them but are not recorded.
  - "oplocení" appears only in the text of 1.27 AREÁL ÚČELOVÉ ZÁSTAVBY ("obvykle hranicemi užívání půdy, často oplocením").
- **Other ČÚZK products:** Data50 (69 layers) and Data250 (118 layers) have no fence layer. The RÚIAN service has none. The cadastral WMS (services.cuzk.gov.cz/wms/wms.asp) has "Další prvky mapy" but no fence layer. Fences **do** exist in the regional Digitální technická mapa (DTM, "plot" lines), covered in [known-dtm-zps-kraje](known-dtm-zps-kraje.md): 5,888 fence lines in Telč alone.
- **Gap (Kutná Hora, Postpass 2026-09-27):** ZABAGED 247 lines / 17.3 km; OSM 88 barrier=wall (4.8 km) + 61 retaining_wall (2.1 km) + 12 city_wall (1.1 km). 155 ZABAGED segments (10.5 km) have no OSM wall or fence within 8 m.
- **Caveats:** the catalogue sets a minimum length of 50 m for "zeď ostatní"; retaining walls have no minimum, so ZOP dominates. ZVD (walls of hydraulic structures) overlap dams and weirs. Lines should be matched and drawn by a mapper (Sync/MapRoulette), not imported blind. Low routing value, higher value for rendering and hiking in terrain (retaining walls along paths).
- Wiki pages read: Tag:barrier=wall, Tag:barrier=retaining_wall, Key:wall, Key:ref:zabaged.

## Wiki entry
```
===ZABAGED – zdi a opěrné zdi===
* dataset: ZABAGED® 1.23 Zeď (zeď opěrná, zeď ostatní, zeď vodního díla, protihluková stěna)
* gestor: [https://www.cuzk.gov.cz/ ČÚZK]
* licence: CC BY 4.0 + souhlas ČÚZK [https://creativecommons.org/licenses/by/4.0/]
* datové primitivy: linie
* odkaz: https://ags.cuzk.gov.cz/arcgis/rest/services/ZABAGED_POLOHOPIS/MapServer/39
* navržený tag {{tag|barrier|retaining_wall}}, {{tag|barrier|wall}}, {{tag|wall|noise_barrier}}, {{tag|ref:zabaged|<FID_ZBG>}}
* poznámka: 83 833 linií (56 474 opěrných zdí); v Kutné Hoře chybí v OSM 10,5 km ze 17,3 km; ploty ZABAGED neobsahuje
```
