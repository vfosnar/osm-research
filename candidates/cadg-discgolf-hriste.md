# ČADG – registry of disc golf courses (Mapa hřišť, iDiscGolf)

| Field | Value |
|---|---|
| publisher | Česká asociace discgolfu, z.s. (ČADG), IČO 22889591 – portal https://ceskydiscgolf.cz/ |
| url | https://api.ceskydiscgolf.cz/api/core/fields/ (list, JSON); detail https://api.ceskydiscgolf.cz/api/core/fields/&lt;uuid&gt;/ ; web map https://ceskydiscgolf.cz/cadg/discgolf/mapa-hrist |
| format | JSON REST API behind the Nuxt web app (no auth for the course endpoints) |
| coords | yes (gps_lat / gps_lng, WGS84; 241 of 312 records, all 200 permanent courses) |
| records | 312 courses (2026-09-27): 212 type "Pevné" (permanent), 100 "Dočasné" (temporary tournament layouts). Permanent: 96 with 9 holes, 33 with 6, 26 with 18, 16 with 12. Detail: par 200/200, established_date 198/200, layouts with per-hole par and length 186/200, paid (fee) flag, rental/shop flags, tee and basket type, link to a course map image |
| osm_tags | leisure=disc_golf_course + sport=disc_golf + name, disc_golf:course=&lt;n&gt;_hole, disc_golf:par, fee=yes/no (wiki Tag:leisure=disc_golf_course, Key:disc_golf) |
| osm_count_cz | leisure=disc_golf_course 80, sport=disc_golf 97, disc_golf=basket 465, disc_golf=hole 422 (taginfo CZ, data until 2026-09-26) |
| license | none stated (no licence or terms of use on ceskydiscgolf.cz; only "Obchodní a platební podmínky" and GDPR pages for the member system) |
| license_url | n/a |
| license_status | unclear |
| update_freq | continuous (courses are added by clubs and ČADG staff in the iDiscGolf system; it is also used for live scoring) |
| impact | 3 |
| verified | yes |

## Try it
- **Map preview:** no sample, because the licence is `unclear`.
- **QGIS:** download the list and flatten it to CSV:
  `curl -s https://api.ceskydiscgolf.cz/api/core/fields/ | jq -r '["id","name","hole_count","length","type","paid","gps_lat","gps_lng"], (.[] | select(.gps_lat != null) | [.id,.name,.hole_count,.length,.type,.paid,.gps_lat,.gps_lng]) | @csv' > discgolf.csv`
  (tested: 241 rows). Then *Layer → Add Layer → Add Delimited Text Layer*, file `discgolf.csv`, delimiter comma, X field `gps_lng`, Y field `gps_lat`, CRS EPSG:4326. Filter `"type" = 'Pevné'` to hide temporary tournament layouts.
- **Web viewer:** https://ceskydiscgolf.cz/cadg/discgolf/mapa-hrist (course pages at https://ceskydiscgolf.cz/idg/hriste/&lt;uuid&gt;).

## Notes
- **Gap (Postpass, 2026-09-27):** of the 200 permanent courses with coordinates, only 80 have any
  `leisure=disc_golf_course`, `sport=disc_golf` or `disc_golf=*` object within 500 m. **120 permanent courses
  (60 %) are missing from OSM.** Missing examples: BÚŘOV DISCGOLF – Komárno DiscGolfPark (18 holes), Disc Golf
  Moravan park in Podkopná Lhota (18), DiscGolf Vacenovice (18), DiscGolfPark Budišov nad Budišovkou (18),
  DiscGolfPark Chateau Hostačov (18), DiscGolfPark Amfiteátr Mikulov (6), DiscGolfPark Benešov (6).
- **Why it is niche but useful:** disc golf courses are free public sports grounds in parks, often without a
  visible boundary, so mappers rarely notice them. Disc golf apps (UDisc and others) and OSM-based sport maps
  read `leisure=disc_golf_course`. One course node with name, number of holes, par and fee is exactly what
  the wiki recommends as the minimum.
- **Use only the permanent courses** (`type = "Pevné"`). "Dočasné" records are tournament layouts (names like
  "BDL 2022 2# Teplice") and some have placeholder locations ("International", "Evropa").
- **Coordinates:** a single point per course, usually the first tee or the parking area. Some locations are
  free text with coordinates in them ("49.5881594N, 17.9992747E"). No hole or basket coordinates in the API:
  the hole list has only number, par, length and elevation. It gives course-level tags, not hole geometry.
- **Attributes → tags:** `hole_count` → `disc_golf:course=<n>_hole`; `par` → `disc_golf:par`; `paid` ("0"/"1",
  plus a few "Ne"/"ANO"/"ne" free-text values) → `fee=no/yes`; `established_date` → `start_date`;
  `has_rental` → no established key, so leave it out. Suggested stable ID: `ref:cadg=<uuid>`. The UUIDs are
  stable across the list and detail endpoints, so Sync could keep the data matched.
- **ZABAGED overlap:** none. The ČÚZK ZABAGED_POLOHOPIS map service (149 layers, checked 2026-09-27) has no
  sports-ground or disc golf layer.
- **Not on the known lists:** not on Cs:Česko/freemap (including Potencionální zdroje), Cs:Zdroje_v_jednani or
  in Sync's config.toml.
- **Licence / contact:** no licence is stated, so ask ČADG for consent (ODbL-compatible use of the course list
  and coordinates). General contact podpora@ceskydiscgolf.cz; the board (výkonná rada) is at vr@cadg.cz, and
  the contacts page https://ceskydiscgolf.cz/cadg/kontakty lists the named officers. The sport's community
  is small and friendly to mapping. The ČADG site itself uses an OSM basemap on its course map.
- Wiki pages read: Tag:leisure=disc_golf_course, Key:disc_golf.

## Wiki entry
```
===Discgolfová hřiště (ČADG)===
* dataset: Mapa hřišť / iDiscGolf – seznam discgolfových hřišť
* gestor: [https://ceskydiscgolf.cz/ Česká asociace discgolfu, z.s.]
* licence: neuvedena – nutno požádat o souhlas (podpora@ceskydiscgolf.cz)
* datové primitivy: body
* odkaz: https://api.ceskydiscgolf.cz/api/core/fields/
* navržený tag {{tag|leisure|disc_golf_course}} + {{tag|sport|disc_golf}}, {{tag|disc_golf:course|<počet>_hole}}, {{tag|disc_golf:par}}, {{tag|ref:cadg|<uuid>}}
* poznámka: z 200 stálých hřišť jich 120 v OSM chybí (nic do 500 m); data mají počet jamek, par, rok založení a příznak placení
```
