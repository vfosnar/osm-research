name: Protihlukové bariéry (Praha)
publisher: IPR Praha
url: https://mp.iprpraha.cz/arcgis/rest/services/Hosted/HM_CUR_HM_HLUKOCHR_BARIERY_L/FeatureServer/0 ; catalogue https://opendata.geoportalpraha.cz/datasets/iprpraha::protihlukové-bariéry-1
format: ArcGIS FeatureServer (JSON/GeoJSON), Hub downloads
coords: yes (lines)
records: 731 line segments (2026-09-27), total geodesic length 118.1 km (computed from WGS84 geometry; SHAPE__Length sum 184 km is in Web Mercator units)
osm_tags: barrier=wall + wall=noise_barrier + height=<vyska>
osm_count_cz: wall=noise_barrier 2,089 CZ (taginfo 2026-09-27); Prague 209 ways, 36.9 km (Postpass ST_Length geography, relation 435514)
license: CC BY 4.0 + IPR consent for all open data in OSM (2018)
license_url: https://geoportalpraha.cz/data-a-sluzby/otevrena-data ; https://lists.openstreetmap.org/pipermail/talk-cz/2018-February/018526.html
license_status: ok
update_freq: irregular (dct:modified 2024-09-13)
impact: 3
verified: yes

## Notes

**Fields.**
- `ulice`: street, e.g. "Pražský okruh" or "Evropská".
- `popis`, `vyska` (height in m), `kat_uzemi`, `id_clona` (e.g. "clona-001", a barrier id
  usable as a ref), `globalid`.

**OSM gap.** OSM has about 37 km of noise barriers in Prague, against about 118 km in the
dataset, so roughly 80 km are missing. Heights are also missing on most OSM barriers.

**Caveats.**
- Geometry comes from the noise-mapping inputs, so alignment should be checked against the IPR
  orthophoto (itself permitted for OSM). There is also a companion layer "Protihlukové valy"
  (earth berms, `HM_CUR_HM_HLUKOCHR_VALY_P`), which I did not evaluate.
- Wiki read: Tag:wall=noise_barrier (requires barrier=wall; height optional).

## Wiki entry
```
===Protihlukové stěny (Praha)===
* dataset: Protihlukové bariéry
* gestor: [https://geoportalpraha.cz IPR Praha]
* licence: CC BY 4.0 + souhlas IPR s využitím všech opendat pro OSM (2018) [https://lists.openstreetmap.org/pipermail/talk-cz/2018-February/018526.html]
* datové primitivy: linie
* odkaz: https://mp.iprpraha.cz/arcgis/rest/services/Hosted/HM_CUR_HM_HLUKOCHR_BARIERY_L/FeatureServer/0
* navržený tag {{tag|barrier|wall}} + {{tag|wall|noise_barrier}}, {{tag|height|<vyska>}}
* poznámka: ~118 km protihlukových stěn s výškou, v pražském OSM je jich ~37 km.
```
