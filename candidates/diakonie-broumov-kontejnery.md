# Diakonie Broumov – textile collection containers (address list, placed via RÚIAN)

| Field | Value |
|---|---|
| publisher | Diakonie Broumov, sociální družstvo (Husova 319, Broumov; web https://diakoniebroumov.org/) |
| url | https://diakoniebroumov.org/sberne-kontejnery/ (one HTML table, "Seznam sběrných kontejnerů") |
| format | HTML table: container type, municipality (Obec), street or part of municipality (Ulice), house number (Číslo popisné), postcode (PSC) |
| coords | address-only; 752 of 889 rows placed on a RÚIAN address point (681 unambiguously) |
| records | 889 rows (2026-09-28): 696 KTM (small container), 156 KTV (large), 14 KTS (medium), 12 SD (collection yard), 6 KTV at a collection yard, 2 KTZ (bell), 2 KLEC (textile cage), 1 LTM; spread over the whole country, mostly small municipalities |
| osm_tags | amenity=recycling + recycling_type=container + recycling:clothes=yes + operator=Diakonie Broumov (the form already used on 20 OSM objects). Wiki Tag:amenity=recycling (approved; lists `operator`), Key:recycling:clothes (de facto, clothes including shoes), Key:recycling_type – same pages as cited in textil-kontejnery-kloktex-potex.md |
| osm_count_cz | taginfo Geofabrik CZ (2026-09-28): recycling:clothes=yes 4,564. Postpass (2026-09-28, CZ bbox): 24 amenity=recycling objects with an operator containing "Diakonie" (20 × "Diakonie Broumov") |
| license | none stated |
| license_url | none |
| license_status | unclear |
| update_freq | maintained by the operator on its website (no date on the page) |
| impact | 3 |
| sync_fit | MapRoulette (address-point positions must be moved to the container on imagery or survey; 183 cases are attribute-only: add recycling:clothes=yes + operator to an existing recycling point) |
| verified | yes |

## Try it
- **Map preview:** none (licence unclear).
- **Web viewer:** https://diakoniebroumov.org/sberne-kontejnery/ (table only, no map).
- **QGIS:** the page is a plain HTML table, not a data endpoint. Extract it to CSV with
  `curl -s https://diakoniebroumov.org/sberne-kontejnery/ | python3 -c "import re,sys,html,csv;w=csv.writer(sys.stdout);[w.writerow([html.unescape(re.sub('<[^>]+>','',c)).strip() for c in re.findall(r'<td[^>]*>(.*?)</td>',r,re.S)]) for r in re.findall(r'<tr[^>]*>(.*?)</tr>',sys.stdin.read(),re.S)]" > dbk.csv`
  (tested 2026-09-28: 889 data rows with 5 columns). There are no coordinates; to place the rows, query the RÚIAN
  address-point layer `https://ags.cuzk.gov.cz/arcgis/rest/services/RUIAN/Prohlizeci_sluzba_nad_daty_RUIAN/MapServer/1/query`
  with `where=psc=<PSC> AND cislodomovni=<number>`, `outFields=kod,adresa`, `outSR=4326`, `f=json`, and keep the
  candidate whose `adresa` contains the Ulice value (tested: `psc=41108 AND cislodomovni=5` returns
  "Předonín 5, 41108 Bechlín", kod 16619391). In QGIS the resulting CSV is added via *Layer → Add Layer → Add
  Delimited Text Layer* with X = lon, Y = lat, EPSG:4326.

## Notes
- **Geocoding (2026-09-28):** of 889 rows, 18 have no usable house number/postcode, 22 have no RÚIAN address with
  that postcode and house number, 97 have candidates none of which names the given street. 681 rows resolved to a
  single address point (603 by postcode + house number + street/part name, 78 where postcode + house number is
  unique); 71 more resolved to several address points with the same name and number (first one kept, flagged
  ambiguous). The house number is sometimes an orientation number or a nearby building, so positions are
  "at the address", typically a municipal office, shop or school yard, not the container itself.
- **Gap analysis** with Postpass (2026-09-28, all amenity=recycling in the CZ bbox, 50,557 objects), 742 placed
  containers excluding the pure collection-yard rows, radius 100 m around the address point (generous because of
  the address-level position):
  - 157 (21 %) have an amenity=recycling with recycling:clothes=yes within 100 m; only 9 of those carry a
    Diakonie operator tag, 142 have no operator.
  - 196 (26 %) have an amenity=recycling within 100 m that lacks the clothes attribute – candidates for adding
    recycling:clothes=yes + operator after checking imagery.
  - 389 (52 %) have no recycling object at all within 100 m. Restricted to the 681 unambiguous rows: 336 none,
    183 recycling without clothes, 152 with clothes.
  - Most missing in Praha 5 (13), Sedlčany (10), Paskov (9), Otrokovice (6), Praha 9 (6), Velká Losenice (6).
- There is no container ID in the table, only the address, so ongoing sync is not realistic; this is a one-off
  MapRoulette challenge (the RÚIAN address code can serve as the task ID, not as an OSM tag).
- Not listed on Cs:Česko/freemap (incl. Potencionální zdroje), Cs:Zdroje_v_jednani or in Sync config.toml
  (checked 2026-09-28 against the saved copies).
- Contact: diakonie@diakoniebroumov.org. The operator may have container GPS positions internally (the collection
  route needs them); ask for those together with an OSM consent.
- Related: KlokTex and Potex containers in textil-kontejnery-kloktex-potex.md.

## Wiki entry
```
===Diakonie Broumov – sběrné kontejnery na textil===
* dataset: Seznam sběrných kontejnerů
* gestor: [https://diakoniebroumov.org/ Diakonie Broumov, sociální družstvo]
* licence: neuvedena, nutno požádat o souhlas
* datové primitivy: body (jen adresy, lze umístit na adresní místa RÚIAN)
* odkaz: https://diakoniebroumov.org/sberne-kontejnery/
* navržený tag {{tag|amenity|recycling}}, {{tag|recycling_type|container}}, {{tag|recycling:clothes|yes}}, {{tag|operator|Diakonie Broumov}}
* poznámka: u 585 z 742 kontejnerů umístěných na adresu není v OSM do 100 m sběrné místo s recycling:clothes=yes, u 389 žádné sběrné místo
```
