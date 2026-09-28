# Open data for OpenStreetMap in Czechia

Which open datasets would help the Czech OpenStreetMap map the most — and aren't
already being imported?

This repository collects candidate data sources. For each one we fetched the data itself,
looked up its licence, and measured how much of it is already in OSM. Everything was
checked against live sources on 27–28 September 2026; there are 103 candidate files so far.

### How it was researched

The research ran in rounds, each one a batch of AI agents working through a theme and
writing up what held up. Every round started by ruling out what the community already
imports or tracks (see [What's already covered](#whats-already-covered)).

1. **Baseline.** National registries, city open-data portals and well-known POI sources.
2. **What other maps use.** The data sources [Google, TomTom, Apple, HERE](research/google-and-others-sources.md)
   and [Mapy.com](research/mapy-com-sources.md) credit for Czechia.
3. **Niche but useful.** Community maps, institutional systems, hobby associations, and
   ZABAGED layers outside the POI import.
4. **Mapotic.** A scan of the Czech NGO maps hosted there ([research/mapotic-maps.md](research/mapotic-maps.md)),
   plus write-ups of the best leads from round 3.
5. **Follow-ups** on the Mapotic leads.
6. **Wide sweep.** uMap, ArcGIS Online and Zenodo ([research/platform-sweeps.md](research/platform-sweeps.md)),
   air sports, tourism associations, NGO social services, accessibility, bank ATMs,
   machine-learning datasets and safety points.
7. **ZABAGED audit.** All 149 layers ranked against OSM ([research/zabaged-layer-audit.md](research/zabaged-layer-audit.md)),
   plus more city accessibility maps.
8. **Everyday services.** Health, clothes containers and zero-waste shops, and stop
   accessibility from transit GTFS feeds outside Prague.
9. **Last round** (in progress). ZABAGED tag-mapping fixes for the iD fork, stop
   accessibility in the remaining cities, culture and sports venues, charity shops, and
   places for children and families.

Each candidate says which route into OSM fits it: Sync, the geometry harness planned for
the osmcz iD fork, or MapRoulette (see [By route](#by-route)).

<sub>All nine rounds ran on the $250 of Claude credit Anthropic handed out, with about $10
left over at the end — roughly $2.40 per candidate file.</sub>

## Shortlist

### 1. Ready to go — licence already fine, big gap

| Source | What you get | In OSM today | Route |
|---|---|---|---|
| [Library directory](candidates/nk-adresar-knihoven.md) (Národní knihovna) | ~5,160 public libraries with coordinates and opening hours, weekly updates | 1,556 libraries | Sync |
| [Plzeň open data](candidates/plzen-open-data.md) | 48k trees, 24k street lights, toilets, bike racks, artworks, shelters | 8.9k trees / 1.7k lamps in Plzeň | MapRoulette |
| [Prague trees](candidates/prague-stromy-sdz.md) (IPR, 2018 consent) | 171k trees | 18.6k in Prague; ~97 % missing | Sync |
| [Prague lamps & hydrants](candidates/prague-dtm-lampy-hydranty.md) (IPR technical map) | 121k lamp posts, 1.6k above-ground hydrants | ~90 % missing | MapRoulette |
| [Waste facilities](candidates/mzp-isoh-zarizeni-odpady.md) (MŽP ISOH) | ~5,000 active collection yards, scrap yards, car dismantlers, composting | ~24 % of collection yards mapped | MapRoulette |
| [Power plants](candidates/eru-vyrobny-elektriny.md) (ERÚ) | 38k licensed plants incl. 1,600 hydro, 420 biogas | ~500 hydro; needs geocoding from parcels | MapRoulette |
| [Springs and wells](candidates/zabaged-prameny-studny.md) (ZABAGED 4.01, not in the POI import) | 11,060 springs (5,370 named), 21,652 wells, stable IDs | 4,844 springs; Brdy: 47 of 86 missing | Sync + MapRoulette |
| [Cyklisté vítáni](candidates/known-cyklisti-vitani.md) (known: 2022 consent on Cs:Zdroje_v_jednani, never imported) | 853 certified bike-friendly places, stable IDs | 0 tagged; 125 of 437 accommodation places missing | MapRoulette |
| [Tourist accommodation](candidates/csu-huz-ubytovani.md) (ČSÚ, CC0) | 10,454 hotels, guest houses, hostels, campsites, stable IDs | 4,693 of 10,454 missing nationally (2,028 pensions); Pec pod Sněžkou 88 of 170 | Sync + MapRoulette |
| [Prague disabled parking](candidates/prague-ipr-stani-ztp.md) (IPR/TSK, 2018 IPR consent) | 2,192 reserved ZTP/P spots (3,264 spaces) | 954 missing; centre 265 of 293 | MapRoulette |
| [Tree rows and hedges](candidates/zabaged-liniova-vegetace.md) (ZABAGED 6.12 + Copernicus Small Woody Features) | 351,319 tree rows | 15,921 tree_row + 17,080 hedge ways | iD fork |
| [Power plant areas](candidates/zabaged-elektrarny-plochy.md) (ZABAGED, with ERÚ IDs) | 2,141 plant polygons incl. 1,679 solar parks with MW and `id_eru` | 1,212 solar parks and 310 of 325 gas/biogas plants without an OSM plant | iD fork |
| [Solitary landmark trees](candidates/zabaged-osamele-stromy.md) (ZABAGED 6.11) | 33,592 landmark trees | 31,918 missing (95 %) | Sync + iD fork |
| [Covered water reservoirs](candidates/zabaged-vodojemy-zemni.md) (ZABAGED areál – vodojem zemní) | 6,950 reservoirs | 5,776 missing; 613 `reservoir_covered` in CZ | Sync + iD fork |
| [Industrial chimneys](candidates/zabaged-tovarni-kominy.md) (ZABAGED 1.10) | 6,117 chimneys, 1,997 with height | 3,650 missing | Sync + iD fork |
| [Out-of-hours emergency services](candidates/kraje-lspp-pohotovosti.md) (4 regions, NKOD) | 37 LSPP places with hours and pavilion | 5 with a nearby "pohotovost" object; `healthcare:speciality=emergency` used 7× in CZ | MapRoulette + Sync |
| [Gates and barriers](candidates/zabaged-zabrany.md) (ZABAGED 2.36, not in the POI import) | 36,809 barriers, mostly on forest tracks | Křivoklátsko: 321 of 375 missing | MapRoulette |

### 2. Worth asking for consent — high impact, CC BY or no licence

| Source | What you get | In OSM today | Who to ask | Route |
|---|---|---|---|---|
| [Listed monuments](candidates/npu-uskp-pamatky.md) (NPÚ ÚSKP) | 39k monuments, each with a RÚIAN building code → can tag existing buildings | ~5 % tagged | NPÚ | Sync + iD fork |
| [Brno open data](candidates/brno-data-portal.md) | 120k trees, 42k light poles, 12k benches, bins, playgrounds | 9.4k trees in Brno | data.Brno (Jiří Komínek) | Sync + MapRoulette |
| [Doctors & dentists](candidates/uzis-nrpzs-ambulantni.md) (ÚZIS NRPZS) | 40k practices: 5.6k dentists, 7.3k GPs, specialists, opticians | 585 dentists | ÚZIS | Sync |
| [MUNI indoor maps](candidates/muni-indoor-munimap.md) | 26.5k rooms, 24k doors, toilets, lifts | Bohunice campus: 57 of 7,003 rooms | MUNI | MapRoulette |
| [Parcel lockers](candidates/atp-and-brands.md): [DPD](candidates/dpd-pickup-cz.md), [GLS](candidates/gls-cz-parcel-box.md), [Balíkovna](candidates/ceska-posta-balikovna.md) | AlzaBox ~2,000, GLS ~1,590, DPD ~550 missing lockers; 3,800 Balíkovna counters | Zásilkovna consent is the precedent | each operator | – |
| [Memorial trees](candidates/known-aopk-pamatne-stromy.md) (AOPK) | 5,359 protected trees/groups | ~half missing in samples | AOPK | Sync + iD fork |
| [Mine shafts & adits](candidates/cgs-dulni-dila.md) (ČGS) | ~15.7k shafts and adits | ~900 | ČGS | MapRoulette |
| [River gauges](candidates/chmu-vodomerne-stanice.md) (ČHMÚ) | 563 stations with flood-stage levels | ~93 % missing | ČHMÚ | Sync |
| [Street lamps & sirens, Most](candidates/most-opendata.md) (CC BY-SA) | 7,039 lamps with pole codes, 26 sirens | 15 lamps, 0 sirens | město Most | Sync + MapRoulette |
| [VozejkMap](candidates/vozejkmap.md) (CZEPA, Mapotic) | 18,132 accessibility POIs incl. 8,178 disabled parking spaces, 577 accessible toilets | 5,537 of 8,157 disabled spaces missing nationally (Prague centre 342 of 388); 481 of 567 toilets lack accessible OSM toilet | CZEPA | MapRoulette |
| [Bank ATMs](candidates/bank-atm-locators-cz.md) (Sdílený bankomat network, Česká spořitelna API) | 3,095 ATMs of KB, MONETA, Air Bank, UniCredit, ČS; deposit flag, live state | 1,248 without a same-bank ATM within 50 m; 151 closed ČS ATMs still in OSM | KB, ČS | Sync + MapRoulette |
| [Paragliding launch sites](candidates/paragliding-mapa-startovacky.md) (paragliding-mapa.cz) + [ParaglidingEarth](candidates/paraglidingearth-cz.md) (CC BY-SA, now also ODbL) | 234 launch sites with status, wind directions, landings | 24 of 234 in OSM; 43 `sport=free_flying` in CZ | ifire; ParaglidingEarth | Sync |
| [Warning sirens](candidates/czech-siren-tech-mapa-siren.md) (Czech Siren Tech hobby map) | 4,335 JSVV sirens with manufacturer and model | 422 sirens in OSM; Brno 51 vs 2, Ostrava 62 vs 0 | Czech Siren Tech | MapRoulette |
| [VLS rescue points](candidates/vls-body-zachrany.md) (military training areas; OCR CSV from talk-cz 2024) | 484 rescue points with refs | 224 missing (Libavá, Březina, Hradiště) | VLS ČR | Sync |
| [Vets](candidates/kvl-veterinarni-pracoviste.md) (Komora veterinárních lékařů; terms forbid redistribution) | 948 practices, 142 with 24h/emergency, hours | 199 in OSM (21 %) | KVL ČR (written consent) | Sync |
| [Railway station accessibility](candidates/sz-pristupnost-stanic.md) (Správa železnic map API) | 2,700 stations: step-free building/platforms, assistance, SR70 IDs | 465 stations with any wheelchair tag; 512 of 680 fully step-free untagged | SŽ | Sync |
| [Public bookcases](candidates/knihobudka-verejne-knihovnicky.md) (KnihoBudka) | 1,538 bookcases with coordinates | ~850 missing | knihobudka@gmail.com | MapRoulette |
| [Disc golf courses](candidates/cadg-discgolf-hriste.md) (Česká asociace discgolfu API) | 212 permanent courses, par, hole layouts, stable IDs | 120 of 200 missing | ČADG | MapRoulette |
| [Street-workout parks](candidates/woclub-workout-hriste.md) (WOclub map) | 707 parks | 467 of 660 outdoor parks missing | WOclub | Sync |
| [Community gardens and composters](candidates/kokoza-komunitni-zahrady.md) (Kokoza, Mapotic) | 224 gardens, 97 community composters | 195 of 213 gardens, 92 of 97 composters missing | Kokoza | MapRoulette |
| [Prague airport services](candidates/letiste-praha-sluzby.md) | 249 terminal POIs with terminal, floor, hours | 92 of 313 POIs have `level` | Letiště Praha | MapRoulette |
| [Fruit trees](candidates/na-ovoce.md) (Na ovoce, Mapotic) | 20,816 fruit trees and shrubs with species | 19,257 of 19,571 have no OSM tree within 10 m; species on 13 of 314 matched | Na ovoce z.s. | MapRoulette |
| [Catholic mass times](candidates/cirkev-bohosluzby.md) (ČBK) | service times, language, wheelchair access per church (attributes only) | 133 `service_times` on 6,662 catholic places of worship (109 of 2,822 churches) | ČBK | MapRoulette |
| [Homeless services](candidates/mapabezdomova-sluzby.md) (Mapa bez domova) | food, showers, day centres, night shelters in Prague, Ostrava, Liberecký kraj | Prague: 3 of 96 in OSM | Mapa bez domova | MapRoulette |
| [Family centres](candidates/sit-pro-rodinu-centra.md) (Síť pro rodinu) | 266 mother/family/community centres | 232 missing; 7 `community_centre=family_centre` in CZ | Síť pro rodinu | MapRoulette |
| [Protestant service times](candidates/cce-evangnet-sbory.md) (ČCE, evangnet.cz) | 230 congregations with Sunday service time and a stable code | 20 of 150 matched churches have `service_times` | Evangnet z. s. | MapRoulette |
| [Public toilets and Euroklíč](candidates/wc-kompas.md) (WC kompas, Mapotic) | 1,339 public and 415 Euroklíč toilets | 25 `centralkey=eurokey`; no OSM toilet within 50 m for 835 of 1,321 public and 304 of 381 Euroklíč | Pacienti IBD | MapRoulette |
| [Karst register JESO](candidates/aopk-jeso-krasove-jevy.md) (AOPK, CC BY 4.0) | 542 caves, 2,332 sinkholes, 452 ponors/karst springs | 214 caves, 264 sinkholes | AOPK | Sync + MapRoulette |
| [Pump tracks](candidates/mtbczech-pumptracky.md) (mtbczech.cz) | 145 tracks with surface | 57 missing (national extract: 61), 44 lack `cycling=pump_track` | mtbczech.cz | MapRoulette |
| [Sign-language services](candidates/znakomapa-znakovy-jazyk.md) (ZnakoMapa, Znakovárna) | 201 places with Czech sign-language service: deaf associations, interpreters, museums with sign-language tours | `deaf` used once in CZ; tagging (`language:cse=yes`?) needs agreement | Znakovárna | MapRoulette |
| [City accessibility maps](candidates/mesta-mapy-pristupnosti.md) (Brno CC BY; Ostrava, Hradec Králové, Opava, Olomouc unclear) | Brno 287 rated buildings; Ostrava 2,060 points; Hradec voice beacons; Opava 162 ZTP bays, 528 crossings with tactile flags | Brno 116 of 287 lack wheelchair info; Opava 154 of 157 ZTP bays missing | cities | MapRoulette |
| [Hearing loops](candidates/unb-indukcni-smycky.md) (Unie neslyšících Brno, Mapotic) | 161 loops | 1 (tag is a draft proposal); 85 of 137 CZ loops have an OSM object within 50 m | UNB | MapRoulette |
| [Farms and farm shops](candidates/duha-adresar-farmaru.md) (Hnutí DUHA, Mapotic) | 424 farms, farm shops, educational farms | 408 missing; 89 `shop=farm` in all CZ | Hnutí DUHA | MapRoulette |
| [Wine map](candidates/vinarsky-fond-vinarska-mapa.md) (Vinařský fond) | 1,731 wineries, wine shops, cellars | 632 of 765 wineries, 535 of 671 wine shops missing | Vinařský fond | MapRoulette |
| [Tourist information centres](candidates/atic-certifikovana-tic.md) (A.T.I.C. ČR) | 546 certified centres with contacts | 226 of 510 missing; most matched lack contacts | A.T.I.C. ČR | MapRoulette |
| [Clothes collection containers](candidates/textil-kontejnery-kloktex-potex.md) (KlokTex, Potex) | 1,463 containers with ids | 869 of 1,192 KlokTex missing; 214 of those only lack `recycling:clothes` | KlokTex, Potex | Sync |
| [Diakonie Broumov containers](candidates/diakonie-broumov-kontejnery.md) (address table, placed via RÚIAN) | 889 textile containers, 752 placed | 585 of 742 without a clothes container within 100 m | Diakonie Broumov |
| [Zero-waste map](candidates/reduca-bezodpadova-mapa.md) (Reduca) | 1,334 places: 479 bulk shops, milk machines, charity shops | 16 `bulk_purchase` in CZ; mostly 2017–2020 data | Reduca | MapRoulette |
| [Socialist-era public art](candidates/vetrelci-volavky-socharstvi.md) (Vetřelci a volavky) | 2,970 sculptures, reliefs, mosaics with artist and year | 945 of 2,689 missing; 286 of 1,744 matched have `artist_name` | Pavel Karous |
| [Member cinemas](candidates/kinari-clenska-kina.md) (Asociace provozovatelů kin) | 233 cinemas incl. summer cinemas, stable ids | 57 missing (small towns) | APK |
| [Water dispensers](candidates/lokni-vydejniky-vody.md) (LOKNI) | 102 indoor refill points at stations and universities | 95 missing | LOKNI | Sync |

### 3. Maintenance and enrichment — mostly mapped, adds IDs and fixes

- [Pharmacies](candidates/sukl-lekarny.md) (SÚKL, CC0) — 1,884 pharmacies without `ref:SUKL`, 301 stale refs, opening hours.
- [Regional technical maps](candidates/known-dtm-zps-kraje.md) (DTM, 5 regions, no copyright) — sidewalk and step
  outlines per municipality. Telč: 370 OSM footways lie inside DTM sidewalks but lack `footway=sidewalk`,
  ~16.5 km of sidewalk and ~20 flights of steps missing, 147 handrails (OSM 0).
- [Level crossings](candidates/sz-prejezdy.md) (SŽ) — 321 missing, 616 outdated refs.
- [Railway stations & platforms](candidates/era-rinf-stanice-nastupiste.md) (ERA RINF) — ~2,000 `uic_ref`, platform heights.
- [Regional public-transport stops](candidates/kraje-zastavky-verejne-dopravy.md) (Jihočeský CC0; Karlovarský,
  Královéhradecký, Olomoucký no rights claimed) — coordinates for stops `jizdni-rady-osm` can't place;
  `ref:CIS_JR` for ~3,400 stops (needs a wiki page first).
- [PID stop attributes](candidates/prague-pid-gtfs-atributy-zastavek.md) — wheelchair access, platform codes, ~1,400 stale `ref:PID`.
- [Plzeň and Olomouc stop accessibility](candidates/pmdp-gtfs-pristupnost-zastavek.md) (PMDP GTFS, CC0-like) — 597 of 680 matched
  Plzeň platforms have no wheelchair tag.
- [IDS JMK stop attributes](candidates/known-idsjmk-gtfs-atributy-zastavek.md) (known, consent 2024) — 1,368 of 1,488 matched
  Brno platforms have no wheelchair tag; regional values are a default, use Brno only.
- [Protected areas](candidates/aopk-zvlaste-chranena-uzemi.md) (AOPK) — IDs and boundary updates.
- [Prague cycle routes](candidates/prague-ipr-cyklotrasy.md) (IPR, 2018 consent) — ~16 missing routes, lane check (IPR ~335 km vs OSM 193 km).
- [Weather stations](candidates/chmu-meteostanice.md) (ČHMÚ, CC BY 4.0) — 760 stations, `ref:wigos` IDs.
- [Plzeň traffic signs](candidates/plzen-dopravni-znaceni.md) (CC0) — 28,396 signs for review tasks: stop signs
  (OSM has 5 of 86), weight limits without `maxweight`, 30 zones without `maxspeed`.
- [Wikidata QIDs for niche classes](candidates/wikidata-niche-qid.md) (CC0, QIDs only) — extends Sync's
  Wikidata group: 1,332 unlinked stolpersteine, 1,712 fingerposts, 1,549 abandoned villages, 626 bunkers;
  1,239 of those stolpersteine and 1,592 fingerposts already have an OSM object nearby (linking only).
- [War graves](candidates/known-valecne-hroby-kraje.md) (Liberec, Hradec Králové regions, CC0) — register IDs.

### 4. Smaller or local

Prague: [paid-parking sections](candidates/prague-zps-useky.md), [noise barriers](candidates/prague-protihlukove-steny.md),
[dog zones](candidates/prague-psi-zony.md), [park names](candidates/prague-parky-nazvy.md),
[toilets](candidates/prague-verejne-toalety.md), [fountains and springs](candidates/known-prague-oazy-chladu.md),
[playgrounds](candidates/prague-verejna-hriste.md), [collection yards](candidates/prague-sberne-dvory.md).
Elsewhere: [Pardubice region cycle survey](candidates/pardubicky-kraj-cyklopasport.md),
[nextbike stations](candidates/nextbike-gbfs.md) (mostly virtual — review layer only),
[Ostrava](candidates/ostrava-gis-opendata.md), [Olomouc](candidates/olomouc-opendata.md),
[Jihlava](candidates/jihlava-opendata.md), [TV/radio transmitters](candidates/ctu-vysilace-tv-rozhlas.md),
[dams and weirs](candidates/mze-isvs-voda-hraze-jezy.md), [bathing waters](candidates/vuv-koupaci-vody.md),
[vessel berths](candidates/sps-euris-stanoviste-plavidel.md), [ambulance stations](candidates/kraje-zzs-vyjezdove-zakladny.md),
[geological sites](candidates/cgs-geologicke-lokality.md), [sports registry](candidates/nsa-rejstrik-sportu.md),
[regional tourism layers](candidates/regional-tourism-hubs.md),
[amphibian road crossings](candidates/csop-akce-zaba.md) (ČSOP, 678 sections, 673 unmapped),
[canoe put-ins, re-use centres, shelters](candidates/mapotic-outdoor-small-maps.md) (small Mapotic maps),
[Ústí small monuments](candidates/usti-drobne-pamatky.md), [Orlické hory memorials](candidates/pomniky-orlickych-hor.md) (thesis field survey),
[AI road detections](candidates/ai-road-detections.md) (Microsoft 2025: only 2.5–5.5 % missing — OSM is already complete),
[heliports and ultralight fields](candidates/rlp-vfr-prirucka-heliporty-slz.md) (ŘLP VFR příručka — terms forbid reuse; attributes only),
[mountain rescue stations and webcams](candidates/horska-sluzba-mapa.md) (Horská služba, CC BY-SA),
[boulders and rocks](candidates/zabaged-osamele-balvany-skaly.md) (ZABAGED, 11,216 missing; stone vs rock is the mapper's call),
[walls](candidates/zabaged-zdi.md) (ZABAGED 1.23; ZABAGED has no fence type).

### Open leads not yet researched

From rounds 3–6 (checked, not written up):

- Regionální značky: 1,445 certified products/services with GPS in one JSON call; mostly products at producers'
  addresses. Official hotel stars (Hotelstars Union, 275 CZ hotels): terms forbid reuse.

- Platform sweeps (uMap, ArcGIS Online, Zenodo) found little original open Czech data from non-government
  people — see [research/platform-sweeps.md](research/platform-sweeps.md).

- zanikleobce.cz abandoned villages (OSM has 155): all rights reserved, ask the author.
- mtbczech.cz trail centres and bike parks: same structure as the pump-track list.

- MŠMT school register (CC0) for what ZABAGED lacks: 298 of 531 art schools (ZUŠ), 221 of 326 youth centres,
  300 of 356 student dormitories missing.
- ČHMÚ air-quality stations (CC BY 4.0): 208, only 33 in OSM.
- Opava city map services (© only): 1,266 benches, 268 tactile crossings, 162 disabled parking spaces.
- Děčín public lighting (CC0 DXF): 7,313 luminaires against 10 in OSM, no IDs.
- Overture Places (licence fine, CDLA Permissive 2.0): Kolín test found mostly Facebook-page businesses and
  name mismatches — a hint layer only. Mapillary detections need a free token to measure.
- zanikleobce.cz (abandoned villages, 1,733 Wikidata links) and vodopady.info (waterfalls): licences unchecked.

Earlier rounds:

- ŘSD bridges, kilometre posts and rest areas (the existing ŘSD permission is about road numbers).
- ERÚ heat plants and electricity storage; ČHMÚ groundwater wells.
- Prague district (MČ) datasets in the Prague LKOD; Golemio (needs an API key, no licence found).
- Děčín and Liberec city portals (unreachable during this round).
- ŘSD/NDIC data portal `mobilitydata.rsd.cz` (rest areas, truck parking) and the Ústecký kraj stop API —
  unreachable from the research environment; retry from another network.
- Worth asking, no open dataset: KČT trail network, Český horolezecký svaz rock database (climbing bans),
  Asociace lanové dopravy (ropeways), Ministry of Health bathing places (koupacivody.cz).
- Mapy.com's ODbL [missing-paths file](https://pro.mapy.com/osm-user-updates/2026.geojson.gz) has nothing
  in Czechia (mostly Alps) — could be passed to AT/IT/SI communities.

### Corrections for Cs:Česko/freemap

- estudanky.eu is now CC BY-NC-SA 4.0 (the page says CC BY-NC-ND 3.0) — still incompatible.
- Memorial trees (AOPK): licence is CC BY 4.0 (the page says unknown).
- IPR Praha: besides the orthophoto consent, a 2018 consent covers all IPR open data
  ([talk-cz](https://lists.openstreetmap.org/pipermail/talk-cz/2018-February/018526.html)).

## By route

Which of the community's routes into OSM fits each candidate (the `sync_fit` row; see
[AGENTS.md](AGENTS.md#scoring-impact-15)). Sorted by impact; the icon is the licence status.
A candidate with several layers can appear under more than one route.

### Sync — points with a stable ID and a 1:1 tag mapping (42)

- ✅ [Centrální adresář knihoven a informačních institucí v ČR](candidates/nk-adresar-knihoven.md) — impact 5
- ✅ [Sdílená data o zeleni](candidates/prague-stromy-sdz.md) — impact 5
- ✍️ [data.Brno](candidates/brno-data-portal.md) — impact 5
- ✍️ [Ústřední seznam kulturních památek](candidates/npu-uskp-pamatky.md) — impact 5
- ❓ [Bank ATM locators](candidates/bank-atm-locators-cz.md) — impact 4
- ❓ [DPD CZ Pickup](candidates/dpd-pickup-cz.md) — impact 4
- ❓ [GLS Czech Republic](candidates/gls-cz-parcel-box.md) — impact 4
- ✍️ [NRPZS](candidates/uzis-nrpzs-ambulantni.md) — impact 4
- ✍️ [Památné stromy](candidates/known-aopk-pamatne-stromy.md) — impact 4
- ❓ [Paragliding Mapa](candidates/paragliding-mapa-startovacky.md) — impact 4
- ❓ [Správa železnic](candidates/sz-pristupnost-stanic.md) — impact 4
- ✅ [ZABAGED 4.01 Zdroj podzemních vod](candidates/zabaged-prameny-studny.md) — impact 4
- ✅ [ČSÚ](candidates/csu-huz-ubytovani.md) — impact 4
- ❓ [Česká pošta](candidates/ceska-posta-balikovna.md) — impact 4
- ❓ [ERA RINF](candidates/era-rinf-stanice-nastupiste.md) — impact 3
- ✅ [IDS JMK GTFS](candidates/known-idsjmk-gtfs-atributy-zastavek.md) — impact 3
- ❌ [KVL ČR](candidates/kvl-veterinarni-pracoviste.md) — impact 3
- ✍️ [Ostrava](candidates/ostrava-gis-opendata.md) — impact 3
- ✅ [PMDP Plzeň GTFS](candidates/pmdp-gtfs-pristupnost-zastavek.md) — impact 3
- ✍️ [ParaglidingEarth](candidates/paraglidingearth-cz.md) — impact 3
- ✅ [Regional public transport stop registers](candidates/kraje-zastavky-verejne-dopravy.md) — impact 3
- ✅ [SÚKL Seznam lékáren](candidates/sukl-lekarny.md) — impact 3
- ❓ [Textile collection containers](candidates/textil-kontejnery-kloktex-potex.md) — impact 3
- ❓ [VLS ČR](candidates/vls-body-zachrany.md) — impact 3
- ❓ [WOclub / WOblog](candidates/woclub-workout-hriste.md) — impact 3
- ✅ [ZABAGED 1.27 Areál účelové zástavby](candidates/zabaged-vodojemy-zemni.md) — impact 3
- ✅ [ZABAGED 6.11 Významný nebo osamělý strom](candidates/zabaged-osamele-stromy.md) — impact 3
- ✅ [nextbike Czech Republic](candidates/nextbike-gbfs.md) — impact 3
- ✍️ [ČHMÚ](candidates/chmu-vodomerne-stanice.md) — impact 3
- ✍️ [AOPK JESO](candidates/aopk-jeso-krasove-jevy.md) — impact 2
- ✍️ [Data Olomouc](candidates/olomouc-opendata.md) — impact 2
- ✍️ [Horská služba ČR](candidates/horska-sluzba-mapa.md) — impact 2
- ✅ [Kraje](candidates/kraje-lspp-pohotovosti.md) — impact 2
- ❓ [LOKNI](candidates/lokni-vydejniky-vody.md) — impact 2
- ✅ [MZe ISVS-VODA](candidates/mze-isvs-voda-hraze-jezy.md) — impact 2
- ✍️ [Most city open data](candidates/most-opendata.md) — impact 2
- ✍️ [PID GTFS](candidates/prague-pid-gtfs-atributy-zastavek.md) — impact 2
- ❓ [Seznam železničních přejezdů na síti Správy železnic](candidates/sz-prejezdy.md) — impact 2
- ✍️ [VÚV TGM / MŽP](candidates/vuv-koupaci-vody.md) — impact 2
- ✅ [ZABAGED 1.10 Tovární komín](candidates/zabaged-tovarni-kominy.md) — impact 2
- ❓ [opendata.jihlava.cz](candidates/jihlava-opendata.md) — impact 2
- ✍️ [ČHMÚ](candidates/chmu-meteostanice.md) — impact 2

### iD fork — lines and areas for the planned geometry harness in the osmcz iD fork (13)

- ✍️ [Ústřední seznam kulturních památek](candidates/npu-uskp-pamatky.md) — impact 5
- ✍️ [Památné stromy](candidates/known-aopk-pamatne-stromy.md) — impact 4
- ✅ [ZABAGED 6.12 Liniová vegetace](candidates/zabaged-liniova-vegetace.md) — impact 4
- ✅ [ZABAGED Elektrárna](candidates/zabaged-elektrarny-plochy.md) — impact 4
- ✅ [Digitální technická mapa krajů](candidates/known-dtm-zps-kraje.md) — impact 3
- ✅ [ZABAGED 1.27 Areál účelové zástavby](candidates/zabaged-vodojemy-zemni.md) — impact 3
- ✅ [ZABAGED 6.11 Významný nebo osamělý strom](candidates/zabaged-osamele-stromy.md) — impact 3
- ✅ [MZe ISVS-VODA](candidates/mze-isvs-voda-hraze-jezy.md) — impact 2
- ✅ [Umístění a vlastnosti stanovišť pro plavidla](candidates/sps-euris-stanoviste-plavidel.md) — impact 2
- ✅ [ZABAGED 1.10 Tovární komín](candidates/zabaged-tovarni-kominy.md) — impact 2
- ✅ [ZABAGED 1.23 Zeď](candidates/zabaged-zdi.md) — impact 2
- ✅ [ZABAGED 7.10 Osamělý balvan, skála, skalní suk](candidates/zabaged-osamele-balvany-skaly.md) — impact 2
- ✍️ [Zvláště chráněná území + Natura 2000](candidates/aopk-zvlaste-chranena-uzemi.md) — impact 2

### MapRoulette — pointers for a human: tag choices, no stable ID, or needs a look (68)

- ✍️ [data.Brno](candidates/brno-data-portal.md) — impact 5
- ✅ [opendata.plzen.eu](candidates/plzen-open-data.md) — impact 5
- ✅ [Archivní DTM Prahy](candidates/prague-dtm-lampy-hydranty.md) — impact 4
- ❓ [Bank ATM locators](candidates/bank-atm-locators-cz.md) — impact 4
- ❓ [DPD CZ Pickup](candidates/dpd-pickup-cz.md) — impact 4
- ✅ [ERÚ](candidates/eru-vyrobny-elektriny.md) — impact 4
- ❓ [Masarykova univerzita](candidates/muni-indoor-munimap.md) — impact 4
- ✅ [MŽP ISOH](candidates/mzp-isoh-zarizeni-odpady.md) — impact 4
- ✅ [Praha](candidates/prague-ipr-stani-ztp.md) — impact 4
- ❓ [VozejkMap](candidates/vozejkmap.md) — impact 4
- ✅ [ZABAGED 4.01 Zdroj podzemních vod](candidates/zabaged-prameny-studny.md) — impact 4
- ✅ [ČSÚ](candidates/csu-huz-ubytovani.md) — impact 4
- ❓ [Česká pošta](candidates/ceska-posta-balikovna.md) — impact 4
- ❓ [A.T.I.C. ČR](candidates/atic-certifikovana-tic.md) — impact 3
- ❓ [Adresář farmářů](candidates/duha-adresar-farmaru.md) — impact 3
- ✍️ [City accessibility maps](candidates/mesta-mapy-pristupnosti.md) — impact 3
- ✅ [Cyklisté vítáni](candidates/known-cyklisti-vitani.md) — impact 3
- ✅ [Cyklopasport Pardubického kraje](candidates/pardubicky-kraj-cyklopasport.md) — impact 3
- ❓ [Czech Siren Tech](candidates/czech-siren-tech-mapa-siren.md) — impact 3
- ✅ [Digitální technická mapa krajů](candidates/known-dtm-zps-kraje.md) — impact 3
- ✍️ [Důlní díla v České republice](candidates/cgs-dulni-dila.md) — impact 3
- ❓ [Evangnet](candidates/cce-evangnet-sbory.md) — impact 3
- ❓ [Katolické bohoslužby v ČR](candidates/cirkev-bohosluzby.md) — impact 3
- ❓ [KnihoBudka](candidates/knihobudka-verejne-knihovnicky.md) — impact 3
- ❓ [Mapa bez domova](candidates/mapabezdomova-sluzby.md) — impact 3
- ❓ [Na ovoce](candidates/na-ovoce.md) — impact 3
- ✍️ [Ostrava](candidates/ostrava-gis-opendata.md) — impact 3
- ✅ [Oázy chladu](candidates/known-prague-oazy-chladu.md) — impact 3
- ✅ [Parky](candidates/prague-parky-nazvy.md) — impact 3
- ✅ [Plzeň](candidates/plzen-dopravni-znaceni.md) — impact 3
- ✅ [Protihlukové bariéry](candidates/prague-protihlukove-steny.md) — impact 3
- ❓ [Síť pro rodinu](candidates/sit-pro-rodinu-centra.md) — impact 3
- ✅ [Veřejné toalety](candidates/prague-verejne-toalety.md) — impact 3
- ❓ [Vinařský fond](candidates/vinarsky-fond-vinarska-mapa.md) — impact 3
- ✅ [Volný pohyb psů](candidates/prague-psi-zony.md) — impact 3
- ❓ [WC kompas](candidates/wc-kompas.md) — impact 3
- ✅ [ZABAGED 2.36 Zábrana](candidates/zabaged-zabrany.md) — impact 3
- ✅ [Úseky parkování v zónách placeného stání](candidates/prague-zps-useky.md) — impact 3
- ❓ [ČADG](candidates/cadg-discgolf-hriste.md) — impact 3
- ✍️ [AOPK JESO](candidates/aopk-jeso-krasove-jevy.md) — impact 2
- ❓ [Akce žába](candidates/csop-akce-zaba.md) — impact 2
- ✍️ [Data Olomouc](candidates/olomouc-opendata.md) — impact 2
- ❓ [Kokoza](candidates/kokoza-komunitni-zahrady.md) — impact 2
- ✅ [Kraje](candidates/kraje-lspp-pohotovosti.md) — impact 2
- ❓ [Letiště Praha](candidates/letiste-praha-sluzby.md) — impact 2
- ❓ [MTBczech.cz](candidates/mtbczech-pumptracky.md) — impact 2
- ✅ [MZe ISVS-VODA](candidates/mze-isvs-voda-hraze-jezy.md) — impact 2
- ✍️ [Most city open data](candidates/most-opendata.md) — impact 2
- ✅ [Odpadní zařízení pro občany](candidates/prague-sberne-dvory.md) — impact 2
- ✅ [Prague cycle routes and cycling infrastructure](candidates/prague-ipr-cyklotrasy.md) — impact 2
- ❓ [Reduca](candidates/reduca-bezodpadova-mapa.md) — impact 2
- ❓ [Rejstřík sportu](candidates/nsa-rejstrik-sportu.md) — impact 2
- ❓ [Unie neslyšících Brno](candidates/unb-indukcni-smycky.md) — impact 2
- ✅ [Veřejná hřiště](candidates/prague-verejna-hriste.md) — impact 2
- ✅ [Výjezdové základny zdravotnické záchranné služby](candidates/kraje-zzs-vyjezdove-zakladny.md) — impact 2
- ✍️ [Významné geologické lokality v ČR](candidates/cgs-geologicke-lokality.md) — impact 2
- ✅ [Wikidata](candidates/wikidata-niche-qid.md) — impact 2
- ✅ [ZABAGED 7.10 Osamělý balvan, skála, skalní suk](candidates/zabaged-osamele-balvany-skaly.md) — impact 2
- ❓ [ZnakoMapa](candidates/znakomapa-znakovy-jazyk.md) — impact 2
- ❓ [opendata.jihlava.cz](candidates/jihlava-opendata.md) — impact 2
- ✅ [ČTÚ](candidates/ctu-vysilace-tv-rozhlas.md) — impact 2
- ❌ [ŘLP ČR VFR příručka](candidates/rlp-vfr-prirucka-heliporty-slz.md) — impact 2
- ✅ [AI road detections: Meta MapWithAI Czechia export and Microsoft Road Detections](candidates/ai-road-detections.md) — impact 1
- ✅ [Krajské datové portály](candidates/regional-tourism-hubs.md) — impact 1
- ❓ [Pomníky Orlických hor](candidates/pomniky-orlickych-hor.md) — impact 1
- ❓ [Small Mapotic maps: canoe put-ins](candidates/mapotic-outdoor-small-maps.md) — impact 1
- ✅ [Válečné hroby](candidates/known-valecne-hroby-kraje.md) — impact 1
- ✍️ [Ústí nad Labem](candidates/usti-drobne-pamatky.md) — impact 1

## What's already covered

Known sources are tracked upstream and deliberately left out:
[Cs:Česko/freemap](https://wiki.openstreetmap.org/wiki/Cs:%C4%8Cesko/freemap) (permissions,
potential sources, finished imports), [Cs:Zdroje v jednani](https://wiki.openstreetmap.org/wiki/Cs:Zdroje_v_jednani),
the [ZABAGED POI import](https://wiki.openstreetmap.org/wiki/Cs:POI_ZABAGED_Import) and the
datasets in [Sync](https://codeberg.org/osmcz/sync). Good finds from here get hand-picked
and added to Cs:Česko/freemap.

## Reading a candidate

Each file in [`candidates/`](candidates/) describes one source:

- **Licence status**
  - ✅ **ok** — can be used in OSM (CC0, ODbL, or explicit permission)
  - ✍️ **needs waiver** — attribution licence such as CC BY 4.0; the publisher has to
    give OSM explicit consent first
  - ❌ **incompatible** — can't be used
  - ❓ **unclear** — no licence found; someone has to ask
- **Impact 1–5** — how much it would improve the map: how many features are missing in
  OSM and how useful they are.
- **OSM count** — how many such features OSM in Czechia has today.
- **Try it** — a map preview (a small extract in [`samples/`](samples/), shown as a map by
  GitHub) and what to paste into QGIS to load the full dataset.

For how the research is done, see [`AGENTS.md`](AGENTS.md).
