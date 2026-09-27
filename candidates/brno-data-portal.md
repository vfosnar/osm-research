name: data.Brno – pasport zeleně, mobiliář, veřejné osvětlení, cyklo (multi-layer)
publisher: Statutární město Brno (Odbor životního prostředí, MČ, TSB/Brněnské komunikace, OD), portal data.brno.cz
url: https://data.brno.cz/ (ArcGIS Hub; org services6.arcgis.com/fUWVlHWZNxUvTUh8)
format: ArcGIS FeatureServer (JSON/GeoJSON via query), hub download GeoJSON/CSV/SHP/GPKG/KML; mirrors on https://gis.brno.cz/public/opendata/
coords: yes (points EPSG:3857 in FeatureServer; S-JTSK/WGS84 in file mirrors)
records: trees+shrubs 142,442 (≈119,600 trees); benches 12,305; street-light poles 42,158; litter bins 5,775; playground elements 2,123; bike stands 613 (+298 in mobiliar_doprava); sport grounds/clubs 823; cycling measures 716 lines; drinking fountains 44; dog urinals 15 (all verified 2026-09-27 via returnCountOnly)
osm_tags: natural=tree (+leaf_type, leaf_cycle), amenity=bench, highway=street_lamp, amenity=waste_basket, playground=* / leisure=playground, amenity=bicycle_parking (+capacity), leisure=pitch / leisure=sports_centre, amenity=drinking_water, cycleway=* / highway=cycleway
osm_count_cz: natural=tree 136,307; amenity=bench 89,222; highway=street_lamp 62,220; amenity=waste_basket 26,290; amenity=bicycle_parking 13,650; leisure=playground 15,549; amenity=drinking_water 1,486 (taginfo Geofabrik CZ 2026-09-26)
license: CC BY 4.0 on "autorské dílo"; NKOD says database is NOT protected by sui-generis right and NOT a copyright database
license_url: https://creativecommons.org/licenses/by/4.0/ ; portal terms https://data.brno.cz/pages/licence
license_status: needs_waiver
update_freq: exports refreshed daily/weekly (datum_exportu 2026-09-25/26); NKOD says IRREG, street lights BIENNIAL
impact: 5
verified: yes

## Layers (FeatureServer base https://services6.arcgis.com/fUWVlHWZNxUvTUh8/arcgis/rest/services/<name>/FeatureServer/0)

| layer (name) | count | key attributes | OSM in Brno bbox (Postpass 2026-09-27) |
|---|---|---|---|
| stromy_kere (Pasport zeleně – stromy, keře) | 142,442 (65,536 solitérní listnaté, 25,443 jehličnaté, 23,589 stromořadí…, 155 pařezů) | druh_bio_kod, spravce_tid, nazev (taxon, sparse), GlobalID, ogcfid | natural=tree 9,394 |
| mobiliar_nabytek_a_vybaveni (typ_tid = Lavičky, sedátka) | 12,305 benches of 14,223 (+38 posezení, 16 stolů, 5 ohniště) | typ_tid, popis, spravce, technicky_stav, address | amenity=bench 8,076 |
| ODAE_street_lights (gis.brno.cz/ags1/rest/services/ODAE/ODAE_street_lights/FeatureServer/0) | 42,158 | pole ID | highway=street_lamp 2,688 (only 2 with ref) |
| odpadkove_kose | 5,775 | typ, majitel, spravce, material, konstrukce, GlobalID | amenity=waste_basket 3,099 |
| mobiliar_hriste (Hřiště a herní prvky) | 2,123 elements (herní prvky, sportovní vybavení) | typ_tid, popis, sprava | leisure=playground 720 |
| stojany_na_kola | 613 | kapacita, typ_stojanu, rok_realizace, mc | amenity=bicycle_parking 929 |
| mobiliar_doprava | 1,682 (298 stojany na kola, 3 boxy) | typ_tid | – |
| mobiliar_vodni_prvky | 110 (43 pítka, 23 kašny, 17 hydranty) | typ_tid | drinking_water 79 |
| DrinkingFountains (Pítka) | 44 | TITLE, DESCRIPTION, Spravce | drinking_water 79 |
| mobiliar_jine | 7,876 (15 psí pisoáry, 42 posypové nádoby, 38 telefonní budky) | typ_tid | – |
| sportoviste | 823 (kluby + sportoviště) | nazev, typ_sportoviste_nazev, url | leisure=pitch 1,131 |
| cykloopatreni_realizovana_opendata | 716 lines (164 protisměr, 104 C9, 53 V14, 77 V20…) | typ_opatreni, rok_realizace | – |

Sample rows checked (e.g. bench: typ_tid "Lavičky, sedátka", address, spravce MČ; bike stand: kapacita 10, typ "jiný").

## Notes
- Biggest gaps: street lamps (42k vs 2.7k), trees (~120k vs 9.4k), benches (12k vs 8k), bins. Existing OSM trees in Brno have no source/ref tags (manual), so conflation must be distance-based.
- Tree layer has no species for most records (`nazev` sparse) — only leaf_type/leaf_cycle derivable from druh_bio_kod (listnaté → broadleaved, jehličnaté → needleleaved; leaf_cycle NOT derivable). "Stromy ve stromořadí" could become natural=tree_row lines only via manual work; import as nodes.
- Street lights: only poles, no lamp_mount etc.; wiki Key:lamp_ref shows 0 use in CZ; use `ref` on highway=street_lamp as wiki Tag:highway=street_lamp suggests.
- Brno mobiliář is maintained by individual city districts (MČ) — completeness varies by district; check per-MČ coverage before import.
- License: CC BY 4.0 ⇒ explicit waiver/consent needed per LWG. Precedent: data.Brno already granted explicit consent for OSM use of the IDS JMK GTFS dataset (from 2024-11-18, OSMCZ request template, see Cs:Česko/freemap "Jízdní řád IDS JMK GTFS") — the same portal team can likely extend it to these layers. Contact: data.brno.cz team; talk-cz thread "Souhlas s užitím dat z data.brno.cz" (2024-10/11, https://openstreetmap.cz/talkcz/c4107) names Jiří Komínek (MMB spatial-data administrator) as the contact, offered via Tomáš Kasparek. Earlier talk-cz 2016-10 "Brno – otevřená data (zápis z kontaktní schůzky)" records the city being open to OSM imports (memorial trees and bins were named as candidate POI imports; city was to pick 1–3 pilot projects) — no import followed.
- Suggested ref key: `ref:brno:globalid` is not established; prefer no ref for trees/bins (volatile ogcfid); for street lamps use `ref=<pole number>`.
- Wiki pages read: Tag:natural=tree, Tag:amenity=bench, Tag:highway=street_lamp, Key:lamp_ref, Tag:amenity=waste_basket, Tag:amenity=bicycle_parking, Tag:leisure=playground, Tag:amenity=drinking_water, Tag:leisure=pitch, Tag:highway=cycleway.

## Wiki entry
```
===Brno – pasport zeleně, mobiliář, veřejné osvětlení===
* dataset: Pasport zeleně – stromy, keře; Mobiliář městských částí (lavičky, hřiště, vodní prvky); Stožáry veřejného osvětlení; Odpadkové koše; Stojany na kola; Pítka
* gestor: [https://data.brno.cz/ Statutární město Brno]
* licence: CC BY 4.0 [https://creativecommons.org/licenses/by/4.0/] – nutný souhlas (data.Brno již udělilo souhlas pro GTFS IDS JMK)
* datové primitivy: body (stromy, lavičky, lampy, koše, stojany), linie (cykloopatření)
* odkaz: https://services6.arcgis.com/fUWVlHWZNxUvTUh8/arcgis/rest/services/stromy_kere/FeatureServer/0
* navržený tag {{tag|natural|tree}}, {{tag|amenity|bench}}, {{tag|highway|street_lamp}} + {{tag|ref|<číslo stožáru>}}, {{tag|amenity|waste_basket}}, {{tag|amenity|bicycle_parking}}
* poznámka: V OSM je v Brně ~9 400 stromů a ~2 700 lamp oproti ~120 000 stromům a 42 000 stožárům v pasportu.
```
