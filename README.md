# Open data for OpenStreetMap in Czechia

Which open datasets would help the Czech OpenStreetMap map the most — and aren't
already being imported?

This repository collects candidate data sources, each checked by hand: does the data
really exist, what licence it has, and how much of it is already in OSM.

> **Status:** first research round done (27 September 2026). 45 candidate files, all
> numbers measured against live OSM data on that date.

## Shortlist

### 1. Ready to go — licence already fine, big gap

| Source | What you get | In OSM today |
|---|---|---|
| [Library directory](candidates/nk-adresar-knihoven.md) (Národní knihovna) | ~5,160 public libraries with coordinates and opening hours, weekly updates | 1,556 libraries |
| [Plzeň open data](candidates/plzen-open-data.md) | 48k trees, 24k street lights, toilets, bike racks, artworks, shelters | 8.9k trees / 1.7k lamps in Plzeň |
| [Prague trees](candidates/prague-stromy-sdz.md) (IPR, 2018 consent) | 171k trees | 18.6k in Prague; ~97 % missing |
| [Prague lamps & hydrants](candidates/prague-dtm-lampy-hydranty.md) (IPR technical map) | 121k lamp posts, 1.6k above-ground hydrants | ~90 % missing |
| [Waste facilities](candidates/mzp-isoh-zarizeni-odpady.md) (MŽP ISOH) | ~5,000 active collection yards, scrap yards, car dismantlers, composting | ~24 % of collection yards mapped |
| [Power plants](candidates/eru-vyrobny-elektriny.md) (ERÚ) | 38k licensed plants incl. 1,600 hydro, 420 biogas | ~500 hydro; needs geocoding from parcels |
| [Regional technical maps](candidates/known-dtm-zps-kraje.md) (5 regions) | Fences, walls, steps, sidewalks per municipality | Telč: 5,888 fences vs 125 |

### 2. Worth asking for consent — high impact, CC BY or no licence

| Source | What you get | In OSM today | Who to ask |
|---|---|---|---|
| [Listed monuments](candidates/npu-uskp-pamatky.md) (NPÚ ÚSKP) | 39k monuments, each with a RÚIAN building code → can tag existing buildings | ~5 % tagged | NPÚ |
| [Brno open data](candidates/brno-data-portal.md) | 120k trees, 42k light poles, 12k benches, bins, playgrounds | 9.4k trees in Brno | data.Brno (Jiří Komínek) |
| [Doctors & dentists](candidates/uzis-nrpzs-ambulantni.md) (ÚZIS NRPZS) | 40k practices: 5.6k dentists, 7.3k GPs, specialists, opticians | 585 dentists | ÚZIS |
| [MUNI indoor maps](candidates/muni-indoor-munimap.md) | 26.5k rooms, 24k doors, toilets, lifts | Bohunice campus: 57 of 7,003 rooms | MUNI |
| [Parcel lockers](candidates/atp-and-brands.md): [DPD](candidates/dpd-pickup-cz.md), [GLS](candidates/gls-cz-parcel-box.md), [Balíkovna](candidates/ceska-posta-balikovna.md) | AlzaBox ~2,000, GLS ~1,590, DPD ~550 missing lockers; 3,800 Balíkovna counters | Zásilkovna consent is the precedent | each operator |
| [Memorial trees](candidates/known-aopk-pamatne-stromy.md) (AOPK) | 5,359 protected trees/groups | ~half missing in samples | AOPK |
| [Mine shafts & adits](candidates/cgs-dulni-dila.md) (ČGS) | ~15.7k shafts and adits | ~900 | ČGS |
| [River gauges](candidates/chmu-vodomerne-stanice.md) (ČHMÚ) | 563 stations with flood-stage levels | ~93 % missing | ČHMÚ |

### 3. Maintenance and enrichment — mostly mapped, adds IDs and fixes

- [Pharmacies](candidates/sukl-lekarny.md) (SÚKL, CC0) — 1,884 pharmacies without `ref:SUKL`, 301 stale refs, opening hours.
- [Level crossings](candidates/sz-prejezdy.md) (SŽ) — 321 missing, 616 outdated refs.
- [Railway stations & platforms](candidates/era-rinf-stanice-nastupiste.md) (ERA RINF) — ~2,000 `uic_ref`, platform heights.
- [PID stop attributes](candidates/prague-pid-gtfs-atributy-zastavek.md) — wheelchair access, platform codes, ~1,400 stale `ref:PID`.
- [Protected areas](candidates/aopk-zvlaste-chranena-uzemi.md) (AOPK) — IDs and boundary updates.
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
[regional tourism layers](candidates/regional-tourism-hubs.md).

### Open leads not yet researched

- ŘSD bridges, kilometre posts and rest areas (the existing ŘSD permission is about road numbers).
- ERÚ heat plants and electricity storage; ČHMÚ groundwater wells.
- Prague district (MČ) datasets in the Prague LKOD; Golemio (needs an API key, no licence found).
- Děčín and Liberec city portals (unreachable during this round).

### Corrections for Cs:Česko/freemap

- estudanky.eu is now CC BY-NC-SA 4.0 (the page says CC BY-NC-ND 3.0) — still incompatible.
- Memorial trees (AOPK): licence is CC BY 4.0 (the page says unknown).
- IPR Praha: besides the orthophoto consent, a 2018 consent covers all IPR open data
  ([talk-cz](https://lists.openstreetmap.org/pipermail/talk-cz/2018-February/018526.html)).

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

For how the research is done, see [`AGENTS.md`](AGENTS.md).
