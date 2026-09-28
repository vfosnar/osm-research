# Na ovoce – volně dostupné ovocné stromy a keře

| Field | Value |
|---|---|
| publisher | Na ovoce, z.s. (IČ 04380215), Mapotic map id 9288, web map https://map.na-ovoce.cz/ |
| url | https://www.mapotic.com/api/v1/maps/9288/pois.geojson/ |
| format | GeoJSON FeatureCollection (Mapotic API, no key needed for this endpoint), 9 MB |
| coords | yes (WGS84 points) |
| records | 26,278 POIs, 20,816 in the CZ bbox (the rest mostly Slovakia). In the CZ bbox: Jabloň 3,166, Ořešák 2,668, Třešeň 2,642, Myrobalán 1,883, Šípková růže 1,614, Švestka 1,336, Bez černý 1,247, Hrušeň 1,134, Ostružiník 771, Líska 728, Višeň 356, other species 3,271; also categories Sady (orchards) and Ovocné trasy (fruit routes) |
| osm_tags | natural=tree + genus/species (wiki Tag:natural=tree, Key:species); orchards landuse=orchard |
| osm_count_cz | natural=tree 136,307; species 2,442; genus 3,123 (taginfo 2026-09-27). Local match against the 2026-09-27 Czechia extract (Postpass unavailable): 19,257 of 19,571 Na ovoce points inside the CZ border (98.4 %) have no natural=tree within 10 m; of the 314 that do, 13 have genus/species/taxon |
| license | none published; the association calls it an "otevřená mapa" (open map) on https://na-ovoce.cz/web/vyvoj-mapovaci-aplikace, but no licence is stated. Mapotic terms (https://www.mapotic.com/terms/) give other users no rights to content |
| license_url | https://na-ovoce.cz/web/vyvoj-mapovaci-aplikace |
| license_status | unclear |
| update_freq | crowdsourced by volunteers; 21,383 records carry a 2021 last_update (migration to Mapotic), then 571–1,249 changes a year (2026: 999) |
| impact | 3 |
| verified | yes |

## Try it
- **Map preview:** none (licence unclear). Web map: https://map.na-ovoce.cz/.
- **QGIS:** *Layer → Add Layer → Add Vector Layer*, source type *Protocol: HTTP(S)*, type *GeoJSON*, URI `https://www.mapotic.com/api/v1/maps/9288/pois.geojson/` (tested 2026-09-27: FeatureCollection of 26,278 points). The species is in `category_name` (Czech and English), so style by that field.

## Notes
- **Gap (Prague 6 – Střešovice/Břevnov, bbox 14.37,50.09,14.39,50.11, OSM API data fetched 2026-09-28; Postpass returned 503 all session):** 309 Na ovoce points (Hrušeň 132, Švestka 41, Hloh 38, Myrobalán 32, Třešeň 13, Ořešák 12). OSM has 1,498 natural=tree there, only 41 with species/genus. **219 of 309 (71 %) have no OSM tree within 10 m**, and of the 90 that do, only 1 has a genus or species tag.
- **Gap, national (local match against the 2026-09-27 Czechia extract, Postpass unavailable; same rule,
  natural=tree node or way within 10 m; 145,062 OSM trees in the extract; points inside the CZ border):**
  19,571 Na ovoce points. Only **314 (1.6 %)** have an OSM tree within 10 m, and of those only 13 carry genus,
  species or taxon. By type: tree categories (Jabloň, Třešeň, Ořešák, Myrobalán, Švestka, Hrušeň, Višeň,
  Morušovník, Kaštan jedlý, Jeřáb and other trees) 13,185 points, 258 with an OSM tree within 10 m, 12 of them
  with a species tag; shrub and herb categories 6,334 points, 56 near an OSM tree (a coincidence, since shrubs
  are not trees); Sady and Ovocné trasy 52, none. The Prague 6 sample (90 of 309 matched) is not
  representative of the country: the national matched share is far lower. The same extract reproduces the
  Prague 6 figure exactly (90 of 309), so the difference is real and not a method artefact.
- Nationally OSM Czechia has about 3,100 genus and 2,400 species tags in total; Na ovoce alone names the species of 20,816 plants, so even where the tree exists the species is a clear add.
- Positions come from volunteers' phones and are not survey-grade. Use as a review layer (tree exists? add genus/species), not a blind import. Shrub categories (Šípková růže, Bez černý, Ostružiník, Maliník, Borůvka, Líska) are not trees and should not become natural=tree.
- Category → tag: Jabloň genus=Malus; Hrušeň genus=Pyrus; Ořešák species=Juglans regia; Třešeň species=Prunus avium; Višeň species=Prunus cerasus; Švestka species=Prunus domestica; Myrobalán species=Prunus cerasifera; Morušovník genus=Morus; Kaštan jedlý species=Castanea sativa (wiki Key:species asks for the scientific name).
- The "Sady" category (orchards) is the other useful layer: many are old public orchards that OSM may lack as landuse=orchard.
- Na ovoce publishes a code of conduct (https://www.na-ovoce.cz/kodex) for picking; only publicly accessible plants are meant to be mapped, so there is no private-garden issue like the Kokoza vermicomposters.
- The Mapotic POI `id` is stable; the per-POI detail endpoint returns 401, so notes and photos are not anonymous.
- **Not known upstream:** not on Cs:Česko/freemap, Cs:Zdroje_v_jednani or in Sync config.toml (grep 2026-09-27); the OSM wiki full-text search for "na ovoce" only matches unrelated shop/landuse pages.
- **Licence / contact:** Na ovoce, z.s., team@na-ovoce.cz, coordinator Katka Kubánková (https://na-ovoce.cz/web/kontakt). Since they already call the map open, ask them to put an explicit ODbL/CC0 licence on it.
- Wiki pages read: Tag:natural=tree, Key:species.

## Wiki entry
```
===Na ovoce===
* dataset: Na ovoce – mapa volně dostupných ovocných stromů a keřů (mapa Mapotic)
* gestor: [https://na-ovoce.cz/ Na ovoce, z.s.]
* licence: neuvedena („otevřená mapa“), nutné vyžádat souhlas
* datové primitivy: body
* odkaz: https://www.mapotic.com/api/v1/maps/9288/pois.geojson/
* navržený tag {{tag|natural|tree}} + {{tag|genus|<rod>}} / {{tag|species|<druh>}}
* poznámka: 20 816 ovocných stromů a keřů s druhem; u 19 257 z 19 571 bodů v Česku (98 %) není v OSM do 10 m žádný strom a z 314 nalezených má rod nebo druh jen 13
```
