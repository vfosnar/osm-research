# VLS ČR – body záchrany (kontaktní místa IZS) in military training areas

| Field | Value |
|---|---|
| publisher | Vojenské lesy a statky ČR, s.p. (VLS), Pod Juliskou 1621/5, Praha 6; maps made with the Army and HZS. CSV transcription by OSM contributor martin-kokos (talk-cz, 2024-04-09) |
| url | source PDFs: https://www.vls.cz/cs/nase-cinnosti/zachranny-system (16 maps `https://www.vls.cz/media/downloadables/mapy_IZS_*.pdf`, one per division/detached area, map sheets dated 2014, files last-modified 2015-08-03). OCR'd CSV: https://lists.openstreetmap.org/pipermail/talk-cz/attachments/20240409/4ad882a6/attachment.csv |
| format | PDF maps with DMS coordinate tables (15 have a text layer; Mimoň–Ralsko is image-only); CSV (columns ref, DMS parts, name, y = lat, x = lon) |
| coords | yes (WGS84 DMS on the signs and maps) |
| records | 484 points in the CSV (457 with a local name); some marked on the maps as water-draw points ("s možností čerpání vody") |
| osm_tags | highway=emergency_access_point + ref=&lt;number on sign&gt; + name=&lt;local name&gt; + operator=VLS ČR, s.p. + operator:wikidata=Q11863366 + emergency_telephone_code=112 (wiki Cs:Tag:highway=emergency_access_point, which uses a VLS sign as its example). Water points: emergency=suction_point (wiki Tag:emergency=suction_point) |
| osm_count_cz | highway=emergency_access_point 1,920, emergency=access_point 284, operator:wikidata=Q11863366 167 (taginfo 2026-09-28). Local match against the 2026-09-27 Czechia extract: 260 of 484 VLS points have an emergency access point within 150 m (252 with the same ref); **224 missing** |
| license | none stated ("© Vojenské lesy a statky ČR, s.p." in the site footer); the CSV is a volunteer transcription of the PDFs, no licence |
| license_url | – |
| license_status | unclear |
| update_freq | none visible (maps from 2014; the signs carry the same number, coordinates and name) |
| impact | 3 |
| verified | yes |

## Try it
- **Map preview:** no sample, because the licence is `unclear`.
- **QGIS:** *Layer → Add Layer → Add Vector Layer*, source type *File*, paste
  `/vsicurl/https://lists.openstreetmap.org/pipermail/talk-cz/attachments/20240409/4ad882a6/attachment.csv`,
  and under *Options* set `X_POSSIBLE_NAMES=x`, `Y_POSSIBLE_NAMES=y`; the layer is EPSG:4326. (The URL
  was fetched and returns `text/csv`, 484 rows plus header.)
- **Source maps:** open any PDF on https://www.vls.cz/cs/nase-cinnosti/zachranny-system, such as
  https://www.vls.cz/media/downloadables/mapy_IZS_Karlovy_Vary_Hradiste.pdf.

## Notes
- **Status of the lead:** the LČR body záchrany were imported in 2019 (consent recorded on
  Cs:Zdroje_v_jednani) and are maintained through RichMar's tool (https://richmar.github.io/BZ). The VLS
  points were never added to that tool. In the talk-cz thread "Body záchrany Lesy ČR" (April–June 2024)
  VladaC asked for them, martin-kokos posted the OCR'd CSV, and Spratek (the tool's author) asked what
  licence the data has. Nobody answered and nothing was imported. The VLS points already in OSM were
  added one by one by mappers (the thread mentions photographing the signs for Fody).
- **Gap per area (local match, 150 m):** Libavá 15 of 87 in OSM, Březina 8 of 75, Hradiště 23 of 60;
  Brdy 48/48, Boletice 64/65 and Ralsko 53/54 are already done. The 224 missing points are mostly in the
  three active training areas (Libavá, Březina, Hradiště), where public access is restricted and survey
  is hard, so the data is the practical route.
- **Operator values** on the 260 matched OSM points are inconsistent (12 variants: "VLS ČR, s.p." 166,
  none 44, "VLS ČR" 12, "VLS" 12, "Vojenské lesy a statky ČR" 8 …). A conflation would also normalise them
  to the wiki's example `operator=VLS ČR, s.p.` + `operator:wikidata=Q11863366`.
- **ref is not unique:** numbering restarts at 1 in each division (Libavá also uses V1–V26), so a sync key
  needs the area: suggest `ref` as on the sign plus matching by position; no national ID exists.
- **Caveats:** the CSV is an OCR of 2014 maps. It was checked by hand, but a few coordinates could be
  wrong and some signs may have moved. The 252 ref matches suggest the transcription is good.
- **Licence:** the PDFs are published by a state enterprise for public safety, but there is no licence
  text. The points themselves are facts printed on public signs, so survey mapping is fine. A bulk import
  from the PDFs needs consent. Contact VLS (https://www.vls.cz/cs/kontakty, the divisions Lipník nad
  Bečvou, Plumlov and Karlovy Vary manage the missing areas).
- Wiki pages read: Cs:Tag:highway=emergency_access_point, Tag:emergency=suction_point.

## Wiki entry
```
===VLS ČR – body záchrany ve vojenských újezdech===
* dataset: Záchranný systém – mapy IZS (kontaktní místa IZS)
* gestor: [https://www.vls.cz/cs/nase-cinnosti/zachranny-system Vojenské lesy a statky ČR, s.p.]
* licence: neuvedena, nutný souhlas VLS ČR
* datové primitivy: body
* odkaz: https://www.vls.cz/cs/nase-cinnosti/zachranny-system (PDF); CSV přepis https://lists.openstreetmap.org/pipermail/talk-cz/attachments/20240409/4ad882a6/attachment.csv
* navržený tag {{tag|highway|emergency_access_point}}, {{tag|ref|<číslo na ceduli>}}, {{tag|operator|VLS ČR, s.p.}}, {{tag|operator:wikidata|Q11863366}}
* poznámka: z 484 bodů VLS je v OSM 260; chybí 224, hlavně v újezdech Libavá (15 z 87), Březina (8 z 75) a Hradiště (23 z 60)
```
