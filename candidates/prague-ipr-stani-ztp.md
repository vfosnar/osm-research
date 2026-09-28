# Praha – vyhrazená parkovací stání pro držitele průkazu ZTP/P (IPR Praha)

| Field | Value |
|---|---|
| publisher | Institut plánování a rozvoje hl. m. Prahy (IPR Praha), IČO 70883858; data from TSK (all records `id_poskyt` = 38) |
| url | https://lkod-iprpraha.hub.arcgis.com/api/download/v1/items/ab4a8cd8fc284b738ca806681559d694/geojson?layers=0 (ZTP/P spaces, points); ArcGIS: https://gp-dc.iprpraha.cz/arcgis/rest/services/app_dop/mapapristupnosti/FeatureServer/0 (same layer with coded-value domains, layer 1 = 16 "Vybrané bezbariérové trasy"); related: https://mp.iprpraha.cz/arcgis/rest/services/Hosted/DOP_CUR_DOP_ZPS_ZTP_SDR_P/FeatureServer/0 ("Vyhrazená stání pro invalidy – sdružená", polygons in the paid-parking zones) and https://lkod-iprpraha.hub.arcgis.com/api/download/v1/items/1e6b9ad51a12468193f47e2b9b1b94ed/csv?layers=0 ("Vyhrazené stání pro invalidy s registrační značkou") |
| format | GeoJSON (CRS84), CSV, SHP, FileGDB; ArcGIS FeatureServer |
| coords | yes (points; ZPS layers are polygons of the marked space) |
| records | 2,192 points = 3,264 spaces (`pocet_ps`), with length/width, layout (`typ_ps`: 1,194 kolmé, 670 podélné, 294 šikmé, 34 partly on the pavement), surface type and material, slope, whether the space sits in a dog zone. ZPS "sdružená" layer: 1,456 polygons (`pocinvst` = number of spaces). ZPS spaces tied to a licence plate: 2,085 rows |
| osm_tags | amenity=parking_space + parking_space=disabled (wiki Tag:parking_space=disabled: area inside an amenity=parking, status de facto); capacity=&lt;pocet_ps&gt;; on street-side parking alternatively capacity:disabled on the parent amenity=parking (wiki Key:capacity) |
| osm_count_cz | parking_space=disabled 4,940; amenity=parking_space 46,464; capacity:disabled 10,558 (taginfo 2026-09-28). Local match against the 2026-09-27 Czechia extract (Postpass 503): Prague bbox has 3,840 objects with parking_space=disabled / capacity:disabled / access:disabled=designated; **954 of 2,192 ZTP/P points (44 %) have none within 30 m**; in the centre (bbox 14.41,50.07,14.45,50.11) **265 of 293 (90 %)** have none |
| license | CC BY 4.0 (NKOD terms of use: author IPR Praha) + explicit IPR consent for use of all IPR open data in OSM (e-mail from Mgr. Bohdan Baron, 2018-01-29) |
| license_url | https://creativecommons.org/licenses/by/4.0/ ; consent: https://lists.openstreetmap.org/pipermail/talk-cz/2018-February/018526.html |
| license_status | ok |
| update_freq | ZTP/P layer "other" (irregular); the two ZPS layers weekly (NKOD accrualPeriodicity) |
| impact | 4 |
| sync_fit | MapRoulette (no stable id; one point aggregates several spaces, ZPS polygons need imagery) |
| verified | yes |

## Try it
- **Map preview:** [samples/prague-ipr-stani-ztp.geojson](../samples/prague-ipr-stani-ztp.geojson): 424 ZTP/P parking points in central Prague (bbox 14.40,50.06,14.46,50.10). Red = no OSM disabled parking object within 30 m (383), green = one exists (41).
- **QGIS:** *Layer → Add Layer → Add Vector Layer*, source type *Protocol: HTTP(S)*, type *GeoJSON*, URI `https://lkod-iprpraha.hub.arcgis.com/api/download/v1/items/ab4a8cd8fc284b738ca806681559d694/geojson?layers=0` (tested 2026-09-28: FeatureCollection, 2,192 points, 0.9 MB). For readable attribute values (domains) use *Add ArcGIS REST Server Layer*, URL `https://gp-dc.iprpraha.cz/arcgis/rest/services/app_dop/mapapristupnosti/FeatureServer`, layer 0 "Vyhrazená stání ZTP".
- **Web:** IPR accessibility app https://app.iprpraha.cz/apl/app/bezbariery/

## Notes
- **Not known:** no mention of ZTP, "vyhrazená stání" or disabled parking on Cs:Česko/freemap (incl. Potencionální zdroje), Cs:Zdroje_v_jednani or in Sync `config.toml` (checked 2026-09-28). The Cs:Import Mapy bez bariér import covers monuments/museums/churches (POV's mapybezbarier.cz), not parking. No OSM parking_space=disabled object in the Prague bbox has a `ref` or `source` pointing at TSK/IPR (1,919 of 1,920 have no source tag).
- **Gap:** see osm_count_cz. Outside the centre about 60 % of the spaces already have an OSM disabled-parking object nearby, but in the historic centre and the paid zones almost nothing is mapped. The ZPS "sdružená" layer (disabled spaces inside the paid-parking zones) matches OSM for only 181 of 1,456 polygon centroids within 30 m.
- **Overlap with VozejkMap:** VozejkMap's Prague disabled-parking points (candidate `vozejkmap.md`, licence unclear) most likely derive from the same TSK register. This is the official, openly licensed version, so it is the better import source for Prague.
- **Tagging:** point → amenity=parking_space + parking_space=disabled + capacity=pocet_ps. The wiki prefers an area inside amenity=parking; the ZPS layers already are polygons of the marked space and can be imported as areas. The "s registrační značkou" spaces are reserved for one named vehicle; tag access=private (or leave them out).
- **IDs:** `globalid` (GUID) is stable in the ArcGIS layer; suggested `ref:tsk:ztp=<globalid>` only if the community wants Sync; otherwise one-shot import plus periodic diff.
- **Extra accessibility fields** (surface of the space and of the adjacent pavement, kerb height `VYS_HRAN`, tactile elements `HMAT_PRV`, slope) exist in the FeatureServer but are mostly "Nezadáno"; not worth importing.
- **Licence:** CC BY 4.0, covered by the 2018 IPR consent for "všech našich opendat" (same basis as `prague-stromy-sdz.md`). The data originate at TSK hl. m. Prahy and are published by IPR as IPR open data; worth confirming with IPR that the consent covers TSK-originated layers.
- Wiki pages read: Tag:parking_space=disabled, Key:wheelchair.

## Wiki entry
```
===Praha – vyhrazená parkovací stání ZTP/P===
* dataset: Vyhrazená parkovací stání pro držitele průkazu ZTP/P bez vazby na registrační značku vozidla; Vyhrazená stání pro invalidy – sdružená (ZPS)
* gestor: [https://iprpraha.cz/ Institut plánování a rozvoje hl. m. Prahy] (data TSK)
* licence: CC BY 4.0 [https://creativecommons.org/licenses/by/4.0/]
* datové primitivy: body, plochy
* odkaz: https://lkod-iprpraha.hub.arcgis.com/api/download/v1/items/ab4a8cd8fc284b738ca806681559d694/geojson?layers=0
* navržený tag {{tag|amenity|parking_space}} + {{tag|parking_space|disabled}} + {{tag|capacity|<počet stání>}}
* poznámka: 2 192 míst (3 264 stání); u 954 z nich (v centru u 265 z 293) není v OSM do 30 m žádné vyhrazené stání; kryto souhlasem IPR z roku 2018
```
