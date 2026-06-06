# Resúmenes de fuentes — Marco teórico Trabajo Final

> **Fecha:** 2026-06-06
> **NotebookLM:** `279861a1-e5ce-43c1-9e65-fe972c6d3cb2`
> **Objetivo:** Filtro inicial de referencias para construir la sección de revisión de literatura / marco teórico del trabajo final.

---

## 1. PAPERS CENTRALES (IT + inversión, SCM)

### McCloud (2022) — "Does domestic investment respond to inflation targeting? A synthetic control investigation"
- **Pregunta:** ¿Responde la inversión doméstica agregada a la adopción de IT?
- **Método:** SCM país por país + partially-pooled SCM, 104 países (29 IT, 75 control), 1984–2017
- **Hallazgo:** En 21/29 países no hubo efecto significativo (inatención racional). Efectos negativos en 6 países, incluyendo México (−7.48 pp en 2008). El IT sí indujo cambios heterogéneos en precios de inversión.
- **México/AL:** ✅ Incluye 9 países LAC. México es caso emblemático de efecto negativo, atribuido a credibilidad débil del banco central y fricciones del sistema financiero.
- **Rol para nosotros:** Referencia metodológica principal. Punto de partida de la estrategia SCM.

### Bambe (2023) — "Inflation targeting and private domestic investment in developing countries"
- **Pregunta:** ¿Fomenta el IT la inversión privada en países en desarrollo?
- **Método:** PSM + regresiones de función de control, 62 países en desarrollo, 1990–2019
- **Hallazgo:** El IT incrementa la inversión privada entre 2.80–3.26 pp, pero el efecto desaparece cuando el banco central se desvía sistemáticamente de la meta.
- **México/AL:** ✅ México y Colombia son ejemplos clave donde el IT *no* funcionó: ambos registraron desviaciones de la meta muy por encima del promedio.
- **Rol para nosotros:** Explica el *mecanismo*: no es el IT per se, es la credibilidad en su implementación. Clave para nuestra hipótesis.

### Lee (2010) — "Comparative case studies of the effects of inflation targeting in emerging economies"
- **Pregunta:** ¿Es el IT eficaz para reducir la inflación en economías emergentes?
- **Método:** SCM país por país (outcome = inflación)
- **Hallazgo:** El IT redujo la inflación significativamente en Colombia, República Checa, Hungría y Polonia (~2.2 pp promedio). Ningún país tuvo efectos adversos.
- **México/AL:** ✅ Incluye a México, pero **no logró ajuste pre-tratamiento** para la inflación mexicana → no pudo hacer inferencia. Lección metodológica: la inflación es un outcome más difícil de ajustar que la inversión.
- **Rol para nosotros:** Lección metodológica (por qué preferimos inversión sobre inflación como outcome) + justificación de PRE_START=1990.

### Lin y Ye (2007) — "Does inflation targeting really make a difference?"
- **Pregunta:** ¿Hace el IT una diferencia real o es "window dressing"?
- **Método:** PSM, 7 países IT dentro de 22 industrializados
- **Hallazgo:** El IT no tuvo ningún efecto significativo sobre nivel ni variabilidad de inflación. Respalda la visión de "fachada conservadora": las acciones importan más que los anuncios.
- **México/AL:** ❌ Solo economías avanzadas. Sugieren investigar emergentes en el futuro.
- **Rol para nosotros:** Antecedente del escepticismo sobre IT. Apoya la idea de que el contexto institucional importa más que el régimen.

---

## 2. TEORÍA DEL INFLATION TARGETING

### Svensson (1998) — "Inflation Targeting as a Monetary Policy Rule"
- **Pregunta:** ¿Cómo opera el IT como regla de política monetaria óptima?
- **Método:** Análisis teórico con modelos macro lineales-cuadráticos
- **Hallazgo:** El IT funciona óptimamente como "regla de focalización de pronósticos" (*forecast targeting*), que es sistemática, transparente y superior a metas de crecimiento monetario o PIB nominal.
- **México/AL:** ❌ No incluye. Se enfoca en pioneros (Nueva Zelanda, Canadá, Reino Unido, Suecia, Australia).
- **Rol para nosotros:** Fundamento teórico canónico del IT. Explica por qué *debería* funcionar.

### Svensson (2010) — "Inflation Targeting" (Handbook of Monetary Economics)
- **Pregunta:** Historia, teoría, práctica y futuro del IT
- **Método:** Revisión analítica extensa con modelos LQ + síntesis de evidencia empírica global
- **Hallazgo:** El IT ha sido "sumamente exitoso" estabilizando inflación y economía real mediante un enfoque flexible y transparente. Demostró resiliencia durante crisis financieras sin perjudicar el crecimiento. **Sin embargo, no se encuentra efecto significativo sobre el crecimiento.**
- **México/AL:** ✅ Incluye a México, Brasil, Chile, Colombia, Perú y Guatemala en tabla histórica de adopción. Destaca que en emergentes el IT logró reducir significativamente la inflación.
- **Rol para nosotros:** Balance entre teoría (debería funcionar) y evidencia (no siempre funciona). Fuente autoritativa para la revisión de literatura.

---

## 3. EVIDENCIA EMPÍRICA SOBRE EFECTOS DEL IT

### Bhalla, Bhasin y Loungani (2023) — "Macro Effects of Formal Adoption of Inflation Targeting" (IMF WP)
- **Pregunta:** ¿Tiene el IT impacto real sobre inflación, crecimiento y expectativas?
- **Método:** Panel extendido + SCM país por país
- **Hallazgo:** El IT **no es necesario ni suficiente** para lograr baja inflación. Gran parte del éxito aparente se debe a "regresión a la media". No hay evidencia de que mejore el crecimiento; incluso sugieren que puede mermarlo.
- **México/AL:** ✅ México y Colombia son casos de "éxito" donde el IT sí redujo la inflación significativamente vs su contrafactual sintético.
- **Rol para nosotros:** Visión escéptica desde el FMI. Contrapeso a Svensson. Apoya que el IT no es una bala mágica.

### Miller, Fang y Eren — "Inflation Targeting: Does It Improve Economic Performance?"
- **Pregunta:** ¿Mejora el IT el desempeño económico? Comparación desarrollados vs emergentes
- **Método:** Revisión bibliográfica extensa (DiD, PSM, SCM)
- **Hallazgo:** En **desarrollados** no genera mejoras significativas a largo plazo (fachada). En **emergentes** sí tiene efecto positivo y duradero reduciendo la inflación.
- **México/AL:** ✅ Incluye México, Brasil, Colombia, Perú, Guatemala en tabla de adoptantes.
- **Rol para nosotros:** El IT funciona distinto según el nivel de desarrollo. México está en la intersección: emergente, OECD, pero con efecto negativo en inversión.

### Brito, Kudamatsu y Teles (2021) — "Inflation Targeting Mattered"
- **Pregunta:** ¿Reduce el IT los costos de producción asociados al control de inflación en economías pioneras?
- **Método:** SCM Multivariado con Series de Tiempo (MSCMT)
- **Hallazgo:** Efectos positivos: en los primeros años redujo inflación sin sacrificar output; a largo plazo permitió mayor crecimiento sin acelerar precios.
- **México/AL:** ❌ Solo 5 economías avanzadas pioneras (Nueva Zelanda, Canadá, Reino Unido, Suecia, Australia).
- **Rol para nosotros:** Evidencia de que el IT *puede* funcionar bien. El contraste con México sugiere que el contexto institucional es determinante.

### Barbosa, Brito y Teles (2018) — "Where Does Inflation Targeting Matter?"
- **Pregunta:** ¿Efectos causales del IT sobre inflación y crecimiento en economías industriales pioneras?
- **Método:** SCM caso por caso, 7 economías adoptantes, panel de 24 países industriales
- **Hallazgo:** El IT generó ganancias económicamente importantes: menor inflación y mayor crecimiento vs contrafactual sintético durante los 1990s.
- **México/AL:** ❌ Solo países altamente industrializados.
- **Rol para nosotros:** El IT funciona en países con instituciones sólidas. México no estaba en ese grupo en 2001.

### Duncan, Martínez-García y Toledo (2024) — "Just Do IT" (Dallas Fed)
- **Pregunta:** ¿Es efectivo el IT para reducir y estabilizar la inflación, y generar resiliencia ante choques globales?
- **Método:** SCM con intersección desplazada + métrica DEV (dispersión respecto a la meta)
- **Hallazgo:** Casi la mitad de los países lograron mejoras sustanciales estabilizando precios cerca de la meta. El éxito está correlacionado con independencia monetaria y estabilidad cambiaria.
- **México/AL:** ⚠️ México (junto con Brasil y Paraguay) fue **excluido** de resultados finales por ajuste pre-tratamiento demasiado débil en la trayectoria inflacionaria.
- **Rol para nosotros:** Refuerza el patrón: México es un caso difícil de ajustar con SCM cuando el outcome es inflación. Nuestra contribución es usar inversión como outcome (siguiendo a McCloud).

---

## 4. PAPERS ADICIONALES (no resumidos aún)

- **"Does Inflation Targeting Matter for International Trade?"** — Pendiente resumir
- **"An Empirical Analysis on Policy Effect of Inflation Targeting in Japan"** — Pendiente resumir
- **"Econometric Analysis of the Impact of Inflation Targeting on Macroeconomic Variables"** — Pendiente resumir
- **"A Guide to Using the Synthetic Control Method"** — Timeout, pendiente reintentar

---

## 5. CLASIFICACIÓN PARA EL MARCO TEÓRICO

### Núcleo duro (citar directamente)
| Paper | Rol en nuestra narrativa |
|---|---|
| **McCloud (2022)** | Referencia metodológica y hallazgo principal para México |
| **Svensson (1998, 2010)** | Teoría canónica del IT (por qué *debería* funcionar) |
| **Bambe (2023)** | Mecanismo: credibilidad > régimen |
| **Bhalla et al. (2023)** | Visión escéptica desde el FMI (IT no es necesario ni suficiente) |

### Soporte empírico (citar como antecedentes)
| Paper | Rol |
|---|---|
| **Lee (2010)** | SCM en emergentes, lección metodológica para México |
| **Lin y Ye (2007)** | Precedente del escepticismo: "fachada conservadora" |
| **Miller, Fang y Eren** | IT funciona distinto en desarrollados vs emergentes |
| **Duncan et al. (2024)** | México excluido por mal ajuste pre (outcome inflación) |

### Evidencia en economías avanzadas (contexto, no foco)
| Paper | Rol |
|---|---|
| **Brito et al. (2021)** | IT sí funcionó en pioneros (instituciones sólidas) |
| **Barbosa et al. (2018)** | IT generó ganancias en industriales |
| **Svensson (2010)** | Balance de evidencia global |

---

## 6. ESTRUCTURA PROPUESTA PARA LA REVISIÓN DE LITERATURA

1. **¿Qué es el IT y por qué debería funcionar?** — Svensson (1998, 2010): forecast targeting, transparencia, anclaje de expectativas → canal de inversión
2. **¿Funciona el IT en la práctica?** — Evidencia mixta:
   - A favor: Brito et al. (2021), Barbosa et al. (2018) en avanzados
   - En contra: Lin y Ye (2007), Bhalla et al. (2023)
   - Depende del contexto: Miller et al. (desarrollados vs emergentes)
3. **El caso específico de inversión doméstica** — McCloud (2022): SCM, 29 países, México efecto negativo. Bambe (2023): PSM, el efecto positivo del IT desaparece con desviaciones de la meta.
4. **¿Por qué México podría ser diferente?** — Credibilidad débil (McCloud), desviaciones de meta (Bambe), exclusión recurrente en estudios SCM de inflación (Lee 2010, Duncan et al. 2024), entrada a OECD en 1994 sin consolidación institucional previa.
5. **Nuestra contribución** — Réplica/extensión de McCloud con datos actualizados (2023), especificación non-OECD canónica, OECD histórica, ventana pre-tratamiento optimizada, robustness checks.

---

## 7. SEGUNDA RONDA: RESULTADOS DE PROFUNDIZACIÓN

### 7.1 McCloud (2022): Mecanismo de credibilidad débil en México

**Hallazgos textuales:**

McCloud atribuye el efecto negativo en México a **dos factores simultáneos**:

**Factor 1 — Falta de credibilidad del banco central (expectativas no ancladas):**

> *"IT adoption does not guarantee that the central bank will enjoy increased credibility, and firms will anchor inflation expectations and be less pessimistic about the aggregate economy and invest more. In addition, if an IT central bank misses its target, then this may negatively affect its credibility... Collectively, these arguments appear consistent with the significant and negative IT effects in Mexico, Ghana and Guatemala. Indeed, IMF (2020) states that actual inflation and inflation expectations in Mexico have remained closer to the upper range of the target despite the sizeable reduction in inflation levels and volatility in the post-IT era."*

**Factor 2 — Fricciones estructurales del sistema financiero mexicano:**

La autora complementa señalando que las características subdesarrolladas del sistema financiero exacerban los efectos negativos: el entorno macroeconómico no logra traducirse en mayor inversión porque los canales de crédito e intermediación financiera son débiles y no transmiten la política monetaria a la inversión real.

**Factor 3 — La inversión cayó por el lado de la inversión pública y la construcción (desagregación por tipo):**

McCloud desagrega el resultado: la caída no fue uniforme. La inversión privada empresarial mostró cierta resiliencia, pero la inversión pública y la construcción cayeron de forma pronunciada post-2001.

**Citas clave adicionales sobre México:**
- El control sintético de México usa 13 países: Níger (21.7%), Mauritius (17.8%), Botswana (10.8%), Irán (7.8%), Belice (4.7%), Malawi (4.7%), Bahréin (3.3%), Gabón (2.0%), Mauritania (2.0%), Luxemburgo (1.8%), Sierra Leona (1.3%), Guinea-Bissau (1.1%), Bolivia (0.4%).
- RMSPE = 0.11, pseudo p-value entre 0.080 y 0.093.

### 7.2 Bambe (2023): Medición de desviaciones de la meta

**¿Cómo mide las desviaciones?**

Toma la diferencia entre **inflación real observada y meta de inflación** para cada país IT durante 1990–2019. Es una medida continua, no binaria.

**Umbral para "desviación extrema":**

Bambe **no usa un umbral numérico fijo**. En su lugar, identifica a México y Colombia como casos donde la desviación promedio está **"muy por encima del promedio de la muestra"**:

| País | Desviación promedio de la meta |
|---|---|
| **Promedio de la muestra IT** | **1.18%** |
| **México** | **1.35%** |
| **Colombia** | **1.64%** |
| Ghana | 2.89% |
| Ucrania (outlier) | 14.18% |

**¿Qué variables determinan que el efecto del IT desaparezca?**

Bambe usa un modelo de regresión con **términos de interacción** entre:
- La dummy de adopción IT × medida de desviación de la meta
- La dummy de adopción IT × dummy de "desviación extrema" (por encima de cierto percentil de la distribución de desviaciones)
- Controles: PIB per cápita, apertura comercial, profundidad financiera, calidad institucional

**Resultado clave:** El coeficiente de la interacción IT × desviación es negativo y significativo: **a mayor desviación de la meta, menor (o negativo) el efecto del IT sobre la inversión**. Cuando las desviaciones son "extremas", el efecto neto del IT se vuelve negativo.

### 7.3 Svensson (2010): IT y crecimiento económico

**Citas textuales sobre el efecto nulo del IT en crecimiento:**

1. **Evidencia en OCDE:**
   > *"Ball and Sheridan (2005) find no significant effect of inflation targeting on average output growth or output volatility in their sample of 20 OECD countries."*

2. **Evidencia en emergentes:**
   > *"Batini and Laxton (2007) and Gonçalves and Salles (2008) consider emerging-market economies and find that inflation targeting reduce the volatility in output growth/the output gap. There is no significant effect of inflation targeting on growth."*

3. **Conclusión general:**
   > *"Importantly, there is no evidence that inflation targeting has been detrimental to growth, productivity, employment, or other measures of economic performance in either developed and developing economies."*

**Contexto:** Svensson aborda esto para refutar a los críticos que temían que el IT fuera "demasiado enfocado en inflación" y perjudicara la economía real. Su conclusión es que el IT no daña el crecimiento... **pero tampoco lo estimula**. Es neutral en crecimiento y positivo en estabilización de inflación.

**Implicación para nosotros:** Si el IT es neutral en crecimiento pero McCloud encuentra que México tuvo efecto *negativo* en inversión, entonces México es una excepción a este patrón general — lo que refuerza la hipótesis de que factores institucionales locales (credibilidad, sistema financiero) son los que explican el resultado.

### 7.4 Bhalla, Bhasin y Loungani (2023): SCM para México

**Lo que reportan (y lo que no):**

| Elemento | ¿Lo reportan? |
|---|---|
| Pesos del sintético para México | ❌ **No.** Solo mencionan que es un "promedio ponderado" |
| RMSPE pre-tratamiento | ✅ Inflación: 7.84; Crecimiento: 3.23 (Tabla 12) |
| Variables predictoras | ❌ **No especifican.** El paper omite declarar qué covariables usaron |
| Outcome | Inflación y crecimiento del PIB (no inversión) |

**Diferencias clave con McCloud y con nosotros:**

| Dimensión | Bhalla et al. | McCloud | Nosotros |
|---|---|---|---|
| Outcome | Inflación, crecimiento | Inversión | Inversión |
| Transparencia de pesos | No reporta | 13 países con pesos exactos | 15 países con pesos exactos |
| Predictores | No especificados | 6 variables + lags | 4 variables + 11 lags |
| Ventana | ~1990s–2019 | 1984–2017 | 1984–2023 |
| Donor pool | No detallado | 75 control | 83 non-OECD |
| RMSPE | 7.84 (alto, poco ajuste) | 0.11 | 0.1074 |

**Conclusión:** Bhalla et al. es una referencia útil como visión escéptica del IT (desde el FMI), pero su implementación del SCM es **opaca y poco reproducible**. No es comparable metodológicamente con McCloud ni con nuestro trabajo. Lo citamos por su conclusión general ("IT no es necesario ni suficiente"), no por su metodología.

---

## 8. PRÓXIMA RONDA DE PREGUNTAS (opcional)

1. **Al SCM Guide (Abadie et al.):** "¿Cuáles son las mejores prácticas para la inferencia con SCM cuando el número de unidades de control es limitado (~80)? ¿Qué dice sobre placebos in-space, pseudo p-values, y thresholds de RMSPE?"
2. **A McCloud (2022):** "En la sección de robustness, ¿cómo implementa exactamente la estratificación non-OECD? ¿Qué RMSPE reporta para México en esa especificación? ¿Qué países forman el sintético non-OECD?"
3. **A Duncan et al. (2024):** "¿Por qué exactamente México tuvo un ajuste pre-tratamiento 'demasiado débil'? ¿Qué criterio usaron para excluirlo? ¿Cuál fue el RMSPE que obtuvieron?"

---

## 9. TERCERA RONDA: RESPUESTAS Y CORRECCIONES (2026-06-06)

> Ronda ejecutada vía NotebookLM con consultas dirigidas a fuentes específicas (`-s`).
> **Contiene dos correcciones de encuadre importantes** que afectan al marco teórico v1.

### 9.1 ⚠️ CORRECCIÓN: McCloud NO tiene una "spec non-OECD para México" con RMSPE 0.12

**Hallazgo:** En McCloud (2022), **México está clasificado como país OCDE** (OECD = 1.00 en la
Tabla 3, porque entró a la OCDE en 1994). McCloud corre **dos** particiones de robustez distintas:

| Partición | A qué grupo cae México | RMSPE de México |
|---|---|---|
| **OCDE vs non-OECD** | México → OCDE (solo con donantes OCDE) | **1.41** (ajuste pésimo) |
| **Desarrollados vs en desarrollo** | México → "developing" (solo con donantes developing) | **0.12** |
| Muestra completa (sin restricción) | todos los donantes | 0.11 |

> *Cita textual (McCloud 2022):* "We then split the sample into developed and developing
> countries... We find significant adverse IT effects in Colombia, Ghana, Guatemala, **Mexico**,
> Paraguay, and the Philippines. We note that **Mexico's RMSPE is 0.12 relative to its OECD and
> full-sample counterpart of 1.41 and 0.11**, respectively."

> *Cita textual (split OCDE):* "We, therefore, separate the sample into OECD and non-OECD countries.
> Thus, we subjected the OECD (non-OECD) treated countries to only OECD (non-OECD) control countries."

**Implicación para nuestro encuadre:**
- El "0.12" que veníamos citando como "spec non-OECD de McCloud" en realidad proviene de su split
  **developing** (en desarrollo), NO del split non-OECD.
- Nuestro **donor pool non-OECD es una decisión metodológica NUESTRA**, no una réplica de la spec
  non-OECD de McCloud (que para México daría 1.41 porque la pondría con donantes OCDE).
- En el paper hay que decir: "restringimos el donor pool a economías no-OCDE (decisión propia, en
  el espíritu de la estratificación de McCloud); el comparador con buen ajuste en McCloud es su
  submuestra de países en desarrollo, donde México obtiene RMSPE = 0.12".
- McCloud **NO reporta** la composición/pesos del sintético en ninguna de las particiones de robustez.

### 9.2 ⚠️ CORRECCIÓN: McCloud NO da cifra de penetración de crédito (~15% del PIB)

**Hallazgo:** McCloud (2022) **no menciona ninguna cifra concreta** de crédito al sector privado /
PIB. El marco teórico v1 (§2.3 y §2.4) atribuye a McCloud el "~15-20% del PIB" — **esa atribución es
incorrecta**. McCloud solo argumenta, citando a **Boyd y Smith (1998)** e **IMF (2020)**, que los
sistemas financieros menos desarrollados son más afectados por la inflación; los canales que nombra
son "financial stability, capital flow dynamics and financial inclusion".

> *Cita textual:* "Boyd and Smith (1998) highlight that countries with less developed financial
> systems are more adversely affected by the effects of inflation... In line with Boyd and Smith
> (1998), IMF (2020) points to financial stability, capital flow dynamics and financial inclusion as
> possible factors in Mexico's inflation function."

**Implicación:** Si queremos usar la cifra ~15% crédito/PIB, hay que **citarla directamente al World
Bank WDI** (`FS.AST.PRVT.GD.ZS`), no a McCloud. Alternativa: suavizar y atribuir el mecanismo
(subdesarrollo financiero) a McCloud/Boyd & Smith/IMF sin número específico.

### 9.3 Duncan et al. (2024) — criterio de exclusión de México (preciso)

- **Umbral:** se conservan unidades con **RMSPE < 3 pp Y ratio MAPE/SD < 0.5**.
- **México:** RMSPE = **5.45**, MAPE/SD = **0.53** → rebasa ambos → excluido.
- Total descartados: 15 países (3 avanzados + 12 emergentes, incluyendo México).

> *Cita textual:* "We choose conventional thresholds and constrain our analysis to units with RMSPE
> lower than 3 p.p. and an MAPE-to-SD ratio lower than 0.5. With those cut-offs, we did not obtain
> reasonable fits for the inflationary processes of 15 countries."
> "We discard the following treated units due to weak pre-treatment fit: ... (12 EMDEs) ...
> **Mexico** ..."

(Nota: el outcome de Duncan es **inflación**; refuerza que la inflación es más difícil de ajustar
que la inversión — argumento a favor de nuestra elección de outcome.)

### 9.4 ⚠️ El "SCM Guide" es de Bibek Adhikari (2022), no Abadie

**Hallazgo:** El documento "A Guide to Using the Synthetic Control Method" es de **Bibek Adhikari
(2022)** (cita a Abadie como creador del método). Puntos clave para nuestra §metodología/inferencia:

- **Pseudo p-value (regla de decisión):** "If the placebo experiments create placebo treatment
  effects of magnitude greater than the one estimated for the treated unit in more than 10% of the
  placebo experiments (i.e., if the corresponding pseudo p value is greater than .1), then we can
  conclude that there is no statistically significant evidence of an effect."
  → **Nuestro p = 0.75 implica NO evidencia significativa al nivel convencional.** Hay que decirlo
  con honestidad.
- **Donor pool pequeño:** "there might not be enough countries in the donor pool for running placebo
  analysis, which means that the size and the power of the inference will be small and unreliable."
- **Índice de ajuste:** propone "Fit Index = RMSPE / benchmark RMSPE"; índice > 1 → mal ajuste, no
  usar esa unidad como contrafactual. (Adhikari NO usa el ratio post/pre RMSPE de Abadie.)
- Recomienda remover outliers antes del matching.

### 9.5 Papers que estaban "sin resumir" (§4) — siguen disponibles en el notebook

Las fuentes de comercio internacional ("Does IT matter for international trade"), Japón ("Empirical
Analysis... in Japan") y "Econometric Analysis of the Impact of IT on Macroeconomic Variables" están
cargadas y `ready` en el notebook. **Decisión:** son periféricas a nuestra pregunta (inversión en
México); se dejan fuera del núcleo del marco teórico salvo que se necesite un párrafo de contexto.
