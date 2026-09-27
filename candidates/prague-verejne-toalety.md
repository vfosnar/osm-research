# Veřejné toalety (Praha)

| Field | Value |
|---|---|
| publisher | IPR Praha (source provider id 43 = HMP-IPR) |
| url | https://mp.iprpraha.cz/arcgis/rest/services/Hosted/FSV_CUR_FSV_VEREJNAWC_B/FeatureServer/0 (`/query?where=1%3D1&outFields=*&outSR=4326&f=geojson`); catalogue https://opendata.geoportalpraha.cz/datasets/iprpraha::veřejné-toalety |
| format | ArcGIS FeatureServer (JSON/GeoJSON), Hub downloads |
| coords | yes |
| records | 458 (2026-09-27) |
| osm_tags | amenity=toilets; wheelchair=yes\|no (from `vozickari`); access=customers for shopping-centre / fast-food toilets; centralkey=eurokey for "neveřejné toalety, Euroklíč" |
| osm_count_cz | amenity=toilets 3,315 CZ (taginfo 2026-09-27); 418 in Prague (Postpass, relation 435514) |
| license | CC BY 4.0 + IPR consent for all open data in OSM (2018) |
| license_url | https://geoportalpraha.cz/data-a-sluzby/otevrena-data ; https://lists.openstreetmap.org/pipermail/talk-cz/2018-February/018526.html |
| license_status | ok |
| update_freq | irregular (dct:modified 2025-08-26) |
| impact | 3 |
| verified | yes |

## Try it

- **Map preview:** [samples/prague-verejne-toalety.geojson](../samples/prague-verejne-toalety.geojson): all 458 toilets, pre-tagged `amenity=toilets` + `wheelchair` from `vozickari`.
- **QGIS:** *Layer → Add Layer → Add Vector Layer… → Source type: Protocol: HTTP(S)*, URI `https://mp.iprpraha.cz/arcgis/rest/services/Hosted/FSV_CUR_FSV_VEREJNAWC_B/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=geojson` (whole layer, WGS84).

## Notes

**Fields.**
- `lokalita`: a descriptive name (one read: "HLAVNÍ NÁDRAŽÍ (ČD) - WC  I").
- `adresa`, `globalid`.
- `vozickari`: wheelchair access (1 ano, 0/2 ne, 99 neurčeno).
- `typ`:
  - 1 = DPP / transport hub, 93 records
  - 2 = WC kiosk, 134 records
  - 3 = inside a business or office, 231 records
- `umisteni_podrob`, the detailed location:
  - metro A/B/C: 16/25/20
  - railway station or other public transport: 23
  - shopping centre: 63
  - McDonald's / KFC / Burger King: 21/11/5
  - column with integrated WC: 9
  - public WC: 4
  - Euroklíč: 23
  - playground: 12
  - closable grounds: 12
  - paid-entry areas: 4
  - unset: 184

**OSM gap.** 197 of 458 (43%) have no OSM `amenity=toilets` (or `toilets=*` on another feature)
within 50 m (Postpass, 2026-09-27). Many of the unmatched are indoor toilets in shopping
centres and fast-food restaurants. For those, OSM prefers `toilets=yes` on the host POI, or a
node inside the building with `access=customers`. The metro, kiosk and Euroklíč subsets are
directly useful for OSM, and wheelchair information is valuable.

**Caveats.** There are no opening hours or fee information. `lokalita` is not a proper name, so
don't put it in `name`; `description` is fine. Wiki read: Tag:amenity=toilets and
Cs:Tag:amenity=toilets (wheelchair, access, fee); Key:centralkey (value eurokey used 25x in CZ per taginfo).

## Wiki entry
```
===Veřejné toalety (Praha)===
* dataset: Veřejné toalety
* gestor: [https://geoportalpraha.cz IPR Praha]
* licence: CC BY 4.0 + souhlas IPR s využitím všech opendat pro OSM (2018) [https://lists.openstreetmap.org/pipermail/talk-cz/2018-February/018526.html]
* datové primitivy: body
* odkaz: https://mp.iprpraha.cz/arcgis/rest/services/Hosted/FSV_CUR_FSV_VEREJNAWC_B/FeatureServer/0
* navržený tag {{tag|amenity|toilets}}, {{tag|wheelchair|yes/no}}
* poznámka: 458 toalet s údajem o bezbariérovosti, 197 z nich nemá v OSM do 50 m protějšek.
```
