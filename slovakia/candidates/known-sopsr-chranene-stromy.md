# Chránené stromy: ŠOP SR register of protected trees (update of the 2008 import)

| Field | Value |
|---|---|
| publisher | Štátna ochrana prírody Slovenskej republiky (ŠOP SR), Banská Bystrica |
| url | WFS 2.0: `https://www.sopsr.sk/geoserver/chranene_objekty/ows?service=WFS&version=2.0.0&request=GetFeature&typeNames=chranene_objekty:chranene_stromy&outputFormat=application/json&srsName=EPSG:4326` (also `chranene_objekty:chranene_stromy_stzoz`, one point per tree with declaration data); capabilities `https://www.sopsr.sk/geoserver/chranene_objekty/chranene_stromy/ows?service=WFS&version=2.0.0&request=GetCapabilities`; catalogue https://data.gov.sk/set/afbc398a44c9c298146b94ebdd432e6b , metadata https://rpi.gov.sk/metadata/c3dda821-2cf6-4fce-8231-198126d1fb00 |
| format | GeoServer WFS (GeoJSON output), WMS |
| coords | yes (points, 4 decimal places ≈ 7–11 m) |
| records | 1,199 tree points in 438 protected objects (`chranene_stromy`), 1,228 points in 445 objects in `chranene_stromy_stzoz` (fetched 30 Sep 2026). in `stzoz`, 470 per-tree records have a declaration dated after 2008 (93 in 2021, 118 in 2022, 189 in 2023, 65 in 2024) |
| osm_tags | `natural=tree` + `denotation=natural_monument` + `protected=yes`, `name` (the object name), `species:sk`/`species`; suggested `ref:sopsr=<Cislo_statneho_zoznamu>` (state-list number; not in use yet, taginfo 0). Checked against Tag:denotation=natural_monument and Tag:natural=tree (wiki, raw, 30 Sep 2026) |
| osm_count_sk | `denotation=natural_monument` 281; 1,204 nodes with `import_ref=sk_sopsr_chs_2008` (the 2008 import), of which 22 have a `name`; `ref:sopsr` 0 (taginfo and Postpass, 30 Sep 2026). 335 of the 1,199 register trees have no OSM protected/imported tree within 30 m, 223 none within 100 m (111 protected objects). 254 of the 1,204 imported 2008 nodes have no register tree within 100 m |
| license | CC BY 4.0 for author's work, database and sui generis right (national catalogue terms of use). The 2008 import carries `source=(C)2008 Štátna ochrana prírody SR Banská Bystrica www.sopsr.sk`, so data was given to OSM then; that permission is not on `WikiProject Slovakia/Sources` |
| license_url | https://data.gov.sk/set/afbc398a44c9c298146b94ebdd432e6b ; https://creativecommons.org/licenses/by/4.0/ |
| license_status | needs_waiver |
| update_freq | continuous (the register follows new declarations by okresné úrady; data includes 2024 decrees) |
| impact | 3 |
| sync_fit | Sync (points, one tag set 1:1, stable state-list number + tree number; update the existing 2008 nodes with the ref and name, add the ~220 missing trees, flag the ~250 orphaned nodes for review) |
| verified | yes |

## Try it

- **Map preview:** [../samples/known-sopsr-chranene-stromy.geojson](../samples/known-sopsr-chranene-stromy.geojson) has all 1,199 register trees with name, species, number of trees, location text, the link to the state list and `osm_protected_tree_30m` (false for 335).
- **QGIS:** *Layer → Add Layer → Add WFS Layer…*, new connection `https://www.sopsr.sk/geoserver/chranene_objekty/ows`, add `Chránené stromy`. QGIS's own user agent is accepted; plain `curl` without a browser-like `User-Agent` gets `403 Forbidden` from this server.
- **Web:** https://www.sopsr.sk/chranene-uzemia-a-chranene-stromy/vyhladavanie-chranenych-uzemi-a-chranenych-stromov/ ; each feature's `Odkaz_na_statny_zoznam` points to `http://data.sopsr.sk/chranene-objekty/chranene-stromy/detail/<number>` (that host answered 503 on 30 Sep 2026).

## Notes

Known (OSM import `import_ref=sk_sopsr_chs_2008`, 1,204 nodes in OSM; not listed on `WikiProject Slovakia/Sources` or in known-sources) — adds: a stable state-list ID for every tree, names (only 22 of the imported nodes have one), the trees declared or re-declared since 2008 (470 records dated 2009–2024), and a way to find the imported trees that are no longer protected.

- **Attributes.** `Cislo_statneho_zoznamu` (state-list number, 438 distinct), `Poradove_cislo_stromu` (tree number within the object), `Pocet_stromov`, `Nazov_chraneneho_stromu`, `Lokalita`, `Dovod_ochrany`, `Typ_ochranneho_pasma`, `Druh` (Slovak species name), `Odkaz_na_statny_zoznam`. The `stzoz` layer adds the declaring decree (`orgvyhl_cisvyhl`, `datvyhl`) and S-JTSK coordinates.
- **What the 2008 import has.** `natural=tree`, `protected=yes`, `species`, `species:sk`, `description` (holding the object name, not `name`), `sopsr:count`, `denotation` on only 205 of them. So a Sync run would move `description` to `name`, add `denotation=natural_monument` and the ref.
- **Orphans.** 254 imported nodes have no current register tree within 100 m. Some trees died or were de-listed, some were moved when re-declared under the new decrees (2021–2024). They need a human check, not deletion.
- **Other trees.** Košice ("Chránené stromy na území Košíc") and Trnava region ("Chránené stromy v TTSK ŠOPSR") republish subsets of the same register in the catalogue; this national WFS supersedes them. Bratislava's tree passport is a separate topic.
- **ZBGIS overlap.** ZBGIS `EC030 Strom` has the category "Chránený strom" and an attribute `H_IDENTIF` "Jednoznačný identifikátor objektov v správe MŽP SR (pr. hydronyma, číslo stromu)", so ZBGIS copies the same register. The register is the primary source and is fresher.
- **Same publisher, other layers.** The `chranene_objekty` workspace also has the protected-area layers (known: reimported 2022) and `zachranne_stanice`, which are catchment polygons of wildlife rescue stations, not station points.
- Contact: ŠOP SR, https://www.sopsr.sk/kontakt/kontakt-sop-sr/ ; ŠOP SR already provided protected-area data for OSM in 2022 (known-sources), so the same contact route may work.

## Wiki entry

```
=== Chránené stromy (ŠOP SR) – aktualizácia importu z roku 2008 ===
* dataset: Chránené stromy
* správca: [https://www.sopsr.sk/ Štátna ochrana prírody SR]
* licencia: CC BY 4.0 [https://data.gov.sk/set/afbc398a44c9c298146b94ebdd432e6b]
* dátové primitívy: body
* odkaz: https://www.sopsr.sk/geoserver/chranene_objekty/ows?service=WFS&version=2.0.0&request=GetFeature&typeNames=chranene_objekty:chranene_stromy&outputFormat=application/json
* navrhované značky: {{tag|natural|tree}} + {{tag|denotation|natural_monument}} + {{tag|protected|yes}}, {{tag|ref:sopsr|<číslo štátneho zoznamu>}}
* poznámka: import z roku 2008 (1 204 bodov) nemá ID ani názvy; 223 stromov z registra nemá v OSM chránený strom do 100 m a 254 importovaných bodov už v registri nie je.
```
