# Data providers credited for Czechia by Google, TomTom, Apple and HERE

Checked 2026-09-27. Each entry gives the evidence URL and what it means for OSM.

## Google Maps / Google Earth

Evidence: <https://www.google.com/help/legalnotices_maps/> ("Legal Notices for Google Maps/Google Earth…",
section *Czechia*, plus the *European Union* section).

| Credited as | Link Google gives | Actual dataset | Meaning for OSM |
|---|---|---|---|
| Prague PID Agency (CC BY 4.0) | creativecommons.org/licenses/by/4.0 | PID GTFS, `https://data.pid.cz/PID_GTFS.zip` (ROPID) | Already a candidate: [prague-pid-gtfs-atributy-zastavek](../candidates/prague-pid-gtfs-atributy-zastavek.md). |
| Czech Office for Surveying, Mapping and Cadastre / Czech Land Survey and Cadastre Office / "Stahovací služby Atom: ČÚZK" | cuzk.cz open data pages, atom.cuzk.cz | ČÚZK open data (ZABAGED, RÚIAN, ortho) | Known: ČÚZK CC BY 4.0 + OSM consent on Cs:Česko/freemap; ZABAGED POI import and Sync. |
| Data.Brno (CC BY 4.0) | licence only | Unspecified (probably cycling layers) | data.Brno already a candidate: [brno-data-portal](../candidates/brno-data-portal.md) (includes cyklo measures). |
| Geoportal Praha (CC BY 4.0) | geoportalpraha.cz/…/45063acce89d4b37afc6d51f03f3ad49 | IPR "Cyklistické trasy" (DOP_CUR_DOP_CYKLOTRASY_L) | **New candidate:** [prague-ipr-cyklotrasy](../candidates/prague-ipr-cyklotrasy.md). Covered by IPR's 2018 consent. OSM routes are nearly complete; useful for QA of lanes and contraflow. |
| Pardubicky Kraj Map portal (CC BY 4.0) | mapy.pardubickykraj.cz/data | Cyklopasport | Already a candidate: [pardubicky-kraj-cyklopasport](../candidates/pardubicky-kraj-cyklopasport.md). |
| Data Olomouc (CC BY 4.0) | opendata.olomouc.eu/datasets/ea0770e82b3941379989303e5c5ada91_0 | "Cyklostezky Olomouc" (95 lines) | Already a candidate: [olomouc-opendata](../candidates/olomouc-opendata.md). |
| Czech Data Portal (CC BY 4.0) | data.gov.cz/…/00266094/de4ba6a0ef4db1d074a9d719a45332a0 | Statutární město Most (IČO 00266094). The NKOD record is gone (404, not in SPARQL); probably "Cyklotrasy vnitřní". | **New candidate:** [most-opendata](../candidates/most-opendata.md). Most's hub is CC BY-SA 4.0; its 7,039 street lamps are the valuable part (OSM has 15). |
| Otevřená data MMPr. (CC BY 4.0) | open-data-prerov.hub.arcgis.com/datasets/c18ef7eaa5aa493298294eb7c5395e94 | Přerov "SHP_cyklostezky" (177 segments, 30.8 km) | No candidate: Postpass shows 164/177 segment midpoints already have an OSM cycleway or bicycle-designated way within 15 m. |
| Address points Open data portal in Czechia (CZ) | data.gov.cz/dataset | RÚIAN address points | Known (RÚIAN on Cs:Česko/freemap, finished import). |
| © GEODIS Brno (listed under *Slovakia*, with Eurosense/Geodis Slovakia) | – | Commercial aerial imagery | Not obtainable; Czech firm, commercial imagery supplier. |

What the Google list shows:

- Apart from ČÚZK, RÚIAN and PID, every Czech entry Google credits is a **municipal or regional cycling
  layer**, picked up for the Google Maps bicycle layer.
- The originals are all open CC BY 4.0 (Most: BY-SA), so OSM can use them on the same footing once a waiver
  is granted. IPR already has one.
- **Transit:** Google credits only PID for CZ. The Mobility Database (`https://files.mobilitydatabase.org/feeds_v2.csv`)
  lists these CZ feeds:
  - PID (mdb-767), CC BY 4.0
  - IDS JMK (mdb-2155); known, OSM consent on Cs:Česko/freemap
  - DPMO Olomouc (mdb-1901, `https://www.dpmo.cz/doc/dpmo-olomouc-cz.zip`): 373 stops, no licence stated
  - DPMLJ Liberec (mdb-1902, `https://www.dpmlj.cz/gtfs.zip`): download failed, status inactive
  - PMDP Plzeň (tld-7926, `https://jizdnirady.pmdp.cz/jr/gtfs`): 719 stops; NKOD "Jízdní řády PMDP" terms
    say no copyright, no DB rights
  - a CESNET-hosted "Czech national bus feed JDF" (mdb-2904), which is converted CIS JŘ and already known
    via jizdni-rady-osm
- The city GTFS feeds are small, and their stops are mostly in OSM already.
- The bigger find from this lead is the **regional stop registers with coordinates and CIS stop names**:
  [kraje-zastavky-verejne-dopravy](../candidates/kraje-zastavky-verejne-dopravy.md). They could place most of
  jizdni-rady-osm's 6,025 unlocated CIS stops.
- Google's other Czech data (business listings, Street View, indoor maps, EV chargers, traffic) carries no
  per-country credit in the notices. That points to Google's own collection or global commercial suppliers.
  - Indoor maps exist for Václav Havel Airport Prague and large Prague malls. No open source exists for them.
  - EV chargers: the official MPO register of public charging points is republished openly by data.Brno as
    "Veřejné dobíjecí stanice v ČR" (3,072 points; `https://data.brno.cz/api/download/v1/items/0214aa59d4ad481683345703467f35f1/geojson?layers=0`,
    CC BY 4.0 per NKOD). OSM already has a charging station within 50 m of 354 of 400 sampled points, and
    ZABAGED charging stations are in Sync plus the evmapa.cz permission. So there is little gap; no candidate.
    The operator and power fields are empty in the republished copy.

## TomTom

Evidence: <https://download.tomtom.com/open/legal/copyright-notices-product-attribution-2026-06.pdf> (section
"Czechia") and <https://download.tomtom.com/open/legal/third-party-product-terms-eula-2026-06.pdf>.

| Credited as | Meaning for OSM |
|---|---|
| © ČÚZK, CC BY 4.0 | Known (OSM has consent). |
| Traffic data from ŘSD, Odbor silniční databanky a NDIC (https://mobilitydata.rsd.cz) | Lead only. mobilitydata.rsd.cz (ŘSD's National Access Point for DATEX II traffic data) was unreachable from this environment (connection reset/503). NKOD has only one ŘSD dataset: "Dopravní informace související s bezpečností silničního provozu (SRTI)" (LOD). Static road data (restrictions, speed limits, truck parking) there would be worth checking from another network. It matches the README's open lead "ŘSD bridges, kilometre posts, rest areas". |

## Apple Maps

Evidence: <https://gspe21-ssl.ls.apple.com/html/attribution.html> (Acknowledgements).

- No Czech-specific provider is named. Apple credits OpenStreetMap contributors plus global suppliers
  (Booking.com, Foursquare, Tripadvisor, Yelp, Actonia and others) and a transit-provider list with no
  Czech city. So Apple's CZ base map is OSM plus commercial data, and there is nothing new to obtain.

## HERE

Evidence: <https://legal.here.com/en-gb/terms/general-content-supplier-terms-and-notices>.

- The page has no Czech entry (Austria and Germany are listed), so there is nothing to follow.

## Leads not pursued or not obtainable

- Google Base Map Partner / Geo Data Upload: no Czech municipality announcement found in search. The
  legal-notice entries above are the only public trace.
- Google indoor maps partners (airport, malls): commercial, no open data.
- GEODIS Brno imagery: commercial.
- ÚK (DÚK) CIS stop API (`tabule.portabo.cz`): blocked by this environment's proxy. Its NKOD terms say
  no rights, so retry from another network.
