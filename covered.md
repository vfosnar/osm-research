# Already covered — do not propose

Sources that are already imported, being imported, synced, or in negotiation.
Snapshot 2026-09-27. Sources: OSM wiki (Cs:POI ZABAGED Import, Cs:Česko/freemap,
Cs:Zdroje v jednani, Cs:Import*), codeberg.org/osmcz/sync `backend/config.toml`,
talk-cz archive.

## ZABAGED POI import (Cs:POI_ZABAGED_Import, via Sync)
fuel (MPO, ref:CZ:evcs), embassies (MZV), charging stations (MPO), fire stations
(HZS, ref:CZ:jpo), weather stations (ČHMÚ/ŘSD), hospitals + healthcare facilities
(ÚZIS, ref:CZ:uzis), police (ref:CZ:ps), post offices, schools + school facilities
(MŠMT, ref:izo/izonew/redizo), social facilities (MPSV, ref:CZ:mpsv), public offices (MV).
ZABAGED as a whole is served by osmcz/zabaged-map — treat any ZABAGED layer as known.

## Sync (osmcz/sync) datasets
- drobnepamatky.cz (incl. chapels)
- Wikidata museums, castles (QID only)
- Česká pošta post boxes (schránky)
- Pražská pítka? (`prazskapitka`)
- Zásilkovna Z-BOX CZ + SK
- Prague open data (IPR): metro entrances, parking machines, recycling containers
- Powerbox e-bike chargers
- AllThePlaces spiders: Action, Albert, Billa, Brněnka, Burger King, Costa, Decathlon,
  Deichmann, dm, Douglas, Dr.Max, Dráčik, H&M, JYSK, Kaufland, KFC, KiK, Lidl, McDonald's,
  Můj obchod, New Yorker, Novák, O2, OMV, Penny, Pepco, Rossmann, Shell, Sokol,
  Starbucks, Takko, Tchibo, TEDi, Teta, Traficon, Vodafone

## Other community projects
- Public transport stops vs CIS JŘ (vfosnar/jizdni-rady-osm)
- Mapy.com user POI corrections (osmcz/mcom-contributions)
- RÚIAN addresses (Cs:Import adres z RUIAN), UIR-ZSJ, obce, katastrální hranice
- DIBAVOD water, HS-RS roads, ÚHÚL forest cover, fio ATMs
- Mapy bez bariér (Cs:Import Mapy bez bariér)
- Prague schools/kindergartens activity (#SkolyPraha)
- Zaniklé obce + Geonames (talk-cz thread Sept 2026)

## Permission already granted (Cs:Česko/freemap)
IDS JMK GTFS, Nadace Partnerství POI (Cyklisté vítáni, vinařské stezky), Brno účelová
mapa, EkoKom containers, Zásilkovna, caves.cz, Lesy ČR záchranné body, ČÚZK (CC BY 4.0
+ consent), IPR Praha orthophoto, ČEPS, ŘSD, pLPIS, EEA, ČSÚ RSO.

## In negotiation
- AED zachrankaapp.cz (Ondřej Lopatka, 2026-05)
- KODA chimney database (stalled since 2020)
