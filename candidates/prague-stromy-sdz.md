# Sdílená data o zeleni – vegetační prvky – body (stromy, keře)

| Field | Value |
|---|---|
| publisher | IPR Praha (data from MHMP-OCP, TSK hl. m. Prahy, MHMP-HOM and 13 městské části) |
| url | https://mp.iprpraha.cz/arcgis/rest/services/Hosted/OPK_CUR_OPK_SMZ_VP_B/FeatureServer/0 (tested query `/query?where=kod_vp%3D71&outFields=*&outSR=4326&f=geojson`, paged by 2000); catalogue page https://opendata.geoportalpraha.cz/datasets/iprpraha::sdílená-data-o-zeleni-vegetační-prvky-body-1 |
| format | ArcGIS FeatureServer (GeoJSON/JSON via REST, also SHP/CSV/GeoJSON download from ArcGIS Hub) |
| coords | yes (multipoint, one point each) |
| records | 201,702 points, of which 171,276 are kod_vp=71 "Strom" (trees), 30,170 kod_vp=51 "Keř" (shrubs), 181 container greenery, 75 climbers (fetched 2026-09-27) |
| osm_tags | natural=tree; leaf_type=broadleaved\|needleleaved from kod_drevin (1 Jehličnatý → needleleaved, 2 Listnatý → broadleaved, 3 Ovocný → broadleaved); optional ref:ipr=&lt;globalid&gt; |
| osm_count_cz | natural=tree 136,307 in CZ (taginfo Geofabrik, 2026-09-27); 18,576 in Prague (Postpass, within relation 435514, 2026-09-27) |
| license | CC BY 4.0 ("datový podklad © IPR Praha") + explicit IPR consent for use of all IPR open data in OSM (e-mail from Mgr. Bohdan Baron, 2018-01-29) |
| license_url | https://geoportalpraha.cz/data-a-sluzby/otevrena-data ; consent: https://lists.openstreetmap.org/pipermail/talk-cz/2018-February/018526.html (listed on wiki Contributors page) |
| license_status | ok |
| update_freq | continuous (dct:modified 2026-09-25; per-record `aktualizace` dates from 2025-02 to 2026-08) |
| impact | 5 |
| verified | yes |

## Try it

- **Map preview:** [samples/prague-stromy-sdz.geojson](../samples/prague-stromy-sdz.geojson): the 1,909 trees (`kod_vp=71`) in part of Vinohrady (bbox 14.436,50.070–14.446,50.076; 1,062 managed by MČ Praha 2 and 847 by TSK), pre-tagged `natural=tree` + `leaf_type`.
- **QGIS:** *Layer → Add Layer → Add ArcGIS REST Server Layer… → New*, URL `https://mp.iprpraha.cz/arcgis/rest/services/Hosted/OPK_CUR_OPK_SMZ_VP_B/FeatureServer` → *Connect* → add layer 0 (QGIS reprojects and pages the requests itself). Filter `kod_vp = 71` for trees only.

## Notes

**What it is.** The city's shared greenery passport ("Sdílená data o zeleni", layer
`OPK_SMZ_VP_b`) that the city, TSK and several districts maintain in one database. Every tree
and shrub they look after is a point. Fields: `kod_sprav` (správce, the owner), `kod_udrz`
(udržovatel, the maintainer), `kod_vp` (vegetation element type), `kod_drevin` (tree category),
`kod_tvar`, `kod_zapoj`, `kod_sk_vp`, `id_strom` (ID in a street tree row, only for some trees),
`aktualizace` (last update) and `globalid`.
**There is no species or genus field**, so the only attributes it can add are position and leaf_type.

**Coverage by správce (all vegetation points):** TSK 55,787; MČ Praha 4 29,551; MHMP-OCP 25,602;
Praha 14 19,756; Praha 12 12,953; MHMP-HOM 12,606; Praha 2 9,654; Praha 15 9,502; Praha 9 7,248;
Praha 3 6,241; Praha 5 5,087; Zličín 2,810; Kunratice 2,548; Dolní Měcholupy 1,232;
Dolní Chabry 682; Řeporyje 443. Praha 1, 6, 7, 8, 10, 11, 13 and others have no data yet,
so coverage is partial but growing.

**OSM gap.** I took a systematic sample (every 40th objectid) of 4,281 trees and checked it with Postpass.
Only 89 (2.1%) had an OSM `natural=tree` within 3 m, and 138 (3.2%) had one within 8 m.
About 10% fall inside OSM `natural=wood`, `landuse=forest` or `natural=tree_row` (within 5 m).
So roughly 160,000 of the trees are missing from OSM. This is by far the largest Prague gap found.

**Caveats.**
- Many trees stand in parks that OSM maps as woods or tree_rows. The community has to decide
  whether single trees are wanted there. A reasonable first step is street trees (TSK, 55k) and
  trees in park lawns outside `natural=wood`.
- There is no species field. This is a much thinner dataset than, for example, Vienna's
  Baumkataster.
- I did not verify whether `globalid` stays stable across updates, and IPR does not guarantee
  it. `objectid` is not stable. If a ref is wanted, use `ref:ipr=<globalid>`, as Sync
  already does with `ref:ipr` for Prague containers and parking machines. At 171k points, this may
  be too heavy to store as a tag.
- Licence: the 2018 IPR consent covers "všech našich opendat". Some of this data comes from TSK
  and districts but is published by IPR as IPR open data. It is worth confirming with IPR
  (opendata contact: Mgr. Karolina Lejsková, lejskova@ipr.praha.eu) that the consent still
  applies after the move to CC BY 4.0. The 2019 IPR power-station import relied on the same
  consent (wiki: IPRPraha Powerstations Import).
- Wiki pages read: Tag:natural=tree and Cs:Tag:natural=tree (leaf_type, genus, species,
  denotation) and Key:leaf_type.

**Suggested workflow.** A Sync dataset (`ref:ipr`, `create_keys=["natural","leaf_type"]`)
with a manual review queue, starting with TSK street trees.

## Wiki entry
```
===Stromy – Sdílená data o zeleni (Praha)===
* dataset: Sdílená data o zeleni – vegetační prvky – body
* gestor: [https://geoportalpraha.cz IPR Praha] (data MHMP, TSK, MČ)
* licence: CC BY 4.0 + souhlas IPR s využitím všech opendat pro OSM (2018) [https://lists.openstreetmap.org/pipermail/talk-cz/2018-February/018526.html]
* datové primitivy: body
* odkaz: https://mp.iprpraha.cz/arcgis/rest/services/Hosted/OPK_CUR_OPK_SMZ_VP_B/FeatureServer/0
* navržený tag {{tag|natural|tree}}, {{tag|leaf_type|broadleaved/needleleaved}}, {{tag|ref:ipr|<globalid>}}
* poznámka: 171 tis. stromů (TSK, MHMP, 13 MČ), v OSM je v Praze jen ~18,6 tis. stromů a vzorek ukazuje, že ~97 % stromů z datasetu v OSM chybí; bez druhu dřeviny.
```
