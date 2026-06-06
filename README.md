# Efecto del *Inflation Targeting* sobre la inversión doméstica en México (2001)

Trabajo final de Econometría II. Investigación que estima el efecto causal de la
adopción del régimen de *Inflation Targeting* (IT) en México sobre la formación bruta de
capital fijo, mediante el **método de control sintético**. Toma a McCloud (2022) como
referencia metodológica.

- **Pregunta:** ¿Cuál fue el efecto causal de la adopción del IT en 2001 sobre la inversión
  doméstica agregada en México?
- **Método:** Synthetic Control Method (Abadie et al., 2010), *donor pool* no-OCDE,
  ventana pre-tratamiento 1990–2000, datos hasta 2023.
- **Hallazgo:** efecto negativo y persistente (≈ −3.7 pp del PIB en promedio post-2001,
  mínimo ≈ −7.3 pp), coherente con McCloud en dirección y magnitud; pseudo *p-value* de
  placebos ≈ 0.75 (no significativo al nivel convencional → inferencia cauta).

## Entregables

| Artefacto | Qué es |
|---|---|
| `script/00_datos.ipynb` | **Paso 00:** obtención y limpieza de datos (descarga WDI → congela el CSV). |
| **`01_analisis.qmd`** → `01_analisis.pdf` | **Paso 01:** documento central autocontenido (informe tipo paper). Narrativa + código econométrico inline + citas. |
| `01_analisis.ipynb` | Notebook de análisis derivado del `.qmd` (`quarto convert` + ejecución); entregable oficial. |

## Arquitectura (separación de capas)

```
00. DATOS (run-once, frágil)   script/00_datos.ipynb  →  data/panel_mccloud_mexico.csv
01. ANÁLISIS (autocontenido)   01_analisis.qmd  →  01_analisis.pdf  +  01_analisis.ipynb
                               (lee el CSV congelado; econometría inline, sin API)
 ·  Placebos (costoso)         script/_run_placebos.py  →  caché en out/  (lo lee 01_analisis)
 ·  scm.py                     motor de respaldo/CLI que usa _run_placebos.py
```

El paso 00 **no** se re-ejecuta al analizar: la API del Banco Mundial sufre *rate-limiting*
que corrompe el CSV en modo headless. El CSV congelado es el insumo de todo lo demás.

## Estructura del proyecto

```
├── 01_analisis.qmd            ← documento central autocontenido (Quarto → PDF + ipynb)
├── _quarto.yml                ← configuración de render
├── referencias.bib            ← bibliografía (BibTeX, extraída vía NotebookLM)
├── requirements.txt
├── data/
│   └── panel_mccloud_mexico.csv   ← panel WDI 1984–2023, 108 países (congelado)
├── script/
│   ├── 00_datos.ipynb             ← obtención + limpieza de datos (paso 00)
│   ├── scm.py                     ← motor de respaldo/CLI (lo usa _run_placebos.py)
│   └── _run_placebos.py           ← regenera la caché del test de placebos
├── out/                           ← figuras y caché del test de placebos
└── control/
    ├── planning/                  ← documentación de planificación
    ├── handoffs/                  ← bitácoras de sesiones
    └── legacy/                    ← artefactos de la etapa de réplica (no son entregable)
```

## Instalación

```bash
pip install -r requirements.txt
# Para renderizar el PDF se necesita Quarto (https://quarto.org) y una distribución LaTeX
# (MiKTeX o TinyTeX). Quarto trae su propio pandoc.
```

## Reproducir el análisis

El análisis principal vive **inline** en `01_analisis.qmd` (se reproduce al renderizar; ver abajo).
`scm.py` se conserva como motor de respaldo / CLI equivalente:

```bash
cd script/
python scm.py                 # especificación base (non-OECD, 1990–2000)
python scm.py --savings       # robustez: + ahorro bruto
python scm.py --pre1984       # robustez: ventana 1984–2000
```

**Regenerar la caché de placebos** (único cálculo costoso; en paralelo por procesos
independientes, ~20 min):

```bash
cd script/
python _run_placebos.py chunk 0 4   # repetir con 1 4, 2 4, 3 4 (en paralelo)
python _run_placebos.py combine 4   # combina y escribe out/placebo_pvalue.txt + figura
# alternativa de un solo proceso (lento, ~80 min): python _run_placebos.py serial
```

## Renderizar el documento

```bash
quarto render 01_analisis.qmd --to pdf        # → 01_analisis.pdf
quarto convert 01_analisis.qmd                # → 01_analisis.ipynb
# (opcional) ejecutar el notebook para embeber salidas:
jupyter nbconvert --to notebook --execute --inplace 01_analisis.ipynb
```

El render lee el CSV congelado y corre el SCM inline (rápido). El test de placebos usa una
**caché manual** en `out/` (`mexico_placebo_tests.png` + `placebo_pvalue.txt`): si existen,
se reutilizan; si no, se recomputan. Borra esos dos archivos para forzar el recálculo.

## Toolkit

| Librería | Uso |
|----------|-----|
| `pysyncon` | Control sintético (Dataprep, Synth, PlaceboTest) |
| `pandas` / `numpy` | Manejo de datos panel |
| `matplotlib` | Visualización |
| `requests` | Descarga WDI (solo capa 1) |
| Quarto + LaTeX | Render del informe a PDF |

## Nota sobre archivos legacy (`control/legacy/`)

La carpeta `control/legacy/` conserva artefactos de la etapa inicial de réplica que **no**
forman parte del entregable: `run_scm_from_csv.py` (precursor de `scm.py`; misma lógica y
mismos resultados, pero `scm.py` lo refactoriza en funciones importables sin variables
globales), utilidades de diagnóstico (`check_savings.py`, `inject_notebook_outputs.py`) y el
resumen previo en LaTeX (`resumen_proyecto.tex/.pdf`, superado por `01_analisis.pdf`).

## Referencias principales

- McCloud, N. (2022). Does domestic investment respond to inflation targeting? *International Economics*, 169, 98–134.
- Abadie, A., Diamond, A., & Hainmueller, J. (2010). Synthetic control methods for comparative case studies. *JASA*, 105(490), 493–505.
- Bambe, B.-W.-W. (2023). Inflation targeting and private domestic investment in developing countries. *Economic Modelling*, 125.
- Adhikari, B. (2022). A guide to using the synthetic control method. *The American Economist*, 67(1), 46–63.

La bibliografía completa está en [`referencias.bib`](referencias.bib).
