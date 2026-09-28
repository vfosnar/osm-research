# ZnakoMapa – místa se službou v českém znakovém jazyce (Znakovárna)

| Field | Value |
|---|---|
| publisher | Znakovárna, z.s. (Mapotic map id 8162, `owner_name` in the map metadata; web https://www.znakovarna.cz/znakomapa/, map https://znakomapa.mapotic.com/) |
| url | https://www.mapotic.com/api/v1/maps/8162/pois.geojson/ (metadata: https://www.mapotic.com/api/v1/maps/8162/) |
| format | GeoJSON FeatureCollection (Mapotic API, no key needed), 226 kB |
| coords | yes (WGS84 points) |
| records | 478 POIs (fetched 2026-09-28): Video průvodce 251, Služby a organizace 140, Vzdělávání a volný čas 41, Restaurace, kavárna 19, Zpřístupnění pro neslyšící 17, Ubytování, hotely 3, Instituce a úřady 3, Tichá linka 3, Akce 1. Inside the CZ bbox: 144 video guides and 201 service points (26 service points are abroad) |
| osm_tags | no established tag. Proposal: deaf=yes + deaf:description=* on the existing object (wiki Key:deaf: status "in use" but marked {{Undocumented tag}}); alternative language:cse=yes (wiki Key:language:*) |
| osm_count_cz | deaf 1 (value yes), deaf:description 0, hearing_loop 1 (Geofabrik taginfo, data until 2026-09-27). Sample of 40 CZ service points against the OSM API (2026-09-28): 8 have an existing OSM object to attach the tag to |
| license | none published for the map data; Mapotic terms (https://www.mapotic.com/terms/) give other users no rights to content |
| license_url | https://www.mapotic.com/terms/ |
| license_status | unclear |
| update_freq | continuous, entries added by the owner on request (map homepage text); last_update 2026: 444 POIs, 2025: 7, 2024: 24, 2023: 3 |
| impact | 2 |
| sync_fit | MapRoulette (no established tag; needs matching to existing OSM object) |
| verified | yes |

## Try it
- **Map preview:** none (licence unclear). Web map: https://znakomapa.mapotic.com/ (also linked from https://www.znakovarna.cz/znakomapa/).
- **QGIS:** *Layer → Add Layer → Add Vector Layer*, source type *Protocol: HTTP(S)*, type *GeoJSON*, URI `https://www.mapotic.com/api/v1/maps/8162/pois.geojson/` (tested 2026-09-28: FeatureCollection of 478 points). Filter the service points with `"category" <> 21051` (21051 = Video průvodce).

## Notes
- **What the map is:** the homepage text says it lists services, firms, organisations, institutions and schools "zprostředkovány v českém znakovém jazyce", made by the community centre Znakovárna, z.s. The anonymous GeoJSON has only `id`, `name`, `slug`, `category`, `category_name`, `last_update`; the per-POI detail endpoint (`/api/v1/maps/8162/pois/715925/`) returns 401, so descriptions, websites and addresses are not available without an agreement.
- **Categories (all 478):**
  - *Video průvodce* (251; English label "Průvodce v ČZJ"; 144 in the CZ bbox): sign-language video guides to sights, mostly in central Prague (Staroměstská radnice, Katedrála sv. Víta, Tančící dům, Kampa, mills, churches, fountains). These describe a sight, they are not a service at it.
  - *Služby a organizace* (140): deaf associations and their branches (Česká unie neslyšících and its branches, Tichý svět – kontaktní místo in 13 towns, Centrum pro neslyšící a nedoslýchavé, Svaz neslyšících a nedoslýchavých osob, Centra pro zdravotně postižené), interpreter and transcription services (Česká komora tlumočníků znakového jazyka, Transkript online), early-care services, and small businesses run by or serving deaf people (tyre service Pneu Procházka, shoe repair, carpenters, hairdresser, optician Optika Novotný, driving school Autoškola pro neslyšící, accountant, doctor MUDr. Klára Cais Kučerová, lawyer JUDr. Dan Zwieb).
  - *Vzdělávání a volný čas* (41): schools for hearing-impaired pupils (Holečkova and Výmolova Praha, Ječná, Gellnerka Brno, Hradec Králové, Olomouc, Plzeň, Liberec, Valašské Meziříčí), speciálně pedagogická centra, sign-language courses and centres (Pevnost, Trojrozměr, Evoluce), university units (Ústav jazyků a komunikace neslyšících FF UK, JAMU), deaf sports clubs.
  - *Zpřístupnění pro neslyšící* (17): museums and sights with sign-language tours or guides (Národní muzeum, Uměleckoprůmyslové museum, Muzeum Karla Zemana, Technické muzeum v Brně, Památník Terezín, Státní zámek Lednice, Muzeum loutkářských kultur Chrudim), plus a T-Mobile shop.
  - *Restaurace, kavárna* (19): only 3 in Czechia (Tichá kavárna, Tichá cukrárna, Restaurace Na Staré); the rest are deaf-run cafés abroad (Rome, Paris, London, Washington, Tokyo).
  - *Tichá linka* (3): Úřad práce ČR offices in Prague with a sign-language line. *Instituce a úřady* (3): TV programmes and Nová radnice Prahy 12. *Ubytování* (3), *Akce* (1, Winter Deaflympics 2027).
- **Gap (40 randomly sampled CZ service points, OSM API map call per point, 2026-09-28; Postpass returned 503):**
  - **8 of 40 (20 %) have an OSM object to attach a tag to.** 6 match directly by name: Muzeum Karla Zemana (tourism=museum), Uměleckoprůmyslové muzeum (tourism=museum), Tichá kavárna (amenity=cafe), Pneu Procházka Čakovice (shop=car_repair), Tichý svět Pardubice (amenity=social_centre), SŠ/ZŠ/MŠ pro sluchově postižené Holečkova (amenity=school). 2 are speciálně pedagogická centra housed in a school that is in OSM (Ječná, Ostrava-Poruba). For Gellnerka Brno only the school canteen is in OSM.
  - **18 of 40 are real premises missing from OSM:** association offices and contact points (Plzeňská unie neslyšících, Tichý svět Brno and Kladno, Česká unie neslyšících Liberec, Centrum pro neslyšící a nedoslýchavé Beroun and Vysočina, Centra pro zdravotně postižené Jablonec and Semily, Česká komora tlumočníků znakového jazyka, VIA, Evoluce), university units, an Úřad práce office, a driving school, a shop, a holiday cottage. No object with a matching name within about 200 m. These would be new office=association / social_facility objects, which the anonymous point data alone is too thin to create.
  - **13 of 40 are not mappable places:** online or mobile services, programmes and media (Zdravá prsa pro neslyšící, Znakovka do škol, Tiché zprávy, Zprávy v českém znakovém jazyce, Deaf Friendly certification, Hands Dance), and sole traders located at a home address. The 40th, Gellnerka Brno, is the partial match above.
  - Scaled to the 201 CZ service points: roughly 40 existing OSM objects could get a sign-language tag, roughly 90 organisations are missing from OSM.
- **Tagging (needs community agreement first):**
  - Key:deaf (raw wiki text read 2026-09-28): status "in use", marked {{Undocumented tag}}, description "Indicates whether a feature supports accessibility for people with hearing impairments". It does not say whether that means sign-language staff, an induction loop, subtitles or visual announcements. Worldwide taginfo: deaf=yes 3,179, limited 12, no 4, partial 2, designated 1; about 3,150 of the deaf=yes uses are on public-transport route relations carrying payment:troika / payment:podorozhnik (Russian transit routes), so the dominant meaning in the data is vehicle accessibility, not sign language.
  - How others describe it: deaf:description 80 (German "Optischer Aufruf vorhanden", "DGS wird gesprochen", one French "Personnel qui parle la LSF"), deaf:description:fr 281 (mostly ATMs with an audio jack and induction loops), deaf:description:en 50 (one says "The staff is able to communicate using the Czech Sign Language"). Other keys in use: access:deaf 62, special_needs:deaf 46, hearing_loop 843, deaf:gebaerdendolmetcher 1. The wiki page Disabilities (section Hearing impaired/deafness → Tagging) lists "Sign language translation" as a need with no tag.
  - Language keys: Key:language:* is "in use" for languages offered at a POI and has service sub-keys (language:physicians:cs 3, language:waiters:cs 5, language:guides:cs 20). The wiki tells mappers to use ISO 639-1/639-2 codes, but sign languages only have ISO 639-3 codes; a few are already used that way: language:vgt 3, language:ase 2, language:gsg 2, language:sgn 2, language:asl 1, language:fsl 1, language:rsl 1, language:sgn-GB 1. Czech Sign Language is ISO 639-3 `cse`; language:cse is not used. No sign_language* key exists besides name:sign_language (2).
  - Options for the Czech community to choose from, then document on the wiki: (a) deaf=yes + deaf:description=„Personál komunikuje v českém znakovém jazyce“, which fits existing usage but stays vague; (b) language:cse=yes, which is precise and follows Key:language:*, but stretches that page's code rule; (c) both. For museums and castles offering sign-language tours, language:guides:cse=yes would follow the existing language:guides:* pattern. Suggested reference key: ref:znakomapa=<Mapotic id>.
  - **Video guides:** no OSM tag fits. They are videos about a sight, not a feature of it; the anonymous data does not even include the video URL (detail endpoint 401). A sight could at most link a video through a website-style key, which would misuse those keys. Leave them out of OSM.
- **Not known upstream:** no match for "znakov", "neslyš" or "deaf" on Cs:Česko/freemap, Cs:Zdroje_v_jednani or in Sync config.toml; OSM wiki full-text search for "znakomapa" returns nothing (checked 2026-09-28).
- **Licence / contact:** Znakovárna, z.s., https://www.znakovarna.cz/znakomapa/, info@znakovarna.cz (site). The map homepage names honza.wirth@znakovarna.cz for new entries. Ask for consent to use the names and positions, ideally with the attributes behind the detail endpoint. The data volume is small; what it mainly adds is a trusted list of places for a need OSM has no tag for yet.

## Wiki entry
```
===ZnakoMapa===
* dataset: ZnakoMapa – mapa pro neslyšící (mapa Mapotic)
* gestor: [https://www.znakovarna.cz/znakomapa/ Znakovárna, z.s.]
* licence: neuvedena, nutné vyžádat souhlas
* datové primitivy: body
* odkaz: https://www.mapotic.com/api/v1/maps/8162/pois.geojson/
* navržený tag {{tag|deaf|yes}} + {{tag|deaf:description|Personál komunikuje v českém znakovém jazyce}} nebo {{tag|language:cse|yes}} (nutná dohoda komunity), {{tag|ref:znakomapa|<id>}}
* poznámka: 201 míst v Česku, kde se neslyšící domluví v českém znakovém jazyce; OSM pro to nemá ustálený tag (deaf=* je v Česku použit jednou) a asi 90 spolků a poraden v OSM chybí úplně
```
