# Centrálny register AED (OS ZZS SR) – verejná mapa defibrilátorov

| Field | Value |
|---|---|
| publisher | Operačné stredisko záchrannej zdravotnej služby SR (OS ZZS SR), IČO 36076643, state organisation of the Ministry of Health |
| url | list: https://aed.155.sk/api/landingPage/aedMap/getAedList ; detail: https://aed.155.sk/api/landingPage/aedMap/getAedDetail?id=&lt;id&gt; (public JSON behind the map https://aed.155.sk/#map , linked from https://155.sk/mapa-aed/) |
| format | JSON array (no auth); detail endpoint returns one JSON object per device |
| coords | yes (WGS84 `lat`/`lng` on every record) |
| records | 5,069 published AEDs (4,792 `ready`, 277 `notReady`) on 30 Sep 2026; by region id 7: 789, 1: 762, 5: 687, 3: 638, 8: 615, 6: 591, 2: 498, 4: 489 |
| osm_tags | emergency=defibrillator, defibrillator:location=&lt;location&gt;, opening_hours, operator=&lt;holderName&gt;, access (checked on Tag:emergency=defibrillator) |
| osm_count_sk | emergency=defibrillator 658 nodes (taginfo europe:slovakia, data until 2026-09-29) |
| license | none stated; the map exists because §3 k) of Act 579/2004 obliges OS ZZS SR to publish where AEDs are |
| license_url | https://155.sk/wp-content/uploads/2026/02/Podmienky-registracie-AED.pdf (registration terms, section 6 "Zverejnenie AED") |
| license_status | unclear |
| update_freq | continuous (owners register and update devices in the aed.155.sk form; status changes automatically when electrodes, batteries or consents expire) |
| impact | 5 |
| sync_fit | Sync (points, stable numeric `id`, category maps 1:1 to emergency=defibrillator; availability hours and location text fit update keys) |
| verified | yes |

## Try it
- **Map preview:** no sample, because no licence is stated (`unclear`).
- **QGIS:** the list is a plain JSON array, not GeoJSON. Convert it in one line, then open `aed.geojson` with *Layer → Add Layer → Add Vector Layer*:
  `curl -s https://aed.155.sk/api/landingPage/aedMap/getAedList | jq '{type:"FeatureCollection",features:[.[]|{type:"Feature",geometry:{type:"Point",coordinates:[.lng,.lat]},properties:.}]}' > aed.geojson`
  (tested 30 Sep 2026: 5,069 features, EPSG:4326).
- **Web:** https://aed.155.sk/#map

## Notes
- Known (osm_sk thread "Verejne prístupné defibrilátory (AED)", `4CTh6o6LbsM`, 2020–2025; licence never resolved, no import) — adds: a live JSON API with a stable ID per device, 6.5× more devices than the 778 mentioned in the thread in May 2024 (the 2024 thread used a Google My Maps KML and a hand-made ODS table), and structured availability hours and location text. It is not on `WikiProject Slovakia/Sources` and not in the known-sources baseline.
- List fields: `id` (stable integer), `holderName`, `state` (`ready`/`notReady`), `regionId`, `street`, `registryNumber`, `orientationNumber`, `city`, `district`, `postalCode`, `lat`, `lng`. Detail fields: `location` (free text such as "na budove obecného úradu pri vchode"), `availabilityType` (`Nepretržite`, `Prevádzkové dni`, `Prevádzkové mesiace`), `availabilityHours` (such as `Po-Ne, 00:00-24:00` or `Po 08:00-12:00,12:30-15:30;St 08:00-12:00,12:30-16:30;Pi 08:00-11:30`), `unavailableOnHolidays`, `manufacturerName`, `manufacturerModelName`, `documentIds` (photos via `getAedImage`).
- In a random sample of 60 details, all 60 had `location` and a manufacturer, and 36 were available 24/7 (`Nepretržite`). The day/time strings use Slovak day abbreviations and convert to `opening_hours` mechanically (Po=Mo, Ut=Tu, St=We, Št=Th, Pi=Fr, So=Sa, Ne=Su).
- Holders: municipalities dominate (1,349 "Obec …", 182 "Mesto …"), then 326 volunteer fire brigades, 168 more fire-brigade holders, schools, and 82 Tesco stores. Since 1 January 2025 every municipality over 500 inhabitants must keep a public AED and register it (§3 ods. 5 of Act 369/1990 as quoted in the registration terms), so the dataset keeps growing.
- Gap (Postpass, 30 Sep 2026): 49 of 400 randomly sampled AEDs have an OSM `emergency=defibrillator` within 100 m (12 %). That puts roughly 4,400 AEDs missing from OSM.
- Caveats: a 2024 osm_sk post said positions are often 20 m off and some AEDs are in vehicles; filter `state=ready` and review positions against imagery or the `location` text. Do not import photos (some are Street View screenshots, per the same thread). The public map shows only devices whose owner agreed to publication, and only non-personal fields (terms, section 6).
- Licence: the terms say published data is "anonymised" and the map exists to raise public awareness, but give no reuse licence. Košický kraj republished the Košice-region AEDs on its Geoportál KSK "with the consent" of OS ZZS SR (SITA, 2025), so OS ZZS SR does grant reuse on request. Needs explicit consent for OSM.
- Suggested ref: `ref:oszzs=<id>` (agree the key in osm_sk first). `operator` from `holderName` only for organisations; keep `defibrillator:location` in Slovak.
- ZBGIS: no AED object type in the ZBGIS catalogue (KTO checked 30 Sep 2026).
- Wiki pages read: Tag:emergency=defibrillator.
- Contact: OS ZZS SR, Trnavská cesta 8/A, Bratislava (AED register team, https://155.sk/automaticky-externy-defibrilator-aed/).

## Wiki entry
```
=== Centrálny register AED (OS ZZS SR) ===
* dataset: Verejná mapa automatických externých defibrilátorov
* správca: [https://155.sk/ Operačné stredisko záchrannej zdravotnej služby SR]
* licencia: neuvedená – potrebný súhlas [https://155.sk/wp-content/uploads/2026/02/Podmienky-registracie-AED.pdf]
* dátové primitívy: body
* odkaz: https://aed.155.sk/api/landingPage/aedMap/getAedList
* navrhované značky: {{tag|emergency|defibrillator}}, {{tag|defibrillator:location|<umiestnenie>}}, {{tag|opening_hours|24/7}}, {{tag|ref:oszzs|<id>}}
* poznámka: Register zverejňuje 5 069 AED so súradnicami a stálym ID, v OSM je 658 defibrilátorov a v náhodnej vzorke má náprotivok v OSM len 12 %.
```
