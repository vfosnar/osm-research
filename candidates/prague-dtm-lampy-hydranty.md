# Archivní DTM Prahy – inženýrské sítě – povrchové znaky zobrazené symbolem (street lamps, fire hydrants, …)

| Field | Value |
|---|---|
| publisher | IPR Praha |
| url | https://mp.iprpraha.cz/arcgis/rest/services/Hosted/DTMP_CUR_TMISZNAK_B/FeatureServer/0 (filter by `ctmtp_kod`, e.g. `/query?where=ctmtp_kod%3D606560&outFields=*&outSR=4326&f=geojson`); catalogue https://opendata.geoportalpraha.cz/datasets/iprpraha::archivní-dtm-prahy-inženýrské-sítě-povrchové-znaky-zobrazené-symbolem-1 |
| format | ArcGIS FeatureServer (JSON/GeoJSON), Hub downloads |
| coords | yes (points) |
| records | 1,387,674 points in total. Relevant classes (fetched 2026-09-27): 606560 "svítidlo na stožáru" 121,337; 606580 "svítidlo slav. osvět. na soklu" 2,788; 606570 "svítidlo slav. osvět. na stožáru" 757; 606561 "svítidlo na objektu" 1,189; 406130 "hydrant podzemní – povrch. znak" 24,320; 406120 "hydrant nadzemní – povrch. znak" 1,619; 605250 "semafor" 5,742; 736750 "telefonní budka volně stojící" 1,196 |
| osm_tags | highway=street_lamp (+ support=pole / lamp_mount); emergency=fire_hydrant + fire_hydrant:type=underground\|pillar |
| osm_count_cz | highway=street_lamp 62,220 CZ / 20,328 Prague; emergency=fire_hydrant 4,217 CZ / 495 Prague; fire_hydrant:type=underground 1,051 CZ (taginfo Geofabrik and Postpass within relation 435514, 2026-09-27) |
| license | CC BY 4.0 ("datový podklad © IPR Praha") + IPR consent for all open data in OSM (2018) |
| license_url | https://geoportalpraha.cz/data-a-sluzby/otevrena-data ; https://lists.openstreetmap.org/pipermail/talk-cz/2018-February/018526.html |
| license_status | ok |
| update_freq | none, archival snapshot ("Stav k 30.6.2024, dále neaktualizované") |
| impact | 4 |
| verified | yes |

## Notes

**What it is.** The point symbols (`ctmtp_kod` and `ctmtp_popis`) of Prague's former Digital
Technical Map (DTM), which covers utilities of all networks. It was frozen on 30 June 2024,
when the state-regulated DTM kraje replaced it. The layer carries only a code, a description,
the provider and a `globalid`. There is no lamp ID and no hydrant number.

**OSM gap (Postpass sample, 2026-09-27).**
- Street lamps on poles: in a sample of every 40th point (3,014), 2,749 (91%) had no OSM
  `highway=street_lamp` within 3 m. That puts roughly 110,000 lamps missing, against
  20,328 lamps OSM has in Prague.
- Above-ground hydrants (all 1,619): 1,504 (93%) had no OSM `emergency=fire_hydrant` within 5 m.
  Underground hydrants (24,320) are almost entirely missing, since OSM has only 495 hydrants in
  Prague.

**Caveats.**
- The snapshot dates from 2024 and will not be updated. Lamps and hydrants rarely move, but
  there will be removals and additions since then, so treat it as a one-shot import or QA
  layer, not a Sync source.
- Every DTM feature exists twice, as a "povrch. znak" (surface sign) and a "podz. vedení"
  (underground network) code. Use only the *povrch. znak* codes listed above.
- There are no stable public IDs. `globalid` identifies the archive record only.
- The symbol position is the survey point of the object (±cm, geodetic survey), which is far
  better than imagery.
- Traffic signals (`semafor`, 5,742) are signal heads and poles, not road-node positions, so
  they are unsuitable for direct import but useful for QA of `highway=traffic_signals`.
- Standalone phone booths (1,196) are likely mostly removed by now. Skip them.
- Wiki pages read: Tag:highway=street_lamp (support, lamp_mount, ref) and
  Cs:Tag:highway=street_lamp; Tag:emergency=fire_hydrant and Cs:Tag:emergency=fire_hydrant
  (`fire_hydrant:type=underground/pillar`).
- The companion layer "Archivní DTM Prahy – … – autorizovaná data správců" contains data from
  the network operators themselves. I did not check it; it may carry third-party rights.

## Wiki entry
```
===Veřejné osvětlení a hydranty – archivní DTM Prahy===
* dataset: Archivní DTM Prahy – inženýrské sítě – povrchové znaky zobrazené symbolem
* gestor: [https://geoportalpraha.cz IPR Praha]
* licence: CC BY 4.0 + souhlas IPR s využitím všech opendat pro OSM (2018) [https://lists.openstreetmap.org/pipermail/talk-cz/2018-February/018526.html]
* datové primitivy: body
* odkaz: https://mp.iprpraha.cz/arcgis/rest/services/Hosted/DTMP_CUR_TMISZNAK_B/FeatureServer/0
* navržený tag {{tag|highway|street_lamp}}, {{tag|emergency|fire_hydrant}} + {{tag|fire_hydrant:type|underground/pillar}}
* poznámka: 121 tis. stožárových svítidel a 26 tis. hydrantů (stav 30. 6. 2024), v OSM je v Praze ~20 tis. lamp a 495 hydrantů; ~91 % lamp ze vzorku v OSM chybí.
```
