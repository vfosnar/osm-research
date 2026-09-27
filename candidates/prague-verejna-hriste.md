# Veřejná hřiště (Praha) – dětská a veřejná hřiště

| Field | Value |
|---|---|
| publisher | IPR Praha (ÚAP layer RV_VybavenostVPP_b) |
| url | https://mp.iprpraha.cz/arcgis/rest/services/Hosted/FSV_CUR_RV_VYBAVENOSTVPP_B/FeatureServer/0 ; catalogue https://opendata.geoportalpraha.cz/datasets/iprpraha::veřejná-hřiště |
| format | ArcGIS FeatureServer (JSON/GeoJSON), Hub downloads |
| coords | yes (points) |
| records | 1,772 (typ_uap 11_03 dětské hřiště 1,340; 11_02 veřejné hřiště 432); verej_pristup: přístupný 1,514, v režimu 88, nepřístupný 158, účelový 12 (2026-09-27) |
| osm_tags | leisure=playground (11_03); leisure=pitch (11_02, sport unknown); access=private / no for verej_pristup 3 |
| osm_count_cz | leisure=playground 15,549 CZ / 1,698 Prague; leisure=pitch 2,672 Prague (taginfo Geofabrik and Postpass relation 435514, 2026-09-27) |
| license | CC BY 4.0 + IPR consent for all open data in OSM (2018) |
| license_url | https://geoportalpraha.cz/data-a-sluzby/otevrena-data ; https://lists.openstreetmap.org/pipermail/talk-cz/2018-February/018526.html |
| license_status | ok |
| update_freq | irregular (dct:modified 2026-07-30) |
| impact | 2 |
| verified | yes |

## Try it

- **Map preview:** [samples/prague-verejna-hriste.geojson](../samples/prague-verejna-hriste.geojson): all 1,772 points, pre-tagged `leisure=playground` (1,340) or `leisure=pitch` (432).
- **QGIS:** *Layer → Add Layer → Add ArcGIS REST Server Layer… → New*, URL `https://mp.iprpraha.cz/arcgis/rest/services/Hosted/FSV_CUR_RV_VYBAVENOSTVPP_B/FeatureServer` → *Connect* → add layer 0 (QGIS reprojects and pages the requests itself).

## Notes

**Fields.** `typ_uap`, `verej_pristup`, `kod` (land-use class of the surrounding area:
RPU parkově upravené plochy 1,095, RPP 271, RAP 118, …), `poskyt`, `globalid`.
There are **no names, no equipment and no age groups**.

**OSM gap (Postpass, 2026-09-27).**
- 231 of 1,340 children's playgrounds have no OSM `leisure=playground` within 60 m.
- 34 of 432 public pitches have no OSM `leisure=pitch|sports_centre|playground|fitness_station`
  within 60 m.

OSM coverage in Prague is already about 83%, so the value is a QA and "missing playground" list
rather than an import.

**Caveats.**
- These are points, so they give no geometry.
- District datasets with names and equipment exist in the Prague LKOD (titles seen: "Dětská hřiště a
  sportoviště na MČ Praha 12", "Seznam dětských hřišť na území MČ Praha 11 - 3/2026",
  "Sportoviště v MČ Praze 8" at https://lkod.cz/catalog/praha/datasets). I did not evaluate
  their licences.
- Golemio `/v2/playgrounds` needs an API key, and I could not verify it.
- Wiki read: Tag:leisure=playground and Cs:Tag:leisure=playground, Tag:leisure=pitch.

## Wiki entry
```
===Veřejná hřiště (Praha)===
* dataset: Veřejná hřiště
* gestor: [https://geoportalpraha.cz IPR Praha]
* licence: CC BY 4.0 + souhlas IPR s využitím všech opendat pro OSM (2018) [https://lists.openstreetmap.org/pipermail/talk-cz/2018-February/018526.html]
* datové primitivy: body
* odkaz: https://mp.iprpraha.cz/arcgis/rest/services/Hosted/FSV_CUR_RV_VYBAVENOSTVPP_B/FeatureServer/0
* navržený tag {{tag|leisure|playground}}, {{tag|leisure|pitch}}
* poznámka: 1340 dětských hřišť, 231 z nich nemá v OSM do 60 m protějšek; vhodné spíš jako kontrolní seznam.
```
