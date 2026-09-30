# Slovakia: working endpoints and example queries

Tested from this environment on 30 September 2026. "Works" means a live request returned data;
anything that failed is listed under "Unreachable" with the symptom, so later rounds don't burn
time on it.

## OSM side

### Taginfo for Slovakia (Geofabrik) — works

Region path is `europe:slovakia`.

```
https://taginfo.geofabrik.de/europe:slovakia/api/4/key/stats?key=ref:minvskaddress
https://taginfo.geofabrik.de/europe:slovakia/api/4/tag/stats?key=amenity&value=pharmacy
https://taginfo.geofabrik.de/europe:slovakia/api/4/key/values?key=brand&query=Slovnaft
```

Checked: `ref:minvskaddress` = 1,493,182 objects; `amenity=pharmacy` = 1,694 (data until
2026-09-29T20:15Z). Use taginfo for national totals.

### Postpass — works

Same API as for Czechia (`/api/interpreter`, tables `postpass_point|line|polygon|pointpolygon…`).
Slovakia bbox `16.83,47.73,22.57,49.61` overlaps Austria, Hungary, Czechia, Poland and Ukraine
heavily:

```
curl https://postpass.geofabrik.de/api/interpreter \
  --data-urlencode "data=SELECT count(*) AS n FROM postpass_pointpolygon
    WHERE tags->>'amenity'='pharmacy'
    AND geom && ST_MakeEnvelope(16.83,47.73,22.57,49.61,4326)" \
  --data-urlencode "options[geojson]=false"
```

Returned `n = 2833` against taginfo's 1,694 for all of Slovakia — the bbox is ~70 % inflated.
Use bboxes of single towns/districts for gap checks, taginfo for totals. The SK country relation
is `14296` (used as `osm_query_area` in Sync).

### OSM wiki — works

```
curl -G https://wiki.openstreetmap.org/w/index.php --data-urlencode 'title=WikiProject Slovakia/Sources' --data action=raw
curl "https://wiki.openstreetmap.org/w/api.php?action=query&list=allpages&apprefix=Sk:&aplimit=500&format=json"
curl "https://wiki.openstreetmap.org/w/api.php?action=query&list=categorymembers&cmtitle=Category:Import_from_Slovakia&cmlimit=500&format=json"
```

Slovak pages use both `Sk:` and `SK:` prefixes (list both). Tag pages: check `Sk:Tag:…` too, but
they are mostly stubs; the English and `Cs:` pages are usually more complete.

### osm_sk Google group — works without login (HTML)

```
https://groups.google.com/g/osm_sk                      # latest ~30 threads
https://groups.google.com/g/osm_sk/search?q=import      # search (~30 hits per page)
https://groups.google.com/g/osm_sk/c/<thread-id>        # one thread, full text
```

Thread links in the HTML look like `href="./g/osm_sk/c/<id>"`; the `<title>` of a thread page is
the subject. Pages are ~1 MB of HTML; strip `<script>`/tags to read.

### Community's other tools

- Sync config (Czech community): `https://codeberg.org/osmcz/sync/raw/branch/main/backend/config.toml`
  — SK coverage only in `zasilkovna.dataset.zbox_sk` and `powerbox.dataset.powerbox`.
- POI-Importer: `https://openstreetmap.cz/poi-importer/datasets.js` (dataset list).
- Freemap downloads: `https://download.freemap.sk/` (directory index), address tooling
  `https://download.freemap.sk/minvskaddress/`, `https://minvskaddress.freemap.sk/` (weekly
  per-municipality RA vs OSM comparison), `https://download.freemap.sk/minvskaddress/okresy.html`.
- AKO offline mirror (cadastre attributes): `https://osm.margus.sk/ako/data/out/all/`.
- JOSM imagery list (source of SK WMS/TMS URLs): `https://josm.openstreetmap.de/maps`, entries
  with `<country-code>SK</country-code>`: Ortofotomozaika SR tiles
  `https://ofmozaika.tiles.freemap.sk/{zoom}/{x}/{y}.jpg` (also `ofmozaika2c`, `ofmozaika1c` for
  older cycles), DMR 5.0 / DMP 1.0 shading tiles on `*.tiles.freemap.sk`, ZBGIS WMS
  `https://zbgisws.skgeodesy.sk/zbgis_wms_featureinfo/service.svc/get?request=GetCapabilities&service=WMS`,
  Kataster WMS `https://kataster.skgeodesy.sk/eskn/services/NR/kn_wms_orto/MapServer/WmsServer`
  (the two skgeodesy WMS were unreachable from here, see below).

### AllThePlaces — works

```
https://data.alltheplaces.xyz/runs/latest.json                      # run id + URLs
https://alltheplaces-data.openaddresses.io/runs/<run>/stats/_results.json   # per-spider counts
https://alltheplaces-data.openaddresses.io/runs/<run>/stats/_insights.json  # per-brand, per-country splits (9 MB)
```

In `_insights.json`, each row has `atp_splits` keyed by ISO country; `atp_splits.SK` gives the
spiders and feature counts for Slovakia (141 brand/spider pairs, 7,635 features in run
2026-09-26). GitHub (spider source) is blocked here.

## National open data catalogue (data.slovensko.sk) — SPARQL works

`data.slovensko.sk` is a JavaScript front-end (every path returns the same 524-byte shell; CKAN
paths such as `/api/3/action/package_search` are **not** served, and `data.gov.sk` redirects to the
same shell). The working machine interface is SPARQL, DCAT-AP like the Czech NKOD:

```
curl -s https://data.slovensko.sk/api/sparql \
  --data-urlencode query@q.rq -H 'Accept: text/csv'     # or application/sparql-results+json
```

~22,600 datasets. Licences are not on the distribution directly but on a terms-of-use node
(`https://data.gov.sk/def/ontology/legislation/termsOfUse`) with `authorsWorkType`,
`originalDatabaseType`, `databaseProtectedBySpecialRightsType` (EU licence authority IRIs). Titles
carry `@sk`. Keyword search with download URL and database licence:

```sparql
PREFIX dcat: <http://www.w3.org/ns/dcat#>
PREFIX dct:  <http://purl.org/dc/terms/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX leg:  <https://data.gov.sk/def/ontology/legislation/>
SELECT ?title ?publisher ?modified ?format ?download ?dbLicence WHERE {
  ?d a dcat:Dataset ; dct:title ?title ; dcat:distribution ?dist .
  FILTER(lang(?title)="sk" && CONTAINS(LCASE(?title), "cyklo"))
  OPTIONAL { ?d dct:publisher/foaf:name ?publisher }
  OPTIONAL { ?d dct:modified ?modified }
  OPTIONAL { ?dist dct:format ?format }
  OPTIONAL { ?dist dcat:downloadURL ?download }
  OPTIONAL { ?dist leg:termsOfUse/leg:originalDatabaseType ?dbLicence }
} ORDER BY DESC(?modified) LIMIT 50
```

(0.9 s; returned Bratislava cycle-route passport CSV, Trnava region cycle routes SHP, Slovnaft
BAjk stations, …). Licence breakdown by dataset (30 Sep 2026): CC BY 4.0 17,374 (+290 with the
creativecommons.org IRI, +35 `CC_BY`), CC0 2,104, CC BY-SA 4.0 1,073, 0BSD 842, CC BY-NC 4.0 366,
PDM 62. So most catalogue data is `needs_waiver`.

```sparql
PREFIX dcat: <http://www.w3.org/ns/dcat#>
PREFIX leg:  <https://data.gov.sk/def/ontology/legislation/>
SELECT ?lic (COUNT(DISTINCT ?d) AS ?datasets) WHERE {
  ?d a dcat:Dataset ; dcat:distribution ?dist .
  ?dist leg:termsOfUse/leg:originalDatabaseType ?lic .
} GROUP BY ?lic ORDER BY DESC(?datasets)
```

Gotchas:
- Filter by publisher with the IRI, not the name literal: `dct:publisher
  <https://data.gov.sk/id/legal-subject/00151866>` (MV SR, IČO 00151866) works; matching
  `foaf:name "…"@sk` returned nothing. Publisher IRIs are `https://data.gov.sk/id/legal-subject/<IČO>`.
- Catalogue-hosted files download from `https://data.slovensko.sk/download?id=<uuid>` (works).
  Many distributions point to publisher portals instead (ArcGIS Hub:
  `https://data.bratislava.sk/api/download/v1/items/<id>/csv?layers=0` works and returns CSV with
  lat/lon; `opendata.trnava-vuc.sk/datasets/…/explore` links are HTML pages, not files).
- Dataset landing pages still use the old form `https://data.gov.sk/dataset/<slug>` (from
  `dcat:landingPage`).

## ÚGKK / GKÚ (ZBGIS, cadastre, orthophoto, LiDAR)

Works:
- Download page with all open files and their licence lines:
  `https://www.gku.sk/gku/produkty-sluzby/na-stiahnutie/zbgis.html`.
- Open file host: `https://opendata.skgeodesy.sk/static/…` (HEAD/GET work), e.g.
  administrative boundaries `https://opendata.skgeodesy.sk/static/ZBGIS/usj/ah_gpkg_0.zip`
  (40 MB, CC BY 4.0, author GKÚ Bratislava; also `_gdb_`, `_shp_`, `ah_csv.zip`, generalised levels
  1–3, `_sjtsk03` variants), orthophoto `…/static/Ortofotomozaika_SR/<cycle>/…zip` (100+ GB each),
  LiDAR `…/static/LLS/DMR5/DMR5_0_sjtsk03_bpv.zip`, `…/static/LLS/2_cyklus/LOTxx/…`.
- Geographic names (CC BY 4.0): `https://www.gku.sk/files/gku/produkty-sluzby/na-stiahnutie/gn_csv.zip`
  (7.4 MB; also `gn_gpkg.zip`, `gn_shp.zip`, `gn_gdb.zip`).
- ZBGIS sample by category: `https://www.gku.sk/files/gku/produkty-sluzby/na-stiahnutie/vzorka_zbgis_kategorie_gpkg.zip`.
- ZBGIS object catalogue (KTO): `https://www.skgeodesy.sk/files/sk/slovensky/ugkk/geodezia-kartografia/zb-gis/kto_zbgis.pdf`
  (1.6 MB PDF) — the SK counterpart of the ZABAGED catalogue; check it for overlaps.
- Map viewer: `https://zbgis.skgeodesy.sk/mapka/sk/zakladna-mapa` (linked; host unreachable here).

Unreachable from this environment (30 Sep 2026):
- `www.geoportal.sk` serves a certificate for `gku.sk` only → TLS name mismatch (server-side
  misconfiguration, not the proxy). WebFetch got 503. Pages linked from the wiki
  (`/sk/sluzby/mapove-sluzby/`, `/sk/inspire/…`, `/sk/udaje/…`) could not be read.
- `zbgis.skgeodesy.sk`, `zbgisws.skgeodesy.sk`, `kataster.skgeodesy.sk`, `ako.vugk.sk`,
  `inspire.geoportal.sk`: TLS handshake reset / proxy 502. GKÚ announced planned maintenance of
  "elektronické služby" on 30.9.2026 08:00–16:00, so retry on another day before concluding
  they are geo-blocked. `www.skgeodesy.sk`, `www.gku.sk` and `opendata.skgeodesy.sk` work.

## Ministry of Interior (MV SR)

- Address datasets in the catalogue ("Adresy v kraji|okrese|obci …", modified daily, GeoJSON,
  CC BY 4.0 in metadata): distribution URLs like
  `https://rageo.minv.sk/opendata/dataset/address_by_nuts3_SK010.geojson` (SK010 Bratislavský …
  SK042 Košický). **Unreachable here** (connection reset), as are `www.minv.sk` and
  `portal.minv.sk` (register-adries lookup). Find them via SPARQL with publisher IRI
  `https://data.gov.sk/id/legal-subject/00151866`.
- State border info system `https://ives.minv.sk/issh_internet/` works (the ministry says its
  data there is no longer current; `osm_sk` thread `t_1Rqha-CF0`).

## Other gotchas

- GitHub (web and API) returns 403 here; the GitHub MCP tool is scoped to this repo only, so
  `FreemapSlovakia/freemap-operations` issues cannot be read from this environment.
- `wiki.freemap.sk` (old community wiki) → proxy 502.
- `community.openstreetmap.org` has no Slovak category.
