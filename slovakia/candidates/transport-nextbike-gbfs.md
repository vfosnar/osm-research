# nextbike bike-share stations in Slovakia (GBFS, CC0)

| Field | Value |
|---|---|
| publisher | nextbike GmbH feeds for the Slovak systems: nextbike Bratislava and Bajk Trnavskej župy (operator nextbike Czech Republic), BikeKIA Žilina, nextbike Senec and Senica bajk (operator ARRIVA Slovakia a.s.) |
| url | `https://gbfs.nextbike.net/maps/gbfs/v2/nextbike_<id>/en/station_information.json` for `<id>` = `bi` (Bratislava), `zu` (Piešťany, Vrbové, Krakovany, Trebatice), `ak` (Žilina), `as` (Senec), `av` (Senica); discovery via `https://gbfs.nextbike.net/maps/gbfs/v2/nextbike_bi/gbfs.json` and the MobilityData systems list |
| format | GBFS 2.3 JSON |
| coords | yes |
| records | 599 stations: Bratislava 445, Trnava region 66, Žilina 39, Senica 26, Senec 23 (fetched 30 Sep 2026) |
| osm_tags | `amenity=bicycle_rental`, `bicycle_rental=dropoff_point` (virtual stations, 573) or `docking_station` (Senica, 26), `network=<system name>`, `operator`, `ref=<short_name>`, `capacity` where given, `name` |
| osm_count_sk | `amenity=bicycle_rental` 701 (taginfo, 29 Sep 2026). In the bbox 16.9–18.2 E / 47.9–48.8 N, Postpass (30 Sep 2026) returns 278 rental objects: `network=Slovnaft Bajk` 101, `WhiteBikes Bratislava` 58, `Arboria Bike` 51, `nextbike` 26, no network 38. Only 82 of the 445 Bratislava stations, 1 of 66 Trnava-region and 0 of 23 Senec stations have any rental object within 50 m; the 39 Žilina (BikeKIA) stations are all mapped with `ref` |
| license | CC0 1.0 (`license_id: CC0-1.0` in each system's `system_information.json`) |
| license_url | https://gbfs.nextbike.net/maps/gbfs/v2/nextbike_bi/en/system_information.json |
| license_status | ok |
| update_freq | live (feed `ttl` 60 s); the station list changes as operators add stations |
| impact | 3 |
| sync_fit | Sync: points, stable `station_id` and short `ref`, category maps 1:1 to `amenity=bicycle_rental` (+ `bicycle_rental` by `is_virtual_station`); a GBFS→FeatureCollection adapter is trivial |
| verified | yes |

## Try it

- **Map preview:** [../samples/transport-nextbike-gbfs.geojson](../samples/transport-nextbike-gbfs.geojson) has all 599 Slovak stations with proposed tags. `osm_rental_within_50m=false` marks the 451 with no OSM rental object nearby.
- **QGIS:** GBFS is not GeoJSON. Use the sample, or convert with a two-line script: `data.stations[]` has `lat`, `lon`, `name`, `short_name`, `station_id`, `is_virtual_station`, `capacity`.
- **Web:** station map in the nextbike app; operator site https://nextbikeslovakia.com

## Notes

- Gap: about 451 of 599 stations have no OSM counterpart: roughly 363 in Bratislava, 65 in the Trnava region, 23 in Senec. nextbike Bratislava is a separate, operator-run network ("Bratislava je next level" on nextbikeslovakia.com). The 101 OSM stations tagged `network=Slovnaft Bajk` (plus 2 as `Slovnaft BAjk`) belong to the city's Slovnaft BAjk system, launched in 2018. I did not verify whether it still runs alongside nextbike or has been replaced, so check before touching those objects. Some of them sit at the same spots as nextbike stations (48 nextbike stations have a non-WhiteBikes rental object within 50 m). The city's open dataset "Slovnaft BAjk – lokalizácia výpožičných staníc" on data.bratislava.sk (CC BY 4.0, last modified 2024-07-09) still describes the old system; the download returned "file is being generated" on 30 Sep 2026.
- Not AllThePlaces: the ATP run of 2026-09-26 has no nextbike features for Slovakia (SK split of `_insights.json`: only Ionity and GreenWay in the mobility domain). Nor is it in the Czech Sync config.
- Most Slovak nextbike stations are virtual (a painted or signed zone, `station_area` polygon about 30 m wide), which fits `bicycle_rental=dropoff_point` per the wiki page Tag:amenity=bicycle_rental. Map them only where signage exists. Senica's 26 are physical docks with `capacity`.
- `ref`: the feed's `short_name` (`23010`, `5320`) is the number shown on station signs and in the app. `station_id` is the internal ID; keep it for Sync matching or as `ref:nextbike`, subject to community agreement.
- Known and not proposed: WhiteBikes Bratislava (Cyklokoalícia import 2017, `whitebikes.info/gbfs.json`). Dott scooters (19 Slovak cities in the MobilityData list) are free-floating and have nothing to map.
- Contact: nextbike Slovakia, servis@nextbikeslovakia.com (from `system_information.json`); feed contact gbfs@nextbike.net.

## Wiki entry

```
=== Stanice zdieľaných bicyklov nextbike (GBFS) ===
* dataset: GBFS station_information systémov nextbike Bratislava, Bajk Trnavskej župy, BikeKIA, nextbike Senec, Senica bajk
* správca: [https://nextbikeslovakia.com/ nextbike Slovakia / ARRIVA Slovakia]
* licencia: CC0 1.0 [https://gbfs.nextbike.net/maps/gbfs/v2/nextbike_bi/en/system_information.json]
* dátové primitívy: body
* odkaz: https://gbfs.nextbike.net/maps/gbfs/v2/nextbike_bi/en/station_information.json
* navrhované značky: {{tag|amenity|bicycle_rental}}, {{tag|bicycle_rental|dropoff_point}}, {{tag|network|nextbike Bratislava}}, {{tag|ref|<short_name>}}
* poznámka: 599 staníc, z toho asi 451 (hlavne v Bratislave, Piešťanoch a Senci) nemá v OSM žiadny objekt amenity=bicycle_rental do 50 m.
```
