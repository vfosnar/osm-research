# Slovakia: known, imported and consented sources (baseline)

Baseline for the Slovak research track, compiled on 30 September 2026 from live reads of the OSM
wiki, the `osm_sk` Google group, the Czech community's Sync config, AllThePlaces run statistics and
the national data catalogue. Anything listed here is **known** and must not be proposed as a new
candidate. A candidate may still build on one of these if it adds something concrete (a stable ID,
a fresher feed, a missing object type); say so in its notes.

## Where the Slovak community tracks sources

| What | Where | Notes |
|---|---|---|
| Consents / permitted sources | OSM wiki [`WikiProject Slovakia/Sources`](https://wiki.openstreetmap.org/wiki/WikiProject_Slovakia/Sources) | The Slovak equivalent of the "permissions" part of `Cs:Česko/freemap`. One `== Section ==` per source with the consent e-mail pasted in a `<blockquote><pre>` block and a `Tagging: <code>source=…</code>` line. Categories `Data sources from Slovakia`, `Import from Slovakia`. |
| Import list | [`Sk:WikiProjekt Slovensko`](https://wiki.openstreetmap.org/wiki/Sk:WikiProjekt_Slovensko), section "Importy" | Links: `Sk:KaporSKAddress`, `Sk:VUBatm import`, `SK:Import obcí`, `Sk:MinvSKAddress`, `Sk:Slovak Libraries Import`, `Sk:bicycle parking Cyklokoalicia import`. Its "Chcete prispieť?" paragraph still says "máme mnoho zdrojov pri ktorých potrebujeme pomôcť s importom (TODO link na tieto zdroje)" — the list of potential sources was never written. |
| Attribution list | [`Contributors`](https://wiki.openstreetmap.org/wiki/Contributors#Slovakia) → Slovakia | NLC forest roads, Ortofotomozaika SR, ZBGIS WMS, Geografický ústav SAV; "All agreement details … are on WikiProject Slovakia/Sources". |
| Discussion | Google group [`osm_sk`](https://groups.google.com/g/osm_sk) ("Openstreetmap Slovakia") | Active (several threads a month in 2026). Readable without login: thread list at `https://groups.google.com/g/osm_sk`, search at `https://groups.google.com/g/osm_sk/search?q=<term>`, thread at `/g/osm_sk/c/<id>`. |
| Chat | Slack `freemap` (invite link on the wiki page), Matrix `#freemap.sk:matrix.org` (bridged) | |
| Task tracker | GitHub `FreemapSlovakia/freemap-operations` issues | Imports and licence-violation cases are tracked there (the ŠOPSR protected-areas reimport was issue #2). GitHub is blocked from this environment (403), so it was **not read** — check it from a normal browser before a round. |
| Community forum | none | `community.openstreetmap.org` has **no Slovak category** (checked `site.json`: only `users-czech` id 120 and country categories; Slovakia is absent). Do not look for SK discussions there. |
| Organisation | [Freemap Slovakia](https://oz.freemap.sk/) (civic association, OSMF local chapter since 2021) | Consent requests are usually made by its members (Martin Ždila, Michal Bellovič, Filip C, Tomas_J/Tomáš Jančovič, Dodko). |
| Old community wiki | `wiki.freemap.sk` | Referenced from the Sources page (KatasterPortal, NLC, KatasterWMS); **unreachable** from this environment (proxy 502), status unknown. |

### Recommended target page for "## Wiki entry" blocks

There is **no Slovak page equivalent to `Cs:Česko/freemap#Potencionální_zdroje`**. The closest page
is `WikiProject Slovakia/Sources`, but it only lists sources that already have consent (each section
carries the consent e-mail). Recommendation: candidate files end with a paste-ready block for a new
section **`== Potenciálne zdroje ==`** appended to the bottom of `WikiProject Slovakia/Sources`
(above the categories), one `=== … ===` subsection per candidate. That keeps candidates next to the
consented list the community already maintains, and fills the "TODO link na tieto zdroje" on
`Sk:WikiProjekt Slovensko`. Post a link in `osm_sk` when entries are added. Format (Slovak, same
fields as the Czech template so the two tracks stay parallel):

```
=== <Názov> ===
* dataset: <názov datasetu>
* správca: [<url> <organizácia>]
* licencia: <licencia> [<licence_url>]
* dátové primitívy: body/línie/plochy
* odkaz: <download url>
* navrhované značky: {{tag|key|value}}, {{tag|ref:…|<id>}}
* poznámka: <jedna veta o tom, čo v OSM chýba>
```

When a consent is later obtained, the community moves the entry up into its own `== … ==` section
with the e-mail and `Tagging: <code>source=…</code>`, as the existing sections do.

## Imports and bulk edits (done or running)

| Source | Status | Tags / ref | Link |
|---|---|---|---|
| Municipalities (GNS + Štatistický úrad MOS) | Done 19 Feb 2007 (2,608 places) | `city_id`, `import_ref=city_import_sk_1`, `population` | [`SK:Import obcí`](https://wiki.openstreetmap.org/wiki/SK:Import_obc%C3%AD) |
| Country and region borders (VMAP0) | Done Feb 2007 | — | `Sk:História projektu na Slovensku` |
| Cadastre (KaPor / katasterportal) buildings | Near complete by June 2015; buildings of most cadastral areas imported (JOSM FreeKaPor plugin). Catalogue still says "In progress". | `source=kapor2` | [`WikiProject Slovakia/Sources#Cadastral map`](https://wiki.openstreetmap.org/wiki/WikiProject_Slovakia/Sources#Cadastral_map), [`Import/Catalogue`](https://wiki.openstreetmap.org/wiki/Import/Catalogue) |
| KaporSKAddress — conscription numbers from cadastre, then street numbers from municipal FOI replies | 2015 onward; superseded by MinvSKAddress | `addr:conscriptionnumber`, `source:conscriptionnumber=kapor2`, bot `kaporskaddress_bot` | [`Sk:KaporSKAddress`](https://wiki.openstreetmap.org/wiki/Sk:KaporSKAddress) |
| **MinvSKAddress — Register adries (MV SR), CC0** | Main address import since Dec 2017, ongoing. taginfo: **1,493,182** objects with `ref:minvskaddress` (2026-09-29). The ministry stopped publishing structured RA data in January 2025; the last change batch on `download.freemap.sk/minvskaddress/` is `ra_2025-02-04.zip`. Weekly helper output at `https://minvskaddress.freemap.sk/`; stats per district at `https://download.freemap.sk/minvskaddress/okresy.html`. | `ref:minvskaddress`, `source=minvskaddress YYYY-MM`, bot `minvskaddress_bot` | [`Sk:MinvSKAddress`](https://wiki.openstreetmap.org/wiki/Sk:MinvSKAddress), [`Key:ref:minvskaddress`](https://wiki.openstreetmap.org/wiki/Sk:Key:ref:minvskaddress) |
| Slovak National Library directory (SNK) — public libraries | Consent 2016-11-02; import 2016 ("In progress" in catalogue); ~1,742 public libraries in scope | `amenity=library`, no stable ID (MK SR list has IDs, noted as a later `ref` idea) | [`Sk:Slovak Libraries Import`](https://wiki.openstreetmap.org/wiki/Sk:Slovak_Libraries_Import) |
| VÚB bank ATMs | Consent Feb 2016 (address, ID, services; **coordinates excluded**); geocoded import | `ref` = VÚB ATM id | [`Sk:VUBatm import`](https://wiki.openstreetmap.org/wiki/Sk:VUBatm_import) |
| Cyklokoalícia / WhiteBikes Bratislava stands | Consent Mar 2017; imported June 2017, updated 2018 | `ref:cyklokoalicia`, `network=WhiteBikes Bratislava`, bot `cyklokoalicia_bot` | [`Sk:bicycle parking Cyklokoalicia import`](https://wiki.openstreetmap.org/wiki/Sk:bicycle_parking_Cyklokoalicia_import) |
| Slovenská pošta branches | Consent by phone; import June–July 2021 (Dodko) | `amenity=post_office`, `brand=Slovenská pošta`/`Pošta Partner`, `opening_hours` | Sources page, section "Slovenská pošta - pobočky" |
| ŠOP SR protected areas (Štátna ochrana prírody) | Data obtained for OSM in 2022; reimport of 1,161 protected areas done 21 July 2022 (national parks and CHKO still to do at that time); tagging agreed in a shared spreadsheet | — | `osm_sk` thread "reimport chránených oblastí ŠOPSR" (`WZ-s0v8xfyM`), freemap-operations issue #2 |
| SR–CZ border stones (surveyed by user milof) | Import announced 25 May 2025, "licenčne vyriešené" | `boundary=marker` | `osm_sk` thread "Import hraničných kameňov SR ČR" (`t_1Rqha-CF0`) |
| ropiky.net (1936–38 fortification bunkers) | Proposed May 2024 to add `ref:ropiky.net` / state; 290 of 317 SK pillboxes already carry `ref:ropiky.net` | `bunker_type=pillbox`, `ref:ropiky.net`, proposed `state:ropiky.net` | `osm_sk` thread "Import ropiky.net" (`U-f9FKza7jI`) |
| Chimneys from koda.kominari.cz (Czech chimney-sweep association) | Done by Dodko: 498 chimneys added/updated in SK | `height`, `website` (link to the chimney's card) | `osm_sk` thread "Zaujimavy zdroj dat - kominy" (`8NDnYKADITA`) |
| Missing peaks from ZBGIS | Proposed 2018 by Martin Ždila (manual import); licence then questioned; ZBGIS consent came in 2023 | `natural=peak`, `source=ZBGIS` | `osm_sk` thread "import chybajucich vrcholov zo ZBGIS" (`C7x15eijxuw`) |
| MapRoulette: missing town halls | Challenge 55079 by Filip C (May 2026), ~800 municipalities without `amenity=townhall` | `amenity=townhall`, `townhall:type` | `osm_sk` thread `LPxPKgYRv-4` |
| MapRoulette: missing railway level crossings | TomTom challenge (77 tasks), 2026 | `railway=level_crossing` | `osm_sk` thread `gYHRDSz550o` |
| Forest tracks from DMR 5.0 / LLS | Ongoing community tracing project | — | `Sk:WikiProjekt Slovensko/Mapovanie lesnych ciest z DMR5.0` (linked, page not created) |
| Forest/landcover extraction from LLS point clouds | Recipe published (LAStools/whitebox → polygons) | — | [`Sk:LLS ÚGKK SR`](https://wiki.openstreetmap.org/wiki/Sk:LLS_%C3%9AGKK_SR) |
| Road refs from SSC "Miestopisný priebeh cestných komunikácií" | Consent 13 June 2007 | `source:ref=www.ssc.sk` | `Sk:História projektu na Slovensku`, [`Slovakia road mapping status`](https://wiki.openstreetmap.org/wiki/Slovakia_road_mapping_status) |

## Consents on `WikiProject Slovakia/Sources` (all known)

| Source | Holder | Consent | Tagging |
|---|---|---|---|
| Atribúty katastrálneho operátu (AKO), `https://ako.vugk.sk/` open data | ÚGKK SR | e-mail 2022-05-25 | `source=ÚGKK SR AKO` (offline mirror `https://osm.margus.sk/ako/data/out/all/`) |
| Územné a správne usporiadanie (admin boundaries) | GKÚ Bratislava | e-mail 2021-03-16 | `source=GKÚ Bratislava` |
| DMR 5.0 (LiDAR terrain model) | ÚGKK SR | e-mail 2021-03-04 | `source=ÚGKK SR DMR 5.0` |
| All INSPIRE view and download services on geoportal.sk | ÚGKK SR / GKÚ | e-mail 2021-03-04 | `source=ÚGKK SR Inspire` / `GKÚ Bratislava Inspire` |
| Ortofotomozaika SR (orthophoto) | GKÚ + NLC | e-mail 2020-10-13 (free-use terms) | `source=Ortofotomozaika SR`; tiles `https://ofmozaika.tiles.freemap.sk/{zoom}/{x}/{y}.jpg` |
| ZBGIS WMS and all "voľne dostupné služby ZBGIS" on geoportal.sk | GKÚ Bratislava | e-mail 2023-06-28 (replaces 2018 five-year agreement) | `source=ZBGIS` |
| Geomorphological units | Geografický ústav SAV | contract on crz.gov.sk | `source=Geografický ústav SAV` |
| Cadastral map (KaPor) | ÚGKK | "not copyrighted" statement | `source=kapor2` |
| Forest roads | Národné lesnícke centrum (NLC) | agreement (image on wiki) | `source=NLC` |
| VÚB ATMs (address, id; no coordinates) | VÚB | e-mail 2016 | `ref` |
| Tesco shops (name, type, address, hours, contact from tesco.sk/obchody; not map coordinates) | TESCO STORES SR | e-mail (user aceman444) | `source=www.tesco.sk` |
| Barborská cesta GPX | Skeyemap s.r.o. | e-mail | — |
| Bus stops, district Rožňava (name, GPS, ISCP code) | eurobus, a.s. | e-mail | — |
| High Tatras peak/saddle names (map "Východné Tatry 1:20000") | Litvor (Marián Jacina) | Jan 2021 | `source=Litvor` |
| Tatra names from photo maps (not schematic maps) | Miroslav Peťo, miropeto.sk | Feb 2021 | `source=MiroslavPeťo` |
| Slovenská pošta branches (posta.sk, otvaraciehodiny.posta.sk) | Slovenská pošta | phone, 2021 | see import above |
| ŽSR national traffic-point abbreviations | ŽSR | e-mail 2021-09-09 (XLS), requested for OpenRailwayMap | — |
| Bus stops of Banskobystrický samosprávny kraj (XLS: name, GPS, shelter, bench, bin, lit, wheelchair, tactile paving) | BBSK | permission image on proxy.freemap.sk | `source=BBSK` |
| Street art in Trnava (galeriaulice.sk) | Mesto Trnava / Galéria ulice | e-mail 2022-11-09 | — |
| Tatra names from petermatula.github.io/tatry | Peter Matula | e-mail 2024-02-14 | — |
| Cycle routes of Prešovský samosprávny kraj (psk.collect.tmapy.sk) | PSK | e-mail 2026-04-16 | — |
| Climbing sites from zagurami.eu | Robo Garafa | e-mail 2026-08-19 | — |
| Climbing sites from boulder.sk | Oliver Vysloužil | e-mail 2026-08-29 | — |
| Climbing sites from tongba.org (HK TONGBA guides) | Martin Kosír | e-mail 2026-09-22 | — |
| Yahoo aerial imagery (Bratislava) | Yahoo | historical | — |

### ÚGKK / GKÚ (ZBGIS) in short

- Open downloads now sit on `https://opendata.skgeodesy.sk/static/…`, linked from
  `https://www.gku.sk/gku/produkty-sluzby/na-stiahnutie/zbgis.html` (read 30 Sep 2026). Each block
  says "Licenčné podmienky: Autor GKÚ Bratislava / ÚGKK SR, Licencia CC-BY 4.0": administrative
  boundaries (Územné a správne usporiadanie, state 30.06.2026), Administratívna mapa 1:250 000,
  **Geografické názvoslovie** (standardised geographic names, GPKG/SHP/GDB/CSV, state 20.07.2023),
  ZBGIS raster map sheets, Ortofotomozaika SR cycles 1–3 (east 2025 published Aug 2026), LLS
  DMR 5.0 / DMP 1.0, 2nd-cycle DMR 6 / DMP 2 per LOT, DMR 3.5.
- The **full ZBGIS vector database is not an open download**: only a sample
  (`vzorka_zbgis_kategorie_*.zip`) is downloadable; complete data "sú poskytované na základe
  objednávky" (order form to gkuzc@skgeodesy.sk). The ZBGIS object catalogue is
  `https://www.skgeodesy.sk/files/sk/slovensky/ugkk/geodezia-kartografia/zb-gis/kto_zbgis.pdf`.
- OSM has consent for: ZBGIS map services (2023), all INSPIRE view/download services (2021),
  DMR 5.0 (2021), admin boundaries (2021), orthophoto (2020), AKO (2022). So deriving from ZBGIS
  WMS and INSPIRE downloads is covered; geographic names and the newer LLS cycle are CC BY 4.0
  downloads whose coverage by the 2021 INSPIRE/DMR consents is not stated — flag, don't assume.
- Buildings: from KaPor (2010–2015). Addresses: MinvSKAddress (RA, CC0).

## Brand / feed sources already handled by tools

- **Czech Sync tool** (`codeberg.org/osmcz/sync`, `backend/config.toml`, read 30 Sep 2026): two datasets
  cover Slovakia — `zasilkovna.dataset.zbox_sk` "Z-BOX Slovensko" (`osm_query_area = 14296`,
  `ref_tag = ref`, operator Packeta Slovakia) and `powerbox.dataset.powerbox` (Powerbox e-bike
  charging, `osm_query_area = [51684, 14296]`, i.e. CZ + SK). All other datasets (ATP brands,
  ZABAGED, Wikidata, Česká pošta, Prague) are clipped to Czechia (51684) or Prague.
- **POI-Importer** (`openstreetmap.cz/poi-importer`, Marián Kyral): the Z-Boxy dataset was extended
  to Slovak data in Nov 2023 (`osm_sk` thread `IuwYXWAtYVg`). Other datasets there are Czech
  (Česká pošta boxes, NAP accommodation, charging stations).
- **AllThePlaces** (run 2026-09-26, `https://data.alltheplaces.xyz/runs/latest.json`): 19 spiders
  are Slovakia-specific by name — `slovenska_posta_sk` (1,596 features, incl. 243 BalíkoBOX lockers),
  `greenway_pl_sk` (1,221), `slovenska_sporitelna_sk` (787), `vub_sk` (693), `csob_sk` (481),
  `prima_banka_sk` (339), `365_bank_sk` (293), `unicredit_bank_sk` (185), `doctor_optic_cz_sk`,
  `mcdonalds_sk`, `mitsubishi_cz_sk`, `hyundai_sk`, `intersport_sk`, `mazda_sk`,
  `dominos_pizza_sk`, `farmfoods_sk`, and three returning 0 (`decathlon_sk`, `douglas_sk`,
  `tatra_banka_sk`). The ATP insights file attributes 7,635 SK features to 141 brand/spider pairs;
  the biggest multinational ones are Slovnaft (`mol`, 286), Lidl (186), Billa (183), dm (168),
  Pepco (161), OMV (131), KiK, Sinsay, Shell, TEDi, Kaufland, Deichmann, Dráčik, JYSK, CCC, Action,
  Fio banka. Brand chains are therefore an ATP/Sync route, not a research target; note that ATP
  licensing is per spider and the Czech Sync treats ATP as a pointer source.

## Known but not imported (discussed, blocked or partial)

- **Cadastre vector open data (ÚGKK, CC BY 4.0)** — discussed May 2022 (`osm_sk` "Open data Katastra
  (vektor)", `oMjY5c0ZBAs`); licence noted as CC BY 4.0 needing clearance. The AKO consent (2022)
  covers the attribute datasets on `ako.vugk.sk`. Buildings are already in OSM from KaPor.
- **CC BY 4.0 open data in general** — in Jan 2021 the community discussed with a ministry why
  CC BY 4.0 blocks OSM use (`C76yC2UZYg8`); no general waiver resulted. 17,374 of ~22,600 datasets
  in the national catalogue carry CC BY 4.0 (SPARQL count, 30 Sep 2026), so almost every
  government candidate is `needs_waiver` by default.
- **GTFS timetables** — Tomas_J looked for Slovak GTFS in 2026 (`E-FgPzc-cgk`): found Bratislava
  (CC BY 4.0) and ŽSR; most cities don't publish; Trnava region didn't answer. For Organic Maps, not OSM.
- **Packeta / DHL pickup points** — tagging discussion 2026 (`0no6nyM1DFM`); Z-BOX already in Sync.
- **Register adries after 2025** — the wiki (`Key:ref:minvskaddress`) says MV SR stopped publishing
  structured RA data from 1/2025, and the last change batch on `download.freemap.sk/minvskaddress/`
  is from 2025-02-04; freemap still keeps a daily list of cancelled addresses (`zrusene_adresy.html`,
  30 Sep 2026). **But** the national catalogue now lists MV SR datasets "Adresy v kraji …"
  (8), "Adresy v okrese …" and "Adresy v obci …" (2,927), all modified 2026-09-29, with GeoJSON
  distributions on `https://rageo.minv.sk/opendata/dataset/address_by_nuts3_SK0xx.geojson` and
  database licence **CC BY 4.0** in the catalogue metadata (the old RA datasets were CC0). The
  file host resets connections from this environment, so the content was not checked. Whether
  the community has noticed this feed, and whether CC BY 4.0 blocks it, is an open question for
  `osm_sk` — but it is still the MinvSKAddress project, not a new candidate.
- **Trees (`natural=tree` for every tree)** — discussed Mar 2023 (`s-VHFxm8-D4`), no import.

## Channels checked and gaps

- Read: every page returned by `allpages` for prefixes `WikiProject_Slovakia`, `Sk:` (non-Key/Tag),
  `SK:`, `Slovakia`, `Freemap`; categories `Import from Slovakia`, `Data sources from Slovakia`;
  `Contributors`; `Import/Catalogue` (Slovakia rows: Slovak cadaster, KaporSKAddress, Slovak
  Libraries); wiki search "Slovakia import", "Slovensko import", "freemap.sk import";
  `osm_sk` front page and searches for `import`, `zdroj`, `licencia` (83 threads; the ones above are the
  import-relevant ones).
- Not read: GitHub `FreemapSlovakia/freemap-operations` issues (403 here), `wiki.freemap.sk`
  (unreachable), Slack/Matrix history.
