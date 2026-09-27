# Rejstřík sportu – Seznam sportovních zařízení (public part)

| Field | Value |
|---|---|
| publisher | Národní sportovní agentura (NSA) |
| url | https://rejstriksportu.cz/dashboard/public/agenda/sportoviste (JSON API: POST https://rejstriksportu.cz/api/NxWebAgendaEREJPublicSportoviste/List, metadata GET .../ListMetadata) |
| format | JSON via undocumented SPA API (UI offers download from grid) |
| coords | address-only (obec, ulice, č.p., č.o., část obce, PSČ; no RÚIAN code, no coordinates in the public list) |
| records | 11,747 (totalCount reported by API, 2026-09-27) |
| osm_tags | leisure=sports_centre / leisure=pitch / leisure=stadium / leisure=sports_hall / leisure=swimming_pool + sport=* |
| osm_count_cz | leisure=pitch 33,252; leisure=sports_centre 3,046 |
| license | not stated (no NKOD record, no terms on rejstriksportu.cz found) |
| license_url | n/a |
| license_status | unclear |
| update_freq | continuous (registry maintained by sports organisations) |
| impact | 2 |
| verified | partial |

## Try it
- **Map preview:** no sample, for two reasons: the licence is `unclear` and the source has addresses only.
- **QGIS:** there is nothing to load as a layer. The data is available only through the web app grid or its undocumented JSON API.
- **Web:** https://rejstriksportu.cz/dashboard/public/agenda/sportoviste

## Notes
- Confirmed that the public API returns totalCount 11,747 with fields id (GUID), nazev, typ (the returned item had "letiště pro sportovní létání"), obec, ulice, cisloDomovni, cisloOrientacni, castObce, psc, okres, kraj. I could not work out the paging parameters (the API returned only 1 item for every combination I tried), so I have not verified the full type breakdown.
- Legal basis: zákon 115/2001 Sb. o podpoře sportu (§3e public part of the registry). No reuse license is published. Ask NSA to publish on NKOD under CC0, or for explicit consent.
- Value: OSM already has 33k pitches and 3k sports centres. The registry contains only facilities registered by organisations applying for subsidies, with text addresses only and no geometry. Its main use is names and operators for existing features, and a QA list for missing sports halls or swimming pools. Low priority.
- Wiki pages to read before tagging: Tag:leisure=sports_centre (read), Key:sport.
- Contact: info@agenturasport.cz (from nsa.gov.cz/rejstrik/).
- Municipal "Sportoviště" datasets (Ostrava, CC BY 4.0, JTSK GeoJSON; Huntířov) are local only.

## Wiki entry
```
===Rejstřík sportu – sportovní zařízení===
* dataset: Seznam sportovních zařízení (veřejná část)
* gestor: [https://www.agenturasport.cz/ Národní sportovní agentura]
* licence: neuvedena
* datové primitivy: body (pouze adresy)
* odkaz: https://rejstriksportu.cz/dashboard/public/agenda/sportoviste
* navržený tag {{tag|leisure|sports_centre}}, {{tag|leisure|pitch}} + {{tag|sport}}
* poznámka: 11 747 zařízení; licenci je třeba vyjednat
```
