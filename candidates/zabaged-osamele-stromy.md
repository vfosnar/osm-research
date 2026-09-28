# ZABAGED 6.11 Významný nebo osamělý strom – solitary landmark trees

| Field | Value |
|---|---|
| publisher | Český úřad zeměměřický a katastrální (ČÚZK), Zeměměřický úřad |
| url | https://ags.cuzk.gov.cz/arcgis/rest/services/ZABAGED_POLOHOPIS/MapServer/14 (layer "Významný nebo osamělý strom, lesík"); WFS type `ZABAGED_POLOHOPIS:Významný_nebo_osamělý_strom__lesík` at https://ags.cuzk.gov.cz/arcgis/services/ZABAGED_POLOHOPIS/MapServer/WFSServer |
| format | ArcGIS REST (JSON/GeoJSON, outSR=4326), WFS |
| coords | yes (points, stated accuracy 2 m) |
| records | 57,340 points: osamělý strom 33,592, osamělý lesík 23,748 (`typveg_p`); 2,179 trees named (`jmeno`). Stable ID `fid_zbg`. |
| osm_tags | osamělý strom → natural=tree + denotation=landmark; name=&lt;jmeno&gt; when set; ref:zabaged=&lt;fid_zbg&gt;. Osamělý lesík: no import (a point standing for a group of trees; natural=wood needs an area) |
| osm_count_cz | taginfo CZ (data until 2026-09-27): natural=tree 136,325; denotation=landmark 331 |
| license | CC BY 4.0 + explicit ČÚZK consent for OSM |
| license_url | https://creativecommons.org/licenses/by/4.0/ ; consent recorded on https://wiki.openstreetmap.org/wiki/Cs:%C4%8Cesko/freemap |
| license_status | ok |
| update_freq | ZABAGED is updated continuously |
| impact | 3 |
| sync_fit | Sync for osamělý strom: points, 1:1 once filtered on `typveg_p`, stable `fid_zbg`. The iD fork table `vyznamnyneboosamelystromlesik` is empty and needs the same rule. Osamělý lesík: skip. |
| verified | yes |

## Try it
- **Map preview:** [samples/zabaged-osamele-stromy.geojson](../samples/zabaged-osamele-stromy.geojson): all 511 solitary trees in the bbox 15.60,49.40,16.20,49.80 (Žďár nad Sázavou – Velké Meziříčí – Nové Město na Moravě), with `osm_dist_m` (nearest OSM natural=tree) and `in_osm` (within 30 m). 475 of 511 have no OSM tree within 30 m.
- **QGIS:** *Layer → Add Layer → Add ArcGIS REST Server Layer → New*, URL `https://ags.cuzk.gov.cz/arcgis/rest/services/ZABAGED_POLOHOPIS/MapServer`, add layer 14 and filter `typveg_p = 'osamělý strom'`. Or *Add WFS Layer* with URL `https://ags.cuzk.gov.cz/arcgis/services/ZABAGED_POLOHOPIS/MapServer/WFSServer`, layer `Významný_nebo_osamělý_strom__lesík`. Native CRS EPSG:5514.
- One-off GeoJSON: `https://ags.cuzk.gov.cz/arcgis/rest/services/ZABAGED_POLOHOPIS/MapServer/14/query?where=typveg_p%3D%27osam%C4%9Bl%C3%BD%20strom%27&outFields=*&outSR=4326&f=geojson` (max 2,000 records per request; page with `resultOffset`).

## Notes
- **Definition** (catalogue 6.11, `6_Vegetace_a_povrch/ft_ec030.html`): "Osamělý strom – strom rostoucí mimo lesní pozemek, zdaleka viditelný, s orientačním významem. Obsahem jsou i významné pojmenované stromy … obvykle s ochranou podle zákona č. 114/1992 Sb." These are the trees a hiker navigates by, which is what `denotation=landmark` means on Tag:natural=tree ("to enhance landmarks and to tone down or skip unremarkable trees").
- **Gap (local match against the 2026-09-27 Czechia extract):** 31,918 of 33,592 solitary trees (95 %) have no OSM natural=tree within 30 m. OSM's 136k trees are mostly street and park trees in towns, while ZABAGED's are in open country.
- **Overlap:** the 2,179 named trees are mostly památné stromy; AOPK's register ([known-aopk-pamatne-stromy](known-aopk-pamatne-stromy.md)) is the better source for those (species, protection). Run it first and let Sync match the rest by distance.
- **Sync config:** `create_keys = ["natural", "denotation", "ref:zabaged"]`, `osm_query` natural=tree + ref:zabaged, adapter filter `typveg_p = 'osamělý strom'`. Match radius 30 m (stated accuracy 2 m).
- Wiki pages read: Tag:natural=tree, Tag:denotation=landmark, Key:ref:zabaged usage in Sync's `config.toml`.

## Wiki entry
```
===ZABAGED – osamělé stromy===
* dataset: ZABAGED® 6.11 Významný nebo osamělý strom, lesík (typ osamělý strom)
* gestor: [https://www.cuzk.gov.cz/ ČÚZK]
* licence: CC BY 4.0 + souhlas ČÚZK [https://creativecommons.org/licenses/by/4.0/]
* datové primitivy: body
* odkaz: https://ags.cuzk.gov.cz/arcgis/rest/services/ZABAGED_POLOHOPIS/MapServer/14
* navržený tag {{tag|natural|tree}}, {{tag|denotation|landmark}}, {{tag|ref:zabaged|<FID_ZBG>}}
* poznámka: 33 592 orientačně významných stromů ve volné krajině, z nich 31 918 (95 %) v OSM chybí
```
