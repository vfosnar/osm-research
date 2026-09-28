# VÚV TGM / MŽP – Oblasti povrchových vod využívaných ke koupání (official EU bathing waters monitored by KHS)

| Field | Value |
|---|---|
| publisher | Výzkumný ústav vodohospodářský T. G. Masaryka, v.v.i. (for MŽP), IČO 00020711 |
| url | https://heis.vuv.cz/data/webmap/datovesady/isvs/KoupaciOblast/E_ISVS$KOUP_OBL.zip (NKOD: https://data.gov.cz/zdroj/datové-sady/00020711/25ebefbd7d10ebd202cec12d7308de7c); WFS https://ags2.vuv.cz/arcgis/services/isvs_voda/isvs_voda/MapServer/WFSServer |
| format | SHP (multipoint, S-JTSK EPSG:5514, UTF-8 .cpg) |
| coords | yes |
| records | 152 bathing sites (DTMDS_REF 30052025, i.e. the 2025 season list) |
| osm_tags | leisure=bathing_place (node; name=&lt;NAZ_KOBL&gt;), or leisure=swimming_area where roped/buoyed; ref:CZ:koupaci=&lt;KOBL_ID&gt; (KO104001 = koupaliště Šeberák; new key); website=&lt;RZH_URL&gt; (MZe water profile) |
| osm_count_cz | leisure=bathing_place 30; leisure=swimming_area not counted (Geofabrik taginfo 2026-09-27) |
| license | CC BY 4.0 (NKOD terms: copyrighted work + database, authors VÚV TGM and MŽP) |
| license_url | https://creativecommons.org/licenses/by/4.0/ |
| license_status | needs_waiver |
| update_freq | yearly (list set per bathing season; NKOD "OTHER") |
| impact | 2 |
| sync_fit | Sync (points, stable ref:CZ:koupaci proposed, category → bathing_place 1:1) |
| verified | yes |

## Try it
- **Map preview:** [samples/vuv-koupaci-vody.geojson](../samples/vuv-koupaci-vody.geojson): all 152 bathing sites of the 2025 list, with KOBL_ID, name and the MZe profile link.
- **QGIS:** *Layer → Add Layer → Add WFS / OGC API Features Layer → New*, URL `https://ags2.vuv.cz/arcgis/services/isvs_voda/isvs_voda/MapServer/WFSServer`, layer *KoupaciOblasti* (152 features, EPSG:5514). Alternatively, use *Add Vector Layer*, source type *File*, with `/vsizip/vsicurl/https://heis.vuv.cz/data/webmap/datovesady/isvs/KoupaciOblast/E_ISVS$KOUP_OBL.zip/E_ISVS$KOUP_OBL$wm.shp`.

## Notes
- Fields: KOBL_ID (stable EU bathing-water ID), name ("VN Slapy - Měřín" and "koupaliště Šeberák" are in the 2025 list), municipality, stream/reservoir IDs, coordinates, and RZH_URL (link to the MZe bathing-water profile).
- Postpass check: 139 of 152 sites have something swimming-related within 300 m (swimming_pool, water_park, beach, sport=swimming, bathing_place, swimming_area). Only 1 is tagged leisure=bathing_place. The places are mostly known, so the value lies in correct tagging, the official name and ID, and a link to the water-quality profile that people check in summer.
- KHS publishes weekly water-quality results for these sites. The KOBL_ID would let a map app link to them.
- Karlovarský, Královéhradecký and Liberecký kraj publish their own "koupací místa" lists (NKOD), but these are regional subsets.
- Wiki pages read: Tag:leisure=bathing_place (a node, placed in the middle or at the entrance; bathing spot without significant facilities), Tag:leisure=swimming_area (areas marked by rope or buoys). Sites that are managed "koupaliště" with facilities may keep their existing tags, with the ID added.

## Wiki entry
```
===Koupací vody (VÚV TGM)===
* dataset: Oblasti povrchových vod využívaných ke koupání
* gestor: [https://www.vuv.cz/ Výzkumný ústav vodohospodářský T. G. Masaryka]
* licence: CC BY 4.0 [https://creativecommons.org/licenses/by/4.0/] – nutný souhlas
* datové primitivy: body
* odkaz: https://heis.vuv.cz/data/webmap/datovesady/isvs/KoupaciOblast/E_ISVS$KOUP_OBL.zip
* navržený tag {{tag|leisure|bathing_place}}, {{tag|ref:CZ:koupaci|<KOBL_ID>}}
* poznámka: 152 oficiálních koupacích míst; místa v OSM většinou jsou, ale jen 1 má {{tag|leisure|bathing_place}} a žádné nemá ID pro napojení na kvalitu vody
```
