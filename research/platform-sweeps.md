# Platform sweeps: uMap, ArcGIS Online, Zenodo/Figshare (round 6)

Round 6 (2026-09-28) searched hosting platforms for original Czech geodata published by
people and groups outside government under an explicit licence. The result is thin. These
platforms hold very little Czech point data that is original, useful and openly licensed.
Most of it is either government data re-hosted or student exercises with no licence.

## How each platform was searched

### uMap (umap.openstreetmap.fr)
- Search: `https://umap.openstreetmap.fr/en/search/?q=<text>&p=<page>` (HTML, 10 maps/page).
  Each result carries a `data-settings='…'` JSON attribute with `properties.licence`, centre,
  and datalayer ids. It matches map names only. There is no bbox filter and no JSON API.
- Map page `…/en/map/x_<id>` (settings in `data-settings="…"`), datalayer GeoJSON
  `…/en/datalayer/<map_id>/<layer_uuid>/`.
- The instance offers only three licences: ODbL, WTFPL and Licence Ouverte (plus "no licence").
- 99 Czech keywords (towns, regions, POI types) → 720 maps, **186 centred in the CZ bbox**.
  Licence: none 178, ODbL 4, WTFPL 2, Licence Ouverte 1. The largest Czech maps by feature count
  were fetched as well.
- No Czech instance was found: umap.openstreetmap.cz and umap.osm.cz do not resolve. A few test
  queries on umap.openstreetmap.de, umap.osm.ch and umap.openstreetmap.pl returned almost no
  Czech maps.

### ArcGIS Online
- Anonymous search: `https://www.arcgis.com/sharing/rest/search?q=<query>&bbox=12.09,48.55,18.86,51.06&num=100&start=<n>&f=json`.
  `licenseinfo:` is a searchable field. Results include `owner`, `licenseInfo`, `extent`, `url`.
- Licence sweep: `licenseinfo:` "Creative Commons", CC0, "CC BY", "CC-BY", ODbL,
  "Open Data Commons", "public domain", "otevřená data", licence × 6 item types. Items whose
  extent lies within 11–20 °E / 47.8–51.8 °N were kept: **1,297 items**, about 110 owners.
  About 90 % of them come from cities, regions and state bodies (opendatapraha, OpenDataBrno,
  DATAKHK, karp, pk, msk, OK, LK, Most, Jihlava, ČHMÚ, AOPK).
- Topic sweep: 50 Czech POI keywords (studánky, kříže, drobné památky, lavičky, pítka, rozhledny,
  pomníky, sochy, jeskyně, prameny …) plus NGO keywords ("z.s.", spolek, "o.p.s.", KČT, ČSOP,
  Brontosaurus, Muzeum, CHKO, MAS), no licence filter.
- Layer details were read from `<service>/<layer>?f=json`, counts from `query?returnCountOnly=true`.

### Zenodo, Figshare, data.europa.eu
- Zenodo `https://zenodo.org/api/records?q=…&type=dataset&size=25` (size > 25 returns 400
  anonymously): 46 English topic terms combined with (Czech OR Czechia OR Bohemia OR Moravia) → 268
  datasets, plus Czech-language terms (drobné památky, studánky, kříže, mapování, boží muka…).
- Figshare `POST https://api.figshare.com/v2/articles/search` (item_type 3 = dataset), 7 queries.
- data.europa.eu, CZ facet: 30,336 datasets, all from three government catalogues (NKOD 29,165,
  NSIP 918, INSPIRE geoportal 253). It has no non-government Czech publisher.

## Triage

| Platform | Item / map | Owner | Records | Licence | Verdict |
|---|---|---|---|---|---|
| ArcGIS | Válečné hroby a drobné neevidované památky (ORP Ústí n. L.) | Statutární město Ústí nad Labem (`gismmu`) | 177 + 92 pts | CC BY-SA 4.0 | **Candidate** `candidates/usti-drobne-pamatky.md` – 28 small monuments with no OSM object within 75 m |
| ArcGIS | Pomníky Orlických hor – databáze | diploma thesis author (`slanina_spszem`) | 161 pts | none | **Candidate** `candidates/pomniky-orlickych-hor.md` – 25 surviving memorials missing, adds dates/descriptions |
| ArcGIS | Sochařské symposium (Hořice) | Město Hořice (`MEHORI`) | 134 pts | CC BY-SA 4.0 | Rejected: 133 of 134 already in OSM within 30 m (148 OSM artworks in the town, 140 with ref:drobne_pamatky + wikidata); only artist and year would be added |
| ArcGIS | M59 – moderní architektura 60./70. let | NPÚ org (`Eismann`) | 653 pts | CC BY-SA 4.0 | Rejected: derived from Památkový katalog (NPÚ), covered by `npu-uskp-pamatky.md` |
| ArcGIS | Staré lomy Liberecka (stav 1946) | `ondrej.volak` | 232 pts | "Creative Commons 3.0" (variant not stated) | Rejected: historical quarry register, owner/rock data, not current features |
| ArcGIS | Toponymické objekty / Prostorová fixace živých jmen (Živá jména, TUL) | `daniel.vrbik1` | 1,922 pts / 780 hexes | CC BY 4.0 | Rejected: unofficial names as hexagon aggregates; points carry only an object type |
| ArcGIS | Locations of timber buildings (dendrochronology) | Charles Univ. DataHub (`datahub_cuni`) | 1,824 pts | CC BY 4.0 | Rejected: only township/district, no names or object identity |
| ArcGIS | Vodní objekty / Vodní toky 1843, Zaplavené domy 1858, Tramvaje Liberec | `ondrej.coufal` | – | CC BY-SA 3.0 CZ | Rejected: historical reconstructions |
| ArcGIS | Sochy Masarykovy univerzity; Sochy pro Brno | Brno city (`hradecka_mmb`) | 52 / 10 pts | CC BY | Rejected: small, city data (see `brno-data-portal.md`) |
| ArcGIS | KML naučné stezky / tabule / sochy / veřejná WC (Přerov extent) | `martin.bartos` | KML | CC BY | Rejected here: Přerov city layers, belongs to city portals |
| ArcGIS | kamery_hosting | `sicova` | 77 pts | CC0 | Rejected: street-camera list of one town (CISLO, ULICE), no use for OSM |
| ArcGIS | Karlovarský kraj tourism layers (náboženské památky, pivovary, vleky…) | `pavla.brabencova_karp` | – | CC BY 4.0 | Known: `regional-tourism-hubs.md` |
| ArcGIS | Zpracování/skládky/sběrny odpadu ČR; příjmy ORP | `jiri_smida` | – | CC BY-NC-SA 4.0 | Incompatible (NC) |
| ArcGIS | Mapový atlas důlních děl; garanti; Rozdělení území | NPÚ org users | – | CC BY-NC-ND | Incompatible |
| ArcGIS | Barokní exteriérová skulptura – okres Rokycany | NPÚ org (`renatajedlickova`) | 42 pts | none | Rejected: small, links to Památkový katalog |
| ArcGIS | Rozhledny ČR | `Medojed` | 411 pts | none | Rejected: 2016, towers are well mapped in OSM |
| ArcGIS | Springs_eStudanky; prameny_atlas (Prameny spojují) | `jiri_smida`, `daniel.vrbik1` (TU Liberec) | 592 / 254 pts | none | Rejected: eStudánky copy (CC BY-NC-ND); the Prameny spojují field layer is a small research sample |
| ArcGIS | jeskyně CZ (JESO); Správa jeskyní layers | `ivan.balak`, `Sprava_jeskyni` | – | © JESO / none | Known: `aopk-jeso-krasove-jevy.md` |
| ArcGIS | Drobné památky Poruba / Morávka / Vratimov / Jeseník; lavičky, kontejnery, památné stromy (≈100 items) | Ostrava Univ., MENDELU, ČZU, ČVUT, UK student accounts | 10–200 each | none | Rejected: coursework, unmaintained, no licence |
| ArcGIS | Mlýny a vodárny (Chrudim) | Regional museum Chrudim (`zdenek.havlik_meuchrudim`) | 13 pts | none | Rejected: tiny |
| ArcGIS | Cirkev_v_plzenske_diecezi | `76412_muni` | 93/227/78 pts | none | Rejected: NGO registry points (IČO), not places of worship |
| ArcGIS | neratovice/ricany/sedlcany… stromy | `mapy_projekty` | 1,000–1,700 polygons each | none | Open lead: street-tree inventories of towns (species, height, vitality); publisher and licence unknown |
| uMap | Pražská pítka (ODbL) | anonymous | 0 features (empty layers) | ODbL | Rejected: empty |
| uMap | Czech board games, KMŽ Brno I, Praha ×2, Bicycle tour Austria-Czechia | various | 1–7 features | ODbL / WTFPL / LO | Rejected: personal route/meeting maps |
| uMap | OKD / OKK Ostrava | anonymous | 3,767 features | none | Rejected: historical mining railways, no licence |
| uMap | Mapa morušovníků černých v ČR | anonymous | 119 pts | none | Rejected: small, no licence (natural=tree species=Morus nigra) |
| uMap | other 178 Czech maps | – | – | none | Rejected: trip plans, drawings, OSM-traced sketches |
| Zenodo | Coordinates of post-WW2 churches opened 07-06-2024 in Czechia | Jan Lochman | one .ods (17 kB) | CC BY 4.0 | Rejected: one-off list derived from Noc kostelů programme |
| Zenodo | An Unique Dataset for Christian Sacral Objects Identification (JČU) | Univ. of South Bohemia | 11 GB photos | CC BY 4.0 | Rejected: image ML dataset |
| Zenodo | Czech Roads GEOJSON Dataset (2026) | College of Polytechnics Jihlava | – | ODbL | Rejected: OSM extract |
| Zenodo | GIS data – středověké osídlení ČR; Neolithic settlements | researchers | – | CC BY 4.0 | Rejected: archaeology, not current features |
| Zenodo | Database of Prague Funerary Monuments 1500–1650 | researchers | – | CC BY-NC 4.0 | Incompatible |
| Figshare | 7 queries | – | – | – | Nothing relevant (biology, surveys) |
| data.europa.eu | CZ facet | – | 30,336 | – | Only government catalogues (NKOD, NSIP, INSPIRE) |

## Conclusions
- On ArcGIS Online, explicit open licences are set almost only by public bodies. People outside
  government (students, researchers) leave `licenseInfo` empty. The best non-government data (the
  Orlické hory memorials thesis) therefore needs a permission request.
- uMap maps rarely carry a licence (8 of 186 Czech maps), and the licensed ones hold almost no data.
- Research repositories hold Czech field data as tables inside supplementary material, mostly
  ecology plots. There are no POI inventories that OSM could use.
- For the next rounds, sweeping Mapotic (done in round 4) and the Czech NGO websites directly
  gives better results than generic platforms.
