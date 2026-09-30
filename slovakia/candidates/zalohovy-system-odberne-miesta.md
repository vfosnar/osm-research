# Správca zálohového systému – return points for deposit bottles and cans (zálohomaty)

| Field | Value |
|---|---|
| publisher | Správca zálohového systému, n. o. (the national deposit-return operator), site slovenskozalohuje.sk |
| url | POST https://slovenskozalohuje.sk/wp-admin/admin-ajax.php with form fields `action=mmp_map_markers`, `type=map`, `id=1,2,3,4,5,10` (Maps Marker Pro backend of https://slovenskozalohuje.sk/mapa-odbernych-miest/) |
| format | JSON: a wrapper object whose `data` member is a GeoJSON FeatureCollection |
| coords | yes (WGS84 points) |
| records | 3,448 return points (2026-09-30). Layer ids: 4 = automated return (reverse vending machine) 2,603; 5 = manual return at the till 820; 10 = alternative collection (festival and mountain bins, Štrbské Pleso and similar) 25. Also 2 = mandatory return point 1,248 and 3 = voluntary return point 2,175. |
| osm_tags | automated: amenity=vending_machine + vending=bottle_return, recycling:plastic_bottles=yes, recycling:cans=yes, operator=&lt;shop operator&gt;; manual: no established tag (see notes) |
| osm_count_sk | vending=bottle_return 60; recycling_type=reverse_vending_machine 0; recycling:plastic_bottles=yes 217 (taginfo SK, 2026-09-30) |
| license | none stated (site footer "Slovensko Zálohuje ©") |
| license_url | https://slovenskozalohuje.sk/mapa-odbernych-miest/ |
| license_status | unclear |
| update_freq | bulk reloads. All 3,448 markers carry published = modified = 27 Sep 2026 12:00, so the whole list is re-imported at once. |
| impact | 5 |
| sync_fit | MapRoulette (the marker ids are regenerated on each reload, so there is no stable ref for Sync; a mapper places the machine inside the right shop) |
| verified | yes |

## Try it

- **Map preview:** none, because the licence is unclear, so no extract is redistributed here.
- **QGIS:** the backend needs a POST, so save the GeoJSON with curl first (tested 2026-09-30, 3,448 features):
  ```
  curl -s https://slovenskozalohuje.sk/wp-admin/admin-ajax.php -d action=mmp_map_markers -d type=map -d id=1,2,3,4,5,10 | python3 -c "import json,sys;json.dump(json.load(sys.stdin)['data'],open('zaloh.geojson','w'))"
  ```
  Then *Layer → Add Layer → Add Vector Layer…* → `zaloh.geojson` (EPSG:4326). The `maps` attribute is a list of layer ids. Filter on it with `array_contains("maps",'4')` for the automated machines.
- **Web viewer:** https://slovenskozalohuje.sk/mapa-odbernych-miest/

## Notes

- **What it is:** Slovakia has had a deposit on PET bottles and cans since 2022. Every shop above a size threshold must take the containers back ("povinný odber"), and smaller shops can join voluntarily. The operator's map is the only national list of return points. There is no dataset in the national catalogue (SPARQL for "zálohov" on data.slovensko.sk, 2026-09-30, returned nothing) and no ATP spider.
- **Gap:**
  - OSM has 60 `vending=bottle_return` objects in the whole of Slovakia, against 2,603 automated return points.
  - Postpass spatial check on 2026-09-30: of 400 random automated points, 15 have a `vending=bottle_return` (or `recycling_type=reverse_vending_machine`) object within 75 m. That is 3.75 %, so **about 2,500 machines are missing**.
  - 340 of the same 400 points (85 %) have an OSM `shop=*` within 75 m, so in most cases the host shop is already mapped and only the machine node is missing.
  - This is the largest single POI gap found in this theme.
- **Fields:** `id` (Maps Marker Pro marker id, 24031–27478), `name` (shop name as registered, for example "CBA VEREX PJ 026", "BILLA", "LIDL", "SM …", "MIX …" for COOP Jednota shops), `address` (street, postcode, town), `maps` (layer ids). `popup` is empty. No opening hours and no machine type.
- **Names are chain-heavy:** "SM" (546), "MIX" (379) and "J" (325) are COOP Jednota formats, then Lidl 186, Billa 186, Milk-Agro 173 and Kaufland 88. The machine usually sits inside or at the entrance of an existing OSM shop, so a mapper confirms the shop and adds a machine node.
- **Stable id:** none. The ids run 24031–27478 with one publish timestamp, which means the list was bulk re-imported on 27 Sep 2026 and the ids will change at the next reload. Use `name` + `address` for matching. Ask the operator whether an internal return-point id (the registration number of the "odberné miesto") can be published.
- **Tagging:**
  - Tag:vending=bottle_return (wiki, raw, read 2026-09-30) needs `amenity=vending_machine` and lists `recycling:cans`, `recycling:plastic_bottles` and `payment:token` (a voucher redeemed at the till, which is how Slovak machines pay out).
  - Tag:amenity=recycling lists `recycling_type=reverse_vending_machine`. Its own page says that tag started with one undiscussed import in April 2026 and that `vending=bottle_return` is the current method, so propose the vending tag.
  - Manual return at the till has no tag of its own. It could be recorded on the shop, but that needs a community decision in `osm_sk` before anyone adds it.
- **ZBGIS:** the catalogue (KTO ZBGIS) has no object type for return points or vending machines. The only related content is the building use "Obchod".
- **Contact:** Správca zálohového systému, n. o. (contact form at https://slovenskozalohuje.sk/kontakt/, customer line 0907 900 400).

## Wiki entry

```
=== Odberné miesta zálohového systému ===
* dataset: mapa odberných miest zálohovaných obalov (PET fľaše, plechovky)
* správca: [https://slovenskozalohuje.sk/ Správca zálohového systému, n. o.]
* licencia: neuvedená – potrebný súhlas [https://slovenskozalohuje.sk/mapa-odbernych-miest/]
* dátové primitívy: body
* odkaz: https://slovenskozalohuje.sk/wp-admin/admin-ajax.php (POST action=mmp_map_markers, type=map, id=1,2,3,4,5,10)
* navrhované značky: {{tag|amenity|vending_machine}}, {{tag|vending|bottle_return}}, {{tag|recycling:plastic_bottles|yes}}, {{tag|recycling:cans|yes}}
* poznámka: 2 603 automatov na vrátenie obalov, v OSM je na Slovensku 60 objektov vending=bottle_return (9/2026).
```
