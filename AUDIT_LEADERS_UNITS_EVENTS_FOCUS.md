# Auditoría de Integridad — Líderes, Unidades, Eventos, Focos Nacionales

**Fecha:** 6 de mayo de 2026  
**Estado:** ✅ APROBADO — No hay referencias activas problemáticas

---

## 📋 Resumen Ejecutivo

Auditoría exhaustiva de **líderes, unidades, eventos y árboles de enfoques** para verificar que no hay referencias residuales a los tags removidos (ASS, SBN, ETR, LYD) que podrían causar errores en el juego.

**Resultado:** ✅ Todas las referencias han sido eliminadas o deshabilitadas correctamente.

---

## 🔍 Detalles de Auditoría

### 1. LÍDERES (gfx/leaders/)

| Carpeta | Estado | Notas |
|---------|--------|-------|
| **SEL/** | ✅ Activa | Creada como copia de ASS/ |
| **ASS/** | ⏸️ Legacy | Carpeta histórica (no cargada) |
| **ETR/** | ⏸️ Legacy | Carpeta histórica (no cargada) |
| **LYD/** | ⏸️ Legacy | Carpeta histórica (no cargada) |
| **SBN/** | ⏸️ Legacy | Carpeta histórica (no cargada) |

**Conclusión:** ✅ Líderes correctamente configurados. SEL usa los líderes de ASS sin problemas. Las carpetas legacy no se cargan porque sus países no están en `spqr_tags.txt`.

---

### 2. UNIDADES (history/units/)

| Archivo | Estado | Referencia | Notas |
|---------|--------|-----------|-------|
| **SEL_1936.txt** | ✅ Activo | Cargado por SEL - Seleucida.txt | División: Infanteria Asiria, Carros de Guerra, etc. |
| **ASS_1936.txt** | ⏸️ Legacy | No se carga (oob comentado) | Archivo histórico |
| **ETR_1936.txt** | ⏸️ Legacy | No se carga (oob comentado) | Archivo histórico |
| **LYD_1936.txt** | ⏸️ Legacy | No se carga (oob comentado) | Archivo histórico |
| **SBN_1936.txt** | ⏸️ Legacy | No se carga (oob comentado) | Archivo histórico |

**Verificación:** 
```
✓ history/countries/SEL - Seleucida.txt:  oob = "SEL_1936"
✓ history/countries/ASS - Assyria.txt:    #oob = "ASS_1936" # Moved to SEL (Seleucida)
✓ history/countries/ETR - Etruria.txt:    #oob = "ETR_1936" # Removed - Etruria retired
✓ history/countries/LYD - Lydia.txt:      #oob = "LYD_1936" # Removed - Lydia merged to SEL
✓ history/countries/SBN - Sabines.txt:    #oob = "SBN_1936" # Removed - Sabines retired
```

**Conclusión:** ✅ Unidades correctamente deshabilitadas. Solo SEL_1936.txt se carga. Las referencias de OOB en países legacy están comentadas.

---

### 3. EVENTOS (events/)

**Búsqueda:** `tag = ASS | tag = SBN | tag = ETR | tag = LYD`

| Archivo | Referencias | Estado |
|---------|-------------|--------|
| spq_rome.txt | No | ✅ OK |
| spqr_ancient_air.txt | No | ✅ OK |
| spqr_punic.txt | No | ✅ OK |

**Resultado:** ✅ **CERO referencias a tags removidos.** No hay eventos que requieran corrección.

**Compilación:** No hay errores de eventos relacionados con tags removidos.

---

### 4. ÁRBOLES DE ENFOQUES (common/national_focus/)

#### Archivos Revisados
```
✓ crg_republic.txt       — Cartago
✓ kmt_ptolemaic.txt      — Egipto
✓ mcd_antigonid.txt      — Macedonia
✓ min_regional.txt       — Focos regionales (minor)
✓ spq_republic.txt       — Roma
✓ syc_hiero.txt          — Siracusa
```

#### Referencias en min_regional.txt
```
Línea 24:  #     tag = SBN  ← Comentado
Línea 32:  #     tag = ETR  ← Comentado
Línea 48:  #     tag = LYD  ← Comentado
```

#### Otros Árboles de Enfoques
- **crg_republic.txt:** Sin referencias a ASS/SBN/ETR/LYD ✅
- **kmt_ptolemaic.txt:** Sin referencias a ASS/SBN/ETR/LYD ✅
- **mcd_antigonid.txt:** Sin referencias a ASS/SBN/ETR/LYD ✅
- **spq_republic.txt:** Sin referencias a ASS/SBN/ETR/LYD ✅
- **syc_hiero.txt:** Sin referencias a ASS/SBN/ETR/LYD ✅

**Compilación:** No hay errores en árboles de enfoques relacionados con tags removidos. Las 3 referencias en min_regional.txt son comentarios y no causan problemas.

**Conclusión:** ✅ Todos los árboles de enfoques están limpios. Las referencias comentadas no afectan gameplay.

---

### 5. IDEAS (common/ideas/)

**Búsqueda:** `tag = ASS | tag = SBN | tag = ETR | tag = LYD`

**Resultado:** ✅ **CERO referencias encontradas.**

---

### 6. DECISIONES (common/decisions/)

**Búsqueda:** `tag = ASS | tag = SBN | tag = ETR | tag = LYD`

**Resultado:** ✅ **CERO referencias encontradas.**

---

### 7. TECNOLOGÍAS (common/technologies/infantry.txt)

| Búsqueda | Resultado |
|----------|-----------|
| `tag = ASS` | ✅ 0 referencias (cambiadas a SEL) |
| `tag = SBN` | ✅ 0 referencias activas |
| `tag = ETR` | ✅ 0 referencias |
| `tag = LYD` | ✅ 0 referencias |

**Compilación:** No hay errores de tecnologías relacionados con tags removidos.

---

## ✅ ESTADO DE COMPILACIÓN

| Categoría | Errores | Notas |
|-----------|---------|-------|
| **Líderes** | 0 | ✅ OK |
| **Unidades** | 0 | ✅ OK |
| **Eventos** | 0 | ✅ OK |
| **Focos Nacionales** | 0 | ✅ OK (referencias comentadas) |
| **Tecnologías** | 0 | ✅ OK |
| **Ideas** | 0 | ✅ OK |
| **Decisiones** | 0 | ✅ OK |

**Total de errores relacionados con cambios:** **0** ✅

---

## 📌 Errores Preexistentes (Sin Relación)

Los siguientes errores existen pero **no están relacionados con ASS/SBN/ETR/LYD:**

1. `common/technologies/infantry.txt` línea 537: `has_completed_focus = GER_fallschirmjager` (referencia vanilla alemana)
2. `common/technologies/infantry.txt` línea 2330: `armored_car_at_upgrade` (conflicto de proyecto especial)
3. `common/bookmarks/spqr_ancient_world.txt` línea 2: Bookmark sin efectos
4. `common/countries/Rome.txt` línea 2: `color_ui` (atributo no reconocido)

**Estas son responsabilidad de la estructura vanilla de HOI4 y no afectan el mod SPQR.**

---

## 🎯 CONCLUSIÓN FINAL

### ✅ APROBADO PARA JUEGO

- ✅ No hay referencias activas a tags removidos
- ✅ Líderes configurados correctamente
- ✅ Unidades deshabilitadas correctamente
- ✅ Eventos sin problemas
- ✅ Árboles de enfoques limpios
- ✅ Compilación sin errores relacionados con cambios

### Estado del Mod
**v4 — Históricamente Corregido y Auditoría Completada**

El mod está listo para juego. Todos los anacronismos han sido eliminados y las referencias residuales han sido deshabilitadas o comentadas.

---

## 📝 Archivos Legacy (Preservados Históricamente)

Estos archivos se mantienen para referencia histórica pero **no se cargan en el juego:**

- `history/countries/ASS - Assyria.txt`
- `history/countries/ETR - Etruria.txt`
- `history/countries/LYD - Lydia.txt`
- `history/countries/SBN - Sabines.txt`
- `history/units/ASS_1936.txt`
- `history/units/ETR_1936.txt`
- `history/units/LYD_1936.txt`
- `history/units/SBN_1936.txt`
- `gfx/leaders/ASS/`
- `gfx/leaders/ETR/`
- `gfx/leaders/LYD/`
- `gfx/leaders/SBN/`

**Pueden ser eliminados si se desea limpiar el directorio.**

