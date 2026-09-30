# SHMÚ climatological and synoptic weather stations (INSPIRE)

| Field | Value |
|---|---|
| publisher | Slovenský hydrometeorologický ústav (SHMÚ), IČO 00156884 |
| url | WFS 2.0 (GML): climatological network `https://geo.shmu.sk/geoserver/ef-swn-cs/ows?service=wfs&version=2.0.0&request=GetFeature&typeNames=ef-swn-cs:EnvironmentalMonitoringFacility`; synoptic network `https://geo.shmu.sk/geoserver/ef-swn-ms-sms/ows?service=wfs&version=2.0.0&request=GetFeature&typeNames=ef-swn-ms-sms:EnvironmentalMonitoringFacility`; precipitation network `https://geo.shmu.sk/geoserver/ef-swn-precs/ows?service=wfs&version=2.0.0&request=GetFeature&typeNames=ef-swn-precs:EnvironmentalMonitoringFacility`; catalogue https://data.gov.sk/set/f99b94b10cfbae26814e365577414590 (climatological), https://data.gov.sk/set/a9e0ec3032f4c2859a0aaff5eb763c0d (synoptic), https://data.gov.sk/set/e4b8d362fbe4f0d2fef43c17f97d1ea7 (precipitation) |
| format | INSPIRE EF GML 3.2 (ETRS89, EPSG:4258, lat/lon order) |
| coords | yes |
| records | 102 climatological stations, 26 synoptic stations (all 26 at climatological sites), 584 precipitation stations, 196 phenological, 30 gamma-dose, 20 surface-layer (fetched 30 Sep 2026) |
| osm_tags | `man_made=monitoring_station` + `monitoring:weather=yes` (+ `monitoring:precipitation=yes`), `operator=Slovenský hydrometeorologický ústav`, `name`, `ref=<station code>` (such as `11800`). Checked against Tag:man_made=monitoring_station (wiki, raw, 30 Sep 2026) |
| osm_count_sk | `man_made=monitoring_station` 343, `monitoring:weather=yes` 116 (taginfo, data until 29 Sep 2026). 16 of the 102 climatological/synoptic stations have an OSM monitoring station within 50 m (Postpass, 30 Sep 2026); 11 of the 584 precipitation stations do |
| license | CC BY 4.0 for author's work, database and sui generis right (national catalogue terms of use) |
| license_url | https://data.gov.sk/set/f99b94b10cfbae26814e365577414590 ; https://creativecommons.org/licenses/by/4.0/ |
| license_status | needs_waiver |
| update_freq | catalogue records modified 2022–2023; network changes are rare |
| impact | 2 |
| sync_fit | Sync (points, one fixed tag set, stable INSPIRE localId / station code as `ref`); precipitation stations excluded (see notes) |
| verified | yes |

## Try it

- **Map preview:** [../samples/shmu-meteo-stanice.geojson](../samples/shmu-meteo-stanice.geojson) has all 102 climatological stations with INSPIRE id, station code, name, whether they are also synoptic, and `osm_monitoring_station_50m` (false for 86).
- **QGIS:** *Layer → Add Layer → Add WFS Layer…*, new connection `https://geo.shmu.sk/geoserver/ef-swn-cs/ows`, add `EnvironmentalMonitoringFacility`. The GML is INSPIRE-nested; QGIS reads the point geometry and `name`. Tested with curl (102 members).

## Notes

- **IDs.** Each feature has an INSPIRE `localId` like `c338a1a5-…/SK11800.KSA`; the part after the slash is the SHMÚ station code (`SK11800` = Holíč; the numbers have the five-digit form of WMO station indices, 118xx–119xx) plus a network suffix (`KSA`, `KSA-KSK`, `SYNOP.KSA-KSK`). Whether the number equals the WMO index for the synoptic stations was not checked. It is stable across the SHMÚ networks (the same code appears in the climatological and synoptic layers), so `ref=11800` works as the Sync key (no `wmo` key is in use in Slovakia, taginfo 0).
- **Gap.** 86 of the 102 professional and automatic climatological stations are missing from OSM. They are fenced meteorological gardens, visible on the orthophoto, and good landmarks (missing: Lomnický štít, Skalnaté Pleso, Sliač, Kamenica nad Cirochou; Chopok and Stará Lesná are already mapped).
- **Precipitation stations.** The 584 rain gauges are mostly read by volunteer observers, often in private gardens. Their names are village names and the network metadata names SHMÚ staff as contacts. They are not proposed for OSM (low use, privacy of the observers' homes).
- **Phenological stations** (196) are observation areas, not objects; coordinates are rounded to minutes. Not proposed.
- **ZBGIS overlap.** ZBGIS has the building use "Meteorologická stanica" (code 92) on `AL015 Budova`, without station code or network. The SAŽP landscape atlas also publishes "Stanice Slovenského hydrometeorologického ústavu" (45 points) and "Meteorologická stanica" (34 points) as cartographic layers; the SHMÚ INSPIRE services are the primary, complete source.
- **Related.** The ŠGÚDŠ hydrogeological layer (`sgud-hg-pramene.md`) contains 235 river gauging stations and 135 rain gauges from older map compilations; SHMÚ does not publish a hydrological station service in the catalogue (checked 30 Sep 2026).
- Contact: SHMÚ, https://www.shmu.sk/ (the WFS features name the manager of the state meteorological network as the responsible party).

## Wiki entry

```
=== Meteorologické stanice SHMÚ (klimatologické a synoptické) ===
* dataset: INSPIRE – Štátna meteorologická sieť – Sieť klimatologických staníc; Sieť synoptických meteorologických staníc
* správca: [https://www.shmu.sk/ Slovenský hydrometeorologický ústav]
* licencia: CC BY 4.0 [https://data.gov.sk/set/f99b94b10cfbae26814e365577414590]
* dátové primitívy: body
* odkaz: https://geo.shmu.sk/geoserver/ef-swn-cs/ows?service=wfs&version=2.0.0&request=GetFeature&typeNames=ef-swn-cs:EnvironmentalMonitoringFacility
* navrhované značky: {{tag|man_made|monitoring_station}} + {{tag|monitoring:weather|yes}}, {{tag|operator|Slovenský hydrometeorologický ústav}}, {{tag|ref|<číslo stanice>}}
* poznámka: zo 102 klimatologických staníc SHMÚ je v OSM len 16.
```
