# Textile collection containers – KlokTex and Potex container maps

| Field | Value |
|---|---|
| publisher | KlokTex (charity textile collection linked to KLOKTEX help nadační fond, Křižovnická 86/6, Praha 1; web https://www.kloktex.cz/); Potex (textile collection for charities, web https://potex.cz/) |
| url | KlokTex: https://www.kloktex.cz/mapa-kontejneru/ (all markers inline in the page as `mapData[i]=new Array(...)`, windows-1250); Potex: https://potex.cz/api/apps/699c2619e852e37d40e7c4a2/entities/ContainerLocation?limit=10000 (anonymous JSON, Base44 app backend) |
| format | KlokTex: JavaScript arrays in HTML (town, street + note, marker icon, detail URL, lon, lat, active flag, container type code); Potex: JSON array (`id`, `address`, `district`, `lat`, `lng`, `active`, `note`, `updated_date`) |
| coords | yes (WGS84) |
| records | KlokTex 1,192 containers (665 type M-Z small green, 362 M-M small blue, 18 V-Z large green, rest other colours), from Plzeň and Chodov to Liberec and Čelákovice, bbox 12.81–15.18 E, 49.69–50.82 N; Potex 271 containers, all in Prague and its ring (Praha 8: 35, Praha 11: 30) |
| osm_tags | amenity=recycling + recycling_type=container + recycling:clothes=yes (+ recycling:shoes=yes where accepted) + operator=KlokTex / Potex. Wiki Tag:amenity=recycling (approved; lists `operator`), Key:recycling:clothes (de facto, "whether there are clothes accepted for recycling (including shoes)"), Key:recycling_type |
| osm_count_cz | taginfo Geofabrik CZ (2026-09-28): recycling:clothes=yes 4,564. In the 2026-09-27 Czechia extract 88 clothes containers carry operator=KlokTex, 19 Potex, 6 POTEX |
| license | none stated on either site |
| license_url | none |
| license_status | unclear |
| update_freq | KlokTex: live list from the operator's CMS (all 1,192 flagged active); Potex: records created 2026-02, maintained in the operator's app |
| impact | 3 |
| sync_fit | Sync (points, one category → fixed tags amenity=recycling + recycling_type=container + recycling:clothes=yes + operator; stable IDs: KlokTex detail-page slug, Potex 24-hex id) |
| verified | yes |

## Try it
- **Map preview:** none (licence unclear).
- **Web viewer:** https://www.kloktex.cz/mapa-kontejneru/ (Google Maps; each container also has a detail page
  such as https://www.kloktex.cz/mapa/kobylisy-siskova-1223-23), https://potex.cz/FindContainer.
- **QGIS (Potex):** the URL
  `https://potex.cz/api/apps/699c2619e852e37d40e7c4a2/entities/ContainerLocation?limit=10000` returns a plain
  JSON array (tested 2026-09-28: 271 objects), not GeoJSON. Convert it to CSV
  (`python3 -c "import json,csv,sys;d=json.load(sys.stdin);w=csv.writer(sys.stdout);[w.writerow([o['id'],o['address'],o['district'],o['lng'],o['lat']]) for o in d]"`),
  then *Layer → Add Layer → Add Delimited Text Layer*, delimiter comma, X = column 4, Y = column 5, EPSG:4326.
- **QGIS (KlokTex):** no machine endpoint; the page must be parsed. One line of Python turns it into CSV:
  `re.findall(r'mapData\[(\d+)\]=new Array\("(.*?)","(.*?)", "(.*?)", "(.*?)", "(.*?)", "(.*?)","(.*?)","(.*?)"\);', html)`
  (fields: index, town, address + note, icon, detail path, lon, lat, active, type); decode as cp1250.

## Notes
Gap analysis is a local match against the 2026-09-27 Czechia extract (amenity=recycling objects):

- **KlokTex:** 869 of 1,192 containers (73 %) have no amenity=recycling with recycling:clothes=yes within 50 m;
  323 match (median 6 m). For 214 of the 869 there is an amenity=recycling within 30 m that lacks the clothes
  attribute (typically the sorting point next to which the container stands), so the fix is often adding
  `recycling:clothes=yes` and `operator` rather than a new node. Worst towns: Kladno 53 of 56 missing, Česká Lípa
  29, Teplice 27, Děčín 23, Louny 14, Neratovice 14. In the Prague bbox 296 of 440 are missing.
- **Potex:** 153 of 271 (56 %) missing, 118 matched (median 4 m); 37 of the missing sit within 30 m of an
  amenity=recycling without the clothes attribute.
- Sync already carries Prague's recycling points (`group.prague_opendata.dataset.recycling`, source
  `prague_recycling`), but its `create_keys` are only amenity, recycling_type, ref and ref:ipr, so textile
  containers of charity operators are not covered by it.
- IDs: KlokTex detail slugs are unique for 1,189 of 1,192 entries (one slug repeated three times); Potex ids are
  unique. Suggested keys `ref:kloktex` (slug) and `ref:potex` (id). The KlokTex notes give access
  restrictions ("uvnitř areálu MŠ") that belong in `access=customers`/`description`.
- Other operators checked: Diakonie Broumov publishes 889 containers only as an address table; 752 of them
  were placed on RÚIAN address points, see diakonie-broumov-kontejnery.md. TextilEco
  (https://textil-eco.cz/vyhledat-kontejner) redirects to a page for municipalities with no map; TextilEco is the
  former REVENGE, a.s. (per the Olomouc city news https://www.olomouc.eu/aktualni-informace/aktuality/13454), and
  revenge.cz no longer resolves (2026-09-28), so Revenge is not a separate source. Klokánek (klokanek.cz) still returns
  HTTP 502 (retried 2026-09-28), so whether it runs its own containers or shares the KlokTex network could not be
  checked. Dimatex (https://www.dimatex.cz/) has no public container
  map.
- Arnika's "Udržitelná Šestka" (https://arnika.org/udrzitelna-sestka) is a Mapotic map
  (https://www.mapotic.com/api/v1/maps/19589/pois.geojson/, map "Praha 6 textil", Mapotic terms as in
  mapotic-outdoor-small-maps.md) with 44 textile containers and 9 second-hand shops in Prague 6, last edited
  2024-09. 18 of the 44 containers have an OSM recycling:clothes=yes object within 50 m (Postpass, 2026-09-28), so
  26 are missing; too small for its own candidate, but a ready survey list for Prague 6.
- Contacts: KlokTex kloktex@kloktex.cz, tel. +420 608 958 030; Potex via https://potex.cz/Contact. Both are
  charity-linked operators that benefit from people finding their containers, so a consent for OSM is plausible.

## Wiki entry
```
===Kontejnery na textil – KlokTex a Potex===
* dataset: mapa kontejnerů KlokTex; vyhledávač kontejnerů Potex
* gestor: [https://www.kloktex.cz/ KlokTex], [https://potex.cz/ Potex]
* licence: neuvedena, nutno požádat o souhlas
* datové primitivy: body
* odkaz: https://www.kloktex.cz/mapa-kontejneru/ ; https://potex.cz/api/apps/699c2619e852e37d40e7c4a2/entities/ContainerLocation?limit=10000
* navržený tag {{tag|amenity|recycling}}, {{tag|recycling_type|container}}, {{tag|recycling:clothes|yes}}, {{tag|operator|KlokTex}}, {{tag|ref:kloktex|<slug>}}
* poznámka: 869 z 1 192 kontejnerů KlokTex a 153 z 271 kontejnerů Potex nemá v OSM do 50 m sběrné místo s recycling:clothes=yes
```
