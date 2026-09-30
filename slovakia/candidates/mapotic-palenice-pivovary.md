# Pálenice a pivovary Slovenska (hobby maps on Mapotic)

| Field | Value |
|---|---|
| publisher | private Mapotic account (owner shown as "Pivní B."), two maps: "Pálenice Slovenska" (id 3857, https://www.mapotic.com/palenice-slovenska) and "Pivovary Slovenska" (id 2006, https://www.mapotic.com/pivovary-slovenska) |
| url | https://www.mapotic.com/api/v1/maps/3857/pois.geojson/ ; https://www.mapotic.com/api/v1/maps/2006/pois.geojson/ |
| format | GeoJSON FeatureCollection (Mapotic API, anonymous) |
| coords | yes (WGS84 points) |
| records | Pálenice: 229 (all in SK): Pestovateľská pálenica 191, Obecná pálenica 23, Liehovar 8, Ovocný liehovar 4, Likérka 3. Pivovary: 427: Pivovary 100, Pivotéky 87, Zrušené pivovary 77, Kočovné pivovary 74, Domovariči 44, Klientské pivovary 17, Veľkoobchod 9, Sladovne 7 |
| osm_tags | `craft=distillery` (Tag:craft=distillery, "an establishment for distilling"); `craft=brewery` (brewery) or `microbrewery=yes` on a pub/restaurant; `name`, `operator` |
| osm_count_sk | craft=distillery 69; craft=brewery 48 (taginfo, data until 2026-09-29) |
| license | none stated (no custom terms, crowdsourcing off: the owner curates both maps); Mapotic terms give other users no rights to content |
| license_url | https://www.mapotic.com/terms/ |
| license_status | unclear |
| update_freq | Pálenice: last_update 2019 17, 2021 208, 2025 4 (mostly static since 2021). Pivovary: maintained, 2024 110, 2025 84, 2026 18 changes |
| impact | 2 |
| sync_fit | MapRoulette (small, no official id; distillery category → craft=distillery 1:1, brewery vs brewpub needs a human) |
| verified | yes |

## Try it

- **Map preview:** none (licence unclear). Web maps: https://www.mapotic.com/palenice-slovenska , https://www.mapotic.com/pivovary-slovenska
- **QGIS:** *Layer → Add Layer → Add Vector Layer*, *Protocol: HTTP(S)*, type *GeoJSON*, URI
  `https://www.mapotic.com/api/v1/maps/3857/pois.geojson/` (229 points) or `…/maps/2006/pois.geojson/` (427 points),
  both tested 2026-09-30. Style by `category`.

## Notes

- The distillery map describes itself as "Kompletný zoznam oficiálnych pestovateľských pálenic na Slovensku".
  Pestovateľské pálenice (contract fruit distilleries for households) are licensed by the customs/tax administration;
  no open official list was found (web search and the national catalogue SPARQL for "páleni"/"liehovar" returned nothing on 2026-09-30).
- **Gap (whole Slovakia, Postpass 2026-09-30):**
  - Pálenice: of 229 points, **only 53 have** a `craft=distillery`, `industrial=distillery` or an object named
    "*pálen*" within 150 m; **176 (77 %) have none**. OSM Slovakia has only 69 craft=distillery in total.
  - Active breweries (categories Pivovary + Klientské pivovary, 117 in SK): 62 have a `craft=brewery`,
    `microbrewery=yes`, `industrial=brewery` or "*pivovar*" name within 150 m; **55 (47 %) have none**.
- Leave out closed breweries (Zrušené), gypsy brewers (Kočovné, no premises) and home brewers (Domovariči, private).
  Pivotéky (87 beer shops) could become `shop=alcohol`/`shop=beverages`, but they are ordinary businesses.
- Contact: the owner through Mapotic ("Pivní B."); the same account runs both maps.

## Wiki entry
```
=== Pálenice a pivovary Slovenska (Mapotic) ===
* dataset: Pálenice Slovenska (Mapotic 3857), Pivovary Slovenska (Mapotic 2006)
* správca: [https://www.mapotic.com/palenice-slovenska súkromný účet na Mapotic]
* licencia: neuvedená, treba vyžiadať súhlas [https://www.mapotic.com/terms/]
* dátové primitívy: body
* odkaz: https://www.mapotic.com/api/v1/maps/3857/pois.geojson/ , https://www.mapotic.com/api/v1/maps/2006/pois.geojson/
* navrhované značky: {{tag|craft|distillery}}, {{tag|craft|brewery}}, {{tag|microbrewery|yes}}
* poznámka: 176 z 229 pestovateľských páleníc a 55 zo 117 pivovarov nemá v OSM do 150 m zodpovedajúci objekt
```
