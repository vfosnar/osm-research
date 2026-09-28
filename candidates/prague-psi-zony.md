# Volný pohyb psů – psí zóny (Praha)

| Field | Value |
|---|---|
| publisher | IPR Praha (provider MHMP-INF / districts) |
| url | https://mp.iprpraha.cz/arcgis/rest/services/Hosted/AGD_CUR_AGD_POHYBPSU_P/FeatureServer/0 ; catalogue https://opendata.geoportalpraha.cz/datasets/iprpraha::volný-pohyb-psů-psí-zóny |
| format | ArcGIS FeatureServer (JSON/GeoJSON), Hub downloads |
| coords | yes (polygons) |
| records | 2,066 polygons: typ 1 "Volný pohyb psů" 318, typ 2 "Prosíme, nevstupujte se psy" 3, typ 4 "Psi jen na vodítku" 1,426, typ 3 "Zákaz vstupu psů" 319; the domain value typ 5 "Psí hřiště" has 0 records (2026-09-27) |
| osm_tags | leisure=dog_park (typ 1 only where signed or designated on the ground; typ 5 "Psí hřiště" would fit but is empty); dog=leashed (typ 4) / dog=no (typ 3) on the park or area; name from `nazev` |
| osm_count_cz | leisure=dog_park 422 CZ / 82 Prague (taginfo Geofabrik and Postpass relation 435514, 2026-09-27) |
| license | CC BY 4.0 + IPR consent for all open data in OSM (2018) |
| license_url | https://geoportalpraha.cz/data-a-sluzby/otevrena-data ; https://lists.openstreetmap.org/pipermail/talk-cz/2018-February/018526.html |
| license_status | ok |
| update_freq | irregular (dct:modified 2025-10-29) |
| impact | 3 |
| sync_fit | MapRoulette (dog-zone polygons; draw from imagery) |
| verified | yes |

## Try it

- **Map preview:** [samples/prague-psi-zony.geojson](../samples/prague-psi-zony.geojson): all 318 free-run areas (`typ` 1, "Volný pohyb psů") in Prague. The leash and ban zones are left out.
- **QGIS:** *Layer → Add Layer → Add ArcGIS REST Server Layer… → New*, URL `https://mp.iprpraha.cz/arcgis/rest/services/Hosted/AGD_CUR_AGD_POHYBPSU_P/FeatureServer` → *Connect* → add layer 0 (QGIS reprojects and pages the requests itself). For a one-off full download: *Layer → Add Layer → Add Vector Layer… → Source type: Protocol: HTTP(S)*, URI `https://mp.iprpraha.cz/arcgis/rest/services/Hosted/AGD_CUR_AGD_POHYBPSU_P/FeatureServer/0/query?where=typ%3D1&outFields=*&outSR=4326&f=geojson`.

## Notes

**Fields.**
- `nazev` ("psí louka Folimanka" and "Lumírovy sady" among the values read).
- `typ`: see records above.
- `stav`: Zákaz dle vyhlášky MHMP / Návrh MČ / Schváleno MČ / Jiný správce / Správce MHMP.
- `duvod`: reason for a ban (children's playground, flower bed, meadow).
- `mc`, `globalid`.

These are legally designated areas under Prague's dog ordinance (vyhláška).

**OSM gap.** 308 of 318 free-run areas have no OSM `leisure=dog_park` (or `dog=unleashed|yes|designated`)
within 80 m of their centroid (Postpass, 2026-09-27). Leash and ban zones are practically
absent in OSM.

**Caveats.**
- The wiki (Tag:leisure=dog_park) defines a dog park as a "designated area, with or without a
  fenced boundary, where dog-owners are permitted to exercise their pets unrestrained".
  Legally designated free-run meadows fit that, but many are unmarked parts of larger parks.
  The community should decide whether an unfenced ordinance zone becomes `leisure=dog_park`
  or `dog=unleashed` on the containing area.
- Key:dog values (yes/no/leashed/unleashed) read on the wiki. Rows with stav=2 ("Návrh MČ",
  proposals) must be skipped.

## Wiki entry
```
===Psí zóny Prahy===
* dataset: Volný pohyb psů – psí zóny
* gestor: [https://geoportalpraha.cz IPR Praha] / MHMP
* licence: CC BY 4.0 + souhlas IPR s využitím všech opendat pro OSM (2018) [https://lists.openstreetmap.org/pipermail/talk-cz/2018-February/018526.html]
* datové primitivy: plochy
* odkaz: https://mp.iprpraha.cz/arcgis/rest/services/Hosted/AGD_CUR_AGD_POHYBPSU_P/FeatureServer/0
* navržený tag {{tag|leisure|dog_park}}, {{tag|dog|leashed}}, {{tag|dog|no}}
* poznámka: 318 ploch pro volný pohyb psů, v OSM má protějšek jen 10; zóny „jen na vodítku“ (1426) a zákazy (319) v OSM chybí.
```
