name: Data Olomouc – Stojany Olomouc, Hydranty SMOl, Cyklostezky Olomouc
publisher: Statutární město Olomouc
url: https://opendata.olomouc.eu/ (ArcGIS Hub; services3.arcgis.com/W4pu2xsRj3cVEctz)
format: ArcGIS FeatureServer + hub downloads (GeoJSON, CSV, SHP, KML)
coords: yes
records: bike stands 395 points; fire hydrants 277 points; cycle paths 95 lines; public (cyklo)servisní místa 4
osm_tags: amenity=bicycle_parking; emergency=fire_hydrant (+fire_hydrant:type=underground|pillar — CZ usage 1,051 / 2,931; fire_hydrant:diameter; ref); highway=cycleway
osm_count_cz: amenity=bicycle_parking 13,650; emergency=fire_hydrant 4,217 (taginfo CZ 2026-09-26)
license: CC BY 4.0 (item licenseInfo "Licence CC BY 4.0" on every dataset)
license_url: https://creativecommons.org/licenses/by/4.0/
license_status: needs_waiver
update_freq: unknown (hydrant revisions dated 2024)
impact: 2
verified: yes

## Endpoints
- https://services3.arcgis.com/W4pu2xsRj3cVEctz/arcgis/rest/services/stojany_OL/FeatureServer/0 (fields: Typ "STOJAN", ID only)
- https://services3.arcgis.com/W4pu2xsRj3cVEctz/arcgis/rest/services/Hydranty_SMOl/FeatureServer/0 (PODTYP podzemní/nadzemní, C_DIMEN, C_DRUHV1 pitná voda, OZNACENI address, provozovatel MOVO, GLOBALID, revision date)
- https://services3.arcgis.com/W4pu2xsRj3cVEctz/arcgis/rest/services/Cyklostezky_Olomouc/FeatureServer/0

## Notes
- OSM in Olomouc bbox (17.18,49.54,17.33,49.66, Postpass 2026-09-27): bicycle_parking 258 vs 395; fire_hydrant 36 vs 277; street lamps already 6,582 (well mapped); benches 1,132.
- Hydrants are the clearest gap (+~240) with good attributes (type, DN, pressure). Hydrant layer covers only the city's own network part (C_VLAST1 "Pomoraví", operator MOVO) — not all hydrants.
- Bike stands have no capacity/type → low attribute value.
- Olomouc does not publish trees, benches, playgrounds or toilets as open data (54 hub datasets checked, mostly pocitové mapy and cenové mapy).
- Suggested ref: `ref` = OBJECTI0 for hydrants (city hydrant ID).
- Wiki pages read: Tag:emergency=fire_hydrant, Tag:amenity=bicycle_parking.

## Wiki entry
```
===Olomouc – hydranty a stojany na kola===
* dataset: Hydranty SMOl; Stojany Olomouc; Cyklostezky Olomouc
* gestor: [https://opendata.olomouc.eu/ Statutární město Olomouc]
* licence: CC BY 4.0 [https://creativecommons.org/licenses/by/4.0/] – nutný souhlas
* datové primitivy: body (hydranty, stojany), linie (cyklostezky)
* odkaz: https://services3.arcgis.com/W4pu2xsRj3cVEctz/arcgis/rest/services/Hydranty_SMOl/FeatureServer/0
* navržený tag {{tag|emergency|fire_hydrant}}, {{tag|fire_hydrant:type|underground}}, {{tag|amenity|bicycle_parking}}
* poznámka: V OSM je v Olomouci 36 hydrantů oproti 277 v datech města.
```
