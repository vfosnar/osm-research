# Mapa bez domova (mapabezdomova.cz) – food, showers, day centres and night shelters for homeless people in Prague, Ostrava and Liberecký kraj

| Field | Value |
|---|---|
| publisher | volunteer project started by the critical social work platform KRISA, seeded from "Mapa služeb pro ženy bez domova" by Jako doma, o.p.s.; contact praha@mapabezdomova.cz, https://www.facebook.com/mapabezdomova |
| url | https://www.mapabezdomova.cz/info (categories, tags, cities); https://www.mapabezdomova.cz/service/find/&lt;city&gt;?category=all with city `praha`, `ostrava`, `liberecky_kraj` (also `bratislava`, outside CZ); detail https://www.mapabezdomova.cz/service/get/&lt;city&gt;/&lt;place url&gt; |
| format | JSON (undocumented API behind the web app); send `Accept: application/json` |
| coords | yes (WGS84 `latitude`/`longitude` per place) |
| records | 2026-09-28: Praha 549 places / 685 services (268 of the places are public toilets copied from IPR Praha), Ostrava 67, Liberecký kraj 195. Each place has `id`, `url` slug, title, address, contacts; each service has category (21 categories: jídlo, hygiena, denní centra, noclehárny, zdraví, závislosti, materiální pomoc, poradenství…), `time` (free text), `price`, description, tags (muži, ženy, cizinci, mladí, senioři…) |
| osm_tags | `amenity=social_facility` + `social_facility=soup_kitchen` (hot meals) or `=food_bank` (food parcels) or `=outreach` (day centre) or `=shelter` (night shelter) + `social_facility:for=homeless`; `amenity=shower` + `fee=no` for hygiene; `amenity=food_sharing` for "Veřejná lednice" (community fridges); `opening_hours` or `service_times` from `time`; suggested `ref:mapabezdomova=&lt;id&gt;` |
| osm_count_cz | taginfo 2026-09-28: amenity=social_facility 765, social_facility=shelter 24, =outreach 28, =food_bank 3, =soup_kitchen 0, social_facility:for=homeless 8, amenity=shower 352. Local match against the 2026-09-27 Czechia extract: Prague has 110 social_facility/shower/social_centre objects, 1 with social_facility:for=homeless |
| license | none stated (the site credits only the IPR Praha toilets layer, CC BY-SA 4.0) |
| license_url | – |
| license_status | unclear |
| update_freq | irregular, crowd-sourced (users and providers send corrections through the feedback form); no per-record update date |
| impact | 3 |
| verified | yes |

## Try it
- **Map preview:** none, licence unclear.
- **Browser / curl:** `curl -H 'Accept: application/json' 'https://www.mapabezdomova.cz/service/find/praha?category=all'` returns `{"places":[…],"services":[…],"tags":[…]}`; services link to places by `placeId`. Filter one category with its `url` from `/info`, for example `category=jidlo` or `category=hygiena`. Without `category` the answer is empty.
- **One record:** `https://www.mapabezdomova.cz/service/get/praha/denni_centrum_pro_zeny` (Denní centrum pro ženy, Žitná 35: shower 10:30–11:30, soup 11:30–11:45 for 5 Kč, clothing Tu–Fr).
- **QGIS:** not a GIS service; flatten `places` to CSV (X = `longitude`, Y = `latitude`, EPSG:4326) and load with *Layer → Add Layer → Add Delimited Text Layer*.
- **Web viewer:** https://mapabezdomova.cz/praha

## Notes
- **What it adds:** the places people without a home look for first: where to eat today, where to take a
  shower, where to sleep, where to get clothes or see a doctor for free, with times and prices. Most of these
  are not registered social services (church soup runs, Food not bombs, community fridges, laundromats and
  cafés in the "Místní místním" network), so they are **not** in the MPSV register that feeds ZABAGED
  `SocialniZarizeniDefinicniBod` (Cs:POI_ZABAGED_Import §11) and Sync.
- **Gap, measured (local match against the 2026-09-27 Czechia extract, 60 m radius against any
  amenity=social_facility, social_facility=*, amenity=shower or amenity=social_centre):** Prague has **96**
  places in the core categories (food 56, health 39, hygiene 16, material help 14, day centres 7, addiction
  services 6, night shelters 3; toilets excluded); **3** have a matching OSM object. Liberecký kraj: 31 core
  places (16 addiction services), 2 matched. Ostrava: 5 core places.
- **Caveats:** freshness is unknown (no update dates; a "COVID opatření" category still exists), so every
  record needs a check before import, better as a survey list than a bulk import. Some food points are street
  distributions at a square (Food not bombs, "Muslimové rozdávají jídlo"); map only fixed facilities.
  Skip category `nasili` (Oběti násilí): shelter locations for violence survivors are deliberately hidden.
  Skip category `wc` (IPR Praha, CC BY-SA 4.0, already covered by `prague-verejne-toalety.md`).
- **Stable id:** numeric `id` and a slug `url` per place.
- **Contact:** praha@mapabezdomova.cz (volunteer team) for consent; the original women's service map
  belongs to Jako doma, o.p.s.
- **Rejected in the same theme:** Česká federace potravinových bank (food banks are warehouses supplying
  NGOs, 3 social_facility=food_bank in OSM, few points); Prague winter help lists on district sites (PDF
  articles, no data); mamikam.cz and baby-friendly.cz (commercial listings of family-friendly cafés and
  play corners, no licence, not NGO data).
- Wiki pages read: Tag:amenity=social_facility, Key:social_facility, Tag:social_facility=soup_kitchen,
  Tag:amenity=shower, Tag:amenity=food_sharing.

## Wiki entry
```
===Mapa bez domova – služby pro lidi bez domova===
* dataset: databáze služeb mapabezdomova.cz (Praha, Ostrava, Liberecký kraj)
* gestor: [https://mapabezdomova.cz/ Mapa bez domova (dobrovolnický projekt, KRISA)]
* licence: neuvedena, nutno vyjednat (praha@mapabezdomova.cz)
* datové primitivy: body
* odkaz: https://www.mapabezdomova.cz/service/find/praha?category=all
* navržený tag {{tag|amenity|social_facility}} + {{tag|social_facility|soup_kitchen}} / {{tag|social_facility|shelter}} + {{tag|social_facility:for|homeless}}, {{tag|amenity|shower}}, {{tag|ref:mapabezdomova|<id>}}
* poznámka: v Praze 96 míst s jídlem, hygienou, noclehem či zdravotní pomocí; v OSM odpovídající objekt jen u 3
```
