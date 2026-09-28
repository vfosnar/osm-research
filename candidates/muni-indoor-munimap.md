# Masarykova univerzita – munimap / Kompas indoor data (rooms, doors, POIs, buildings)

| Field | Value |
|---|---|
| publisher | Masarykova univerzita, Ústav výpočetní techniky (ÚVT MU) – Kompas / munimap / geoportal.muni.cz |
| url | https://maps.muni.cz/arcgis/rest/services/munimap/MapServer (public ArcGIS REST, no auth); apps https://kompas.muni.cz/ , https://www.muni.cz/mapa , https://geoportal.muni.cz/en/online-map-applications/indoor-maps-of-mu-and-virtual-tours |
| format | ArcGIS MapServer query (JSON/GeoJSON, maxRecordCount 10,000) |
| coords | yes (polygons for rooms/doors/buildings, points for POI; outSR=4326 works) |
| records | rooms (mistnosti) 26,535; doors (dvere) 24,124; POI (body_zajmu) 4,365; buildings (budovy) 393; areas (arealy) 40 (+ layers 5/6: 686 / 25). POI types: WC 876, WC muži 749, WC ženy 657, WC invalidé 458, výtah 617, učebna 648, přebalovací pult 33, vstup do budovy 68, knihovna 25, studovna 8, jídelna 9, tiskové centrum 28, informace 43 |
| osm_tags | Simple Indoor Tagging – indoor=room\|corridor\|area + level=* (+ref=room number, name), indoor=door / door=*, amenity=toilets (+wheelchair=yes, male/female), highway=elevator, entrance=*, changing_table=yes, amenity=library, building=university |
| osm_count_cz | indoor=room 1,643; indoor=door 277; indoor (any) 10,249; level 22,086 (taginfo CZ 2026-09-26) |
| license | none stated (MapServer copyrightText empty; no licence on geoportal pages) |
| license_url | n/a |
| license_status | unclear |
| update_freq | continuous (operational passport system of MU) |
| impact | 4 |
| sync_fit | MapRoulette (rooms/doors/buildings drawn from imagery; POI points are 1:N by type) |
| verified | partial |

## Try it
- **Map preview:** no sample, because no licence is stated (`unclear`). Ask ÚVT MU for permission first.
- **QGIS:** *Layer → Add Layer → Add ArcGIS REST Server Layer → New*, URL `https://maps.muni.cz/arcgis/rest/services/munimap/MapServer`. Layers: 0 body_zajmu (POIs), 1 mistnosti (rooms), 2 budovy, 3 dvere, 4 arealy. Filter a floor with an expression on `polohKod`.
- **Web viewer:** https://kompas.muni.cz/

## Notes
- Coverage check (Postpass 2026-09-27): MUNI Bohunice campus (UKB) bbox 16.562,49.172,16.582,49.182 has 7,003 rooms in munimap vs 57 indoor=room (+8 doors) in OSM; city-centre MU buildings bbox 16.590,49.180,16.610,49.200 has 16 indoor=room in OSM. Essentially no indoor data for MU in OSM.
- Attributes: polohKod (stable location code; the value BHA21N02007 was seen in the data and reads as areál/building/floor/room), cislo, ucel_nazev (posluchárna, laboratoř, knihovna, vnější sportoviště…), vychoziPodlazi, nazev/nazevEn, inetId. Floors encoded in polohKod (N01, P01 = podzemní) → map to level=*.
- munimap itself uses OSM as basemap; ÚVT MU develops it (open-source JS library "munimap"). The data is operational facility-management data — needs an explicit permission from MU (ÚVT / Kompas team) before any import; a waiver would ideally cover rooms, doors and POIs.
- Also include the public toilets/wheelchair toilets/elevators (≈3,300 POIs) — highest everyday value for OSM users (routing, accessibility apps).
- Suggested ref: `ref:muni=<polohKod>` (stable, human-meaningful); room numbers → `ref`.
- Other universities checked: VŠB-TUO has a public room API (https://mapy.vsb.cz/maps/api/v0/rooms/<id>?language=cs) giving only room point coordinates + floor, no polygons – low value; ČVUT, VUT, UK, UPOL publish only static PDF/HTML campus maps (no indoor dataset found); Univerzita Karlova NKOD records are statistics, not geodata.
- Wiki pages read: Simple_Indoor_Tagging, Tag:amenity=toilets.

## Wiki entry
```
===Masarykova univerzita – vnitřní mapy (munimap / Kompas)===
* dataset: munimap – místnosti, dveře, body zájmu, budovy
* gestor: [https://geoportal.muni.cz/ Masarykova univerzita, ÚVT]
* licence: neuvedena – nutný souhlas [https://maps.muni.cz/arcgis/rest/services/munimap/MapServer]
* datové primitivy: plochy (místnosti, dveře, budovy), body (WC, výtahy, vstupy)
* odkaz: https://maps.muni.cz/arcgis/rest/services/munimap/MapServer/1
* navržený tag {{tag|indoor|room}}, {{tag|level|1}}, {{tag|amenity|toilets}}, {{tag|highway|elevator}}, {{tag|ref:muni|<polohKod>}}
* poznámka: Na kampusu Bohunice je v OSM 57 místností, munimap jich má přes 7 000.
```
