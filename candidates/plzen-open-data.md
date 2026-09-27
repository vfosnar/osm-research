# opendata.plzen.eu – pasport stromů, světelná místa, WC, cyklostojany, WiFi, umělecká díla, přístřešky MHD, parkoviště

| Field | Value |
|---|---|
| publisher | Statutární město Plzeň (Správa informačních technologií města Plzně, SITmP) |
| url | https://opendata.plzen.eu/ |
| format | ZIP per format (GeoJSON, KML, SHP, DXF, DGN) at https://opendata.plzen.eu/public/opendata/download-file/&lt;id&gt; |
| coords | yes (WGS84 in GeoJSON/KML; many layers are cartographic symbols → polygons/GeometryCollections, need centroid) |
| records | trees 48,354 (unique ID_STR); street-light points 24,389 (22,994 lamp on pole, 484 on building, 164 crossing lights…); WC 71 (67 "vlídné WC" in businesses + 4 public); lockable bike stands 497 KML placemarks; WiFi 116 coverage polygons; artworks/monuments 397 (KOD P…); MHD shelters 368 (ID_PRIS); parking 120 polygons |
| osm_tags | natural=tree; highway=street_lamp (+lamp_mount); amenity=toilets (+toilets:access=customers for "vlídné WC"); amenity=bicycle_parking; tourism=artwork / historic=memorial / historic=wayside_shrine; amenity=shelter + shelter_type=public_transport (or shelter=yes on the stop); amenity=parking; internet_access=wlan |
| osm_count_cz | natural=tree 136,307; highway=street_lamp 62,220; amenity=toilets 3,315; amenity=bicycle_parking 13,650; tourism=artwork 12,102 (taginfo CZ 2026-09-26) |
| license | NKOD terms: "neobsahuje autorská díla", "není autorskoprávně chráněnou databází", "není chráněna zvláštním právem pořizovatele databáze" (skos:narrowMatch CC0); talk-cz 2019 announcement also states CC0 |
| license_url | https://data.gov.cz/podmínky-užití/neobsahuje-autorská-díla/ ; https://data.gov.cz/podmínky-užití/není-chráněna-zvláštním-právem-pořizovatele-databáze/ |
| license_status | ok |
| update_freq | trees and street lights CONT (files regenerated; WC file dated 2026-08-04); others IRREG |
| impact | 5 |
| verified | yes |

## Try it

- **Map preview:** [samples/plzen-open-data-stromy.geojson](../samples/plzen-open-data-stromy.geojson) (1,909 trees with `ref:plzen:strom`) and [samples/plzen-open-data-lampy.geojson](../samples/plzen-open-data-lampy.geojson) (1,774 light points, `lamp_mount` from `OBJEKT`), both for the city centre, bbox 13.365,49.740–13.385,49.752. The source draws each object as a symbol polygon, so the samples use the centre of each symbol's bounding box.
- **QGIS:** download `https://opendata.plzen.eu/public/opendata/download-file/405` (trees, 13 MB ZIP holding `stromy.geojson`, 113 MB, WGS84) or `…/download-file/370` (street lights, 17 MB ZIP holding `svetelnamista.geojson`), then drag the ZIP into QGIS or use *Layer → Add Layer → Add Vector Layer… → File*. Expect symbol polygons and GeometryCollections; run *Vector → Geometry Tools → Centroids* to get points.

## Layers verified (download ids are GeoJSON zips unless noted)

| layer | NKOD dataset | download | records | OSM in Plzeň bbox 13.26,49.68,13.47,49.80 (Postpass) |
|---|---|---|---|---|
| Pasport stromů | .../00075370/839a48f8de3046298e118ecf2b2f1… | download-file/405 | 48,354 (ID_STR unique) | natural=tree 8,897 |
| Světelná místa | .../00075370/761b56fa3a94dbf8527f7250ff11a… | download-file/370 | 24,389 (OBJEKT type) | highway=street_lamp 1,663 |
| WC | .../00075370/4bbdb0c48189650fa7bae75ef326fd52 | download-file/390 | 71 (NAZEV, ADRESA) | amenity=toilets 80 |
| Uzamykatelné stojany (cyklostojany) | .../00075370/ef6762e856c5f1119a83404… | download-file/188 (KML; the GeoJSON 187 is malformed JSON) | 497 placemarks (OBJEKT, POCET, ADRESA, UMISTENI; duplicate points per rack) | amenity=bicycle_parking 339 |
| WiFi | .../00075370/aa9440be1d10513128f18de89cd28391 | download-file/68 | 116 coverage polygons (one read: "WIFI4EU Plzen 9", venkovní, SITmP) | internet_access=wlan 254 (all objects) |
| Umělecká díla | .../00075370/8fdb98b57bb034cdac631b2cdffc87da | download-file/137 (KML; GeoJSON 136 malformed – unescaped quotes) | 397 (KOD, NAZEV, LOKALITA) | memorial/shrine/cross/artwork 798 |
| Přístřešky MHD | .../00075370/669396148f94af7ffaca8d642856c07d | download-file/3 | 368 (ID_PRIS, TYP A–G, INFO) | shelter 447 |
| Parkoviště | .../00075370/05cd91577a4b867c5ec9281d96d2e83f | download-file/166 | 120 polygons (TYP) | amenity=parking 2,148 (low value) |

## Notes
- Highest value: trees (48k vs 8.9k; existing OSM trees mostly without source → spatial conflation) and street lights (24k vs 1.7k).
- Geometry is exported from a CAD/MicroStation cartographic model: point features come as symbol polygons or GeometryCollections of LineStrings. Take the centroid; test positional accuracy against the city's orthophoto (Plzeň ortofoto 2024 already has consent, see Cs:Česko/freemap).
- Tree layer has no species/genus attribute in the export (only RC "Pasportizovaný strom" + ID_STR) → imports would be bare natural=tree; still the geometry is surveyed.
- Street lights: OBJEKT tells lamp_mount-like info ("lampa na stožáru" → keep bare highway=street_lamp, mast shape unknown; "lampa na objektu" → lamp_mount=wall; "lampa na převěsu" → lamp_mount=suspended; "Zemní světlo" has no documented lamp_mount value (ground used 3× in CZ) — values per Key:lamp_mount wiki and CZ taginfo). The file dated 2026-08-04 does export a pole number `CISLO` (21,880 of 24,389 filled, no duplicates, checked 2026-09-27) → usable as `ref`.
- WC: 67 of 71 are "vlídné WC" (restaurants letting public use toilets) — tag toilets on the business POI (toilets=yes + toilets:access=customers/yes per Tag:amenity=toilets) rather than separate nodes.
- Artworks overlap with drobnepamatky.cz (already in Sync) — use only to add missing items/ref.
- Earlier discussed on talk-cz (2019-04 "Nová otevřená data v Plzni", Pavel Cvráček: WC, cyklostojany, kontejnery, parkovací automaty; CC0) but no import followed and it is not listed on Cs:Česko/freemap.
- Suggested ref keys: `ref:plzen:strom=<ID_STR>`, `ref:plzen:pristresek=<ID_PRIS>`; none in use yet.
- Contact: SITmP, opendata.plzen.eu (portal "Kontakt").
- Wiki pages read: Tag:natural=tree, Tag:highway=street_lamp, Tag:amenity=toilets, Tag:amenity=bicycle_parking, Tag:tourism=artwork, Tag:amenity=shelter, Key:internet_access, Tag:amenity=parking.

## Wiki entry
```
===Plzeň – pasport stromů, veřejné osvětlení, WC, cyklostojany===
* dataset: Pasport stromů; Světelná místa; WC; Uzamykatelné stojany; Umělecká díla; Přístřešky MHD
* gestor: [https://opendata.plzen.eu/ Statutární město Plzeň (SITmP)]
* licence: bez autorskoprávní ochrany, dle NKOD ekvivalent CC0 [https://data.gov.cz/podmínky-užití/neobsahuje-autorská-díla/]
* datové primitivy: body (symboly jako polygony – nutný centroid), plochy (WiFi, parkoviště)
* odkaz: https://opendata.plzen.eu/public/opendata/download-file/405
* navržený tag {{tag|natural|tree}}, {{tag|highway|street_lamp}}, {{tag|amenity|toilets}}, {{tag|amenity|bicycle_parking}}, {{tag|ref:plzen:strom|<ID_STR>}}
* poznámka: V OSM je v Plzni ~8 900 stromů a ~1 700 lamp oproti 48 354 stromům a 24 389 světelným místům v pasportu.
```
