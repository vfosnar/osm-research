# KVL ČR – mapa veterinárních pracovišť (vet practices, emergency flag, hours, species)

| Field | Value |
|---|---|
| publisher | Komora veterinárních lékařů České republiky (KVL ČR), IČO 44015364, Novoměstská 1965/2, Brno |
| url | https://vetkom.cz/veterinari (map; all markers are embedded in the page as a JS array `var markers = [...]`); detail https://vetkom.cz/veterinari/case:pracoviste/id:&lt;workplaceId&gt; ; list of vets https://vetkom.cz/veterinari/case:seznam (244 pages) |
| format | HTML page with embedded JS objects (no API, no download) |
| coords | yes (lat/lng per workplace, geocoded address) |
| records | 948 workplaces with coordinates (unique workplaceId), fetched 2026-09-28; 142 flagged `pohotovost: 1` (emergency service), 339 with weekly hours, 696 with phone, 465 with website; species focus on 923 (dogs 780, cats 748, small mammals 423, cattle 192, horses 177, zoo animals 29) |
| osm_tags | amenity=veterinary (+ emergency=yes where pohotovost=1), opening_hours, phone, website, name; suggested ref:CZ:kvl=&lt;workplaceId&gt; |
| osm_count_cz | amenity=veterinary 531 (taginfo 2026-09-27; 445 of OSM vets in the CZ bbox have opening_hours, 8 have emergency=*) |
| license | none; page states: "Obsah této „Databáze“ je poskytován pouze pro soukromé použití. Jakékoliv komerční použití, šíření či rozmnožování bez písemného souhlasu KVL ČR je přísně zakázáno." |
| license_url | https://vetkom.cz/veterinari |
| license_status | incompatible (private use only; written consent from KVL ČR would change this) |
| update_freq | live (vets edit their own workplace entries) |
| impact | 3 |
| sync_fit | Sync, if consent is obtained (points, stable workplaceId, 1:1 amenity=veterinary; emergency and hours as update keys) |
| verified | yes |

## Try it
- **Map preview:** none (licence forbids redistribution). Use the publisher's own map.
- **Web viewer:** https://vetkom.cz/veterinari. Filters by workplace type (ambulance/ordinace, klinika, nemocnice, terénní, výjezdní, mobilní služba), species and "Pohotovost".
- **QGIS:** not directly loadable. The page source holds a `var markers = [ … ];` array with `lat`, `lng`, `name`, `address`, `phone1`, `www`, `focus`, `pohotovost`, `workplaceId`, per-day `po_o1…ne_d2` (morning/afternoon hours) and `em_po_o1…` (emergency hours).

## Notes
- **Gap (Postpass 2026-09-28, all amenity=veterinary / healthcare=veterinary in the CZ bbox, 1,050 objects):** only 199 of 948 KVL workplaces (21 %) have an OSM vet within 150 m (185 within 50 m, 223 within 300 m). About 750 practices are missing. Of the 142 emergency-flagged practices, 33 have an OSM vet nearby, and only 8 OSM vets in the whole bbox carry any emergency tag.
- **Not covered elsewhere:** the NRPZS register (uzis-nrpzs-ambulantni.md) covers human healthcare only; vets are not in NRPZS, SÚKL or ZABAGED. No vet source on Cs:Česko/freemap, Cs:Zdroje_v_jednani or in the Sync config (checked 2026-09-28). Taginfo shows the OSM vets were mapped by hand.
- **Coverage caveat:** the map is opt-in. It shows 948 workplaces while the list has 244 pages of individual vets, and some cities are thin (63 workplaces with a Praha address, 53 in Brno). OSM also has vets that are not in KVL, so this would add to OSM, not replace it.
- **Data caveats:** 59 workplaces share coordinates with another one (the same clinic listed under two operators or vets). "Terénní / výjezdní / mobilní" services have no public premises and should be filtered out; the marker array has no type field, so the type must be read from the detail page ("Údaje o pracovišti"). Personal names of sole-practitioner vets are the business name, as in NRPZS.
- **Tagging:** Tag:amenity=veterinary lists opening_hours and `emergency=yes` "if an animal hospital is staffed for emergency patients", which matches the KVL `pohotovost` flag. Wiki pages read: Tag:amenity=veterinary (also exists as Cs:Tag:amenity=veterinary).
- **Licence / contact:** KVL ČR is a public-law professional chamber (zákon 381/1991 Sb.). The terms forbid distribution without written consent, so an OSM import needs an explicit written permission. Contact: vetkom@vetkom.cz, secretariat 549 256 407. The chamber's interest (pet owners finding emergency vets) aligns with OSM, which makes a consent request plausible.

## Wiki entry
```
===KVL ČR – veterinární pracoviště===
* dataset: Mapa veterinárních pracovišť
* gestor: [https://vetkom.cz/ Komora veterinárních lékařů České republiky]
* licence: pouze pro soukromé použití, šíření jen s písemným souhlasem KVL ČR [https://vetkom.cz/veterinari]
* datové primitivy: body
* odkaz: https://vetkom.cz/veterinari
* navržený tag {{tag|amenity|veterinary}}, {{tag|emergency|yes}}, {{tag|ref:CZ:kvl|<workplaceId>}}
* poznámka: z 948 pracovišť KVL má v OSM do 150 m veterinu jen 199; ze 142 pracovišť s pohotovostí 33; nutný písemný souhlas KVL
```
