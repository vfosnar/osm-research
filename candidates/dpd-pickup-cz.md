```
name: DPD CZ Pickup – export of all pickup points and lockers (DPD boxes + partner lockers AlzaBox, GLS, One Box, OX Point, Z-BOX)
publisher: Direct Parcel Distribution CZ s.r.o. (DPD CZ)
url: https://pickup.dpd.cz/api/getAll?country=203  (also https://pickup.dpd.cz/Export/xml?country=203 and https://pickup.dpd.cz/Export/csv?country=203; documented at https://pickup.dpd.cz/integrace/)
format: JSON (also XML, CSV)
coords: yes
records: 16,087 CZ items (2026-09-27): 4,297 pickup_point (shops) + 11,790 dpd_box. The dpd_box items are 4,056 Z-BOX, 3,987 AlzaBox, 1,808 GLS, 790 One Box, 728 DPD box (DPD's own), 405 OX Point and 16 AlzaWall
osm_tags: amenity=parcel_locker + brand/brand:wikidata/operator per NSI (DPD Pickup Box Q114273730; AlzaBox Q115254158; One Box Q110738715; Penguin/OX see notes); ref=<DPD id> for DPD's own boxes only; opening_hours; parcel_mail_in (from dropoff_allowed)
osm_count_cz: amenity=parcel_locker 11,567 (taginfo CZ, data 2026-09-26); brand:wikidata=Q114273730 (DPD Pickup Box) 205; Q115254158 (AlzaBox) 2,136; Q110738715 (One Box) 602; brand=OX Point 93
license: none stated
license_url: https://pickup.dpd.cz/integrace/ (integration page; publishes the export URLs with no licence text)
license_status: unclear
update_freq: live API. The response carries a `hash` field that changes when the list changes.
impact: 4
verified: yes
```

## Notes

**Gap (spatial check, 2026-09-27).** Each locker was matched to OSM amenity=parcel_locker within 40 m. The OSM side came from Postpass (CZ bbox), matched by brand/operator/name keyword. Z-BOX, which Sync already covers, is the control: 92 % of Z-BOX lockers match, which validates the method.

| Family in DPD feed | Feed | Same-brand OSM locker ≤40 m | Missing |
|---|---|---|---|
| AlzaBox | 3,987 | 1,980 | **2,007** |
| DPD box (own) | 728 | 175 | **553** |
| OX Point | 405 | 126 | **279** |
| One Box | 790 | 557 | **233** |
| Z-BOX (control, already in Sync) | 4,056 | 3,729 | 327 |

- **AlzaBox is the single biggest missing parcel-locker network in CZ.** Alza's own AlzaBox API requires OAuth partner credentials: https://github.com/AlzaBox/AlzaBox-API-Description, token URL identitymanagement.phoenix.alza.cz. This DPD export and the Česká pošta Balíkovna XML (see `ceska-posta-balikovna.md`) are the only open-access lists with coordinates.
  - Caveat: the ids here are DPD ids (for example `CZ21570`), not Alza box ids.
  - About 1,055 OSM AlzaBoxes carry some `ref`. Conflation must therefore match by position and name, with no ref_tag, or use a namespaced `ref:dpd`.
- **DPD's own boxes:**
  - DPD ids (`CZ24301` style) match the few existing OSM `ref` values on DPD Pickup Box (9 of 207 in the CZ bbox). So `ref` = DPD id is a natural key, the same as for Z-BOX in Sync (`ref_tag = "ref"`).
  - NSI entry "DPD Pickup Box" (cz): brand=DPD Pickup Box, brand:wikidata=Q114273730, operator=Direct Parcel Distribution CZ, operator:wikidata=Q58550406.
- **Pickup points (4,297):** these are DPD pickup counters inside existing shops. They could add `post_office=post_partner` / `post_office:*` attributes, but that has lower value than the lockers.
- **Record fields:** `id`, `company` (display name), street/house_number/city/postcode, `latitude`/`longitude`, `pickup_network_type`, `dropoff_allowed`, `cardpayment_allowed`, and `hours` per day.
- **Wiki read:** Tag:amenity=parcel_locker (raw). brand is "important"; operator, ref, parcel_mail_in, parcel_pickup and opening_hours are optional. Do not put the locker id into `name`.
- **Licence:** there is no licence. The export is public and documented for e-shops, but reusing it in OSM needs consent. Zásilkovna is the precedent: its consent is recorded on Cs:Česko/freemap (2021) and Z-BOX is now synced. Contact: info@dpd.cz, which is the contact given in the feed records.
- Not ATP: there is no DPD CZ spider (only `dpd_de`).

## Wiki entry

```
===DPD Pickup – výdejní místa a boxy===
* dataset: seznam výdejních míst a výdejních boxů DPD (vč. partnerských AlzaBoxů, One Box, OX Point, GLS)
* gestor: [https://pickup.dpd.cz/ Direct Parcel Distribution CZ s.r.o.]
* licence: neuvedena – nutný souhlas [https://pickup.dpd.cz/integrace/]
* datové primitivy: body
* odkaz: https://pickup.dpd.cz/api/getAll?country=203
* navržený tag {{tag|amenity|parcel_locker}}, {{tag|brand|DPD Pickup Box}}, {{tag|ref|<id>}}
* poznámka: v OSM chybí cca 2 000 AlzaBoxů, 550 DPD boxů a 280 OX Pointů (prostorové porovnání 40 m, 9/2026).
```
