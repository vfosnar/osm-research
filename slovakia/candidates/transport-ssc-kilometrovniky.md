# Road kilometre posts (kilometrovníky) from the SSC road databank

| Field | Value |
|---|---|
| publisher | Slovenská správa ciest (SSC), Cestná databanka (CDB), IČO 00003328 |
| url | ArcGIS REST (GeoJSON, WGS84): `https://ismcs.cdb.sk/inspire/rest/services/FREE/WFS_ReferencnaSiet/MapServer/1/query?where=1%3D1&outFields=*&outSR=4326&f=geojson` (1,000 per page, page with `resultOffset`); WFS 2.0: `https://ismcs.cdb.sk/inspire/services/FREE/WFS_ReferencnaSiet/MapServer/WFSServer` layer `WFS_ReferencnaSiet:DZ_Kilometrovnik`; road numbers from layer 2 `Usek` of the same service |
| format | ArcGIS REST GeoJSON / WFS 2.0 GML (EPSG:25834) |
| coords | yes (3D points) |
| records | 13,176 posts: diaľnice and rýchlostné cesty 3,358, I. trieda 3,544, II. trieda 3,118, III. trieda 3,148, účelové cesty 8 (fetched 30 Sep 2026, state 1 Jan 2026) |
| osm_tags | `highway=milestone`, `distance=<value on the sign>`, `ref=<road number>` (the road number in CDB, `cisloPK`, has the same form as OSM `ref`: `D1`, `R1`, `61`, `507`, `2084`) |
| osm_count_sk | `highway=milestone` 64 nodes in all of Slovakia (taginfo, 29 Sep 2026); 0 in the Žilina district bbox (Postpass, 30 Sep 2026) |
| license | CC BY 4.0 ("Autor: Slovenská správa ciest, Licencia: CC-BY 4.0" on the CDB map-services page; `AccessConstraints: Creative Commons Attribution License` in the WFS capabilities) |
| license_url | https://www.cdb.sk/sk/poskytovanie-udajov/poskytovanie-vektorovych-udajov-CTEPK/mapove-sluzby.alej |
| license_status | needs_waiver |
| update_freq | yearly (state on 1 January) |
| impact | 3 |
| sync_fit | Sync: points with a 1:1 tag mapping (`highway=milestone`); there is no stable publisher ID (only `OBJECTID`), so ongoing sync needs a composite key such as `ref` + `distance` |
| verified | yes |

## Try it

- **Map preview:** [../samples/transport-ssc-kilometrovniky.geojson](../samples/transport-ssc-kilometrovniky.geojson) has all 257 posts in the Žilina district, with the road number joined from the `Usek` layer. OSM has none there.
- **QGIS:** *Layer → Add Layer → Add Vector Layer*, source type *Protocol: HTTP(S)*, URI
  `https://ismcs.cdb.sk/inspire/rest/services/FREE/WFS_ReferencnaSiet/MapServer/1/query?where=1%3D1&outFields=*&outSR=4326&f=geojson`
  (loads the first 1,000 posts). For the full layer use *Layer → Add Layer → Add WFS Layer*, a new connection with URL
  `https://ismcs.cdb.sk/inspire/services/FREE/WFS_ReferencnaSiet/MapServer/WFSServer`, then pick `DZ_Kilometrovnik`. The ArcGIS REST connection (*ArcGIS REST Server* in the Data Source Manager, URL `https://ismcs.cdb.sk/inspire/rest/services/FREE/WFS_ReferencnaSiet/MapServer`) works too.
- **Web:** CDB map viewer https://ismcs.cdb.sk/portal/mapviewer

## Notes

- Attributes per post: `usek` (ID of the reference-network section), `stanicenieZaciatku` (chainage within the section in metres), `umiestnenie` (P/L side: 12,588 right, 585 left, 3 other), `udajNaZnacke` (the value printed on the sign, like `128,0`). The road number is not on the post. Join `usek` to `usekId` in layer 2 (`Usek`: `triedaPK`, `cisloPK`, `spravca_skratka`, `Okres`). All 13,176 posts matched a section.
- Gap: OSM has 64 `highway=milestone` in Slovakia, so about 13,100 posts are missing. The posts are useful for emergency calls ("som na D1 na 128. kilometri"), for navigation apps that show them, and for positioning road incidents. Motorway posts often also have 100 m intermediate signs, but CDB only has the kilometre signs.
- Tags: per the wiki page Tag:highway=milestone, `distance` holds the number and `ref` the road reference, and the node may sit on the road way or at the sign next to it. The CDB points are at the sign (side P/L). Convert `128,0` to `distance=128.0` or `128`.
- ZBGIS: the ZBGIS object catalogue (`kto_zbgis.pdf`) has no kilometre-post class, so this is not a duplicate of the consented ZBGIS services. The WFS says it contains "dopravnú značku kilometrovník", and the same service carries the reference network (sections, nodes, roads, E-roads).
- Licence: CC BY 4.0, so a waiver is needed. There is a precedent with SSC: the 2007 consent for road refs from the "Miestopisný priebeh cestných komunikácií" (known-sources). A new request could cover the whole CDB (this file plus `transport-ssc-cestne-objekty.md`).
- Contact: Slovenská správa ciest, Cestná databanka, https://www.cdb.sk/ (contacts on the site).

## Wiki entry

```
=== Kilometrovníky zo SSC Cestnej databanky ===
* dataset: Údaje centrálnej technickej evidencie ciest – WFS referenčnej siete, vrstva DZ_Kilometrovnik
* správca: [https://www.cdb.sk/ Slovenská správa ciest – Cestná databanka]
* licencia: CC BY 4.0 [https://www.cdb.sk/sk/poskytovanie-udajov/poskytovanie-vektorovych-udajov-CTEPK/mapove-sluzby.alej]
* dátové primitívy: body
* odkaz: https://ismcs.cdb.sk/inspire/services/FREE/WFS_ReferencnaSiet/MapServer/WFSServer
* navrhované značky: {{tag|highway|milestone}}, {{tag|distance|<údaj na značke>}}, {{tag|ref|<číslo cesty>}}
* poznámka: 13 176 kilometrovníkov na diaľniciach a cestách I.–III. triedy, v OSM je v celom Slovensku 64 uzlov highway=milestone.
```
