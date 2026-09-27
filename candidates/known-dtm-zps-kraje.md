# Digitální technická mapa krajů – ZPS (základní prostorová situace) per obec, JVF DTM open data

| Field | Value |
|---|---|
| publisher | Kraje via krajdtm.cz (verified: Kraj Vysočina vys.krajdtm.cz, Jihočeský jck.krajdtm.cz, Královéhradecký khk.krajdtm.cz, Ústecký usk.krajdtm.cz, Moravskoslezský msk.krajdtm.cz); editor packages suffixed _KR (kraj), _OPL, _DOP, _PB |
| url | NKOD datasets "ZPS obec &lt;name&gt;" / "ZPS MoMc &lt;name&gt;", e.g. https://data.gov.cz/zdroj/datové-sady/70892156/a873f14ecf3b50a433325193c458d611 |
| format | JVF DTM XML (GML 3.2, EPSG:5514 S-JTSK, 3D) zipped; e.g. https://vys.krajdtm.cz/dmx-server/orders/30588/download_package/VS/2026/06/30/ZPS/public/VS_CZ063_OBEC_588024_20260630_ZPS_KR.jvf.zip |
| coords | yes (geodetic accuracy, S-JTSK) |
| records | per municipality; Telč (all 4 packages) 56,548 objects in KR + 12,995 OPL + 131,813 survey points: 5,888 plot (fences), 2,021 zeď, 6,590 budova, 1,388 chodník, 654 parkoviště, 589 schodiště, 147 zábradlí, 72 hřiště, 63 drobná sakrální stavba, 12 studna na veř. prostranství; Koštice (ÚK) 24,720 objects. NKOD holds ~2,700 (Vysočina), ~2,400 (JčK), ~1,900 (KHK), ~1,500 (ÚK), ~1,300 (MSK) dataset records (mostly ZPS packages) |
| osm_tags | barrier=fence, barrier=wall / barrier=retaining_wall, building=*, highway=footway + footway=sidewalk, amenity=parking, highway=steps, barrier=guard_rail, leisure=pitch, historic=wayside_shrine / wayside_cross, man_made=water_well, man_made=chimney |
| osm_count_cz | barrier=fence 140,340; barrier=wall 26,568; barrier=retaining_wall 10,325; highway=steps 32,691 (taginfo CZ 2026-09-26); OSM in Telč bbox (Postpass): 125 fences, 85 walls, 13 retaining walls vs 5,888 plot + 2,021 zeď objects in ZPS |
| license | NKOD terms of use: "neobsahuje autorská díla", "není autorskoprávně chráněnou databází", "není chráněna zvláštním právem pořizovatele databáze", "neobsahuje osobní údaje" |
| license_url | https://data.gov.cz/podmínky-užití/neobsahuje-autorská-díla ; https://data.gov.cz/podmínky-užití/není-chráněna-zvláštním-právem-pořizovatele-databáze |
| license_status | ok |
| update_freq | monthly/quarterly snapshots (packages dated 2026-06-30) |
| impact | 4 |
| verified | partial |

Known (listed on Cs:Česko/freemap under "Zdroje pro odvozování dat" → "Digitální technická mapa (DTM)", as a general tracing source) — adds: the ZPS vector data is downloadable per municipality as open data via NKOD from at least 5 regional DTM portals, with explicit "no copyright / no sui-generis right" terms (i.e. usable for import, not only for tracing), plus verified object counts and format.

## Notes
- Content verified by parsing two packages (Koštice ÚK, Telč Vysočina). Object classes: budova/hranice budovy, plot, zeď, chodník, schodiště, zábradlí, svodidlo, parkoviště, hřiště, dvůr, zahrada, udržovaná plocha zeleně, les, vodní tok, propustky, drobná sakrální/kulturní stavba, studna na veřejném prostranství, komín… No trees, benches or street lamps observed in ZPS (TI/lighting is a separate TI content part, not in these public packages).
- Biggest OSM gain: fences and walls (barrier=*) — almost unmapped in small towns; also sidewalks/steps and precise building outlines. Buildings conflict with existing RÚIAN-based building imports (ref:ruian:building 3.8M in CZ) — use DTM for geometry QA, not bulk replacement.
- Geometry is stored as boundary lines ("hranice …") + definition points ("… DefinicniBod") rather than closed polygons → polygon assembly needed. Coordinates are S-JTSK (EPSG:5514) with Z; transform with a proper grid (EPSG:5514→4326 with the ČÚZK transformation) to keep sub-metre accuracy.
- Multiple packages per municipality by editor (KR = kraj/údržba, OPL/DOP/PB = other editors; PB = raw survey points). Coverage is uneven — many municipalities have only partial ZPS.
- Regions not seen with ZPS packages in NKOD: JMK (dtm.jmk.cz), STČ, PLK, LBK, OLK, ZLK, PAK, KVK — check their DTM portals separately.
- The download URLs 301-redirect to a trailing-slash URL; use curl -L.
- Suggested ref: `ref:dtm=<ID>` (17-digit object ID in SpolecneAtributyVsechObjektu/ID, e.g. 42000040000306516) — not in use yet.
- Wiki pages read: Tag:barrier=fence (way, approved), Tag:barrier=wall, Tag:barrier=retaining_wall, Tag:highway=steps, Tag:footway=sidewalk, Tag:amenity=parking, Tag:leisure=pitch.

## Wiki entry
```
===Digitální technická mapa – ZPS jako otevřená data (doplnění)===
* dataset: ZPS obec <název> (JVF DTM)
* gestor: [https://data.gov.cz/ kraje – Vysočina, Jihočeský, Královéhradecký, Ústecký, Moravskoslezský (krajdtm.cz)]
* licence: bez autorskoprávní ochrany a bez zvláštního práva pořizovatele databáze dle NKOD [https://data.gov.cz/podmínky-užití/neobsahuje-autorská-díla]
* datové primitivy: body, linie (hranice objektů), plochy odvozené
* odkaz: https://vys.krajdtm.cz/dmx-server/orders/30588/download_package/VS/2026/06/30/ZPS/public/VS_CZ063_OBEC_588024_20260630_ZPS_KR.jvf.zip
* navržený tag {{tag|barrier|fence}}, {{tag|barrier|wall}}, {{tag|highway|steps}}, {{tag|ref:dtm|<ID>}}
* poznámka: Např. v Telči je v OSM 125 plotů, ZPS jich obsahuje 5 888.
```
