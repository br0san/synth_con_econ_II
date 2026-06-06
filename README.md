# Replicación McCloud (2022): Efecto del Inflation Targeting sobre la Inversión Doméstica en México

Replicación y extensión del análisis de Synthetic Control Method (SCM) de [McCloud (2022)](#referencias) sobre el efecto del *Inflation Targeting* (IT) en la inversión doméstica, enfocado en México como caso principal.

## Paper objetivo

**McCloud, Nadine (2022).** "Does domestic investment respond to inflation targeting? A synthetic control investigation." *International Economics*, 169, 98–134.

- **Pregunta:** ¿Responde la inversión doméstica agregada al régimen de metas de inflación?
- **Método:** Synthetic Control Method (SCM) país por país + Partially-Pooled SCM
- **Muestra:** 104 países (29 IT, 75 control), 1984–2017
- **Resultado para México:** Efecto negativo significativo de hasta −7.48 pp en 2008 (RMSPE = 0.11, p = 0.08)

## Resultados actuales de la replicación

**Especificación non-OECD** (donor pool restringido a países no-OCDE):

| Métrica | Nuestra estimación | McCloud (2022) |
|---|---|---|
| Muestra | 25 IT + 83 non-OECD = 108 países | 29 IT + 75 control = 104 |
| RMSPE pre-tratamiento | **0.1074** | 0.12 |
| Efecto en 2008 | **−6.50 pp** | −7.48 pp |
| Efecto en 2011 | **−7.30 pp** | −6.25 pp |
| Donantes principales | Mongolia (17.9%), Mauritius (15.7%), Bolivia (12.9%) | Níger (21.7%), Mauritius (17.8%), Botswana (10.8%) |

Mauritius, Botswana y Guinea-Bissau son compartidos con el sintético de McCloud. EE.UU. está completamente fuera del sintético.

## Estructura del proyecto

```
├── README.md
├── requirements.txt
├── control/
│   ├── planning/
│   │   └── replicacion-mccloud2022-mexico.md   ← plan de trabajo detallado
│   ├── handoffs/
│   │   ├── session-2026-05-18.md               ← sesiones a+b
│   │   ├── session-2026-05-18c.md              ← sesión c
│   │   └── session-2026-06-05.md               ← sesión d (non-OECD fix)
│   └── resumen_proyecto.tex                    ← resumen para equipo/profesor
├── data/
│   └── panel_mccloud_mexico.csv                ← panel WDI 1984–2023, 108 países
├── script/
│   ├── 01_data_pipeline.ipynb                  ← pipeline completo (datos + SCM)
│   ├── run_scm_from_csv.py                     ← SCM standalone sin API (recomendado)
│   └── inject_notebook_outputs.py              ← utilidad: actualiza outputs del notebook
└── out/
    ├── mexico_series_preview.png
    ├── mexico_synthetic_control.png            ← path plot (spec non-OECD)
    ├── mexico_treatment_gap.png                ← gap México vs sintético
    ├── mexico_placebo_tests.png                ← placebos in-space (83 donantes)
    ├── mexico_synthetic_control_savings.png    ← robustness: con gross_savings
    ├── mexico_treatment_gap_savings.png
    └── mexico_placebo_tests_savings.png
```

## Instalación

```bash
pip install -r requirements.txt
```

## Uso

### Opción A — Script standalone (recomendado, sin API)

El CSV ya está guardado en `data/`. No requiere conexión a internet.

```bash
cd script/

# Spec base (non-OECD, 83 donantes)
python run_scm_from_csv.py

# Con placebos (~5 min)
python run_scm_from_csv.py --placebos

# Robustness con gross_savings (56 donantes)
python run_scm_from_csv.py --savings --placebos
```

### Opción B — Notebook completo (requiere API del Banco Mundial)

> ⚠️ **Advertencia:** Las celdas de descarga de datos pueden fallar silenciosamente en modo headless (rate-limiting de la API). Ejecutar solo de forma interactiva en Jupyter o VS Code. **No usar `nbconvert --execute`.**

1. Abrir `script/01_data_pipeline.ipynb` en Jupyter o VS Code.
2. Ejecutar las celdas en orden (`Kernel → Restart & Run All`).
3. Si solo quieres re-estimar sin re-descargar, ejecuta a partir de la sección §4.

## Toolkit

| Librería | Uso |
|----------|-----|
| `pysyncon` | SCM (Dataprep, Synth, AugSynth, PlaceboTest) |
| `requests` | Descarga de datos vía World Bank API |
| `pandas` | Manejo de datos panel |
| `matplotlib` | Visualización |

## Estado del proyecto

Replicación principal completada. Ver `control/handoffs/session-2026-06-05.md` para el estado detallado.

**Pendientes metodológicos:**
- OECD membership histórica (México entró en 1994, la dummy debería ser dinámica)
- Ventana de estimación 1984–2000 como robustness check
- Augmented SCM (Ben-Michael et al., 2021)

## Referencias

- McCloud, N. (2022). Does domestic investment respond to inflation targeting? *International Economics*, 169, 98–134.
- Abadie, A., Diamond, A., & Hainmueller, J. (2010). Synthetic control methods for comparative case studies. *JASA*, 105(490), 493–505.
- Ben-Michael, E., Feller, A., & Rothstein, J. (2021). The augmented synthetic control method. *JASA*, 116(536), 1789–1803.
- Firpo, S., & Possebom, V. (2018). Synthetic control method: Inference, sensitivity analysis and confidence sets. *Journal of Causal Inference*, 6(2).
