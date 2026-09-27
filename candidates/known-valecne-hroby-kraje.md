# Válečné hroby – regional open-data extracts of the Central War Graves Register (Liberecký kraj, Královéhradecký kraj)

| Field | Value |
|---|---|
| publisher | Liberecký kraj (IČO 70891508); Královéhradecký kraj (IČO 70889546). Source register: Ministerstvo obrany, Centrální evidence válečných hrobů (CEVH) |
| url | Liberec: https://www.datalk.cz/api/download/v1/items/e7c67bee712f450783b490883fb6ff09/geojson?layers=0 (REST https://services7.arcgis.com/46Lck1orT7mvuzK5/arcgis/rest/services/V%C3%A1le%C4%8Dn%C3%A9_hroby_v_Libereck%C3%A9m_kraji/FeatureServer/0); KHK: https://www.datakhk.cz/api/download/v1/items/f51fcdb253344157a658e9fe3a4cd385/csv?layers=0 (REST https://services6.arcgis.com/ogJAiK65nXL1mXAW/arcgis/rest/services/V%C3%A1le%C4%8Dn%C3%A9_hroby/FeatureServer/0) |
| format | GeoJSON, CSV, KML, ArcGIS FeatureServer |
| coords | yes |
| records | Liberec 896 (Pietní místo – objekt 400, Válečný hrob s ostatky 376, deska 98, …); KHK 1,423 (checked 2026-09-27) |
| osm_tags | historic=memorial + memorial=war_memorial (+ memorial=plaque for desky); graves with remains: historic=tomb + tomb=war_grave; memorial:conflict; suggested ref:cevh=&lt;ID_hrobů, e.g. CZE5101-43071&gt; |
| osm_count_cz | historic=memorial 30,272; memorial=war_memorial 2,897; tomb=war_grave 30; ref:cevh 2 (taginfo 2026-09-26) |
| license | NKOD terms: contains no copyrighted works, not a copyright-protected database, no sui generis right, no personal data (mapped to CC0) |
| license_url | https://data.gov.cz/zdroj/datové-sady/70891508/30baff3f7c8600b5375c6527731fb852 ; https://data.gov.cz/zdroj/datové-sady/70889546/1f05b2ceb4d26640181f7f0e840ce864 |
| license_status | ok |
| update_freq | unknown / irregular (regional extracts) |
| impact | 1 |
| verified | yes |

## Notes
Known (listed on Cs:Česko/freemap, "Evidence válečných hrobů", licence empty there) — adds: the national MO register (evidencevh.mo.gov.cz) still has **no open download**. It is a Kendo web app; the linked CENIA WMS `mo_valecne_hroby` returned 503/timeouts on 2026-09-27, and there is no licence statement. However, two kraje republish their part as open data with public-domain-equivalent NKOD terms.

- **Gap is small.** Postpass test: 35 of 40 random Liberec records already have a memorial/tomb/wayside cross in OSM within 50 m, probably thanks to the drobnepamatky.cz sync. The main value is adding `ref:cevh` (Liberec carries the CEVH ID `ID_hrobů` plus a link `https://evidencevh.mo.gov.cz/Evidence/detail-hrobu-ci-mista?id=…`) and `memorial:conflict` (field `Historické_události`), and distinguishing graves with remains from memorials.
- The KHK layer has its own `dp_id` (VH1…) and no CEVH ID, so it is less useful. The Karlovarský kraj dataset "Vojenské a pietní památky" has only 11 records and is not worth using.
- **Caveat.** Liberec `WKT_souřadnice` has swapped lat/lon and uses decimal commas. Use the geometry, not the WKT string.
- **Wiki pages read:** Tag:memorial=war_memorial (links `historic=tomb` + `tomb=war_grave` for war graves), Tag:historic=memorial.
- Better long-term: ask MO (valecnehroby.mo.gov.cz) to publish the national register as open data. The regional extracts show it is feasible.

## Wiki entry
```
===Válečné hroby – krajské výřezy (Liberecký a Královéhradecký kraj)===
* dataset: Válečné hroby v Libereckém kraji; Válečné hroby (Královéhradecký kraj)
* gestor: [https://www.kraj-lbc.cz/ Liberecký kraj], [https://www.khk.cz/ Královéhradecký kraj] (zdroj: Centrální evidence válečných hrobů MO)
* licence: neobsahuje autorská díla, není chráněnou databází (CC0) [https://data.gov.cz/zdroj/datové-sady/70891508/30baff3f7c8600b5375c6527731fb852]
* datové primitivy: body
* odkaz: https://www.datalk.cz/api/download/v1/items/e7c67bee712f450783b490883fb6ff09/geojson?layers=0 , https://www.datakhk.cz/api/download/v1/items/f51fcdb253344157a658e9fe3a4cd385/csv?layers=0
* navržený tag {{tag|historic|memorial}} + {{tag|memorial|war_memorial}}, {{tag|historic|tomb}} + {{tag|tomb|war_grave}}, {{tag|ref:cevh|<ID hrobu>}}
* poznámka: většina míst už v OSM je (v Libereckém kraji ~88 % v okruhu 50 m), přínosem je hlavně ID z CEVH; celostátní evidence MO otevřená data nemá
```
