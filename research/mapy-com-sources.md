# Data sources credited by Mapy.com (Seznam.cz) for Czechia

Checked 2026-09-27. For every credited source this page gives the evidence URL, the original publisher,
and what it means for OSM.

## Primary evidence: the official "Zdroje dat" document

The "© Přispěvatelé OpenStreetMap a další" link in the Mapy.com map footer opens the licence site
(`lang.copyright.others` in `https://mapy.com/js/lang-cs.2.84.38.js`). That site is a JS shell. It loads
its documents from a public API:

- Human URL: <https://licence.mapy.com/?doc=mapy_attr>
- Raw JSON: <https://pro.mapy.com/licence/v1/documents?types=mapy_attr&lang=cs>
  (document `MAPY_ATTR_0.29`, "Mapy - Zdroje dat", version 0.6)

The document lists credits by map layer. Other evidence used on this page:

- the 3D scene config <https://mapserver-3d.mapy.cz/scenes/latest/mapConfig.json> (credits Seznam, Melown,
  GEODIS, TopGis, Jonathan de Ferranti, basemap.at, USGS/NASA);
- the winter-map legend string "hlavní lyžařská trasa …; značení KČT" (lang-cs.js);
- press coverage, linked in each row.

Mapy.com's own data is proprietary. What matters for OSM is whether each **original** publisher offers
the data openly.

## Czech-relevant credits

### Base, tourist and winter maps

| Credited as | Original / what it is | Open? Licence | Meaning for OSM |
|---|---|---|---|
| © Seznam.cz, a.s. | Own cartography, own field survey, user tracks | No | – |
| © AOPK ČR | Protected areas, memorial trees | Yes. ZCHÚ: see candidate; memorial trees CC BY 4.0 | Already candidates: [aopk-zvlaste-chranena-uzemi](../candidates/aopk-zvlaste-chranena-uzemi.md), [known-aopk-pamatne-stromy](../candidates/known-aopk-pamatne-stromy.md). |
| © Přispěvatelé OpenStreetMap | OSM | ODbL | – |
| © Digitize the Planet e.V. | Protected-area visitor rules and closures, API `https://content.digitizetheplanet.org/api/v2/` | Yes, **CC0** by default (API docs page) | **No candidate.** `protected-areas?country_id=16` (Czechia) returns only 5 records, all Bavarian border areas, and `has_rules=true` returns 0. Nothing Czech to take today. Worth watching: if AOPK or the NP administrations start publishing rules there, it becomes a CC0 source of `access` and seasonal-closure data. |
| © Natural Earth, Austrian sources (BEV, gip.gv.at, Wien…) | Small-scale and Austria | – | Not CZ. |
| "značení KČT" (winter legend) | Klub českých turistů: the marked hiking, cycling and ski trail network. KČT is not credited in "Zdroje dat"; only the legend names it. A web-search snippet claimed that KČT regularly sends network changes to Mapy.cz, but I could not confirm this on kct.cz or cs.wikipedia (2026-09-27) | **No.** Bilateral deal, no open dataset found | **Lead:** KČT (kct.cz, Rada značení). The single most valuable source Mapy.com has that OSM lacks is an authoritative, current trail network. Ask KČT whether it shares route changes with Seznam and whether it would do the same for OSM. |

### Cadastre, aerial, panorama, 3D, elevation

| Credited as | Meaning for OSM |
|---|---|
| ČÚZK (cadastre z16-20, orthophoto CC BY 4.0, elevation, addresses) | Known: ČÚZK CC BY 4.0 + OSM consent (Cs:Česko/freemap). |
| TopGis s.r.o., GEODIS BRNO s.r.o. (aerial z8-20 in CZ, archive aerial '03-'15, panorama, 3D, elevation) | Commercial imagery. Not obtainable. |
| Cyclomedia Technology B.V., GIS – Stavinvex a.s. (Panorama) | Commercial street-level imagery. Not obtainable. |
| Melown Maps (3D) | Seznam's own 3D subsidiary. No. |
| 2nd Military Survey (Austrian State Archive), MŽP ČR, Laboratoř geoinformatiky UJEP (historical map) | Old maps (oldmaps.geolab.cz). Not usable for current OSM features. |
| Sentinel-2 cloudless (EOX), NASA, Microsoft, ESA, JAXA, Sonny, Jonathan de Ferranti | Global imagery and DEMs, used outside CZ or at low zoom. Not relevant. |

### Addresses

ČÚZK (RÚIAN), OSM, Wikidata and foreign cadastres. RÚIAN is known (finished import). Wikidata is CC0, but
the community does not bulk-import it (see the Sync config comment).

### Points of interest (the interesting part)

| Credited as | Original / what it is | Open? Licence | Meaning for OSM |
|---|---|---|---|
| © Wikipedia.org, © Wikidata.org | – | CC BY-SA / CC0 | Wikipedia is incompatible. Wikidata is not bulk-imported by convention. |
| © Booking.com | Accommodation | No | Commercial. |
| © Overture Maps Foundation | Global places, buildings | Places CDLA-Permissive-2.0; other themes ODbL (mostly OSM-derived) | Not CZ-specific; not a Czech candidate. |
| © Dopravniinfo.cz, © RSD.cz | ŘSD / NDIC (Národní dopravní informační centrum). Probably motorway rest areas (odpočívky, with services and truck spaces), closures and events. NDIC publishes a DATEX II "Truck Rest Areas (predefined locations)" table (`registr.dopravniinfo.cz/…/cz-ndic_d2-itp-table/`) | **Registration only:** a signed "podmínky užití" through <https://mobilitydata.rsd.cz> (mobilitydata@rsd.cz, per NDIC registry docs) | **Lead, unverified.** rsd.cz, dopravniinfo.cz, registr.dopravniinfo.cz and mobilitydata.rsd.cz all reset the connection from this environment (2026-09-27), so the terms could not be read. The existing ŘSD permission on Cs:Česko/freemap covers only road numbers. Rest areas are already an "open lead" in README. The only NKOD record from ŘSD is SRTI safety events (LOD), which are not map features. |
| © Bezpecneparkovani.cz | Supervised car parks, mostly in Prague, with online booking | No (commercial portal) | Lead only; small. |
| © ANTHONYapp s.r.o. | Ostrava start-up. Live car-park occupancy from barrier and ANPR systems ("also available on mapy.cz", anthonyapp.com) | No | Commercial. Occupancy is not OSM data anyway. |
| © fDrive.cz | Media site with its own field-verified EV charger map (fdrive.cz/mapa-nabijecich-stanic) | No | Commercial. The open equivalent is the **MPO register of public charging stations**, republished by Brno: NKOD `…/44992785/86ea2ee70870ed560996b293d8472369`, `https://data.brno.cz/api/download/v1/items/0214aa59d4ad481683345703467f35f1/geojson?layers=0`, CC BY 4.0, **3,072 stations**. OSM already has 3,086 `amenity=charging_station` (taginfo 2026-09-27), and ZABAGED charging stations are already in Sync, so **no new candidate**. It could serve as a QA layer for sockets and dates. |
| © Powerbox s.r.o. | E-bike charging stations | Permission granted | Known: Cs:Česko/freemap + Sync `powerbox` dataset. |
| © GDDKiA, NAP Slovenija | Polish and Slovenian road authorities | – | Not CZ. |
| © Český hydrometeorologický ústav | Weather and gauging stations (and probably the weather and radar layers) | Yes: opendata.chmi.cz, CC BY 4.0 (but the INSPIRE station layer is CC BY-NC-ND) | Gauging stations: existing candidate [chmu-vodomerne-stanice](../candidates/chmu-vodomerne-stanice.md). **New candidate:** [chmu-meteostanice](../candidates/chmu-meteostanice.md). 760 weather and precipitation stations, 314 within 150 m of OSM, and adds `ref:wigos`. Partly known via the ZABAGED meteo import. |
| © eStudanky.cz | Springs register | CC BY-NC-SA 4.0 | Known, incompatible (see README corrections). |
| © VodackaNavigace.cz | River kilometrage, weirs, put-ins | Unknown | Known (Cs:Česko/freemap "Vodácká navigace a kilometráž"). |
| © Padler.cz | Paddling portal: rivers, campsites, boat rental | No licence found | Lead only (commercial community portal). |
| © Ropiky.net | Pre-war fortifications | Unknown | Known (Cs:Česko/freemap). |
| © ALDR.cz | **Asociace lanové dopravy**: cableways and ski resorts association (not airports) | No open data. aldr.cz announces a "Návrh datového prostoru pro oblast lanové dopravy a horské infrastruktury v ČR" project | **Lead:** ALDR, for an authoritative list of aerialways and ski lifts. Aerialway data is also already open regionally: Karlovarský kraj "Lyžařské vleky a lanovky" (NKOD `…/70891168/637c900d621588d9e9e5702bb711272a`), covered by [regional-tourism-hubs](../candidates/regional-tourism-hubs.md). |
| © Holidayinfo.cz | Ski resort status, webcams | No | Commercial lead. |
| © Bilestopy.cz | Groomed cross-country trails. Mapy shows grooming age and machine type ([mobilenet.cz](https://mobilenet.cz/clanky/mapycz-nove-zobrazi-uroven-upravenosti-bezkarskych-tras-42883)) | CC BY-SA 3.0 (per Cs:Česko/freemap) | Known. |
| © jdemenabezky.cz | Cross-country ski portal | No licence found | Lead only. |
| © zazijcesko.cz | Activity/tourism catalogue (ski, bike, spa) | No licence found | Lead only; no dataset. |
| © Capsa.cz s.r.o. (Skimapa.cz) | Ski resorts, pistes | No | Commercial lead. |
| © Karlovarský kraj | Regional tourism layers ("Lyžařské vleky a lanovky", "Aquaparky, koupaliště a bazény", "Koupací místa s kontrolou kvality vody v roce 2026") | Yes, NKOD / datazapad.cz | Already covered by [regional-tourism-hubs](../candidates/regional-tourism-hubs.md). |
| © ÚZIS ČR | NRPZS healthcare providers | Yes | Already a candidate: [uzis-nrpzs-ambulantni](../candidates/uzis-nrpzs-ambulantni.md). |
| © Státní zdravotní ústav, © Krajské hygienické stanice | Bathing-water quality. The MZd portal koupacivody.cz is backed by `https://geoportal.mzcr.cz/server/rest/services/VerejneAplikace/KoupaciVody_View/MapServer/0` (layer `bathingPlace`: title, type, operator, hasWc/hasShowers/…) | Not in NKOD; no licence found | **Lead, unverified.** The layer schema is readable, but every `query` call timed out (2026-09-27), so I could not get record counts. The official EU bathing sites are already in [vuv-koupaci-vody](../candidates/vuv-koupaci-vody.md). The MZd layer may add bathing places with amenities; ask MZd (Odbor ochrany veřejného zdraví) for its terms. |
| © Český horolezecký svaz | Rock database "Skály ČR". All rock objects with GPS go to Mapy.cz daily ([ČHS, 2017-10-18](https://www.horosvaz.cz/chs-informace/skaly-z-databaze-skal-chs-na-mapy-cz/)), shown as the "Lezecký terén" category | No open download or licence found | Known (Cs:Česko/freemap "Databáze skal ČR", no licence). **Lead:** ask ČHS (skalycr@horosvaz.cz) for the same feed under an OSM-compatible licence. It includes climbing bans (zákaz lezení), which OSM lacks. |
| © Covid Forms App | 2020–22 vaccination/testing sites | – | Obsolete. |

### Public transport

Mapy.com credits no Czech transit operator. The long list is foreign (French, Polish, Italian, Japanese…
GTFS feeds). For CZ, Seznam originally machine-read the timetables CHAPS publishes
([blog.seznam.cz 2015-04](https://blog.seznam.cz/2015/04/na-mapycz-najdete-jizdni-rady-pro-celou-cr/)).
Today the CIS JŘ JDF export is open and is **already used** by the OSM community (vfosnar/jizdni-rady-osm).
Nothing new.

## Partners known from press releases but not in the credits list

| Partner | What | Open? | Meaning for OSM |
|---|---|---|---|
| CCS (Card Commerce Services) | Fuel prices at ~1,663 CZ stations, twice daily ([Seznam blog 2016-06](https://blog.seznam.cz/2016/06/jezdite-na-vylety-autem-mapycz-ukazuji-ceny/)) | No | Commercial; prices are not OSM data. Station lists are covered by ATP/brand work. |
| Portál nehod (DataFriends, ČKP) | Accident hot spots and wildlife-collision warnings in navigation ([portalnehod.cz/produkty-sluzby/mapy-com](https://portalnehod.cz/produkty-sluzby/mapy-com/)) | Derived from Policie ČR accident data | Not map features; nothing for OSM. |
| Ministerstvo zdravotnictví / KHS | Bathing-water quality | See SZÚ/KHS row | See above. |
| KČT | Trail network changes | No | See the KČT lead above. |

## Mapy.com's own open data

<https://pro.mapy.com/osm-user-updates/index.html> (ODbL 1.0) has two datasets:

1. **User Updates to OpenStreetMap POIs** (`2025.jsonl.gz`, `2026.jsonl.gz`): already used by
   [osmcz/mcom-contributions](https://codeberg.org/osmcz/mcom-contributions) (`src/mapy.rs`). Skipped.
2. **Paths Missing from OpenStreetMap** (`2026.geojson.gz`, 174 kB, Last-Modified 2026-09-15): **new and
   not used** by mcom-contributions. The file has 1,574 LineStrings (1,559 `highway=path`, 8 `highway=track`,
   about 585 km), mostly in the Alps. **None lie inside Czechia**: the 44 in the CZ bbox are all in Austria
   (point-in-polygon against the Nominatim CZ border). So it is not a Czech candidate today. It is worth
   passing to the Austrian, Italian and Slovenian communities, and worth re-checking when the next annual
   edition appears.

## Leads to contact (no open dataset exists)

| Organisation | Why | Contact route |
|---|---|---|
| Klub českých turistů | Authoritative marked hiking, cycling and ski trail network (Mapy.com shows "značení KČT") | kct.cz → Rada značení KČT |
| Český horolezecký svaz | Rock and crag database with climbing bans | skalycr@horosvaz.cz |
| ŘSD / NDIC | Rest areas and truck parking (DATEX II), after registration | mobilitydata@rsd.cz, <https://mobilitydata.rsd.cz> |
| Asociace lanové dopravy (ALDR) | National aerialway / ski-lift register (data-space project) | aldr.cz → Kontakty |
| Ministerstvo zdravotnictví | Bathing places layer behind koupacivody.cz | geoportal.mzcr.cz / MZd OOVZ |
| Holidayinfo, Skimapa (Capsa), jdemenabezky, Padler, fDrive, Bezpečné parkování, ANTHONYapp, CCS | Commercial content | Not worth pursuing for OSM, except perhaps Padler (paddling POIs) |
