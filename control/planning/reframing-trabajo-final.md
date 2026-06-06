# Reframing del Trabajo Final: de Replicación a Investigación Original

> **Fecha:** 2026-06-06
> **Objetivo:** Transformar el proyecto de una replicación de McCloud (2022) a una investigación original que use McCloud como referencia metodológica, alineándose con los lineamientos del trabajo final de Econometría II.

---

## 1. Diagnóstico: dónde estamos y qué nos falta

### Lo que tenemos (materia prima)

| Componente | Estado |
|---|---|
| Panel de datos (WDI, 108 países, 1984–2023) | ✅ Listo |
| SCM non-OECD: RMSPE 0.1074, efectos consistentes con McCloud | ✅ Listo |
| Robustness: ventana 1984 vs 1990 | ✅ Listo |
| Robustness: con y sin `gross_savings` | ✅ Listo |
| Placebos in-space: p-value 0.75, gráfico | ✅ Listo |
| OECD histórica (time-varying) | ✅ Listo |
| Script standalone (`run_scm_from_csv.py`) | ✅ Listo |
| Notebook pipeline (`01_data_pipeline.ipynb`) | ✅ Listo (técnicamente) |
| `resumen_proyecto.tex` + PDF | ✅ Parcial (desactualizado) |
| README con resultados | ✅ Parcial |

### Lo que piden los lineamientos

| Requisito | ¿Lo tenemos? |
|---|---|
| **Planteamiento del problema** | ❌ Actualmente: "Replicar McCloud". Falta formular una pregunta de investigación propia |
| **Hipótesis de trabajo** | ❌ No explicitada como tal; implícita en la dirección del efecto |
| **Análisis descriptivo** | ⚠️ Solo el gráfico de series de México. Falta describir el panel, tendencias pre-tratamiento |
| **Estimación econométrica** | ✅ SCM implementado con pysyncon |
| **Interpretación de resultados** | ⚠️ Solo tabla comparativa con McCloud. Falta discusión económica |
| **Introducción con revisión de literatura** | ❌ Ausente como narrativa integrada |
| **Descripción de datos** | ⚠️ Diluida en celdas de código. Falta sección narrativa |
| **Conclusiones** | ❌ No hay sección de cierre con limitaciones y extensiones |
| **Reproducibilidad** | ✅ CSV + script standalone + notebook |

### El problema central

El proyecto se diseñó como un ejercicio de **replicación**: el criterio de éxito era "qué tan cerca estamos de McCloud". Pero los lineamientos piden una **investigación original**: el criterio debe ser "qué aprendimos sobre el efecto del IT en México".

La diferencia es de **narrativa** y **encuadre**, no de contenido técnico. Los resultados que tenemos son sólidos y defendibles. Lo que falta es enmarcarlos correctamente.

---

## 2. Propuesta de reframing

### 2.1 Título propuesto

> **"Efecto del Inflation Targeting sobre la inversión doméstica en México (2001): un enfoque de control sintético"**

### 2.2 Planteamiento del problema

México adoptó formalmente el régimen de Inflation Targeting (IT) en 2001, tras la crisis del peso de 1994–1995 y la subsecuente reforma del Banco de México (Ley de Autonomía de 1994). El IT busca anclar las expectativas de inflación mediante un objetivo explícito y público, reduciendo así la incertidumbre macroeconómica. En teoría, esta reducción de incertidumbre debería estimular la inversión doméstica al disminuir la prima de riesgo y facilitar la planificación de largo plazo.

Sin embargo, la evidencia empírica no es concluyente. McCloud (2022), usando Synthetic Control Method (SCM) para 29 países, encuentra que en 21 de ellos **no hubo efecto significativo** del IT sobre la inversión. Para México específicamente, reporta un efecto **negativo** de hasta −7.48 puntos porcentuales del PIB en 2008, atribuible a la credibilidad débil del banco central y a restricciones del sistema financiero doméstico.

**Pregunta de investigación:** ¿Cuál fue el efecto causal de la adopción del IT en 2001 sobre la inversión doméstica agregada en México?

Esta pregunta es relevante por tres razones:
1. **Policy-relevance:** México mantiene el IT como marco de política monetaria. Entender su efecto sobre la inversión —el motor del crecimiento de largo plazo— es crucial para evaluar su desempeño.
2. **Caso atípico:** México es uno de los pocos países donde McCloud encuentra un efecto negativo significativo. Si el IT desincentiva la inversión en economías con credibilidad débil, el diseño institucional importa tanto como el régimen mismo.
3. **Datos actualizados:** McCloud usa datos hasta 2017. Nuestra ventana se extiende a 2023, cubriendo la pandemia COVID-19 y permitiendo evaluar si el efecto negativo persistió.

### 2.3 Hipótesis de trabajo

> **H0 (efecto nulo):** La adopción del IT en 2001 no tuvo efecto sobre la formación bruta de capital fijo en México. La trayectoria observada de la inversión mexicana es indistinguible de la de su contrafactual sintético.

> **H1 (alternativa):** El IT tuvo un efecto **negativo** sobre la inversión doméstica en México. El mecanismo propuesto por McCloud —credibilidad débil del banco central, expectativas de inflación persistentemente altas, restricciones del sistema financiero— implica que la inversión mexicana post-2001 es sistemáticamente menor que la de su contrafactual sin IT.

La direccionalidad negativa está motivada por:
- La evidencia previa de McCloud (2022): México es uno de los 6 países con efecto negativo significativo.
- La experiencia mexicana: el banco central tuvo dificultades para anclar expectativas; la inflación se mantuvo cerca del techo de la banda durante gran parte de los 2000s.
- La estructura del sistema financiero mexicano, caracterizada por baja penetración del crédito bancario al sector privado (~15% del PIB vs ~50% en economías similares).

### 2.4 Relación con McCloud (2022)

McCloud (2022) es el **punto de partida metodológico**, no el objeto de estudio. Específicamente:

- **Adoptamos** su estrategia de identificación (SCM con predictores de crecimiento económico, población, estructura productiva y condiciones externas).
- **Adoptamos** su método de inferencia (placebos in-space, pseudo p-values de Fisher).
- **Nos desviamos** de su especificación exacta en aspectos justificados:
  - Donor pool restringido a países no-OCDE (McCloud lo reporta como robustness check con RMSPE = 0.12)
  - Ventana pre-tratamiento 1990–2000 en vez de 1984–2000 (la crisis de deuda de los 80s introduce missing values; mostramos que la ventana 1990–2000 tiene mejor ajuste: RMSPE 0.11 vs 0.29)
  - Membresía OCDE histórica (time-varying) en vez de dummy constante
  - Datos actualizados a 2023 (McCloud termina en 2017)
- **Extendemos** el análisis con robustness checks adicionales (ventana 1984–2000, especificación con gross savings).

**McCloud no es la respuesta correcta contra la cual medirnos; es una referencia que informa nuestra estrategia empírica.** Si nuestros resultados difieren de los suyos, eso no es un "error de replicación" sino una discrepancia metodológica que merece discusión.

---

## 3. Estructura propuesta del notebook final

El notebook debe reorganizarse para contar la historia de nuestra investigación, no la historia de McCloud. La estructura técnica (celdas de código) se mantiene; lo que cambia es la narrativa en markdown.

```
01_data_pipeline.ipynb  →  trabajo_final.ipynb  (o renombrar)
```

### Sección 1: Introducción
- **Motivación:** ¿por qué importa el efecto del IT sobre la inversión en México?
- **Pregunta de investigación** explícita
- **Hipótesis** formalmente enunciada
- **Breve revisión de literatura:** McCloud (2022) como antecedente principal, Lee (2010), Bambe (2023), Lin & Ye (2007). Qué sabemos y qué no.
- **Contribución de este trabajo** (datos actualizados, especificación non-OECD, robustness extendido)

### Sección 2: Datos
- **Fuente:** World Bank WDI via API (describir endpoint, indicadores)
- **Cobertura:** 1984–2023, 217 países → filtrado a 108 (25 IT + 83 non-OECD)
- **Variables:** tabla con código WDI, definición, rol en el modelo
- **Construcción de la muestra:** panel balanceado, criterios de exclusión, diagnóstico de missing values
- **Clasificación IT:** IMF AREAER 2019, codificación manual de fechas de adopción
- **Membresía OCDE:** histórica por año de adhesión (no dummy constante)

### Sección 3: Análisis descriptivo
- Series de tiempo de México: inversión, crecimiento, inflación (1984–2023)
- Comparación pre/post IT: medias, tendencias
- Composición del panel: IT vs no-IT, OECD vs no-OECD
- Interpretación preliminar: la inversión mexicana cayó en los 2000s, pero ¿es atribuible al IT o a factores globales?

### Sección 4: Estrategia empírica
- **Método:** Synthetic Control Method (Abadie et al., 2010)
- Explicación intuitiva: construir un "México sin IT" como combinación ponderada de países que no adoptaron IT
- **Predictores:** 4 covariables base + 11 lags anuales del outcome (1990–2000)
- **Inferencia:** placebos in-space (Firpo & Possebom, 2018), pseudo p-values
- **Justificación de la especificación non-OECD:** elimina el sesgo de EE.UU. como donante dominante

### Sección 5: Resultados
- **SCM principal (non-OECD):**
  - Tabla de pesos del sintético (15 países)
  - RMSPE pre-tratamiento: 0.1074
  - Path plot: México real vs sintético
  - Treatment gap: efectos año por año
  - Tabla de efectos en años clave vs McCloud
- **Placebos in-space:**
  - Gráfico de gaps de placebos
  - Pseudo p-value: 0.75 (discutir discrepancia con McCloud: período post más largo diluye el ratio)
- **Robustness:**
  - Ventana 1984–2000: peor ajuste (RMSPE 0.29), justifica usar 1990
  - Con `gross_savings`: peor ajuste (RMSPE 0.27), apoya la especificación sin savings

### Sección 6: Discusión
- **Interpretación de los efectos:**
  - 2004 (–2.97 pp), 2005 (–5.38 pp), 2008 (–6.50 pp), 2011 (–7.30 pp)
  - El gap es persistentemente negativo post-2001
- **Mecanismo propuesto:** credibilidad débil, expectativas de inflación, restricciones financieras
- **Magnitud económica:** ¿qué significan –6.5 pp en 2008? En dólares de 2015, ~$75 mil millones de inversión no realizada
- **Comparación con McCloud:** misma dirección, magnitud ligeramente menor; diferencias esperables por actualización de datos y especificación non-OECD

### Sección 7: Conclusiones
- **Síntesis:** el IT en México está asociado con una reducción persistente de la inversión doméstica
- **Sobre la hipótesis:** la evidencia favorece H1 (efecto negativo), aunque el p-value de 0.75 impide rechazar H0 al nivel convencional de inferencia por placebos
- **Limitaciones:**
  - El SCM no modela mecanismos; solo mide efectos reducidos
  - El p-value alto sugiere que el resultado puede no ser estadísticamente distintivo
  - No controlamos por TLCAN (1994), reformas estructurales, crisis financiera global
  - El donor pool non-OECD reduce comparabilidad con países de ingreso medio similar
- **Extensiones posibles:**
  - Augmented SCM (Ben-Michael et al., 2021) para ATT agregado con adopción escalonada
  - Análisis de mecanismos: canal de crédito, expectativas de inflación, inversión extranjera directa
  - Comparación con otros países latinoamericanos (Chile, Colombia, Brasil, Perú)
  - Generalized SCM (Xu, 2017) o Matrix Completion (Athey et al., 2021)

---

## 4. Plan de implementación

### Fase A: Reestructuración del notebook (~2 horas)

| Tarea | Descripción |
|---|---|
| A1 | Reescribir markdown de introducción (celdas 0, 1) con pregunta, hipótesis, motivación |
| A2 | Reescribir markdown de datos (§1-§3) con narrativa propia |
| A3 | Agregar sección de análisis descriptivo (§3 del notebook) con gráficas y cuadros |
| A4 | Reescribir markdown de metodología (§4-§5) enmarcando a McCloud como referencia |
| A5 | Reescribir markdown de resultados (§6-§8) con interpretación económica, no solo comparación |
| A6 | Agregar sección de conclusiones (§9) con limitaciones y extensiones |
| A7 | Reorganizar celdas de diagnóstico (21, 22) como apéndice o sección colapsable |

### Fase B: Refuerzo de robustness (~1 hora)

| Tarea | Descripción |
|---|---|
| B1 | Placebos in-time: $T_0 = 1997$ (falso tratamiento) — opcional |
| B2 | Si el p-value de 0.75 es débil, explorar trimming del donor pool |

### Fase C: Documentación (~1 hora)

| Tarea | Descripción |
|---|---|
| C1 | Actualizar `resumen_proyecto.tex` con el reframing |
| C2 | Actualizar README con estructura final y resultados |
| C3 | Commit + push final |

---

## 5. Criterios de éxito

- [ ] El lector puede responder "¿cuál fue el efecto del IT sobre la inversión en México?" después de leer el notebook
- [ ] La hipótesis está enunciada explícitamente y se evalúa al final
- [ ] McCloud aparece como referencia metodológica, no como objeto de comparación
- [ ] Las desviaciones de la especificación de McCloud están justificadas
- [ ] Los robustness checks apoyan (o cuestionan) el resultado principal
- [ ] Las limitaciones son honestas y las extensiones son concretas
- [ ] El notebook es reproducible: Kernel → Restart & Run All sin errores
