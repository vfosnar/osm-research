# Prague cycle routes and cycling infrastructure (Cyklistické trasy, DOP_CUR_DOP_CYKLOTRASY_L)

| Field | Value |
|---|---|
| publisher | Institut plánování a rozvoje hl. m. Prahy (IPR Praha), IČO 70883858 (source attribute poskyt = HMP-IPR) |
| url | https://mp.iprpraha.cz/arcgis/rest/services/Hosted/DOP_CUR_DOP_CYKLOTRASY_L/FeatureServer/0 ; catalogue https://geoportalpraha.cz/en/data-and-services/45063acce89d4b37afc6d51f03f3ad49 |
| format | ArcGIS FeatureServer (GeoJSON/JSON query), lines |
| coords | yes |
| records | 6,328 segments (2,205 realizace=1 existing, 4,123 realizace=0 proposed); 295 distinct route numbers |
| osm_tags | route=bicycle relations (network=lcn/rcn/ncn, ref=*); cycleway:right\|left\|both=lane / share_busway; oneway:bicycle=no; highway=cycleway; highway=path\|footway + bicycle=designated |
| osm_count_cz | Prague bbox (14.22,49.94,14.71,50.18, Postpass 2026-09-27): 466 route=bicycle relations, 331 distinct refs; cycle lanes 193 km; oneway:bicycle=no 105 km; share_busway 40 km; cycleway/designated paths 582 km |
| license | CC BY 4.0 + IPR consent for all open data in OSM (2018) |
| license_url | https://creativecommons.org/licenses/by/4.0/ ; https://lists.openstreetmap.org/pipermail/talk-cz/2018-February/018526.html |
| license_status | ok |
| update_freq | continuous (item modified 2026-08) |
| impact | 2 |
| sync_fit | MapRoulette (bicycle route lines and relations; draw from imagery) |
| verified | yes |

## Try it

- **Map preview:** [samples/prague-ipr-cyklotrasy.geojson](../samples/prague-ipr-cyklotrasy.geojson): the 364 built segments (`realizace=1`) in the inner city (bbox 14.38,50.05–14.48,50.11), with route number and `dopr_stav` decoded.
- **QGIS:** *Layer → Add Layer → Add ArcGIS REST Server Layer… → New*, URL `https://mp.iprpraha.cz/arcgis/rest/services/Hosted/DOP_CUR_DOP_CYKLOTRASY_L/FeatureServer` → *Connect* → add layer 0 (QGIS reprojects and pages the requests itself). Filter `realizace = 1` to hide proposed routes.

## Notes
- **Why it is here:** Google's legal notices for Czechia credit "Geoportal Praha" and link this exact item
  (`45063acce89d4b37afc6d51f03f3ad49`). It is the source of the Google Maps cycling layer in Prague.
- **Route numbers:** 295 IPR route refs (split on commas, spaces removed); 213 of them exist as `ref` on OSM
  route=bicycle relations. Of the 82 missing, almost all are proposed routes (realizace=0). Only about 16
  signed routes are missing: A0, A251, A277, A30, A436, GW, H, H/P15, J07, K07, K08, P14, plus a few named
  trails such as "Krajem zlatokopů" and "Po stopách minulosti", which may be hiking or educational trails.
  So signed route relations are essentially complete.
- **Infrastructure attribute `dopr_stav`** (coded; km of segments):
  - cyklotrasa v běžné ulici 798; shared foot/cycle path (6) 391; bezmotorová cesta 374
  - ochranný cyklopruh 145; cykloobousměrka (contraflow) 121; cyklopruh 119; MTB 130
  - piktokoridor 71; buspruh 56; segregated path (7) 25; samostatná cyklostezka 11
- **Infrastructure gap:** OSM has 193 km of lanes against 335 km of IPR lane, ochranný-lane and
  piktokoridor segments. That comparison is rough, because IPR measures centreline and OSM measures ways,
  with side ambiguity. Contraflow is 105 vs 121 km and bus lanes 40 vs 56 km. Useful as a QA layer (MapRoulette
  or Sync review) for cycleway:* on Prague streets, not as an import. Mapping:
  - cyklopruh → cycleway:*=lane
  - ochranný cyklopruh → cycleway:*=lane + cycleway:*:lane=advisory
  - piktokoridor → cycleway:*=shared_lane
  - buspruh → cycleway:*=share_busway
  - cykloobousměrka → oneway:bicycle=no
  - 6 → highway=path + bicycle=designated + foot=designated + segregated=no
  - 7 → the same with segregated=yes
- **IDs:** only `objectid` and `globalid`; there is no stable per-route ID other than the ref.
- Wiki pages read: Tag:route=bicycle (network mandatory, ref) and Key:cycleway (use the :left/:right/:both
  side suffixes).
- **Licence:** IPR's 2018 consent covers all IPR open data (see README corrections). The layer's
  accessInformation is `CZ-70883858-DOP_CUR.DOP_Cyklotrasy_l`, which is the IPR IČO.

## Wiki entry
```
===Cyklistické trasy a cyklistická infrastruktura Prahy (IPR)===
* dataset: Cyklistické trasy (DOP_CUR_DOP_CYKLOTRASY_L)
* gestor: [https://geoportalpraha.cz IPR Praha]
* licence: CC BY 4.0 + souhlas IPR s využitím všech opendat pro OSM (2018) [https://lists.openstreetmap.org/pipermail/talk-cz/2018-February/018526.html]
* datové primitivy: linie
* odkaz: https://mp.iprpraha.cz/arcgis/rest/services/Hosted/DOP_CUR_DOP_CYKLOTRASY_L/FeatureServer/0
* navržený tag {{tag|route|bicycle}} + {{tag|ref|<číslo trasy>}}, {{tag|cycleway:right|lane}}, {{tag|cycleway:right|share_busway}}, {{tag|oneway:bicycle|no}}
* poznámka: značené trasy v OSM téměř kompletní (chybí ~16); vhodné jako kontrolní vrstva pro cyklopruhy (OSM 193 km vs IPR ~335 km) a cykloobousměrky
```
