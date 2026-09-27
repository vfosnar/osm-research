# Commercial networks not yet in Sync: AllThePlaces spiders and brand feeds (CZ)

- **ATP run:** `2026-09-19-13-32-18` (https://data.alltheplaces.xyz/runs/latest.json → output.zip, 5,262 spiders).
  - CZ records were counted by scanning every spider's GeoJSON for `addr:country=CZ`.
  - "CZ records" are unique locations. Car-dealer spiders emit one feature per category (car / car_repair / car_parts), so they are deduplicated by coordinate.
- **OSM counts:** taginfo Geofabrik `europe:czech-republic` (data until 2026-09-26). The count is the larger of `brand:wikidata=<QID>` and `brand=<text>`. Parcel lockers also use a Postpass spatial match (≤40 m, same brand, CZ bbox, 2026-09-27).
- **Gap:** CZ records − OSM count, or "missing" from the spatial match where one exists. It is an upper bound: OSM objects without brand tags are not counted.
- **Excluded:** every spider in Sync's `[group.atp.dataset.*]` (codeberg.org/osmcz/sync `backend/config.toml`, read 2026-09-27). That covers action, albert_cz, billa, brnenka_cz, burger_king_cz, costa_coffee_cz, decathlon_cz, deichmann, dm, douglas_cz, dr_max, dracik, hm, jysk, kaufland, kfc_cz, kik, lidl_cz, mcdonalds_cz, mujobchod_cz, newyorker, novak_cz, o2_cz, omv, penny, pepco, rossmann_cz, shell, sokol_cz, starbucks_eu, takko_fashion, tchibo, tedi, teta_cz, traficon_cz and vodafone_cz.
- **Sync DROP list:** Sync's config explicitly drops `cba_cz`, `hruska_cz` and `zabka_cz` (no per-store id) and `cerveny_kriz_cz` (broken output). These are marked "DROP".
- **Licence:** ATP output is CC0 (ATP's own claim). The brands' own website terms were not checked per brand. Non-ATP feeds have their own candidate files.

## Try it

- **Map preview:** [samples/atp-and-brands.geojson](../samples/atp-and-brands.geojson) shows Coop (row 5 below): the 357 `coop_cz` stores in the South Bohemia bbox 13.5,48.55,15.6,49.6. `osm_coop_within_150m` is false for 196 of them, meaning no OSM shop with brand or name Coop/Jednota lies within 150 m (Postpass, 2026-09-27). There is no locker sample: AlzaBox, GLS and DPD lockers are not in ATP, and their operator feeds have no licence (see those files).
- **QGIS:** *Layer → Add Layer → Add Vector Layer…* → Source type *Protocol: HTTP(S)*, URI `https://alltheplaces-data.openaddresses.io/runs/2026-09-19-13-32-18/output/coop_cz.geojson`. For any other spider, replace `coop_cz`. The current run id is in https://data.alltheplaces.xyz/runs/latest.json.

## Table (sorted by gap)

| # | Brand / network | Spider or feed | CZ records | OSM count CZ | Gap | Notes |
|---|---|---|---|---|---|---|
| 1 | Nextbike stations | ATP `gbfs` (45 nextbike CZ GBFS systems) | 4,179 | ~110–190 (brand=nextbike 114; brand:wikidata=Q2351279 108) | ~3,870 | GBFS `license_id` CC0-1.0. Most stations are dockless spots, and the wiki says not to map virtual drop-offs. Covered in detail by `nextbike-gbfs.md`. |
| 2 | Balíkovna partner points (post_partner) | feed `balikovny.xml` (3,847); ATP `czech_post_cz` "amenity=yes" (4,497) | 3,847 | post_office=post_partner 71 | ~3,780 | Attribute on existing shops (Allwyn/Žabka, tobacconists), not new points. See `ceska-posta-balikovna.md`. |
| 3 | AlzaBox | **not in ATP**. Feeds: DPD `getAll` (3,987), Balíkovna XML (3,840), GLS JSON (1,454) | 3,987 | 2,136 (Q115254158) | **2,007 missing** (spatial) | Alza's own API needs OAuth partner credentials. Partner feeds carry DPD/ČP ids, not Alza ids. See `dpd-pickup-cz.md`. |
| 4 | GLS Parcel Box | **not in ATP**. Feed `map.gls-czech.com/data/deliveryPoints/cz.json` | 2,059 | 552 | **1,590 missing** (spatial) | Stable id `CZ…-PARCELLOCK..`. See `gls-cz-parcel-box.md`. |
| 5 | Coop (Jednota, Tuty, Konzum, Tip…) | ATP `coop_cz` | 2,264 | ~870 (brand Coop 389 + COOP Jednota 258 + Coop Tuty 62 + Coop Konzum 60 + Coop Tip 36 + others; Q52851660 = 560) | ~1,390 | Stable ref (URL slug). Every record is shop=supermarket and has no `name`, but many are convenience-size village shops. The spider logged 12 errors in this run, which were not investigated. |
| 6 | Bala | ATP `bala_cz` | 1,312 | 11 | ~1,300 | Purchasing alliance of independent grocers (mojebala.cz). Stores trade under their own names, so treat "Bala" as a network or affiliation rather than a sign brand. Has ref and opening_hours. |
| 7 | DPD Pickup Box (own) | **not in ATP**. Feed DPD `getAll` | 728 | 205 (Q114273730) | **553 missing** (spatial) | DPD id matches the existing OSM `ref` format. |
| 8 | TUI | ATP `tui` | 510 | 2 | 508 | **Low quality:** the CZ records come from tui.pl and are partner agencies (for example "Invia.cz, a.s.") branded as TUI. Not recommended. |
| 9 | CBA | ATP `cba_cz` | 469 | 29 | 440 | **DROP** in Sync: no ref. |
| 10 | Penguin Box | **not in ATP**. Feed Balíkovna XML (BOX_PROVIDER=PB) | 384 | 172 | **326 missing** (spatial) | NSI Q120022128. |
| 11 | OX Point | **not in ATP**. Feeds DPD `getAll` and Balíkovna XML | 405 | 93 | **279–287 missing** (spatial) | OSM refs `OX-00025` style exist on 52 objects. |
| 12 | AS 24 (truck fuel) | ATP `as_24` (289) / `total_energies` (112) | 112–289 | 1 | ~110–290 | Card-only truck lanes, often inside other stations. Fuel is covered by ZABAGED, so this only enriches brands. |
| 13 | One Box (Allegro) | **not in ATP**. Feed DPD `getAll` | 790 | 602 | **233 missing** (spatial) | 600 of 602 OSM objects already have ref. |
| 14 | UniCredit Bank (branches + ATMs) | ATP `unicredit_bank_cz` | 344 features / 243 sites (114 bank, 230 ATM) | 150 (brand UniCredit 74 + UniCredit Bank 76; Q45568 147) | ~190 | Stable ref and opening hours. The only big-bank ATM spider for CZ. |
| 15 | Hruška | ATP `hruska_cz` | 420 (no coords) | 259 | 161 | **DROP** in Sync: no ref and no coordinates. |
| 16 | Škoda (dealers/service) | ATP `skoda` | 220 | 83 | 137 | Car shops. |
| 17 | BENU | ATP `benu_cz` | 432 | 307 | 125 | ref = URL. Pharmacies are also in `sukl-lekarny.md`. |
| 18 | MoneyGram | ATP `moneygram` | 109 | 2 | 107 | Service inside other shops. Low map value. |
| 19 | Sinsay | ATP `sinsay` | 148 | 53 | 95 | No ref (KML): the same problem as the DROP list. |
| 20 | Volkswagen (+ Commercial Vehicles) | ATP `volkswagen`, `porsche_holding` | 90 (+87 CV) | 12 | ~78 | Car shops. |
| 21 | Doctor Optic | ATP `doctor_optic_cz_sk` | 88 | 10 | 78 | Optician. |
| 22 | Řeznictví RABBIT | ATP `reznictvi_rabbit_cz` | 91 | ~20 (name Rabbit*; no brand tag) | ~70 | Butcher counters, often inside Penny. |
| 23 | Dacia / Renault | ATP `renault` | 60 / 60 (same sites) | 9 / 24 | 51 / 36 | Car shops. |
| 24 | T-Mobile | ATP `tmobile_cz` | 99 | 50 | 49 | ref present, no opening_hours. |
| 25 | Seat | ATP `seat` | 49 | 2 | 47 | Car shops. |
| 26 | Bonett (CNG/fuel) | ATP `maes_dkv` | 48 | 7 | 41 | DKV card network. Fuel covered by ZABAGED, so this only enriches brands. |
| 27 | Žabka | ATP `zabka_cz` | 112 | 72 | 40 | **DROP** in Sync: no ref. |
| 28 | Audi / Ford / Peugeot / Hyundai | ATP `audi`, `ford`, `peugeot`, `hyundai_cz` | 39 / 64 / 62 / 59 | 5 / 30 / 30 / 30 | 34 / 34 / 32 / 29 | Car shops. |
| 29 | Sport Vision | ATP `sport_vision` | 45 | 16 | 29 | |
| 30 | KM-Prona / Eurobit / Robin Oil | ATP `maes_dkv` | 48 / 43 / 74 | 19 / 20 / 49 | 29 / 23 / 25 | Fuel enrichment only. |
| 31 | CCC | ATP `ccc` | 81 | 55 | 26 | |
| 32 | Mitsubishi / Mazda | ATP `mitsubishi_cz_sk`, `mazda_cz` | 27 / 25 | 2 / 4 | 25 / 21 | |
| 33 | Manufaktura | ATP `manufaktura` | 42 | 18 | 24 | |
| 34 | Benzina (ORLEN) | ATP `orlen` (283 Benzina + 108 unbranded), `maes_dkv` (430 Orlen) | ~390–430 | Orlen 570 + Benzina 154 | ≤0 | **Known (freemap).** Enrichment only: brand rename Benzina→ORLEN, opening hours. |
| 35 | EuroOil (Čepro) | ATP `maes_dkv` | 205 | 231 | ≤0 | **Known (freemap).** |
| 36 | MOL | ATP `mol` (302), `maes_dkv` (288) | 302 | 400 | ≤0 | Enrichment only. |
| 37 | Tesco / Tesco Express | ATP `tesco_eu` | 113 / 12 | 179 / 24 | ≤0 | OSM has more, possibly closed stores. Opening-hours enrichment only. |
| 38 | OBI / Hornbach / IKEA / Paul | ATP `obi_eu`, `hornbach`, `ikea`, `paul_cz` | 32 / 10 / 4 / 19 | 35 / 11 / 10 / 13 | ≤6 | Well mapped already. |
| 39 | Fio banka ATMs/branches | ATP `fio_banka_atm`, `fio_banka` | 244 / 86 | 296 | ≤0 | Already imported ("fio ATMs", Cs:Česko/freemap). |

## Wanted networks with no ATP spider and no open feed found

| Network | What exists | Status |
|---|---|---|
| PPL Parcelbox / ParcelShop | Widget API `https://api.dhl.com/ecs/ppl/widget/v1/accessPoints` needs a per-e-shop `dhl-api-key` (the public widget key returned 401). The CPL API needs a Client ID and secret. www.ppl.cz/en/pickup-points-list is an HTML list of detail pages for PPL/DHL points across Europe. | No open feed. OSM has 749 PPL Parcelbox (Q132131206). |
| Česká spořitelna, KB, ČSOB, Raiffeisenbank, Moneta ATMs/branches | No CZ spiders (ATP has `csob_sk`, `raiffeisen_bank_hr`, `slovenska_sporitelna_sk` only). The ČS "Places API" sits behind the Erste developer portal (registration). The old ČS Garmin XML is listed under *Zastaralé/nefunkční zdroje* on Cs:Česko/freemap. | Known (freemap, obsolete) for ČS; others not found. |
| Euronet ATMs | `euronet_pl` only | not found for CZ |
| Globus, Norma, Flop, Bauhaus, Uni Hobby | Spiders exist only for DE/AT/other countries (`globus_de`, `norma_de`, `bauhaus_*`); none produce CZ output | not found |
| Pilulka Box, Dr.Max Box lockers | none checked in depth (OSM: Q130684499 3, Q133275002 29) | not investigated |

## Method (reproducible)

1. `curl https://data.alltheplaces.xyz/runs/latest.json` → `output.zip` (2.44 GB), plus `stats/_insights.json`. `_insights.json` has per-country `atp_splits` for NSI-matched brands.
2. For each `output/*.geojson` containing `"addr:country": "CZ"`, count features with `addr:country=CZ` by (brand, brand:wikidata, category, ref present).
3. Get taginfo `key/values?key=brand:wikidata` and `tag/stats?key=brand&value=…` for CZ.
4. Match parcel lockers spatially against Postpass `postpass_pointpolygon WHERE tags->>'amenity'='parcel_locker'` in the CZ bbox.
