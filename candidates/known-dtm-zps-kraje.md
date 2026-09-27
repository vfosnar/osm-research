# Digitální technická mapa krajů – ZPS per obec: chodníky, schodiště, zábradlí (JVF DTM open data)

| Field | Value |
|---|---|
| publisher | Kraje via their DTM portals on krajdtm.cz. Investigated in depth: Kraj Vysočina (vys.krajdtm.cz, NKOD publisher 70890749). ZPS packages were also found in NKOD in an earlier round for Jihočeský (jck.krajdtm.cz), Královéhradecký (khk.krajdtm.cz), Ústecký (usk.krajdtm.cz) and Moravskoslezský (msk.krajdtm.cz) kraj. |
| url | Investigated package: Telč (obec 588024), NKOD dataset "ZPS obec Telč" https://data.gov.cz/zdroj/datové-sady/70890749/98097a8ff9892ad2192f50640fdc3426 (package `_KR`, lines + definition points) and https://data.gov.cz/zdroj/datové-sady/70890749/83d3b24d923d6338af951dbcf75879ae (package `_OPL`, ready-made area polygons). Downloads: https://vys.krajdtm.cz/dmx-server/orders/30588/download_package/VS/2026/06/30/ZPS/public/VS_CZ063_OBEC_588024_20260630_ZPS_KR.jvf.zip and https://vys.krajdtm.cz/dmx-server/orders/30588/download_package/VS/2026/06/30/ZPS/public/VS_CZ063_OBEC_588024_20260630_ZPS_OPL.jvf.zip. The scheme is one set of packages per municipality, each listed as its own NKOD dataset ("ZPS obec &lt;název&gt;"). |
| format | JVF DTM 1.4.3 XML (GML 3.2 geometry, EPSG:5514 S-JTSK), one `.jvf.xml` per zip. `_KR`: LineString (3D) + Point; `_OPL`: Polygon (2D) + MultiCurve (3D) |
| coords | yes (geodetic accuracy, S-JTSK) |
| records | Telč, 2026-06-30 snapshot. `_OPL` polygons: chodník 692 (96,600 m²; ≈ 40 km of sidewalk by a crude rectangle estimate), schodiště 293, parkoviště/odstavná plocha 327, drobná sakrální stavba 24. `_KR`: 696 chodník + 296 schodiště definition points, 604 hranice schodiště lines, 147 zábradlí lines (2.0 km), 2,965 "hranice dopravní stavby nebo plochy" lines with type 2 = chodník (45.4 km), 12 studna na veřejném prostranství. Secondary: 5,888 plot lines, 1,043 zeď lines + 489 zeď polygons. |
| osm_tags | Sidewalk: `area:highway=footway` for the polygon, plus a centreline `highway=footway` + `footway=sidewalk` (needs derivation, see notes); on roads `sidewalk=separate` / `sidewalk:left/right=*`; `surface=*` from PrevazujiciPovrch. Steps: `highway=steps` (way) with optional `area:highway=steps`. Handrail: `barrier=handrail` or `handrail=yes` on the steps way. Secondary: `amenity=parking`, `barrier=fence`, `barrier=wall` / `barrier=retaining_wall` |
| osm_count_cz | Taginfo CZ (data until 2026-09-26): highway=steps 32,691; footway=sidewalk 60,724; area:highway=footway 3,498; area:highway=steps 104; barrier=handrail 655; handrail=* 17,386; sidewalk=* 54,670. Postpass, inside the OSM boundary of Telč (relation 441173), 2026-09-27: highway=steps 12, footway=sidewalk 13, highway=footway 641, roads carrying a sidewalk* tag 3 (of 649 road ways), area:highway 0, barrier=handrail 0, handrail=* 8, amenity=parking 51 |
| license | NKOD terms of use for all four Telč datasets: "neobsahuje autorská díla", "není autorskoprávně chráněnou databází", "není chráněna zvláštním právem pořizovatele databáze" |
| license_url | https://data.gov.cz/podmínky-užití/neobsahuje-autorská-díla ; https://data.gov.cz/podmínky-užití/není-autorskoprávně-chráněnou-databází ; https://data.gov.cz/podmínky-užití/není-chráněna-zvláštním-právem-pořizovatele-databáze |
| license_status | ok |
| update_freq | periodic full snapshots (Telč packages dated 2026-06-30, written 2026-07-01) |
| impact | 3 |
| verified | yes (Telč packages downloaded and parsed; OSM compared); other kraje: partial |

Known (listed on Cs:Česko/freemap under "Zdroje pro odvozování dat" → "Digitální technická mapa (DTM)", as a general tracing source) — adds: the ZPS vector data is downloadable per municipality as open data via NKOD with explicit "no copyright / no sui-generis right" terms (so usable for import, not only for tracing). The `_OPL` package has ready-made sidewalk and step polygons. ZABAGED does not contain either of these, and neither does anything else that has been imported.

## Try it

- **Map preview:** [`../samples/known-dtm-zps-kraje.geojson`](../samples/known-dtm-zps-kraje.geojson). It covers the centre of Telč (bbox 15.4435,49.1775 – 15.4625,49.1905): 516 chodník polygons, 204 schodiště polygons and 96 zábradlí lines (816 features, 784 kB). Properties are `class` (Czech), `osm_tag` (suggested), `ref:dtm`, `povrch`/`surface` and `plocha_m2`. The polygons come straight from the `_OPL` package and the handrails from `_KR`. They were transformed to WGS84 with pyproj's default EPSG:5514→4326 operation ("S-JTSK to WGS 84 (5)", stated accuracy 1 m) and rounded to 7 decimals.
- **QGIS:** download and unzip one of the packages above, then open the `.jvf.xml` with the QGIS plugin **JVF DTM Plugin** (Plugins → Manage and Install Plugins → "JVF DTM Plugin", https://plugins.qgis.org/plugins/qgis_jvf_dtm_plugin/, version 4.3.4). It loads JVF files into styled layer groups. I did not test the plugin (no QGIS here). What I did test: plain GDAL (3.12.4, GML driver) is **not** usable. On the `_KR` file it finds 0 layers. On the `_OPL` file it finds a single "LineString" layer (14,014 features) with no attributes and no CRS, because JVF nests the features too deeply for the GML driver's auto-detection. Renaming to `.gml` changes nothing. A remote `/vsizip/vsicurl/<url>/<member>.jvf.xml` path also failed to open here: the server answers the zip URL with a 301 to a trailing-slash URL and a `Content-Length: 0` redirect. So download first. The GMLAS driver was not tested.
- **Web viewer:** Kraj Vysočina's public DTM map, "Mapový klient – mapa pro veřejnost": https://vys.krajdtm.cz/-/public (HTTP 200, listed on https://vys.krajdtm.cz/portal-vys/moduly).

## Notes

### What ZABAGED has (and doesn't)
I checked against the ČÚZK *Katalog objektů ZABAGED* v4.7 (issued 3 July 2026; index https://geoportal.cuzk.gov.cz/Dokumenty/ZABAGED_katalog/CS/). I downloaded all 153 object-type pages and searched them.
- **Walls: yes.** 1.23 ZEĎ (`al260`) is a line covering cemetery walls, retaining walls, "massive walls acting as a fence" and noise barriers. Ordinary walls are included only from 50 m length; retaining walls have no length limit. This matches the known situation: walls are in ZABAGED, just not imported.
- **Fences: no separate type in the catalogue.** The only fence-like entries are the massive walls inside 1.23 and 6.12 LINIOVÁ VEGETACE (which includes clipped hedges). Light fences (plot) do not appear in any object definition. This contradicts the assumption that fences are in ZABAGED, so it is worth double-checking with the community. As agreed, fences and walls are not the selling point here anyway.
- **Sidewalks: no.** ZABAGED has street centrelines (2.02 ULICE; the C_TYPULICE code 225 "ulice typu chodník" marks a whole street segment as pedestrian-only) and 2.04 PĚŠINA. It has no roadside sidewalk areas or lines.
- **Steps, handrails: no.** No object type exists for either.
- **Parking:** 2.15 PARKOVIŠTĚ has a size limit ("plocha > 600 m²"). DTM also has the small ones. In Telč, DTM has 327 parking/hardstanding polygons: 12 are ≥ 600 m² (6 of those touch an OSM amenity=parking) and 101 are 100–600 m² (44 touch OSM). Caveat: DTM's "odstavná plocha" also covers private hardstanding.
- **Small sacral buildings and wells:** partly in ZABAGED already, via 1.21 KŘÍŽ, SLOUP KULTURNÍHO VÝZNAMU and 4.01 ZDROJ PODZEMNÍCH VOD ("vertikální jímací objekt podzemní vody"). Low extra value.

### Geometry: what DTM actually contains
- **`_KR` package (the one linked in the previous round):** everything is lines and points. Areas are stored as shared boundary lines plus a definition point: `HraniceDopravniStavbyPlochy` with attribute `TypDopravniStavbyNeboPlochy`, where code 2 = chodník per the JVF 1.4.3 code list in ČÚZK `atributy.xlsx`, https://www.cuzk.cz/DMVS/JVF-DTM/atributy.aspx; `HraniceSchodiste`; `ChodnikDefinicniBod`; `SchodisteDefinicniBod`. I polygonized all 31,813 boundary lines myself (shapely). 640/696 sidewalk points fell inside a closed face, but 128 of those faces were > 2,000 m² (leaking through gaps). So self-assembly from `_KR` is unreliable.
- **`_OPL` package:** the same objects as ready-made `gml:Polygon` areas (code suffix 03). There are 692 ChodnikPlocha and 293 SchodistePlocha, all valid polygons. **Use this package.** Their IDs (prefix 6300301…) differ from the definition-point IDs in `_KR`. Whether they stay stable between snapshots is unknown. Compare two monthly snapshots before relying on `ref:dtm` for Sync.
- **Sidewalks are polygons, fragmented.** They are cut at every driveway (nájezd) and crossing: 692 pieces, median 21 m², merging into 409 contiguous areas. Attributes are only `PrevazujiciPovrch`, which maps cleanly: 3 dlažba → `surface=paving_stones` (590 of 696), 1 asfalt → `asphalt`, 2 beton → `concrete`, 7 nezpevněno → `unpaved`. There is no width attribute, but width can be measured from the polygon.
- **Steps are polygons of the whole flight, mostly tiny.** In Telč, 205 of 293 are < 5 m² and 196 touch a building outline, so they are entrance steps to houses. Only 26 are ≥ 10 m². `DruhSchodiste` is 1 = vícestupňové for 290 and 2 = single-step platform for 3. There is no step count and no direction (up/down).
- **Handrails** are 3D lines (147 lines, 2.0 km).

### Tagging (wiki pages read, raw wikitext, 2026-09-27)
- Tag:footway=sidewalk / Cs:Tag:footway=sidewalk: "sidewalks as separate ways", way only, requires `highway=footway`. The Cs page recommends `sidewalk=*` on the road instead when the sidewalk is separated only by a kerb. When moving to separate ways, set `sidewalk=separate` on the road and connect the sidewalk to the network (crossings, driveways).
- Key:area:highway / Tag:area:highway=footway: area only, de facto / in use. "Don't create an area:highway=footway area without also creating a highway=footway linear way along the centerline". For stairs use `area:highway=steps`. Routers ignore area:highway.
- Tag:highway=steps / Cs:Tag:highway=steps: way only, drawn along the flight with `incline=up/down`; "For areas also use area:highway=steps"; `handrail=*`, `step_count=*` as extras.
- Tag:barrier=handrail: way, de facto ("questioned: unclear difference from fence"); alternatively `handrail=yes` on the steps way. Key:handrail: `handrail=yes/no`, `handrail:left/right/center`.

### How an importer would get OSM ways (honestly)
- **Sidewalk polygons → `area:highway=footway`** is direct, but the wiki says it is useless without a centreline, and area:highway has almost no users in CZ (3,498). On its own it is micromapping.
- **Sidewalk centrelines** (`highway=footway` + `footway=sidewalk`): these must be derived from the polygons with a straight skeleton or medial axis. The polygons are fragmented and have branches at corners and driveways, so this is non-trivial. The result then needs splicing into the road network with crossings. Doing it well is a per-street manual or semi-automatic job, not a bulk import.
- **Cheaper, robust use: tagging existing OSM data.** Test on which side of each OSM road a DTM sidewalk polygon lies and set `sidewalk:left/right=yes|no`, or `separate` where a parallel OSM footway already exists. Add `footway=sidewalk` and `surface=*` to existing OSM footways that lie inside a DTM sidewalk polygon.
- **Steps:** the polygon gives position and extent. The `highway=steps` way should run along the flight (long axis of the polygon) and be connected to the paths at both ends. `incline` can be derived from the 3D boundary lines in `_KR` (they carry Z). Only the ~26 non-trivial flights per town like Telč are worth it; the house-entrance steps are not.

### Gap in Telč (Postpass + OSM highway lines fetched 2026-09-27, compared in S-JTSK)
- **Sidewalks:** 370 OSM `highway=footway` ways (18.7 km) already lie mostly inside DTM sidewalk polygons, but only 13 ways in the whole municipality carry `footway=sidewalk`, and only 3 roads carry a sidewalk* tag. So in Telč much of the geometry exists; the missing parts are the *sidewalk semantics* (footway=sidewalk, sidewalk=* on roads, surface).
  - 280 of the 409 contiguous sidewalk areas (≈ 16.5 km, crude estimate) have less than 30 % of their length covered by any OSM foot/cycle way. That is the missing geometry.
- **Steps:** OSM has 12; DTM has 293 polygons, of which 26 are ≥ 10 m² and only 5 of those touch an OSM `highway=steps`. So about 20 real flights are missing in one small town.
- **Handrails:** 2.0 km in DTM; 0 `barrier=handrail` and 8 `handrail=*` in OSM.
- **Secondary (fences/walls):** 5,888 plot lines in DTM vs 110 `barrier=fence` in OSM inside the Telč boundary (Postpass 2026-09-27); walls 1,043 lines + 489 polygons in DTM vs 81 `barrier=wall` + 12 `barrier=retaining_wall` in OSM. Walls are in ZABAGED and simply not imported yet.

### Other caveats
- Coverage is uneven between municipalities and kraje. Regions without ZPS packages in NKOD (JMK, STČ, PLK, LBK, OLK, ZLK, PAK, KVK) were not investigated further.
- Multiple packages per municipality. For Telč: `_KR` has lines and points; `_OPL` has polygons; `_DOP` holds only "doprovodné informace" (change records: order name, submission ID, change-area polygons), no objects; `_PB` has survey points.
- Coordinates need a proper S-JTSK→ETRS89 transformation for sub-metre accuracy; pyproj's default here (no grid) has 1 m accuracy.
- Download URLs 301-redirect to a trailing-slash URL; use `curl -L`.
- Suggested ref: `ref:dtm=<ID>`, the 17-digit `SpolecneAtributyVsechObjektu/ID` (not in use in OSM). Its stability across snapshots is unverified.

## Wiki entry
```
===Digitální technická mapa – ZPS jako otevřená data: chodníky a schodiště===
* dataset: ZPS obec <název> (JVF DTM 1.4.3), balíčky _OPL (plochy) a _KR (linie a body); ověřeno na ZPS obec Telč
* gestor: [https://vys.krajdtm.cz/portal-vys/ Kraj Vysočina – DTM kraje] (balíčky ZPS v NKOD publikují také Jihočeský, Královéhradecký, Ústecký a Moravskoslezský kraj)
* licence: bez autorskoprávní ochrany a bez zvláštního práva pořizovatele databáze dle podmínek užití v NKOD [https://data.gov.cz/podmínky-užití/není-chráněna-zvláštním-právem-pořizovatele-databáze]
* datové primitivy: plochy (chodník, schodiště), linie (zábradlí)
* odkaz: https://vys.krajdtm.cz/dmx-server/orders/30588/download_package/VS/2026/06/30/ZPS/public/VS_CZ063_OBEC_588024_20260630_ZPS_OPL.jvf.zip
* navržený tag {{tag|footway|sidewalk}} (osa odvozená z plochy), {{tag|area:highway|footway}}, {{tag|sidewalk|separate}}, {{tag|highway|steps}}, {{tag|barrier|handrail}}, {{tag|ref:dtm|<ID>}}
* poznámka: V Telči má DTM 692 ploch chodníků a 293 schodišť, v OSM je jen 13 cest s footway=sidewalk a 12 schodišť; chodníky ani schodiště ZABAGED neobsahuje.
```
