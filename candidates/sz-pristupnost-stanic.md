# Správa železnic – přístupnost stanic (step-free station buildings, platforms, passenger assistance)

| Field | Value |
|---|---|
| publisher | Správa železnic, státní organizace (IČO 70994234), interactive map https://mapy.spravazeleznic.cz/pristupnost |
| url | POST `https://mapy.spravazeleznic.cz/serverside/request2.php` with form fields `module=Layers\Bezbarierovost` and `action=load0` (all stations), `load31` (station building accessibility), `load32` (platform accessibility), `load38` (passenger assistance). Per-station services: `module=Layers\ZeleznicniStanice&action=loadStaniceSluzbyV2&ZST_SR70=<5-digit SR70>` |
| format | JSON `{"result":[GeoJSON Feature…]}`, points in S-JTSK (EPSG:5514), undocumented internal API of the map app |
| coords | yes |
| records | 2,700 stations and halts (ZST_SR70, ZST_NAZEV). Building: 1,208 accessible (b1 = step-free incl. ticket office 206, b2 = step-free building 1,002). Platforms: 875 (n1 = all platforms step-free and at standard height 550/380 mm 773, n3 = at least one such platform 102). Passenger assistance available: 931 |
| osm_tags | on railway=station/halt (+ public_transport=station): wheelchair=yes (n1 + b1/b2), wheelchair=limited (n3, or n1 without an accessible building); railway:ref=&lt;SR70 with check digit&gt; for matching |
| osm_count_cz | railway=station 1,218, railway=halt 1,642 (taginfo CZ 2026-09-26). Matching the 2,700 SŽ stations (Postpass 2026-09-27): 2,633 found (1,606 by railway:ref, 1,027 within 250 m), and only **465 carry any wheelchair tag** |
| license | none published. The map and the spravazeleznic.cz site state no terms of use, and SŽ has no datasets in NKOD |
| license_url | https://mapy.spravazeleznic.cz/pristupnost |
| license_status | unclear |
| update_freq | live (served from SŽ's station database; accessibility follows the SŽ SM122 categorisation) |
| impact | 4 |
| verified | yes |

## Try it
- **Map preview:** no sample, because the licence is `unclear`. The publisher's own map shows the layers: https://mapy.spravazeleznic.cz/pristupnost (layer switch "Přístupnost stanice").
- **QGIS:** QGIS cannot POST to this endpoint. Fetch a layer and save it as GeoJSON first:
  ```
  curl -s https://mapy.spravazeleznic.cz/serverside/request2.php \
    --data-urlencode 'module=Layers\Bezbarierovost' --data-urlencode 'action=load32' \
    | python3 -c "import json,sys; print(json.dumps({'type':'FeatureCollection','features':json.load(sys.stdin)['result']}))" > sz_nastupiste.geojson
  ```
  Then *Layer → Add Layer → Add Vector Layer* → `sz_nastupiste.geojson` and set the layer CRS to **EPSG:5514**. The `icon` field holds the n1/n3 or b1/b2 code, and `STAV_SLUZBY` holds its text.

## Notes
- **Gap analysis (all CZ, Postpass 2026-09-27):**
  - 680 stations are fully step-free (n1 with b1/b2). 512 of them have no wheelchair tag in OSM, and 15 are tagged wheelchair=no.
  - 1,383 stations appear in neither accessible layer. 28 of these are tagged wheelchair=yes in OSM, so they are worth a check.
  - For the 931 stations with assistance there is no established OSM key. It could go into `wheelchair:description`, or a new key could be discussed.
- **Matching:** SŽ's `ZST_SR70` is the 5-digit SR70 code. In CZ, OSM `railway:ref` holds the 6-digit form with a check digit (Pardubice hl. n. = 536136). Match on the first 5 digits. The median offset of ref-matched stations is 15 m.
- **ČD station pages** (https://www.cd.cz/stanice/, 2,159 stations; JSON list via POST `/stanice/Home/GetSR70`) use the same b/n codes and add more:
  - codes for visually and hearing-impaired passengers: z1 voice beacons, z2/z2x tactile guide lines, z3 audio information, s1 induction loop, s2 text displays;
  - accessible WC, a mobile wheelchair lift with its hours, luggage and bicycle storage.
  - The station URL id is the 6-digit SR70 (Český Těšín `/stanice/cesky-tesin/332346`).
  - The ČD portal terms (https://www.cd.cz/info/cim-se-ridime/-25703/, §1.3 and §2.2) forbid copying or reuse without a prior written licence, so ČD is `incompatible` unless ČD agrees.
  - Pardubický kraj crawl (139 stations): 122 of the matched OSM stations have no wheelchair tag.
- **Overlap:**
  - ZABAGED has railway stations but no accessibility.
  - [era-rinf-stanice-nastupiste](era-rinf-stanice-nastupiste.md) gives platform heights and `uic_ref`, which complements this.
  - [prague-pid-gtfs-atributy-zastavek](prague-pid-gtfs-atributy-zastavek.md) covers Prague only.
  - Not on Cs:Česko/freemap, Cs:Zdroje_v_jednani or in Sync.
- **Contact:** Správa železnic (the map app is published as `cz.spravazeleznic.datel`). Ask for a CC0 or ODbL consent covering the accessibility layers and the station service list.
- Wiki pages read: Key:wheelchair (values yes/limited/no, public-transport guidance), Key:railway:ref.

## Wiki entry
```
===Správa železnic – přístupnost stanic===
* dataset: Interaktivní mapa SŽ – Přístupnost stanice (bezbariérovost budov, nástupišť, asistence)
* gestor: [https://www.spravazeleznic.cz/ Správa železnic, s. o.]
* licence: neuvedena – nutno požádat o souhlas
* datové primitivy: body
* odkaz: https://mapy.spravazeleznic.cz/pristupnost
* navržený tag {{tag|wheelchair|yes}} / {{tag|wheelchair|limited}} na {{tag|railway|station}}, párování přes {{tag|railway:ref|<SR70>}}
* poznámka: SŽ eviduje 680 plně bezbariérových stanic a 931 stanic s asistencí; z 2 633 stanic nalezených v OSM má značku wheelchair jen 465
```
