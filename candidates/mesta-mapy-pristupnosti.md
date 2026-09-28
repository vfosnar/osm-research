# City accessibility maps (Mapa přístupnosti) – Brno, Ostrava, Hradec Králové

| Field | Value |
|---|---|
| publisher | Statutární město Brno, Odbor zdraví (IČO 44992785); Statutární město Ostrava (map run with the city's advisory service Bez bariér Ostravsko, https://www.ostrava-bezbarier.cz/); Statutární město Hradec Králové ("Bezbariérový Hradec", mapped with Centrum pro integraci osob se zdravotním postižením Královéhradeckého kraje and TyfloCentrum Hradec Králové) |
| url | Brno: https://services6.arcgis.com/fUWVlHWZNxUvTUh8/arcgis/rest/services/mapa_pristupnosti_budovy/FeatureServer/0 (buildings), https://services6.arcgis.com/fUWVlHWZNxUvTUh8/arcgis/rest/services/vstupy_budov/FeatureServer/0 (accessible entrances), file downloads under https://gis.brno.cz/public/opendata/mapr_g_budovy_b_wgs84.gpkg. Ostrava: https://mapy.ostrava.cz/arcgisserver/rest/services/SMO_Pristupnost/mapa_pristupnosti/MapServer/8. Hradec Králové: https://geoportal.mmhk.cz/arcgis/rest/services/thematic_bariery (services nevidomi, vozickari, neslysici, ost_objekty, mapovane_trasy) |
| format | ArcGIS REST (Brno FeatureServer, Ostrava and Hradec MapServer with Query enabled; outSR=4326 works); Brno also GeoJSON/GPKG/SHP/CSV |
| coords | yes |
| records | Brno: 287 buildings (189 přístupné, 63 s asistencí, 35 nepřístupné; 89 surgeries/hospitals, 30 offices, 25 museums/galleries, 20 pharmacies…; name, address, phone, web, accessible WC flag, 14 pictogram flags, long Czech/English descriptions; all updated 2025–2026) + 62 accessible entrances with direction. Ostrava: 2,060 points with a 3-level rating (447/343/210 in the first 1,000) and subcategory (1,066 public-transport stops, 994 buildings: shops, offices, surgeries, schools, banks, toilets…); no names in the layer (`id_wp` links to the web page). Hradec Králové, blind layers: 168 buildings (15 flagged with orientation voice beacons, `MAJACEK`=1), 72 stops, 177 crossings (tactile elements, light and acoustic signals), 321 route segments (natural/artificial guide lines); wheelchair layers: 149 buildings (entrance, door width, steps, accessible WC), 181 crossing problems, 22 stops; 5 induction loops; 7 public toilets |
| osm_tags | wheelchair=yes/limited/no (wiki Key:wheelchair), toilets:wheelchair=yes (wiki Tag:amenity=toilets), wheelchair:description:cs (used by Cs:Import Mapy bez bariér); entrances: entrance=* + wheelchair=yes; Hradec blind layers: tactile_paving=yes/no (wiki Key:tactile_paving), traffic_signals:sound=yes/no (wiki Key:traffic_signals:sound), blind=yes/limited/no only where no specific tag fits (wiki Key:blind); voice beacons: no established tag (taginfo CZ: acoustic_beacon=yes 2 uses) |
| osm_count_cz | wheelchair 53,314; wheelchair:description 151; tactile_paving 99,839; traffic_signals:sound 3,911 (taginfo 2026-09-28). Local match against the 2026-09-27 Czechia extract: Brno 116 of 287 buildings and Ostrava 763 of 994 buildings have no wheelchair-tagged OSM object within 30 m. Hradec Králové (OSM API, 2026-09-28): 868 of 999 OSM crossings in the centre already carry tactile_paving |
| license | Brno: CC BY 4.0 (NKOD terms: database not protected by the sui generis right). Ostrava and Hradec Králové: no licence stated, not in NKOD |
| license_url | https://creativecommons.org/licenses/by/4.0/ (Brno) |
| license_status | needs_waiver (Brno); unclear (Ostrava, Hradec Králové) |
| update_freq | Brno every 3 years plus corrections (dataset description); Ostrava and Hradec Králové irregular |
| impact | 3 |
| verified | yes |

## Try it
- **Map preview:** [samples/mesta-mapy-pristupnosti.geojson](../samples/mesta-mapy-pristupnosti.geojson): all 287 Brno buildings (name, type, rating, accessible WC, address). Ostrava and Hradec Králové are not included (licence unclear).
- **QGIS:** *Layer → Add Layer → Add ArcGIS REST Server Layer → New*:
  - Brno: URL `https://services6.arcgis.com/fUWVlHWZNxUvTUh8/arcgis/rest/services/mapa_pristupnosti_budovy/FeatureServer` (tested: 287 points), entrances `…/vstupy_budov/FeatureServer` (62 points).
  - Ostrava: URL `https://mapy.ostrava.cz/arcgisserver/rest/services/SMO_Pristupnost/mapa_pristupnosti/MapServer`, layer 8 "Kategorizace přístupnosti" (2,060 points, max 1,000 per request).
  - Hradec Králové: URL `https://geoportal.mmhk.cz/arcgis/rest/services/thematic_bariery`, services *nevidomi* (layers 1–4), *vozickari* (1–3), *neslysici* (1), *ost_objekty*. CRS EPSG:5514.
- **Web:** Brno https://data.brno.cz/datasets/cca344ea2fb24eecb4e449c5970fd401_0, Ostrava https://mapy.ostrava.cz/mapa-pristupnosti/mapa/, Hradec Králové https://geoportal.mmhk.cz/mapa/mapa-bezbariery/

## Notes
- **Not known:** none of the three appears on Cs:Česko/freemap, Cs:Zdroje_v_jednani or in Sync `config.toml` (checked 2026-09-28). Cs:Import Mapy bez bariér imports the national POV project mapybezbarier.cz (castles, museums, churches); these city maps use the same methodology (Metodika kategorizace přístupnosti objektů, POV) but cover offices, surgeries, pharmacies, banks, shops and stops. The index of Czech accessibility maps at https://www.ostrava-bezbarier.cz/studie-rady-informace/mapy-pristupnosti-cr/ lists more cities (see open leads).
- **Brno (best source):** rich, current (198 records updated 2026), openly licensed. The healthcare records cover the whole city, the rest only the centre. The rating maps directly to wheelchair=yes/limited/no, the `wc` field to toilets:wheelchair. 171 of 287 already have some wheelchair-tagged OSM object within 30 m, but that radius is loose in the centre, so part of those 171 still lack the tag on the right object. The `GlobalID` is stable; suggested `ref:brno:pristupnost=<GlobalID>` if the community wants Sync.
- **Ostrava:** the largest set (2,060 rated points) but the layer has only rating + subcategory, no name; names and descriptions are on ostrava-bezbarier.cz pages that the WordPress API does not expose. Matching must be spatial against existing OSM POIs of the right type. The 1,066 stop ratings could fill wheelchair=* on highway=bus_stop / railway=tram_stop; only 74 of them have a wheelchair-tagged OSM object within 30 m.
- **Hradec Králové (blind-specific):** the only city layer found that records what blind people need: tactile elements and acoustic signals on 177 crossings, Braille/contrast notes on 72 stops, orientation voice beacons on 15 buildings (Terminál MHD 3 beacons, Krajský úřad 7…), guide lines on 321 route segments. But OSM in Hradec is already well mapped: 135 of the 139 surveyed crossings that have an OSM crossing within 25 m carry tactile_paving; only 10 crossings with tactile paving and 4 with acoustic signals are missing, and all 59 matched stops have tactile_paving. The added value is the voice beacons and the qualitative notes, not bulk tags. The project started before 2014 (Zlatý erb award that year); the city page says the map is updated continuously, but the layers carry no survey dates, so check on the ground.
- **Voice beacons in general:** No public list of installed orientation voice beacons was found from SONS, the Centrum pro nevidomé pages on VPN transmitters, or the manufacturers. Hradec Králové's 15 flagged buildings are the only machine-readable record found.
- **Licence:** Brno CC BY 4.0 → consent from Magistrát města Brna, Odbor zdraví (named as author in NKOD). Ostrava: ask Magistrát města Ostravy / Bez bariér Ostravsko (poradenství bez bariér). Hradec Králové: ask Magistrát města Hradec Králové, odbor sociálních věcí a zdravotnictví (named on the Bezbariérový Hradec page as the organiser).
- Wiki pages read: Key:wheelchair, Key:tactile_paving, Key:traffic_signals:sound, Key:blind, OSM for the blind, Cs:Import Mapy bez bariér.

## Wiki entry
```
===Mapy přístupnosti měst (Brno, Ostrava, Hradec Králové)===
* dataset: Mapa přístupnosti – Budovy, Vstupy do budov (Brno); Kategorizace přístupnosti (Ostrava); Bezbariérový Hradec (Hradec Králové)
* gestor: [https://data.brno.cz/ Statutární město Brno], [https://mapy.ostrava.cz/mapa-pristupnosti/mapa/ Statutární město Ostrava], [https://geoportal.mmhk.cz/mapa/mapa-bezbariery/ Statutární město Hradec Králové]
* licence: Brno CC BY 4.0 [https://creativecommons.org/licenses/by/4.0/]; Ostrava a Hradec Králové neuvedena
* datové primitivy: body, linie
* odkaz: https://services6.arcgis.com/fUWVlHWZNxUvTUh8/arcgis/rest/services/mapa_pristupnosti_budovy/FeatureServer/0
* navržený tag {{tag|wheelchair|yes/limited/no}}, {{tag|toilets:wheelchair|yes}}, {{tag|tactile_paving|yes}}, {{tag|traffic_signals:sound|yes}}
* poznámka: v Brně 116 z 287 a v Ostravě 763 z 994 hodnocených budov nemá v OSM do 30 m žádný objekt s tagem wheelchair; nutný souhlas (Brno CC BY 4.0) nebo zjištění licence
```
