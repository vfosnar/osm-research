# ZABAGED Elektrárna (plocha): solar parks and other power plants with ERÚ ID and output, cross-checked with Global Renewables Watch

| Field | Value |
|---|---|
| publisher | Český úřad zeměměřický a katastrální (ČÚZK), Zeměměřický úřad. Cross-check: Microsoft AI for Good, Global Renewables Watch (GRW) |
| url | https://ags.cuzk.gov.cz/arcgis/rest/services/ZABAGED_POLOHOPIS/MapServer/126 (layer "Elektrárna (plocha)"); point layer 86 "Elektrárna (bod)"; bulk https://openzu.cuzk.gov.cz/opendata/ZABAGED-GPKG/epsg-5514/ZABAGED-5514-gpkg-20260818.zip. GRW: https://github.com/microsoft/global-renewables-watch/releases/download/v1.0/solar_all_2024q2_v1.gpkg and …/wind_all_2024q2_v1.gpkg |
| format | ArcGIS REST (GeoJSON, outSR=4326), GeoPackage. GRW: GeoPackage, EPSG:3857 |
| coords | yes (polygons) |
| records | ZABAGED layer 126: 2,141 polygons. podtypel_p: solární 1,679; plynová a spalovací 325; vodní 76; parní 54; vodní přečerpávací 3; jaderná 2; paroplynová 1; větrná 1. Fields: fid_zbg, jmeno, id_eru, vykon (MW). 1,642 of the 1,679 solar polygons carry id_eru and vykon (1,537 distinct id_eru). GRW Czechia: 835 solar polygons (construction quarter, land cover 2018) and 174 wind turbines |
| osm_tags | power=plant + plant:source=solar + plant:method=photovoltaic + plant:output:electricity=&lt;vykon&gt; MW; gas/combustion: power=plant + plant:source=biogas\|gas (check with ERÚ fuel); ref:zabaged=&lt;fid_zbg&gt;; ERÚ premise ID as proposed in `eru-vyrobny-elektriny.md` |
| osm_count_cz | power=plant 886; plant:source=solar 524; generator:source=solar 41,785 (mostly rooftop and panel rows) (Geofabrik taginfo CZ, 2026-09-28) |
| license | ZABAGED: CC BY 4.0 + ČÚZK consent for OSM. GRW: MIT (repository LICENSE; the README gives no separate data licence) |
| license_url | https://creativecommons.org/licenses/by/4.0/ ; https://wiki.openstreetmap.org/wiki/Cs:%C4%8Cesko/freemap#%C4%8C%C3%9AZK ; https://github.com/microsoft/global-renewables-watch/blob/main/LICENSE |
| license_status | ok (ZABAGED). GRW: needs_waiver (MIT carries a notice requirement; the LWG has not ruled) |
| update_freq | ZABAGED continuous; GRW one release (2024 Q2) |
| impact | 4 |
| sync_fit | iD fork (power-plant polygons, stable ref:zabaged fid_zbg, plant:source mapping) |
| verified | yes |

## Try it
- **Map preview:** [samples/zabaged-elektrarny-plochy.geojson](../samples/zabaged-elektrarny-plochy.geojson): all 98
  ZABAGED power-plant polygons in Slovácko (bbox 17.25,48.75,17.75,49.25), with `id_eru`, `vykon_MW`,
  `osm_power_plant_within_300m` and `osm_solar_object_within_300m`. 87 solar polygons: 21 have no OSM solar
  object within 300 m, and 67 have no power=plant within 300 m. The 8 gas/combustion polygons (biogas
  stations) have no OSM plant.
- **QGIS:** *Layer → Add Layer → Add ArcGIS REST Server Layer → New*, URL
  `https://ags.cuzk.gov.cz/arcgis/rest/services/ZABAGED_POLOHOPIS/MapServer`, add *Elektrárna (plocha)*
  (id 126). Native CRS EPSG:5514. GRW: *Add Vector Layer* on the downloaded `.gpkg`, filter `"COUNTRY" = 'Czechia'`.

## Notes
- **Upstream status:** listed in the ZABAGED table on the Codeberg wiki `vfosnar/osm` page [Synchronizace](https://codeberg.org/vfosnar/osm/wiki/Synchronizace) with no status mark (not compared or imported yet, as of 2026-09-28).
- **Gap, national** (local match against the 2026-09-27 Czechia extract; OSM nodes and way centroids of
  power=plant/generator; 38 plant relations not included, so the gap is slightly overstated):
  - Of the 1,679 ZABAGED solar polygons, 1,212 have no OSM power=plant within 300 m of the polygon centroid.
    294 have no ground-mounted OSM solar object at all (plant, or generator not tagged as rooftop/building).
    The remaining ~920 are drawn as panel rows or landuse but lack power=plant, name and output. ZABAGED's
    `vykon` and `id_eru` fill exactly that.
  - Gas/combustion (mostly biogas and CHP): 310 of 325 have no OSM power=plant within 300 m. This matches
    the biogas gap found in `eru-vyrobny-elektriny.md`. Hydro: 43 of 76. Steam: 32 of 54.
- **Link to ERÚ:** `id_eru` has the same form as the ERÚ PremiseElecId (`14294_T11`), so
  ZABAGED supplies the geometry that the ERÚ licence register lacks. Join the two for the name, operator
  and fuel.
- **Not known upstream:** layer 126 is not on Cs:POI_ZABAGED_Import and not a dataset in Sync's
  `config.toml` (checked 2026-09-28).
- **Global Renewables Watch as a cross-check** (arXiv 2503.14860; quarterly detections 2017 Q4 to 2024 Q2):
  - Solar: 835 CZ polygons, 36.7 km². Only 26 are more than 400 m from any ZABAGED solar polygon
    (by detection date: 2024: 7, 2022: 6, 2021: 1, 2019: 3, 2018: 4, 2017 or earlier: 5), so GRW mostly
    confirms ZABAGED and adds about 14 farms first detected in 2021 or later. 579 of 835 have no OSM power=plant within 300 m.
  - Wind: 174 turbines, 172 of them have an OSM wind generator within 150 m. There is no wind gap.
  - Use GRW only to find new farms ZABAGED has not yet surveyed, then map them from ortophoto.
- **Rejected alternatives** (checked 2026-09-28):
  - TransitionZero Solar Asset Mapper (Zenodo 11368204) is CC BY-NC 4.0, so incompatible.
  - Global Energy Monitor Global Solar Power Tracker (Feb 2026, CC BY 4.0; copy in Zenodo 20843067
    `GEM_GSPT.xlsx`) has 735 CZ rows, but 700 carry TransitionZero IDs. GEM's methodology page says
    1–20 MW records come from "TransitionZero's Solar Asset Mapper" where no government source exists, and
    the same page cites TZ-SAM as CC BY-NC 4.0. Czech coverage is therefore NC-derived.
- Wiki pages read: Tag:power=plant (below 1 MW use power=generator; plant:output:* recommended),
  Key:plant:source. Filter out polygons with `vykon` &lt; 1 MW, or tag them power=generator.

## Wiki entry
```
===ZABAGED – elektrárny (plochy), zejména fotovoltaické===
* dataset: ZABAGED Elektrárna (plocha)
* gestor: [https://www.cuzk.cz/ ČÚZK – Zeměměřický úřad]
* licence: CC BY 4.0 + souhlas ČÚZK [https://creativecommons.org/licenses/by/4.0/]
* datové primitivy: plochy
* odkaz: https://ags.cuzk.gov.cz/arcgis/rest/services/ZABAGED_POLOHOPIS/MapServer/126
* navržený tag {{tag|power|plant}} + {{tag|plant:source|solar}} + {{tag|plant:output:electricity|<vykon> MW}}, {{tag|ref:zabaged|<fid_zbg>}}
* poznámka: 1 679 solárních elektráren s ID ERÚ a výkonem; 1 212 z nich nemá v OSM power=plant, 294 v OSM chybí úplně; bioplynové stanice (310 z 325) v OSM chybí
```
