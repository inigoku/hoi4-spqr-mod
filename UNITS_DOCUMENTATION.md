# SPQR Mod - Units Documentation

Documentación completa de todas las unidades disponibles en el mod SPQR. Este documento detalla estadísticas, restricciones, requisitos tecnológicos y roles estratégicos de cada unidad.

---

## Tabla Resumen de Unidades

| Tipo | Abrev. | Clasificación | Disponible | Tech Base | Tech +1 | Tech +2 | Notas |
|------|--------|---------------|-----------|-----------|---------|---------|-------|
| **Levy** | LEV | Infantería Básica | TODOS | `levy` | `levy2` | `levy3` | Conscriptos, entrenamiento rápido |
| **Infantry** | INF | Infantería Regular | TODOS | N/A | N/A | N/A | Veterana, disponible al inicio |
| **Hastati** | LEG | Infantería Elite | SPQ | `roman_legion` | `roman_legion1` | `roman_legion2` | Solo Roma - Primera línea de batalla |
| **Marine** | MRN | Infantería Especializada | TODOS | `marines` | `marines2` | `marines3` | Operaciones anfibias |
| **Paratrooper** | PAR | Infantería Aérea | SPQ | `paratroopers` | `paratroopers2` | `paratroopers3` | Solo Roma, desembarque aéreo |
| **Light Armor** | LT | Caballería Ligera | TODOS | N/A | N/A | N/A | Disponible al inicio |
| **Heavy Armor** | HV | Caballería Pesada | TODOS | N/A | N/A | N/A | Disponible al inicio |
| **War Elephant** | ELP | Caballería Especial | CRG | `war_elephant` | `war_elephant1` | `war_elephant2` | Solo Cartago |
| **Heavy Chariot** | CHR | Caballería Especial | ASS | `heavy_chariot` | `heavy_chariot1` | `heavy_chariot2` | Solo Asiria |

---

## Unidades de Infantería

### 1. Levy (LEV) - Infantería Básica

**Clasificación:** Infantería conscripta, reclutamiento masivo  
**Disponibilidad:** TODOS los países  
**Restricción Tecnológica:** Ninguna (investigable por todos)

#### Localización

| País | Código | Inglés | Español |
|------|--------|--------|---------|
| **Default** | - | *(No específica)* | *(No específica)* |

*Nota: Levy usa nombres genéricos de infantería en cada país*

#### Estadísticas
| Stat | Valor | vs. Infantry | vs. Roman Legion |
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
- **Tier 1:** `levy` (1936) - Habilita la unidad
- **Tier 2:** `levy2` (1939) - +3 máxima organización, +0.05 ataque blando
- **Tier 3:** `levy3` (1943) - +3 máxima organización, +0.05 ataque blando

---

### 2. Infantry (INF) - Infantería Regular

**Clasificación:** Infantería veterana y entrenada  
**Disponibilidad:** TODOS los países  
**Restricción Tecnológica:** Ninguna (disponible al inicio)

#### Localización

| País | Código | Inglés | Español |
|------|--------|--------|---------|
| **Default** | - | Legionarii | Legionarius |
| 🇷🇴 Roma | SPQ | Roman Legionarii | Legionario Romano |
| 🇬🇷 Grecia | GRC | Hoplites | Hoplitas |
| 🐘 Cartago | CRG | African Infantry | Infanteria Africana |
| 🇲🇰 Macedonia | MCD | Pezhetairoi | Pezhetairoi |
| ⚔️ Asiria | ASS | Assyrian Infantry | Infanteria Asiria |
| 🇪🇬 Egipto | KMT | Ptolemaic Infantry | Infanteria Ptolemaica |

#### Estadísticas
| Stat | Valor | vs. Levy | vs. Roman Legion |
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
- ❌ Peor que los legionarios en combate
- ❌ Sin bonificaciones de terreno
- ❌ Entrenamiento más lento que levy

#### Rol Estratégico
Unidad estándar de infantería para la mayoría de países. Base sólida para formaciones defensivas. Combina coste razonable con capacidades efectivas. Usarla como estructura central del ejército.

#### Bonificaciones de Terreno
Ninguna especial (es la unidad base de comparación).

---

### 3. Hastati (LEG) - Infantería Elite Romana

**Clasificación:** Primera línea de batalla romana, infantería profesional y altamente entrenada  
**Disponibilidad:** 🇷🇴 **SPQ (Roma) SOLO**  
**Restricción Tecnológica:** `allow = { tag = SPQ }` en todas las tecnologías

#### Nota Histórica
Los **Hastati** eran la primera línea de la falange romana manipular, compuestos por soldados jóvenes pero altamente entrenados. Representan la elite de combate romano.

#### Localización

| País | Código | Inglés | Español |
|------|--------|--------|---------|
| 🇷🇴 Roma | SPQ | Hastati | Hastati |

*Nota: Única para Roma, restricción tecnológica exclusiva*

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
- **Tier 1:** `roman_legion` (1936) - Habilita la unidad (SPQ SOLO)
- **Tier 2:** `roman_legion1` (1936) - +0.05 ataque blando
- **Tier 3:** `roman_legion2` (1939) - +0.05 ataque blando, +3 máxima organización, +0.05 breakthrough

---

### 4. Marine (MRN) - Infantería Marina Especializada

**Clasificación:** Infantería especializada en operaciones anfibias  
**Disponibilidad:** TODOS los países  
**Restricción Tecnológica:** Ninguna (investigable por todos)

#### Localización

| País | Código | Inglés | Español |
|------|--------|--------|---------|
| **Default** | - | Elite Legions | Legiones de Elite |
| 🇷🇴 Roma | SPQ | Roman Praetorians | Pretorianos Romanos |
| 🇬🇷 Grecia | GRC | Greek Marines | Marines Griegos |
| 🐘 Cartago | CRG | Carthaginian Marines | Marines Cartagineses |
| 🇲🇰 Macedonia | MCD | Macedonian Marines | Marines Macedonios |
| ⚔️ Asiria | ASS | Assyrian Marines | Marines Asirios |
| 🇪🇬 Egipto | KMT | Egyptian Marines | Marines Egipcios |

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
- ❌ Capacidades limitadas en tierra

#### Rol Estratégico
Para operaciones anfibias y conquista de zonas costeras/islas. Usar en desembarques coordinados. Especializada en Mediterraneo. Menos útil en tierra interior.

#### Tecnología
- **Tier 1:** `marines` (1936) - Habilita la unidad
- **Tier 2:** `marines2` (1939) - +5 máxima organización, +0.05 ataque blando
- **Tier 3:** `marines3` (1943) - +5 máxima organización

---

### 5. Paratrooper (PAR) - Speculatores (Infiltración)

**Clasificación:** Tropas especializadas en infiltración y tareas secretas  
**Disponibilidad:** 🇷🇴 **SPQ (Roma) SOLO**  
**Restricción Tecnológica:** `allow = { tag = SPQ }` en tecnología `paratroopers`

#### Nota Histórica
Los **Speculatores** eran tropas especializadas romanas en infiltración, espionaje y operaciones secretas. Desembarco aéreo en el contexto del juego representa su capacidad de infiltrarse detrás de líneas enemigas.

#### Localización

| País | Código | Inglés | Español |
|------|--------|--------|---------|
| **Default** | - | Speculatores | Especuladores |
| 🇷🇴 Roma | SPQ | Speculatores | Especuladores |
| 🇬🇷 Grecia | GRC | Greek Elite Hoplites | Hoplitas de Elite |
| 🐘 Cartago | CRG | Carthaginian Elite | Elite Cartaginesa |
| 🇲🇰 Macedonia | MCD | Macedonian Elite | Elite Macedonia |
| ⚔️ Asiria | ASS | Assyrian Elite | Elite Asiria |
| 🇪🇬 Egipto | KMT | Egyptian Elite | Elite Egipcia |

*Nota: Solo investigable por Roma, pero localizaciones definidas para todos*

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
- ✅ Desembarque aéreo directo (infiltración)
- ✅ Unidad especial (fuerzas especiales)
- ✅ Capacidad de aterrizaje en cualquier terreno
- ✅ Solo para Roma

#### Desventajas
- ❌ Requiere transporte aéreo
- ❌ Entrenamiento lento
- ❌ Capacidades limitadas sin apoyo aéreo
- ❌ Solo disponible para SPQ

#### Rol Estratégico
Operaciones detrás de líneas enemigas. Infiltración en territorio hostil. Requiere coordinación con aviación. Unidad premium para Roma.

#### Tecnología
- **Tier 1:** `paratroopers` (1936) - Habilita la unidad (SPQ SOLO)
- **Tier 2:** `paratroopers2` (1939) - Mejoras a paratrooper
- **Tier 3:** `paratroopers3` (1943) - Mejoras adicionales

---

## Unidades de Caballería

### 6. Light Armor (LT) - Caballería Ligera

**Clasificación:** Caballería de reconocimiento y acoso  
**Disponibilidad:** TODOS los países  
**Restricción Tecnológica:** Ninguna (disponible al inicio)

#### Localización

| País | Código | Inglés | Español |
|------|--------|--------|---------|
| **Default** | - | Shock Cavalry | Equites de Choque |
| 🇷🇴 Roma | SPQ | Roman Shock Cavalry | Equites Romanos |
| 🇬🇷 Grecia | GRC | Greek Hippeis | Hippeis Griegos |
| 🐘 Cartago | CRG | Numidian Cavalry | Caballeria Numida |
| 🇲🇰 Macedonia | MCD | Macedonian Light Cavalry | Caballeria Ligera Macedonia |
| ⚔️ Asiria | ASS | Assyrian Light Cavalry | Caballeria Ligera Asiria |
| 🇪🇬 Egipto | KMT | Egyptian Light Cavalry | Caballeria Ligera Egipcia |

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

### 7. Heavy Armor (HV) - Caballería Pesada

**Clasificación:** Caballería de combate pesado  
**Disponibilidad:** TODOS los países  
**Restricción Tecnológica:** Ninguna (disponible al inicio)

#### Localización

| País | Código | Inglés | Español |
|------|--------|--------|---------|
| **Default** | - | Heavy Cavalry | Caballeria Pesada |
| 🇷🇴 Roma | SPQ | Roman Heavy Cavalry | Caballeria Pesada Romana |
| 🇬🇷 Grecia | GRC | Greek Heavy Cavalry | Caballeria Pesada Griega |
| 🐘 Cartago | CRG | African Heavy Cavalry | Caballeria Pesada Africana |
| 🇲🇰 Macedonia | MCD | Macedonian Companion Cavalry | Hetairoi - Caballeria Real |
| ⚔️ Asiria | ASS | Assyrian Heavy Cavalry | Caballeria Pesada Asiria |
| 🇪🇬 Egipto | KMT | Egyptian Heavy Cavalry | Caballeria Pesada Ptolemaica |

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

### 8. War Elephant (ELP) - Elefantes de Guerra

**Clasificación:** Caballería especial - Elefantes  
**Disponibilidad:** 🐘 **CRG (Cartago) SOLO**  
**Restricción Tecnológica:** `allow = { tag = CRG }` en todas las tecnologías

#### Localización

| País | Código | Inglés | Español |
|------|--------|--------|---------|
| **Default** | - | War Elephants | Elefantes de Guerra |
| 🐘 Cartago | CRG | Carthaginian War Elephants | Elefantes Cartagineses |

*Nota: Única para Cartago, restricción tecnológica exclusiva*

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
- ✅ Psicología: Miedo a elefantes

#### Desventajas
- ❌ Horrible en ciudades (-25%)
- ❌ Malo en bosques (-10%)
- ❌ Solo Cartago
- ❌ Manpower alto (600)

#### Rol Estratégico
Fuerza de choque en batallas abiertas, especialmente en terr

eno mediterráneo. Evitar operaciones urbanas. Ideal en el norte de África y Mediterráneo. Símbolo del poder cartaginés.

#### Tecnología
- **Tier 1:** `war_elephant` (1936) - Habilita la unidad (CRG SOLO)
- **Tier 2:** `war_elephant1` (1936) - +0.05 ataque blando, +0.1 ataque duro
- **Tier 3:** `war_elephant2` (1939) - +0.05 ataque blando, +0.1 ataque duro, +3 máxima organización

---

### 9. Heavy Chariot (CHR) - Carros de Guerra Pesados

**Clasificación:** Caballería especial - Carros  
**Disponibilidad:** ⚔️ **ASS (Asiria) SOLO**  
**Restricción Tecnológica:** `allow = { tag = ASS }` en todas las tecnologías

#### Localización

| País | Código | Inglés | Español |
|------|--------|--------|---------|
| **Default** | - | Heavy Chariots | Carros de Guerra Pesados |
| ⚔️ Asiria | ASS | Assyrian War Chariots | Carros de Guerra Asirios |

*Nota: Única para Asiria, restricción tecnológica exclusiva*

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
- ✅ Perfecto para asedio

#### Desventajas
- ❌ Horrible en ciudades (-55%)
- ❌ Catastrófico en jungla (-60%)
- ❌ Solo Asiria
- ❌ Manpower muy alto (650)
- ❌ Entrenamiento muy lento (170 días)

#### Rol Estratégico
Arma de asedio y guerra en campo abierto. Máximo breakthrough y supresión. Evitar terreno urbano y jungla. Ideal para Mesopotamia y Asia Menor. Unidad de elit

a asiria.

#### Tecnología
- **Tier 1:** `heavy_chariot` (1936) - Habilita la unidad (ASS SOLO)
- **Tier 2:** `heavy_chariot1` (1936) - +0.1 ataque blando, +0.15 ataque duro
- **Tier 3:** `heavy_chariot2` (1939) - +0.1 ataque blando, +0.15 ataque duro, +3 máxima organización

---

## Composición de Divisiones Típicas

### División Romano (SPQ)
```
Legio Romana
├─ 6x Roman Legion (LEG)
├─ 1x Artillery (supp)
└─ 1x Anti-Tank (supp)
```
**Rol:** Ataque y defensa balanceado. Elite romana.

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
┌─────────────────┬──────┬─────┬─────┬─────┬─────┐
│ Unidad          │ TODOS│ SPQ │ CRG │ ASS │ etc │
├─────────────────┼──────┼─────┼─────┼─────┼─────┤
│ Levy            │  ✅  │  ✅ │  ✅ │  ✅ │  ✅ │
│ Infantry        │  ✅  │  ✅ │  ✅ │  ✅ │  ✅ │
│ Roman Legion    │  ❌  │  ✅ │  ❌ │  ❌ │  ❌ │
│ Marine          │  ✅  │  ✅ │  ✅ │  ✅ │  ✅ │
│ Paratrooper     │  ❌  │  ✅ │  ❌ │  ❌ │  ❌ │
│ Light Armor     │  ✅  │  ✅ │  ✅ │  ✅ │  ✅ │
│ Heavy Armor     │  ✅  │  ✅ │  ✅ │  ✅ │  ✅ │
│ War Elephant    │  ❌  │  ❌ │  ✅ │  ❌ │  ❌ │
│ Heavy Chariot   │  ❌  │  ❌ │  ❌ │  ✅ │  ❌ │
└─────────────────┴──────┴─────┴─────┴─────┴─────┘
```

---

## Notas Técnicas

### Sistema de Equipo
- **Infantry Equipment:** Usado por infantería (Levy, Infantry, Roman Legion, Marine, Paratrooper)
- **Light Tank Chassis:** Usado por caballería ligera y elefantes
- **Heavy Tank Chassis:** Usado por caballería pesada y carros

### Tecnologías Base
Algunas unidades no requieren tecnología específica (están activas = no):
- Infantry (siempre disponible)
- Light Armor (siempre disponible)
- Heavy Armor (siempre disponible)

### Unidades Especiales
Las siguientes tienen flags especiales:
- **Marine:** `special_forces = yes`, `marines = yes`
- **Paratrooper:** `special_forces = yes`

---

## Cambios desde Versión Anterior

### Nuevas Unidades Agregadas
- ✅ **Levy (LEV)** - Infantería conscripta básica
- ✅ **Roman Legion (LEG)** - Elite romana exclusiva
- ✅ **War Elephant (ELP)** - Exclusiva Cartago
- ✅ **Heavy Chariot (CHR)** - Exclusiva Asiria

### Restricciones Implementadas
- ✅ Roman Legion → SPQ solo
- ✅ Paratrooper → SPQ solo (tecnología)
- ✅ War Elephant → CRG solo
- ✅ Heavy Chariot → ASS solo

### Tecnologías Nuevas
- ✅ Tier 3 para Levy (levy3)
- ✅ Tier 2-3 para Roman Legion
- ✅ Tier 2-3 para War Elephant
- ✅ Tier 2-3 para Heavy Chariot

---

## Estrategia General de Composición

### Ejército Balanceado Temprano
- 60% Levy (rápidos y económicos)
- 30% Infantry (soporte veterano)
- 10% Light Armor (reconocimiento)

### Ejército Medio
- 40% Infantry
- 20% Unidades Especiales (Roman Legion / War Elephant / Chariot)
- 20% Caballería
- 20% Apoyo

### Ejército Late-Game
- Mayoría unidades de Tier 3 con investigación completa
- Mix de especialistas según terreno
- Alta proporción de unidades especiales (Legions/Elephants/Chariots)

---

## Referencia Completa de Localizaciones

### Tabla por País - Nombres en Inglés

| SPQ (Roma) | GRC (Grecia) | CRG (Cartago) | MCD (Macedonia) | ASS (Asiria) | KMT (Egipto) |
|-----------|-------------|-------------|---------------|------------|-------------|
| Roman Legionarii | Hoplites | African Infantry | Pezhetairoi | Assyrian Infantry | Ptolemaic Infantry |
| Hastati | Greek Elite Hoplites | Carthaginian Elite | Macedonian Elite | Assyrian Elite | Egyptian Elite |
| Roman Praetorians | Greek Marines | Carthaginian Marines | Macedonian Marines | Assyrian Marines | Egyptian Marines |
| Roman Shock Cavalry | Greek Hippeis | Numidian Cavalry | Macedonian Light Cavalry | Assyrian Light Cavalry | Egyptian Light Cavalry |
| Roman Heavy Cavalry | Greek Heavy Cavalry | African Heavy Cavalry | Macedonian Companion Cavalry | Assyrian Heavy Cavalry | Egyptian Heavy Cavalry |
| Speculatores | (no available) | (no available) | (no available) | (no available) | (no available) |
| (no available) | (no available) | Carthaginian War Elephants | (no available) | (no available) | (no available) |
| (no available) | (no available) | (no available) | (no available) | Assyrian War Chariots | (no available) |

### Tabla por País - Nombres en Español

| SPQ (Roma) | GRC (Grecia) | CRG (Cartago) | MCD (Macedonia) | ASS (Asiria) | KMT (Egipto) |
|-----------|-------------|-------------|---------------|------------|-------------|
| Legionario Romano | Hoplitas | Infanteria Africana | Pezhetairoi | Infanteria Asiria | Infanteria Ptolemaica |
| Especuladores | Hoplitas de Elite | Elite Cartaginesa | Elite Macedonia | Elite Asiria | Elite Egipcia |
| Pretorianos Romanos | Marines Griegos | Marines Cartagineses | Marines Macedonios | Marines Asirios | Marines Egipcios |
| Equites Romanos | Hippeis Griegos | Caballeria Numida | Caballeria Ligera Macedonia | Caballeria Ligera Asiria | Caballeria Ligera Egipcia |
| Caballeria Pesada Romana | Caballeria Pesada Griega | Caballeria Pesada Africana | Hetairoi - Caballeria Real | Caballeria Pesada Asiria | Caballeria Pesada Ptolemaica |
| Especuladores | (no disponible) | (no disponible) | (no disponible) | (no disponible) | (no disponible) |
| (no disponible) | (no disponible) | Elefantes Cartagineses | (no disponible) | (no disponible) | (no disponible) |
| (no disponible) | (no disponible) | (no disponible) | (no disponible) | Carros de Guerra Asirios | (no disponible) |

### Mapa de Códigos de País

| Código | País | Localizaciones Exclusivas |
|--------|------|---------------------------|
| **SPQ** | Roma / SPQR | Roman Legion, Paratrooper |
| **GRC** | Grecia | - |
| **CRG** | Cartago | War Elephant |
| **MCD** | Macedonia | - |
| **ASS** | Asiria | Heavy Chariot |
| **KMT** | Egipto (Kemet) | - |

---
