# SPS (Slovak Parcel Service) – balíkovo boxes and balíkovo pickup points

| Field | Value |
|---|---|
| publisher | Slovak Parcel Service s.r.o. |
| url | https://backend.sps-sro.sk/api/places/all (JSON, all points); CSV export https://backend.sps-sro.sk/api/places/export?box=1&format=csv (both are used by the map at https://www.sps-sro.sk/balikovo/) |
| format | JSON array; CSV (`;`-separated, UTF-8 with BOM) |
| coords | yes |
| records | 14,300 points in the JSON (2026-09-30). 11,168 of them are PPL CZ points (place_id `8006-…`), which the SPS map also shows. The 3,132 Slovak points are **2,192 balíkovo boxes** (`SPS-…`, type PT; 2,187 status 1) and **940 balíkovo pickup shops** (`PS-…`, type PS) |
| osm_tags | amenity=parcel_locker, brand=balíkovo box, brand:wikidata=Q132188077, operator=Slovak Parcel Service, ref=&lt;place_id&gt;, opening_hours, parcel_mail_in=yes (type_podaj=1) |
| osm_count_sk | brand=balíkovo box 244, brand=balíkovo 27, operator=Slovak Parcel Service 220 (taginfo SK, 2026-09-30); 62 OSM parcel lockers carry an `SPS-…` ref (Postpass, SK bbox, 2026-09-30) |
| license | none stated |
| license_url | https://www.sps-sro.sk/balikovo/integracia-pre-e-shopy (e-shop integration page) |
| license_status | unclear |
| update_freq | live API (per-point `status`, today's opening hours) |
| impact | 4 |
| sync_fit | Sync (points, stable place_id already used as `ref` by OSM mappers, category maps 1:1 to amenity=parcel_locker) |
| verified | yes |

## Try it

- **Map preview:** none, because the licence is unclear, so no extract is redistributed here.
- **QGIS:** save https://backend.sps-sro.sk/api/places/export?box=1&format=csv as `sps.csv` (tested 2026-09-30: 2,189 rows, 2,186 of them Slovak `SPS-…` boxes). Then *Layer → Add Layer → Add Delimited Text Layer…*: custom delimiter `;`, UTF-8, X = `Lng`, Y = `Lat`, EPSG:4326. Filter `"Krajina" = 'SK'`.
- **Web viewer:** https://www.sps-sro.sk/balikovo/

## Notes

- **Gap:** Postpass spatial check on 2026-09-30 with 300 random boxes.
  - 29 have an OSM parcel locker tagged balíkovo/SPS within 50 m (10 %). 77 have a locker of any brand within 50 m (26 %).
  - So **about 1,950 balíkovo boxes are missing**. It is the largest locker network in Slovakia after Z-BOX, and nobody syncs it.
- **Stable id:** `place_id` (for example `SPS-D007149`). OSM mappers already use this exact value as `ref`: 62 OSM lockers have it, which makes a Sync dataset with `ref_tag = ref` straightforward. As in the Z-BOX config, gate the ref index on the brand, because bare `ref` values collide across operators.
- **Fields (JSON):** `id` (internal), `place_id`, `name` (for example "balíkovo box – Abrahám - Abrahám 145 (COOP Jednota)"), `address`, `lat`, `lng`, `type` (PT box / PS shop), `type_box`, `type_store`, `type_podaj` (parcels can be sent from here), `status`, `opening_hours`. The CSV adds `Virtuálne PSČ` (SPS's virtual postcode per point), `COD`, `Foto URL` and `Partner`.
- **Host:** the name holds the host site in brackets (COOP Jednota, Obecný úrad, Lekáreň, Autobusová zastávka). That text helps a mapper place the box. It must not go into `name`: the locker's name is the brand. Put the host in `description` only if the community wants it.
- **Pickup shops (940 `PS-…`):** these are counters in existing shops. They are better as a MapRoulette pointer or as a `post_office=post_partner`-style attribute on the shop than as new nodes. Decide in `osm_sk`; the Czech community's tagging of Balíkovna/PPL shops is a reference.
- **Coverage:** no ATP spider covers SPS, and Sync has no SPS dataset.
- **Tagging:** Tag:amenity=parcel_locker (wiki, raw, read 2026-09-30) marks `brand` as important and lists `operator`, `ref` and `parcel_mail_in`. The id belongs in `ref`, not in `name`. The brand:wikidata Q132188077 is the value already used on OSM balíkovo lockers.
- **ZBGIS:** the catalogue has no object type for parcel lockers.
- **Contact:** Slovak Parcel Service s.r.o., https://www.sps-sro.sk/ (the e-shop integration page is the natural entry point).

## Wiki entry

```
=== Balíkovo boxy SPS ===
* dataset: výdajné miesta a boxy balíkovo (Slovak Parcel Service)
* správca: [https://www.sps-sro.sk/ Slovak Parcel Service s.r.o.]
* licencia: neuvedená – potrebný súhlas [https://www.sps-sro.sk/balikovo/integracia-pre-e-shopy]
* dátové primitívy: body
* odkaz: https://backend.sps-sro.sk/api/places/export?box=1&format=csv
* navrhované značky: {{tag|amenity|parcel_locker}}, {{tag|brand|balíkovo box}}, {{tag|brand:wikidata|Q132188077}}, {{tag|ref|SPS-…}}
* poznámka: 2 192 boxov balíkovo, v OSM je asi 270 a v priestorovom porovnaní (50 m) chýba asi 1 950 (9/2026).
```
