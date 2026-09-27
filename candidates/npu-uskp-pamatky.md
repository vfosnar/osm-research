```
name: Ústřední seznam kulturních památek (ÚSKP) – immovable cultural monuments, incl. spatial identification (definition points / centroids / polygons)
publisher: Národní památkový ústav (NPÚ), IČO 75032333
url: attributes CSV https://www.pamatkovykatalog.cz/opendata/npu_opendata_KP.csv (also _NKP, _PR, _PZ, _OP, _SD, _NZ.csv); points: ATOM https://geoportal.npu.cz/opendata/atom/NPU_USKP_DefinicniBod/npu.xml -> per-region GML e.g. https://geoportal.npu.cz/opendata/atom/NPU_USKP_DefinicniBod/NPU_USKP_DefinicniBod_CZ010.gml (also NPU_USKP_Centroid, NPU_USKP_Polygon feeds)
format: CSV (UTF-8, comma); GML 3 (FME) in EPSG:5514, 14 files (one per kraj)
coords: yes (GML points/polygons, S-JTSK); CSV is address-only
records: CSV KP 39,161 (objekt 25,924, areál 12,194, soubor 985); GML definition points 39,357 over 14 regions (checked 2026-09-27)
osm_tags: heritage=3 (kulturní památka) / heritage=2 (národní kulturní památka), heritage:operator=npu, ref:npu=<katalogové číslo>; optionally heritage:ref=<rejstříkové číslo ÚSKP>; added to existing building/historic objects
osm_count_cz: heritage=* 1,916; heritage:operator=npu 1,355; ref:npu 492 (449 distinct); heritage:ref 265 (taginfo 2026-09-26)
license: CSV: CC BY 4.0 (NKOD terms spec: autorské dílo CC BY 4.0, not a copyright-protected DB, no sui generis right). GML (ÚSKP spatial identification): NKOD spec says CC BY-SA 4.0 while the ATOM feed <rights> says "CC-BY 4.0" – conflicting.
license_url: https://data.gov.cz/zdroj/datové-sady/75032333/1319287273 ; https://data.gov.cz/zdroj/datové-sady/75032333/4eddaa535b9455da1dbb30ca4fd13d44 ; https://creativecommons.org/licenses/by/4.0/
license_status: needs_waiver
update_freq: CSV monthly; GML "continuous" (feed updated 2025-11-21 at time of check)
impact: 5
verified: yes
```

## Notes
- **Gap is huge.** Czechia has ~39k listed immovable monuments; OSM has only 1,916 objects with `heritage=*` and 492 with `ref:npu`. Prague bbox (Postpass): 242 heritage-tagged objects vs 2,173 ÚSKP points in Prague.
- **Easy conflation via RÚIAN.** Each GML point has `KodStavObjRUIAN` (RÚIAN building code). It is filled for 1,215/2,173 (56 %) in Prague. OSM has 3.8M `ref:ruian:building`. Postpass test: 181 of the first 200 Prague RÚIAN codes match an OSM building polygon, and only 11 of those carry `heritage`. So most of the work is adding tags to existing buildings, with no new geometry. Non-building monuments (crosses, statues, chapels, areals) need point matching. drobnepamatky.cz (already synced) covers many small monuments, so add `ref:npu` to those rather than duplicating them.
- **IDs.** GML fields: `rejstrikoveCisloUSKP` (e.g. 105884), `prvekId`, `prStavId`, `IDOB_PG`, `typOchranyKod` (KP/NKP), `NazevPrvku`, address, `datumOchranyOd`. CSV: `katalogové_číslo` (10-digit, e.g. 1000118337, the same form as existing OSM `ref:npu` values), `rejstříkové_číslo_ÚSKP`, `PrStavId`, `anotace`. Join CSV↔GML on `PrStavId`/`prStavId`, which still needs checking.
- **Tagging.** Key:heritage wiki, Czech Republic section: `heritage=2` (NKP) / `heritage=3` (KP) + `heritage:operator=npu` + `ref:npu=*`. Read at https://wiki.openstreetmap.org/wiki/Key:heritage (raw). There is no Cs:Key:heritage page.
- **Alternative (CC0).** Wikidata has 43,223 items with P762 (ÚSKP ID), 43,413 coordinate statements (WDQS 2026-09-27). It could be used for `wikidata=*` linking, but the provenance of its coordinates is unknown. Sync already handles Wikidata castles and museums (QID only).
- **Licence.** CC BY 4.0 needs an explicit OSM waiver from NPÚ. Also ask NPÚ to fix the BY-SA vs BY conflict on the spatial dataset. Contact: gis@npu.cz (ATOM author).
- Památkové zóny/rezervace (PZ 503, PR 114 rows in CSV) could go into `boundary=protected_area` + `protect_class=22`. OSM has only 8 `protect_class=22`. Polygons would need the NPÚ geoportal (not checked in detail).

## Wiki entry
```
===Ústřední seznam kulturních památek (NPÚ)===
* dataset: Kulturní památky + Prostorová identifikace ÚSKP (definiční body, polygony)
* gestor: [https://www.npu.cz/ Národní památkový ústav]
* licence: CC BY 4.0 (prostorová data dle NKOD CC BY-SA 4.0, v ATOM CC-BY 4.0) [https://data.gov.cz/zdroj/datové-sady/75032333/1319287273] – nutný souhlas pro OSM
* datové primitivy: body, plochy (+ CSV s adresami)
* odkaz: https://www.pamatkovykatalog.cz/opendata/npu_opendata_KP.csv , https://geoportal.npu.cz/opendata/atom/NPU_USKP_DefinicniBod/npu.xml
* navržený tag {{tag|heritage|3}} / {{tag|heritage|2}}, {{tag|heritage:operator|npu}}, {{tag|ref:npu|<katalogové číslo>}}
* poznámka: v OSM 1 916 objektů s heritage (492 s ref:npu) z ~39 000 památek; body obsahují kód stavebního objektu RÚIAN, takže jde většinou jen o doplnění tagů na existující budovy
```
