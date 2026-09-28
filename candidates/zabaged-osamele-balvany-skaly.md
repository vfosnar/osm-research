# ZABAGED 7.10 Osamělý balvan, skála, skalní suk – boulders and rock outcrops

| Field | Value |
|---|---|
| publisher | Český úřad zeměměřický a katastrální (ČÚZK), Zeměměřický úřad |
| url | https://ags.cuzk.gov.cz/arcgis/rest/services/ZABAGED_POLOHOPIS/MapServer/10 (layer "Osamělý balvan, skála, skalní suk"); WFS type `ZABAGED_POLOHOPIS:Osamělý_balvan__skála__skalní_suk` at https://ags.cuzk.gov.cz/arcgis/services/ZABAGED_POLOHOPIS/MapServer/WFSServer |
| format | ArcGIS REST (JSON/GeoJSON, outSR=4326), WFS |
| coords | yes (points, stated accuracy 10 m) |
| records | 12,538 points, 788 named (`jmeno`). No attribute separating boulder, rock and rock knob. Stable ID `fid_zbg`. |
| osm_tags | osamělý balvan → natural=stone; osamělá skála / skalní suk → natural=rock; name=&lt;jmeno&gt;; ref:zabaged=&lt;fid_zbg&gt; |
| osm_count_cz | taginfo CZ (data until 2026-09-27): natural=stone 1,718; natural=rock 2,659 |
| license | CC BY 4.0 + explicit ČÚZK consent for OSM |
| license_url | https://creativecommons.org/licenses/by/4.0/ ; consent recorded on https://wiki.openstreetmap.org/wiki/Cs:%C4%8Cesko/freemap |
| license_status | ok |
| update_freq | ZABAGED is updated continuously |
| impact | 2 |
| sync_fit | MapRoulette: 1:N with no deciding attribute (the mapper chooses natural=stone or natural=rock from imagery or photos); the iD fork table `osamelybalvanskalaskalnisuk` is empty. The 788 named objects make a good first challenge. |
| verified | yes |

## Try it
- **Map preview:** [samples/zabaged-osamele-balvany-skaly.geojson](../samples/zabaged-osamele-balvany-skaly.geojson): all 305 points in the bbox 14.90,50.40,15.40,50.70 (Český ráj, Mnichovo Hradiště – Turnov – Jičín), with name, `osm_dist_m` and `in_osm` (OSM natural=stone or rock within 50 m). 287 of 305 have none.
- **QGIS:** *Layer → Add Layer → Add ArcGIS REST Server Layer → New*, URL `https://ags.cuzk.gov.cz/arcgis/rest/services/ZABAGED_POLOHOPIS/MapServer`, add layer 10. Or *Add WFS Layer*, URL `https://ags.cuzk.gov.cz/arcgis/services/ZABAGED_POLOHOPIS/MapServer/WFSServer`, layer `Osamělý_balvan__skála__skalní_suk`. Native CRS EPSG:5514.
- One-off GeoJSON: `https://ags.cuzk.gov.cz/arcgis/rest/services/ZABAGED_POLOHOPIS/MapServer/10/query?where=1%3D1&outFields=*&outSR=4326&f=geojson` (2,000 per page, use `resultOffset`).

## Notes
- **Definition** (catalogue 7.10, `7_Terenni_relief/ft_db161.html`): "Osamělý balvan – izolovaný úlomek horniny větších rozměrů odloučený od skalního útvaru a přemístěný gravitací, vodou apod." and "Osamělá skála – izolovaný, málo rozlehlý skalní útvar, který výrazně vyčnívá nad okolní povrch". Capture criteria: height over 1 m, area under 1,000 m².
- **Tags:** Tag:natural=stone "A single notable freestanding rock, which may differ from the composition of the terrain it lies in" fits balvan; Tag:natural=rock "A notable rock or group of rocks attached to the underlying bedrock" fits skála and skalní suk. The ZABAGED record doesn't say which, hence MapRoulette.
- **Gap (local match against the 2026-09-27 Czechia extract):** 11,216 of 12,538 (89 %) have no OSM natural=stone or natural=rock within 50 m. In the Žďár sample (bbox A of the audit) 19 of 30 were missing, in Český ráj (bbox B) 103 of 105.
- Named rocks are hiking destinations; the 10 m accuracy is enough to find them on the orthophoto or DMR 5G hillshade.
- Related: layer 12/13 Skupina balvanů (68,348 points, 9,611 lines) and layer 130 Skalní útvary (39,450 areas) cover boulder fields and larger rock areas; see [research/zabaged-layer-audit.md](../research/zabaged-layer-audit.md).

## Wiki entry
```
===ZABAGED – osamělé balvany a skály===
* dataset: ZABAGED® 7.10 Osamělý balvan, skála, skalní suk
* gestor: [https://www.cuzk.gov.cz/ ČÚZK]
* licence: CC BY 4.0 + souhlas ČÚZK [https://creativecommons.org/licenses/by/4.0/]
* datové primitivy: body
* odkaz: https://ags.cuzk.gov.cz/arcgis/rest/services/ZABAGED_POLOHOPIS/MapServer/10
* navržený tag {{tag|natural|stone}} nebo {{tag|natural|rock}} (volí maper), {{tag|ref:zabaged|<FID_ZBG>}}
* poznámka: 12 538 balvanů a skal (788 pojmenovaných), 11 216 (89 %) z nich v OSM chybí
```
