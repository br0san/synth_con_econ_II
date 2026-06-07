# Autocrítica Metodológica — Plan de Reframing del Trabajo Final

> **Fecha:** 2026-06-07
> **Versión:** v1 — Síntesis del reporte crítico externo y plan de acción para el Camino A
> **Decisión:** Transformar el trabajo de "el SCM encuentra efecto negativo del IT" a "el SCM no puede responder esta pregunta — y he aquí por qué eso es informativo"

---

## 0. Diagnóstico de partida

### Lo que tenemos

Un documento Quarto autocontenido y reproducible (`01_analisis.qmd`) que:

- Estima el efecto del IT (2001) sobre la formación bruta de capital fijo en México vía SCM
- Donor pool: economías no-OCDE (83 donantes)
- RMSPE pre-tratamiento: 0.1074 (excelente)
- Gap promedio post-2001: −3.7 pp del PIB, mínimo de ~−7.3 pp hacia 2011–2012
- Placebos in-space: pseudo p-value ≈ 0.75
- Conclusión actual: "efecto económicamente relevante pero estadísticamente no concluyente"

### El problema

El trabajo actual **reconoce** las limitaciones (p-value alto, variables omitidas, no identifica mecanismos) pero no las **desarrolla**. La estructura narrativa sigue siendo "encontramos un efecto negativo, aunque no es significativo". Esto es débil académicamente porque:

1. Un p-value de 0.75 no es "no concluyente": es evidencia de **ausencia de efecto distinguible del ruido**
2. El documento no aborda los sesgos de identificación más graves (China Shock, inversión pública)
3. La Crítica de Lucas y SUTVA —objeciones fundamentales a usar SCM para evaluar regímenes monetarios— están ausentes
4. Las referencias usadas son mayoritariamente de la literatura de IT; faltan las de metodología SCM crítica y las de determinantes estructurales de la inversión en México

### La oportunidad

El reporte crítico externo (fuente no citada explícitamente en este planning, pero cuyas ideas se incorporan como insumo analítico) identifica **cuatro dimensiones de crítica** que, desarrolladas adecuadamente, transforman el trabajo en una pieza de *metacrítica metodológica*: un análisis que usa el SCM no para responder la pregunta causal sino para demostrar **por qué el SCM no es la herramienta adecuada** para evaluar regímenes monetarios en presencia de choques globales coincidentes y cambios estructurales en el régimen de formación de expectativas.

Esto es más honesto intelectualmente y más interesante académicamente que insistir en un resultado no significativo.

---

## 1. Síntesis destilada del reporte crítico externo

> El reporte original contiene ~20,000 palabras pero sufre de extensos pasajes de texto degenerado (repetición infinita) en las secciones 7.2, 7.3 y 7.4. Lo que sigue es la **destilación de las ideas sustanciales**, preservando solo lo argumentativamente válido.

### Dimensión I: La Crítica de Lucas (1976) — Inestabilidad paramétrica

**El argumento central:**

La adopción del IT no es un ajuste marginal de política sino un **cambio de régimen estructural** que altera el Data Generating Process (DGP). Antes del IT, los agentes económicos en México operaban bajo un régimen de alta inflación con indexación retrospectiva (backward-looking). Después del IT —y especialmente tras la consolidación de la autonomía de Banxico—, los agentes transitaron hacia una formación de expectativas prospectiva (forward-looking).

**Por qué invalida el SCM:**

El SCM construye el contrafactual estimando ponderaciones $w_j$ que minimizan la distancia entre México y su sintético en el período pre-tratamiento (1990–2000). Estas ponderaciones reflejan la estructura de correlaciones **bajo el régimen antiguo**. Si el DGP cambió en 2001, esas ponderaciones **dejaron de ser válidas** en el instante mismo de la adopción del IT. El "México sintético" post-2001 no es un contrafactual creíble: es una extrapolación mecanicista de parámetros que ya no gobiernan la economía mexicana.

**Referencias clave:**
- Lucas, R.E. (1976). "Econometric Policy Evaluation: A Critique." *Carnegie-Rochester Conference Series on Public Policy*, 1, 19–46.
- Rudebusch, G. (2005). "Assessing the Lucas Critique in Monetary Policy Models." *Journal of Money, Credit and Banking*, 37(2), 245–272.
- Ramos-Francia, M. & Torres, A. (2005). "Reducing Inflation Through Inflation Targeting: The Mexican Experience." *Banxico Working Paper 2005-01*. — Documenta la transición de Banxico hacia reglas de Taylor prospectivas.

---

### Dimensión II: El "China Shock" como variable omitida fundamental

**El argumento central:**

El ingreso de China a la OMC ocurrió en **diciembre de 2001** —el mismo año que México adoptó formalmente el IT—. Este evento generó un choque comercial masivo y asimétrico:

- México, como economía manufacturera integrada al mercado norteamericano vía TLCAN, sufrió un **desplazamiento competitivo severo**: las exportaciones chinas erosionaron las ventajas arancelarias mexicanas en el mercado estadounidense
- Las industrias manufactureras más intensivas en capital fueron las más afectadas: la caída en la rentabilidad sectorial forzó la cancelación de planes de expansión de capacidad instalada
- El efecto sobre la formación bruta de capital fijo fue **directo, masivo y enteramente exógeno a la política monetaria**

**Por qué el SCM es ciego a esto:**

El SCM usa predictores macroeconómicos altamente agregados (crecimiento del PIB, población, inflación, dummy de exportador petrolero). No incluye ninguna medida de exposición comercial a China, integración en cadenas de valor, o vulnerabilidad manufacturera. La coincidencia temporal exacta (2001) hace imposible que el algoritmo discierna entre el efecto del IT y el efecto del China Shock: **atribuye mecánicamente al IT lo que fue un choque comercial global**.

**Por qué otros países del donor pool no sufrieron igual:**

Muchos países del donor pool (Mongolia, Bolivia, Mauritania, Madagascar) son exportadores de materias primas que se **beneficiaron** del super-ciclo de commodities generado precisamente por la demanda china. Mientras México sufría desindustrialización, estos países experimentaban booms de exportaciones primarias. El "gap sintético" captura esta divergencia asimétrica, no un efecto del IT.

**Referencias clave:**
- Autor, D., Dorn, D. & Hanson, G. (2016). "The China Shock: Learning from Labor-Market Adjustment to Large Changes in Trade." *Annual Review of Economics*, 8, 205–240.
- "The China Shock 2.0: How China's Ongoing Export Surge Differs from the Early 2000s." *FEDS Notes*, Federal Reserve Board (2026).
- "Mexico Is Facing a Second — and Worse — 'China Shock'." *Council on Foreign Relations* (2025–2026).
- "Trade and factor intensity, and the transmission of the global shock to labor: A panel analysis of the fall of the labor income share in the Mexican manufacturing sector." *Economic Systems*, 47(1), 2023.

---

### Dimensión III: El colapso de la inversión pública y la austeridad fiscal

**El argumento central:**

A partir de los años 2000, México adoptó un paradigma de **austeridad fiscal** que desplomó la inversión pública federal. La formación bruta de capital del sector público cayó a niveles del 3–4% del PIB, entre los más bajos de América Latina. La literatura sobre determinantes de la inversión en México documenta un fuerte efecto de **crowding-in**: la inversión pública en infraestructura (carreteras, puertos, energía, telecomunicaciones) complementa y cataliza la inversión privada al reducir costos logísticos y aumentar la tasa de retorno esperada de los proyectos de capital.

**Evidencia econométrica:**

Estudios con modelos VAR y de cointegración para el período 2005–2020 identifican consistentemente dos determinantes principales del estancamiento de la inversión privada en México:
1. El retiro de la inversión pública (crowding-in invertido)
2. La histéresis del crecimiento del PIB (bajo dinamismo de la demanda agregada)

**Por qué el SCM es ciego a esto:**

El SCM no incluye la inversión pública como predictor ni controla por el sesgo de política fiscal. Atribuir la caída de la inversión total al IT cuando el Estado se retiró simultáneamente de su rol como inversor en infraestructura es un error de atribución.

**Referencias clave:**
- "El estancamiento de la inversión privada en México: un análisis de sus determinantes en el período 2005-2020." *Redalyc / Revista de Economía*.
- "Los determinantes de la inversión privada en México (1988-2015)." *Facultad de Economía, UNAM, Economía Informa*, No. 413.
- "Efecto de la incertidumbre sobre las tasas de interés de largo plazo." *Banxico, Informe Trimestral*, recuadro.

---

### Dimensión IV: Violación de SUTVA y riesgos de sobreajuste

**Sub-dimensión IV.a: SUTVA (Stable Unit Treatment Value Assumption)**

El SCM exige **ausencia de interferencia cruzada** (spillovers) entre la unidad tratada y las unidades de control. Esto es insostenible en macroeconomía global:

- La Reserva Federal de EE.UU. afecta las condiciones financieras de **todas** las economías del donor pool simultáneamente
- El China Shock y el super-ciclo de commodities afectaron de forma **asimétrica** a México (manufacturero, integrado a EE.UU.) vs. los donantes (muchos exportadores de materias primas que se beneficiaron)
- La crisis financiera global de 2008–2009 fue un choque común con transmisión heterogénea

**Sub-dimensión IV.b: Sobreajuste (over-fitting)**

El período pre-tratamiento (1990–2000) incluye la crisis del Tequila (1994–1995), un evento de volatilidad extrema idiosincrásica de México. Conseguir un RMSPE de 0.1074 usando una combinación de países tan disímiles (Mongolia, Mauricio, Bolivia, Mauritania...) sugiere que el algoritmo **sobreajustó ruido** en lugar de capturar la señal estructural.

**Sub-dimensión IV.c: Interpretación del pseudo p-value**

Un p-value de 0.75 significa que **el 75% de los placebos generan gaps igual o más extremos que el de México**. Esto no es "no concluyente": es evidencia de que el efecto estimado es indistinguible del ruido aleatorio del sistema macroeconómico global. La distinción entre "significancia estadística" y "relevancia económica" que hace el documento actual es una falacia: en el marco del SCM, el pseudo p-value **es** el test de relevancia. Si 75% de los placebos muestran el mismo "efecto", el efecto no existe.

**Referencias clave:**
- Abadie, A. (2021). "Using Synthetic Controls: Feasibility, Data Requirements, and Methodological Aspects." *Journal of Economic Literature*, 59(2), 391–425.
- Adhikari, B. (2022). "A Guide to Using the Synthetic Control Method." *The American Economist*, 67(1), 46–63.
- "Identification and Bayesian Inference for Synthetic Control Methods with Spillover Effects." *The Econometrics Journal* / arXiv:2408.00291 (2025–2026).
- "Synthetic Controls with Machine Learning: Application on the Effect of Labour Deregulation on Worker Productivity in Brazil." *BIS Working Paper No. 1181*.
- "Synthetic Control Method for Dutch Policy Evaluation." *PMC/NIH* (2023).

---

## 2. Fuentes seleccionadas para profundizar

### Prioridad 1 — Ya cargadas en NotebookLM (5 de 6)

| # | Referencia | Dimensión | Estado |
|---|---|---|---|
| 1 | **Lucas, R.E. (1976).** "Econometric Policy Evaluation: A Critique." | I — Crítica de Lucas | ✅ Cargada |
| 2 | **Rudebusch, G. (2005).** "Assessing the Lucas Critique in Monetary Policy Models." | I — Crítica de Lucas | ✅ Cargada |
| 3 | **Autor, Dorn & Hanson (2016).** "The China Shock." | II — China Shock | ✅ Cargada |
| 4 | **"El estancamiento de la inversión privada en México (2005-2020)."** Redalyc | III — Inversión pública | ✅ Cargada |
| 5 | **Christensen, Fischer & Rudebusch (2024).** "Inflation Expectations and Risk Premia in Emerging Bond Markets: Evidence from Mexico." | Contra-evidencia de credibilidad débil | ✅ Cargada |

### Prioridad 2 — Pendientes de cargar en NotebookLM

| # | Referencia | Dimensión | Justificación |
|---|---|---|---|
| 6 | **"Los determinantes de la inversión privada en México (1988-2015)."** UNAM | III — Inversión pública | Complementa la #4 con estimaciones del multiplicador de crowding-in |
| 7 | **Ramos-Francia & Torres (2005).** "Reducing Inflation Through Inflation Targeting: The Mexican Experience." *Banxico WP 2005-01* | Contra-evidencia | Documenta la transición a reglas de Taylor prospectivas en Banxico |
| 8 | **Abadie, A. (2021).** "Using Synthetic Controls: Feasibility, Data Requirements, and Methodological Aspects." *JEL* | IV — Límites SCM | Advierte sobre sobreajuste y requisitos de validez del SCM |

### Prioridad 3 — Citar sin necesidad de NotebookLM (uso acotado)

| # | Referencia | Uso específico |
|---|---|---|
| 9 | **"Identification and Bayesian Inference for SCM with Spillover Effects"** (arXiv:2408.00291) | Una frase sobre desarrollos recientes en SUTVA para SCM |
| 10 | **"Anclaje de las Expectativas de Inflación ante Choques de Oferta Adversos"** (Banxico, varios años) | Evidencia de que las expectativas se anclaron — contra McCloud |
| 11 | **"Inflation targeting in Mexico: evolution, achievements and policy lessons."** *BIS Papers No. 143* (2024) | Síntesis institucional del éxito del IT en México |
| 12 | **"Dinámica de la Prima por Plazo y sus Determinantes: El Caso Mexicano."** *Banxico WP* | Evidencia de compresión de prima por riesgo inflacionario |
| 13 | **"Efecto de la incertidumbre sobre las tasas de interés de largo plazo."** *Banxico, Informe Trimestral* | Efecto de incertidumbre de política económica sobre inversión |
| 14 | **"Trade and factor intensity, and the transmission of the global shock to labor."** *Economic Systems*, 47(1), 2023 | China Shock: efecto asimétrico por intensidad de capital |

---

## 3. Estructura propuesta del nuevo documento

### Sección 1: Introducción (reescritura parcial)

**Mantener:**
- Motivación del tema (IT en México, relevancia para política)
- Pregunta de investigación
- Hipótesis H0 y H1

**Agregar:**
- Un párrafo que siembre el giro metodológico: "Este trabajo evalúa no solo el efecto del IT sino, de manera más fundamental, **si el SCM es la herramienta adecuada para esta pregunta**. La respuesta, anticipamos, es que no —y entender por qué es informativo para la práctica de la evaluación de políticas macroeconómicas."

### Sección 2: Marco teórico (ampliación sustancial)

**Reorganizar en tres subsecciones:**

**2.1 El IT como régimen de política monetaria** (≈lo actual, condensado)
- Svensson (1998, 2010), canal de expectativas → inversión

**2.2 Evidencia empírica sobre el IT** (≈lo actual, condensado)
- La heterogeneidad de resultados como hecho estilizado
- McCloud (2022) y Bambe (2023) como antecedentes directos

**2.3 Límites metodológicos del SCM en macroeconomía de panel** (NUEVO — ~4–5 párrafos)
- La Crítica de Lucas y la invarianza paramétrica
- El supuesto SUTVA y su inviabilidad en macro global
- Riesgos de sobreajuste en ventanas de alta volatilidad
- Límites de la inferencia por placebos con donor pools pequeños
- El SCM como herramienta de "casos ideales", no de preguntas con choques coincidentes

### Sección 3: Datos (≈igual)

Mantener la sección actual. Es sólida.

### Sección 4: Análisis descriptivo (ampliación)

**Agregar 2–3 gráficas/series adicionales:**

1. **Inversión pública federal como % del PIB** (para la Dimensión III) — fuente: WDI `NE.CON.GOVT.ZS` o similar
2. **Exportaciones manufactureras de México** (para la Dimensión II) — fuente: WDI `TX.VAL.MANF.ZS.UN` o similar
3. **Crédito doméstico al sector privado (% PIB)** — fuente: WDI `FS.AST.PRVT.GD.ZS`

Cada serie con breve interpretación vinculada a las dimensiones críticas.

### Sección 5: Estrategia empírica (reescritura parcial)

**Mantener:**
- Explicación técnica del SCM
- Implementación con pysyncon

**Agregar:**
- Un apartado "Supuestos del SCM y su plausibilidad en este contexto" que enumere explícitamente:
  1. Invarianza paramétrica (Crítica de Lucas)
  2. SUTVA / no interferencia
  3. Ausencia de choques coincidentes no controlados
  4. Ajuste pre-tratamiento como condición necesaria pero no suficiente
- Cada supuesto con una frase sobre su fragilidad en el caso mexicano (desarrollada en §7)

### Sección 6: Resultados (≈igual)

Los resultados numéricos no cambian. Lo que cambia es **cómo se presentan**:

- Ya no decir "el gap es negativo y grande, ergo el IT dañó la inversión"
- Decir: "el SCM produce un gap negativo y grande. La pregunta relevante no es si el gap *existe* sino si *significa lo que parece significar*. Las secciones siguientes examinan esta cuestión."

### Sección 7: Discusión — Las cuatro dimensiones críticas (REESCRITURA TOTAL)

Esta sección **reemplaza** la discusión actual. Estructura:

**7.1 ¿Es válido el contrafactual sintético? La Crítica de Lucas**
- Desarrollo de 3–4 párrafos
- Evidencia de que Banxico sí logró anclar expectativas (Christensen et al. 2024, Ramos-Francia & Torres 2005, Banxico recuadros)
- Implicación: el DGP cambió; las ponderaciones pre-2001 no son extrapolables
- Conclusión parcial: el "México sin IT" del SCM es una proyección de un régimen que dejó de existir

**7.2 El China Shock: ¿política monetaria o comercio global?**
- Desarrollo de 3–4 párrafos
- Cronología exacta: OMC diciembre 2001 = adopción IT 2001
- Mecanismo de desplazamiento manufacturero y caída de inversión en sectores capital-intensivos
- Asimetría: donantes exportadores de commodities se beneficiaron; México sufrió
- Conclusión parcial: el gap sintético captura el diferencial de exposición al China Shock, no el efecto del IT

**7.3 La inversión pública como determinante omitido**
- Desarrollo de 2–3 párrafos
- Evidencia VAR/cointegración de los determinantes de la inversión privada en México
- El crowding-in como mecanismo: sin inversión pública, la privada se estanca
- Conclusión parcial: atribuir la caída al IT ignorando la austeridad fiscal es un error de atribución

**7.4 SUTVA, sobreajuste y los límites de la inferencia**
- Desarrollo de 2–3 párrafos
- Spillovers globales (Fed, crisis financiera, commodities) que contaminan el donor pool
- Over-fitting: RMSPE 0.1074 conseguido sobre una ventana que incluye la crisis del Tequila, usando países sin relación estructural con México
- El p-value de 0.75: no es "no concluyente", es evidencia de ausencia de señal
- Conclusión parcial: incluso si no existieran las críticas anteriores, la inferencia no soporta la conclusión de un efecto causal

**7.5 Síntesis: lo que el SCM puede y no puede decirnos**
- 1–2 párrafos que integren las cuatro dimensiones
- El SCM es una herramienta poderosa para casos donde el tratamiento es el único cambio estructural relevante en el entorno de la unidad tratada. No es el caso de México en 2001.

### Sección 8: Conclusiones (reescritura total)

**Estructura:**

1. **Sobre la pregunta de investigación:** No podemos afirmar que el IT haya tenido un efecto causal negativo sobre la inversión. Tampoco podemos afirmar que no lo haya tenido. Lo que podemos afirmar es que el SCM no es capaz de discernirlo.

2. **Sobre el método:** Este ejercicio es informativo no por su respuesta sino por sus límites. Ilustra los peligros de aplicar SCM a preguntas de política monetaria sin atender a la Crítica de Lucas, a la coincidencia de choques globales, y a los determinantes estructurales omitidos.

3. **Sobre México:** La evidencia institucional —anclaje de expectativas, compresión de primas de riesgo, reglas de Taylor prospectivas— sugiere que el IT fue, en balance, una política estabilizadora exitosa. Si la inversión cayó, no fue por el IT.

4. **Extensiones:** Augmented SCM, Generalized SCM, o métodos de control por exposición comercial podrían abordar algunas de estas limitaciones. Pero la lección principal es anterior a la elección del estimador: ninguna herramienta econométrica puede aislar el efecto de una política cuando esta coincide con una constelación de choques estructurales de escala global.

---

## 3.5 ⚠️ CORRECCIONES TRAS NOTEBOOKLM (2026-06-07)

> Las consultas a las 5 fuentes revelaron **4 correcciones importantes** al planning original. Ver `resumenes-fuentes-autocritica.md` para detalle completo.

### Corrección 1: Rudebusch (2005) DEBILITA la Dimensión I

**Lo que asumíamos:** La Crítica de Lucas invalida el SCM porque los parámetros cambian ante un nuevo régimen monetario.

**Lo que Rudebusch encuentra:** Los parámetros de modelos de política monetaria son **sorprendentemente estables** ante cambios de régimen. "There is little evidence that the Lucas critique is empirically important." Las pruebas de Chow rechazan estabilidad en <16% de los casos.

**Estrategia revisada para Dimensión I:**
- NO afirmar que la Crítica de Lucas "invalida" el SCM
- SÍ argumentar que Lucas advierte sobre cambios "fuera de la experiencia histórica" — y el IT lo fue para México
- Rudebusch mismo advierte: una representación invariante podría fallar si el nuevo régimen implica "políticas fuera de la experiencia histórica"
- Usar esto como tensión metodológica (debate no zanjado), no como refutación categórica

### Corrección 2: China Shock — cronología matizada y sectores afectados

**Lo que asumíamos:** El China Shock empezó exactamente en 2001 con la OMC; afectó más a industrias capital-intensivas.

**Lo que Autor et al. documentan:** El shock empezó en los 1990s y se **aceleró** post-2001. Las más afectadas fueron industrias **trabajo-intensivas** (no capital-intensivas). México: "Growing Chinese import competition increases plant exit and reduces firm growth."

**Estrategia revisada para Dimensión II:**
- Enfatizar la **aceleración** post-2001, no el inicio absoluto
- Enfatizar la **asimetría**: exportadores de commodities (muchos en el donor pool: Mongolia, Bolivia, Mauritania) se beneficiaron; manufactureros como México sufrieron
- Esta asimetría contamina el gap sintético independientemente de la fecha exacta

### Corrección 3: Determinantes de inversión — crowding-OUT, no crowding-in

**Lo que asumíamos:** La inversión pública tiene efecto crowding-in sobre la privada; su caída post-2001 explica el gap.

**Lo que Cruz & Brid (2018) encuentran:**
- Crowding-out neto de -0.15 pp (muy pequeño)
- La caída de inversión pública **precede** a 2001: mínimo en 1995-00 (3.04% del PIB), recuperación parcial post-2001 (4.37%)
- La tasa de interés NO es determinante significativo; el IT no se menciona
- Determinantes: PIB, gasto público, inversión privada rezagada

**Estrategia revisada para Dimensión III:**
- NO argumentar crowding-in de inversión pública
- SÍ argumentar que la política monetaria NO aparece como determinante de la inversión en México
- La inversión pública sí cayó (7.92% → 3.04%) pero la caída fue en los 90s, no post-2001
- Esta dimensión se vuelve más débil de lo planeado; posiblemente fusionarla con Dimensión II o tratarla como "determinantes omitidos" en general

### Corrección 4: Fuente de expectativas

**Lo que asumíamos:** Teníamos a Christensen, Fischer & Rudebusch (2024, JIE).

**Realidad:** El paper en NotebookLM es **Beauregard et al. (2021)**, un paper relacionado pero distinto. Hallazgos: expectativas ancladas en ~2.87% (dic 2019), prima comprimida desde 2009, pero NO discute implicaciones para inversión productiva.

**Acción:** `.bib` ya corregido (`christensen2024` → `beauregard2021`). Si se consigue Christensen et al. (2024), agregarlo como fuente adicional.

### Re-calibración de las 4 dimensiones

A la luz de estos hallazgos, el peso relativo de cada dimensión cambia:

| Dimensión | Estado original | Tras NotebookLM |
|---|---|---|
| **I — Crítica de Lucas** | ⭐⭐⭐ Fuerte | ⭐⭐ Matizada (Rudebusch la debilita) |
| **II — China Shock (asimetría)** | ⭐⭐⭐ Fuerte | ⭐⭐⭐ Muy fuerte (la asimetría commodities vs manufacturas es el argumento más sólido) |
| **III — Inv. pública / determinantes** | ⭐⭐ Media | ⭐ Débil (crowding-out, no crowding-in; caída pre-2001) |
| **IV — SUTVA / sobreajuste / p-value** | ⭐⭐⭐ Fuerte | ⭐⭐⭐ Muy fuerte (Abadie 2021 + p-value 0.75 + donor pool disímil) |

La Dimensión II (China Shock asimétrico) y la Dimensión IV (SUTVA/sobreajuste) emergen como los pilares más sólidos. La Dimensión I debe matizarse. La Dimensión III debe reformularse o fusionarse.

---

## 4. Plan de implementación

### Fase 1: Investigación (NotebookLM + lecturas dirigidas)

| Tarea | Responsable | Estado |
|---|---|---|
| 1.1 Cargar referencias prioridad 1 en NotebookLM y generar resúmenes | Bruno | ✅ 5/5 consultadas |
| 1.2 Cargar referencias prioridad 2 (#6, #7, #8) en NotebookLM | Bruno | Pendiente (baja prioridad — ver recalibración) |
| 1.3 Generar resúmenes orientados por dimensión crítica | Claude | ✅ Completado en `resumenes-fuentes-autocritica.md` |
| 1.4 Extraer evidencia concreta y corregir el planning | Claude | ✅ Completado (§3.5 de este documento) |

### Fase 2: Nuevo `.bib` y referencias

| Tarea | Responsable |
|---|---|
| 2.1 Agregar ~14 referencias nuevas a `referencias.bib` | Claude |
| 2.2 Verificar que todas las citas en el nuevo texto tengan entrada en el `.bib` | Claude |

### Fase 3: Datos adicionales para §4 (análisis descriptivo ampliado)

| Tarea | Responsable |
|---|---|
| 3.1 Verificar disponibilidad en WDI de: inversión pública (`NE.CON.GOVT.ZS`), exportaciones manufactureras (`TX.VAL.MANF.ZS.UN`), crédito al sector privado (`FS.AST.PRVT.GD.ZS`) | Claude (sobre el CSV existente o vía consulta) |
| 3.2 Si están disponibles en el panel actual, generar las series; si no, documentar la limitación | Claude |

### Fase 4: Escritura del nuevo `01_analisis.qmd`

| Tarea | Descripción | Prioridad |
|---|---|---|
| 4.1 Reescribir §2.3 (límites del SCM) | Nueva subsección sobre Lucas, SUTVA, over-fitting | Alta |
| 4.2 Reescribir §1 (introducción) | Agregar párrafo de giro metodológico | Alta |
| 4.3 Reescribir §5 (estrategia empírica) | Agregar apartado de supuestos y su plausibilidad | Alta |
| 4.4 Reescribir §7 (discusión) | Las cuatro dimensiones críticas — **el corazón del nuevo paper** | Alta |
| 4.5 Reescribir §8 (conclusiones) | Reorientar hacia "el método no es adecuado" | Alta |
| 4.6 Ampliar §4 (análisis descriptivo) | Agregar series de inversión pública, crédito, exportaciones | Media |
| 4.7 Ajustar §6 (resultados) | Cambiar el tono de presentación del gap y p-value | Media |
| 4.8 Revisar consistencia global | Que no queden residuos del framing anterior | Media |

### Fase 5: Verificación y entrega

| Tarea | Responsable |
|---|---|
| 5.1 Render completo (Quarto → PDF + notebook) sin errores | Claude |
| 5.2 Verificar que todas las referencias cruzadas funcionan | Claude |
| 5.3 Commit + push final | Bruno/Claude |

---

## 5. Criterios de éxito del nuevo documento

- [ ] El lector entiende que la contribución principal es **metodológica**, no sustantiva
- [ ] Las cuatro dimensiones críticas están desarrolladas con evidencia concreta, no solo con argumentos teóricos
- [ ] El documento reconoce los resultados del SCM (no los esconde) pero los reinterpreta a la luz de las críticas
- [ ] McCloud (2022) queda como referencia metodológica, no como autoridad contra la cual peleamos
- [ ] La Crítica de Lucas está explicada de forma accesible para un lector de Econometría II
- [ ] El China Shock está documentado con fechas, mecanismos y referencias precisas
- [ ] La conclusión es clara: el SCM no puede responder esta pregunta — y eso es un hallazgo en sí mismo
- [ ] El notebook es reproducible: Kernel → Restart & Run All sin errores
- [ ] Las limitaciones son frontales y honestas, no relegadas a un párrafo al final

---

## 6. Notas sobre el tono

- **NO** es un ataque a McCloud (2022). McCloud hizo un análisis riguroso con la mejor metodología disponible. Nuestra crítica es al **método**, no al paper.
- **NO** es un documento de "todo está mal". Es un documento de "el SCM funciona bajo condiciones X; México en 2001 no las cumple; aprendemos más de ese desajuste que de forzar una respuesta".
- **SÍ** es un documento que toma posición: la honestidad intelectual exige decir cuando una herramienta no es adecuada, incluso si eso debilita la "historia" del paper.
- **SÍ** usa evidencia institucional mexicana (Banxico, Christensen et al.) para mostrar que el IT fue probablemente exitoso — no como afirmación categórica, sino como contrapeso al framing negativo.

---

*Este documento es el punto de partida para la Fase 4 de escritura. Se actualizará con los hallazgos de NotebookLM (Fase 1) antes de comenzar a escribir.*
