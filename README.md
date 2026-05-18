# Replicación McCloud (2022): Efecto del Inflation Targeting sobre la Inversión Doméstica en México

Replicación y extensión del análisis de Synthetic Control Method (SCM) de [McCloud (2022)](#referencias) sobre el efecto del *Inflation Targeting* (IT) en la inversión doméstica, enfocado en México como caso principal.

## Paper objetivo

**McCloud, Nadine (2022).** "Does domestic investment respond to inflation targeting? A synthetic control investigation." *International Economics*, 169, 98–134.

- **Pregunta:** ¿Responde la inversión doméstica agregada al régimen de metas de inflación?
- **Método:** Synthetic Control Method (SCM) país por país + Partially-Pooled SCM
- **Muestra:** 104 países (29 IT, 75 control), 1984–2017
- **Resultado para México:** Efecto negativo significativo de hasta −7.48 pp en 2008

## Estructura del proyecto

```
├── README.md                                     ← este archivo
├── requirements.txt                              ← dependencias Python
├── control/
│   ├── planning/
│   │   └── replicacion-mccloud2022-mexico.md     ← plan de trabajo detallado
│   └── handoffs/
│       └── session-2026-05-18.md                 ← bitácora de sesión
├── data/
│   └── panel_mccloud_mexico.csv                  ← panel descargado (WDI, 1984–2023)
├── script/
│   └── 01_data_pipeline.ipynb                    ← pipeline de datos + estimación SCM
└── out/
    ├── mexico_series_preview.png                 ← preview de series temporales
    └── mexico_treatment_gap.png                  ← gap México vs sintético
```

## Requisitos

- Python 3.9+
- Conexión a internet (para descargar datos del World Bank API)

## Instalación

```bash
pip install -r requirements.txt
```

## Uso

1. Abrir `script/01_data_pipeline.ipynb` en Jupyter o VS Code.
2. Ejecutar todas las celdas en orden (`Kernel → Restart & Run All`).
3. Las secciones del notebook son:
   - **§1:** Descarga de datos desde World Bank API
   - **§2:** Exploración y limpieza
   - **§3:** Clasificación manual de países IT
   - **§4:** Construcción del panel balanceado para SCM
   - **§5:** Estimación del Synthetic Control para México
   - **§6:** Visualización del control sintético
   - **§7:** Placebos e inferencia
   - **§8:** Robustness con Augmented SCM
   - **§9:** Próximos pasos (trabajo manual requerido)

## Toolkit

| Librería | Uso |
|----------|-----|
| `pysyncon` | SCM (Dataprep, Synth, AugSynth, PlaceboTest) |
| `requests` | Descarga de datos vía World Bank API |
| `pandas` | Manejo de datos panel |
| `matplotlib` | Visualización |

## Estado del proyecto

Work in progress. Ver `control/handoffs/session-2026-05-18.md` para el estado detallado de la última sesión.

## Referencias

- McCloud, N. (2022). Does domestic investment respond to inflation targeting? *International Economics*, 169, 98–134.
- Abadie, A., Diamond, A., & Hainmueller, J. (2010). Synthetic control methods for comparative case studies. *JASA*, 105(490), 493–505.
- Ben-Michael, E., Feller, A., & Rothstein, J. (2021). The augmented synthetic control method. *JASA*, 116(536), 1789–1803.
- Plan de trabajo completo en `control/planning/replicacion-mccloud2022-mexico.md`.
