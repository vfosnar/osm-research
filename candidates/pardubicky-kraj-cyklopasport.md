name: Cyklopasport Pardubického kraje – rozcestníky (značení), odpočívky, trasy
publisher: Pardubický kraj (data.pardubickykraj.cz)
url: https://data.pardubickykraj.cz/ (ArcGIS Hub items c1579b1fbd5949a599658850ac94be25 rozcestníky, 8b2c2bb2f53946bca23079e57bd9cda9 odpočívky, 5068a184a052451eb1d59a3dc6dfea08 trasy)
format: ArcGIS FeatureServer: https://services.arcgis.com/S6UQzkU4EoJgYA53/arcgis/rest/services/Cyklopasport_rozcestniky/FeatureServer/8 ; .../Cyklopasport_odpocivky/FeatureServer/7 ; .../Cyklopasport_trasy/FeatureServer/4 (hub download GeoJSON/CSV/SHP)
coords: yes
records: rozcestníky/značení 8,722 points (ZNACENI_OL: 5,731 silniční, 2,528 pásové, 387 jiné…); odpočívky 1,015 points (399 lavice se stolem, 261 lavice, 191 mapa, 128 informační tabule, 23 tabule, 1 samoobslužný servis…); trasy 379 line sections (trasa name, úroveň nadregionální/regionální, úsek)
osm_tags: odpočívky → leisure=picnic_table / amenity=bench / tourism=information + information=board|map (+ bicycle=yes), amenity=waste_basket (KOS), covered/shelter (KRYTE); značení → tourism=information + information=guidepost + bicycle=yes (only where it is a directional sign; strip/road markers = information=route_marker); trasy → QA for route=bicycle relations
osm_count_cz: information=guidepost 27,839; leisure=picnic_table 8,749; amenity=bench 89,222 (taginfo CZ 2026-09-26)
license: CC0 (item licenseInfo "CC0")
license_url: https://creativecommons.org/publicdomain/zero/1.0/
license_status: ok
update_freq: survey 2021 (photo filenames IMG_20210902…); layer last edited 2024-02-08, item modified 2024-11
impact: 3
verified: yes

## Notes
- OSM in a Pardubický-kraj bbox (15.40,49.60,16.90,50.15 – includes border strips of neighbouring regions; Postpass 2026-09-27): information=guidepost 2,830 (1,051 with bicycle=yes/guidepost=bicycle), picnic_table 980, bench 7,513. Dataset adds up to ~660 benches/tables along cycle routes and fills cycle-sign gaps.
- Rozcestníky layer has almost no attributes (only FOTO1/FOTO2 filenames, POZN, ZNACENI_OL); photos not public. "silniční" = road-type cycle sign (IS 19/IS 20 style), "pásové" = painted strip marks — the latter are route markers, not guideposts. Use mainly as QA for route=bicycle relations, not blind import.
- Odpočívky has rich attributes: MAJITEL, SPRAVCE, KOS, KRYTE, MAPA, INFO_TAB, STOJAN_KOL, PUMPA, VODA, SAMO_SERVI, TYP → good for leisure=picnic_table/amenity=bench with covered=*, and amenity=bicycle_repair_station for "samoobslužný servis".
- Trasy: 379 sections with names like "Praha – Brno" (nadregionální) – compare with route=bicycle relations (network=ncn/rcn) for missing sections.
- Suggested ref: `ref:cyklopasport:pk=<OBJECTID>` only for odpočívky (KID field also present).
- Contact: Krajský úřad Pardubického kraje, odbor rozvoje (via data.pardubickykraj.cz).
- Wiki pages read: Tag:information=guidepost, Tag:leisure=picnic_table, Tag:amenity=bench, Tag:amenity=bicycle_repair_station, Tag:amenity=shelter.

## Wiki entry
```
===Cyklopasport Pardubického kraje===
* dataset: Cyklopasport – rozcestníky, odpočívky, trasy
* gestor: [https://data.pardubickykraj.cz/ Pardubický kraj]
* licence: CC0 [https://creativecommons.org/publicdomain/zero/1.0/]
* datové primitivy: body (značení, odpočívky), linie (trasy)
* odkaz: https://services.arcgis.com/S6UQzkU4EoJgYA53/arcgis/rest/services/Cyklopasport_odpocivky/FeatureServer/7
* navržený tag {{tag|leisure|picnic_table}}, {{tag|amenity|bench}}, {{tag|information|guidepost}} + {{tag|bicycle|yes}}
* poznámka: 1 015 odpočívek a 8 722 bodů cykloznačení z terénního pasportu 2021; vhodné hlavně k doplnění laviček/stolů a kontrole cyklotras.
```
