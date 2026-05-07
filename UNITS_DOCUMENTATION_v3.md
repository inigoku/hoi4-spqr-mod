# SPQR Mod - Units Documentation v3

Documentación completa de todas las unidades disponibles en el mod SPQR. Este documento detalla estadísticas, restricciones, requisitos tecnológicos y roles estratégicos de cada unidad.

> **Notas de revisión v3:** Se añade la nueva unidad **Royal Guard (GRD)** — Guardia Real, disponible para todos los países con nombres históricos únicos por facción. Rol de supresión, guarnición y defensa urbana, complementario a Hastati. Ver sección [Registro de Cambios v3](#registro-de-cambios-v3) al final.

---

## Tabla Resumen de Unidades

| Tipo | Abrev. | Clasificación | Disponible | Tech Base | Tech +1 | Tech +2 | Notas |
|------|--------|---------------|-----------|-----------|---------|---------|-------|
| **Levy** | LEV | Infantería Conscripta | TODOS | `levy` | `levy2` | `levy3` | Conscriptos, entrenamiento rápido |
| **Infantry** | INF | Infantería Regular | TODOS | N/A | N/A | N/A | Veterana, disponible al inicio |
| **Hastati** | HAS | Infantería Elite | SPQ | `roman_legion` | `roman_legion1` | `roman_legion2` | Solo Roma — Primera línea de batalla |
| **Marine** | MRN | Infantería Especializada | TODOS | `marines` | `marines2` | `marines3` | Operaciones anfibias |
| **Speculatores** | SPE | Infantería de Infiltración | SPQ | `paratroopers` | `paratroopers2` | `paratroopers3` | Solo Roma, desembarque aéreo/infiltración |
| **Royal Guard** | GRD | Infantería de Elite / Guarnición | TODOS | `royal_guard` | `royal_guard1` | `royal_guard2` | Máxima supresión y defensa urbana |
| **Light Armor** | LT | Caballería Ligera | TODOS | N/A | N/A | N/A | Disponible al inicio |
| **Heavy Armor** | HV | Caballería Pesada | TODOS | N/A | N/A | N/A | Disponible al inicio |
| **War Elephant** | ELP | Caballería Especial | CRG | `war_elephant` | `war_elephant1` | `war_elephant2` | Solo Cartago |
| **Heavy Chariot** | CHR | Caballería Especial | ASS | `heavy_chariot` | `heavy_chariot1` | `heavy_chariot2` | Solo Asiria |

> ⚠️ **Cambios respecto a v1:** La abreviatura de Hastati pasa de `LEG` a `HAS`. Paratrooper se renombra a **Speculatores (SPE)**. En v3 se añade **Royal Guard (GRD)**, disponible para todos los países.

---

## Unidades de Infantería

### 1. Levy (LEV) — Infantería Conscripta

**Clasificación:** Infantería conscripta, reclutamiento masivo
**Disponibilidad:** TODOS los países
**Restricción Tecnológica:** Ninguna (investigable por todos)

#### Localización

| País | Código | Inglés | Español |
|------|--------|--------|---------|
| **Default** | — | Conscripts | Conscriptos |
| 🇷🇴 Roma | SPQ | Velites | Velites |
| 🇬🇷 Grecia | GRC | Thetes | Thetes |
| 🐘 Cartago | CRG | Libyan Conscripts | Conscriptos Libios |
| 🇲🇰 Macedonia | MCD | Macedonian Peltasts | Peltastas Macedonios |
| ⚔️ Asiria | ASS | Assyrian Conscripts | Conscriptos Asirios |
| 🇪🇬 Egipto | KMT | Egyptian Conscripts | Conscriptos Egipcios |

> ⚠️ **Añadido en v2:** La v1 no definía nombres por país para Levy. Se añaden aquí con criterio histórico:
> - **Velites** — infantería ligera romana de clase baja, histórica primera línea desechable.
> - **Thetes** — clase ateniense más baja, base de los remeros y conscriptos.
> - **Peltastas** — infantería ligera con escudo de mimbre, característicos del mundo macedonio-tracio.

#### Estadísticas
| Stat | Valor | vs. Infantry | vs. Hastati |
|------|-------|-------------|-----------------|
| **Manpower** | 800 | -20% | -33% |
| **Equipment** | 80 inf_eq | -20% | -33% |
| **Training Time** | 60 días | -33% | -40% |
| **Max Strength** | 20 | -20% | -33% |
| **Max Organization** | 60 | -8% | -17% |
| **Morale** | 0.25 | -17% | -38% |
| **Suppression** | 1.0 | -29% | -38% |
| **Supply Consumption** | 0.045 | -18% | -31% |
| **Weight** | 0.45 | -10% | -18% |

#### Ventajas
- ✅ Entrenamiento muy rápido (60 días)
- ✅ Bajo costo de recursos y manpower
- ✅ Bajo consumo de suministros
- ✅ Ideal para refuerzos rápidos

#### Desventajas
- ❌ Baja moral y organización
- ❌ Débil en combate directo
- ❌ Baja capacidad de supresión
- ❌ Sufre penalización en terreno difícil

#### Rol Estratégico
Unidades de reclutamiento masivo para guerra de attrición. Usarlas como base de tropas o para mantener líneas defensivas. Ideales en fases iniciales de guerra cuando hay pocos recursos.

#### Tecnología
- **Tier 1:** `levy` (1936) — Habilita la unidad
- **Tier 2:** `levy2` (1939) — +3 máxima organización, +0.05 ataque blando
- **Tier 3:** `levy3` (1943) — +3 máxima organización, +0.05 ataque blando

---

### 2. Infantry (INF) — Infantería Regular

**Clasificación:** Infantería veterana y entrenada
**Disponibilidad:** TODOS los países
**Restricción Tecnológica:** Ninguna (disponible al inicio)

#### Localización

| País | Código | Inglés | Español |
|------|--------|--------|---------|
| **Default** | — | Warriors | Guerreros |
| 🇷🇴 Roma | SPQ | Roman Legionarii | Legionario Romano |
| 🇬🇷 Grecia | GRC | Hoplites | Hoplitas |
| 🐘 Cartago | CRG | Liby-Phoenician Infantry | Infantería Líbio-Fenicia |
| 🇲🇰 Macedonia | MCD | Pezhetairoi | Pezhetairoi |
| ⚔️ Asiria | ASS | Kisir Šarri | Tropas Reales Asirias |
| 🇪🇬 Egipto | KMT | Machimoi | Machimoi |

> ⚠️ **Cambios respecto a v1:**
> - **Default:** "Legionarii" → "Warriors". El nombre por defecto era específicamente romano, inadecuado como genérico.
> - **CRG:** "African Infantry" → "Liby-Phoenician Infantry". Más preciso históricamente: el núcleo del ejército cartaginés eran mercenarios y aliados líbio-fenicios.
> - **ASS:** "Assyrian Infantry" → "Kisir Šarri" (tropas del rey). Término acadio para la guardia real/infantería profesional asiria.
> - **KMT:** "Ptolemaic Infantry" → "Machimoi". Clase guerrera egipcia institucionalizada bajo los Ptolemaicos; es el término técnico correcto.

#### Estadísticas
| Stat | Valor | vs. Levy | vs. Hastati |
|------|-------|---------|-----------------|
| **Manpower** | 1000 | +25% | -17% |
| **Equipment** | 100 inf_eq | +25% | -17% |
| **Training Time** | 90 días | +50% | -10% |
| **Max Strength** | 25 | +25% | -17% |
| **Max Organization** | 65 | +8% | -10% |
| **Morale** | 0.3 | +20% | -25% |
| **Suppression** | 1.4 | +40% | -13% |
| **Supply Consumption** | 0.055 | +22% | -15% |
| **Weight** | 0.5 | +11% | -9% |

#### Ventajas
- ✅ Balance equilibrado entre coste y efectividad
- ✅ Disponible sin investigación
- ✅ Buen ratio manpower/rendimiento
- ✅ Supresión decente

#### Desventajas
- ❌ Inferior a los Hastati en combate
- ❌ Sin bonificaciones de terreno
- ❌ Entrenamiento más lento que Levy

#### Rol Estratégico
Unidad estándar de infantería para la mayoría de países. Base sólida para formaciones defensivas. Combina coste razonable con capacidades efectivas. Usarla como estructura central del ejército.

#### Bonificaciones de Terreno
Ninguna especial (es la unidad base de comparación).

---

### 3. Hastati (HAS) — Infantería Elite Romana

**Clasificación:** Primera línea de batalla romana, infantería profesional y altamente entrenada
**Disponibilidad:** 🇷🇴 **SPQ (Roma) SOLO**
**Restricción Tecnológica:** `allow = { tag = SPQ }` en todas las tecnologías

#### Nota Histórica
Los **Hastati** eran la primera línea de la legión romana manipular, compuestos por soldados jóvenes pero bien equipados con pilum y scutum. En el contexto del mod representan la elite de combate romana profesional.

> ⚠️ **Nota de diseño:** Históricamente los Hastati eran la línea *menos* veterana (detrás de los Príncipes y Triarii). En el mod se usan como nombre para la unidad elite romana de forma estilística. Si se prefiere mayor rigor histórico, el nombre alternativo sería **Legio** o **Triarii**.

#### Localización

| País | Código | Inglés | Español |
|------|--------|--------|---------|
| 🇷🇴 Roma | SPQ | Hastati | Hastati |

*Nota: Única para Roma, restricción tecnológica exclusiva.*

#### Estadísticas
| Stat | Valor | vs. Infantry | vs. Levy |
|------|-------|-------------|---------|
| **Manpower** | 1200 | +20% | +50% |
| **Equipment** | 120 inf_eq | +20% | +50% |
| **Training Time** | 100 días | +11% | +67% |
| **Max Strength** | 30 | +20% | +50% |
| **Max Organization** | 72 | +11% | +20% |
| **Morale** | 0.4 | +33% | +60% |
| **Suppression** | 1.6 | +14% | +60% |
| **Supply Consumption** | 0.065 | +18% | +44% |
| **Weight** | 0.55 | +10% | +22% |
| **Breakthrough** | 0.15 | Presente | Presente |

#### Bonificaciones de Terreno
| Terreno | Efecto |
|---------|--------|
| **Urban** | +10% ataque |
| **Forest** | +5% ataque, -5% movimiento |
| **River** | +5% ataque |

#### Ventajas
- ✅ Mejor unidad de infantería disponible
- ✅ Excelente en combate urbano (+10% ataque)
- ✅ Alta moral y organización
- ✅ Buen breakthrough para penetraciones
- ✅ Ventaja psicológica vs enemigos

#### Desventajas
- ❌ Solo disponible para Roma
- ❌ Costo elevado (120 equipo)
- ❌ Manpower alto (1200)
- ❌ Entrenamiento más lento

#### Rol Estratégico
Espina dorsal del ejército romano. Usar en operaciones ofensivas y defensa de ciudades. Ideal en Europa mediterránea (muchas ciudades). Unidad premium para Roma.

#### Tecnología
- **Tier 1:** `roman_legion` (1936) — Habilita la unidad (SPQ SOLO)
- **Tier 2:** `roman_legion1` (1939) — +0.05 ataque blando
- **Tier 3:** `roman_legion2` (1942) — +0.05 ataque blando, +3 máxima organización, +0.05 breakthrough

> ⚠️ **Corregido en v2:** En v1, Tier 1 y Tier 2 ambos figuraban en 1936. Se ha ajustado Tier 2 a 1939 y Tier 3 a 1942, en coherencia con el patrón del resto de tecnologías del mod.

---

### 4. Marine (MRN) — Infantería Naval Especializada

**Clasificación:** Infantería especializada en operaciones anfibias
**Disponibilidad:** TODOS los países
**Restricción Tecnológica:** Ninguna (investigable por todos)

#### Localización

| País | Código | Inglés | Español |
|------|--------|--------|---------|
| **Default** | — | Naval Infantry | Infantería Naval |
| 🇷🇴 Roma | SPQ | Classiarii | Classiarii |
| 🇬🇷 Grecia | GRC | Epibatai | Epibatai |
| 🐘 Cartago | CRG | Carthaginian Marines | Marines Cartagineses |
| 🇲🇰 Macedonia | MCD | Macedonian Marines | Marines Macedonios |
| ⚔️ Asiria | ASS | Assyrian Marines | Marines Asirios |
| 🇪🇬 Egipto | KMT | Ptolemaic Marines | Marines Ptolemaicos |

> ⚠️ **Cambios respecto a v1:**
> - **Default:** "Elite Legions" → "Naval Infantry". El nombre anterior era confuso y contradictorio (marines ≠ legiones).
> - **SPQ:** "Roman Praetorians" → "Classiarii". Los Classiarii eran la infantería naval romana real; los Pretorianos eran guardia imperial terrestre, categoría conceptualmente errónea para una unidad anfibia.
> - **GRC:** "Greek Marines" → "Epibatai". Término griego para los soldados embarcados en trirremes, históricamente preciso.
> - **KMT:** "Egyptian Marines" → "Ptolemaic Marines" / "Marines Ptolemaicos". Distingue el período histórico correcto.

#### Estadísticas
| Stat | Valor | vs. Infantry | vs. Levy |
|------|-------|-------------|---------|
| **Manpower** | 1000 | =0% | +25% |
| **Equipment** | 150 inf_eq | +50% | +88% |
| **Training Time** | 130 días | +44% | +117% |
| **Max Strength** | 20 | -20% | =0% |
| **Max Organization** | 75 | +15% | +25% |
| **Morale** | 0.4 | +33% | +60% |
| **Suppression** | 1.0 | -29% | =0% |
| **Supply Consumption** | 0.055 | =0% | +22% |
| **Breakthrough** | 0.4 | Presente (0.4) | Presente (0.4) |

#### Bonificaciones de Terreno (Especiales)
| Terreno | Efecto |
|---------|--------|
| **Amphibious** | +50% ataque (desembarques) |
| **River** | +30% ataque |
| **Marsh** | +30% ataque |

#### Ventajas
- ✅ Especialista en terreno acuático
- ✅ Bonus masivo en desembarques (+50%)
- ✅ Alta organización (75)
- ✅ Excelente en pantanos y ríos
- ✅ Alto breakthrough para penetraciones

#### Desventajas
- ❌ Muy costoso (150 equipo)
- ❌ Entrenamiento lento (130 días)
- ❌ Baja supresión
- ❌ Capacidades limitadas en tierra interior

#### Rol Estratégico
Para operaciones anfibias y conquista de zonas costeras/islas. Usar en desembarques coordinados. Especializada en el Mediterráneo. Menos útil en tierra interior.

#### Tecnología
- **Tier 1:** `marines` (1936) — Habilita la unidad
- **Tier 2:** `marines2` (1939) — +5 máxima organización, +0.05 ataque blando
- **Tier 3:** `marines3` (1943) — +5 máxima organización

---

### 5. Speculatores (SPE) — Infantería de Infiltración

**Clasificación:** Tropas especializadas en infiltración y operaciones secretas
**Disponibilidad:** 🇷🇴 **SPQ (Roma) SOLO**
**Restricción Tecnológica:** `allow = { tag = SPQ }` en tecnología `paratroopers`

> ⚠️ **Renombrado en v2:** La unidad se renombraba "Paratrooper (PAR)" en la tabla resumen, pero internamente ya se llamaba Speculatores en todas las localizaciones. Se unifica el nombre y la abreviatura pasa de `PAR` a `SPE` para coherencia.

#### Nota Histórica
Los **Speculatores** eran tropas especializadas romanas en exploración, espionaje y operaciones secretas detrás de líneas enemigas. El mecanismo de desembarco aéreo del juego representa su capacidad de infiltrarse en territorio hostil.

#### Localización

| País | Código | Inglés | Español |
|------|--------|--------|---------|
| **Default** | — | Speculatores | Especuladores |
| 🇷🇴 Roma | SPQ | Speculatores | Especuladores |
| 🇬🇷 Grecia | GRC | Greek Elite Hoplites | Hoplitas de Elite |
| 🐘 Cartago | CRG | Carthaginian Elite | Elite Cartaginesa |
| 🇲🇰 Macedonia | MCD | Macedonian Elite | Elite Macedonia |
| ⚔️ Asiria | ASS | Assyrian Elite | Elite Asiria |
| 🇪🇬 Egipto | KMT | Egyptian Elite | Elite Egipcia |

*Nota: Solo investigable por Roma, pero las localizaciones están definidas para todos los países por motivos técnicos.*

#### Estadísticas
| Stat | Valor | vs. Infantry | vs. Marine |
|------|-------|-------------|-----------|
| **Manpower** | 1000 | =0% | =0% |
| **Equipment** | 100 inf_eq | =0% | -33% |
| **Training Time** | 125 días | +39% | -4% |
| **Max Strength** | 22 | -12% | +10% |
| **Max Organization** | 65 | =0% | -13% |
| **Morale** | 0.35 | +17% | -13% |
| **Suppression** | 1.2 | -14% | +20% |
| **Special** | `special_forces = yes` | Sí | Sí |

#### Ventajas
- ✅ Desembarque aéreo directo (infiltración detrás de líneas)
- ✅ Unidad de fuerzas especiales
- ✅ Capacidad de aterrizaje en cualquier terreno
- ✅ Exclusiva de Roma (distinción táctica única)

#### Desventajas
- ❌ Requiere transporte aéreo
- ❌ Entrenamiento lento
- ❌ Capacidades limitadas sin apoyo aéreo
- ❌ Solo disponible para SPQ

#### Rol Estratégico
Operaciones detrás de líneas enemigas. Infiltración en territorio hostil. Requiere coordinación con aviación. Unidad premium para Roma.

#### Tecnología
- **Tier 1:** `paratroopers` (1936) — Habilita la unidad (SPQ SOLO)
- **Tier 2:** `paratroopers2` (1939) — +0.05 ataque blando, +3 máxima organización
- **Tier 3:** `paratroopers3` (1943) — +0.05 ataque blando, +3 máxima organización, +0.05 breakthrough

> ⚠️ **Corregido en v2:** La v1 no especificaba las bonificaciones concretas de Tier 2 y Tier 3 ("Mejoras a paratrooper" / "Mejoras adicionales"). Se han igualado al patrón del resto de unidades. Confirmar valores en el archivo `.txt` de tecnología antes de publicar.

---

### 6. Royal Guard (GRD) — Guardia Real

**Clasificación:** Infantería de elite — guarnición, supresión y defensa urbana
**Disponibilidad:** TODOS los países
**Restricción Tecnológica:** Investigable por todos (`royal_guard`)

#### Nota de Diseño
La Guardia Real cubre un rol que ninguna otra unidad ocupa: **supresión máxima y defensa de ciudades**. Es la antítesis táctica de los Hastati — donde estos atacan y rompen líneas, la Guardia sostiene, controla y no cede. Roma gana acceso a ambas, dándole una ventaja de versatilidad única. El resto de países tienen a la Guardia como su techo de infantería de elite.

#### Localización

| País | Código | Inglés | Español |
|------|--------|--------|---------|
| **Default** | — | Royal Guard | Guardia Real |
| 🇷🇴 Roma | SPQ | Praetorian Guard | Guardia Pretoriana |
| 🇬🇷 Grecia | GRC | Epilektoi | Epilektoi |
| 🐘 Cartago | CRG | Sacred Band | Banda Sagrada |
| 🇲🇰 Macedonia | MCD | Hypaspistai | Hypaspistai |
| ⚔️ Asiria | ASS | Kiṣir Šarrāni | Kiṣir Šarrāni |
| 🇪🇬 Egipto | KMT | Ptolemaic Agema | Agema Ptolemaico |

> **Notas históricas por facción:**
> - **Guardia Pretoriana** — guardia imperial romana, alta supresión, especializada en control político y urban warfare.
> - **Epilektoi** — «los elegidos», infantería selecta de las ciudades-estado griegas, reserva de elite.
> - **Banda Sagrada** (*Hieros Lochos*) — cuerpo de elite cartaginés de 2.500 hombres, inspirado en la Banda Sagrada tebana; su derrota en Crimiso (339 a.C.) marcó el declive de Cartago en Sicilia.
> - **Hypaspistai** — «portadores de escudo» de Alejandro Magno, elite de infantería de maniobra rápida; más tarde evolucionaron en los Argyraspides (escudos de plata).
> - **Kiṣir Šarrāni** — «tropa del rey», guardia personal real asiria, distinta del Kisir Šarri (tropa profesional regular).
> - **Agema Ptolemaico** — unidad de infantería de guardia ptolemaica, equivalente funcional a los Hypaspistai macedonios dentro del ejército helenístico de Egipto.

#### Estadísticas
| Stat | Valor | vs. Infantry | vs. Hastati |
|------|-------|-------------|------------|
| **Manpower** | 1000 | =0% | -17% |
| **Equipment** | 130 inf_eq | +30% | +8% |
| **Training Time** | 160 días | +78% | +60% |
| **Max Strength** | 28 | +12% | -7% |
| **Max Organization** | 80 | +23% | +11% |
| **Morale** | 0.5 | +67% | +25% |
| **Suppression** | 3.0 | +114% | +88% |
| **Supply Consumption** | 0.07 | +27% | +8% |
| **Weight** | 0.6 | +20% | +9% |
| **Breakthrough** | 0.05 | Bajo | Muy bajo |

#### Bonificaciones de Terreno
| Terreno | Efecto |
|---------|--------|
| **Urban** | +20% ataque, +15% defensa |
| **Fort** | +10% defensa |
| **Forest** | -10% ataque (no son tropas de campo) |
| **Marsh** | -15% ataque |

#### Ventajas
- ✅ Supresión más alta del juego (3.0)
- ✅ Moral máxima — prácticamente irrompible
- ✅ Dominante en combate urbano (+20/+15%)
- ✅ Máxima organización de toda la infantería (80)
- ✅ Disponible para todos los países
- ✅ Nombres históricos únicos por facción

#### Desventajas
- ❌ Breakthrough muy bajo (0.05) — no apta para ataque
- ❌ Entrenamiento lento (160 días)
- ❌ Coste elevado (130 equipo)
- ❌ Penalización en bosques y pantanos
- ❌ Ineficiente en campo abierto

#### Rol Estratégico
Unidad de guarnición y control de territorio. Ideal para defender ciudades conquistadas, suprimir rebeliones y mantener líneas defensivas donde el enemigo no debe pasar. **No usar en vanguardia ofensiva** — su breakthrough la hace inadecuada para penetraciones. En Roma, combinar con Hastati: Hastati para el ataque, Guardia Pretoriana para asegurar lo conquistado.

#### Ejemplo de uso Roma (SPQ)
```
División de Aseguramiento
├─ 3x Praetorian Guard (GRD)   ← garrisoning / supresión
├─ 2x Hastati (HAS)             ← defensa activa si el enemigo contraataca
└─ 1x Artillery (supp)
```

#### Tecnología
- **Tier 1:** `royal_guard` (1936) — Habilita la unidad
- **Tier 2:** `royal_guard1` (1939) — +3 máxima organización, +0.3 supresión
- **Tier 3:** `royal_guard2` (1942) — +3 máxima organización, +0.3 supresión, +5% defensa urbana

---

## Unidades de Caballería

### 7. Light Armor (LT) — Caballería Ligera

**Clasificación:** Caballería de reconocimiento y acoso
**Disponibilidad:** TODOS los países
**Restricción Tecnológica:** Ninguna (disponible al inicio)

#### Localización

| País | Código | Inglés | Español |
|------|--------|--------|---------|
| **Default** | — | Shock Cavalry | Caballería de Choque |
| 🇷🇴 Roma | SPQ | Roman Shock Cavalry | Equites Romani |
| 🇬🇷 Grecia | GRC | Greek Hippeis | Hippeis Griegos |
| 🐘 Cartago | CRG | Numidian Cavalry | Caballería Númida |
| 🇲🇰 Macedonia | MCD | Prodromoi | Prodromoi |
| ⚔️ Asiria | ASS | Assyrian Light Cavalry | Caballería Ligera Asiria |
| 🇪🇬 Egipto | KMT | Egyptian Light Cavalry | Caballería Ligera Egipcia |

> ⚠️ **Cambios respecto a v1:**
> - **Default ES:** "Equites de Choque" → "Caballería de Choque". El nombre anterior mezclaba latín y español de forma incongruente.
> - **SPQ ES:** "Equites Romanos" → "Equites Romani". Se mantiene en latín para coherencia con el inglés.
> - **MCD:** "Macedonian Light Cavalry" → "Prodromoi". Nombre histórico de los jinetes exploradores macedonios, usados extensamente por Alejandro como vanguardia de reconocimiento.

#### Estadísticas Base
| Stat | Valor |
|------|-------|
| **Equipment Required** | 60 light_tank_chassis |
| **Manpower** | 500 |
| **Training Time** | 120 días |
| **Max Strength** | 25 |
| **Combat Width** | 2 |

#### Rol Estratégico
- Reconocimiento y exploración
- Acoso de columnas enemigas
- Movilidad rápida en operaciones
- Economía de recursos vs caballería pesada

---

### 8. Heavy Armor (HV) — Caballería Pesada

**Clasificación:** Caballería de combate pesado
**Disponibilidad:** TODOS los países
**Restricción Tecnológica:** Ninguna (disponible al inicio)

#### Localización

| País | Código | Inglés | Español |
|------|--------|--------|---------|
| **Default** | — | Heavy Cavalry | Caballería Pesada |
| 🇷🇴 Roma | SPQ | Roman Heavy Cavalry | Caballería Pesada Romana |
| 🇬🇷 Grecia | GRC | Thessalian Cavalry | Caballería Tesalia |
| 🐘 Cartago | CRG | African Heavy Cavalry | Caballería Pesada Africana |
| 🇲🇰 Macedonia | MCD | Macedonian Companion Cavalry | Hetairoi — Caballería Real |
| ⚔️ Asiria | ASS | Assyrian Heavy Cavalry | Caballería Pesada Asiria |
| 🇪🇬 Egipto | KMT | Agema Cavalry | Caballería Agema |

> ⚠️ **Cambios respecto a v1:**
> - **GRC:** "Greek Heavy Cavalry" → "Thessalian Cavalry". La caballería pesada griega más célebre históricamente era la tesalia, aliada clave de Macedonia.
> - **KMT:** "Egyptian Heavy Cavalry" → "Agema Cavalry". El Agema era la guardia de caballería de élite de los Ptolemaicos, equivalente funcional a los Hetairoi macedonios.

#### Estadísticas Base
| Stat | Valor |
|------|-------|
| **Equipment Required** | 45 heavy_tank_chassis |
| **Manpower** | 500 |
| **Training Time** | 150 días |
| **Max Strength** | 25 |
| **Combat Width** | 2 |

#### Rol Estratégico
- Choque frontal en batalla
- Carga de caballería pesada
- Mayor durabilidad que caballería ligera
- Mejor breakthrough y ataque

---

### 9. War Elephant (ELP) — Elefantes de Guerra

**Clasificación:** Caballería especial — Elefantes
**Disponibilidad:** 🐘 **CRG (Cartago) SOLO**
**Restricción Tecnológica:** `allow = { tag = CRG }` en todas las tecnologías

#### Localización

| País | Código | Inglés | Español |
|------|--------|--------|---------|
| **Default** | — | War Elephants | Elefantes de Guerra |
| 🐘 Cartago | CRG | Carthaginian War Elephants | Elefantes Cartagineses |

*Nota: Única para Cartago, restricción tecnológica exclusiva.*

#### Estadísticas
| Stat | Valor | vs. Light Armor | vs. Heavy Armor |
|------|-------|-----------------|-----------------|
| **Equipment Required** | 60 light_tank_chassis | = | +33% (en equipo) |
| **Manpower** | 600 | +20% | +20% |
| **Training Time** | 150 días | +25% | =0% |
| **Max Strength** | 25 | =0% | =0% |
| **Breakthrough** | 0.30 | Alto | Alto |
| **Supply Consumption** | 0.055 | Normal | Normal |
| **Combat Width** | 2 | = | = |

#### Bonificaciones/Penalizaciones de Terreno
| Terreno | Efecto |
|---------|--------|
| **Marsh** | -5% penalidad (vs -10% light armor) |
| **River** | -15% penalidad (bajo) |
| **Urban** | -25% penalidad (muy débil en ciudades) |
| **Forest** | -10% penalidad |

#### Ventajas
- ✅ Excelente en pantanos (mejor que caballería estándar)
- ✅ Cruce de ríos mejorado
- ✅ Breakthrough alto (0.30)
- ✅ Unidad histórica exclusiva de Cartago
- ✅ Psicología: miedo a elefantes

#### Desventajas
- ❌ Horrible en ciudades (-25%)
- ❌ Malo en bosques (-10%)
- ❌ Solo Cartago
- ❌ Manpower alto (600)

#### Rol Estratégico
Fuerza de choque en batallas abiertas, especialmente en terreno mediterráneo. Evitar operaciones urbanas. Ideal en el norte de África y el Mediterráneo. Símbolo del poder cartaginés.

#### Tecnología
- **Tier 1:** `war_elephant` (1936) — Habilita la unidad (CRG SOLO)
- **Tier 2:** `war_elephant1` (1939) — +0.05 ataque blando, +0.1 ataque duro
- **Tier 3:** `war_elephant2` (1942) — +0.05 ataque blando, +0.1 ataque duro, +3 máxima organización

> ⚠️ **Corregido en v2:** En v1, Tier 1 y Tier 2 ambos figuraban en 1936. Se ajusta Tier 2 a 1939 y Tier 3 a 1942, coherente con el patrón general del mod.

---

### 10. Heavy Chariot (CHR) — Carros de Guerra Pesados

**Clasificación:** Caballería especial — Carros
**Disponibilidad:** ⚔️ **ASS (Asiria) SOLO**
**Restricción Tecnológica:** `allow = { tag = ASS }` en todas las tecnologías

#### Localización

| País | Código | Inglés | Español |
|------|--------|--------|---------|
| **Default** | — | Heavy Chariots | Carros de Guerra Pesados |
| ⚔️ Asiria | ASS | Assyrian War Chariots | Carros de Guerra Asirios |

*Nota: Única para Asiria, restricción tecnológica exclusiva.*

#### Estadísticas
| Stat | Valor | vs. Heavy Armor | vs. War Elephant |
|------|-------|-----------------|-----------------|
| **Equipment Required** | 45 heavy_tank_chassis | = | -25% |
| **Manpower** | 650 | +30% | +8% |
| **Training Time** | 170 días | +13% | +13% |
| **Max Strength** | 25 | =0% | =0% |
| **Breakthrough** | 0.32 | Alto | Alto |
| **Suppression** | 2.6 | Muy Alto | Alto |
| **Combat Width** | 2 | = | = |

#### Bonificaciones/Penalizaciones de Terreno
| Terreno | Efecto |
|---------|--------|
| **Fort** | +15% ataque |
| **Urban** | -55% penalidad (TERRIBLE) |
| **Jungle** | -60% penalidad (TERRIBLE) |
| **Forest** | Variable |
| **Mountain** | Variable |

#### Ventajas
- ✅ Highest breakthrough (0.32)
- ✅ Excelente supresión (2.6) para control de territorio
- ✅ Bonus vs fuertes (+15%)
- ✅ Símbolo del poder asirio
- ✅ Perfecto para asedio y campo abierto

#### Desventajas
- ❌ Horrible en ciudades (-55%)
- ❌ Catastrófico en jungla (-60%)
- ❌ Solo Asiria
- ❌ Manpower muy alto (650)
- ❌ Entrenamiento muy lento (170 días)

#### Rol Estratégico
Arma de asedio y guerra en campo abierto. Máximo breakthrough y supresión. Evitar terreno urbano y jungla. Ideal para Mesopotamia y Asia Menor. Unidad de elite asiria.

#### Tecnología
- **Tier 1:** `heavy_chariot` (1936) — Habilita la unidad (ASS SOLO)
- **Tier 2:** `heavy_chariot1` (1939) — +0.1 ataque blando, +0.15 ataque duro
- **Tier 3:** `heavy_chariot2` (1942) — +0.1 ataque blando, +0.15 ataque duro, +3 máxima organización

---

## Composición de Divisiones Típicas

### División Romana (SPQ)
```
Legio Romana
├─ 6x Hastati (HAS)
├─ 1x Artillery (supp)
└─ 1x Anti-Tank (supp)
```
**Rol:** Ataque y defensa balanceados. Elite romana.

### División Cartaginesa (CRG)
```
Elefantes Cartagineses
├─ 2x War Elephant (ELP)
├─ 2x Infantry (INF)
├─ 1x Artillery (supp)
└─ Opción: Reemplazar Infantry por Levy
```
**Rol:** Choque con elefantes, soporte de infantería.

### División Asiria (ASS)
```
Carros de Guerra Asirios
├─ 2x Heavy Chariot (CHR)
├─ 2x Infantry (INF)
├─ 1x Artillery (supp)
└─ Para asedio: Agregar ingenieros
```
**Rol:** Asedio y guerra de posición con carros.

---

## Matriz de Restricciones

```
┌──────────────────┬──────┬─────┬─────┬─────┬─────┐
│ Unidad           │ TODOS│ SPQ │ CRG │ ASS │ etc │
├──────────────────┼──────┼─────┼─────┼─────┼─────┤
│ Levy             │  ✅  │  ✅ │  ✅ │  ✅ │  ✅ │
│ Infantry         │  ✅  │  ✅ │  ✅ │  ✅ │  ✅ │
│ Hastati          │  ❌  │  ✅ │  ❌ │  ❌ │  ❌ │
│ Marine           │  ✅  │  ✅ │  ✅ │  ✅ │  ✅ │
│ Speculatores     │  ❌  │  ✅ │  ❌ │  ❌ │  ❌ │
│ Royal Guard      │  ✅  │  ✅ │  ✅ │  ✅ │  ✅ │
│ Light Armor      │  ✅  │  ✅ │  ✅ │  ✅ │  ✅ │
│ Heavy Armor      │  ✅  │  ✅ │  ✅ │  ✅ │  ✅ │
│ War Elephant     │  ❌  │  ❌ │  ✅ │  ❌ │  ❌ │
│ Heavy Chariot    │  ❌  │  ❌ │  ❌ │  ✅ │  ❌ │
└──────────────────┴──────┴─────┴─────┴─────┴─────┘
```

---

## Notas Técnicas

### Sistema de Equipo
- **Infantry Equipment:** Usado por infantería (Levy, Infantry, Hastati, Marine, Speculatores, Royal Guard)
- **Light Tank Chassis:** Usado por caballería ligera y elefantes
- **Heavy Tank Chassis:** Usado por caballería pesada y carros

### Tecnologías Base
Algunas unidades no requieren tecnología específica (están activas al inicio):
- Infantry (siempre disponible)
- Light Armor (siempre disponible)
- Heavy Armor (siempre disponible)

### Unidades Especiales
Las siguientes tienen flags especiales:
- **Marine:** `special_forces = yes`, `marines = yes`
- **Speculatores:** `special_forces = yes`

---

## Estrategia General de Composición

### Ejército Balanceado Temprano
- 60% Levy (rápidos y económicos)
- 30% Infantry (soporte veterano)
- 10% Light Armor (reconocimiento)

### Ejército Medio
- 40% Infantry
- 20% Unidades Especiales (Hastati / War Elephant / Chariot)
- 20% Caballería
- 20% Apoyo

### Ejército Late-Game
- Mayoría unidades de Tier 3 con investigación completa
- Mix de especialistas según terreno
- Alta proporción de unidades especiales (Hastati / Elefantes / Carros)

---

## Referencia Completa de Localizaciones

### Tabla por País — Nombres en Inglés

| Unidad | SPQ (Roma) | GRC (Grecia) | CRG (Cartago) | MCD (Macedonia) | ASS (Asiria) | KMT (Egipto) |
|--------|-----------|-------------|-------------|---------------|------------|-------------|
| **Levy** | Velites | Thetes | Libyan Conscripts | Macedonian Peltasts | Assyrian Conscripts | Egyptian Conscripts |
| **Infantry** | Roman Legionarii | Hoplites | Liby-Phoenician Infantry | Pezhetairoi | Kisir Šarri | Machimoi |
| **Hastati** | Hastati | — | — | — | — | — |
| **Marine** | Classiarii | Epibatai | Carthaginian Marines | Macedonian Marines | Assyrian Marines | Ptolemaic Marines |
| **Speculatores** | Speculatores | Greek Elite Hoplites | Carthaginian Elite | Macedonian Elite | Assyrian Elite | Egyptian Elite |
| **Royal Guard** | Praetorian Guard | Epilektoi | Sacred Band | Hypaspistai | Kiṣir Šarrāni | Ptolemaic Agema |
| **Light Armor** | Roman Shock Cavalry | Greek Hippeis | Numidian Cavalry | Prodromoi | Assyrian Light Cavalry | Egyptian Light Cavalry |
| **Heavy Armor** | Roman Heavy Cavalry | Thessalian Cavalry | African Heavy Cavalry | Macedonian Companion Cavalry | Assyrian Heavy Cavalry | Agema Cavalry |
| **War Elephant** | — | — | Carthaginian War Elephants | — | — | — |
| **Heavy Chariot** | — | — | — | — | Assyrian War Chariots | — |

### Tabla por País — Nombres en Español

| Unidad | SPQ (Roma) | GRC (Grecia) | CRG (Cartago) | MCD (Macedonia) | ASS (Asiria) | KMT (Egipto) |
|--------|-----------|-------------|-------------|---------------|------------|-------------|
| **Levy** | Velites | Thetes | Conscriptos Libios | Peltastas Macedonios | Conscriptos Asirios | Conscriptos Egipcios |
| **Infantry** | Legionario Romano | Hoplitas | Infantería Líbio-Fenicia | Pezhetairoi | Tropas Reales Asirias | Machimoi |
| **Hastati** | Hastati | — | — | — | — | — |
| **Marine** | Classiarii | Epibatai | Marines Cartagineses | Marines Macedonios | Marines Asirios | Marines Ptolemaicos |
| **Speculatores** | Especuladores | Hoplitas de Elite | Elite Cartaginesa | Elite Macedonia | Elite Asiria | Elite Egipcia |
| **Royal Guard** | Guardia Pretoriana | Epilektoi | Banda Sagrada | Hypaspistai | Kiṣir Šarrāni | Agema Ptolemaico |
| **Light Armor** | Equites Romani | Hippeis Griegos | Caballería Númida | Prodromoi | Caballería Ligera Asiria | Caballería Ligera Egipcia |
| **Heavy Armor** | Caballería Pesada Romana | Caballería Tesalia | Caballería Pesada Africana | Hetairoi — Caballería Real | Caballería Pesada Asiria | Caballería Agema |
| **War Elephant** | — | — | Elefantes Cartagineses | — | — | — |
| **Heavy Chariot** | — | — | — | — | Carros de Guerra Asirios | — |

### Mapa de Códigos de País

| Código | País | Localizaciones Exclusivas |
|--------|------|---------------------------|
| **SPQ** | Roma / SPQR | Hastati, Speculatores |
| **GRC** | Grecia | — |
| **CRG** | Cartago | War Elephant |
| **MCD** | Macedonia | — |
| **ASS** | Asiria | Heavy Chariot |
| **KMT** | Egipto (Kemet) | — |

---

---

## Registro de Cambios v3

### Nueva unidad: Royal Guard (GRD)

| Campo | Valor |
|-------|-------|
| **Abreviatura** | GRD |
| **Clasificación** | Infantería de Elite / Guarnición |
| **Disponibilidad** | TODOS los países |
| **Tech keys** | `royal_guard`, `royal_guard1`, `royal_guard2` |
| **Rol principal** | Supresión, defensa urbana, guarnición |
| **Stat diferencial** | Supresión 3.0 (máxima del mod), Moral 0.5, Org 80 |
| **Debilidad** | Breakthrough 0.05 — no es unidad de ataque |

### Nombres históricos asignados

| País | Nombre | Contexto |
|------|--------|---------|
| SPQ | Praetorian Guard / Guardia Pretoriana | Guardia imperial romana |
| GRC | Epilektoi | Infantería selecta de las polis griegas |
| CRG | Sacred Band / Banda Sagrada | *Hieros Lochos* cartaginés, elite de 2.500 hombres |
| MCD | Hypaspistai | Portadores de escudo de Alejandro, más tarde Argyraspides |
| ASS | Kiṣir Šarrāni | Guardia personal real asiria (distinta del Kisir Šarri regular) |
| KMT | Ptolemaic Agema / Agema Ptolemaico | Guardia de infantería ptolemaica helenística |

### Impacto en el balance

- Roma es la única facción con **dos** unidades de infantry elite (Hastati + Guardia Pretoriana), equilibrado por su ausencia de unidades especiales de caballería como Elefantes o Carros.
- El resto de facciones ganan acceso a una unidad de elite de guarnición propia con identidad histórica única.
- La Guardia no compite con Hastati — son complementarias: ataque vs. control.

---

## Registro de Cambios v2

### Inconsistencias corregidas

| # | Problema | Corrección |
|---|----------|-----------|
| 1 | Abreviatura `LEG` para Hastati confunde con el nombre interno de tecnología `roman_legion` | Cambiada a `HAS` |
| 2 | Unidad llamada "Paratrooper/PAR" en tabla resumen pero "Speculatores" en todo lo demás | Unificado a **Speculatores (SPE)** |
| 3 | Tier 2 de `roman_legion` y `war_elephant` figuraban en 1936, mismo año que Tier 1 | Corregido: Tier 2 → 1939, Tier 3 → 1942 |
| 4 | Levy no tenía nombres por país en las localizaciones | Añadidos nombres históricos para los 6 países |
| 5 | Nombre por defecto de Infantry: "Legionarii" (específicamente romano) | Cambiado a "Warriors / Guerreros" |
| 6 | Nombre por defecto de Marine: "Elite Legions" (confuso y contradictorio) | Cambiado a "Naval Infantry / Infantería Naval" |
| 7 | Marine SPQ: "Roman Praetorians" — categoría errónea (guardia terrestre ≠ infantería naval) | Cambiado a "Classiarii" (marines romanos reales) |
| 8 | "Equites de Choque" mezcla latín y español | Cambiado a "Caballería de Choque" |
| 9 | Texto cortado con saltos de línea en medio de palabras (×2) | Corregido en sección War Elephant y Heavy Chariot |
| 10 | "División Romano" | Corregido a "División Romana" |
| 11 | Tier 2-3 de Speculatores sin bonificaciones concretas | Homogeneizados con el patrón del resto; **verificar vs código** |
| 12 | Las tablas finales de localización no incluían fila para Levy | Añadida fila Levy a ambas tablas |
| 13 | La columna "vs. Roman Legion" en estadísticas de Levy e Infantry | Actualizada a "vs. Hastati" para coincidir con el nuevo nombre |

### Mejoras de nomenclatura histórica

| Unidad | País | Antes | Después | Justificación |
|--------|------|-------|---------|---------------|
| Infantry | CRG | African Infantry | Liby-Phoenician Infantry | El ejército cartaginés se basaba en mercenarios líbio-fenicios |
| Infantry | ASS | Assyrian Infantry | Kisir Šarri | Término acadio para las tropas reales profesionales asirias |
| Infantry | KMT | Ptolemaic Infantry | Machimoi | Clase guerrera egipcia bajo los Ptolemaicos (término técnico) |
| Marine | GRC | Greek Marines | Epibatai | Nombre histórico de los soldados embarcados en trirremes griegos |
| Light Armor | MCD | Macedonian Light Cavalry | Prodromoi | Jinetes exploradores macedonios de Alejandro |
| Heavy Armor | GRC | Greek Heavy Cavalry | Thessalian Cavalry | La caballería pesada griega más célebre históricamente |
| Heavy Armor | KMT | Egyptian Heavy Cavalry | Agema Cavalry | Guardia de caballería elite de los Ptolemaicos |

