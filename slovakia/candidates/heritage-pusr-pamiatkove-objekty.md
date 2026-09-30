# Pamiatkový úrad SR – open data PAMIS: register of immovable national cultural monuments (NNKP) and monument objects (PO)

| Field | Value |
|---|---|
| publisher | Pamiatkový úrad Slovenskej republiky (PÚ SR), information system PAMIS |
| url | https://www.pamiatky.sk/fileadmin/documents/opendata/pamiatkove-objekty.xml (PO, 62 MB) and https://www.pamiatky.sk/fileadmin/documents/opendata/nehnutelne-narodne-kulturne-pamiatky.xml (NNKP, 11 MB); index of all 20 packages: https://www.pamiatky.sk/online-sluzby/open-data |
| format | XML (one file per register, namespace `https://www.pamiatky.sk/opendata/1.0/…`) |
| coords | address-only: municipality and cadastral-area codes, street, súpisné číslo (conscription number), orientačné číslo, parcel numbers. No coordinates (the map tab of the online register is switched off) |
| records | 18,155 monument objects (PO) in 10,230 monuments (NNKP), 2026-09-30. PO with a súpisné číslo: 10,576. Largest types: DOM MEŠTIANSKY 2,312, KOSTOL 1,571, DOM ĽUDOVÝ 773, SOCHA 578, DOM BYTOVÝ 435, KAŠTIEĽ 424, TABUĽA PAMÄTNÁ 391, POMNÍK 306, PARK 286, KAPLNKA KRÍŽOVEJ CESTY 284 |
| osm_tags | heritage=2, heritage:operator=pusr, ref:pusr=&lt;ÚZPF number of the PO&gt; on the building or object; a type=site relation with the same tags for an NNKP made of several PO (per Key:heritage). This is the scheme already in use in Slovakia (see notes) |
| osm_count_sk | ref:pusr 271, heritage:operator=pusr 269, heritage (any) 450 (taginfo SK, 2026-09-30) |
| license | CC BY 4.0 ("Pamiatkový úrad poskytuje open data pod licenciou CC BY 4.0", also in the XML header comment). In June 2011 PÚ SR (Odbor ŠIS) answered an OSM volunteer by e-mail that its published lists "sú voľne šíriteľné. Takže máte náš súhlas" (osm_sk thread `TJS7gCF9muc`); that consent is not recorded on WikiProject Slovakia/Sources |
| license_url | https://www.pamiatky.sk/online-sluzby/open-data |
| license_status | needs_waiver (CC BY 4.0; the 2011 e-mail consent is a precedent to renew and record on the wiki) |
| update_freq | daily ("Open data sú aktualizované denne"; the PO file had Last-Modified 2026-09-30 06:20 GMT) |
| impact | 5 |
| sync_fit | Buildings with a súpisné číslo (~10,000 PO): MapRoulette tag-fix challenge built by joining (municipality, súpisné číslo) to MinvSKAddress address points and the building around them. Only tags are added, no geometry is imported. Objects without a number (statues, memorials, crosses, parks, ~7,600 PO): MapRoulette pointers at the parcel centroid. Not Sync: the source has no coordinates. The stable ref:pusr would let a later Sync dataset (ref_tag = ref:pusr) track changes |
| verified | yes |

## Try it

- **Map preview:** [../samples/heritage-pusr-pamiatkove-objekty-levoca.geojson](../samples/heritage-pusr-pamiatkove-objekty-levoca.geojson): all 341 PO in Levoča that have a súpisné číslo matching an OSM address point. Each point sits on that address point, which lies inside an OSM building in every case. The properties give the proposed `ref:pusr`, the unified and usual name, use, style, date and NNKP name. None of these 341 buildings carries a `heritage` tag in OSM today.
- **QGIS:** the XML has no geometry. Use the sample, or open the register as a table: *Layer → Add Layer → Add Vector Layer*, source `/vsicurl/https://www.pamiatky.sk/fileadmin/documents/opendata/pamiatkove-objekty.xml`. GDAL reads it as GML-less XML only partly, so converting with a script is more reliable. One `ns:po` element has `pusr_id`, `cislo_uzpf`, `unifikovany_nazov_po/nazov`, `zauzivany_nazov`, `obec/item/nazov`+`kod`, `ulica/item/nazov`, `supisne_cislo`, `orentacne_cislo` (sic) and `parcely/item/data` (`730/1-C-07.11.2024-Neurčené`).
- **Web:** register search https://www.pamiatky.sk/online-sluzby/registre-evidencie/register-nnkp ; monument detail `https://www.pamiatky.sk/online-sluzby/registre-evidencie/register-nnkp/detail-nnkp?code=RNNKP&detail_id=<NNKP entita_id>`

## Notes

- **Gap (Postpass, 2026-09-30).** PO are joined to OSM address points by `addr:city` = municipality and `addr:conscriptionnumber` = súpisné číslo. Four historic towns were checked; "tagged" counts buildings around the address point that already carry `heritage` or `ref:pusr`:

  | Town | PO | with súpisné číslo | found in OSM addresses | already tagged |
  |---|---|---|---|---|
  | Levoča | 401 | 348 | 341 | 0 |
  | Banská Štiavnica | 334 | 273 | 259 | 0 |
  | Kremnica | 183 | 134 | 127 | 0 |
  | Bardejov | 189 | 165 | 136 | 66 |

  About 94 % of numbered PO can be located this way, and apart from Bardejov (where someone has started) nothing is tagged. Nationally, 271 objects carry `ref:pusr` against 18,155 PO, so **about 17,900 protected objects have no heritage tagging in OSM**. The 271 existing ones cluster around Bardejov (84), Rožňava/Krásna Hôrka (53) and Bratislava.
- **Existing tagging scheme** (Postpass sample): `heritage=2` + `heritage:operator=pusr` + `ref:pusr=303/7`, sometimes with `source=https://www.pamiatky.sk/nkp-a-po/register-po/objekt-detail/?idObjekt=…` (the old register URL). `ref:pusr` holds the ÚZPF number of the PO (`<NNKP number>/<object index>`). A few objects keep the pre-2002 number (`101-203/0`); the PAMIS files have only the current one. Neither `ref:pusr` nor the Slovak operator is documented on the wiki yet: Key:heritage has no Slovakia section. Adding one with this scheme is the first step. Wiki pages read: Key:heritage (single object → `heritage`, `heritage:operator=xxx`, `ref:xxx`; ensembles → type=site relation), Tag:historic=memorial.
- **Stable IDs:** `cislo_uzpf` (the legal ÚZPF number, the value for `ref:pusr`), plus `pusr_id` (`PO9679`, `NNKP13086`) and `entita_id` (UUID). An NNKP with several PO (a manor house with chapel and park) becomes a site relation carrying the NNKP number, and each member gets its PO number.
- **Positioning without coordinates:**
  - Súpisné číslo covers 58 % of PO (10,576): mostly town houses, churches, manor houses, folk houses, villas. The OSM side is reliable because MinvSKAddress put `addr:conscriptionnumber` on 1.49 million address points.
  - The remaining 7,579 PO are mostly small objects: SOCHA 567, POMNÍK 296, PARK 253, KAPLNKA KRÍŽOVEJ CESTY 243, PODSTAVEC 203, graves, gardens, church-yard cemeteries. 7,339 of them have parcel numbers with the cadastral-area code. Parcel centroids can come from the cadastre INSPIRE download (the 2021 ÚGKK consent covers INSPIRE services). They are pointers only, so the object itself is found on imagery or in the field.
  - Some PO with a súpisné číslo are parts of one building complex, so several PO can land on one address. Join on street and orientačné číslo too where both are present.
- **ZBGIS overlap (KTO ZBGIS):** ZBGIS has buildings with a use code (Kostol 50, Kaplnka 3, Hrad 4, Synagóga 308, Múzeum 9), AL116 Božie muky/kríž, AL130 Pomník and the "Sakrálne pamiatky" / "Hrad, zámok; hrádok" / "Zrúcanina" features. None of these carries protection status or the ÚZPF number. PAMIS adds legal status, the stable number, dates, style and the unified name, which ZBGIS lacks.
- **Other PAMIS packages** (same page, same licence): pamiatkové rezervácie (28) and pamiatkové zóny (82). Both have name, type, declaring act, area in m² and cadastral areas but **no polygons**. So `boundary=protected_area` + `protect_class=22` areas still have to be drawn from the declaring acts. Also available: ochranné pásma, svetové kultúrne dedičstvo, bývalé NKP (72), súčasti architektúry. Archeologické náleziská and archeologické výskumy (geom) were empty on 2026-09-30.
- **Attributes worth carrying:** `start_date` from `vznik` (free text such as "1636" or "pred 1627", so normalise it), `architecture` from `prevladajuci_sloh` (needs a mapping table: renesancia → renaissance, barok → baroque), `name` only where `zauzivany_nazov` is a real name ("Andrássyovský kaštieľ"), not a description ("prícestný kríž").
- **Caveats:** the register is legal and descriptive, not geometric. "Open data majú informatívny charakter" (not valid for legal purposes). Hnuteľné NKP and pamiatkové predmety are published only in restricted form and are out of scope anyway.
- **Contact:** PÚ SR, Odbor evidencie pamiatkového fondu (https://www.pamiatky.sk/pusr/odbor-evidencie-pamiatkoveho-fondu); open data page https://www.pamiatky.sk/online-sluzby/open-data.

## Wiki entry
```
=== Register nehnuteľných NKP a pamiatkových objektov (PAMIS) ===
* dataset: Open data PAMIS – Nehnuteľné národné kultúrne pamiatky, Pamiatkové objekty (denne aktualizované XML)
* správca: [https://www.pamiatky.sk/ Pamiatkový úrad SR]
* licencia: CC BY 4.0 [https://www.pamiatky.sk/online-sluzby/open-data] (súhlas PÚ SR e-mailom z 21. 6. 2011, vlákno osm_sk TJS7gCF9muc – treba obnoviť a zapísať)
* dátové primitívy: body (bez súradníc – adresa so súpisným číslom, parcely)
* odkaz: https://www.pamiatky.sk/fileadmin/documents/opendata/pamiatkove-objekty.xml
* navrhované značky: {{tag|heritage|2}}, {{tag|heritage:operator|pusr}}, {{tag|ref:pusr|<číslo ÚZPF PO>}}
* poznámka: 18 155 pamiatkových objektov, v OSM má ref:pusr len 271 objektov; ~10 000 budov sa dá nájsť cez súpisné číslo z MinvSKAddress (v Levoči 341 z 348, žiadna nie je označená).
```
