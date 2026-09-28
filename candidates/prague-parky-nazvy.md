# Parky (ÚAP) – named park polygons of Prague

| Field | Value |
|---|---|
| publisher | IPR Praha |
| url | https://mp.iprpraha.cz/arcgis/rest/services/Hosted/URK_CUR_URK_PARKY_P/FeatureServer/0 ; catalogue https://opendata.geoportalpraha.cz/datasets/iprpraha::parky-úap-1 (related: MPP – Městské parky https://mp.iprpraha.cz/arcgis/rest/services/Hosted/MPP_CUR_MPP_100_PARKY_P/FeatureServer/0, 953 polygons) |
| format | ArcGIS FeatureServer (JSON/GeoJSON), Hub downloads |
| coords | yes (polygons) |
| records | 1,064 polygons, all with `nazev` (2026-09-27) |
| osm_tags | name=* on existing leisure=park / leisure=garden; leisure=park for missing parks (charakter_uap 1–3, 5, 12); access hints from `pristupnost` |
| osm_count_cz | leisure=park 6,568 CZ (taginfo 2026-09-27); Prague 830, of which only 178 have a name (Postpass, relation 435514) |
| license | CC BY 4.0 + IPR consent for all open data in OSM (2018) |
| license_url | https://geoportalpraha.cz/data-a-sluzby/otevrena-data ; https://lists.openstreetmap.org/pipermail/talk-cz/2018-February/018526.html |
| license_status | ok |
| update_freq | irregular, planning-analysis layer (dct:modified 2026-06-06) |
| impact | 3 |
| sync_fit | MapRoulette (park polygons drawn from imagery; name matching to existing parks) |
| verified | yes |

## Try it

- **Map preview:** [samples/prague-parky-nazvy.geojson](../samples/prague-parky-nazvy.geojson): the 143 named park polygons in central Prague (bbox 14.40,50.06–14.47,50.10), with coded fields decoded.
- **QGIS:** *Layer → Add Layer → Add ArcGIS REST Server Layer… → New*, URL `https://mp.iprpraha.cz/arcgis/rest/services/Hosted/URK_CUR_URK_PARKY_P/FeatureServer` → *Connect* → add layer 0 (QGIS reprojects and pages the requests itself).

## Notes

**Fields.**
- `id` (park id), `nazev`, `globalid`.
- `hierarchie`: 1 metropolitní 71, 2 čtvrťový 64, 3 lokalitní 171, 4 místní 658,
  5 na náměstí 100.
- `charakter_uap`:
  - park 588
  - park ve volné zástavbě 86
  - park na náměstí 100
  - hřbitov 64
  - lesopark 110
  - sad/vinice 17
  - okrasná zahrada 32
  - hřiště 22
  - kompoziční pás 27
  - lesnatá území 12
  - vnitroblok 5
  - parkový areál 1
- `pristupnost`: přístupný 912, v režimu 133, nepřístupný 19.
- `hodnoceni_uap2020`: funkční / k obnově / k založení.

**OSM gap (Postpass, polygon centroid in OSM polygon, 2026-09-27).** Of the 588 features with
character "park", only 200 have a centroid inside an OSM `leisure=park|garden`, and only 83
are inside a *named* one. For "park na náměstí" the figures are 45 and 6 of 100; for
"lesopark", 10 and 6 of 110. Most Prague parks in OSM are unnamed or mapped only as
`landuse=grass`, so names are the main value.

**Caveats.**
- These are planning (ÚAP) polygons, not surveyed park boundaries. Use them for names and
  existence, not geometry. Some names are descriptive ("Vnitroblok Radhošťská", "Park Belvedér").
  Check names against the RÚIAN / Pražský místopis, or against official names where they exist.
- Leave out rows with `hodnoceni_uap2020` = 3 ("k založení", not yet built) and cemeteries.
- Wiki read: Tag:leisure=park and Cs:Tag:leisure=park.

## Wiki entry
```
===Parky Prahy (ÚAP)===
* dataset: Parky (ÚAP)
* gestor: [https://geoportalpraha.cz IPR Praha]
* licence: CC BY 4.0 + souhlas IPR s využitím všech opendat pro OSM (2018) [https://lists.openstreetmap.org/pipermail/talk-cz/2018-February/018526.html]
* datové primitivy: plochy
* odkaz: https://mp.iprpraha.cz/arcgis/rest/services/Hosted/URK_CUR_URK_PARKY_P/FeatureServer/0
* navržený tag {{tag|leisure|park}}, {{tag|name|<nazev>}}
* poznámka: 1064 pojmenovaných parků; z 830 parků v pražském OSM má jméno jen 178.
```
