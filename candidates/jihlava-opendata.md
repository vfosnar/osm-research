# opendata.jihlava.cz – odpadkové koše, dětská hřiště, sportoviště, parkoviště, lokality pro psy

| Field | Value |
|---|---|
| publisher | Statutární město Jihlava (Magistrát, oddělení GIS) |
| url | https://opendata.jihlava.cz/ (ArcGIS Hub; services5.arcgis.com/yyjDpIHsxn6gXsED) |
| format | ArcGIS FeatureServer + hub downloads (GeoJSON, CSV, SHP, GPKG, KML) |
| coords | yes |
| records | odpadkové koše 658 points; dětská hřiště 79 polygons; sportoviště 38 polygons; parkoviště polygons + lines; lokality pro psy (areas) |
| osm_tags | amenity=waste_basket; leisure=playground (+playground=* equipment list); leisure=pitch (+sport, surface); amenity=parking; leisure=dog_park (only for fenced dog areas) |
| osm_count_cz | amenity=waste_basket 26,290; leisure=playground 15,549; leisure=pitch 33,252 (taginfo CZ 2026-09-26) |
| license | CONFLICTING – NKOD entries (publisher 00286010) state "neobsahuje autorská díla / není autorskoprávně chráněnou databází"; the ArcGIS item licenseInfo says "Toto dílo je licencováno pod licencí Creative Commons CC-BY-SA" |
| license_url | https://data.gov.cz/zdroj/datové-sady/00286010/c6668d6897256bfa1da3dd0aa4a… (NKOD) ; https://www.arcgis.com/sharing/rest/content/items/17a8cec608944ef0813f43f49a609025 |
| license_status | unclear |
| update_freq | koše CONT, others OTHER |
| impact | 2 |
| sync_fit | Sync for waste baskets (points); MapRoulette for playgrounds/pitches/parking |
| verified | yes |

## Try it

- **Map preview:** none. The licence is `unclear` (NKOD and the ArcGIS item disagree), so no extract is redistributed here.
- **QGIS:** *Layer → Add Layer → Add Vector Layer… → Source type: Protocol: HTTP(S)*, URI `https://services5.arcgis.com/yyjDpIHsxn6gXsED/arcgis/rest/services/opendata_OZP_odpady_kose_b/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=geojson` (all 658 bins, WGS84). Other layers: *Layer → Add Layer → Add ArcGIS REST Server Layer… → New*, URL `https://services5.arcgis.com/yyjDpIHsxn6gXsED/arcgis/rest/services/opendata_MO_detska_hriste_p/FeatureServer` → *Connect*.

## Endpoints
- Koše: https://services5.arcgis.com/yyjDpIHsxn6gXsED/arcgis/rest/services/opendata_OZP_odpady_kose_b/FeatureServer/0 (fields cislo, ulice, druh, objem, typ, globalid)
- Hřiště: .../opendata_MO_detska_hriste_p/FeatureServer/0 (prvky, one record read: "pískoviště, 2x koník, skluzavka, lanový trychtýř, houpačka, herní sestava"; umisteni)
- Sportoviště: .../opendata_MO_sportoviste_p/FeatureServer/0 (povrch, sport)
- Parkoviště: .../opendata_OD_parkoviste_p/FeatureServer/0 and _l

## Notes
- OSM in Jihlava bbox (15.52,49.35,15.66,49.44, Postpass): waste_basket 40 vs 658 in dataset; playground 83 vs 79; pitch 133 vs 38; street lamps 1,421 (already well mapped).
- Main gain: waste baskets (+~600). Playground polygons carry equipment lists → could add playground:* detail but mostly already mapped.
- Needs a written clarification from the city which licence applies (NKOD "no copyright" would make it ok; CC BY-SA would need a waiver).
- Suggested ref: none (objectid/globalid only).
- Wiki pages read: Tag:amenity=waste_basket, Tag:leisure=playground, Tag:leisure=pitch.

## Wiki entry
```
===Jihlava – odpadkové koše a dětská hřiště===
* dataset: odpadkové koše; dětská hřiště; sportoviště
* gestor: [https://opendata.jihlava.cz/ Statutární město Jihlava]
* licence: nejasná – NKOD uvádí „neobsahuje autorská díla“, ArcGIS položka CC BY-SA [https://opendata.jihlava.cz/]
* datové primitivy: body (koše), plochy (hřiště, sportoviště)
* odkaz: https://services5.arcgis.com/yyjDpIHsxn6gXsED/arcgis/rest/services/opendata_OZP_odpady_kose_b/FeatureServer/0
* navržený tag {{tag|amenity|waste_basket}}, {{tag|leisure|playground}}
* poznámka: V OSM je v Jihlavě 40 odpadkových košů oproti 658 v datech města.
```
