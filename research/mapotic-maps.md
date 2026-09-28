# Czech maps on Mapotic

Mapotic (mapotic.com) is a Czech map-hosting platform used by NGOs, clubs and hobby
communities. This page lists the Czech public maps found in round 4 (2026-09-27/28) and
which of them are worth asking for OSM use.

## How the maps were found

- **Map metadata (anonymous):** `https://www.mapotic.com/api/v1/maps/<id>/` returns
  name, slug, `lang`, `center`, `owner`, `owner_name`, `domain`, categories and
  `meta.pois_count`. Unpublished or private maps return 401.
- **Search (anonymous):** `https://www.mapotic.com/api/v1/maps/search/?q=<text>` returns up
  to 9 maps per query and has no paging. 114 Czech keywords gave 394 maps.
- **Full scan:** ids 1–34,000 (the highest id seen in search results was 33,650). 6,316 maps
  answered anonymously; 2,069 have `lang=cs`, 38 `lang=sk`. 2,214 have their centre in
  the CZ bbox (12.09,48.55,18.86,51.06), 364 of them with ≥ 100 POIs.
- **POIs (anonymous):** `https://www.mapotic.com/api/v1/maps/<id>/pois.geojson/` returns
  every published POI as a GeoJSON point with `id`, `name`, `slug`, `category`,
  `category_name`, `last_update`. The per-POI detail endpoint
  (`/api/v1/maps/<id>/pois/<poi>/`) needs authentication, so attributes (address, opening
  hours, accessibility details) are not available anonymously.
- The general map listing `/api/v1/maps/` needs authentication (401).
- **Licence:** no map examined states a data licence. Mapotic's terms
  (https://www.mapotic.com/terms/) give other users no rights to content, so every map is
  `unclear` and the owner organisation is who to ask.

## Triage

POI counts are `meta.pois_count` (all countries) unless noted. "CZ" counts are points in
the CZ bbox from the GeoJSON.

| id | Map | Owner | POIs | Verdict |
|---|---|---|---|---|
| 1304 | VozejkMap | Česká asociace paraplegiků – CZEPA, z.s. | 19,499 (CZ 18,132) | **Candidate** `candidates/vozejkmap.md`: 8,178 disabled parking spaces, 342 of 388 missing in Prague centre |
| 10 | WC kompas | Pacienti IBD z.s. | 14,479 (CZ 13,943) | **Candidate** `candidates/wc-kompas.md`: 1,339 public + 415 Euroklíč toilets; the 11,453 "Ostatní" are WC-karta partner places, not public toilets |
| 9288 | Na ovoce | Na ovoce, z.s. | 26,278 (CZ 20,816) | **Candidate** `candidates/na-ovoce.md`: fruit trees with species; 71 % missing in a Prague 6 sample |
| 13630 | Indukční smyčky | Unie neslyšících Brno | 319 (CZ 161) | **Candidate** `candidates/unb-indukcni-smycky.md`: hearing loops; OSM CZ has 1 hearing_loop tag |
| 61 | Mapa komunitních zahrad a kompostérů (Mapko) | Kokoza, o.p.s. | 1,596 | Already written up in round 3 (`candidates/kokoza-komunitni-zahrady.md`) |
| 3964 | Euroklíč | private user | 335 | Static since 2019 (all last_update 2019); use only to cross-check WC kompas Euroklíč layer |
| 9291 | Zapádluj (zapadluj.cz) | Mapotic account | 1,126 | Paddling map: 194 weirs, 153 dangerous weirs, 138 put-in/take-out points, 141 camps. Put-ins (canoe=put_in) are the only OSM-relevant layer; weirs are covered by `mze-isvs-voda-hraze-jezy.md`. Data from 2021 only. Open lead |
| 20 | Bivaky a přístřešky | private user | 444 | 347 hiking shelters, 48 rock overhangs; 2017–2021, hobby-grade. Possible MapRoulette list for amenity=shelter; low priority |
| 5478 | ruční pumpy | private user | 187 | Hand water pumps (mostly Prague, Znojemsko); small, 2020 data. Low priority |
| 18659 | Re-use v ČR | private user | 140 | 64 re-use centres, 56 re-use points, 10 furniture banks (2024). Small but a niche OSM lacks; owner unclear |
| 2887 | Semínkovny | private user | 287 | Seed libraries (261 active), mostly inside public libraries; niche |
| 7149 | Nabíjím levně | private user | 164 | EV chargers (CZ 83); charging stations are better from operators and ATP |
| 1479 | Voda na cestách | Městský úřad (owner "Městský úřad K.") | 50 | Only 22 in CZ; too small |
| 8318 | Mapujeme stromy | MapujemeStromy | 3,244 | Street trees and planting problems, 2021 only |
| 12528 | Zachraň Oběd – charity | private user | 5,949 | Social services list (2025), service providers rather than places; low value for OSM |
| 3439 | Psí místo | private user | 569 | Dog beaches, dog-friendly restaurants, dog meadows; mostly opinions, little OSM value |
| 7130 | Drobné památky | private user | 38,708 | Mirror of drobnepamatky.cz, already in Sync (`[group.drobne_pamatky]`) |
| 452 | Mateřské školky | Mapotic account | 5,349 | Kindergartens; the official school register is the better source |
| 2803 | Malotřídky v ČR | Mapotic account | 1,352 | Small village schools; same as above |
| 1323 | Kde hrát discgolf | proDiscgolf | 201 | Covered by `cadg-discgolf-hriste.md` |
| 3 | Dětská hřiště | private user | 342 | Playgrounds, crowd-sourced, old |
| 14366 | Praha – kam na hřiště? | Pražské zkratky | 331 | Prague playgrounds; `prague-verejna-hriste.md` covers the official source |
| 3415 | Zimní stadiony | private user | 486 | Ice rinks; low priority |
| 861 | Samoobslužné automyčky | private user | 339 | Self-service car washes; low value |
| 13712 | Akce žába | Akce žába | 679 | Amphibian road-crossing sections and barriers; line/zone data for hazard=animal_crossing. Open lead |
| 12366 | Železniční strážní domky, hradla, hlásky | private user | 382 | Railway heritage hobby map; low value |
| 9415 | Možnosti sportování lidí s omezením pohybu | private user | 351 | Organisations (clubs, NGOs), not places |
| 8162 | ZnakoMapa | Znakovárna, z.s. | 478 | Places with sign-language service; no established OSM tag. Open lead if a tag is agreed |
| 15847 | Mapa psychické pomoci | Safezóna | 1,467 | Mental-health services; addresses of practices, not a POI layer for OSM |
| 42 | Tříděný odpad – kovy, biodpad | private user | 520 | Local recycling containers; municipal open data is better |
| 4975 | Udržitelné Vrchlabí | private user | 272 | Local recycling containers in one town |
| 7551 | Sběrná místa ve Frenštátě | Spolek | 348 | Same, one town |
| 2399 | Adresář Farmářů | Adresář Farmářů | 632 | Farm shops; could feed shop=farm, but mostly farm addresses; open lead |
| 5170 | Vyrobeno v Pardubickém kraji | Agrovenkov | 607 | Local producers (businesses) |
| 2004 | Bitcoin mapa | Bitperia | 880 | payment:bitcoin; BTCMap already edits OSM directly, so low value |
| 603, 4610 | Mapa českých pivovarů, Minipivovárci | private users | 457, 2,599 | Breweries and brewpubs; hobby lists, low priority |
| 1845, 2917, 2307 | Rozhledny, Vodopády, Studánky a větrné mlýny | private users | 1,159, 370, 349 | Hobby lists of features OSM and ZABAGED already cover |
| 78 | Školní zahrady | private user | 952 | School gardens; inside school grounds, not public |
| 4807 | Putování s koňmi | private user | 384 | Horse-riding stables and routes; small |
| 3976, 506, 1807, 208, 32370 | FandiMat, Nadace Veronica, social-service maps | NGOs / municipal office | 54–662 | Donation needs and service providers, not mappable places |

All other Czech maps checked by name and category were personal trip logs, event
maps (Týden vědy, Ukliďme svět, festivals), business locators (SAZKAmobil, ČSOB ATMs,
Lidl) or tourist tips. Business locators belong to AllThePlaces, not Mapotic.

## Maps that need authentication

The Mlékomaty map found in round 3 and every id that returned 401 in the scan are
private or unpublished; their POIs cannot be read anonymously.

## Round 5 follow-up (2026-09-28)

The open leads above were re-fetched (`/api/v1/maps/<id>/` and `pois.geojson/`) and matched against the
local 2026-09-27 Czechia extract (Postpass unavailable). No map states a data licence.

| id | Map | Owner found | Result |
|---|---|---|---|
| 2399 | Adresář Farmářů | Hnutí DUHA; KPZ and educational farms maintained by AMPI (map about page) | **Candidate** `candidates/duha-adresar-farmaru.md`: 408 of 424 farms/farm shops have no shop=farm within 150 m; OSM CZ has about 100 shop=farm |
| 13712 | Akce žába | Český svaz ochránců přírody (campaign linked from biodiverzita.csop.cz) | **Candidate** `candidates/csop-akce-zaba.md`: 678 road sections (33 signed); 673 have no hazard=* within 500 m, OSM CZ has 0 hazard:animal=amphibian |
| 9291 | Zapádluj | Mapotic team account (zapadluj.cz) | In `candidates/mapotic-outdoor-small-maps.md`: 70 of 79 CZ put-ins lack canoe=* within 150 m; static since 2021 |
| 18659 | Re-use v ČR | private user, label "pef čzu" (student project) | Same file: 133 of 140 missing; only the 74 re-use centres and furniture banks fit shop=second_hand |
| 20 | Bivaky a přístřešky | private user | Same file: 191 of 263 shelters already in OSM within 100 m; 72 missing |
| 8162 | ZnakoMapa | Znakovárna, z.s. (contact given on the map for new entries) | Not written up: 251 of 478 points are "Video průvodce" (sign-language video guides), 140 services and organisations; no OSM tag for sign-language service exists, so there is nothing to import |

mtbczech.cz trail centres and bike parks (`/trailcentra` and `/bikeparky` list the same 57 detail pages under
`/strediska/<slug>`; 49 have `var lat/lon`): not written up. They are well-known trail networks (Rychlebské
stezky, Singltrek pod Smrkem, Kouty Bike Park) whose value for OSM is the trail geometry, which must be traced,
not a point per centre. In the filtered extract 30 of 49 have a site-level cycling object (sport=mtb/cycling,
cycling=*, or a trail/bike name) within 1.5 km; the extract has no highway=path or route relations, so the
19 others are not necessarily missing.
