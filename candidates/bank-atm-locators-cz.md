# Bank ATM locators – Sdílený bankomat (KB, MONETA, Air Bank, UniCredit) and Česká spořitelna Places API

| Field | Value |
|---|---|
| publisher | Komerční banka, a.s. (IČO 45317054; runs sdilenybankomat.cz for the shared network of KB, MONETA Bank, Air Bank and UniCredit Bank); Česká spořitelna, a.s. |
| url | https://sdilenybankomat.cz/data/atm_import_log/data-171.js (static JS array behind https://sdilenybankomat.cz/; the file number changes with each import, so read the current `<script src>` from the home page); https://www.csas.cz/webapi/api/v3/places/?size=5000 (needs header `Web-Api-Key: &lt;key from the page source&gt;`, the public key embedded in https://www.csas.cz/cs/pobocky-a-bankomaty); KB only: POST https://www.kb.cz/api/BranchAndAtmList/Atms (see notes) |
| format | JavaScript marker array (Sdílený bankomat); JSON (ČS, KB) |
| coords | yes |
| records | Sdílený bankomat 1,912 ATMs (2026-09-28): KB 739, MONETA 542, Air Bank 372, UniCredit 259; 983 deposit ("Vkladový"), 929 withdrawal-only. ČS Places API: 1,511 CZ ATMs (1,153 OPEN, 30 OUT_OF_ORDER, 328 CLOSED) + 377 CZ branches; the same API also returns 2,080 Erste ATMs in SK/AT/HU/HR. KB API: 744 ATMs with `sourceItemId` (S1AS…) |
| osm_tags | amenity=atm, brand + brand:wikidata of the bank (Česká spořitelna Q341100, Komerční banka Q1541079, Moneta Bank Q24282966, Air Bank Q10723691, UniCredit Bank Q45568 – the values already used in OSM), operator, cash_in=yes for deposit ATMs, opening_hours (24/7 for "nepřetržitě"/"Přístup 24/7"), ref=&lt;ATM number&gt; (Tag:amenity=atm lists brand, operator, network, cash_in, ref, opening_hours) |
| osm_count_cz | amenity=atm 3,424 (taginfo CZ, data 2026-09-26). Local match against the 2026-09-27 Czechia extract: 4,146 ATM objects (amenity=atm, or bank + atm=yes); brand Česká spořitelna 737, Komerční banka 404, Moneta 198, Air Bank 131, UniCredit 67 |
| license | none stated |
| license_url | https://sdilenybankomat.cz/ (footer names KB as site operator; no terms of use for the data); https://www.csas.cz/cs/pobocky-a-bankomaty (no data terms) |
| license_status | unclear |
| update_freq | Sdílený bankomat: per import (Last-Modified 2026-09-14, import no. 171); ČS and KB: live, with per-ATM state (ČS: OPEN / OUT_OF_ORDER / CLOSED) |
| impact | 4 |
| sync_fit | Sync for KB ATMs (stable sourceItemId); MapRoulette for other banks (no stable id) |
| verified | yes |

## Try it

- **Map preview:** none, because the licence is unclear (no terms published), so no extract is redistributed here.
- **QGIS (Sdílený bankomat):** convert the JS to CSV (tested 2026-09-28, 1,912 rows):
  ```
  curl -s https://sdilenybankomat.cz/data/atm_import_log/data-171.js | python3 -c "import re,sys,csv;s=sys.stdin.read();w=csv.writer(open('sdileny.csv','w'));w.writerow(['lat','lon','bank','text']);[w.writerow([a,b,re.sub('<br>.*','',c)[3:],re.sub('<[^>]+>',' ',c)]) for a,b,c in re.findall(r'lat =\s*([-\d.]+)\s*;\s*gm_t.lng =\s*([-\d.]+)\s*;\s*gm_t.city =\s*\"(.*?)\";',s,re.S)]"
  ```
  Then *Layer → Add Layer → Add Delimited Text Layer…*: `sdileny.csv`, CSV, UTF-8, X = `lon`, Y = `lat`, CRS EPSG:4326.
- **QGIS (Česká spořitelna):** the API needs a request header, so fetch it with curl (tested 2026-09-28, 1,888 CZ rows):
  ```
  curl -s -H "Web-Api-Key: $CS_KEY" 'https://www.csas.cz/webapi/api/v3/places/?size=5000' | python3 -c "import json,sys,csv;w=csv.writer(open('cs.csv','w'));w.writerow(['id','type','state','name','address','city','lat','lon','accessType','deposit']);[w.writerow([i['id'],i['type'],i.get('state'),i['name'],i['address'],i['city'],i['location']['lat'],i['location']['lng'],i.get('accessType'),i.get('serviceStatusDeposit')]) for i in json.load(sys.stdin)['items'] if i['country']=='CZ']"
  ```
  Add `cs.csv` as a delimited text layer: X = `lon`, Y = `lat`, EPSG:4326. Filter `"type" = 'ATM' AND "state" <> 'CLOSED'`.
- **Web viewers:** https://sdilenybankomat.cz/ , https://www.csas.cz/cs/pobocky-a-bankomaty , https://www.kb.cz/cs/pobocky-a-bankomaty/bankomaty

## Notes

**Gap (local match against the 2026-09-27 Czechia extract, 50 m radius).** "Same bank" means an OSM ATM within 50 m whose brand/operator/name/network names that bank.

| Network | Feed ATMs | Any OSM ATM ≤50 m | Same-bank OSM ATM ≤50 m | Missing (no same-bank match) |
|---|---|---|---|---|
| Komerční banka (Sdílený bankomat) | 739 | 520 | 460 | 279 |
| MONETA Bank (Sdílený bankomat) | 542 | 309 | 248 | 294 |
| Air Bank (Sdílený bankomat) | 372 | 278 | 170 | 202 |
| UniCredit Bank (Sdílený bankomat) | 259 | 162 | 135 | 124 |
| Česká spořitelna (state ≠ CLOSED) | 1,183 | 914 | 834 | 349 |
| **Total** | **3,095** | 2,183 | 1,847 | **1,248** |

- About 910 of the feed ATMs have no OSM ATM of any bank within 50 m; the rest of the 1,248 are OSM ATMs with a different or missing brand (the shared network moved and rebranded duplicate ATMs, so an old MONETA-tagged ATM may now be a KB one). The missing ATMs are spread across the country: Praha 48, Ostrava 36, Brno 22, Plzeň 19, Liberec 17 among the shared ones.
- **Stale OSM data:** 328 ČS ATMs are `CLOSED` in the API, and 151 of them still have a Česká spořitelna ATM in OSM within 50 m. This is a list of likely-removed ATMs to check.
- **IDs:** ČS gives `atmNumber` (1,511 unique). OSM already carries ČS ATM numbers in `ref` on 123 ATMs (formats `3130` and `CS7517`; 48 match the API numbers exactly). KB's API gives `sourceItemId` (`S1AS5290`), the same format already present in OSM `ref` on KB ATMs (`S1AS7060`). The Sdílený bankomat file has **no id**, only coordinates, address and a free-text location, so for KB use the KB API instead; MONETA ATM detail URLs contain `S1DS…` ids (https://www.moneta.cz/kontakt/bankomaty-moneta-money-bank) but no coordinates were found in the HTML.
- **Attributes:** Sdílený bankomat marks deposit vs withdrawal ATMs ("Vkladový"/"Výběrový", which maps to cash_in), 24/7 vs shop hours, wheelchair and contactless icons. ČS gives accessType ("nepřetržitě" 1,168; "denně 07:00-22:00" 100), serviceStatusDeposit (445 Available), install date and live state. ČS branch records also include staff names and phone numbers, which must not be imported.
- **KB API recipe (tested 2026-09-28):** GET https://www.kb.cz/cs/pobocky-a-bankomaty with a cookie jar, read `requestVerificationToken` from the page's `WIDGETS_CONFIG`, then POST JSON `{"latitude":50.08,"longitude":14.42,"baseUrl":"/cs/pobocky-a-bankomaty/bankomaty","limit":5000,"offset":0,"cultureCode":"cs-CZ","isPageDetail":false}` with header `__RequestVerificationToken: <token>`; the response `payload.data` has 744 ATMs. Without the token it returns HTTP 400.
- **Known status:** Cs:Česko/freemap lists the old ČS Garmin XML (gps_ATM_poi_garmin.xml) under *Zastaralé/nefunkční zdroje* with licence "neznámá". The v3 Places API is a different, live source. The only bank with OSM consent on the page is Fio banka. Neither AllThePlaces (only `unicredit_bank_cz`, `fio_banka*`) nor Sync covers these banks.
- **Not covered:** ČSOB (~427 ATMs in OSM) – its locator page is behind an F5 bot challenge (TSPD), no feed found. Raiffeisenbank – locator is server-rendered, no API endpoint found. Euronet – only a PL spider in ATP.
- **Licence:** no terms published for either feed. Contacts: Komerční banka (operator of sdilenybankomat.cz, on behalf of the four banks) and Česká spořitelna. A bank's written consent would follow the Fio banka precedent on Cs:Česko/freemap.
- Suggested `ref` handling: keep the existing OSM practice of `ref=<bank ATM id>`; a namespaced key (`ref:csas`, `ref:kb`) would avoid clashes when an ATM changes operator in the shared network.
- Wiki page read: Tag:amenity=atm.

## Wiki entry
```
===Bankomaty – Sdílený bankomat (KB, MONETA, Air Bank, UniCredit) a Česká spořitelna===
* dataset: Sdílené bankomaty (sdilenybankomat.cz); Česká spořitelna – pobočky a bankomaty (webapi v3/places)
* gestor: [https://sdilenybankomat.cz/ Komerční banka, a.s.] (za KB, MONETA, Air Bank, UniCredit); [https://www.csas.cz/cs/pobocky-a-bankomaty Česká spořitelna, a.s.]
* licence: neuvedena
* datové primitivy: body
* odkaz: https://sdilenybankomat.cz/data/atm_import_log/data-171.js ; https://www.csas.cz/webapi/api/v3/places/?size=5000 (hlavička Web-Api-Key z webu ČS)
* navržený tag {{tag|amenity|atm}}, {{tag|brand|<banka>}}, {{tag|cash_in|yes}} u vkladových, {{tag|ref|<číslo bankomatu>}}
* poznámka: ve 3 095 bankomatech z obou zdrojů chybí v OSM do 50 m bankomat téže banky u 1 248 (asi 910 bez jakéhokoli bankomatu); 151 bankomatů ČS označených v API jako zrušené v OSM stále je
```
