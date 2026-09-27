```
name: Významné geologické lokality v ČR – výběr nejzajímavějších (significant geological sites)
publisher: Česká geologická služba (ČGS), IČO 00025798
url: https://od.geology.cz/lokality.zip (lokality_body.geojson + lokality_plochy.geojson); NKOD https://data.gov.cz/zdroj/datové-sady/00025798/b1dc60a0b1c8ef92b26f90426d2f88e4 ; detail pages https://lokality.geology.cz/<id>
format: GeoJSON (WGS84)
coords: yes (points and polygons)
records: 584 points + 1,010 polygons = 1,594 sites (files dated 2025-12-11)
osm_tags: depends on type: geological=outcrop / geological=palaeontological_site / natural=rock|stone|cliff / landuse=quarry (+ disused), name, description; suggested ref:cgs:lokality=<id>
osm_count_cz: geological=* 71 (outcrop 19, palaeontological_site 21, volcanic_mofetta 14, columnar_jointing 6); natural=rock 2,659; landuse=quarry 1,246 (taginfo 2026-09-26)
license: CC BY 4.0 (NKOD terms spec: autorské dílo + DB as copyright work CC BY 4.0, no sui generis right)
license_url: https://data.gov.cz/zdroj/datové-sady/00025798/b1dc60a0b1c8ef92b26f90426d2f88e4
license_status: needs_waiver
update_freq: weekly per NKOD (actual file date 2025-12-11)
impact: 2
verified: yes
```

## Notes
- **Contents.** Each site has `id`, `nazev`, `technicke_prvky` (e.g. "lom"), `pristup` (access description), `charakt`, `abstract_cz`, `geologicka_charakteristika`, `url`. Many are quarries, rock outcrops, road cuts, fossil sites and volcanic features. Text fields are long descriptive prose, which is copyrightable and should not go into OSM.
- **Gap.** OSM hardly uses the `geological=*` key (71 in CZ). Many sites exist in OSM as a quarry, rock or cliff without a geological tag or name. Value: adding names and `geological=*` to about 1,600 notable sites that interest hikers and geotourists. The sites are few and the tagging is heterogeneous, so this is a manual/MapRoulette-style task, not a bulk import.
- **Tagging.** Read Key:geological and Tag:geological=outcrop (raw, 2026-09-27). Outcrop is for exposed bedrock and is "in use". Polygons often outline whole quarries: tag an existing `landuse=quarry` instead of adding new areas.
- **Licence.** NKOD distribution spec checked 2026-09-27: CC BY 4.0. The descriptive texts are authored works, so take only name, type and geometry.
- Related: AOPK "Geoparky" (NKOD) and ČGS mine workings (see cgs-dulni-dila.md).

## Wiki entry
```
===Významné geologické lokality (ČGS)===
* dataset: Významné geologické lokality v České republice – výběr nejzajímavějších
* gestor: [https://www.geology.cz/ Česká geologická služba]
* licence: CC BY 4.0 [https://data.gov.cz/zdroj/datové-sady/00025798/b1dc60a0b1c8ef92b26f90426d2f88e4] – nutný souhlas pro OSM
* datové primitivy: body, plochy
* odkaz: https://od.geology.cz/lokality.zip
* navržený tag {{tag|geological|outcrop}}, {{tag|geological|palaeontological_site}}, {{tag|ref:cgs:lokality|<id>}}
* poznámka: 1 594 lokalit; klíč geological=* je v OSM použit jen 71×, vhodné spíše pro ruční doplnění názvů a typů
```
