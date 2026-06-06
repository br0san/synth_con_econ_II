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

## 7. PRÓXIMA RONDA DE PREGUNTAS AL NOTEBOOKLM

Una vez que revisemos este filtro, sugiero las siguientes preguntas de profundización:

1. **A McCloud (2022):** "¿Qué dice McCloud específicamente sobre el mecanismo de credibilidad débil en México? Extrae los párrafos relevantes sobre México de la sección de resultados y discusión."
2. **A Bambe (2023):** "¿Cómo mide Bambe las desviaciones de la meta de inflación? ¿Qué umbral utiliza para clasificar a México como caso de 'desviación extrema'?"
3. **A Svensson (2010):** "¿Qué dice Svensson sobre el efecto del IT en el crecimiento económico? Extrae los párrafos donde concluye que no hay efecto significativo."
4. **Al SCM Guide:** "¿Cuáles son las mejores prácticas para la inferencia con SCM cuando el número de unidades de control es limitado (~80)? ¿Qué dice sobre placebos in-space y pseudo p-values?"
5. **A Bhalla et al. (2023):** "En su análisis SCM para México, ¿cuáles son los pesos del sintético y el RMSPE que reportan? ¿Qué variables usan como predictores?"
