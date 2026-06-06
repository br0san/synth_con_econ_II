"""Runner auxiliar: computa el test de placebos in-space y escribe la caché que
consume 01_analisis.qmd: out/mexico_placebo_tests.png y out/placebo_pvalue.txt.

El cálculo es costoso (~80 estimaciones SCM). pysyncon.PlaceboTest.fit usa un
ProcessPoolExecutor que en Windows (multiprocessing *spawn*) es inestable: se cuelga
desde `python -c` / el kernel de Jupyter de Quarto, y a veces crashea un worker. Por
eso este runner paraleliza con **procesos independientes** (sin pool): cada proceso
calcula serialmente un subconjunto de donantes y guarda un parcial; luego se combinan.

Uso recomendado (≈4 procesos, ~20 min):

    python _run_placebos.py chunk 0 4   &   (cada uno en su terminal / segundo plano)
    python _run_placebos.py chunk 1 4
    python _run_placebos.py chunk 2 4
    python _run_placebos.py chunk 3 4
    python _run_placebos.py combine 4

Alternativa simple (un proceso, serial, lento ~80 min):

    python _run_placebos.py serial
"""
import copy
import sys
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
from pysyncon import Synth
from pysyncon.utils import PlaceboTest

import scm

OUT = (Path(__file__).resolve().parent / "../out").resolve()
MSPE_THRESHOLD = 5.0


def _placebo_gaps_for(units, dataprep, all_controls, tag=""):
    gaps = {}
    for j, unit in enumerate(units, 1):
        _dp = copy.copy(dataprep)
        _dp.treatment_identifier = unit
        _dp.controls_identifier = [c for c in all_controls if c != unit]
        _, gap = PlaceboTest._single_placebo(dataprep=_dp, scm=Synth())
        gaps[unit] = gap
        print(f"{tag}({j}/{len(units)}) {unit}", flush=True)
    return pd.DataFrame(gaps)


def chunk(idx, nchunks):
    res = scm.estimate()
    controls = list(res.dataprep.controls_identifier)
    mine = controls[idx::nchunks]
    df = _placebo_gaps_for(mine, res.dataprep, controls, tag=f"[chunk {idx}] ")
    OUT.mkdir(exist_ok=True)
    df.to_csv(OUT / f"_placebo_part_{idx}.csv")
    print(f"[chunk {idx}] guardado: {len(mine)} gaps", flush=True)


def _build_figure(gaps, treated_gap, treatment_year):
    pre_mspe = gaps.loc[:treatment_year].pow(2).sum(axis=0)
    pre_mspe_treated = treated_gap.loc[:treatment_year].pow(2).sum()
    keep = pre_mspe[pre_mspe < MSPE_THRESHOLD * pre_mspe_treated].index
    gaps_plot = gaps[keep]

    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.plot(gaps_plot.index, gaps_plot.values, color="gray", alpha=0.3, lw=0.8)
    ax.plot(treated_gap.index, treated_gap.values, color="red", lw=2.5, label="México")
    ax.axhline(y=0, color="black", lw=0.5)
    ax.axvline(x=treatment_year, color="red", ls="--", alpha=0.5, label=f"IT ({treatment_year})")
    ax.set_title("Placebos in-space: México vs donantes non-OECD")
    ax.set_xlabel("Año")
    ax.set_ylabel("Gap (real − sintético)")
    ax.grid(alpha=0.3)
    ax.legend()
    fig.tight_layout()
    return fig


def _finalize(gaps, treated_gap, treatment_year):
    placebo = PlaceboTest()
    placebo.gaps = gaps
    placebo.treated_gap = treated_gap
    p_val = float(placebo.pvalue(treatment_time=treatment_year))

    OUT.mkdir(exist_ok=True)
    fig = _build_figure(gaps, treated_gap, treatment_year)
    fig.savefig(OUT / "mexico_placebo_tests.png", dpi=150, bbox_inches="tight")
    (OUT / "placebo_pvalue.txt").write_text(f"{p_val:.6f}")
    print(f"\nPseudo p-value (Fisher): {p_val:.4f}")
    print(f"Caché escrita en: {OUT}")
    return p_val


def combine(nchunks):
    res = scm.estimate()
    parts = []
    for i in range(nchunks):
        p = OUT / f"_placebo_part_{i}.csv"
        if not p.exists():
            raise FileNotFoundError(f"Falta el parcial {p}. ¿Corrieron todos los chunks?")
        parts.append(pd.read_csv(p, index_col=0))
    gaps = pd.concat(parts, axis=1)
    gaps.index = gaps.index.astype(int)

    print("Calculando gap de la unidad tratada (México)...", flush=True)
    _, treated_gap = PlaceboTest._single_placebo(dataprep=res.dataprep, scm=Synth())

    _finalize(gaps, treated_gap, res.config.treatment_year)
    for i in range(nchunks):
        (OUT / f"_placebo_part_{i}.csv").unlink(missing_ok=True)
    print("Parciales eliminados.")


def serial():
    res = scm.estimate()
    controls = list(res.dataprep.controls_identifier)
    gaps = _placebo_gaps_for(controls, res.dataprep, controls)
    print("Calculando gap de la unidad tratada (México)...", flush=True)
    _, treated_gap = PlaceboTest._single_placebo(dataprep=res.dataprep, scm=Synth())
    _finalize(gaps, treated_gap, res.config.treatment_year)


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "serial"
    if mode == "chunk":
        chunk(int(sys.argv[2]), int(sys.argv[3]))
    elif mode == "combine":
        combine(int(sys.argv[2]))
    elif mode == "serial":
        serial()
    else:
        raise SystemExit(f"Modo desconocido: {mode}")
