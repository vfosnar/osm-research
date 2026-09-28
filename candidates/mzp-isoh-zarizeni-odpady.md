# MŽP ISOH – Seznam zařízení pro nakládání s odpady (waste facility register: collection yards/scrap buyers, composting, landfills, car dismantlers, transfer stations)

| Field | Value |
|---|---|
| publisher | Ministerstvo životního prostředí (MŽP), IČO 00164801 (ISOH / VISOH2) |
| url | https://data.mzp.cz/isoh2/OpenData/HF09/Zarizeni.xml (NKOD: https://data.gov.cz/zdroj/datové-sady/00164801/a7be43fdca614429fc50f48883a50298) |
| format | XML (namespace http://mzp.cz/visoh2registrv1.xsd), about 400+ MB single file; the server does not support byte ranges and the proxy reset the transfer at about 377 MB twice |
| coords | yes (umisteni/gpsSirka + gpsDelka, WGS84, 6 decimals), plus a RÚIAN-style address (obec, ZÚJ code, street, č.p.) |
| records | at least 8,753 facilities parsed from a truncated download that covered 11 of 14 regions. Of these, 5,056 are active, 3,185 closed, 293 permitted and 219 suspended; 6,416 have GPS. The full file probably holds about 11k facilities. |
| osm_tags | by kodTypuZarizeni: Sberna -&gt; amenity=recycling + recycling_type=centre (municipal yards / scrap buyers; add recycling:*=yes from permitted waste codes); ZpracVozidel/SberVozidel -&gt; industrial=scrap_yard; Skladka -&gt; landuse=landfill; Kompost/KompostMale -&gt; no established tag (see notes; possibly amenity=recycling + recycling:organic=yes or landuse=industrial); Prekladiste -&gt; amenity=waste_transfer_station; Spalovani/ZEVO -&gt; power=plant / man_made=works (check); ref:CZ:isoh=&lt;icz&gt; (new key, needs documenting) |
| osm_count_cz | recycling_type=centre 902; industrial=scrap_yard 53; amenity=waste_transfer_station 24; landuse=landfill 387 (Geofabrik taginfo 2026-09-27) |
| license | NKOD terms: no copyright work, not a copyright-protected database, no sui generis right (NKOD maps it to CC0). The dataset is flagged "obsahuje osobní údaje" because operators can be natural persons. |
| license_url | https://data.gov.cz/podmínky-užití/neobsahuje-autorská-díla/ ; https://data.gov.cz/podmínky-užití/není-chráněna-zvláštním-právem-pořizovatele-databáze/ |
| license_status | ok |
| update_freq | annual (NKOD). The export header shows datumExportu 2026-09-26, so the file is actually regenerated daily. |
| impact | 4 |
| sync_fit | MapRoulette (facility type → many different tag schemes, some undocumented) |
| verified | partial |

## Try it
- **Map preview:** [samples/mzp-isoh-zarizeni-odpady.geojson](../samples/mzp-isoh-zarizeni-odpady.geojson): 309 active facilities with GPS in Královéhradecký kraj (icz prefix CZH), including 135 Sberna and 32 ZpracVozidel. Mobile, sludge-on-field and backfilling types are left out. The sample was parsed from the first 120 MB of the 2026-09-26 export. Operator names are dropped because they include natural persons.
- **QGIS:** there is no direct load. The source is a single ~400 MB custom XML (not GML), and I found no public map service: isoh.mzp.cz reset the connection. Download the sample and drag it into QGIS instead.

## Notes
- This is the statutory register of every facility permitted under §21 of Act 541/2020 (and the older 185/2001). Each facility has a stable ID `icz`; CZK00551 is the first record in the 2026-09-26 export. The first three letters encode the region (CZA Praha, CZS Středočeský, CZT Moravskoslezský, and so on).
- Facility types (`kodTypuZarizeni`) among active records in the partial parse: Sberna 1,533 (all with GPS); MobSber 758 (mobile, no location, skip); MobMechZprac 388 (mobile, skip); Recyklace 311; Kompost 282; ZpracVozidel 250 (car dismantlers); Stac01 150; KalZemPud 138 (sludge on fields, skip); Zasyp 127 (backfilling, skip); KompostMale 124; Skladka 80; TridDotrid 79; Prekladiste 54; SberVozidel 32; COV 31; Bioplyn 23+16; Spalovani 14.
- OSM gap, checked with Postpass on a random sample of 200 active facilities per type, looking for an OSM feature within 200 m:
  - Sberna: 48/200 (24%) matched any of recycling_type=centre, scrap_yard, waste_transfer_station, landfill or shop=scrap. About 76% are missing.
  - ZpracVozidel: 19/200 (10%) matched.
  - Skladka: 49/80 (61%) matched landuse=landfill.
  - Kompost: 90/200 matched a loose industrial/landfill/recycling condition. Specific tagging is absent.
- "Sberna" mixes municipal collection yards (sběrné dvory, run by the obec or its technické služby) with commercial scrap buyers (výkupny kovů/papíru). The operator's IČO and name tell them apart: public-sector IČO means a sběrný dvůr, otherwise shop=scrap / recycling centre. Map only facilities with a GPS position and the state `aktivni`.
- Personal data: operators who are natural persons appear by their personal name. Do not import operator names for those; take only location, type and icz.
- Composting has no well-established tag. Check the wiki (Tag:amenity=recycling mentions compost as a recycling:* material; Tag:landuse=industrial) and the CZ community before mapping.
- A national register of this kind is not in covered.md, and "sběrné dvory" does not appear among the known ideas on Cs:Česko/freemap. EkoKom (covered) covers containers, not yards.
- Wiki pages read: Tag:amenity=recycling, Tag:recycling_type=centre (approved; combination landuse=industrial), Tag:industrial=scrap_yard (de facto; alternatives amenity=recycling+recycling_type=centre+recycling:metal=yes), Tag:landuse=landfill, Tag:amenity=waste_transfer_station.
- Practical: download the file with a long timeout from a stable network, or ask MŽP for a GeoJSON/CSV. An ISOH map service may also exist (not checked).

## Wiki entry
```
===Zařízení pro nakládání s odpady (ISOH)===
* dataset: Seznam zařízení pro nakládání s odpady
* gestor: [https://www.mzp.cz/ Ministerstvo životního prostředí]
* licence: neobsahuje autorská díla, není chráněnou databází (CC0) [https://data.gov.cz/zdroj/datové-sady/00164801/a7be43fdca614429fc50f48883a50298]
* datové primitivy: body (GPS)
* odkaz: https://data.mzp.cz/isoh2/OpenData/HF09/Zarizeni.xml
* navržený tag {{tag|amenity|recycling}} + {{tag|recycling_type|centre}}, {{tag|industrial|scrap_yard}}, {{tag|landuse|landfill}}, {{tag|ref:CZ:isoh|<IČZ>}}
* poznámka: registr všech povolených sběren, sběrných dvorů, autovrakovišť, kompostáren a skládek; v OSM chybí asi 3/4 sběren (vzorek 200 bodů, 24 % nalezeno)
```
