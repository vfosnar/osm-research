# ŘLP ČR VFR příručka – HEMS heliports, LZS landing sites, SLZ (ultralight) fields, drop zones

| Field | Value |
|---|---|
| publisher | Řízení letového provozu ČR, s. p. (Air Navigation Services of the CR), AIM centre, aim@ans.cz |
| url | https://aim.rlp.cz/vfrmanual/actual/hel_1_cz.html (heliports + LZS sites of public interest); https://aim.rlp.cz/vfrmanual/actual/ad_1_cz.html (index of aerodromes and SLZ fields, one page per site at `…/actual/<code>_text_cz.html`, such as https://aim.rlp.cz/vfrmanual/actual/lkbole_text_cz.html) |
| format | HTML (tables and per-site pages); PDF print version. The AIXM 5.1 datasets on the AIM "Data Sets" page cover only obstacles and terrain, on request |
| coords | yes (DMS; ARP for aerodromes/SLZ, TLOF/centre for heliports) |
| records | edition WEF 17 SEP 26: 74 heliports (12 non-public, 62 for the air rescue service, 4-letter LKxx codes); 65 "místa veřejného zájmu pro LZS" (PC2 sites, LK002–LK0xx, with elevation); from the 223 per-site pages fetched: 82 aerodromes, 69 SLZ fields (6-letter LKxxxx codes, RWY direction and size, radio frequency, operator contact); 48 sites list "výsadková činnost" (parachuting) |
| osm_tags | heliport: aeroway=heliport (whole facility) or aeroway=helipad (pad), icao=&lt;code&gt;, ele, operator; wiki Tag:aeroway=heliport, Tag:aeroway=helipad (emergency landing sites are emergency=landing_site). SLZ: aeroway=aerodrome (or aeroway=airstrip) + icao (wiki Tag:aeroway=aerodrome: "issued by the ICAO, or the national Civil Aviation Authority"). Drop zones: sport=parachuting |
| osm_count_cz | aeroway=aerodrome 241, airstrip 44, helipad 366, heliport 2, sport=parachuting 2, key icao 106 (taginfo CZ 2026-09-28). See the gap table in the notes (local match against the 2026-09-27 Czechia extract) |
| license | none. The aim.rlp.cz Terms of Use (15 May 2012) allow personal use only and prohibit "to provide contents of the Website or any part of it as part of another product/service, commercial or noncommercial, without prior consent of the Operator" |
| license_url | https://aim.rlp.cz/?lang=en&p=terms-of-use |
| license_status | incompatible (without consent from ŘLP ČR) |
| update_freq | AIRAC cycle (28 days) |
| impact | 2 |
| sync_fit | MapRoulette (heliport vs SLZ vs drop-zone classification needs judgement) |
| verified | yes |

## Try it
- **Map preview:** none, because the terms forbid reuse.
- **QGIS:** no machine-readable service. The heliport and LZS tables parse to CSV (tested: 74 heliports +
  65 LZS sites). Load the CSV with *Layer → Add Layer → Add Delimited Text Layer*, X `lon`, Y `lat`,
  EPSG:4326:
  ```
  python3 - <<'E'
  import re,html,csv,urllib.request
  s=urllib.request.urlopen('https://aim.rlp.cz/vfrmanual/actual/hel_1_cz.html').read().decode()
  t=re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',s)))
  w=csv.writer(open('heliporty.csv','w',newline='')); w.writerow(['code','name','lat','lon'])
  for m in re.finditer(r'(LK[A-Z]{2}|LK\d{3}) (.+?) (\d\d) (\d\d) ([\d,]+) N 0?(\d+) (\d\d) ([\d,]+) E',t):
      g=[float(x.replace(',','.')) for x in m.groups()[2:]]
      w.writerow([m.group(1),m.group(2),round(g[0]+g[1]/60+g[2]/3600,6),round(g[3]+g[4]/60+g[5]/3600,6)])
  E
  ```
- **Web:** https://aim.rlp.cz/vfrmanual/actual/hel_1_cz.html

## Notes
- **Gap:** local match against the 2026-09-27 Czechia extract (aerodromes and SLZ within 1.5 km of an
  aeroway=aerodrome/airstrip; heliports within 150 m of an aeroway=helipad/heliport; code = the
  code in `icao`/`ref` anywhere in the extract):

  | Class | In VFR příručka | OSM feature nearby | OSM carries the code |
  |---|---|---|---|
  | Aerodromes | 82 | 78 | 82 |
  | SLZ fields | 69 | 68 | 0 |
  | HEMS heliports | 60 (with pages) | 58 | 15 |
  | Other heliports | 12 | 12 | 4 |
  | LZS PC2 sites | 65 | 49 | 2 |
  | Parachuting sites | 48 | – | 2 × sport=parachuting in all of CZ |

- **Assessment:** the geometry is already in OSM. Czech mappers have drawn nearly every airfield, SLZ
  strip and hospital helipad. What is missing are attributes: the LKxxxx codes of the SLZ fields and
  most HEMS heliports, `aeroway=heliport` (2 in CZ against 74 official heliports; the HEMS bases are
  mapped as bare helipads), runway size and orientation, and `sport=parachuting` for 48 drop zones.
  Missing LZS sites: 16 of 65 have no helipad within 150 m (Brno Mendlovo nám., Rumburk, Rychnov n. K.,
  Tanvald, Ústí nad Orlicí, Volyně and others). Some of these are ad-hoc landing spots in HZS
  (fire-brigade) yards or car parks, which fit emergency=landing_site better than aeroway=helipad.
- **Why only impact 2:** a few hundred attribute edits, which a mapper could do by hand once permission
  exists. The 6-letter SLZ codes are the useful part: the VFR příručka defines them as the identifiers of SLZ
  fields (not usable in flight plans), so they suit `icao` (taginfo CZ already has one 6-letter value, LKCBVR).
- **Licence:** the terms of use make the data unusable as a source without prior written consent. The
  underlying registers belong to ÚCL (Evidence letišť, a PDF with no coordinates:
  https://www.caa.gov.cz/wp-content/uploads/2026/05/Evidence-letist_20_05_2026.pdf) and LAA ČR (register
  of SLZ fields; the LAA web page https://www.laacr.cz/provozni-informace/plochy-slz/ only links to the
  VFR příručka). Contact for consent: ŘLP ČR AIM, aim@ans.cz. Alternatively ask LAA ČR (Ke Kablu 289,
  Praha 10) for its own SLZ register, which also covers fields not published in the VFR příručka
  ("VFR příručka ČR neobsahuje informace o všech plochách SLZ").
- **Known:** "Letiště a nouzové přistávací plochy" (aerobaze.cz) is on Cs:Česko/freemap#Potencionální_zdroje.
  This is a different, official source that also covers heliports and LZS sites, which the wiki entry
  does not mention.
- Wiki pages read: Tag:aeroway=heliport, Tag:aeroway=helipad, Tag:aeroway=aerodrome,
  Cs:Tag:aeroway=aerodrome, Tag:sport=parachuting.

## Wiki entry
```
===VFR příručka ČR – heliporty LZS, plochy SLZ, výsadková činnost===
* dataset: VFR příručka ČR (HEL 1 Heliporty, AD 1 Letiště a plochy SLZ)
* gestor: [https://aim.rlp.cz/ Řízení letového provozu ČR, s. p. – AIM]
* licence: podmínky užití webu – jen pro osobní potřebu, nutný souhlas ŘLP (aim@ans.cz) [https://aim.rlp.cz/?lang=en&p=terms-of-use]
* datové primitivy: body
* odkaz: https://aim.rlp.cz/vfrmanual/actual/hel_1_cz.html
* navržený tag {{tag|aeroway|heliport}} / {{tag|aeroway|helipad}} + {{tag|icao|<kód>}}, {{tag|sport|parachuting}}
* poznámka: polohy v OSM většinou jsou, chybí kódy (0 z 69 ploch SLZ, 15 z 60 heliportů LZS), aeroway=heliport (2 v ČR) a sport=parachuting (2 proti 48 místům s výsadkovou činností)
```
