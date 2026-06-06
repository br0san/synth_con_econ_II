# Efecto del *Inflation Targeting* sobre la inversión doméstica en México (2001)

Trabajo final de Econometría II. Investigación original que estima el efecto causal de la
adopción del régimen de *Inflation Targeting* (IT) en México sobre la formación bruta de
capital fijo, mediante el **método de control sintético**. Toma a McCloud (2022) como
referencia metodológica, no como objeto de réplica.

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
| **`trabajo_final.qmd`** → `trabajo_final.pdf` | Documento central (informe tipo paper). Narrativa + código + citas. |
| `trabajo_final.ipynb` | Notebook de análisis derivado del `.qmd` (`quarto convert`). |
| `script/00_data_pipeline.ipynb` | Notebook de obtención y limpieza de datos (descarga WDI → congela el CSV). |

## Arquitectura (separación de capas)

```
1. DATOS (run-once, frágil)     script/00_data_pipeline.ipynb  →  data/panel_mccloud_mexico.csv
2. MOTOR DE ANÁLISIS            script/scm.py   (funciones importables + CLI; única fuente de verdad)
3. INFORME / PDF               trabajo_final.qmd  →  trabajo_final.pdf   (importa scm.py, lee el CSV)
4. NOTEBOOK DE ANÁLISIS        quarto convert trabajo_final.qmd  →  trabajo_final.ipynb
```

La capa 1 **no** se re-ejecuta al renderizar: la API del Banco Mundial sufre *rate-limiting*
que corrompe el CSV en modo headless. El CSV congelado es el insumo de todo lo demás.

## Estructura del proyecto

```
├── trabajo_final.qmd          ← documento central (Quarto → PDF)
├── _quarto.yml                ← configuración de render
├── referencias.bib            ← bibliografía (BibTeX, extraída vía NotebookLM)
├── requirements.txt
├── data/
│   └── panel_mccloud_mexico.csv   ← panel WDI 1984–2023, 108 países (congelado)
├── script/
│   ├── 00_data_pipeline.ipynb     ← obtención + limpieza de datos (capa 1)
│   ├── scm.py                     ← motor de análisis (capa 2): estimate(), figuras, CLI
│   └── run_scm_from_csv.py        ← script original (precursor de scm.py; ver Nota)
├── out/                           ← figuras y caché del test de placebos
└── control/                       ← planning, handoffs, resumen LaTeX (documentación interna)
```

## Instalación

```bash
pip install -r requirements.txt
# Para renderizar el PDF se necesita Quarto (https://quarto.org) y una distribución LaTeX
# (MiKTeX o TinyTeX). Quarto trae su propio pandoc.
```

## Reproducir el análisis (sin API, segundos)

```bash
cd script/
python scm.py                 # especificación base (non-OECD, 1990–2000)
python scm.py --placebos      # + placebos in-space (~5–10 min)
python scm.py --savings       # robustez: + ahorro bruto
python scm.py --pre1984       # robustez: ventana 1984–2000
```

Desde Python / un notebook:

```python
import scm
res = scm.estimate()                 # SCMResult con .rmspe, .gap, .weights, .effects_table
scm.fig_path(res); scm.fig_gap(res)  # figuras matplotlib
```

## Renderizar el documento

```bash
quarto render trabajo_final.qmd --to pdf      # → trabajo_final.pdf
quarto convert trabajo_final.qmd              # → trabajo_final.ipynb
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

## Nota sobre `run_scm_from_csv.py`

`scm.py` es el sucesor refactorizado de `run_scm_from_csv.py`: misma lógica y mismos
resultados, pero organizado en funciones importables (sin variables globales) para que el
documento Quarto pueda llamarlo. `run_scm_from_csv.py` se conserva como referencia histórica.

## Referencias principales

- McCloud, N. (2022). Does domestic investment respond to inflation targeting? *International Economics*, 169, 98–134.
- Abadie, A., Diamond, A., & Hainmueller, J. (2010). Synthetic control methods for comparative case studies. *JASA*, 105(490), 493–505.
- Bambe, B.-W.-W. (2023). Inflation targeting and private domestic investment in developing countries. *Economic Modelling*, 125.
- Adhikari, B. (2022). A guide to using the synthetic control method. *The American Economist*, 67(1), 46–63.

La bibliografía completa está en [`referencias.bib`](referencias.bib).
