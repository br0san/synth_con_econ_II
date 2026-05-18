# Replicación McCloud (2022) para México: Plan de Trabajo

> **Objetivo:** Replicar y extender el análisis de Synthetic Control Method (SCM) de Nadine McCloud (2022) sobre el efecto del Inflation Targeting (IT) en la inversión doméstica, enfocándonos en México como caso principal.

> **Fecha:** 2026-05-18

---

## 1. Contexto académico

### Paper objetivo

**McCloud, Nadine (2022).** "Does domestic investment respond to inflation targeting? A synthetic control investigation." *International Economics*, 169, 98–134.

- **Pregunta:** ¿Responde la inversión doméstica agregada al régimen de metas de inflación?
- **Método:** Synthetic Control Method (SCM) país por país + Partially-Pooled SCM (Ben-Michael et al., 2021) para efectos agregados.
- **Muestra:** 104 países (29 IT, 75 control), 1984–2017.
- **Outcome:** Gross capital formation (% GDP) — World Bank WDI.
- **Predictores:** GDP growth, gross domestic savings, log population, GDP deflator, oil exporter dummy, OECD dummy, y **todos los valores pre-tratamiento del outcome**.
- **Resultado principal:** Sin efecto significativo en 21/29 países (consistente con inatención racional). Efectos negativos significativos en 6 países, incluyendo México.

### Resultados específicos para México

| Año | Efecto (pp) | Pseudo p-value |
|-----|-------------|----------------|
| 2004 | −3.21 | 0.093 |
| 2005 | −3.54 | 0.093 |
| 2007 | −4.79 | 0.093 |
| 2008 | **−7.48** | 0.080 |
| 2011 | −6.25 | 0.080 |

- Tratamiento: adopción IT en **2001** (IMF AREAER 2019).
- Control sintético: 13 países (Níger 21.7%, Mauritius 17.8%, Botswana 10.8%, Irán 7.8%, Belice 4.7%, Malawi 4.7%, Bahréin 3.3%, Gabón 2.0%, Mauritania 2.0%, Luxemburgo 1.8%, Sierra Leona 1.3%, Guinea-Bissau 1.1%, Bolivia 0.4%).
- Ajuste pre-tratamiento: RMSPE = 0.11, $\bar{R}^2 \approx 1.00$.
- **Interpretación de McCloud:** El efecto negativo se debe a credibilidad débil del banco central (expectativas de inflación cerca del techo de la banda) + restricciones del sistema financiero mexicano.

### Otros papers en el NotebookLM de referencia

| Paper | Método | Outcome | México | Resultado |
|-------|--------|---------|--------|-----------|
| Bambe (2023) | PSM | Inversión privada | Citado | IT sube inversión 2.8–3.3 pp, pero desviaciones de meta lo anulan |
| Lee (2010) | SCM | Inflación | Incluido pero **fracasó ajuste** | No se pudo estimar para México |
| Lin & Ye (2007) | PSM | Inflación | No incluido | IT sin efecto en industrializados |

---

## 2. Metodología SCM paso a paso

### 2.1 Modelo subyacente

El SCM asume un modelo de factores lineales para el contrafactual:

$$Y_{it}^N = \beta_t + Z_i\theta_t + \lambda_t\mu_i + \epsilon_{it}$$

Donde $Z_i$ son covariables observables, $\lambda_t$ son factores comunes no observados, $\mu_i$ son factor loadings (heterogeneidad no observada), y $\epsilon_{it}$ son shocks transitorios.

### 2.2 Procedimiento

1. **Encontrar pesos $\omega$** para los países donantes que minimicen:
   $$||X_1 - X_0\omega||_V = \sqrt{(X_1 - X_0\omega)' V (X_1 - X_0\omega)}$$
   Sujeto a $\omega_j \geq 0$, $\sum \omega_j = 1$ (combinación convexa, sin extrapolación).

2. **Optimizar $V$** (matriz de importancia de predictores) para minimizar el RMSPE del outcome en el período pre-tratamiento.

3. **Estimar efecto:** $\hat{\alpha}_{1t} = Y_{1t} - \sum_{i=2}^{J+1} \omega_i^* Y_{it}$ para cada $t > T_0$.

4. **Inferencia:** Placebos in-space (aplicar SCM a cada país de control como si fuera tratado) + pseudo p-values basados en ratios de RMSPE post/pre.

### 2.3 Parámetros clave para México

| Parámetro | Valor |
|-----------|-------|
| Año de tratamiento ($T_0$) | 2001 |
| Período pre-tratamiento | 1984–2000 (16 años) |
| Outcome | Gross capital formation (% GDP) |
| Predictores base | 6 variables (ver sección 3) |
| Special predictors | Todos los valores anuales del outcome 1984–2000 |
| Donor pool | 75 países no-IT |

---

## 3. Datos requeridos

### 3.1 Variables y fuentes

| Variable | Fuente original | Código/Fuente Python |
|----------|----------------|----------------------|
| Gross capital formation (% GDP) | World Bank WDI (2020) | WB API → `NE.GDI.TOTL.ZS` |
| GDP growth (annual %) | World Bank WDI | WB API → `NY.GDP.MKTP.KD.ZG` |
| Gross domestic savings (% GDP) | World Bank WDI | WB API → `NY.GNS.ICTR.ZS` |
| Population (total) | World Bank WDI | WB API → `SP.POP.TOTL` |
| GDP deflator inflation (annual %) | World Bank WDI | WB API → `NY.GDP.DEFL.KD.ZG` |
| Oil exporter dummy | U.S. EIA (2019) | WB API `EN.PET.PROD.KT` o manual |
| OECD member dummy | OECD (2020) | Manual (~38 países, trivial) |
| IT classification + adoption year | IMF AREAER (2019) | **Manual** — no disponible vía API |
| Institutional quality (robustness) | ICRG | Pago, posible usar WGI del WB |
| Lending rate (robustness) | World Bank WDI | WB API → `FR.INR.LEND` |
| FDI inflows/outflows (robustness) | World Bank WDI | WB API → `BX.KLT.DINV.WD.GD.ZS` / `BM.KLT.DINV.WD.GD.ZS` |
| Investment prices (robustness) | Penn World Tables | `pl_i` (price level of investment) |

### 3.2 Periodicidad y cobertura

- **Frecuencia:** Anual
- **Ventana:** 1984–2017 (McCloud original), ampliable a 1984–2023 con datos actualizados
- **Países:** 104 total (29 IT, 75 no-IT)
- **Requiremento crítico:** Panel perfectamente balanceado en el período pre-tratamiento (el SCM no tolera missing values en predictores)
- **NOTA — GDP deflator:** `NY.GDP.DEFL.ZS` (nivel, base year varía por país) **no es comparable entre países**. Se usa `NY.GDP.DEFL.KD.ZG` (tasa de inflación anual). Ver diagnóstico en notebook 01_data_pipeline.ipynb §4.5.

---

## 4. Toolkit Python

### 4.1 Librería principal: `pysyncon` v1.5.2+

```bash
pip install pysyncon
```

**Reemplaza `synth` + `synth_runner` de Stata.** Provee:

| Clase | Función |
|-------|---------|
| `Dataprep` | Preparación de datos (predictores, special predictors, períodos) |
| `Synth` | SCM clásico (Abadie & Gardeazabal 2003; Abadie, Diamond & Hainmueller 2010) |
| `AugSynth` | SCM aumentado — **reemplaza el partially-pooled SCM de Ben-Michael et al. (2021)** |
| `PenSynth` | SCM penalizado (Abadie & L'Hour 2021) |
| `RobustSynth` | SCM robusto (Amjad, Shah & Shen 2018) |
| `PlaceboTest` | Placebos in-space, gaps plots, pseudo p-values (Firpo & Possebom 2018) |
| `confidence_interval()` | Intervalos de confianza conformales (Chernozhukov et al. 2021) |

### 4.2 APIs de datos

| Librería | Fuente | Instalación |
|----------|--------|-------------|
| `requests` | World Bank API (descarga directa) | built-in |
| `pypwt` | Penn World Tables (≤10.01) | `pip install pypwt` |
| `imfp` | IMF Data API | `pip install imfp` |

**Nota sobre `wbwdi`:** Se descartó porque tiene un bug de schema inference en Polars con descargas paginadas grandes (ComputeError al consolidar tipos de datos entre páginas de la API). Usamos `requests` directamente contra la API REST del Banco Mundial, que es más robusto y no introduce dependencias innecesarias.

### 4.3 Dependencias completas

```bash
pip install pysyncon requests pandas numpy matplotlib jupyter
```

---

## 5. Desafíos identificados

| Desafío | Severidad | Mitigación |
|---------|-----------|------------|
| **Panel balanceado** | Alta | SCM no tolera missings en pre-tratamiento. Imputación o restricción de muestra. |
| **Donor pool reducido** | Media | Agregar covariables (FDI, lending rates) reduce el donor pool de 75 a ~22. Usar solo predictores base. |
| **Inversión privada** | Alta | ~1,948 missing country-years. Si se usa este outcome, México no es estimable. Usar gross capital formation total. |
| **Clasificación IT** | Media | No hay API para IMF AREAER. Codificación manual requerida. |
| **Código original no disponible** | Media | McCloud no publicó replication files. El external appendix y resultados adicionales deben solicitarse a la autora. |
| **Validación del control sintético** | Conceptual | México es replicado por Níger (21.7%) + Mauritius (17.8%). ¿Es económicamente interpretable? Revisar literatura de sparse SCM. |

---

## 6. Lecciones de Lee (2010) — qué NO hacer

Lee (2010) fracasó en estimar el efecto del IT sobre inflación para México. Tres lecciones:

1. **Incluir todos los lags pre-tratamiento como predictores** — McCloud incluye cada valor anual 1984–2000 del outcome. Lee solo usó promedios.
2. **Período pre-tratamiento largo** — McCloud usa 16 años. Lee descartó los 80s por hiperinflación y usó solo 1993–1998.
3. **Outcome menos volátil** — La inflación tiene spikes extremos difíciles de replicar con combinaciones convexas. La inversión es estructuralmente más estable.

---

## 7. Robustness checks a implementar

Según McCloud (2022), el checklist completo:

- [ ] Placebos in-space (vía `PlaceboTest`)
- [ ] Placebos in-time (adelantar $T_0$ a 1997)
- [ ] Trimming del donor pool (RMSPE 5x, 20x)
- [ ] Detrending de datos
- [ ] Covariables adicionales (inflación volatility, calidad institucional, lending rates, FDI)
- [ ] Clasificación IT alternativa (Rose 2007: México 1999 en vez de 2001)
- [ ] Partición de muestra (solo developing, solo non-OECD)
- [ ] Outcome alternativo: precios de inversión (PWT `pl_i`)
- [ ] Outcome alternativo: inversión privada (si los datos lo permiten)
- [ ] Augmented SCM para ATT agregado con adopción escalonada

---

## 8. Extensiones posibles más allá de McCloud

1. **Datos actualizados:** Extender la ventana a 2023 (McCloud termina en 2017). ¿El efecto negativo persistió?
2. **Métodos alternativos:**
   - Generalized SCM (Xu 2017) — `gsynth` en R
   - Matrix completion (Athey et al. 2021)
   - Dif-in-dif con staggered adoption (Callaway & Sant'Anna 2021, Sun & Abraham 2021)
3. **Mecanismos:** Testear formalmente el canal de credibilidad (desviaciones de la meta) usando la metodología de Bambe (2023).
4. **Ampliación a América Latina:** Análisis comparativo de los 9 países LAC en McCloud: México, Guatemala, Colombia, Paraguay, República Dominicana, Brasil, Perú, Uruguay, Chile.

---

## 9. Estructura del proyecto

```
final_econometria/
├── control/
│   └── planning/
│       └── replicacion-mccloud2022-mexico.md   ← este documento
├── data/                                        ← datos descargados (CSV)
├── script/
│   └── 01_data_pipeline.ipynb                   ← notebook de pipeline de datos
├── out/                                         ← outputs (gráficos, tablas)
└── README.md                                    ← descripción general
```

---

## 10. Referencias

- McCloud, N. (2022). Does domestic investment respond to inflation targeting? A synthetic control investigation. *International Economics*, 169, 98–134.
- Bambe, B.-W.-W. (2023). Inflation targeting and private domestic investment in developing countries.
- Lee, W.-S. (2010). Comparative case studies of the effects of inflation targeting in emerging economies.
- Lin, S. & Ye, H. (2007). Does inflation targeting really make a difference? Evaluating the treatment effect of inflation targeting in seven industrial countries.
- Abadie, A., Diamond, A., & Hainmueller, J. (2010). Synthetic control methods for comparative case studies. *JASA*, 105(490), 493–505.
- Abadie, A., Diamond, A., & Hainmueller, J. (2015). Comparative politics and the synthetic control method. *AJPS*, 59(2), 495–510.
- Ben-Michael, E., Feller, A., & Rothstein, J. (2021). The augmented synthetic control method. *JASA*, 116(536), 1789–1803.
- Firpo, S. & Possebom, V. (2018). Synthetic control method: Inference, sensitivity analysis and confidence sets. *Journal of Causal Inference*, 6(2).
- Galiani, S. & Quistorff, B. (2017). The synth_runner package: Utilities to automate synthetic control estimation. *Stata Journal*, 17(4), 834–849.
