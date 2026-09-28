# ZABAGED layer audit: which layers to bring into OSM next

This page extends the ZABAGED table on the **Synchronizace** page of the vfosnar/osm Codeberg wiki
(https://codeberg.org/vfosnar/osm/wiki/Synchronizace). It uses the same layer names, shows that page's status
(🟢 compared and missing objects added, 🟡 in progress, ⭐ suited for Sync) and adds three things: a feature count
for every layer, a measured OSM gap, and the route into OSM.

Sources, all read 2026-09-28:

- ČÚZK ArcGIS service `ZABAGED_POLOHOPIS` (https://ags.cuzk.gov.cz/arcgis/rest/services/ZABAGED_POLOHOPIS/MapServer),
  149 layers, counts from `query?where=1=1&returnCountOnly=true`. Licence CC BY 4.0 + ČÚZK consent for OSM
  (recorded on `Cs:Česko/freemap`), so `ok` for every layer.
- ZABAGED object catalogue (https://geoportal.cuzk.gov.cz/Dokumenty/ZABAGED_katalog/CS/index.html; plain curl is redirected
  to Podminky.pdf unless a `Referer: https://geoportal.cuzk.gov.cz/` header is sent).
- iD fork tag file `data/zabaged_osm_tags.json` (Codeberg `osmcz/iD`, branch `cz-develop`, commit of 2026-06-27). The
  "iD fork mapping" column quotes it: `tagged` (fixed tags), `subtype rules on <field>`, `(todo)`, or `empty`
  (table present with no tags). The file has 173 tables: 78 tagged, 3 with subtype rules, 92 empty, 3 todo notes.
  Note for the fork maintainers: `ZABAGED.md` still says "159 tables tagged, 28 with subtype rules, 75 flagged todo" and
  names the ref key `ref:cuzk:zbg`; the code (`modules/ui/zabaged.js`) writes `ref:zabaged`, which matches Sync.
- `Cs:POI_ZABAGED_Import` (13 POI layers, 8 marked ✅) and Sync's `[group.zabaged.dataset.*]` (11 datasets).
- OSM national counts: taginfo Geofabrik Czech Republic (data until 2026-09-27). Gap: local match against the
  2026-09-27 Czechia extract (Postpass returned 503). A ZABAGED feature counts as "missing" when no OSM object with the
  compared tag lies within the radius given (node, or any vertex / centroid of a way). The comparison uses the compared
  tag only, so an object mapped under another tag counts as missing; the notes say where that inflates the gap.

## Routes

- **Sync**: point layer, one OSM tag set per ZABAGED type (or per subtype, chosen by an attribute), stable `fid_zbg`
  written as `ref:zabaged`.
- **iD fork**: line and area layers (and points that must sit on an OSM way). Assumes the planned Sync-like geometry
  harness in the fork (dataset with stable IDs, matched against OSM, worked as a queue). Needs a clear mapping in
  `zabaged_osm_tags.json`; an empty table needs one first. A MapRoulette challenge on top helps when the gap is large.
- **MapRoulette**: 1:N types with no attribute to decide (the mapper looks at imagery and picks the tag), same as the
  earlier ZABAGED challenges (pitches, dog-training grounds, cemeteries, communication towers).
- **skip**: OSM already has it, another source is better, or it is topography / land cover / network data.

## Ranked shortlist

Missing = ZABAGED objects with no OSM object of the compared tag within the radius. "CZ" = whole country;
otherwise a sample bbox: **A** Žďár nad Sázavou – Nové Město na Moravě (15.80,49.50,16.10,49.65),
**B** Turnov / Český ráj (15.05,50.50,15.30,50.62), **C** Krkonoše (15.50,50.68,15.80,50.78).

| # | id | Layer (Synchronizace name) | geometry | ZABAGED | iD fork mapping | tag mapping | OSM tag compared | OSM CZ (taginfo) | missing in OSM | Synchronizace | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 14 | Významný nebo osamělý strom, lesík (VyznamnyNeboOsamelyStromLesik) | point | 57,340 (33,592 osamělý strom, 23,748 osamělý lesík) | empty | 1:1 per subtype via `typveg_p` (strom → natural=tree; lesík is a point for a group of trees, no area) | natural=tree, 30 m | 136,325 | **31,918 of 33,592 trees (95 %) CZ** | – | **Sync** for osamělý strom; lesík skip. [candidate](../candidates/zabaged-osamele-stromy.md) |
| 2 | 114 | Areál účelové zástavby – vodojem zemní | area | 6,950 | empty (whole `arealucelovezastavby` table) | 1:1 (man_made=reservoir_covered) | man_made=reservoir_covered / water_tower / storage_tank / water_works, 100 m | 613 (reservoir_covered) | **5,776 of 6,950 (83 %) CZ** | – | **Sync** (centroid point) or iD fork (area). [candidate](../candidates/zabaged-vodojemy-zemni.md) |
| 3 | 31 | Tovární komín (TovarniKomin) | point | 6,117 | tagged: man_made=chimney | 1:1; `vyska_obj` → height (1,997 have it) | man_made=chimney, 50 m | 2,733 | **3,650 of 6,117 (60 %) CZ** | – | **Sync**. [candidate](../candidates/zabaged-tovarni-kominy.md) |
| 4 | 10 | Osamělý balvan, skála, skalní suk (OsamelyBalvanSkalaSkalniSuk) | point | 12,538 | empty | 1:N, no attribute (balvan → natural=stone, skála / skalní suk → natural=rock) | natural=stone / rock, 50 m | 1,718 + 2,659 | **11,216 of 12,538 (89 %) CZ**; 103 of 105 in B | – | **MapRoulette** (mapper picks stone/rock). [candidate](../candidates/zabaged-osamele-balvany-skaly.md) |
| 5 | 24 | Kříž, sloup kulturního významu (KrizSloupKulturnihoVyznamu) | point | 70,725 | empty | 1:N, no attribute (wayside_cross / wayside_shrine / column / bell tower) | historic=wayside_cross / wayside_shrine / memorial / monument, man_made=cross, 50 m | 34,885 + 9,375 + 1,073 | **24,829 of 70,725 (35 %) CZ** | – | **MapRoulette**, after the Drobné památky import (CC0, `Cs:Drobné_památky_Import`) has run: that source has categories, ZABAGED then finds the remainder |
| 6 | 108 | Nadzemní zásobní nádrž (NadzemniZasobniNadrz) | area | 16,433 | tagged: man_made=storage_tank | 1:1 | man_made=storage_tank / silo / reservoir_covered / wastewater_plant / water_tower, 50 m | 2,239 | **13,462 of 16,433 (82 %) CZ** | – | **iD fork**; large gap, a MapRoulette pointer challenge is worth it |
| 7 | 103 | Rozvalina, zřícenina (RozvalinaZricenina) | area | 12,192 (rozvalina 11,529; zřícenina hradu 399, ostatní 220, zámku 44) | tagged: historic=ruins | 1:N by `podtypob_p` | building=ruins, ruins=yes, historic=ruins / castle, 50 m | 3,330 + 2,004 + 1,938 | **10,636 of 11,529 rozvaliny (92 %)**; castle ruins 350 of 399 already mapped | – | **iD fork**, mapping needs subtype rules first (historic=ruins suits the 663 zříceniny, not 11,529 ruined buildings) |
| 8 | 130 | Skalní útvary (SkalniUtvary) | area | 39,450 | tagged: natural=bare_rock | 1:1 | natural=bare_rock / rock / stone, 100 m of centroid | 5,769 (bare_rock) | 1,693 of 1,740 in B (97 %) | – | **iD fork**; gap overstated (natural=cliff lines not compared), check on a second area |
| 9 | 16 | Lesní průsek (LesniPrusek) | line | 75,250 | tagged: man_made=cutline | 1:1 | man_made=cutline, 20 m | 1,865 | 229 of 230 in A, 299 of 299 in B | – | **iD fork**; many průseky carry a highway=track in OSM (not compared), so conflation must look for tracks |
| 10 | 65 / 78 | Propustek bod / linie (Propustek, Propustek_b) | point / line | 169,126 / 31,632 | empty / empty | 1:1 (tunnel=culvert on the waterway segment) | tunnel=culvert, 30 m / 20 m | 53,952 | 1,008 of 1,215 points, 124 of 155 lines in A (82 %) | – | **iD fork** together with the waterway conflation (a culvert splits the OSM stream); mapping needed first |
| 11 | 28 | Silo | point | 2,755 | tagged: man_made=silo | 1:1 | man_made=silo / storage_tank, building=silo, 50 m | 708 + 132 | **2,436 of 2,755 (88 %) CZ** | – | **Sync** |
| 12 | 128 | Přečerpávací stanice produktovodu (PrecerpavaciStaniceProduktovodu) | area | 2,507 | tagged: man_made=pumping_station | 1:1, but the fork and Synchronizace disagree (Synchronizace: pipeline=substation) | pipeline=substation, 60 m | 404 | **2,351 of 2,507 (94 %) CZ** | – | **Sync** (centroid) once the tag is settled |
| 13 | 25 | Mohyla, pomník, náhrobek (MohylaPomnikNahrobek) | point | 21,082 | empty | 1:N, no attribute (memorial / tomb / artwork) | historic=memorial / tomb / monument / wayside_cross / wayside_shrine, 50 m | 30,273 (memorial) | **7,537 of 21,082 (36 %) CZ** | – | **MapRoulette**, after Drobné památky |
| 14 | 61 | Stožár lanové dráhy (StozarLanoveDrahy) | point on line | 5,531 | tagged: aerialway=pylon | 1:1 | aerialway=pylon, 20 m | 2,053 | **4,100 of 5,531 (74 %) CZ**; 453 of 640 in C | – | **iD fork** (pylons must be vertices of the aerialway way; `lanovadrahalyzarskyvlek` mapping is empty) |
| 15 | 53 | Definiční bod náměstí (DefinicniBodNamesti) | point | 2,645 (all named, with `ulice_id`) | empty | 1:1 (place=square) | place=square, 100 m | 776 | 2,082 of 2,645 (79 %) CZ | – | **Sync**, but the gap is overstated: many squares are named highway=pedestrian areas in OSM (not compared) |
| 16 | 26 | Věž, věžovitá nástavba, subtypes rozhledna / vyhlídková stavba / věž samostatně stojící | point | 2,152 of 17,281 | tagged: man_made=tower | 1:N by `podtypob_p`; věž samostatně stojící is ambiguous | man_made=tower / mast, 60 m | 5,943 | 1,256 of 2,152 CZ (1,155 of them věž samostatně stojící); rozhledny 322 of 390 mapped | 🟡 vysílač (mpr.lt/c/54588) | **MapRoulette** for věž samostatně stojící; church/chapel towers skip (part of the church building) |
| 17 | 114 | Areál účelové zástavby – čistírna odpadních vod, úpravna vody | area | 3,819 + 493 | empty | 1:1 per subtype (man_made=wastewater_plant, man_made=water_works) | same tags, 150 m | 1,703 + 1,317 | 15 of 24 ČOV, 9 of 9 úpravny in A | – | **iD fork** (areas) once `arealucelovezastavby` has subtype rules |
| 18 | 107 | Pozemní nádrž (PozemniNadrz) | area | 20,361 (čištění odpadních vod 9,440, ostatní 7,765, bazén 2,007, sádka 1,149) | empty | 1:N by `podtypob_p` | man_made=wastewater_plant / water_works / storage_tank / reservoir_covered, 100 m | – | 120 of 145 in A | Synchronizace proposes natural=water + water=basin | **iD fork**, subtype rules needed |
| 19 | 110 | Tribuna | area | 1,048 | tagged: building=grandstand | 1:1 | building=grandstand, leisure=bleachers, 60 m | 151 + 291 | 906 of 1,048 (86 %) CZ | – | **iD fork**, low value |
| 20 | 12 / 13 | Skupina balvanů bod / linie | point / line | 68,348 / 9,611 | tagged: natural=rock | 1:N (natural=rock is "a notable rock"; a boulder field is closer to natural=scree or stones) | natural=stone / rock / scree / bare_rock, 50 m | – | 237 of 238 points in B | – | **iD fork**, revisit the mapping first |
| 21 | 66 / 67 | Lávka bod / linie | point / line | 7,847 / 7,345 | tagged: highway=footway + bridge=yes | 1:1 | footway/path/cycleway/steps with bridge, 30 m | – | 38 of 60 points, 21 of 54 lines in A | – | **iD fork**, low: bridges must be split into existing ways |

### Tables in the iD fork file that are empty or todo but have a large OSM gap

Worth finishing first, in this order: `vyznamnyneboosamelystromlesik` (31,918 trees missing; rule `typveg_p`),
`arealucelovezastavby` (vodojem zemní 5,776 missing, plus ČOV and úpravna vody; needs rules on `typzast_p`),
`osamelybalvanskalaskalnisuk` (11,216), `krizsloupkulturnihovyznamu` (24,829) and `mohylapomniknahrobek` (7,537)
(both 1:N, better as MapRoulette), `propustek` / `propustek_b` (82 % missing in A), `pozemninadrz` (rules on
`podtypob_p`), `definicnibodnamesti`, `lanovadrahalyzarskyvlek` (needed before its pylons).

Mappings worth revisiting: `rozvalinazricenina` (historic=ruins for 11,529 ruined buildings; the
Tag:building=ruins page itself discourages building=ruins, so ruins=yes on the building is the likelier target),
`vezvezovitanastavba` (man_made=tower for every subtype, including 6,766 church and chapel towers that OSM maps as
part of the church), `precerpavacistaniceproduktovodu` (man_made=pumping_station vs pipeline=substation on Synchronizace),
`skupinabalvanu` (natural=rock).

## Already covered elsewhere

- POI import / Sync (⭐ on Synchronizace): layers 35, 146, 149, 44, 36, 50, 43, 46, 45 (✅ on `Cs:POI_ZABAGED_Import`),
  47, 48, 49, 51 (listed, not ✅; Sync has `social_facility` and `healthcare`).
- Done or in progress on Synchronizace: Bunkr 🟢, Hřbitov 🟡, vysílač 🟡, Areál účelové zástavby subtypes hřiště 🟢 and
  kynologické cvičiště 🟢.
- Written up in this repo: [zabaged-prameny-studny](../candidates/zabaged-prameny-studny.md) (19),
  [zabaged-zabrany](../candidates/zabaged-zabrany.md) (54), [zabaged-zdi](../candidates/zabaged-zdi.md) (39),
  [zabaged-liniova-vegetace](../candidates/zabaged-liniova-vegetace.md) (15),
  [zabaged-elektrarny-plochy](../candidates/zabaged-elektrarny-plochy.md) (126 and 86). Related non-ZABAGED write-ups
  that cover the same objects better: `cgs-dulni-dila` (34), `mze-isvs-voda-hraze-jezy` (22),
  `known-aopk-pamatne-stromy` (named trees in 14), `sz-prejezdy` (62), `aopk-jeso-krasove-jevy` (11).

### Areál účelové zástavby subtypes (layer 114, 78,622 areas)

škola 9,714; chov hospodářských zvířat 7,241; hřiště 7,035 (🟢); vodojem zemní 6,950 (rank 2); sklad, hangár 4,622;
zemědělský areál ostatní 4,521; čistírna odpadních vod 3,819 (rank 17); strojírenský průmysl 2,886; skupinové garáže
2,877 (OSM landuse=garages 2,858); chatová kolonie 2,807; ostatní průmysl 2,655; zahrádkářská osada 2,610 (OSM
landuse=allotments 7,960); technické služby 2,521; dřevozpracující průmysl 2,389; čerpací stanice PHM 1,982; camping 712
(OSM tourism=camp_site 1,160); koupaliště 687; střelnice 580 (OSM sport=shooting 702); kynologické cvičiště 574 (🟢);
úpravna vody 493 (rank 17); vysílač 334; golfový areál 239 (OSM leisure=golf_course 161); smaller ones below 200.
Camping, střelnice, zahrádky and garáže are at or above OSM counts already, so they are QA material, not gap fillers.

## Full inventory (all 149 layers)

| id | layer | iD fork table | geometry | count | iD fork mapping | Synchronizace | verdict |
|---|---|---|---|---|---|---|---|
| 0 | Hraniční přechod, přeshraniční propojení | `hranicniprechodpreshranicnipropojeni` | point | 773 | empty |  | skip: border crossings; 584 are cross-border links, OSM maps them as the path/road itself |
| 1 | Hranice správní jednotky a KÚ | `hranicespravnijednotkyaku` | line | 39,247 | empty |  | skip: admin boundaries come from RÚIAN |
| 2 | Definiční bod správního celku | `definicnibodspravnihocelku` | point | 13,141 | empty |  | skip: admin centroids |
| 3 | Definiční bod části obce | `definicnibodcastiobce` | point | 11,155 | empty |  | skip: RÚIAN part-of-municipality points |
| 4 | Velkoplošné zvláště chráněné území | `velkoplosnezvlastechraneneuzemi` | area | 31 | empty |  | skip: large protected areas (AOPK) |
| 5 | Maloplošné zvlástě chráněné území | `maloplosnezvlastechraneneuzemi` | area | 2,686 | empty |  | skip: small protected areas (AOPK) |
| 6 | Bod polohového bodového pole | `bodpolohovehobodovehopole` | point | 98,600 | tagged: man_made=survey_point |  | skip: geodetic control points; low map value (fork tags man_made=survey_point; OSM 507) |
| 7 | Bod základního výškového bodového pole | `bodzakladnihovyskovehobodovehopole` | point | 82,141 | tagged: man_made=survey_point + survey_point=leveling |  | skip: levelling points; low map value |
| 8 | Bod základního tíhového bodového pole | `bodzakladnihotihovehobodovehopole` | point | 462 | empty |  | skip: 462 gravity points |
| 9 | Kótovaný bod | `kotovanybod` | point | 146,604 | empty |  | skip: spot heights (terrain) |
| 10 | Osamělý balvan, skála, skalní suk | `osamelybalvanskalaskalnisuk` | point | 12,538 | empty |  | written up: [zabaged-osamele-balvany-skaly](../candidates/zabaged-osamele-balvany-skaly.md) (new) |
| 11 | Vstup do jeskyně | `vstupdojeskyne` | point | 486 | tagged: natural=cave_entrance |  | skip: 486 vs OSM natural=cave_entrance 871; AOPK JESO is the better source (aopk-jeso-krasove-jevy) |
| 12 | Skupina balvanů (bod) | `skupinabalvanu_b` | point | 68,348 | tagged: natural=rock |  | ranked above |
| 13 | Skupina balvanů (linie) | `skupinabalvanu` | line | 9,611 | tagged: natural=rock |  | ranked above |
| 14 | Významný nebo osamělý strom, lesík | `vyznamnyneboosamelystromlesik` | point | 57,340 | empty |  | written up: [zabaged-osamele-stromy](../candidates/zabaged-osamele-stromy.md) (new) |
| 15 | Liniová vegetace | `liniovavegetace` | line | 351,398 | empty |  | written up: [zabaged-liniova-vegetace](../candidates/zabaged-liniova-vegetace.md) |
| 16 | Lesní průsek | `lesniprusek` | line | 75,250 | tagged: man_made=cutline |  | ranked above |
| 17 | Rašeliniště (bod) | `raseliniste_b` | point | 44 | tagged: natural=wetland + wetland=bog |  | skip: 44 bog points (landcover) |
| 18 | Rašeliniště (plocha) | `raseliniste` | area | 153 | tagged: natural=wetland + wetland=bog |  | skip: 153 bog areas (landcover) |
| 19 | Zdroj podzemních vod | `zdrojpodzemnichvod` | point | 35,224 | tagged: natural=spring |  | written up: [zabaged-prameny-studny](../candidates/zabaged-prameny-studny.md) |
| 20 | Vodopád (bod) | `vodopad_b` | point | 386 | tagged: waterway=waterfall |  | skip: 386 vs OSM waterway=waterfall 444 |
| 21 | Vodopád (linie) | `vodopad` | line | 57 | tagged: waterway=waterfall |  | skip: 57 lines |
| 22 | Přehradní hráz, jez | `prehradnihrazjez` | line | 5,879 | subtype rules on `typvod_p` |  | MapRoulette/QA only: weirs 5,696 vs OSM waterway=weir 6,872; MZe ISVS-VODA (mze-isvs-voda-hraze-jezy) has more attributes |
| 23 | Budova jednotlivá nebo blok budov (bod) | `budovajednotlivaneboblokbudov_b` | point | 82 | tagged: building=yes |  | skip: 82 building points (RÚIAN buildings) |
| 24 | Kříž, sloup kulturního významu | `krizsloupkulturnihovyznamu` | point | 70,725 | empty |  | ranked above |
| 25 | Mohyla, pomník, náhrobek | `mohylapomniknahrobek` | point | 21,082 | empty |  | ranked above |
| 26 | Věž, věžovitá nástavba | `vezvezovitanastavba` | point | 17,281 | tagged: man_made=tower | 🟡 subtype vysílač (mpr.lt/c/54588) | ranked above |
| 27 | Vodojem věžový | `vodojemvezovy` | point | 766 | tagged: man_made=water_tower |  | QA only: 766 vs OSM man_made=water_tower 670 |
| 28 | Silo | `silo` | point | 2,755 | tagged: man_made=silo |  | ranked above |
| 30 | Těžní věž | `teznivez` | point | 508 | empty |  | MapRoulette (small): 508 headframes, 439 in operation; OSM headframe=yes 21, man_made=mineshaft 284 |
| 31 | Tovární komín | `tovarnikomin` | point | 6,117 | tagged: man_made=chimney |  | written up: [zabaged-tovarni-kominy](../candidates/zabaged-tovarni-kominy.md) (new) |
| 32 | Větrný mlýn | `vetrnymlyn` | point | 71 | empty |  | skip: 71 vs OSM man_made=windmill 69 |
| 33 | Větrný motor | `vetrnymotor` | point | 298 | tagged: power=generator + generator:source=wind + generator:type=horizontal_axis |  | QA only: 298 wind turbines; OSM generator:source=wind 258; ERÚ id present |
| 34 | Ústí šachty, štoly | `ustisachtystoly` | point | 791 | empty |  | skip: 791 shafts/adits; ČGS Důlní díla (cgs-dulni-dila) is the richer source |
| 35 | Čerpací stanice pohonných hmot - definiční bod | `cerpacistanicepohonnychhmotdefinicnibod` | point | 3,826 | tagged: amenity=fuel | ⭐ | known: POI import / Sync (fuel ✅) |
| 36 | Meteorologická stanice - definiční bod | `meteorologickastanicedefinicnibod` | point | 1,074 | tagged: man_made=monitoring_station + monitoring:weather=yes | ⭐ | known: POI import / Sync (weather_station ✅) |
| 37 | Bunkr | `bunkr` | point | 6,100 | tagged: military=bunker | 🟢 02.2026 (changeset 178882521) | known (🟢 done) |
| 38 | Hradba, val, bašta, opevnění | `hradbavalbastaopevneni` | line | 1,735 | empty |  | QA only: 1,735 lines vs OSM barrier=city_wall 1,787 |
| 39 | Zeď | `zed` | line | 83,833 | tagged: barrier=wall |  | written up: [zabaged-zdi](../candidates/zabaged-zdi.md) |
| 40 | Dopravníkový pás | `dopravnikovypas` | line | 584 | tagged: man_made=goods_conveyor |  | iD fork (small): 584 conveyors vs OSM 343 |
| 41 | Lyžařský můstek | `lyzarskymustek` | line | 40 | empty |  | skip: 40 ski jumps |
| 42 | Doplňková linie | `doplnkovalinie` | line | 579,272 | empty |  | skip: auxiliary cartographic lines |
| 43 | Policejní služebna - definiční bod | `policejnisluzebnadefinicnibod` | point | 718 | tagged: amenity=police | ⭐ | known: POI import / Sync (police ✅) |
| 44 | Hasičská stanice, zbrojnice - definiční bod | `hasicskastanicezbrojnicedefinicnibod` | point | 6,176 | tagged: amenity=fire_station | ⭐ | known: POI import / Sync (fire_station ✅) |
| 45 | Úřad veřejné správy - definiční bod | `uradverejnespravydefinicnibod` | point | 8,346 | empty | ⭐ | known: POI import / Sync (public_office ✅) |
| 46 | Pošta - definiční bod | `postadefinicnibod` | point | 2,969 | tagged: amenity=post_office | ⭐ | known: POI import / Sync (post_office ✅) |
| 47 | Škola - definiční bod | `skoladefinicnibod` | point | 15,919 | tagged: amenity=school | ⭐ | known: POI import / Sync (school (not ✅)) |
| 48 | Školské zařízení - definiční bod | `skolskezarizenidefinicnibod` | point | 485 | empty | ⭐ | known: POI import / Sync (school facility (not ✅)) |
| 49 | Sociální zařízení - definiční bod | `socialnizarizenidefinicnibod` | point | 6,382 | tagged: amenity=social_facility | ⭐ | known: POI import / Sync (social_facility (not ✅)) |
| 50 | Nemocnice - definiční bod | `nemocnicedefinicnibod` | point | 211 | tagged: amenity=hospital | ⭐ | known: POI import / Sync (hospital ✅) |
| 51 | Zdravotnické zařízení - definiční bod | `zdravotnickezarizenidefinicnibod` | point | 3,146 | empty | ⭐ | known: POI import / Sync (healthcare (not ✅)) |
| 52 | Definiční bod adresního místa | `definicnibodadresnihomista` | point | 3,014,190 | empty |  | skip: RÚIAN address points (imported) |
| 53 | Definiční bod náměstí | `definicnibodnamesti` | point | 2,645 | empty |  | ranked above |
| 54 | Zábrana | `zabrana` | point | 36,809 | empty |  | written up: [zabaged-zabrany](../candidates/zabaged-zabrany.md) |
| 55 | Křižovatka mimoúrovňová | `krizovatkamimourovnova` | point | 5,773 | empty |  | skip: road network nodes |
| 56 | Křižovatka úrovňová | `krizovatkaurovnova` | point | 18,841 | empty |  | skip: road network nodes |
| 57 | Uzlový bod silniční sítě (ostatní) | `uzlovybodsilnicnisiteostatni` | point | 5,157 | empty |  | skip: road network nodes |
| 58 | Železniční stanice, zastávka | `zeleznicnistanicezastavka` | point | 2,797 | tagged: railway=station |  | skip: 2,797 stations vs OSM railway=station+halt 2,860 |
| 59 | Stanice metra | `stanicemetra` | point | 58 | tagged: railway=station + station=subway |  | skip: metro |
| 60 | Přístaviště | `pristaviste` | point | 967 | empty |  | MapRoulette (small): 967 landings, 181 named; target tag 1:N (slipway / pier / ferry_terminal) |
| 61 | Stožár lanové dráhy | `stozarlanovedrahy` | point | 5,531 | tagged: aerialway=pylon |  | ranked above |
| 62 | Železniční přejezd (bod) | `zeleznicniprejezd_b` | point | 7,836 | tagged: railway=level_crossing |  | skip: 7,836 vs OSM railway=level_crossing 16,683 (+ sz-prejezdy) |
| 63 | Železniční přejezd (linie) | `zeleznicniprejezd` | line | 1,251 | empty |  | skip: level crossing lines |
| 64 | Podjezd (bod) | `podjezd_b` | point | 984 | empty |  | skip: underpasses (road network) |
| 65 | Propustek (bod) | `propustek_b` | point | 169,126 | empty |  | ranked above |
| 66 | Lávka (bod) | `lavka_b` | point | 7,847 | tagged: highway=footway + bridge=yes |  | ranked above |
| 67 | Lávka (linie) | `lavka` | line | 7,345 | tagged: highway=footway + bridge=yes |  | ranked above |
| 68 | Brod | `brod` | line | 5,089 | tagged: ford=yes |  | QA only: 5,089 fords vs OSM ford=yes 7,136 |
| 69 | Přívoz | `privoz` | line | 34 | empty |  | skip: 34 ferries vs OSM route=ferry 117 |
| 70 | Metro | `metro` | line | 108 | tagged: railway=subway |  | skip: metro |
| 71 | Tramvajová dráha | `tramvajovadraha` | line | 1,440 | tagged: railway=tram |  | skip: tram |
| 72 | Lanová dráha, lyžařský vlek | `lanovadrahalyzarskyvlek` | line | 1,179 | empty |  | skip: 1,179 aerialways, OSM well covered by ski-resort mapping; fork mapping empty |
| 73 | Most | `most` | line | 50,567 | empty |  | skip: bridges belong to the road/rail ways |
| 74 | Tunel | `tunel` | line | 289 | empty |  | skip: 289 tunnels |
| 75 | Železniční trať | `zeleznicnitrat` | line | 5,248 | tagged: railway=rail |  | skip: railways |
| 76 | Železniční vlečka | `zeleznicnivlecka` | line | 7,141 | tagged: railway=rail + service=spur + usage=industrial |  | skip: sidings |
| 77 | Podjezd (linie) | `podjezd` | line | 4,371 | empty |  | skip: underpasses |
| 78 | Propustek (linie) | `propustek` | line | 31,632 | empty |  | ranked above |
| 79 | Silnice, dálnice | `silnicedalnice` | line | 41,325 | empty |  | skip: roads (ŘSD data) |
| 80 | Silnice neevidovaná | `silniceneevidovana` | line | 17,171 | empty |  | skip: roads |
| 81 | Silnice ve výstavbě | `silnicevevystavbe` | line | 894 | tagged: highway=construction |  | skip: roads under construction |
| 82 | Pěšina | `pesina` | line | 74,103 | tagged: highway=path |  | skip: paths (road-network layer; traced in OSM) |
| 83 | Cesta | `cesta` | line | 1,191,516 | tagged: highway=track |  | skip: tracks |
| 84 | Ulice | `ulice` | line | 1,058,631 | empty |  | skip: streets |
| 85 | Osa letištní dráhy | `osaletistnidrahy` | line | 335 | tagged: aeroway=runway |  | skip: runways |
| 86 | Elektrárna (bod) | `elektrarna_b` | point | 35,923 | tagged: power=plant |  | written up: [zabaged-elektrarny-plochy](../candidates/zabaged-elektrarny-plochy.md) (point layer) |
| 87 | Stožár elektrického vedení | `stozarelektrickehovedeni` | point | 189,221 | tagged: power=tower |  | skip: power towers, sample gap only 11% (86 of 759) |
| 88 | Elektrické vedení | `elektrickevedeni` | line | 138,897 | empty |  | skip: power lines; OSM power mapping is dense (towers matched 89%) |
| 89 | Dálkový produktovod, dálkové potrubí | `dalkovyproduktovoddalkovepotrubi` | line | 3,935 | tagged: man_made=pipeline |  | QA only: 3,935 pipeline lines vs OSM man_made=pipeline 4,422 |
| 90 | Akvadukt, shybka | `akvaduktshybka` | line | 306 | subtype rules on `typvod_p` (todo) |  | skip: 306 aqueducts/siphons, fork mapping todo |
| 91 | Plavební komora | `plavebnikomora` | line | 63 | tagged: lock=yes + waterway=lock_gate (todo) |  | skip: 63 locks |
| 92 | Suchá nádrž | `suchanadrz` | point | 466 | empty |  | MapRoulette (small): 466 dry reservoirs; fork mapping empty |
| 93 | Vodní tok | `vodnitok` | line | 358,804 | subtype rules on `typtoku_p+vydattok_p` |  | skip: watercourses (DIBAVOD import; fork conflates waterways) |
| 94 | Rokle, výmol | `roklevymol` | line | 1,386 | empty |  | MapRoulette (small): 1,386 gullies vs OSM natural=gully 311 |
| 95 | Stupeň, sráz | `stupensraz` | line | 847,727 | tagged: natural=cliff |  | skip: terrain edges (847k) |
| 96 | Pata terénního útvaru | `pataterennihoutvaru` | line | 131,814 | empty |  | skip: terrain foot lines |
| 97 | Hranice geomorfologické jednotky | `hranicegeomorfologickejednotky` | line | 6,764 | empty |  | skip: geomorphological boundaries |
| 98 | Heliport | `heliport` | area | 209 | tagged: aeroway=helipad |  | QA only: 209 heliports vs OSM aeroway=helipad 366 |
| 99 | Budova jednotlivá nebo blok budov (plocha) | `budovajednotlivaneboblokbudov` | area | 3,945,151 | tagged: building=yes |  | skip: buildings (RÚIAN import) |
| 100 | Věžovitá stavba | `vezovitastavba` | area | 3,770 | tagged: man_made=tower |  | skip: tower footprints, overlaps layer 26 |
| 101 | Hrad | `hrad` | area | 117 | tagged: historic=castle + castle_type=defensive |  | skip: 117 castles vs OSM historic=castle 1,377 |
| 102 | Zámek | `zamek` | area | 1,216 | tagged: historic=castle + castle_type=stately |  | skip: 1,216 chateaux, covered by historic=castle |
| 103 | Rozvalina, zřícenina | `rozvalinazricenina` | area | 12,192 | tagged: historic=ruins |  | ranked above |
| 104 | Stavební objekt zakrytý | `stavebniobjektzakryty` | area | 7,684 | empty |  | skip: 7,684 covered structures, no clear OSM tag |
| 105 | Kůlna, skleník, fóliovník, přístřešek | `kulnasklenikfoliovnikpristresek` | area | 531,222 | tagged: building=yes |  | skip: sheds/greenhouses (531k), traced from imagery |
| 107 | Pozemní nádrž | `pozemninadrz` | area | 20,361 | empty |  | ranked above |
| 108 | Nadzemní zásobní nádrž | `nadzemnizasobninadrz` | area | 16,433 | tagged: man_made=storage_tank |  | ranked above |
| 109 | Chladící věž | `chladicivez` | area | 133 | tagged: man_made=cooling_tower |  | skip: 133 vs OSM tower:type=cooling 116 |
| 110 | Tribuna | `tribuna` | area | 1,048 | tagged: building=grandstand |  | ranked above |
| 111 | Železniční točna, přesuvna | `zeleznicnitocnapresuvna` | area | 105 | empty |  | skip: 105 turntables vs OSM 146 |
| 112 | Břehová čára | `brehovacara` | line | 202,154 | tagged: natural=coastline (todo) |  | skip: shorelines |
| 113 | Rozvodnice | `rozvodnice` | line | 30,601 | empty |  | skip: watersheds |
| 114 | Areál účelové zástavby | `arealucelovezastavby` | area | 78,622 | empty | 🟢 subtypes hřiště 03.2026 (mpr.lt/c/54107), kynologické cvičiště 06.2026 (mpr.lt/c/54104) | ranked above |
| 115 | Ostatní plocha v sídlech | `ostatniplochavsidlech` | area | 13,823 | empty |  | skip: other urban land |
| 116 | Hřbitov | `hrbitov` | area | 5,735 | tagged: landuse=cemetery | 🟡 mpr.lt/c/55220 | known (🟡 in progress) |
| 117 | Skládka | `skladka` | area | 2,223 | tagged: landuse=landfill |  | QA only: 421 waste landfills vs OSM landuse=landfill 388; 1,802 material stockpiles |
| 118 | Povrchová těžba, lom | `povrchovatezbalom` | area | 641 | tagged: landuse=quarry |  | skip: 641 quarries vs OSM landuse=quarry 1,246 |
| 119 | Úložné místo | `uloznemisto` | area | 187 | empty |  | skip: 187 heaps/tailings ponds |
| 121 | Areál železniční stanice, zastávky | `arealzeleznicnistanicezastavky` | area | 1,117 | tagged: landuse=railway |  | skip: station areas |
| 122 | Kolejiště | `kolejiste` | area | 1,261 | tagged: landuse=railway |  | skip: track areas |
| 123 | Parkoviště, odpočívka | `parkovisteodpocivka` | area | 16,545 | empty |  | skip: 16,545 parkings vs OSM amenity=parking 92,188 |
| 124 | Obvod letištní dráhy | `obvodletistnidrahy` | area | 220 | empty |  | skip: runway areas |
| 125 | Letiště | `letiste` | area | 95 | tagged: aeroway=aerodrome |  | skip: 95 aerodromes |
| 126 | Elektrárna (plocha) | `elektrarna` | area | 2,141 | tagged: power=plant |  | written up: [zabaged-elektrarny-plochy](../candidates/zabaged-elektrarny-plochy.md) |
| 127 | Rozvodna, transformovna | `rozvodnatransformovna` | area | 533 | tagged: power=substation |  | skip: 533 substations vs OSM power=substation 11,559 |
| 128 | Přečerpávací stanice produktovodu | `precerpavacistaniceproduktovodu` | area | 2,507 | tagged: man_made=pumping_station |  | ranked above |
| 129 | Sesuv půdy, suť | `sesuvpudysut` | area | 478 | empty |  | skip: 478 landslide/scree areas |
| 130 | Skalní útvary | `skalniutvary` | area | 39,450 | tagged: natural=bare_rock |  | ranked above |
| 131 | Bažina, močál | `bazinamocal` | area | 17,775 | tagged: natural=wetland + wetland=marsh |  | skip: wetland landcover |
| 132 | Vodní plocha | `vodniplocha` | area | 91,667 | tagged: natural=water |  | skip: water bodies (DIBAVOD) |
| 133 | Hranice užívání půdy | `hraniceuzivanipudy` | line | 3,580,600 | empty |  | skip: land-use boundary lines |
| 134 | Udržovaná zeleň | `udrzovanazelen` | area | 66,570 | empty |  | skip: landcover |
| 135 | Ovocný sad, zahrada | `ovocnysadzahrada` | area | 391,965 | empty |  | skip: landcover |
| 136 | Vinice | `vinice` | area | 4,255 | tagged: landuse=vineyard |  | skip: vineyards, OSM landuse=vineyard 10,857 |
| 137 | Chmelnice | `chmelnice` | area | 530 | empty |  | skip: hop fields, OSM crop=hop 2,533 |
| 138 | Orná půda a ostatní dále nespecifikované plochy | `ornapudaaostatnidalenespecifikovaneplochy` | area | 113,134 | empty |  | skip: landcover |
| 139 | Trvalý travní porost | `trvalytravniporost` | area | 203,421 | tagged: landuse=meadow |  | skip: landcover |
| 140 | Lesní půda s křovinatým porostem | `lesnipudaskrovinatymporostem` | area | 76,125 | tagged: natural=scrub |  | skip: landcover |
| 141 | Lesní půda s kosodřevinou | `lesnipudaskosodrevinou` | area | 319 | empty |  | skip: landcover |
| 142 | Lesní půda se stromy | `lesnipudasestromy` | area | 143,376 | tagged: natural=wood |  | skip: forest (landcover) |
| 143 | Lesní půda se stromy kategorizovaná (bod) | `lesnipudasestromykategorizovana_c` | point | 4,274,501 | empty |  | skip: forest points |
| 144 | Lesní půda se stromy kategorizovaná (plocha) | `lesnipudasestromykategorizovana` | area | 4,274,502 | empty |  | skip: forest categories |
| 145 | Lodní výtah, zdvihadlo | `lodnivytahzdvihadlo` | line | 1 | tagged: waterway=boat_lift |  | skip: 1 boat lift |
| 146 | Cizí zastupitelský úřad – definiční bod | `cizizastupitelskyuraddefinicnibod` | point | 177 | tagged: office=diplomatic | ⭐ | known: POI import / Sync (embassy ✅) |
| 147 | Evropsky významná lokalita | `evropskyvyznamnalokalita` | area | 1,111 | empty |  | skip: Natura 2000 (AOPK is the primary source) |
| 148 | Ptačí oblast | `ptacioblast` | area | 42 | empty |  | skip: Natura 2000 (AOPK) |
| 149 | Dobíjecí stanice | `dobijecistanice` | point | 2,085 | tagged: amenity=charging_station | ⭐ | known: POI import / Sync (charging_station ✅) |
| 150 | Turistická trasa | `turistickatrasa` | line | 20,096 | empty |  | skip: KČT trails, OSM has them as route relations |
| 151 | Stavební objekt GIA | `stavebniobjektgia` | area | 208,938 | empty |  | skip: GIA building objects (RÚIAN buildings) |
