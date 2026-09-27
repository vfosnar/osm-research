```
name: ČHMÚ – metadata meteorologických, klimatologických a srážkoměrných stanic (station list behind the open climate data)
publisher: Český hydrometeorologický ústav (ČHMÚ), IČO 00020699
url: https://opendata.chmi.cz/meteorology/climate/now/metadata/meta1-20260927.json (a new dated file every day; the directory https://opendata.chmi.cz/meteorology/climate/now/metadata/ lists them). NKOD: https://data.gov.cz/zdroj/datové-sady/00020699/2f5c5838ee15a8a7264a04d2b1687ef0
format: JSON (DataCollection: header WSI,GH_ID,FULL_NAME,GEOGR1(lon),GEOGR2(lat),ELEVATION,BEGIN_DATE); meta2 = the elements measured at each station
coords: yes (WGS84)
records: 765 rows, 764 inside the CZ bbox and 760 unique stations (GH_ID). 40 are WMO synoptic stations (WSI 0-20000-0-xxxxx) and 724 are national stations (WSI 0-203-0-xxxx)
osm_tags: man_made=monitoring_station + monitoring:weather=yes (for precipitation-only stations, monitoring:precipitation=yes) + name + ele + operator=Český hydrometeorologický ústav + operator:short=ČHMÚ + operator:wikidata=Q5201751 + ref:wigos=<WSI>
osm_count_cz: man_made=monitoring_station 1,540; monitoring:weather=yes 210; monitoring:precipitation=yes 10; ref:wmo 8; ref:wigos 1 (Geofabrik taginfo, 2026-09-27)
license: CC BY 4.0 (NKOD distribution of the "Aktuální meteorologická data … 10 minut a 1 hodina" dataset, which contains the metadata files). NB: the separate INSPIRE station layer (stanice_CHMU_2024_epsg4258.gpkg, NKOD …/a6dd7826d86120a6ecf42a902fa82aca) is CC BY-NC-ND 4.0, so do not use it
license_url: https://creativecommons.org/licenses/by/4.0/
license_status: needs_waiver
update_freq: daily (metadata file regenerated each day)
impact: 2
verified: yes
```

## Notes
- **Why it is here:** Mapy.com's official data-source list ("Zdroje dat", https://licence.mapy.com/?doc=mapy_attr) credits "© Český hydrometeorologický ústav" for points of interest. This is the open station list behind that credit. The gauging-station half is covered separately in `chmu-vodomerne-stanice.md`.
- **Partly known:** ZABAGED "Meteorologická stanice" (ČHMÚ + ŘSD + army + ÚFA) has already been imported (✅ on Cs:POI_ZABAGED_Import) and is in Sync (`[group.zabaged.dataset.…]` with `man_made=monitoring_station`). The new parts are:
  - stable WIGOS IDs (`ref:wigos`), which are almost absent in CZ (1 use; 8 legacy `ref:wmo`);
  - the precipitation-only network. Hundreds of srážkoměrné stanice are probably not in ZABAGED.
  - start dates and elevation.
- **Gap (Postpass, CZ bbox, 2026-09-27):** 314 of the 760 stations have an OSM `man_made=monitoring_station` within 150 m and 332 within 500 m, which leaves about 430 unmatched. Most of the unmatched ones are probably volunteer precipitation gauges in private gardens. Map them only if they are visible or verifiable (the wiki does not forbid it, but it is borderline "verifiable"). The main value is adding `ref:wigos` to the ~300 existing stations.
- **Wiki pages read:** Tag:man_made=monitoring_station (monitoring:weather, monitoring:precipitation) and Key:ref:wigos (`ref:wmo` redirects to it, and `ref:wigos` "requires" monitoring:weather=yes).
- **Licence caveat:** ČHMÚ publishes the same stations under two conflicting licences: CC BY 4.0 on opendata.chmi.cz and CC BY-NC-ND 4.0 on the INSPIRE GPKG/WFS. Ask ČHMÚ for an explicit OSM consent that covers the station metadata. Do this together with the request for the gauging stations (one letter to ČHMÚ, opendata@chmi.cz / ČHMÚ Oddělení datových služeb).

## Wiki entry
```
===ČHMÚ – meteorologické a srážkoměrné stanice===
* dataset: Aktuální meteorologická data měřená v síti stanic ČHMÚ – metadata stanic (meta1)
* gestor: [https://www.chmi.cz/ Český hydrometeorologický ústav]
* licence: CC BY 4.0 [https://creativecommons.org/licenses/by/4.0/] (INSPIRE vrstva stanic je CC BY-NC-ND 4.0 – nepoužívat)
* datové primitivy: body
* odkaz: https://opendata.chmi.cz/meteorology/climate/now/metadata/
* navržený tag {{tag|man_made|monitoring_station}}, {{tag|monitoring:weather|yes}}, {{tag|operator|Český hydrometeorologický ústav}}, {{tag|ref:wigos|<WSI>}}
* poznámka: 760 stanic, v OSM do 150 m jen 314; hlavně doplnění ref:wigos k již importovaným stanicím ZABAGED (potřeba souhlasu ČHMÚ)
```
