# Auditoría Histórica de Territorios - SPQR Mod (~264 BCE)
## Validación de Precisión Geográfica y Anacrónismos

**Contexto Histórico:** Primera Guerra Púnica (~264-241 BCE), período post-alejandrino.

---

## 📊 TABLA DE VALIDACIÓN POR PAÍS

### ✅ ASIGNACIONES HISTÓRICAMENTE PRECISAS

| País | Tag | Territorios | Estado Histórico ~264 BCE | Precisión |
|------|-----|-------------|---------------------------|-----------|
| **Roma** | SPQ | Italia (2, 117, 156-162) | República romana, control de Italia central/sur | ✅ CORRECTO |
| **Grecia** | GRC | Grecia (47) | Estados-ciudad griegos independientes | ✅ CORRECTO (pero incompleto) |
| **Macedonia** | MCD | Macedonia (106, 731) | Monarquía macedónica postalejandriana | ✅ CORRECTO |
| **Sparta** | LAC | Peloponeso (186) | Sparta controlaba Peloponeso | ✅ CORRECTO (pero limitado) |
| **Cartago** | CRG | Cerdeña (114), Túnez (458), Córdoba (789) | Imperio púnico en Mediterráneo Occidental | ✅ CORRECTO |
| **Galos** | GLN | Provenza (16, 21) | Tribus galas en sur de Francia | ✅ CORRECTO |
| **Iberia** | IBR | Hispania (41, 165, 167, 790) | Tribus ibéricas en Peninsular | ✅ CORRECTO |
| **Iliria** | ILL | Croacia (103) | Reinos ilirios en Balcanes | ✅ CORRECTO |
| **Samnitas** | SMN | Puglia (849) | Confederación samnita en Italia del Sur | ✅ CORRECTO |
| **Siracusa** | SYC | Sicilia (115) | Tiranía griega en Sicilia | ✅ CORRECTO |
| **Tracia** | THR | Tracia (184, 341) | Reinos tracios en Balcanes del Este | ✅ CORRECTO |
| **Egipto** | KMT | Nilo/Cirenaica (183, 450, 452, 456, 663, 907) | Imperio Ptolemaico (posalejandrino) | ✅ CORRECTO |

---

### ⚠️ ASIGNACIONES ANACRRÓNICAS O PROBLEMÁTICAS

#### 1. **Asiria (ASS) - ANACRÓNICA**
- **Territorios:** Mesopotamia (510), Siria (554), Aleppo (677)
- **Problema:** Asiria como imperio cayó en **609 BCE** (~355 años antes de 264 BCE)
- **Realidad ~264 BCE:** Mesopotamia y Siria eran controladas por el **Imperio Seleucida** (herederos de Alejandro)
- **Recomendación:** 
  - Opción A: Renombrar tag ASS → SEL (Seleucida)
  - Opción B: Retirar ASS y asignar a WLD (Tierras Salvajes) o crear nuevo tag
  - Opción C: Mover a período diferente (ej. 1000 BCE) donde Asiria era relevante

#### 2. **Etruria (ETR) - ANACRÓNICA Y GEOGRÁFICAMENTE IMPOSIBLE**
- **Territorios:** Argelia Occidental (459), Argelia Oriental (460)
- **Problemas múltiples:**
  - Etruria fue una región en Italia central (~900-100 BCE), absorbida por Roma ~390 BCE
  - Para 264 BCE, Etruria como entidad política **no existía** (llevaba 126 años bajo dominio romano)
  - Argelia en 264 BCE era bereber, púnica o salvaje - **nunca fue etrusca**
- **Recomendación:** 
  - Mover ETR a Italia central y renombrar como territorio romano menor
  - Asignar Argelia a WLD, o crear tag bereber (BER)
  - O cambiar período histórico del mod

#### 3. **Lidia (LYD) - ANACRÓNICA**
- **Territorios:** Izmir (339), Antalya (342)
- **Problema:** Lidia fue un reino potente en Anatolia Occidental (~700-546 BCE) pero:
  - Cayó bajo el Imperio Persa en 546 BCE
  - Para 264 BCE, era parte del **Imperio Seleucida**
  - Nunca fue independiente en 264 BCE
- **Recomendación:**
  - Renombrar LYD → SEL (Seleucida) o WLD
  - O trasladar a período anterior (ej. 600 BCE)

#### 4. **Fenicia (PHN) - GEOGRÁFICAMENTE INCORRECTA**
- **Territorios:** Marruecos del Norte (461)
- **Problema:**
  - Fenicia es la región en el Levante (Líbano actual), NO Marruecos
  - Marruecos en 264 BCE era bereber, con presencia púnica (Cartago), NO fenicia
- **Recomendación:**
  - Mover PHN a Siria/Líbano (estados del Levante que pertenecen a Seleucidas)
  - Asignar 461 (Marruecos) a CRG (Cartago) o crear tag bereber
  - O renombrar PHN → MAU (Mauritania) para Marruecos

#### 5. **Sabines (SBN) - ANACRÓNICA Y GEOGRÁFICAMENTE IMPOSIBLE**
- **Territorios:** Albania (44), Epiro (185), N. Epiro (805), W. Macedonia (970)
- **Problemas:**
  - Sabines eran una tribu de Italia central-oriental (~290 BCE ya estaban bajo dominio romano)
  - En 264 BCE, Sabines como entidad **no existían** (absorbidos por Roma ~290 BCE)
  - Nunca controlarían territorios griegos (Epiro, Macedonia)
- **Recomendación:**
  - Retirar SBN completamente
  - Asignar Epiro/Albania/W. Macedonia a:
    - Reinos griegos independientes, o
    - Diádocos/sucesores alejandrinos, o
    - WLD (Tierras Salvajes)

#### 6. **Etruria vs Iberia - DUPLICACIÓN GEOGRÁFICA CONFUSA**
- **ETR en Argelia** y **IBR en Iberia** tienen nombres similares pero ETR no debería existir
- **Recomendación:** Resolver el problema de ETR primero

---

## 🗺️ ANÁLISIS GEOGRÁFICO DETALLADO POR REGIÓN

### **MEDITERRÁNEO OCCIDENTAL**
| Región | Actual (Mod) | Histórico ~264 BCE | Precisión |
|--------|-------------|-------------------|-----------|
| Italia | SPQ | República Romana | ✅ |
| Sicilia | SYC | Tiranía griega (Siracusa) | ✅ |
| Cerdeña | CRG | Imperio Púnico (Cartago) | ✅ |
| Túnez | CRG | Imperio Púnico | ✅ |
| Argelia O. | ETR | Bereber/Púnico/Salvaje | ❌ ETR INCORRECTO |
| Argelia E. | ETR | Bereber/Púnico/Salvaje | ❌ ETR INCORRECTO |
| Córdoba (Iberia) | CRG | Púnico/Tartésida | ✅ (CRG plausible) |
| Iberia (resto) | IBR | Tribus ibéricas | ✅ |
| Provenza | GLN | Tribus galas | ✅ |
| Marruecos N. | PHN | Púnico/Bereber (NO Fenicia) | ❌ PHN INCORRECTO |

### **MEDITERRÁNEO ORIENTAL & LEVANTE**
| Región | Actual (Mod) | Histórico ~264 BCE | Precisión |
|--------|-------------|-------------------|-----------|
| Grecia Continental | GRC | Estados griegos independientes | ✅ (incompleto) |
| Peloponeso | LAC | Sparta & Liga Aquea | ✅ (Sparta controlaba) |
| Epiro | SBN | Reinos griegos/epiotes (NO Sabines) | ❌ SBN INCORRECTO |
| Macedonia | MCD | Monarquía macedónica | ✅ |
| Tracia | THR | Reinos tracios | ✅ |
| Anatolia O. (Izmir) | LYD | Seleucida (NO Lidia) | ❌ LYD INCORRECTO |
| Anatolia O. (Antalya) | LYD | Seleucida (NO Lidia) | ❌ LYD INCORRECTO |
| Mesopotamia | ASS | Seleucida (NO Asiria) | ❌ ASS INCORRECTO |
| Siria | ASS | Seleucida (NO Asiria) | ❌ ASS INCORRECTO |
| Aleppo | ASS | Seleucida (NO Asiria) | ❌ ASS INCORRECTO |
| Levante (Fenicia) | PHN (no asignado) | Seleucida & reyes locales | ❌ PHN INCOMPLETO |
| Marruecos | PHN | Púnico/Bereber (NO Fenicia) | ❌ PHN INCORRECTO |
| Égypte/Cirenaica | KMT | Imperio Ptolemaico | ✅ |

### **BALCANES & EUROPA CENTRAL**
| Región | Actual (Mod) | Histórico ~264 BCE | Precisión |
|--------|-------------|-------------------|-----------|
| Italia Central | SPQ | República Romana | ✅ |
| Italia Sur (Puglia) | SMN | Confederación samnita | ✅ |
| Croacia | ILL | Reinos ilirios | ✅ |
| Albania | SBN | Reinos griegos (NO Sabines) | ❌ SBN INCORRECTO |
| W. Macedonia | SBN | Reinos griegos (NO Sabines) | ❌ SBN INCORRECTO |

---

## 🔴 PROBLEMAS CRÍTICOS (PRIORIDAD ALTA)

### **P1: Asiria (ASS) - Anacrónica**
- **Causa:** Asiria histórica cayó 609 BCE; mod la coloca en 264 BCE
- **Impacto:** Rompe inmersión histórica, 355 años de error
- **Solución:** 
  1. Renombrar a Seleucida (SEL)
  2. O mover a período diferente del mod (ej. 1000 BCE)

### **P2: Etruria (ETR) - Anacrónica + Geografía Imposible**
- **Causa:** Etruria desapareció como estado 390 BCE; Argelia nunca fue etrusca
- **Impacto:** Crítico, completamente incorrecto
- **Solución:**
  1. Retirar ETR o moverla a Italia central
  2. Asignar Argelia a WLD, CRG, o crear tag bereber

### **P3: Sabines (SBN) - Anacrónica + Geografía Imposible**
- **Causa:** Sabines desapareció como entidad ~290 BCE; no controlaban Epiro/Macedonia
- **Impacto:** Crítico
- **Solución:**
  1. Retirar SBN
  2. Asignar territorios a reinos griegos o WLD

### **P4: Lidia (LYD) - Anacrónica**
- **Causa:** Lidia no era independiente en 264 BCE (bajo Seleucidas desde 546 BCE)
- **Impacto:** Alto
- **Solución:**
  1. Renombrar a Seleucida
  2. O crear tag específico para sucesores alejandrinos menores

### **P5: Fenicia (PHN) - Geografía Incorrecta**
- **Causa:** PHN en Marruecos (debería ser Levante); PHN es tag sin territorio levantino
- **Impacto:** Medio-Alto
- **Solución:**
  1. Mover PHN a Siria/Líbano (estados seleucidas)
  2. Asignar Marruecos a CRG o crear tag bereber

---

## 🟡 PROBLEMAS SECUNDARIOS (PRIORIDAD MEDIA)

| Problema | Ubicación | Nota | Solución |
|----------|-----------|------|----------|
| Grecia incompleta | GRC = solo estado 47 | GRC debería incluir más territorios griegos | Expandir GRC o crear tags regionales |
| Sparta limitado | LAC = solo Peloponeso | LAC podría incluir alianzas/influencia | Actual es aceptable |
| W. Macedonia asignado a SBN | Estado 970 | Debería ser MCD o reino griego | Reasignar a MCD |

---

## 📋 RESUMEN DE RECOMENDACIONES

### **OPCIÓN 1: Cambiar Período Histórico del Mod**
Si el mod cambia a un período anterior (~600-500 BCE):
- Asiria, Lidia, Etruria serían correctas
- Requeriría reconfiguración completa de tecnologías/dinámicas
- **No recomendado** (demasiado trabajo)

### **OPCIÓN 2: Aplicar Correcciones Mínimas**
**Cambios necesarios:**
1. Renombrar ASS → SEL (Seleucida) 
   - Mesopotamia, Siria, Aleppo → Imperio Seleucida
   - Requiere actualizar localizaciones, tecnologías, colores, líderes

2. Retirar ETR (Etruria) o moverla a Italia central
   - Argelia Occidental/Oriental → WLD
   - Crear nuevo tag "BER" (Bereberes) si se desea

3. Retirar SBN (Sabines) o limitarlo a Italia
   - Epiro, Albania, W. Macedonia → WLD o nuevos tags griegos
   - SMN (Samnitas) ya está en Puglia correctamente

4. Renombrar LYD → SEL o crear tag "HEL" (Helenísticos)
   - Izmir, Antalya → Seleucida

5. Mover PHN (Fenicia) a Levante
   - Marruecos N. (461) → WLD o crear BER
   - Asignar Levante a PHN o SEL

**Impacto:** Cambios significativos en localizaciones, tecnologías, líderes, focos nacionales

### **OPCIÓN 3: Aceptar Anacronismos**
- No hacer cambios
- Documentar que mod usa "timeline ficticio" con naciones antiguas
- **No recomendado** para precisión histórica

---

## 🎯 RECOMENDACIÓN FINAL

**Implementar OPCIÓN 2 (Correcciones Mínimas) porque:**
- ✅ Mejora inmersión histórica sin rehacer el mod
- ✅ Respeta tonalidad ~264 BCE (era Primera Guerra Púnica)
- ✅ Elimina anacronismos principales
- ✅ Mantiene estructura de 18 tags, solo renombra

**Prioridad de cambios:**
1. 🔴 **CRÍTICA:** ASS → SEL, retire SBN
2. 🔴 **CRÍTICA:** Muevaetería a Italia central o retire
3. 🟡 **ALTA:** Lidia → Seleucida o Helenístico
4. 🟡 **ALTA:** Fenicia a Levante

---

## 📝 NOTAS DE IMPLEMENTACIÓN

Si se implementan correcciones, necesitarán actualizarse:
- ✏️ `common/country_tags/spqr_tags.txt` - Cambiar tags (ASS→SEL, etc.)
- ✏️ `common/countries/` - Cambiar archivos de países
- ✏️ `localisation/` - Cambiar nombres en inglés/español
- ✏️ `gfx/flags/` - Cambiar banderas por país
- ✏️ `gfx/leaders/` - Cambiar carpetas de líderes
- ✏️ `history/countries/` - Cambiar archivos históricos
- ✏️ `history/units/` - Cambiar divisiones iniciales
- ✏️ `national_focus/` - Revisar árboles de focos si usan nombres de países
- ✏️ `common/ideas/` - Revisar ideas por país
- ✏️ `events/` - Revisar eventos con referencias a países

