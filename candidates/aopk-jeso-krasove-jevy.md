# AOPK JESO – Jednotná evidence speleologických objektů (caves, sinkholes, ponors, karst springs)

| Field | Value |
|---|---|
| publisher | Agentura ochrany přírody a krajiny ČR (AOPK ČR); data steward Luboš Stárka, lubos.starka@aopk.gov.cz, +420 951 421 231. Data mostly from members of Česká speleologická společnost, in cooperation with Správa jeskyní ČR |
| url | https://data.nature.cz/ds/115/download (zip, `jeso_verej.shp`); dataset page https://data.nature.cz/ds/115 ; metadata https://metadata.nature.cz/record/basic/6853b5c9-fbb0-4dfb-a0e6-5b7d0a020812 ; per-object page https://jeso.nature.cz/?jeso=&lt;KARSOLOGID&gt; |
| format | ESRI Shapefile, points, EPSG:5514 (S-JTSK) |
| coords | yes (with a per-point accuracy/method field) |
| records | 3,393 (all VEREJNE=1): 02 Závrt 2,332; 01 Jeskyně 542; 03 Hydrologický jev 452; 04 Další karsologický objekt 67. Fields: KARSOLOGID, KOD_JESO (unique), NAZEV_JEVU, SYNONYMUM_, URL, NADMORSKA_ (altitude), DELKA_J / HLOUBKA_J / VYSKA_J / DENIVALACE (cave length, depth, height, vertical range in m; length filled for 511 of 542 caves), ZZ_POLOHA (location method), STAV_J (condition), TYP_J |
| osm_tags | natural=cave_entrance; natural=sinkhole + sinkhole=doline / sinkhole=ponor; natural=spring + karst=yes; key cave:ref=&lt;KOD_JESO&gt; |
| osm_count_cz | natural=cave_entrance 870; natural=sinkhole 671 (sinkhole=doline 25, ponor 7, pit 2); natural=spring 4,844; cave:ref 19, of which 4 already hold JESO codes (K2301216-J-11120 ×2, K2301216-J-11160, K2301216-H-00006) (taginfo 2026-09-27) |
| license | CC BY 4.0, attribution "(c) AOPK ČR" (stated on the dataset page) |
| license_url | https://data.nature.cz/ds/115 ; https://creativecommons.org/licenses/by/4.0/ |
| license_status | needs_waiver |
| update_freq | irregular (last update 2025-06-19 per dataset page) |
| impact | 2 |
| sync_fit | Sync for caves/springs (points, cave:ref proposed, 1:1); MapRoulette for sinkholes (subtype 1:N) |
| verified | yes |

## Try it
- **Map preview:** [samples/aopk-jeso-krasove-jevy.geojson](../samples/aopk-jeso-krasove-jevy.geojson): all 831 JESO objects in the northern Moravian Karst (bbox 16.68,49.33,16.78,49.42) with type, condition, location method, cave length/depth, the proposed OSM tags and `osm_karst_feature_within_100m`.
- **QGIS:** download https://data.nature.cz/ds/115/download (a 227 kB zip; the server does not answer range requests, so `/vsizip/vsicurl/` is not reliable), then *Layer → Add Layer → Add Vector Layer…*, pick the zip; QGIS opens `jeso_verej.shp` inside it. CRS is read from the `.prj` (EPSG:5514).
- **Web:** each object has a public page, https://jeso.nature.cz/?jeso=2517 (Koudelkova propast I).

## Notes
- **Not known:** no JESO, AOPK karst or cave source on `Cs:Česko/freemap` (incl. Potencionální zdroje) or
  in Sync `config.toml`. `Cs:Zdroje_v_jednani` has a struck-out (finished) row from 2019: *caves.cz –
  "získání podkladových map jeskyní ČR, kontakt Olga Suldovská" – "získán souhlas"*. That consent covers
  cave maps from caves.cz, not the AOPK register, so an AOPK waiver is still needed; the same contact may
  help because the JESO data largely comes from Česká speleologická společnost.
- **National gap (Postpass, 2026-09-27, earlier round agent; any OSM cave/sinkhole/spring within 100 m):**
  caves 214 of 542 matched, sinkholes 264 of 2,332, hydrological 96 of 452.
  So about 330 cave entrances and over 2,000 sinkholes are missing.
- **Sample area (OSM API map tiles, 2026-09-27, bbox 16.68,49.33,16.78,49.42 – northern Moravian Karst):**
  OSM has 77 cave_entrance, 71 sinkhole and 5 spring objects there; JESO has 831 objects. 288 JESO objects
  have an OSM karst feature within 100 m (caves 80/134, sinkholes 158/586, hydrological 37/81, other 13/30).
  In dense sinkhole fields "within 100 m" often hits a neighbouring sinkhole, so the real gap is larger.
  (Postpass returned 503 all session, so the OSM API was used for this area.)
- **ZABAGED overlap (layer 11 "Vstup do jeskyně" on `ags.cuzk.gov.cz/.../ZABAGED_POLOHOPIS/MapServer`,
  2026-09-27):** 486 cave entrances (346 named), not part of the ZABAGED POI import. 228 of the 542 JESO caves
  have a ZABAGED entrance within 100 m. ZABAGED has no sinkhole, ponor or karst spring layer; its "Zdroj
  podzemních vod" layer holds springs and wells in general. JESO adds sinkholes, ponors, a stable cave-register
  code, cave length/depth and a location-accuracy flag.
- **Tagging** (wiki pages read: Tag:natural=cave_entrance, Cs:Tag:natural=cave_entrance, Cave,
  Tag:natural=sinkhole, Key:sinkhole, Tag:natural=spring):
  - 01 Jeskyně → natural=cave_entrance + name. The Cave page documents `cave:ref` for "an official
    identifier … in a cave cadastre" and lists `cave:length`/`cave:depth` as ideas; CZ mappers already put
    JESO codes into `cave:ref`, so `cave:ref=<KOD_JESO>` is the natural key.
  - 02 Závrt → natural=sinkhole + sinkhole=doline (the Czech term *závrt* is a doline). 1,987 sinkholes
    carry only a survey code as name ("Závrt RP/12", "Závrt č. 60"); these must not go into `name`
    (the sample leaves them out). 1,406 of all 3,393 objects have a real name.
  - 03 Hydrologický jev → by name: "Ponor…/Propadání…" (141) → natural=sinkhole + sinkhole=ponor;
    "Vývěr…/Vyvěračka…/Pramen…/Studánka…" (132) → natural=spring + karst=yes (Tag:natural=spring, section
    Karstic springs); the remaining 179 need manual review.
  - 04 Další karsologický objekt (67: škrapy, hřebenáče, paleokras) → manual review.
  - Skip the 40 objects with STAV_J "06 Antropické zničení objektu" or "07 Přirozený zánik objektu".
- **Location quality:** 2,029 GPS without correction (5–10 m), 805 from DMR 5G (lidar terrain model),
  172 drawn on ZM 1:10 000 (10–20 m), 122 unknown method, 17 verbal description only, 9 drawn on 1:50 000
  (tens to hundreds of m). Import only the precise classes; leave the rest for manual checks.
- **Access:** many cave entrances are gated or closed to the public; add `access=no` / `barrier=gate`
  where known (both listed on Tag:natural=cave_entrance).
- **Show caves (AOPK "Veřejnosti zpřístupněné jeskyně", https://data.nature.cz/ds/33/download):** only
  14 points (KOD_JESO + NAZEV: Punkevní, Koněpruské, Javoříčské, Mladečské, Chýnovská, Bozkovské
  dolomitové…). Every one is a well-known tourist site, so it adds nothing beyond the JESO code, which it
  shares with JESO. Not worth a separate import; use it to set `tourism=attraction`/`fee=yes` on those
  14 entrances.

## Wiki entry
```
===AOPK – JESO (jeskyně, závrty, ponory, vývěry)===
* dataset: JESO – Jednotná evidence speleologických objektů pro veřejnost
* gestor: [https://data.nature.cz/ds/115 AOPK ČR]
* licence: CC BY 4.0 [https://creativecommons.org/licenses/by/4.0/]
* datové primitivy: body
* odkaz: https://data.nature.cz/ds/115/download
* navržený tag {{tag|natural|cave_entrance}}, {{tag|natural|sinkhole}} + {{tag|sinkhole|doline}} / {{tag|sinkhole|ponor}}, {{tag|natural|spring}} + {{tag|karst|yes}}, {{tag|cave:ref|<KOD_JESO>}}
* poznámka: 3 393 krasových jevů; v OSM je do 100 m jen 214 z 542 jeskyní a 264 z 2 332 závrtů; ZABAGED závrty nemá; nutný souhlas AOPK (CC BY)
```
