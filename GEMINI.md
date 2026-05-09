# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

**SPQR: El Amanecer de Roma** — a Hearts of Iron IV mod set in ~264 BCE (First Punic War era). It replaces HoI4's WW2 setting with the ancient Mediterranean world. Targets HoI4 v1.18.*.

The mod has no build system, linter, or test runner. Development means editing plain-text Paradox script files and testing in-game.

## Mod Structure

Follows the standard HoI4 mod layout. Key areas:

- `common/country_tags/spqr_tags.txt` — all playable nation tags
- `common/countries/` — color/graphical culture per country (2-line files)
- `common/national_focus/` — focus trees (one per major nation + `min_regional.txt` for minors)
- `common/technologies/infantry.txt` — all ancient unit tech trees (3,580 lines)
- `common/units/spqr_ancient_land_units.txt` — unit type definitions
- `common/decisions/` — slave labor mechanic
- `common/scripted_effects/` — reusable effect blocks
- `history/countries/` — country setup (capital, OOB, leaders, government, techs)
- `history/states/` — ~1,000+ state definitions with ownership/provinces
- `history/units/` — order-of-battle files per country
- `localisation/english/` and `localisation/spanish/` — all display strings
- `gfx/leaders/{TAG}/` — leader portrait `.tga` files
- `tools/` — shell scripts for generating wasteland states and leader portrait assets

## Active Nations (15 tags)

| Tag | Country |
|-----|---------|
| SPQ | Rome |
| CRG | Carthage |
| MCD | Macedonia |
| KMT | Ptolemaic Egypt |
| SEL | Seleucid Empire |
| SYC | Syracuse |
| GRC | Achaean League |
| LAC | Sparta |
| SMN | Samnium |
| PHN | Mauretania |
| IBR | Iberia |
| GLN | Gauls |
| ILL | Illyria |
| THR | Thrace |
| WLD | Wasteland |

**Removed/deprecated tags** (do not re-add): ASS (Assyria), LYD (Lydia), SBN (Sabines), ETR (Etruria). These were removed for historical inaccuracy relative to 264 BCE. They may still appear commented out in focus trees.

## File Naming Conventions

- Country definition: `common/countries/{CountryName}.txt`
- Country history: `history/countries/{TAG} - {CountryName}.txt`
- Unit OOB: `history/units/{TAG}_1936.txt`
- Focus trees: `common/national_focus/{tag}_{theme}.txt` (e.g., `spq_republic.txt`, `min_regional.txt`)
- States: `history/states/{number}-{RegionName}.txt`
- Events: `events/spqr_{theme}.txt` or `events/spq_{theme}.txt`
- Localisation: `localisation/{lang}/spqr_{feature}_l_{lang}.yml`

## Key Patterns

**Country history files** (`history/countries/`) always set:
```
capital = {state_id}
oob = "{TAG}_1936"
set_research_slots = 3
set_politics = { ruling_party = neutrality; elections_allowed = no }
set_popularities = { neutrality = 100 }
```

**Localisation** requires entries for all ideology variants and the adjective:
```yaml
TAG: "Name"
TAG_neutrality: "..."
TAG_neutrality_DEF: "The ..."
TAG_fascism: "..."
TAG_fascism_DEF: "..."
TAG_democratic: "..."
TAG_democratic_DEF: "..."
TAG_communism: "..."
TAG_communism_DEF: "..."
TAG_ADJ: "Adjective"
```
Both `localisation/english/` and `localisation/spanish/` files must be updated together.

**Focus trees** use country gating:
```
country = { factor = 0; modifier = { add = 10; tag = TAG } }
```

**Minor nations** share `min_regional.txt` rather than having individual focus trees.

## Historical Constraints

- Timeline is ~264 BCE. All content must be historically plausible for that era.
- Do not add nations that did not exist as independent polities in 264 BCE.
- The descriptor replaces HoI4's bookmarks system entirely (`replace_path="common/bookmarks"`).

## Tools

```bash
tools/generate_wasteland_states.sh    # Generate WLD state definitions
tools/generate_leader_portraits.sh    # Batch-generate portrait asset stubs
```
