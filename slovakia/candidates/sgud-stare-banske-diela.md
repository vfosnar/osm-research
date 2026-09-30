# Staré banské diela SR: Geofond register of old mine workings (adits, shafts, heaps, pits)

| Field | Value |
|---|---|
| publisher | Štátny geologický ústav Dionýza Štúra (ŠGÚDŠ), Geofond; for MŽP SR |
| url | ArcGIS REST: `https://ags.geology.sk/arcgis/rest/services/WebServices/SBD/MapServer` (layer 0 `Objekty` points, 1 `Línie`; query `/0/query?where=1%3D1&outFields=*&outSR=4326&f=json&orderByFields=objectid&resultOffset=N&resultRecordCount=1000`); WFS: `https://ags.geology.sk/arcgis/services/WebServices/SBD/MapServer/WFSServer?request=GetCapabilities&service=WFS` (feature types `WebServices_SBD:Objekty`, `WebServices_SBD:Línie`); catalogue https://data.gov.sk/set/c15dcac54bc20be445341173fa8643dc , metadata https://rpi.gov.sk/metadata/d41a677a-8291-4883-a365-0859105391cd |
| format | ArcGIS REST JSON/GeoJSON, WFS, WMS |
| coords | yes (points) |
| records | 17,689 point objects (downloaded 30 Sep 2026): 6,538 heaps (`5 - halda`), 5,677 adits (`2 - štôlňa`), 4,143 pits and pit rows (`4 - pinga, pingový ťah`), 659 shafts (`1 - šachta`), 620 other, 50 tailings ponds, 2 quarries. 13,798 flagged `SBD` (old workings) and 3,835 `BD` |
| osm_tags | adit: `man_made=adit` + `disused=yes`; shaft: `man_made=mineshaft` + `disused=yes` (or `disused:man_made=mineshaft` when little is left, per the wiki); heap: `man_made=spoil_heap`; plus `name` (only real names, not "Štôlňa"/"Halda"), `resource=*` from `sbd_spec_sur`; suggested `ref:sgudds:sbd=<sbd_id>`. Checked against Tag:man_made=adit, Tag:man_made=mineshaft, Tag:man_made=spoil_heap (wiki, raw, 30 Sep 2026) |
| osm_count_sk | `man_made=adit` 3,925 (3,303 with `disused`), `man_made=mineshaft` 243, `historic=mine_shaft` 9, `man_made=spoil_heap` 773 (taginfo, data until 29 Sep 2026). Match against all OSM adit/shaft/mine/heap features in the SK bbox (Postpass, 30 Sep 2026): 1,471 of 5,677 adits and 149 of 659 shafts have an OSM mining feature within 50 m; 1,533 of 6,538 heaps have one within 50 m |
| license | CC BY 4.0 for author's work, database and sui generis right (national catalogue terms of use); the service says "Využitie údajov … predpokladá začlenenie ochranných znakov (copyright ŠGÚDŠ)" |
| license_url | https://data.gov.sk/set/c15dcac54bc20be445341173fa8643dc ; https://creativecommons.org/licenses/by/4.0/ |
| license_status | needs_waiver |
| update_freq | register maintained by Geofond; catalogue record modified 2021-06-23 |
| impact | 3 |
| sync_fit | MapRoulette (stable `sbd_id`, but whether an adit is still open, collapsed or only a heap needs a human with imagery/DMR 5.0; ~4,200 adits and ~500 shafts to review) |
| verified | yes |

## Try it

- **Map preview:** [../samples/sgud-stare-banske-diela.geojson](../samples/sgud-stare-banske-diela.geojson) has the 574 adits and shafts around Banská Štiavnica (bbox 18.82–18.98 E, 48.40–48.50 N). `osm_adit_or_shaft_50m` is false for 352 of 446 adits and 74 of 128 shafts, even in this well-mapped mining town.
- **QGIS:** *Layer → Add Layer → Add WFS Layer…*, new connection with URL `https://ags.geology.sk/arcgis/services/WebServices/SBD/MapServer/WFSServer`, then add `Objekty`. Or *Data Source Manager → ArcGIS REST Server* with `https://ags.geology.sk/arcgis/rest/services/WebServices/SBD/MapServer`. Both answered on 30 Sep 2026 (the host resets a connection now and then; retry).
- **Web:** ŠGÚDŠ map portal https://apl.geology.sk/mapportal/

## Notes

- **Attributes.** `sbd_id` (map sheet + sequence number, 17,678 distinct values out of 17,689, so almost unique), `sbd_naz` (name; mostly generic like "Halda" 2,653×, "Štôlňa" 1,653×, "Bezmenná štôlňa" 387×, so filter generic names before writing `name`), `sbd_typobjektu_`, `sbd_spec_sur` (resource, such as "Au,Ag"), `sbd_sanac_` (remediation need: 587 flagged "ohrozenie bezpečnosti" = a safety hazard), `sbd_rozm` (size), `sbd_rokukonceniabc` (end of mining, such as "17.storočie"), `sbd_spravca`.
- **Gap.** OSM has many adits already, often traced from DMR 5.0 (`source=LIDAR ÚGKK SR DMR 5.0` on ~900 of them) or surveyed. The register adds about 4,200 adits and 500 shafts with no OSM mining feature within 50 m, plus the resource and the end-of-mining century, which OSM rarely has. The safety flag is useful for hikers (`hazard=*` needs a community decision).
- **Heaps and pits.** 6,538 heaps and 4,143 pits are real landscape features but small; import them only where DMR 5.0 shading confirms them. They are best left as a second MapRoulette challenge.
- **Positional quality.** For the 1,919 register adits that have an OSM `man_made=adit` within 100 m, the distance to it is 14 m (25th percentile), 29 m (median) and 53 m (75th percentile). So the points are map-accurate, not survey-accurate, and the 50 m gap figures above slightly overstate the gap. The IDs are per map sheet, so the points were probably digitised from maps. Use DMR 5.0 hillshade (consent exists, known-sources) to place each adit mouth.
- **ZBGIS overlap.** The ZBGIS catalogue has no mine/adit object class; "Baňa, šachta, štôlňa" (code 3) appears only as a category of geographic names, so only named mines are in ZBGIS. The register is the only national source of unnamed workings.
- **Community context.** In June 2025 a geologist asked on `osm_sk` how to map old mine workings ("Zaznacenie banskych diel do mapy - navod", thread `hR8wnfgbNEY`) and was pointed to the wiki; nobody mentioned this register. The "Stare bane a jaskyne na Freemape" thread (`w2EeolKjAwo`, 2015) is about rendering only.
- The line layer (`Línie`) holds linear workings such as pit rows; not evaluated.
- Contact: ŠGÚDŠ, Geofond, Mlynská dolina 1, Bratislava, https://www.geology.sk/

## Wiki entry

```
=== Staré banské diela SR (register Geofondu, ŠGÚDŠ) ===
* dataset: Staré banské diela SR – register Geofondu – objekty
* správca: [https://www.geology.sk/ Štátny geologický ústav Dionýza Štúra]
* licencia: CC BY 4.0 [https://data.gov.sk/set/c15dcac54bc20be445341173fa8643dc]
* dátové primitívy: body
* odkaz: https://ags.geology.sk/arcgis/services/WebServices/SBD/MapServer/WFSServer?request=GetCapabilities&service=WFS
* navrhované značky: {{tag|man_made|adit}} + {{tag|disused|yes}}, {{tag|man_made|mineshaft}}, {{tag|man_made|spoil_heap}}, {{tag|resource|*}}, {{tag|ref:sgudds:sbd|<sbd_id>}}
* poznámka: register má 5 677 štôlní a 659 šácht, z ktorých asi 4 200 štôlní a 500 šácht nemá v OSM do 50 m žiadny banský objekt.
```
