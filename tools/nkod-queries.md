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
