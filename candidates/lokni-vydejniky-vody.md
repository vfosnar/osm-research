# LOKNI – filtered drinking-water dispensers (stations, universities)

| Field | Value |
|---|---|
| publisher | LOKNI (operator of the LOKNI dispenser network and app, https://www.lokni.cz/) |
| url | https://api.lokni.cz/api/v1/automats/in-map (JSON behind the map at https://www.lokni.cz/pro-verejnost/) |
| format | JSON array (`_id`, `name1` = institution, `name2` = building, `location` = where inside, `locationEN`, `address`, `coords.lat/lon`, `fmTypePerTariff`) |
| coords | yes (WGS84) |
| records | 102 dispensers: 71 "sponsored" (partner-funded, up to 3 l a day free through the app, per the LOKNI web page), 30 "free", 1 "paid". Hosts: Správa železnic stations 13, VŠE 10, ČVUT 10, UK 9, MUNI 7, VUT 7, SLU 5, TUL 5, and other universities |
| osm_tags | amenity=drinking_water + indoor=yes + brand=LOKNI + level/description from `location` (wiki Tag:amenity=drinking_water) |
| osm_count_cz | brand=Lokni 1 (taginfo 2026-09-26); 7 of 102 dispensers have any drinking-water object within 50 m (Postpass 2026-09-27) |
| license | none stated |
| license_url | |
| license_status | unclear |
| update_freq | live (the API feeds the app) |
| impact | 2 |
| verified | yes |

## Try it
- **Map preview:** none (licence unclear). Web map: https://www.lokni.cz/pro-verejnost/.
- **QGIS:** convert first:
  `curl -sS https://api.lokni.cz/api/v1/automats/in-map | jq -r '.[] | [._id,.name1,.name2,.location,.address,.coords.lat,.coords.lon,.fmTypePerTariff] | @csv' > lokni.csv`
  (tested: 102 rows). Then *Layer → Add Layer → Add Delimited Text Layer*, no header, X field = field_7, Y field = field_6, CRS EPSG:4326.

## Notes
- **Gap:** 95 of 102 dispensers are missing in OSM. They are indoor points at railway stations (13 Správa železnic stations, among them Praha hlavní nádraží, Ostrava hlavní nádraží, Olomouc, Plzeň, Hradec Králové) and in university buildings and dormitories. Travellers and students look for exactly this kind of point.
- `_id` looks like a device address (10.8.0.x). It is unique in the feed but may change if hardware is swapped. Use it as `ref:lokni` only if the operator confirms it is stable.
- Access is limited: the user must activate the dispenser in the LOKNI app, and the free amount depends on the tariff (the web page says up to 3 l a day free at sponsored stations, and shows 0.5 l a day for the basic tariff). Record this in `description` and do not tag fee=no without checking the app terms. Dispensers inside dormitories may not be public; check `location` and use access=customers or access=private where needed.
- Tagging is debatable. amenity=drinking_water fits a free water point. The alternative amenity=vending_machine + vending=water (wiki Tag:vending=water) fits the one "paid" unit.
- **Licence:** no terms on the API or web page. Ask LOKNI (contact via https://www.lokni.cz/) for consent. The operator gains visibility in OSM-based apps, which is a good argument.
- Wiki pages read: Tag:amenity=drinking_water, Key:drinking_water:refill, Tag:vending=water.

## Wiki entry
```
===LOKNI – výdejníky pitné vody===
* dataset: mapa výdejníků vody LOKNI
* gestor: [https://www.lokni.cz/ LOKNI]
* licence: neuvedena, nutné vyžádat souhlas
* datové primitivy: body
* odkaz: https://api.lokni.cz/api/v1/automats/in-map
* navržený tag {{tag|amenity|drinking_water}} + {{tag|indoor|yes}} + {{tag|brand|LOKNI}}
* poznámka: 95 ze 102 výdejníků (nádraží, univerzity) v OSM chybí; aktivace přes aplikaci, na sponzorovaných stanicích až 3 l denně zdarma
```
