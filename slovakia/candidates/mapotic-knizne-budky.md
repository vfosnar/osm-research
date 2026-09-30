# Knižné búdky (public bookcases map on Mapotic)

| Field | Value |
|---|---|
| publisher | private Mapotic account (owner shown as "Richard P."; map id 9019, slug `knizne-budky`, https://www.mapotic.com/knizne-budky) |
| url | https://www.mapotic.com/api/v1/maps/9019/pois.geojson/ |
| format | GeoJSON FeatureCollection (Mapotic API, anonymous) |
| coords | yes (WGS84 points) |
| records | 161 POIs, 155 inside Slovakia: 147 "exteriérové knihobúdky" (outdoor), 14 "interiérové knihobúdky" (indoor, in hospitals, polyclinics, bus shelters); 2 names flagged "NEFUNKČNÁ" (not working) |
| osm_tags | `amenity=public_bookcase` (Tag:amenity=public_bookcase, node or area), `indoor=yes` or `level` for the indoor ones, `capacity`, `operator` |
| osm_count_sk | amenity=public_bookcase 189 (taginfo, data until 2026-09-29) |
| license | none stated (no custom terms on the map); Mapotic terms give other users no rights to content |
| license_url | https://www.mapotic.com/terms/ |
| license_status | unclear |
| update_freq | crowdsourced (`enabled_crowd_sourcing: true`); last_update 2021 85, 2022 4, 2023 15, 2024 5, 2025 37, 2026 15 |
| impact | 2 |
| sync_fit | MapRoulette (small, no official id, fuzzy match against nearby bookcases) |
| verified | yes |

## Try it

- **Map preview:** none (licence unclear). Web map: https://www.mapotic.com/knizne-budky
- **QGIS:** *Layer → Add Layer → Add Vector Layer*, *Protocol: HTTP(S)*, type *GeoJSON*, URI
  `https://www.mapotic.com/api/v1/maps/9019/pois.geojson/` (tested 2026-09-30: 161 points).

## Notes

- The Czech KnihoBudka map (`candidates/knihobudka-verejne-knihovnicky.md`) has no Slovak entries (its feed has 1,538 rows,
  none in Slovakia apart from two border points in Hodonín). This Mapotic map is the only Slovak bookcase list found.
- Clusters: Martin (16), Košice (about 25 in three cells, many of them in hospitals), Bratislava (10), Poprad (7).
- **Gap (whole Slovakia, Postpass 2026-09-30):** of the 155 Slovak points, **only 36 have an `amenity=public_bookcase`
  within 100 m; 119 (77 %) have none.** OSM already has 189 bookcases, so the two sets overlap little and together
  would roughly double the Slovak count.
- Names carry the location ("Knihobúdka na Brigádnickej ulici", "Knižná skriňa v Novej nemocnici") and should go to
  `name` or `description`. Skip entries marked "NEFUNKČNÁ".
- Contact: the map owner through Mapotic (map page → contact owner).

## Wiki entry
```
=== Knižné búdky (Mapotic) ===
* dataset: Knižné búdky – knihobúdky, knižné skrine (Mapotic 9019)
* správca: [https://www.mapotic.com/knizne-budky súkromný účet na Mapotic]
* licencia: neuvedená, treba vyžiadať súhlas [https://www.mapotic.com/terms/]
* dátové primitívy: body
* odkaz: https://www.mapotic.com/api/v1/maps/9019/pois.geojson/
* navrhované značky: {{tag|amenity|public_bookcase}}, {{tag|indoor|yes}}
* poznámka: 155 knihobúdok na Slovensku, 119 z nich nemá v OSM do 100 m amenity=public_bookcase
```
