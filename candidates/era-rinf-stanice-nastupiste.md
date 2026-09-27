```
name: ERA RINF (Register of Infrastructure) – Czech operational points and platform edges
publisher: European Union Agency for Railways (ERA); data submitted by Správa železnic as infrastructure manager
url: https://rinf.data.era.europa.eu/api/v1/sparql/rinf (SPARQL, POST with Content-Type: application/sparql-query); portal https://rinf.data.era.europa.eu/ ; ERA Knowledge Graph info https://www.era.europa.eu/domains/registers/era-knowlege-graph_en
format: RDF / SPARQL (CSV or JSON results)
coords: yes (wgs84_pos lat/long on each operational point's netReference)
records: 3,678 CZ operational points (1,210 stations, 1,542 passenger stops, 483 junctions, others); 4,965 platform edges at 2,649 operational points
osm_tags: railway=station|halt + uic_ref=54<5-digit code>, railway:ref=<SR70>; railway=platform / railway=platform_edge + height=<m>, length, ref
osm_count_cz: railway=station 1,218, railway=halt 1,642; uic_ref 926 (all objects); railway:ref on 814 stations + 901 halts; railway=platform 5,871; railway=platform_edge 202; height on about 200 platforms in the CZ bbox (taginfo 2026-09-26, Postpass 2026-09-27)
license: unclear. The ERA ontology is EUPL 1.2. The RINF data itself has no explicit licence on the pages I could fetch. The EU reuse policy (Decision 2011/833/EU) usually means CC BY 4.0, but I could not confirm that for RINF
license_url: https://www.era.europa.eu/domains/registers/era-knowlege-graph_en
license_status: unclear
update_freq: continuous, as the infrastructure manager updates RINF; the knowledge graph is refreshed periodically (exact cadence not verified)
impact: 3
verified: yes
```

## Notes
- **Queries run on 2026-09-27.**
  - Each OP has era:uopid (for example CZ54619 = Louny předměstí), era:opName (ASCII, no diacritics), era:opType, era:netReference with wgs84 lat/long, and a label with line km ("km 6.632 on line 191-01_0561").
  - Platform edges hang off tracks (OP → era:hasPart → track → era:hasPart → era:PlatformEdge). They carry era:platformId (e.g. "1 - č.n.:2_1", which is platform 1 on track 2), era:platformHeight and era:lengthOfPlatform (in metres).
  - Platform edges have no geometry of their own. They can only be attached per station, so they need manual or semi-automatic conflation.
- **Platform height distribution (SKOS labels in mm):**
  - 550 mm: 1,756
  - 200 mm: 1,231
  - 150 mm: 1,023
  - 250 mm: 885
  - code 170: 70 (label not resolved)
  - This is exactly the accessibility-relevant attribute (550 mm = level boarding) that OSM almost never has.
- **Gap (2,752 RINF stations and stops vs OSM railway=station|halt in the CZ bbox, via Postpass):**
  - 2,641 have an OSM station or halt within 300 m.
  - 2,046 have no matching uic_ref in OSM.
  - 1,117 have no railway:ref starting with the same 5 digits.
  - In CZ practice, uic_ref = "54" + the 5-digit code (e.g. Třebechovice p. O.: railway:ref=531608, uic_ref=5453160). The RINF uopid digits equal the first 5 SR70 digits, so uic_ref can be derived directly. railway:ref (6-digit SR70 with check digit) needs the check digit, which RINF does not include.
- **Wiki pages read:**
  - Key:uic_ref: always 7 digits with a 2-digit UIC country code. It warns against confusing it with IBNR.
  - Cs:Key:railway:ref: an internal railway code.
  - Tag:railway=platform (ref, wheelchair).
  - Tag:railway=platform_edge ("in use"; height=<metres above rail>, ref = track number).
  - Heights must be converted from mm to m (height=0.55).
- **Caveats:**
  - opName is ASCII-folded, so match by code or position, not by name.
  - RINF also has 483 junctions (railway=junction / railway=service_station), which is a possible extra.
- **Licence action:** ask ERA (RINF team) for a statement on reuse of RINF data under CC BY 4.0 / ODbL compatibility. Alternatively, ask Správa železnic for consent, because they are the data originator. Codes such as uic_ref are facts and arguably not protected, but the bulk extraction of platform attributes is.
- **Suggested keys:** uic_ref, railway:ref (already in use), height on railway=platform_edge.

## Wiki entry
```
===ERA RINF – dopravny a nástupní hrany===
* dataset: Register of Infrastructure (RINF) – operational points a platform edges v CZ
* gestor: [https://www.era.europa.eu/domains/registers/rinf_en European Union Agency for Railways] (data dodává Správa železnic)
* licence: nejasná (ontologie EUPL 1.2, data bez výslovné licence) [https://www.era.europa.eu/domains/registers/era-knowlege-graph_en]
* datové primitivy: body (dopravny), atributy nástupních hran
* odkaz: https://rinf.data.era.europa.eu/api/v1/sparql/rinf
* navržený tag {{tag|uic_ref|54<kód>}}, {{tag|railway:ref|<SR70>}}, {{tag|railway|platform_edge}} + {{tag|height|0.55}}
* poznámka: z 2 752 stanic a zastávek chybí v OSM uic_ref u ~2 050 a výška nástupišť (4 965 hran) v OSM prakticky není
```
