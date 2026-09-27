# NKOD SPARQL queries

Endpoint: `https://data.gov.cz/sparql` (Virtuoso). Send the query as a POST form parameter:

```
curl -sS -m 250 https://data.gov.cz/sparql --data-urlencode "query=$Q" -H 'Accept: text/csv'
```

Tips:
- The endpoint times out (HTTP 504 "Gateway Timeout" HTML page) on heavy GROUP BY/GROUP_CONCAT over all ~30k datasets. Paginate with `LIMIT 5000 OFFSET n` instead, then join locally.
- `text/csv` gives proper UTF-8. `text/tab-separated-values` escapes non-ASCII as `é`.
- IRIs beginning `https://data.gov.cz/zdroj/podněty-na-data-k-otevření/` are *requests* to open data, not datasets. Check `má-stav-návrhu` (e.g. `NelzePublikovat`). Policie ČR "Střelnice" is one of these, so no data exists.
- Licence terms sit on the distribution: `dist <https://data.gov.cz/slovník/podmínky-užití/specifikace> ?s`. `?s skos:narrowMatch` holds the EU licence URI (CC0 / CC_BY_4_0). The keys `autorské-dílo`, `databáze-jako-autorské-dílo`, `databáze-chráněná-zvláštními-právy` and `osobní-údaje` hold the Czech terms.

## 1. Count datasets per publisher that have a geo-format distribution

```sparql
PREFIX dcat: <http://www.w3.org/ns/dcat#> PREFIX dct: <http://purl.org/dc/terms/>
SELECT ?pub (COUNT(DISTINCT ?d) AS ?n) WHERE {
  ?d a dcat:Dataset ; dct:publisher ?pub ; dcat:distribution ?dist .
  ?dist dct:format ?f .
  FILTER(REGEX(STR(?f),"GEOJSON|SHP|GPKG|KML|WFS|GML","i"))
} GROUP BY ?pub ORDER BY DESC(?n) LIMIT 150
```

## 2. Dump all dataset titles and publishers (paginate, OFFSET 0..30000 step 5000)

```sparql
PREFIX dcat: <http://www.w3.org/ns/dcat#> PREFIX dct: <http://purl.org/dc/terms/>
SELECT ?d ?title ?pub WHERE {
  ?d a dcat:Dataset ; dct:title ?title ; dct:publisher ?pub .
  FILTER(LANG(?title)="cs")
} LIMIT 5000 OFFSET 0
```

Then grep titles locally for themes (odpad|sběr|koupa|hřbitov|pohřeb|vysílač|záchrann|jez|hráz|…).

## 3. Publisher names

```sparql
PREFIX foaf: <http://xmlns.com/foaf/0.1/> PREFIX dct: <http://purl.org/dc/terms/> PREFIX dcat: <http://www.w3.org/ns/dcat#>
SELECT DISTINCT ?pub ?name WHERE {
  ?d a dcat:Dataset; dct:publisher ?pub . ?pub foaf:name ?name . FILTER(LANG(?name)="cs")
}
```

## 4. Distributions (download URL, format) for a dataset by exact title

```sparql
PREFIX dcat: <http://www.w3.org/ns/dcat#> PREFIX dct: <http://purl.org/dc/terms/>
SELECT DISTINCT ?d ?f ?dl ?acc WHERE {
  ?d a dcat:Dataset ; dct:title ?t ; dcat:distribution ?x .
  FILTER(STR(?t)="Seznam zařízení pro nakládání s odpady")
  OPTIONAL{?x dcat:downloadURL ?dl} OPTIONAL{?x dcat:accessURL ?acc} OPTIONAL{?x dct:format ?f}
}
```

Note: some titles have a trailing space (e.g. ERÚ "Technologická energetická zařízení - výrobny elektřiny ").

## 5. Licence terms of a dataset's distributions

```sparql
PREFIX dcat: <http://www.w3.org/ns/dcat#> PREFIX dct: <http://purl.org/dc/terms/>
SELECT DISTINCT ?p ?v WHERE {
  ?d a dcat:Dataset ; dct:title ?t ; dcat:distribution ?x .
  FILTER(STR(?t)="Jezy")
  ?x <https://data.gov.cz/slovník/podmínky-užití/specifikace> ?s . ?s ?p ?v
}
```

## 6. Update frequency and EU licence by dataset IRI

```sparql
PREFIX dct: <http://purl.org/dc/terms/> PREFIX dcat: <http://www.w3.org/ns/dcat#>
SELECT DISTINCT ?freq ?lic WHERE {
  <https://data.gov.cz/zdroj/datové-sady/00164801/a7be43fdca614429fc50f48883a50298> dct:accrualPeriodicity ?freq .
  OPTIONAL { <https://data.gov.cz/zdroj/datové-sady/00164801/a7be43fdca614429fc50f48883a50298>
    dcat:distribution/<https://data.gov.cz/slovník/podmínky-užití/specifikace>/<http://www.w3.org/2004/02/skos/core#narrowMatch> ?lic }
}
```

## 7. All properties of one dataset (e.g. to see a "podnět" status)

```sparql
SELECT ?p ?o WHERE { <https://data.gov.cz/zdroj/podněty-na-data-k-otevření/12> ?p ?o }
```

## Postpass sample matcher

`tools/postpass_match.py` contains `match(points, sql_condition, radius_m, table, sample)`. It sends batches of `(id, lon, lat)` as a `VALUES` list to Postpass and counts, for each point, the OSM features within the radius that satisfy the tag condition. It uses `ST_Expand` bbox prefiltering plus `ST_DWithin` on geography.

## 8. High-Value Datasets (EU 2023/138) by publisher

NKOD marks HVD datasets with `dcatap:hvdCategory` (296 datasets on 2026-09-27; 1,390 carry
`dcatap:applicableLegislation <http://data.europa.eu/eli/reg_impl/2023/138/oj>`). Rows repeat a lot, so
deduplicate titles locally.

```sparql
PREFIX dcat: <http://www.w3.org/ns/dcat#> PREFIX dct: <http://purl.org/dc/terms/>
PREFIX dcatap: <http://data.europa.eu/r5r/> PREFIX foaf: <http://xmlns.com/foaf/0.1/>
SELECT ?d ?cat ?title ?pubname WHERE {
  ?d a dcat:Dataset ; dcatap:hvdCategory ?cat ; dct:title ?title ; dct:publisher ?pub .
  FILTER(LANG(?title)="cs")
  OPTIONAL{?pub foaf:name ?pubname FILTER(LANG(?pubname)="cs")}
}
```

## 9. Datasets with a geo-format distribution under CC0 / CC BY 4.0 / ODbL / PDDL

Returned 1,186 distinct datasets (2026-09-27); fits in one page.

```sparql
PREFIX dcat: <http://www.w3.org/ns/dcat#> PREFIX dct: <http://purl.org/dc/terms/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/> PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT DISTINCT ?d ?title ?pubname ?f ?lic WHERE {
  ?d a dcat:Dataset ; dct:title ?title ; dct:publisher ?pub ; dcat:distribution ?x . FILTER(LANG(?title)="cs")
  ?x dct:format ?f . FILTER(REGEX(STR(?f),"GEOJSON|SHP|GPKG|KML|WFS|GML|ARCGIS|ESRI","i"))
  ?x <https://data.gov.cz/slovník/podmínky-užití/specifikace>/skos:narrowMatch ?lic .
  FILTER(REGEX(STR(?lic),"CC0|CC_BY_4_0|ODBL|PDDL","i"))
  OPTIONAL{?pub foaf:name ?pubname FILTER(LANG(?pubname)="cs")}
} LIMIT 5000
```

## 10. Title keyword sweep (server-side REGEX, avoids dumping all titles)

Paginating query 2 without `DISTINCT` returns heavily duplicated rows. Filtering on the server is faster:

```sparql
PREFIX dcat: <http://www.w3.org/ns/dcat#> PREFIX dct: <http://purl.org/dc/terms/> PREFIX foaf: <http://xmlns.com/foaf/0.1/>
SELECT DISTINCT ?d ?title ?pubname WHERE {
  ?d a dcat:Dataset ; dct:title ?title ; dct:publisher ?pub . FILTER(LANG(?title)="cs")
  FILTER(REGEX(?title,"defibril|toalet|bezbariér|pítk|studán|jeskyn|rozhled|koupališ|hřiš","i"))
  OPTIONAL{?pub foaf:name ?pubname FILTER(LANG(?pubname)="cs")}
}
```

## National INSPIRE catalogue (CSW)

All 290 INSPIRE download services (2026-09-27) in Dublin Core, 100 per page:

```
curl 'https://geoportal.gov.cz/php/micka/csw/index.php?SERVICE=CSW&VERSION=2.0.2&REQUEST=GetRecords&TYPENAMES=csw:Record&RESULTTYPE=results&ELEMENTSETNAME=full&OUTPUTSCHEMA=http://www.opengis.net/cat/csw/2.0.2&MAXRECORDS=100&STARTPOSITION=1&CONSTRAINTLANGUAGE=CQL_TEXT&CONSTRAINT_LANGUAGE_VERSION=1.1.0&CONSTRAINT=ServiceType%3D%27download%27'
```

Full ISO record with download links: `REQUEST=GetRecordById&ID=<uuid>&OUTPUTSCHEMA=http://www.isotc211.org/2005/gmd&ELEMENTSETNAME=full`.

## ZABAGED object types (to check overlap)

Layer list: `https://ags.cuzk.gov.cz/arcgis/rest/services/ZABAGED_POLOHOPIS/MapServer?f=json` (149 layers).
Areál účelové zástavby (layer 114) has a `typzast_p` type (čistírna odpadních vod 3,819, úpravna vody 493,
camping 712…); count by type with `/114/query?where=1=1&groupByFieldsForStatistics=typzast_p&outStatistics=[{"statisticType":"count","onStatisticField":"OBJECTID","outStatisticFieldName":"n"}]&f=json`.
