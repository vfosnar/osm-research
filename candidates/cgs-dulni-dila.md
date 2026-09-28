# Důlní díla v České republice (registry of mine workings: shafts, adits, boreholes, collapses)

| Field | Value |
|---|---|
| publisher | Česká geologická služba (ČGS), IČO 00025798 |
| url | https://od.geology.cz/dulni_dila.zip (GeoJSON inside: dulni_dila.geojson, 56 MB); WFS https://mapy.geology.cz/arcgis/services/Dulni_Dila/dulni_dila/MapServer/WFSServer?request=GetCapabilities&service=WFS ; NKOD https://data.gov.cz/zdroj/datové-sady/00025798/2498e3343ea928eb374d534397f4d92a |
| format | GeoJSON (WGS84 points; S-JTSK coordinates also in attributes) |
| coords | yes |
| records | 30,891 (downloaded 2026-09-27; file dated 2026-09-27): Vrt 9,888, Jáma 9,208, Štola 4,435, Jiné 3,410, Šachtice 1,588, Komín 940, Propad 600, Úpadnice 450, Pinka 230, Dobývka 141 |
| osm_tags | Štola/Úpadnice -&gt; man_made=adit (abandoned ones: abandoned:man_made=adit, as used in CZ); Jáma/Šachtice -&gt; man_made=mineshaft (+ disused/abandoned lifecycle prefix, or historic=mine_shaft for historic ones); plus name, resource=*; suggested ref:cgs:dd=&lt;id_dd&gt; |
| osm_count_cz | man_made=adit 589, man_made=mineshaft 284, historic=mine_shaft 33, historic=mine 181, historic=mine_adit 8, abandoned:man_made=adit 51 (taginfo 2026-09-26) |
| license | CC BY 4.0 (NKOD terms spec: autorské dílo + DB as copyright work CC BY 4.0, no sui generis right, no personal data) |
| license_url | https://data.gov.cz/zdroj/datové-sady/00025798/2498e3343ea928eb374d534397f4d92a ; https://creativecommons.org/licenses/by/4.0/ |
| license_status | needs_waiver |
| update_freq | weekly (NKOD); file regenerated daily-ish (timestamp 2026-09-27 04:34) |
| impact | 3 |
| sync_fit | MapRoulette (lifecycle judgement: abandoned/historic/active) despite stable id_dd |
| verified | yes |

## Try it

- **Map preview:** [samples/cgs-dulni-dila.geojson](../samples/cgs-dulni-dila.geojson) has the 288 shafts and adits (Jáma, Šachtice, Štola, Úpadnice) around Příbram (bbox 13.9,49.62,14.1,49.74). `osm_mining_feature_within_50m` is true for only 19 of them (Postpass, 2026-09-27).
- **QGIS:** *Layer → Add Layer → Add Vector Layer…* → *File*, and paste `/vsizip/vsicurl/https://od.geology.cz/dulni_dila.zip/dulni_dila.geojson` into the dataset field. That loads 30,891 WGS84 points from a 3.6 MB download. Alternatively use *Add WFS Layer* with `https://mapy.geology.cz/arcgis/services/Dulni_Dila/dulni_dila/MapServer/WFSServer` (layer `dulni_dila:Důlní_díla`).

## Notes
- **Gap (Příbram bbox 13.9,49.62,14.1,49.74).** ČGS has 151 Jáma + 84 Šachtice + 53 Štola (+ others). Postpass finds only 19 `man_made=mineshaft` + 8 `man_made=adit` in OSM. Nationally OSM has ~900 shaft/adit features vs ~15,700 shafts and adits in the registry.
- **Caveat: surface visibility.** Many entries are sealed or backfilled shafts, or uranium workings (DIAMO manages 14,903 records; "Radioaktivní suroviny" 11,930). They may not be visible on the ground. Import only Jáma/Štola/Šachtice/Úpadnice. Skip Vrt (boreholes), Komín and Propad unless verified. Prefer lifecycle prefixes (`abandoned:`) for closed ones. The open file has no explicit "current state" field, although the dataset description mentions one. It carries `kategorie` (Opuštěné / Provozované / Staré / Neurčeno / "Není důlní dílo" 745, to be excluded), `rok_ukonceni_provozu`, `profil_dila`, `rozmery_usti`, `hloubka_delka`, `surovina`, `spravce`.
- **Useful for:** hiking and cave/mining-heritage maps (adit portals are landmarks), and hazard awareness. Collapses (Propad, 600) could map to `natural=sinkhole`, but check the wiki first.
- **IDs.** `id_dd` is unique (30,891 distinct) and has an IRI (https://registry.geology.cz/od/dulni_dila/<id>), so it is good for Sync. Suggested key `ref:cgs:dd`, which is undocumented and would need a Cs wiki entry. Record names (`nazev_dila`) are always filled, but are often generic ("jáma č. 5").
- **Wiki pages read (raw, 2026-09-27):** Tag:man_made=adit (node at portal), Tag:man_made=mineshaft (node or area, `mineshaft_type`), Tag:historic=mine_shaft, Tag:historic=mine. Cs:Key:historic has no mining-specific guidance.
- Photo links (`obr`) point to app.geology.cz. Do not copy them.
- Contact: ČGS open data (od.geology.cz; the directory index returns 403 but the files are public). Registry of mine workings: Geofond department of ČGS.

## Wiki entry
```
===Důlní díla (ČGS)===
* dataset: Důlní díla v České republice
* gestor: [https://www.geology.cz/ Česká geologická služba]
* licence: CC BY 4.0 [https://data.gov.cz/zdroj/datové-sady/00025798/2498e3343ea928eb374d534397f4d92a] – nutný souhlas pro OSM
* datové primitivy: body
* odkaz: https://od.geology.cz/dulni_dila.zip
* navržený tag {{tag|man_made|adit}}, {{tag|man_made|mineshaft}} (s prefixem abandoned: u zaniklých), {{tag|ref:cgs:dd|<id_dd>}}
* poznámka: v OSM ~900 štol a šachet, v registru ~15 700 jam, štol a šachtic (celkem 30 891 záznamů vč. vrtů); mnohá díla jsou zlikvidovaná a v terénu neviditelná
```
