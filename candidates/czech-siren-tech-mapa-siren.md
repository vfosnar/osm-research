# Czech Siren Tech – Mapa sirén (community map of JSVV warning sirens)

| Field | Value |
|---|---|
| publisher | Czech Siren Tech (four-person hobby group of siren enthusiasts, https://www.czechsirentech.cz/, contact info@czechsirentech.cz) |
| url | web map https://www.czechsirentech.cz/mapa-siren; data = Mapbox vector tileset `czech-siren-tech.9w21l9qy`, layer `Siren_Map`: `https://api.mapbox.com/v4/czech-siren-tech.9w21l9qy/{z}/{x}/{y}.vector.pbf?access_token=&lt;public Mapbox token embedded in the map page source&gt;` (public token embedded in their page); TileJSON `https://api.mapbox.com/v4/czech-siren-tech.9w21l9qy.json?access_token=…` |
| format | Mapbox Vector Tiles (z0–12), points; the full master copy is a Google Earth project (not downloadable) |
| coords | yes |
| records | 4,335 distinct points (all z11 tiles over CZ decoded 2026-09-28). Fields: `Name` = manufacturer + model (251 distinct strings; VEM DS977 2,311, MEZ H1/B2 174, SiRcom ESp 750 MAESTRO 113, MEZ H4/A2 108, …), `Description` (144 filled: history such as "Náhrada za MEZ H1/B2", 39 say dismantled/disconnected). About 192 points are local broadcast systems (BMIS: Bártek SARAH, JD Rozhlasy, PWS Plus VOX, Colsys VoiceGuard, EL-MIK BIS), not sirens. No stable ID. |
| osm_tags | emergency=siren + siren:purpose=civil_defense + siren:type=electronic/electromechanical + manufacturer + model (wiki Tag:emergency=siren) |
| osm_count_cz | emergency=siren 403 (taginfo 2026-09-28); 422 nodes in the local 2026-09-27 Czechia extract |
| license | none stated; site footer "Czech Siren Tech (2021 - 2026) - Všechna práva vyhrazena" |
| license_url | https://www.czechsirentech.cz/mapa-siren |
| license_status | unclear |
| update_freq | "pravidelně aktualizována"; tileset re-uploaded 2026-02-09 (created 2024-12-12) |
| impact | 3 |
| sync_fit | MapRoulette (no stable id, model string needs mapping to siren:type) |
| verified | yes |

## Try it
- **Map preview:** none (licence unclear). Use the web map instead.
- **QGIS:** *Layer → Add Layer → Add Vector Tile Layer → New Generic Connection*, URL
  `https://api.mapbox.com/v4/czech-siren-tech.9w21l9qy/{z}/{x}/{y}.vector.pbf?access_token=TOKEN`,
  min zoom 0, max zoom 12. Replace `TOKEN` with the public `pk.…` token that appears after
  `access_token=` in the embedded Mapbox iframe URL in the source of https://www.czechsirentech.cz/mapa-siren.
  Layer `Siren_Map`, attributes `Name`, `Description`. (Tiles fetched and decoded this way on 2026-09-28.)
- **Web:** https://www.czechsirentech.cz/mapa-siren (simplified Mapbox map; the full Google Earth
  project is linked on the same page).

## Notes
- **What it is:** a volunteer register of JSVV end elements (koncové prvky varování) across Czechia,
  built by the siren-enthusiast community (photos, YouTube recordings with Street View / Mapy.cz links,
  reader reports). HZS ČR, which runs JSVV, publishes no location list; the only open municipal set
  found is Most (26 sirens, `most-opendata.md`).
- **Gap (local match against the 2026-09-27 Czechia extract):** 4,335 map points vs 422 OSM sirens;
  only 71 map points have an OSM siren within 200 m, so about 4,260 are missing. City bboxes (map / OSM):
  Brno 51 / 2, Ostrava 62 / 0, Plzeň 57 / 0, Praha 301 / 58, Olomouc 43 / 60. 340 OSM sirens have no map
  point within 200 m (Olomouc is one such area), so the map is not complete either.
- **Value for OSM:** manufacturer + model per siren is richer than anything in OSM (taginfo CZ:
  `siren:type` on 142 objects, no `siren:model`). `model`/`manufacturer` can be split from `Name`.
- **Caveats:** exclude BMIS/rozhlas points (one icon per whole system, not a device) and points whose
  Description says dismantled; the simplified tiles don't carry the "black icon = disconnected" status of
  the Google Earth master. Positions partly come from Google Street View, which is a licence question for
  OSM in itself, so ask the group how each point was located. No stable ID: a one-shot import or a
  MapRoulette-style check list, not a Sync source, unless the group adds IDs.
- **Contact:** info@czechsirentech.cz (they explicitly invite corrections to the map; also a Discord).
- Wiki page read: Tag:emergency=siren.

## Wiki entry
```
===Czech Siren Tech – mapa sirén===
* dataset: Mapa sirén (varovné koncové prvky JSVV)
* gestor: [https://www.czechsirentech.cz/ Czech Siren Tech (komunita nadšenců)]
* licence: neuvedena („Všechna práva vyhrazena“), nutný souhlas [https://www.czechsirentech.cz/mapa-siren]
* datové primitivy: body
* odkaz: https://www.czechsirentech.cz/mapa-siren (Mapbox tileset czech-siren-tech.9w21l9qy, vrstva Siren_Map)
* navržený tag {{tag|emergency|siren}}, {{tag|siren:purpose|civil_defense}}, {{tag|manufacturer}}, {{tag|model}}
* poznámka: 4 335 bodů s výrobcem a typem sirény proti 422 sirénám v OSM; shoda do 200 m jen u 71 bodů
```
