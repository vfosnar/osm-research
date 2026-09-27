```
name: ERÚ – Technologická energetická zařízení: výrobny elektřiny (licensed power plants: small hydro, biogas, wind, CHP, solar parks)
publisher: Energetický regulační úřad (ERÚ), IČO 70894451
url: https://eru.gov.cz/sites/default/files/obsah/prilohy/tez-sk-11-2026-09-01.xml (monthly dated file; NKOD dataset: https://data.gov.cz/zdroj/datové-sady/70894451/1713221853)
format: XML (schema https://licence.eru.cz/xsd/vzor-11-v5.xsd), 56 MB
coords: no. Location is given as cadastral territory code (CadasterId = RÚIAN KÚ code) plus parcel number(s) in free text (CadasterNote, e.g. "par. č. 313/2, 313/7"), plus obec/PSČ. Hydro plants also have River + RiverKm (1,553 of 1,605).
records: 37,958 premises (37,956 unique PremiseElecId) under 34,141 licences. By type: solar 34,433, gas/combustion 1,677, hydro 1,605, wind 124, steam 108, combined-cycle 4, pumped storage 3, nuclear 2. Of these, 1,196 are 1 MW or more. By fuel: Bioplyn 414 (+ Skládkový plyn 70, Kalový plyn 62), Biomasa 47, Důlní plyn 26.
osm_tags: >=1 MW: power=plant + plant:source=hydro|biogas|wind|solar|gas|biomass + plant:method + plant:output:electricity=<n> MW + name. <1 MW (micro hydro, rooftop PV): power=generator + generator:source + generator:output:electricity. Proposed ref:CZ:eru=<PremiseElecId> (new key).
osm_count_cz: power=plant 886; plant:source=hydro 255; generator:source=hydro 249; plant:source=biogas 5; generator:source=biogas 27; plant:source=wind 11; generator:source=wind 257 (Geofabrik taginfo 2026-09-27)
license: NKOD terms: no copyright work, not a protected database, no sui generis right, no personal data (NKOD maps it to CC0)
license_url: https://data.gov.cz/podmínky-užití/neobsahuje-autorská-díla/ ; https://data.gov.cz/podmínky-užití/není-chráněna-zvláštním-právem-pořizovatele-datab%C3%A1ze/
license_status: ok
update_freq: continuous (NKOD UPDATE_CONT); in practice a new dated XML each month
impact: 4
verified: yes
```

## Notes
- This is the only complete official list of every licensed electricity generator in CZ, with name, installed electrical and thermal output per unit (MW), fuel, and for hydro the river and river km.
- Gap: ERÚ lists 1,605 hydro premises (mostly small MVE on mill weirs), while OSM has about 500 hydro plant+generator objects combined. For biogas, ERÚ has about 420 premises against about 32 in OSM. Every biogas station and most MVE are therefore missing or lack source/output tags. Wind: ERÚ counts premises (farms), OSM counts turbines, so wind is probably well covered.
- Solar dominates the count (34k), but most is rooftop PV under 1 MW. Only 645 solar premises are 1 MW or more, and those are the useful ones (landuse polygons already exist from ortho mapping; add plant tags and output).
- Geocoding: the CadasterId + parcel number can be resolved to a parcel centroid through ČÚZK (the RÚIAN/KN parcel definition point; ČÚZK data is already permitted, see covered.md). The parcel note is free text ("par. č.", "l. v.", comma lists), so expect about 90% to parse. For hydro, snapping to river km on DIBAVOD (covered) is an alternative.
- Stable ID: PremiseElecId (e.g. 01782_T11) persists across licence versions.
- Also available and not verified: separate ERÚ XMLs for heat plants (výrobny tepelné energie), gas production (výrobny plynu, i.e. biomethane), and electricity storage (ukládání elektřiny, i.e. battery storage), all on NKOD under ERÚ.
- The dated file URL changes monthly. Resolve it from the NKOD distribution or the ERÚ open-data page.
- Wiki pages read: Tag:power=plant (generators under 1 MW should not be power=plant; use power=generator; plant:output:* recommended), Key:plant:source, Tag:power=generator, Tag:plant:method=anaerobic_digestion.
- Not in covered.md. "vodnimlyny.cz" on the known list is a heritage mills site, not this.

## Wiki entry
```
===Výrobny elektřiny (ERÚ)===
* dataset: Technologická energetická zařízení – výrobny elektřiny
* gestor: [https://eru.gov.cz/ Energetický regulační úřad]
* licence: neobsahuje autorská díla, není chráněnou databází (CC0) [https://data.gov.cz/zdroj/datové-sady/70894451/1713221853]
* datové primitivy: body (pouze katastrální území + parcelní číslo, u vodních elektráren tok + říční km)
* odkaz: https://eru.gov.cz/sites/default/files/obsah/prilohy/tez-sk-11-2026-09-01.xml
* navržený tag {{tag|power|plant}} / {{tag|power|generator}}, {{tag|plant:source|hydro}}, {{tag|plant:output:electricity|<MW>}}, {{tag|ref:CZ:eru|<PremiseElecId>}}
* poznámka: ERÚ eviduje 1 605 vodních elektráren a ~420 bioplynových stanic, v OSM je jen ~500 vodních a ~32 bioplynových objektů
```
