# nextbike Czech Republic – GBFS station_information (45 systems)

| Field | Value |
|---|---|
| publisher | nextbike Czech Republic s.r.o. (feed hosted by nextbike GmbH, gbfs.nextbike.net) |
| url | https://gbfs.nextbike.net/maps/gbfs/v2/&lt;system_id&gt;/en/station_information.json (e.g. .../nextbike_tg/... Praha, nextbike_te Brno, nextbike_to Ostrava); list of 45 CZ system_ids in https://raw.githubusercontent.com/MobilityData/gbfs/master/systems.csv |
| format | GBFS 2.3 JSON |
| coords | yes |
| records | 4,181 stations across 45 CZ systems (Praha 1,580, Ostrava 434, Brno 332, Mladoboleslavsko 145, Hradec Králové 141, Frýdek-Místek 130, …); 3 flagged is_virtual_station |
| osm_tags | amenity=bicycle_rental + bicycle_rental=docking_station\|dropoff_point, network=nextbike, operator=nextbike Czech Republic, ref=&lt;short_name&gt;, capacity |
| osm_count_cz | amenity=bicycle_rental 610 (taginfo 2026-09-26); in the CZ bbox 123 objects have operator "nextbike Czech Republic…" |
| license | CC0-1.0 (system_information.json license_id, checked for nextbike_tg, _te, _to, _zs) |
| license_url | https://gbfs.nextbike.net/maps/gbfs/v2/nextbike_tg/en/system_information.json (license_id field); https://creativecommons.org/publicdomain/zero/1.0/ |
| license_status | ok |
| update_freq | real-time (ttl 60 s); station list changes as the operator adds or removes stations |
| impact | 3 |
| verified | yes |

## Notes
- **Gap:** only 308 of the 4,181 nextbike stations have any OSM amenity=bicycle_rental within 30 m (Postpass, CZ bbox, 2026-09-27). That leaves about 3,870 stations unmapped.
- **Stable IDs:** station_id is a numeric id, for example 171152709. short_name (for example 49306) is the station number shown to users, and every station has one. Use ref=<short_name>, or introduce ref:nextbike=<station_id>. ref:nextbike has 84 uses worldwide (taginfo.openstreetmap.org) and no CZ convention.
- **Important caveat (Tag:amenity=bicycle_rental wiki):**
  - "Do not add virtual dropoff locations to OpenStreetMap". Only signposted or marked spots qualify, as bicycle_rental=dropoff_point, and docks qualify as docking_station.
  - Most CZ nextbike stations are dockless spots. 2,806 stations have capacity < 5, and many have 0.
  - A blind import is therefore not appropriate. Use it as a sync/review layer in Sync, with import only of stations whose signage is confirmed (street-level imagery or survey), or ask nextbike CZ for a flag marking signposted stations.
  - This limits the impact to 3, even though the licence is clean.
- **Wiki pages read:** Tag:amenity=bicycle_rental (bicycle_rental=docking_station / dropoff_point, ref, capacity, network).
- Rekola, Bolt and Lime publish no CZ GBFS in the MobilityData catalogue (systems.csv), so nextbike is the only one.
- Contact: gbfs@nextbike.net (feed_contact_email); servis@nextbikeczech.com.

- Prague detail (from the Prague research pass, 2026-09-27): 1,580 nextbike stations in Prague, all
  `is_virtual_station=false` in the feed, versus only 11 `amenity=bicycle_rental` in OSM Prague (3 of them
  nextbike). Prague stations are mostly ordinary bike racks marked in the app, so a field check is needed
  before adding them.

## Wiki entry
```
===nextbike GBFS===
* dataset: GBFS station_information (45 systémů nextbike v ČR)
* gestor: [https://www.nextbikeczech.com/ nextbike Czech Republic]
* licence: CC0 1.0 [https://creativecommons.org/publicdomain/zero/1.0/]
* datové primitivy: body
* odkaz: https://gbfs.nextbike.net/maps/gbfs/v2/nextbike_tg/en/station_information.json
* navržený tag {{tag|amenity|bicycle_rental}}, {{tag|bicycle_rental|dropoff_point}}, {{tag|network|nextbike}}, {{tag|ref|<short_name>}}
* poznámka: z 4 181 stanic nextbike je v OSM do 30 m jen ~300; importovat jen značená stanoviště (wiki zakazuje virtuální)
```
