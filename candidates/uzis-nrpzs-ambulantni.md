```
name: NRPZS – Místa poskytování zdravotních služeb (outpatient practices: dentists, GPs, specialists, opticians, physio)
publisher: Ministerstvo zdravotnictví / ÚZIS ČR (NKOD publisher 00024341)
url: https://datanzis.uzis.gov.cz/data/NR-01-NRPZS/NR-01-06/Otevrena-data-NR-01-06-nrpzs-mista-poskytovani-zdravotnich-sluzeb.csv (NKOD: https://data.gov.cz/zdroj/datové-sady/00024341/aa4c99d9f1480cca59807389cf88d4dc)
format: CSV (UTF-8, ~28 MB)
coords: yes (ZZ_GPS as "POINT(lat lon)" – note lat/lon order is swapped vs WKT convention) + ZZ_RUIAN_kod (RÚIAN address point code) on 40,807 rows
records: 40,870 places (unique ZZ_ID); relevant subsets: specialist practice 10,745; dentist (PL-stomatolog) 5,598; GP adults 5,319; GP children 1,969; gynaecologist 1,627; physiotherapist 2,706; optician 956; psychologist 697; speech therapist 606; dental lab 1,403 (not a POI)
osm_tags: amenity=dentist + healthcare=dentist; amenity=doctors + healthcare=doctor + healthcare:speciality=general|paediatrics|gynaecology|<specialty>; healthcare=physiotherapist; shop=optician; ref:CZ:uzis=<ZZ_ID> (to be confirmed – same key as ZABAGED import)
osm_count_cz: amenity=dentist 585, healthcare=dentist 537; amenity=doctors 1,476; healthcare=doctor 1,195; healthcare:speciality=general 198; healthcare=physiotherapist 71; shop=optician 608; ref:CZ:uzis 0
license: CC BY 4.0 (authors listed as Zelinková H., Klimeš D., Šnábl I., Májek T., Jarkovský J., et al.); not a protected database, no sui generis right, no personal data (per NKOD)
license_url: https://creativecommons.org/licenses/by/4.0/
license_status: needs_waiver
update_freq: monthly
impact: 4
verified: yes
```

## Notes
- Scope versus covered.md: the ZABAGED POI import (Cs:POI_ZABAGED_Import §13, ZdravotnickeZarizeniDefinicniBod) covers ÚZIS *facilities* only: hospitals, polyclinics ("poskytovatel amb. služeb", "zdravotnické středisko", "sdružení 4 a více lékařů"), hospices, LDN and similar. Per the wiki, its healthcare layer is "not imported due to tagging diversity". Single-doctor practices (samostatné ordinace), which make up most of NRPZS, are NOT in that list. Pharmacies are better sourced from SÚKL (see sukl-lekarny.md).
- Gap (Postpass, 50 random samples each, OSM feature of the matching kind within 75 m): dentists 6/50 (12%), so about 4,900 are missing; GPs 18/50 (36%, and many hits are the polyclinic building, not the practice), so about 3,400+ missing; specialists 26/50 (mostly polyclinic hits); physiotherapists 12/50; opticians 24/50.
- Caveats:
  - Many practices share one building (polyclinic, health centre). Import them as nodes inside the building, or aggregate them onto an amenity=clinic, following local convention. The coordinates are geocoded to the RÚIAN address point, so stacked duplicates will be common.
  - ZZ_nazev is often the doctor's personal name, e.g. "MUDr. Jan Novák". That is legally public register data, but think about name= policy; some communities use a practice name instead.
  - The rows are "místa poskytování" (places of care). Home care (domácí péče) and ambulance/transport rows have no public POI and must be filtered out.
  - The obor/forma fields map to healthcare:speciality. A mapping table is needed.
- License: CC BY 4.0 needs an explicit waiver of the attribution and DRM clauses for OSM per LWG guidance. ÚZIS/MZ is a state body and the NRPZS register is kept under zákon 372/2011 Sb. §77, but "úřední dílo" (§3 AZ) applies to legal and official texts, not clearly to register extracts. Since NKOD itself states "not a protected database, no sui generis right", the only claimed right is the CC BY on "autorské dílo", which is arguably void for factual data. Still, ask ÚZIS for explicit consent, as was done with ČÚZK. ÚZIS already consented to the ZABAGED channel, which may make this easier.
- Suggested ref: reuse ref:CZ:uzis if ZABAGED id_uzis equals NRPZS ZZ_ID (not verified: ref:CZ:uzis currently has 0 uses in OSM). Otherwise use ref:CZ:nrpzs=<ZZ_ID>.
- Wiki pages read: Tag:amenity=dentist (healthcare=dentist combination), Tag:amenity=doctors (healthcare=doctor, healthcare:speciality; amenity=clinic for larger facilities), Key:healthcare, Key:healthcare:speciality.
- Contact: ÚZIS ČR, NZIS open data, https://datanzis.uzis.gov.cz/ (NRPZS: https://nrpzs.uzis.cz/).
- Regional subsets (Královéhradecký kraj "Zubní lékaři" on datakhk.cz, NKOD terms "neobsahuje autorská díla") are CC0-like and could serve as a license-clean pilot for the KHK region only.
