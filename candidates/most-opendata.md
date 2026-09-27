# Most city open data – street lamps (Stožáry veřejného osvětlení), alarm sirens, inner cycle routes

| Field | Value |
|---|---|
| publisher | Statutární město Most, IČO 00266094 (portal https://opendata.mesto-most.cz/) |
| url | https://mapy.mesto-most.cz/server/rest/services/Opendata/OpendataPasport/FeatureServer/14 (lamps); https://mapy.mesto-most.cz/server/rest/services/Opendata/OpendataUap/FeatureServer/11 (sirens); https://mapy.mesto-most.cz/server/rest/services/Opendata/OpendataProjekty/FeatureServer/4 (Cyklotrasy vnitřní) |
| format | ArcGIS FeatureServer (S-JTSK, outSR=4326 supported) |
| coords | yes |
| records | street lamps 7,039 points (INVCIS inventory no., POZN = code on the pole S-###-###, TYPPORIZ 1 = geodetic survey / 2 = drawn); sirens 26 points; cycle routes 182 lines (ZNACENI only: svisleZnaceni, piktogramyChodnik, opatreniVozovka) |
| osm_tags | highway=street_lamp + lamp_ref=&lt;code on pole&gt;; emergency=siren |
| osm_count_cz | highway=street_lamp 62,220; emergency=siren 403 (taginfo 2026-09-26). Most bbox (13.56,50.46,13.72,50.56, Postpass 2026-09-27): 15 street lamps; 0 sirens (bbox 13.56,50.42,13.72,50.56) |
| license | CC BY-SA 4.0 |
| license_url | https://creativecommons.org/licenses/by-sa/4.0/legalcode.cs |
| license_status | needs_waiver |
| update_freq | irregular (lamp item modified 2025-04) |
| impact | 2 |
| verified | yes |

## Notes
- **Why it is here:** Google's legal notices for Czechia credit a Most (IČO 00266094) NKOD dataset
  (`…/00266094/de4ba6a0ef4db1d074a9d719a45332a0`). That record no longer exists in NKOD (404, not in
  SPARQL). Most likely it is "Cyklotrasy vnitřní", which matches the other Czech entries on Google's list
  (all cycling layers). The city's ArcGIS hub (owner OpenDataMost, 45 items) is live, and its most useful
  layer for OSM is the street lamps.
- **Street lamps:** OSM has almost none in Most (15 against 7,039). The dataset has a surveyed-geometry flag
  and the code printed on each pole. The description says POZN "S-###-###" is shown on the pole as "######".
  `lamp_ref` (wiki: de facto, "identification number of a street lamp, assigned by the operator") fits.
  Taginfo CZ shows lamp_ref as unused so far; other CZ candidates use `ref`, so the community should pick
  one. Import only points with TYPPORIZ=1 (surveyed).
- **Sirens:** 26 points with ID_CO and KAPACITA fields; OSM has none in the area. Tag emergency=siren +
  siren:purpose=civil_defense (wiki Tag:emergency=siren).
- **Cycle routes:** 182 segments with a marking type only (no route number), so low value.
- The hub also has Zastávky MHD, Válečné hroby a památníky, Prostory pro volné pobíhání psů and a detailed
  surface map (Objektová mapa povrchové situace). These were not evaluated.
- **Licence:** CC BY-SA 4.0 on every item, so a waiver/consent from Magistrát města Mostu is needed.
- Wiki pages read: Tag:highway=street_lamp, Key:lamp_ref, Tag:emergency=siren.

## Wiki entry
```
===Most – stožáry veřejného osvětlení a sirény===
* dataset: Stožáry veřejného osvětlení; Poplachové sirény; Cyklotrasy vnitřní
* gestor: [https://opendata.mesto-most.cz/ Statutární město Most]
* licence: CC BY-SA 4.0 [https://creativecommons.org/licenses/by-sa/4.0/legalcode.cs]
* datové primitivy: body, linie
* odkaz: https://mapy.mesto-most.cz/server/rest/services/Opendata/OpendataPasport/FeatureServer/14
* navržený tag {{tag|highway|street_lamp}} + {{tag|lamp_ref|<kód na stožáru>}}, {{tag|emergency|siren}}
* poznámka: v OSM je v Mostě 15 lamp proti 7 039 v datech města a žádná siréna; nutný souhlas (CC BY-SA)
```
