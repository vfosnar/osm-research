# Zvláště chráněná území + Natura 2000 (protected-area boundaries) – AOPK ČR / ÚSOP

| Field | Value |
|---|---|
| publisher | Agentura ochrany přírody a krajiny ČR (AOPK ČR), IČO 62933591 |
| url | MZCHÚ https://data.nature.cz/ds/1/download ; VZCHÚ https://data.nature.cz/ds/3/download ; EVL https://data.nature.cz/ds/8/download ; GeoJSON (MZCHÚ layer, verified 2026-09-27) https://gis-aopkcr.opendata.arcgis.com/datasets/aopkcr::maloplošná-zvláště-chráněná-území.geojson ; REST https://gis.nature.cz/arcgis/rest/services/UzemniOchrana/ChranUzemi/MapServer and .../UzemniOchrana/Natura2000/MapServer ; WFS https://gis.nature.cz/arcgis/services/UzemniOchrana/ChranUzemi/MapServer/WFSServer and https://gis.nature.cz/arcgis/services/UzemniOchrana/Natura2000/MapServer/WFSServer (the earlier path under `/arcgis/rest/services/…/WFSServer` returns HTTP 400) |
| format | SHP (S-JTSK), GeoJSON/KML/CSV (ArcGIS Hub), WFS, ArcGIS REST |
| coords | yes (polygons) |
| records | MZCHÚ 2,687 (PP 1,621, PR 830, NPP 126, NPR 110); VZCHÚ 33 (NP + CHKO); national-park quiet zones 23; Ptačí oblasti 42; EVL 1,111 (REST counts 2026-09-27) |
| osm_tags | boundary=protected_area + protect_class (NP 2, NPP/PP 3, NPR/PR 4, CHKO 5, Natura 2000 97) + protection_title + name (+ leisure=nature_reserve for reserves); suggested ref:drusop=&lt;KOD&gt;, Natura: ref=&lt;SITECODE&gt; or a new ref:natura2000 |
| osm_count_cz | boundary=protected_area 3,661; leisure=nature_reserve 3,376; protect_class 3=2,013, 4=1,062, 5=56, 2=11, 97=18; protection_title "Přírodní památka (PP)" 1,843, "Přírodní rezervace (PR)" 1,015, NPP 160, NPR 123 (taginfo 2026-09-26) |
| license | CC BY 4.0, attribution "(c) AOPK ČR" (same licence block on data.nature.cz dataset pages; NKOD entries carry no terms spec) |
| license_url | https://data.nature.cz/ds/1 ; https://creativecommons.org/licenses/by/4.0/ |
| license_status | needs_waiver |
| update_freq | MZCHÚ quarterly (NKOD); others irregular |
| impact | 2 |
| sync_fit | iD fork (protected-area polygons, stable KOD/SITECODE, protect_class 1:1) |
| verified | partial |

## Try it

- **Map preview:** [samples/aopk-zvlaste-chranena-uzemi.geojson](../samples/aopk-zvlaste-chranena-uzemi.geojson) shows the Natura 2000 gap: the 181 EVL and 8 Ptačí oblasti that intersect the South Moravia bbox 16.0,48.6,17.2,49.3. It was taken from the ArcGIS REST service on 2026-09-27 with boundaries simplified to about 30 m.
- **QGIS:** *Layer → Add Layer → Add ArcGIS REST Server Layer…* → *New*, URL `https://gis.nature.cz/arcgis/rest/services/UzemniOchrana/Natura2000/MapServer` (layer 0 = PO, 1 = EVL). For MZCHÚ/VZCHÚ use `https://gis.nature.cz/arcgis/rest/services/UzemniOchrana/ChranUzemi/MapServer`. As a WFS, use *Add WFS Layer* with `https://gis.nature.cz/arcgis/services/UzemniOchrana/Natura2000/MapServer/WFSServer`.
- **Web viewer:** https://drusop.aopk.gov.cz/ (ÚSOP register). Each sample feature's `url` opens its record there.

## Notes
- **National ZCHÚ are essentially all mapped already.** Counts by `protection_title` meet or exceed AOPK counts, which suggests abolished or duplicate areas. In the South Moravia bbox 16.0,48.6,17.2,49.3, OSM has ~400 protected-area polygons vs 296 AOPK MZCHÚ. CHKOs were imported from EEA CDDA in 2012 (Cs:Česko/freemap). So the value is **maintenance**: stable IDs (AOPK `KOD`, `ID_ISOP`), boundary refresh after re-declarations (`ZMENA_G` = geometry change date), and removal of abolished areas. Few OSM objects carry an AOPK ID (ref:drusop 3, ref:DRUSOP 4, ref:aopk 3).
- **Real gap: Natura 2000.** 42 SPAs + 1,111 SCIs (EVL), with only 18 `protect_class=97` in OSM. Whether Natura 2000 should be in OSM at all is debated, since it is administrative and largely overlaps national ZCHÚ. Ask the community first.
- **Other AOPK layers (same licence).** Geoparky (NKOD), Přírodní parky (REST `ObecnaOchrana/PrirodniPark`), Ekodukty (`AplikovanaOchrana/Ekodukty`), Záchranné stanice (`AplikovanaOchrana/ZachranneStanice`), Smluvně chráněná území, ochranná pásma. Not counted in detail.
- **Tagging.** Read Cs:Tag:boundary=protected area (raw 2026-09-27) for the protect_class table. The Czech mapping in use: PP/NPP=3, PR/NPR=4, CHKO=5, NP=2, Natura 2000=97.
- Contact: AOPK data team via data.nature.cz; the data steward named for AOPK datasets there is Jan Votrubec, jan.votrubec@aopk.gov.cz.

## Wiki entry
```
===Zvláště chráněná území a Natura 2000 (AOPK ČR)===
* dataset: Maloplošná a velkoplošná zvláště chráněná území, Evropsky významné lokality, Ptačí oblasti
* gestor: [https://www.nature.cz/ Agentura ochrany přírody a krajiny ČR]
* licence: CC BY 4.0, uvádět „(c) AOPK ČR“ [https://data.nature.cz/ds/1] – nutný souhlas pro OSM
* datové primitivy: plochy
* odkaz: https://data.nature.cz/ds/1/download , https://gis.nature.cz/arcgis/rest/services/UzemniOchrana/ChranUzemi/MapServer
* navržený tag {{tag|boundary|protected_area}} + {{tag|protect_class|3/4/5}}, {{tag|ref:drusop|<KOD>}}
* poznámka: ZCHÚ jsou v OSM prakticky kompletní (chybí jen ID a aktualizace hranic); Natura 2000 (1 111 EVL + 42 PO) v OSM téměř není
```
