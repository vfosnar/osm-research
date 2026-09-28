# Vinařský fond – Vinařská mapa „Vína z Moravy, vína z Čech“ (vinařství, vinotéky, sklepy, vinné restaurace)

| Field | Value |
|---|---|
| publisher | Vinařský fond (state fund under the viticulture act), IČO 71233717, Žerotínovo náměstí 3, Brno; info@vinarskyfond.cz. Map backend run by mojelahve.cz |
| url | https://mojelahve.cz/api/json/web/vmvc/map/search/do (GET, no parameters, returns everything); type list https://mojelahve.cz/api/json/web/vmvc/map/search/options/get; map shown on https://www.vinazmoravyvinazcech.cz/cs |
| format | JSON (`data[]`: id, type, title, url, location = town, gps = "lat, lon" with decimal commas) |
| coords | yes (all 1,849 records) |
| records | 1,849: winemaker 765 (vinařství), wine_shop 671 (vinotéky), cellar 184 (sklepy/degustace), restaurant 111, event 118 (events, not POIs). 1,731 place records, ids unique; 24 coordinate pairs shared by more than one record. The type labels in the options endpoint are swapped (wine_shop is labelled "Vinaři", winemaker "Vinotéky"); record titles show wine_shop = vinotéky and winemaker = vinařství |
| osm_tags | craft=winery (wiki Tag:craft=winery: building/property producing wine, with name, website, opening_hours); shop=wine (wiki Tag:shop=wine); amenity=restaurant for the restaurant type; proposed ref:vinarskyfond=&lt;id&gt; |
| osm_count_cz | craft=winery 399; shop=wine 551 (taginfo 2026-09-27) |
| license | none stated (no terms on vinazmoravyvinazcech.cz or on the API; Vinařský fond has no datasets in NKOD) |
| license_url | |
| license_status | unclear |
| update_freq | continuous (records edited by the fund and by wineries) |
| impact | 3 |
| verified | yes |

## Try it
- **Map preview:** none, because the licence is unclear.
- **QGIS:** open https://mojelahve.cz/api/json/web/vmvc/map/search/do in a browser or with curl, save it, split the `gps` field on ", " and replace the decimal commas with dots (python or a spreadsheet), then *Layer → Add Layer → Add Delimited Text Layer…*, X = lon, Y = lat, CRS EPSG:4326. QGIS cannot read the raw response directly (plain JSON array with coordinates in one text field).
- **Web:** https://www.vinazmoravyvinazcech.cz/cs (map widget "Vinařská mapa"); detail pages https://www.vinazmoravyvinazcech.cz/cs/vinari/&lt;id&gt;-&lt;slug&gt;

## Notes
- **What it is:** the national wine promotion body's map of wineries, wine shops, tasting cellars and wine restaurants in Moravia and Bohemia. It is not on `Cs:Česko/freemap` or in Sync. `Cs:Zdroje_v_jednani` records consent from Nadace Partnerství for its "Moravské vinařské stezky" POIs (2022). That is a different publisher and dataset; this one is the Vinařský fond list.
- **Gap (local match against the 2026-09-27 Czechia extract; Postpass returned 503):** nearest OSM craft=winery, shop=wine, a wine cellar or an object with wine cuisine within 100 m (restaurants: amenity=restaurant/cafe/pub/bar):
  - winemaker: 632 of 765 (83 %) have no wine POI in OSM within 100 m; 388 of these have no named OSM POI at all within 100 m.
  - wine_shop: 535 of 671 (80 %) unmatched; 466 of these have some other named POI within 100 m (town centres; some may be mapped as another shop type).
  - cellar: 147 of 184 unmatched. restaurant: 27 of 111 unmatched.
  - Mikulovsko sample area (bbox 16.55,48.72,16.90,48.90): 265 listed places against 68 OSM craft=winery + shop=wine objects; 151 of 183 wineries and 32 of 48 cellars have no OSM wine POI within 100 m.
- **Caveats:** many winery records are company seats (s.r.o. names, private persons like "Žáček Jozef"), so the point is often a home or office address rather than a visitable cellar. Import only with review, or use the list to add `website`/`ref` to existing objects and to flag unmapped cellars for survey. Detail pages (opening hours, contacts) are rendered client-side and were not scraped.
- **Licence:** not stated. Vinařský fond is a public-law body, but the database is not an official work; ask Vinařský fond (info@vinarskyfond.cz) for consent for OSM use.
- Wiki pages read: Tag:craft=winery, Tag:shop=wine.

## Wiki entry
```
===Vinařský fond – Vinařská mapa===
* dataset: Vinařská mapa Vína z Moravy, vína z Čech (vinařství, vinotéky, sklepy, restaurace)
* gestor: [https://www.vinarskyfond.cz/ Vinařský fond]
* licence: neuvedena – nutno požádat o souhlas
* datové primitivy: body
* odkaz: https://mojelahve.cz/api/json/web/vmvc/map/search/do
* navržený tag {{tag|craft|winery}}, {{tag|shop|wine}}, {{tag|ref:vinarskyfond|<id>}}
* poznámka: 632 ze 765 vinařství a 535 ze 671 vinoték nemá v OSM do 100 m odpovídající bod; na Mikulovsku 265 míst proti 68 v OSM
```
