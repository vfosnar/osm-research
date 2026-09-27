```
name: Seznam železničních přejezdů na síti Správy železnic (list of level crossings)
publisher: Správa železnic, státní organizace (IČO 70994234)
url: https://www.spravazeleznic.cz/documents/50004227/50164276/Seznam+%C5%BEelezni%C4%8Dn%C3%ADch+p%C5%99ejezd%C5%AF+na+s%C3%ADti+Spr%C3%A1vy+%C5%BEeleznic+k+31.12.2025/819364a0-0709-4bf0-8db8-59fd2591ff7a (linked from https://www.spravazeleznic.cz/bezpecna-zeleznice/bezpecnost-na-prejezdech/seznam-prejezdu)
format: XLSX (one sheet "zdrojová data"; the file is named "...k 31.12.2025.xlsx")
coords: yes (WGS84 in DMS strings, for example 50° 05' 25.95927'' N)
records: 7,464 crossings (file dated 31 Dec 2025)
osm_tags: railway=level_crossing + ref=P<number>, crossing:barrier=*, crossing:light=*, crossing:bell=*, railway:position=<km>
osm_count_cz: railway=level_crossing 16,686 nodes (taginfo, 2026-09-26). In the CZ bbox, 7,760 distinct ref=P<n> values are present (Postpass, 2026-09-27)
license: none stated. The file is published on the SŽ website with no terms of use. The related INSPIRE metadata record CZ-SZCZ-PREJEZD says "Data na vyžádání u správce" (data on request from the administrator)
license_url: https://geoportal.gov.cz/php/micka/record/basic/4d6de208-9080-4488-9863-6e63c0a80138
license_status: unclear
update_freq: about yearly (earlier editions: 27 Jan 2020, 31 Dec 2025)
impact: 2
verified: yes
```

## Notes
- **Columns:** Identifikace přejezdu (P-number, unique and stable, the number that is shown on the crossing sign for IZS), TÚ přejezdu (line section), Evidenční km poloha, Zabezpečení přejezdu, Krajský úřad, Oblastní ředitelství, Třída komunikace, Zeměpisná šířka, Zeměpisná délka.
- **Protection type (Zabezpečení) counts:**
  - N (cross only): 3,142
  - S without barriers: 2,084
  - S with barriers: 2,024
  - M (mechanical): 214
  - These map to crossing:barrier, crossing:light and crossing:bell (plus crossing=uncontrolled for N).
- **Gap analysis (Postpass, CZ bbox, matched on ref):**
  - 7,144 of 7,465 SŽ crossings already exist in OSM with the same ref=P…. The positional agreement is very close: median distance 1.0 m, 90th percentile 3.1 m. The data were almost certainly imported or copied earlier.
  - 321 SŽ crossings are not in OSM by ref. Only 4 of them have an unreferenced OSM crossing within 40 m, so most are really missing or sit on unmapped track.
  - 616 OSM P-refs are no longer in the SŽ list. These are cancelled crossings or crossings on non-SŽ track such as sidings or private lines, and are useful for cleanup.
  - The main remaining value is maintenance: new and removed crossings, and a check of protection-type attributes against the current file. That is why impact is 2.
- **Tagging:**
  - Tag:railway=level_crossing (EN) lists crossing:barrier/light/bell/activation and railway:position. Cs:Tag:railway=level_crossing (template Cs:Railway Crossing Common) suggests crossing_ref for the crossing number.
  - In CZ practice, the P-number is in `ref` (about 9,199 level_crossing nodes carry ref). crossing_ref in CZ holds zebra/pelican values, so keep using `ref=P…`. The wiki (Cs) and practice disagree on this point, and it should be raised on talk-cz.
- **Licence:** SŽ is a state organisation, but it does not publish the list in NKOD and gives no licence. Ask SŽ (GŘ, odbor Správa železniční geodézie, geoportal.spravazeleznic.cz) for explicit consent or a CC0/NKOD release. The old metadata contact was ludek.paznocht@tudc.cz / BrozL@spravazeleznic.cz. §3 AZ úřední dílo does not obviously apply, because this is not a legal document.
- **Suggested key:** existing `ref` (P-number). No new ref:* key is needed.

## Wiki entry
```
===Seznam železničních přejezdů (Správa železnic)===
* dataset: Seznam železničních přejezdů na síti Správy železnic (XLSX, stav k 31. 12. 2025)
* gestor: [https://www.spravazeleznic.cz/ Správa železnic, státní organizace]
* licence: neuvedena, nutno vyžádat souhlas [https://www.spravazeleznic.cz/bezpecna-zeleznice/bezpecnost-na-prejezdech/seznam-prejezdu]
* datové primitivy: body
* odkaz: https://www.spravazeleznic.cz/bezpecna-zeleznice/bezpecnost-na-prejezdech/seznam-prejezdu
* navržený tag {{tag|railway|level_crossing}}, {{tag|ref|P<číslo>}}, {{tag|crossing:barrier}}, {{tag|crossing:light}}
* poznámka: 7 144 ze 7 465 přejezdů už v OSM je s ref=P…, zbývá ~320 chybějících a ~600 zrušených/neplatných ref – vhodné pro údržbu
```
