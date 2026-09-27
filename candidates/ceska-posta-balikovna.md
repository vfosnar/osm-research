# Česká pošta – Balíkovna XML (post offices, Balíkovna partner points, Balíkovna-BOX partner lockers)

| Field | Value |
|---|---|
| publisher | Česká pošta, s.p. |
| url | http://napostu.ceskaposta.cz/vystupy/balikovny.xml |
| format | XML (namespace http://www.cpost.cz/schema/aict/zv_2) |
| coords | yes (WGS84 + S-JTSK) |
| records | 11,428 (generated 2026-09-27T17:52): 2,905 pošta, 3,847 balíkovna partner, 4,629 balíkovna-BOX, 47 depo. The boxes break down by BOX_PROVIDER as AB=AlzaBox 3,840, OX=OX Point 405 and PB=Penguin Box 384. |
| osm_tags | boxes → amenity=parcel_locker + brand of the physical box (AlzaBox Q115254158 / Penguin Box Q120022128 / OX Point); partner points → post_office=post_partner on the host shop (+ parcel_pickup / parcel_mail_in) |
| osm_count_cz | brand:wikidata=Q115254158 (AlzaBox) 2,136; brand=Penguin Box 172; brand=OX Point 93; post_office=post_partner 71 (taginfo CZ, data 2026-09-26) |
| license | none stated |
| license_url | https://www.ceskaposta.cz/en/ke-stazeni/zakaznicke-vystupy (customer-output downloads page; no licence text found) |
| license_status | unclear |
| update_freq | daily (Last-Modified 2026-09-27; &lt;generated&gt; timestamp in the file) |
| impact | 4 |
| verified | yes |

## Try it

- **Map preview:** none, because the licence is unclear (nothing is published), so no extract is redistributed here.
- **QGIS:** the XML is not a GIS format. Convert it to CSV first (tested 2026-09-27, 11,428 rows):
  ```
  curl -s http://napostu.ceskaposta.cz/vystupy/balikovny.xml | python3 -c "import csv,sys,xml.etree.ElementTree as E;n='{http://www.cpost.cz/schema/aict/zv_2}';F=['PSC','NAZEV','TYP','BOX_PROVIDER','ADRESA','SOUR_X_WGS84','SOUR_Y_WGS84'];w=csv.writer(open('balikovny.csv','w'));w.writerow(F);[w.writerow([r.findtext(n+f,'') for f in F]) for r in E.parse(sys.stdin).getroot().iter(n+'row')]"
  ```
  Then *Layer → Add Layer → Add Delimited Text Layer…*: `balikovny.csv`, CSV, UTF-8, X = `SOUR_X_WGS84`, Y = `SOUR_Y_WGS84`, CRS EPSG:4326. To see only the lockers, filter `"TYP" = 'balíkovna-BOX'`.
- **Web viewer:** https://www.balikovna.cz/cs/vyhledat-balikovnu

## Notes

- **Relation to existing work:**
  - Post offices are already covered by the ZABAGED post_office layer in Sync.
  - Česká pošta post boxes (schránky) are already in Sync.
  - This file adds the **Balíkovna network**: the partner pick-up points and the partner lockers.
  - ATP spider `czech_post_cz` scrapes a similar list from postaonline.cz: 12,267 features, including 4,773 unbranded parcel_locker and 4,497 "amenity=yes" partner points. This XML is the operator's own output, with a unique id (`PSC` field, 11,428 unique of 11,428).
- **Locker gap (spatial check within 40 m of an OSM locker of the same brand, Postpass CZ bbox, 2026-09-27):**

  | Provider | Feed | Matched | Missing |
  |---|---|---|---|
  | AlzaBox | 3,840 | 1,809 | **2,031** |
  | Penguin Box | 384 | 58 | **326** |
  | OX Point | 405 | 118 | **287** |

  This is the same AlzaBox gap as in `dpd-pickup-cz.md`. Two independent feeds agree to within 2 %.
- **Partner points:** 3,847 Balíkovna counters sit inside shops (Allwyn/Žabka, tobacconists …). OSM has only 71 `post_office=post_partner` in all of CZ.
  - The fit is `post_office=post_partner` on the host POI. Tag:post_office=post_partner (wiki, raw) says: "Add to the POI the tag post_office=post_partner and specify the postal services over the post_office namespace".
  - This is an attribute conflation (matching to existing shops), not point creation, so it is less suited to automatic Sync.
- **Fields:** PSC (id), NAZEV, ADRESA, TYP, OTEV_DOBY (per-day opening hours), SOUR_X_WGS84 / SOUR_Y_WGS84 (lon / lat), POPIS (location hint, for example "vchod do lékárny"), PRIJEM_NR, TISK_STITKU, BOX_PROVIDER, PLATBA_KARTOU, PODANI_SML_POD.
- **Wiki pages read:** Tag:amenity=parcel_locker, Tag:post_office=post_partner (raw wikitext).
- **Key:** use a namespaced `ref:balikovna=<PSC>` (0 uses today, taginfo CZ). Bare `ref` on AlzaBox lockers already holds Alza's own ids on about 1,055 objects.
- **Branding caveat:** the boxes are physically other brands (AlzaBox, Penguin Box, OX Point). Balíkovna is only a service offered in them. There is no "Balíkovna" brand on OSM lockers in CZ (taginfo brand=Balíkovna: 0).
- **Licence:** none published. Česká pošta is a state enterprise (s.p.), not a public authority. Its data is not úřední dílo, so consent is needed. Contact: Česká pošta customer outputs / info@cpost.cz.

## Wiki entry

```
===Balíkovna – výdejní místa a boxy===
* dataset: seznam poboček, partnerských výdejních míst Balíkovna a Balíkovna-BOXů (AlzaBox, Penguin Box, OX Point)
* gestor: [https://www.ceskaposta.cz/ Česká pošta, s.p.]
* licence: neuvedena – nutný souhlas [https://www.ceskaposta.cz/en/ke-stazeni/zakaznicke-vystupy]
* datové primitivy: body
* odkaz: http://napostu.ceskaposta.cz/vystupy/balikovny.xml
* navržený tag {{tag|amenity|parcel_locker}}, {{tag|post_office|post_partner}}, {{tag|ref:balikovna|<PSC>}}
* poznámka: v OSM chybí cca 2 000 AlzaBoxů, 330 Penguin Boxů, 290 OX Pointů a téměř všech 3 847 partnerských výdejních míst (post_partner jen 71×).
```
