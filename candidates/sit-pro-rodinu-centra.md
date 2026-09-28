# Síť pro rodinu – 266 mother, family and community centres (mateřská a rodinná centra)

| Field | Value |
|---|---|
| publisher | Síť pro rodinu, z.s. (umbrella of Czech mother/family centres), Truhlářská 24, Praha 1, info@sitprorodinu.cz, 602 178 882 |
| url | https://sitprorodinu.cz/o-nas/clenske-organizace/ (JavaScript variable `clenskeOrganizace` in the page HTML) |
| format | JSON array embedded in HTML (WordPress page with a Leaflet map) |
| coords | yes (WGS84 `lat`/`lng`, all 266) |
| records | 266 member organisations (2026-09-28): name, city, address (250), region, website (253), phone (30), profile URL; 264 distinct positions; a few centres appear twice (Centrum pro rodinu Beruška, Uherský Brod) |
| osm_tags | `amenity=community_centre` + `community_centre=family_centre` + `community_centre:for=family` (Key:community_centre); `name`, `website`, `operator` |
| osm_count_cz | taginfo 2026-09-28: community_centre=family_centre 7; name values containing "Rodinné centrum" 14 objects, "Mateřské centrum" 7 |
| license | none stated ("© 2026 Síť pro rodinu" in the footer only) |
| license_url | – |
| license_status | unclear |
| update_freq | membership list, updated as members join or leave (no dates in the data) |
| impact | 3 |
| sync_fit | MapRoulette (no stable id, community_centre subtype is de facto only) |
| verified | yes |

## Try it
- **Map preview:** none, licence unclear.
- **Browser:** https://sitprorodinu.cz/o-nas/clenske-organizace/ shows the map and list.
- **Extract:** `curl -s https://sitprorodinu.cz/o-nas/clenske-organizace/ | python3 -c "import re,sys,json;print(json.dumps(json.loads(re.search(r'var clenskeOrganizace = (\[.*?\]);\n',sys.stdin.read(),re.S).group(1)),ensure_ascii=False))" > spr.json`
  (tested 2026-09-28, 266 records).
- **QGIS:** convert `spr.json` to CSV and load with *Layer → Add Layer → Add Delimited Text Layer*, X = `lng`, Y = `lat`, EPSG:4326.

## Notes
- **What it adds:** mother and family centres are where parents with babies and toddlers go (playrooms,
  courses, baby-changing, breastfeeding support, often a children's group). They are community NGOs, not
  registered social services, so they are **not** in the MPSV register behind ZABAGED
  `SocialniZarizeniDefinicniBod` and Sync. No other national list with coordinates was found.
- **Gap, measured (local match against the 2026-09-27 Czechia extract, 150 m radius):** of 266 centres,
  **14** have an OSM object nearby whose name looks like a family/mother/community centre or that is tagged
  community_centre=family_centre; 20 more have an unnamed or differently named community_centre/childcare
  object nearby; **232** have nothing. Nationally OSM has 7 community_centre=family_centre and about 21
  objects named "Rodinné/Mateřské centrum", against 109 member names starting "Rodinné" or "Mateřské".
- **Caveats:** coordinates are geocoded from the address (some members have no address, only a point), and
  the centre is often one room inside a larger building (a school, parish house or town-hall annex), so
  import as nodes after a check. No opening hours in the data; the member's website usually has them.
  The profile URL slug is derived from the member's e-mail address, so do not use it as a ref.
- **Contact:** Síť pro rodinu, z.s. (info@sitprorodinu.cz) for consent to use the member list.
- Wiki pages read: Key:community_centre (value family_centre, community_centre:for=family).

## Wiki entry
```
===Síť pro rodinu – mateřská a rodinná centra===
* dataset: Členské organizace Sítě pro rodinu
* gestor: [https://sitprorodinu.cz/ Síť pro rodinu, z.s.]
* licence: neuvedena, nutno vyjednat (info@sitprorodinu.cz)
* datové primitivy: body
* odkaz: https://sitprorodinu.cz/o-nas/clenske-organizace/
* navržený tag {{tag|amenity|community_centre}} + {{tag|community_centre|family_centre}}
* poznámka: 266 rodinných a mateřských center se souřadnicemi; v OSM je u 232 z nich v okruhu 150 m nic, family_centre je v ČR jen 7×
```
