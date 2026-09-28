# Wikidata – niche object classes for QID linking in Sync (stolpersteine, barrows, hillforts, abandoned villages, bunkers, waterfalls…)

| Field | Value |
|---|---|
| publisher | Wikidata community (Wikimedia Foundation) |
| url | SPARQL: https://query.wikidata.org/sparql (WDQS; rate-limited to 1 req/min on 2026-09-27 during an outage) or the QLever mirror https://qlever.dev/api/wikidata (data as of 2026-09-24, used for this analysis) |
| format | SPARQL → JSON / CSV (coordinates as WKT `POINT(lon lat)`) |
| coords | yes (P625), but provenance is mixed (see Notes); use only as a hint |
| records | items with P17=Q213 and P625, per class (P31/P279*): Stolperstein Q26703203 1,433; abandoned village Q350895 1,994; abandoned hamlet Q27654220 1,049; fingerpost Q16980762 1,969; bunker Q91122 680; observation tower Q1440300 450; spring Q124714 443; Jewish cemetery Q846659 425; waterfall Q34038 420; hillfort Q744099 388; barrow burial ground Q46329023 333; synagogue Q34627 299; gazebo Q961082 258; cave Q35509 207 |
| osm_tags | `wikidata=Q…` on the existing OSM object (Key:wikidata). Classes map to memorial=stolperstein, abandoned:place=village\|hamlet, information=guidepost, military=bunker, tower:type=observation, natural=spring, landuse=cemetery + religion=jewish, waterway=waterfall, historic=archaeological_site + archaeological_site=fortification\|tumulus, building=synagogue, natural=cave_entrance |
| osm_count_cz | taginfo CZ 2026-09-27: key wikidata 156,701 objects / 134,882 distinct QIDs; memorial=stolperstein 2,128; military=bunker 6,595; waterway=waterfall 444; tower:type=observation 697; abandoned:place=village 155, =hamlet 73; archaeological_site=fortification 102, =tumulus 19; building=synagogue 45; natural=cave_entrance 870; information=guidepost 27,839 |
| license | CC0 1.0 (Wikidata structured data) |
| license_url | https://creativecommons.org/publicdomain/zero/1.0/ |
| license_status | ok for QIDs only; coordinates and other values are NOT importable (see Notes) |
| update_freq | continuous |
| impact | 2 |
| verified | yes (counts, linkage, national spatial match on a local OSM extract) |

## Try it
- **Map preview:** [samples/wikidata-niche-qid.geojson](../samples/wikidata-niche-qid.geojson): 1,840 Czech Wikidata items of the five classes with the biggest OSM gap (barrows 324, hillforts 311, synagogues 220, waterfalls 359, bunkers 626) whose QID is not on any OSM object. Each point carries the coordinate reference (`coord_ref_stated_in` / `coord_ref_imported_from`, QIDs of the source) and, for the 60 sampled items, the result of the OSM check. The points are **hints for mappers**, not import geometry.
- **QGIS:** *Layer → Add Layer → Add Delimited Text Layer…*, paste as file name the URL below (barrows; replace `Q46329023` with any class QID from the table), format CSV, *Geometry definition: Well known text (WKT)*, field `coord`, CRS EPSG:4326.
  `https://qlever.dev/api/wikidata?query=PREFIX+wd%3A+%3Chttp%3A%2F%2Fwww.wikidata.org%2Fentity%2F%3E+PREFIX+wdt%3A+%3Chttp%3A%2F%2Fwww.wikidata.org%2Fprop%2Fdirect%2F%3E+SELECT+%3Fitem+%3Fcoord+WHERE+%7B+%3Fitem+wdt%3AP31%2Fwdt%3AP279%2A+wd%3AQ46329023+.+%3Fitem+wdt%3AP17+wd%3AQ213+.+%3Fitem+wdt%3AP625+%3Fcoord+.+%7D&action=csv_export`
  (tested 2026-09-27: 333 rows, header `item,coord`).

## Notes
- **Partly known.** Sync already has `[group.wikidata]` with two datasets, museums (Q33506) and castles (Q23413), in "licensed" mode: the editor writes only the locked `wikidata` QID and shows the name read-only (Sync `backend/config.toml` and `backend/src/sources/wikidata/datasets.rs`, read 2026-09-27). Drobné památky (`group.drobne_pamatky`) already covers chapels, wayside crosses, statues and small memorials. This file proposes **more classes for the same mechanism**, chosen for niche features that map users look for and OSM rarely links. Hillforts overlap castles only partly: 44 of 388 hillforts are also castle subclasses.
- **Why QIDs only (LWG position).** The OSMF Licence Compatibility page says CC0 "only extends to material the licensor actually has rights in … the licences of all the data that is included in the dataset need to be determined" (https://osmfoundation.org/wiki/Licence/Licence_Compatibility#CC0). The OSM wiki (Wikidata, "Importing data from Wikidata into OSM"; Import/ODbL Compatibility) says imports from Wikidata are generally not permitted because coordinates are often copied from Wikipedia and Google Maps, and that "this does not apply to simply importing Wikidata QIDs". Key:wikidata requires reviewing every edited object, otherwise the Automated Edits code of conduct applies.
- **Coordinate provenance, measured.** For each item, references on P625 were read (P248 "stated in", P143 "imported from Wikimedia project"). Stated sources include **Mapy.com (Q12035233)**, which is proprietary: 86 of 206 caves, 71 of 441 springs and 19 of 446 observation towers cite it. Waterfalls: 382 of 420 cite "Vodopády České republiky" (vodopady.info, no licence found). Barrows (263 of 325) and hillforts (134 of 384) cite Památkový katalog NPÚ, which overlaps the `npu-uskp-pamatky` candidate (every barrow item also has P762 ÚSKP id). Most other items have no reference at all: 1,393 of 1,433 stolpersteine, 1,945 of 1,950 fingerposts, 1,411 of 1,970 abandoned villages and 664 of 680 bunkers. This confirms coordinates must not be copied.
- **Linkage (all of CZ, WD items inside the CZ border ∩ taginfo QID list, 2026-09-27):**

  | Class | WD items | QID already in OSM | Not linked | Not linked with OSM object nearby (national, local extract) | 12-item OSM API sample |
  |---|---|---|---|---|---|
  | Stolperstein | 1,433 | 101 | 1,332 | 1,239 (93 %) within 30 m | 12/12 within 30 m |
  | Fingerpost | 1,950 | 238 | 1,712 | 1,592 (93 %) within 50 m | 12/12 within 50 m |
  | Abandoned village | 1,970 | 421 | 1,549 | 586 (38 %) within 300 m | 3/12 within 300 m |
  | Abandoned hamlet | 1,031 | 153 | 878 | 329 (37 %) within 300 m | 3/12 within 300 m |
  | Bunker | 680 | 54 | 626 | 236 (38 %) within 60 m | 4/12 within 60 m |
  | Waterfall | 420 | 61 | 359 | 10 (3 %) within 150 m ¹ | 6/12 within 150 m |
  | Barrow burial ground | 325 | 1 | 324 | 17 (5 %) within 200 m | 0/12 within 200 m |
  | Hillfort | 384 | 73 | 311 | 59 (19 %) within 300 m | 3/12 within 300 m |
  | Spring | 441 | 170 | 271 | 188 (69 %) within 150 m | 10/12 within 150 m |
  | Observation tower | 446 | 204 | 242 | 193 (80 %) within 150 m | 10/12 within 150 m |
  | Synagogue | 298 | 78 | 220 | 43 (20 %) within 80 m | 3/12 within 80 m |
  | Gazebo | 258 | 56 | 202 | 41 (20 %) within 80 m ¹ | 3/12 within 80 m |
  | Jewish cemetery | 425 | 275 | 150 | 52 (35 %) within 200 m ¹ | 8/12 within 200 m |
  | Cave | 206 | 94 | 112 | 57 (51 %) within 150 m | 7/12 within 150 m |

  The national column is a local match against the 2026-09-27 Czechia extract (Postpass unavailable): every
  unlinked item inside the CZ border against OSM nodes and ways (ways reduced to the mean of their nodes, no
  relations) with the same class tags as the sample, within the class radius capped at 300 m. It confirms the
  sample: stolpersteine (1,239), fingerposts (1,592), observation towers (193) and springs (188) are almost all
  linking jobs, 3,212 in total; barrows (307 of 324 with nothing nearby), hillforts (252 of 311), synagogues
  (177 of 220) and bunkers (390 of 626) are mostly absent from OSM. Abandoned villages and hamlets: 915 of
  2,427 have a place/abandoned:place object within 300 m. ¹ Lower bounds, because the extract lacks part of the
  target tags: it holds only 105 of the 444 waterway=waterfall objects, landuse=cemetery only when a religion
  tag is present, and amenity=shelter only when another filtered key is present (the waterfall run also accepted natural=waterfall); for these classes the 12-item sample is the better guide.
  The sample column checked random unlinked items with one OSM API `map` call each (bbox radius capped at 300 m, 168 calls, 2026-09-27), because Postpass returned 503 all evening. Reading: stolpersteine, fingerposts, springs and observation towers are **linking jobs** (the OSM object exists without `wikidata`). Barrows, hillforts, synagogues, abandoned villages and bunkers are mostly **absent from OSM** and need a survey or another licensed source (NPÚ for barrows and hillforts).
- **Reverse links are already done:** 54,000 CZ items carry P11693 (OSM node ID), and only 392 of them have a QID that is on no OSM object. So the work is OSM→Wikidata tagging, not the other way.
- **ZABAGED overlap** (layer counts from `ags.cuzk.gov.cz/arcgis/rest/services/ZABAGED_POLOHOPIS/MapServer`, 2026-09-27): Vstup do jeskyně 486, Vodopád (bod) 386, Bunkr 6,100, Rozvalina/zřícenina 12,192, Hřbitov 5,735, Věž 17,281. ZABAGED is the better geometry source for caves, waterfalls and bunkers. Wikidata adds the QID and names only.
- **External ids on the items** that could become separate leads: P3003 zanikleobce.cz (1,733 abandoned villages), P5515 znicenekostely.cz (102 synagogues), P6736 Drobné památky. Licences of zanikleobce.cz and vodopady.info were not checked.
- **Suggested Sync setup:** reuse `group.wikidata` with `licensed = true`, `ref_tag = "wikidata"`, `create_keys` empty or class tag only, and a tight `max_distance_m` for point classes (stolperstein 30 m, fingerpost 50 m).
- Wiki pages read: Key:wikidata, Wikidata, Import/ODbL Compatibility, Tag:memorial=stolperstein, Key:abandoned:place, Tag:military=bunker, Tag:waterway=waterfall, Tag:tower:type=observation, Key:archaeological_site.

## Wiki entry
```
===Wikidata – QID pro okrajové třídy objektů===
* dataset: položky Wikidat v ČR se souřadnicemi (P17=Q213, P625) – kameny zmizelých, rozcestníky, zaniklé obce a osady, bunkry, vodopády, mohylníky, hradiště, prameny, rozhledny, synagogy, altány, židovské hřbitovy, jeskyně
* gestor: [https://www.wikidata.org Wikidata]
* licence: CC0 1.0 [https://creativecommons.org/publicdomain/zero/1.0/] – přebírat jen QID, ne souřadnice (část je převzata z Mapy.com a Wikipedie)
* datové primitivy: body
* odkaz: https://query.wikidata.org/sparql
* navržený tag {{tag|wikidata|<QID>}} na existující objekt
* poznámka: z 1 433 kamenů zmizelých ve Wikidatech je v OSM propojeno 101, z 1 950 rozcestníků 238, z 325 mohylníků 1; u 1 239 nepropojených kamenů a 1 592 rozcestníků už objekt v OSM je, stačí doplnit QID; rozšíření skupiny Wikidata v Sync (zatím jen muzea a hrady)
```
