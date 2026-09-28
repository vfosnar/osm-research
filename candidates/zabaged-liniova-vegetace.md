# ZABAGED 6.12 Liniová vegetace (tree rows) + Copernicus Small Woody Features as a review layer

| Field | Value |
|---|---|
| publisher | ZABAGED: Český úřad zeměměřický a katastrální (ČÚZK), Zeměměřický úřad. SWF: European Environment Agency (EEA), Copernicus Land Monitoring Service (CLMS) |
| url | ZABAGED: https://ags.cuzk.gov.cz/arcgis/rest/services/ZABAGED_POLOHOPIS/MapServer/15 (layer "Liniová vegetace"); bulk GeoPackage https://openzu.cuzk.gov.cz/opendata/ZABAGED-GPKG/epsg-5514/ZABAGED-5514-gpkg-20260818.zip (whole ZABAGED). SWF: https://image.discomap.eea.europa.eu/arcgis/rest/services/GioLandPublic/HRL_SmallWoodyFeatures_2021_005m/ImageServer |
| format | ZABAGED: ArcGIS REST (GeoJSON, outSR=4326), GeoPackage. SWF: 5 m raster (ImageServer, EPSG:3035); the CLMS product page also lists a vector version |
| coords | yes (ZABAGED lines; SWF raster pixels) |
| records | ZABAGED layer 15: 351,398 lines nationally (typveg_p: stromořadí 351,319, živý plot 79), attributes typveg_k, typveg_p, fid_zbg. SWF 2021: linear woody features (width ≤ 30 m, length ≥ 30 m) and patches (200–5,000 m²) at 5 m, EEA38 |
| osm_tags | stromořadí → natural=tree_row (way); živý plot → barrier=hedge (way); ref:zabaged=&lt;fid_zbg&gt; (key already used in Sync's ZABAGED group) |
| osm_count_cz | natural=tree_row 15,921 ways; barrier=hedge 17,080 ways (Geofabrik taginfo CZ, 2026-09-28) |
| license | ZABAGED: CC BY 4.0 + ČÚZK consent for OSM. SWF: Copernicus full, free and open data policy (Delegated Regulation (EU) 1159/2013), source must be stated |
| license_url | https://creativecommons.org/licenses/by/4.0/ ; https://wiki.openstreetmap.org/wiki/Cs:%C4%8Cesko/freemap#%C4%8C%C3%9AZK ; https://land.copernicus.eu/en/data-policy |
| license_status | ok (ZABAGED, ČÚZK consent). SWF: ok, covered by the "EU Copernicus (GMES) data" entry on https://wiki.openstreetmap.org/wiki/Contributors |
| update_freq | ZABAGED continuous (GPKG snapshot 2026-08-18); SWF 2015 / 2018 / 2021 editions |
| impact | 4 |
| verified | yes |

## Try it
- **Map preview:** [samples/zabaged-liniova-vegetace.geojson](../samples/zabaged-liniova-vegetace.geojson), rural
  Vysočina between Polná and Přibyslav (bbox 15.62,49.46,15.68,49.50). 72 ZABAGED tree rows (22.7 km,
  `dataset` = ZABAGED, pre-tagged `natural=tree_row` + `ref:zabaged`) and 53 extra linear woody features
  from Copernicus SWF 2021 that are in neither ZABAGED nor OSM (`dataset` = Copernicus…, vectorised by
  this research as centre lines of connected 5 m pixel clusters). OSM has no tree_row or hedge in the whole bbox.
- **QGIS (ZABAGED):** *Layer → Add Layer → Add ArcGIS REST Server Layer → New*, URL
  `https://ags.cuzk.gov.cz/arcgis/rest/services/ZABAGED_POLOHOPIS/MapServer`, add *Liniová vegetace* (id 15).
  Native CRS EPSG:5514.
- **QGIS (SWF):** *Layer → Add Layer → Add ArcGIS REST Server Layer → New*, URL
  `https://image.discomap.eea.europa.eu/arcgis/rest/services/GioLandPublic`, add
  *HRL_SmallWoodyFeatures_2021_005m* (ImageServer, EPSG:3035, 1 band U8). Tested: `exportImage` for a bbox
  in EPSG:3035 returns a PNG in which woody pixels are coloured and the rest is transparent.

## Notes
- **Upstream status:** listed in the ZABAGED table on the Codeberg wiki `vfosnar/osm` page [Synchronizace](https://codeberg.org/vfosnar/osm/wiki/Synchronizace) with no status mark (not compared or imported yet, as of 2026-09-28).
- **Gap, national:** ZABAGED has 351,319 tree-row lines. OSM has 15,921 tree_row and 17,080 hedge ways.
  Even allowing for ZABAGED splitting rows into short segments, OSM holds a small fraction.
- **Gap, sample area** (bbox 15.62,49.46,15.68,49.50, OSM API map call 2026-09-28): OSM has 0 tree_row and
  0 hedge ways. ZABAGED has 72 tree rows, 22.7 km, all missing from OSM.
- **What SWF adds:** in the same bbox SWF 2021 marks 8.7% of the area as woody (1.95 km² in 404 clusters
  of 8 or more pixels). 136 clusters are elongated (length ≥ 40 m, length/width ≥ 3). Of their centre lines,
  11.3 km (61 features) lie outside any OSM wood/forest/scrub polygon. Only 1.8 km of those match a ZABAGED
  tree row within 20 m. The other 9.6 km (53 features) are woody strips that neither OSM nor ZABAGED has:
  field-boundary hedges, scrub along streams and balks. Check each one on the ČÚZK ortophoto;
  treat SWF as a review layer, not an import source. Its 5 m pixels and 2021 date limit the geometry.
- **Why ZABAGED first:** vector lines at 1 m stated accuracy, stable `fid_zbg`, updated continuously, and
  ČÚZK consent already covers OSM. The layer is not listed on Cs:POI_ZABAGED_Import and is not a dataset in
  Sync's `config.toml` (checked 2026-09-28). It is mentioned only in passing in `zabaged-zdi.md` here.
- **Tagging** (wiki Tag:natural=tree_row, Cs:Tag:natural=tree_row "Stromořadí, alej", way only;
  Tag:barrier=hedge "A line of closely spaced shrubs…"): stromořadí → natural=tree_row; the 79 živý plot →
  barrier=hedge. ZABAGED's definition of 6.12 ("Řada stromů případně křovin podél komunikací, vodních toků …
  nebo jednoduchý plot sestavený ze stříhaných křovin") mixes both. Most "stromořadí" lines along roads are
  avenues; check denotation=avenue on the wiki before adding it.
- **Conflation caveats:** skip rows that fall inside existing natural=wood / landuse=forest polygons.
  Cemetery and park avenues may already be mapped as individual natural=tree nodes.
- **SWF licence detail:** the CLMS data policy asks users to state the source and any modification
  ("Generated using European Union's Copernicus Land Monitoring Service information"). The OSM Contributors
  page already lists "EU Copernicus (GMES) data" under Regulation 1159/2013, which covers this. The LWG has
  published no specific ruling on CLMS High Resolution Layers.
- ZABAGED stromořadí count by attribute came from an ArcGIS `outStatistics` query on layer 15 (2026-09-28).

## Wiki entry
```
===ZABAGED – liniová vegetace (stromořadí)===
* dataset: ZABAGED 6.12 Liniová vegetace; doplňkově Copernicus HRL Small Woody Features 2021
* gestor: [https://www.cuzk.cz/ ČÚZK – Zeměměřický úřad]; [https://land.copernicus.eu/ EEA – Copernicus Land Monitoring Service]
* licence: CC BY 4.0 + souhlas ČÚZK [https://creativecommons.org/licenses/by/4.0/]; Copernicus data policy [https://land.copernicus.eu/en/data-policy]
* datové primitivy: linie
* odkaz: https://ags.cuzk.gov.cz/arcgis/rest/services/ZABAGED_POLOHOPIS/MapServer/15
* navržený tag {{tag|natural|tree_row}} (živý plot: {{tag|barrier|hedge}}), {{tag|ref:zabaged|<fid_zbg>}}
* poznámka: ZABAGED má 351 319 stromořadí, OSM jen 15 921 tree_row a 17 080 hedge; SWF navíc ukazuje meze a remízky, které nejsou ani v ZABAGED
```
