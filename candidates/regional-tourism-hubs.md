name: Krajské datové portály (ArcGIS Hub) – turistické POI vrstvy (rozhledny, infocentra, hrady/zámky, muzea, koupaliště, vleky, knihovny, Stromy republiky)
publisher: Královéhradecký kraj (datakhk.cz), Liberecký kraj (datalk.cz), Pardubický kraj (data.pardubickykraj.cz), Olomoucký kraj (dataok.cz), Karlovarský kraj (datazapad.cz), Moravskoslezský kraj (data.msk.cz), Jihomoravský kraj (data.jmk.cz)
url: https://www.datakhk.cz/ ; https://www.datalk.cz/ ; https://data.pardubickykraj.cz/ ; https://www.dataok.cz/ ; https://www.datazapad.cz/ ; https://data.msk.cz/ ; https://data.jmk.cz/
format: ArcGIS FeatureServer + hub downloads (GeoJSON/CSV/SHP)
coords: yes
records: small layers, typically 20–150 points each (e.g. KHK Rozhledny a vyhlídky 49; LK Stromy republiky 67; KVK Přístupné prameny 129; JMK Nabíjecí stanice elektrokol 154)
osm_tags: tourism=viewpoint / man_made=tower + tower:type=observation; tourism=information + information=office; historic=castle; tourism=museum; leisure=swimming_pool / leisure=water_park; aerialway=*; amenity=library; natural=tree + start_date + circumference (metres, Key:circumference); denotation=landmark rather than natural_monument unless legally protected (Key:denotation) (Stromy republiky: memorial trees planted 1918–1919)
osm_count_cz: tourism=artwork 12,102; natural=spring 4,844 (taginfo CZ); other tourism POIs are generally well mapped
license: KHK, LK, PK, OLK: CC0 (item licenseInfo "CC0" / "CC0 1.0"); KVK and MSK: CC BY 4.0 / "CC BY"; JMK: licenseInfo empty
license_url: https://creativecommons.org/publicdomain/zero/1.0/ ; https://creativecommons.org/licenses/by/4.0/
license_status: ok (KHK, LK, PK, OLK); needs_waiver (KVK, MSK); unclear (JMK)
update_freq: mostly one-off / annual
impact: 1
verified: partial

## Notes
- These are compiled tourism lists (castles, museums, infocentra, lookout towers, pools, lifts, libraries, theatres). All are high-profile POIs that are already in OSM nearly everywhere; value is only QA (website/phone/ref) — not import.
- Several layers are compiled from third-party sources: KVK "Přístupné prameny v Karlovarském kraji" (129) links every record to estudanky.eu (listed on Cs:Česko/freemap as CC BY-NC-ND, incompatible) → treat as contaminated; JMK "Nabíjecí stanice elektrokol" (154) was built from Mapy.cz/firmy.cz links → contaminated. Do not use either.
- Worth a look: Liberecký kraj "Stromy republiky" (67 trees planted 1918–1919 with planting date, girth, height; CC0) – small but nice enrichment (start_date, circumference). KHK/LK CC0 museum/castle layers could supply ref/website QA.
- Regional hubs verified via /api/search/v1/collections/dataset/items: data.brno.cz 199, datakhk 131, data.pardubickykraj 120, datazapad 88, datalk 83, dataok 74, data.msk 46, data.jmk 37 datasets. Other regions (Vysočina, JčK, ÚK, STČ, PLK, ZLK) have no ArcGIS Hub; their NKOD records are almost entirely DTM ZPS packages (see known-dtm-zps-kraje.md) — Plzeňský kraj links only a geoportal page, Zlínský kraj one API endpoint.
- Wiki pages read: Tag:natural=tree, Key:denotation, Key:circumference, Tag:natural=spring.

## Wiki entry
```
===Liberecký kraj – Stromy republiky===
* dataset: Stromy republiky
* gestor: [https://www.datalk.cz/ Liberecký kraj]
* licence: CC0 1.0 [https://creativecommons.org/publicdomain/zero/1.0/]
* datové primitivy: body
* odkaz: https://services7.arcgis.com/46Lck1orT7mvuzK5/arcgis/rest/services/Stromy_republiky/FeatureServer/0
* navržený tag {{tag|natural|tree}}, {{tag|start_date|1919}}, {{tag|circumference|2.80}}
* poznámka: 67 lip svobody/stromů republiky s datem výsadby a obvodem kmene; v OSM většinou bez těchto údajů.

===Královéhradecký kraj – turistické vrstvy===
* dataset: Rozhledny a vyhlídky; Infocentra; Hrady; Zámky; Muzea a galerie; Lanovky
* gestor: [https://www.datakhk.cz/ Královéhradecký kraj]
* licence: CC0 [https://creativecommons.org/publicdomain/zero/1.0/]
* datové primitivy: body
* odkaz: https://services6.arcgis.com/ogJAiK65nXL1mXAW/arcgis/rest/services/Rozhledny_a_vyhl%C3%ADdky/FeatureServer/0
* navržený tag {{tag|tourism|viewpoint}}, {{tag|tourism|information}}, {{tag|tourism|museum}}
* poznámka: Objekty jsou v OSM téměř všechny; využití jen ke kontrole webu/telefonu.
```
