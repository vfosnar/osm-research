# ZABAGED 1.27 Areál účelové zástavby – vodojem zemní (covered water reservoirs)

| Field | Value |
|---|---|
| publisher | Český úřad zeměměřický a katastrální (ČÚZK), Zeměměřický úřad |
| url | https://ags.cuzk.gov.cz/arcgis/rest/services/ZABAGED_POLOHOPIS/MapServer/114 (layer "Areál účelové zástavby", filter `typzast_p = 'vodojem zemní'`); WFS type `ZABAGED_POLOHOPIS:Areál_účelové_zástavby` at https://ags.cuzk.gov.cz/arcgis/services/ZABAGED_POLOHOPIS/MapServer/WFSServer |
| format | ArcGIS REST (JSON/GeoJSON, outSR=4326), WFS |
| coords | yes (areas; stated accuracy 2 m on the outline) |
| records | 6,950 areas with `typzast_p` = vodojem zemní (`typzast_k` 407), median 725 m²; no names. Stable ID `fid_zbg`. |
| osm_tags | man_made=reservoir_covered + ref:zabaged=&lt;fid_zbg&gt; (node at the centroid for Sync, or the outline as an area) |
| osm_count_cz | taginfo CZ (data until 2026-09-27): man_made=reservoir_covered 613; man_made=water_tower 670; man_made=water_works 1,317 |
| license | CC BY 4.0 + explicit ČÚZK consent for OSM |
| license_url | https://creativecommons.org/licenses/by/4.0/ ; consent recorded on https://wiki.openstreetmap.org/wiki/Cs:%C4%8Cesko/freemap |
| license_status | ok |
| update_freq | ZABAGED is updated continuously |
| impact | 3 |
| sync_fit | Sync: 1:1 subtype, stable `fid_zbg`; the adapter sends the area centroid as a point (Tag:man_made=reservoir_covered allows nodes). Or iD fork for the outline: the `arealucelovezastavby` table is empty and needs subtype rules on `typzast_p` first. |
| verified | yes |

## Try it
- **Map preview:** [samples/zabaged-vodojemy-zemni.geojson](../samples/zabaged-vodojemy-zemni.geojson): all 470 vodojemy zemní in the bbox 15.40,49.20,16.20,49.80 (Vysočina: Jihlava – Třebíč – Žďár nad Sázavou), outlines with `osm_dist_m` and `in_osm` (OSM reservoir_covered / water_tower / storage_tank / water_works within 100 m of the centroid). 409 of 470 have none.
- **QGIS:** *Layer → Add Layer → Add ArcGIS REST Server Layer → New*, URL `https://ags.cuzk.gov.cz/arcgis/rest/services/ZABAGED_POLOHOPIS/MapServer`, add layer 114, then *Layer Properties → Source → Query Builder* `"typzast_p" = 'vodojem zemní'`. Native CRS EPSG:5514.
- One-off GeoJSON: `https://ags.cuzk.gov.cz/arcgis/rest/services/ZABAGED_POLOHOPIS/MapServer/114/query?where=typzast_p%3D%27vodojem%20zemn%C3%AD%27&outFields=fid_zbg,typzast_p&outSR=4326&f=geojson` (2,000 per page, use `resultOffset`).

## Notes
- **What it is:** the earth-covered drinking-water reservoirs above villages (grassed mound with a small entrance building). ZABAGED captures them as an Areál účelové zástavby subtype (catalogue 1.27, `1_Sidla/ft_al000.html`: "Část území … která slouží k určitému účelu … Způsob využívání areálu je specifikován jeho atributem"). The tower type is a separate layer (1.15 Vodojem věžový, 766 points; OSM already has 670 water towers).
- **Tag:** Tag:man_made=reservoir_covered: "A covered reservoir is a large man-made tank for holding fresh water … functionally equivalent to water towers", onNode=yes, onArea=yes.
- **Gap (local match against the 2026-09-27 Czechia extract):** 5,776 of 6,950 (83 %) have no OSM man_made=reservoir_covered, water_tower, storage_tank or water_works within 100 m of the centroid. Only 404 of those 5,776 have any man_made object within 100 m, mostly towers and masts (hilltop sites). Not checked: OSM buildings named "Vodojem" without a man_made tag; the Sync match step will show them.
- **Why it matters:** hilltop landmarks for orientation, and water infrastructure for utilities and emergency mapping.
- Same approach fits the other `typzast_p` subtypes with a gap: čistírna odpadních vod 3,819 (OSM man_made=wastewater_plant 1,703) and úpravna vody 493. See [research/zabaged-layer-audit.md](../research/zabaged-layer-audit.md).

## Wiki entry
```
===ZABAGED – vodojemy zemní===
* dataset: ZABAGED® 1.27 Areál účelové zástavby, typ vodojem zemní
* gestor: [https://www.cuzk.gov.cz/ ČÚZK]
* licence: CC BY 4.0 + souhlas ČÚZK [https://creativecommons.org/licenses/by/4.0/]
* datové primitivy: plochy (pro Sync centroid jako bod)
* odkaz: https://ags.cuzk.gov.cz/arcgis/rest/services/ZABAGED_POLOHOPIS/MapServer/114
* navržený tag {{tag|man_made|reservoir_covered}}, {{tag|ref:zabaged|<FID_ZBG>}}
* poznámka: 6 950 zemních vodojemů, 5 776 (83 %) z nich v OSM chybí; v OSM je jen 613 man_made=reservoir_covered
```
