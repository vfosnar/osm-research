# VozickarMAP (accessibility map of vozmen, n.o.)

| Field | Value |
|---|---|
| publisher | vozmen, n.o. (Mapotic map id 3480, `owner_name` "Miroslav Zeman - vozmen, n.o."; web map https://vozickar-map.mapotic.com/, apps "VozickarMAP" on Google Play and the App Store, both linked from the map metadata) |
| url | https://www.mapotic.com/api/v1/maps/3480/pois.geojson/ |
| format | GeoJSON FeatureCollection (Mapotic API, anonymous), 5,716 points, per point `id`, `name`, `category_name` (sk/en), `last_update`, `rating` |
| coords | yes (WGS84 points) |
| records | 5,716 POIs, 2,878 inside Slovakia (point-in-polygon against OSM relation 14296, simplified). SK by category: Parkovacie miesto pre vozičkárov 878, Obchod 477, Gastro 298, Turistický cieľ 196, Benzínová pumpa 138, Obchodné centrum 106, Lekáreň 79, Ubytovanie 78, Služby 73, Banka 71, Šport/Zábava 49, Verejné WC 47, Zastávka 39, Úrad 37, AED 25, other 287. The rest of the map is in Czechia |
| osm_tags | disabled parking: `amenity=parking_space` + `parking_space=disabled` (Tag:parking_space=disabled, status de facto, on nodes and areas) or `capacity:disabled=*` on a car park (Key:capacity:disabled); other categories: `wheelchair=yes\|limited` on the existing POI |
| osm_count_sk | parking_space=disabled 1,352; capacity:disabled 2,218 (taginfo, data until 2026-09-29) |
| license | none stated; the map has no custom terms (`has_custom_terms: false`) and no licence field. Mapotic terms (https://www.mapotic.com/terms/) give other users no rights to content |
| license_url | https://www.mapotic.com/terms/ |
| license_status | unclear |
| update_freq | crowdsourced (`enabled_crowd_sourcing: true`). SK POI last_update: 2019 385, 2020 1,239, 2021 49, 2022 43, 2023 770, 2024 246, 2025 115, 2026 31. Disabled parking in SK: 644 of 878 last touched in 2020 |
| impact | 4 |
| sync_fit | MapRoulette (disabled parking: point → check imagery, tag parking_space=disabled or capacity:disabled; no publisher ref, the Mapotic POI id is stable but not an official ID; other categories are wheelchair enrichment of existing POIs) |
| verified | yes |

## Try it

- **Map preview:** none (licence unclear). Web map: https://vozickar-map.mapotic.com/
- **QGIS:** *Layer → Add Layer → Add Vector Layer*, source type *Protocol: HTTP(S)*, type *GeoJSON*, URI
  `https://www.mapotic.com/api/v1/maps/3480/pois.geojson/` (tested 2026-09-30: FeatureCollection of 5,716 points).
  `category_name` is a JSON object with `cs` and `en`; style by `category`, which is the numeric category id.

## Notes

- This is the Slovak counterpart of VozejkMap (CZEPA, Czech research), run by a different organisation (vozmen, n.o.),
  with the interface in Slovak. It is the only large Slovak accessibility layer found on Mapotic (full scan of map ids 1 to 33,755 on 2026-09-30:
  207 maps centred in Slovakia or with `lang=sk`; the next accessibility map is "Verejné WC Vysoké Tatry" with 22 POIs).
- **Gap (Bratislava, bbox 16.95,48.05,17.35,48.28, Postpass 2026-09-30):** 434 VozickarMAP disabled-parking points.
  Only **78 (18 %)** have an OSM object tagged `parking_space=disabled`, `capacity:disabled` or `wheelchair=yes|designated`
  on a parking object within 30 m. 354 have some `amenity=parking|parking_space` within 30 m, so most would be an
  attribute addition (capacity:disabled on the car park, or a new parking_space=disabled node inside it).
- Names of the parking points are generic ("Vozičkárske parkovacie miesto" 538, "Parkovisko" 94, "Parking invalid" 72).
  Some Bratislava spots may be reserved for one registered disabled resident (vyhradené parkovanie for a named
  licence plate). Those are still `parking_space=disabled`, but the mapper should check the sign when surveying.
- Non-parking categories (shops, gastro, petrol stations) mark places the community rated as accessible; the per-POI
  detail with the accessibility attributes needs authentication on Mapotic (`/pois/<id>/` returns 401), so only the
  category and the rating are public. Ask the owner for an export with the attributes.
- No ZBGIS type covers disabled parking or accessibility; municipal "bezbariérové miesta" datasets exist only for
  a few towns in the national catalogue (Senica, Myjava).
- Suggested ref if the owner agrees to a sync: `ref:vozickarmap=<Mapotic POI id>`.
- Contact: vozmen, n.o. through the VozickarMAP apps or the Mapotic map (owner account "Miroslav Zeman - vozmen, n.o.").
  vozmen.org and vozickar.info returned a web-application-firewall block page from this environment.

## Wiki entry
```
=== VozickarMAP ===
* dataset: VozickarMAP – bezbariérové miesta (mapa Mapotic 3480)
* správca: [https://vozickar-map.mapotic.com/ vozmen, n.o.]
* licencia: neuvedená, treba vyžiadať súhlas [https://www.mapotic.com/terms/]
* dátové primitívy: body
* odkaz: https://www.mapotic.com/api/v1/maps/3480/pois.geojson/
* navrhované značky: {{tag|amenity|parking_space}} + {{tag|parking_space|disabled}}, {{tag|capacity:disabled|<počet>}}, {{tag|wheelchair|yes}}
* poznámka: 878 parkovacích miest pre vozičkárov na Slovensku; v Bratislave 356 zo 434 (82 %) nemá v OSM do 30 m žiadne vyhradené parkovanie
```
