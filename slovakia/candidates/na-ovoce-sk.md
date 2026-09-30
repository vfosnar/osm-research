# Na ovoce – fruit trees in Slovakia

| Field | Value |
|---|---|
| publisher | Na ovoce, z.s. (Czech association; Mapotic map id 9288, web map https://map.na-ovoce.cz/) |
| url | https://www.mapotic.com/api/v1/maps/9288/pois.geojson/ |
| format | GeoJSON FeatureCollection (Mapotic API, anonymous), 9 MB for the whole map |
| coords | yes (WGS84 points) |
| records | 26,295 POIs in total, **4,936 inside Slovakia** (point-in-polygon against OSM relation 14296, simplified, 2026-09-30). SK by category: Jabloň (apple) 1,403, Ořešák (walnut) 983, Třešeň (cherry) 731, Švestka (plum) 383, Hrušeň (pear) 293, Myrobalán 141, Šípková růže 120, Bez černý 114, Líska 101, Ostružiník 91, Morušovník 89, Kaštan jedlý 73, Maliník 63, Muchovník 62, Višeň 49, other 240 |
| osm_tags | `natural=tree` + `genus`/`species` (wiki Tag:natural=tree, Key:species: scientific name); orchards `landuse=orchard`; shrub categories are not trees |
| osm_count_sk | natural=tree 99,862; species 2,154; landuse=orchard 1,474 (taginfo, data until 2026-09-29) |
| license | none published; the association calls it an "otevřená mapa" (open map) on https://na-ovoce.cz/web/vyvoj-mapovaci-aplikace (read 2026-09-30), but no licence is stated. Mapotic terms give other users no rights to content |
| license_url | https://na-ovoce.cz/web/vyvoj-mapovaci-aplikace |
| license_status | unclear |
| update_freq | crowdsourced; SK records by last_update: 2021 4,296 (the migration to Mapotic), 2022 112, 2023 140, 2024 127, 2025 128, 2026 133 |
| impact | 3 |
| sync_fit | MapRoulette (no official id; review layer: tree exists? add genus/species; orchard vs single tree is a human judgement) |
| verified | yes |

## Try it

- **Map preview:** none (licence unclear). Web map: https://map.na-ovoce.cz/ (zoom to Banská Bystrica or Bratislava).
- **QGIS:** *Layer → Add Layer → Add Vector Layer*, source type *Protocol: HTTP(S)*, type *GeoJSON*, URI
  `https://www.mapotic.com/api/v1/maps/9288/pois.geojson/` (tested 2026-09-30: 26,295 points). Filter to Slovakia
  with a selection by location against a Slovakia boundary; the species is in `category_name` (cs/en).

## Notes

- Known in the Czech research (the Czech file `candidates/na-ovoce.md` covers CZ); nobody has proposed the Slovak part to the
  Slovak community. The map interface is Czech, but a fifth of the points are in Slovakia.
- Clusters: Banská Bystrica and surroundings (about 1,000 points within 0.1°), Bratislava (about 600), Zvolen,
  Nitra/Hlohovec, Záhorie.
- **Gap (Banská Bystrica, bbox 19.05,48.68,19.25,48.82, Postpass 2026-09-30):** 1,061 Na ovoce points; OSM has 3,940
  `natural=tree` nodes in that bbox. **Only 33 (3 %)** Na ovoce points have an OSM tree within 15 m, and 102 (10 %)
  have a tree or `landuse=orchard` within 15 m. Nationally OSM Slovakia has only 2,154 objects with `species`, so
  the species information alone doubles what OSM holds.
- Positions come from volunteers' phones and are not survey-grade; use it as a review layer, not a blind import.
  Shrub categories (Šípková růže, Bez černý, Ostružiník, Maliník, Líska) must not become `natural=tree`.
- Category → tag (same as the Czech file): Jabloň genus=Malus; Hrušeň genus=Pyrus; Ořešák species=Juglans regia;
  Třešeň species=Prunus avium; Višeň species=Prunus cerasus; Švestka species=Prunus domestica; Myrobalán
  species=Prunus cerasifera; Morušovník genus=Morus; Kaštan jedlý species=Castanea sativa.
- ZBGIS: the catalogue has solitary trees and orchards as land cover, not species; this is a volunteer source for what ZBGIS lacks.
- Contact: Na ovoce, z.s., team@na-ovoce.cz (https://na-ovoce.cz/web/kontakt). One consent covers CZ and SK; the
  Slovak community can coordinate with the Czech one.

## Wiki entry
```
=== Na ovoce – ovocné stromy ===
* dataset: Na ovoce – mapa voľne rastúcich ovocných stromov (Mapotic 9288), slovenská časť
* správca: [https://na-ovoce.cz/ Na ovoce, z.s.]
* licencia: neuvedená („otevřená mapa“), treba vyžiadať súhlas [https://na-ovoce.cz/web/vyvoj-mapovaci-aplikace]
* dátové primitívy: body
* odkaz: https://www.mapotic.com/api/v1/maps/9288/pois.geojson/
* navrhované značky: {{tag|natural|tree}}, {{tag|genus|Malus}}, {{tag|species|Juglans regia}}
* poznámka: 4 936 bodov na Slovensku s druhom dreviny; v Banskej Bystrici má len 33 z 1 061 v OSM strom do 15 m
```
