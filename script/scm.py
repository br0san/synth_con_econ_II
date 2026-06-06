"""
Motor de análisis SCM para México — única fuente de verdad del modelo.

Diseñado para usarse de dos formas:

1. Importable desde un notebook o script (el documento 01_analisis.qmd ya no lo
   importa: incluye su propia copia de la lógica; scm.py se conserva sobre todo
   como motor de `_run_placebos.py`)::

       import scm
       res = scm.estimate(scm.SCMConfig())          # spec base non-OECD
       res.rmspe, res.gap, res.weights, res.effects_table
       fig = scm.fig_path(res)                        # figura matplotlib (no la cierra)

2. Como script de línea de comandos (reproduce el comportamiento histórico,
   guardando los PNG en ../out)::

       python scm.py                  # non-OECD base (sin savings, PRE=1990)
       python scm.py --savings        # non-OECD + gross_savings
       python scm.py --placebos       # incluye placebo tests (~5-10 min)
       python scm.py --pre1984        # robustness: ventana 1984-2000

El cálculo es idéntico al de run_scm_from_csv.py; aquí solo se reestructura en
funciones que devuelven objetos (figuras, DataFrames) en lugar de depender de
variables globales y de efectos secundarios.
"""
from __future__ import annotations

import argparse
import warnings
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pysyncon import Dataprep, Synth
from pysyncon.utils import PlaceboTest

warnings.filterwarnings("ignore")

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR / "../data"
OUT_DIR = SCRIPT_DIR / "../out"

# ── Constantes del modelo ────────────────────────────────────────────────────

IT_ADOPTERS = {
    "Australia": 1993, "Canada": 1991, "Finland": 1993, "Iceland": 2001,
    "Israel": 1992, "Japan": 2013, "Korea, Rep.": 2001, "New Zealand": 1990,
    "Norway": 2001, "Spain": 1995, "Sweden": 1995, "United Kingdom": 1997,
    "Brazil": 1999, "Chile": 1991, "Colombia": 2000, "Czechia": 1998,
    "Dominican Republic": 2012, "Ghana": 2007, "Guatemala": 2005,
    "Hungary": 2001, "Indonesia": 2005, "Mexico": 2001, "Paraguay": 2013,
    "Peru": 2002, "Philippines": 2002, "Poland": 1999, "Romania": 2005,
    "Thailand": 2000, "Uruguay": 2007,
}

PREDICTORS_NO_SAVINGS = ["gdp_growth", "log_population", "gdp_deflator_inflation", "oil_exporter"]
PREDICTORS_SAVINGS = PREDICTORS_NO_SAVINGS + ["gross_savings"]
OUTCOME = "gross_capital_formation"

# Efectos reportados por McCloud (2022) para México, años clave (pp del PIB).
MCCLOUD_EFFECTS = {2004: -3.21, 2005: -3.54, 2007: -4.79, 2008: -7.48, 2011: -6.25}
MCCLOUD_RMSPE = 0.12


# ── Configuración de una corrida ─────────────────────────────────────────────

@dataclass
class SCMConfig:
    """Parámetros de una especificación del SCM."""
    savings: bool = False
    pre_start: int = 1990
    pre_end: int = 2000
    treatment_year: int = 2001
    outcome: str = OUTCOME

    @property
    def predictors(self) -> list[str]:
        return PREDICTORS_SAVINGS if self.savings else PREDICTORS_NO_SAVINGS

    @property
    def suffix(self) -> str:
        """Sufijo de archivo coherente con las figuras históricas en ../out."""
        s = "_savings" if self.savings else ""
        if self.pre_start == 1984:
            s += "_1984"
        return s

    @property
    def label(self) -> str:
        base = "non-OECD + gross_savings" if self.savings else "non-OECD base"
        if self.pre_start == 1984:
            base += f" + PRE={self.pre_start}-{self.pre_end}"
        return base


@dataclass
class SCMResult:
    """Resultado de estimar el SCM para una configuración."""
    config: SCMConfig
    dataprep: Dataprep
    synth: Synth
    treated_pool: list[str]
    donor_pool: list[str]
    weights: pd.DataFrame
    rmspe: float
    Z1: pd.Series
    synthetic: pd.Series
    gap: pd.Series
    effects_table: pd.DataFrame


# ── Carga y construcción de la muestra ───────────────────────────────────────

def load_panel(data_dir: Path | str | None = None) -> pd.DataFrame:
    """Carga el panel congelado desde CSV (sin tocar la API del Banco Mundial)."""
    data_dir = Path(data_dir) if data_dir is not None else DATA_DIR
    df = pd.read_csv(data_dir / "panel_mccloud_mexico.csv")
    df["year"] = df["year"].astype(int)
    return df


def build_sample(df: pd.DataFrame, cfg: SCMConfig, verbose: bool = False):
    """Filtra países con datos completos en el pre-tratamiento y arma el donor pool non-OECD."""
    pre_mask = (df["year"] >= cfg.pre_start) & (df["year"] <= cfg.pre_end)
    df_pre = df[pre_mask]

    all_vars = cfg.predictors + [cfg.outcome]
    missing = df_pre.groupby("country_name")[all_vars].apply(lambda x: x.isnull().sum().sum())
    complete_countries = missing[missing == 0].index.tolist()

    if "Mexico" not in complete_countries:
        raise RuntimeError("México NO tiene datos completos en el periodo pre-tratamiento")

    treated_pool = [c for c in complete_countries if c in IT_ADOPTERS]
    donor_pool_all = [c for c in complete_countries if c not in IT_ADOPTERS]

    # Membresía OECD histórica: un país es donante válido si NO fue OECD durante
    # el pre-tratamiento. Chile (OECD 2010) o Colombia (2020) no son OECD en
    # 1990-2000, pero son IT adopters → no entran al donor pool de todos modos.
    oecd_pre = df_pre.groupby("country_name")["oecd_member"].max()
    non_oecd_countries = oecd_pre[oecd_pre == 0].index.tolist()
    donor_pool = [c for c in donor_pool_all if c in non_oecd_countries]
    excluded_oecd = [c for c in donor_pool_all if c not in non_oecd_countries]

    if verbose:
        print(f"Paises con datos completos {cfg.pre_start}-{cfg.pre_end}: {len(complete_countries)}")
        print(f"Tratados (IT):                  {len(treated_pool)}")
        print(f"Donantes (non-OECD):            {len(donor_pool)}")
        print(f"Donantes OECD excluidos:        {len(excluded_oecd)}: {sorted(excluded_oecd)}")
        print(f"Total muestra:                  {len(treated_pool) + len(donor_pool)}")
        print("(McCloud: 29 IT + 75 control = 104)")

    sample = treated_pool + donor_pool
    df_final = df[df["country_name"].isin(sample)].copy()
    df_final = df_final.sort_values(["country_name", "year"]).reset_index(drop=True)
    return df_final, treated_pool, donor_pool


def fit_scm(df_final: pd.DataFrame, donor_pool: list[str], cfg: SCMConfig):
    """Ajusta el control sintético de México con pysyncon."""
    pre_years = list(range(cfg.pre_start, cfg.treatment_year))
    special_predictors = [(cfg.outcome, [yr], "mean") for yr in pre_years]

    dataprep = Dataprep(
        foo=df_final,
        predictors=cfg.predictors,
        predictors_op="mean",
        special_predictors=special_predictors,
        dependent=cfg.outcome,
        unit_variable="country_name",
        time_variable="year",
        treatment_identifier="Mexico",
        controls_identifier=[c for c in donor_pool if c != "Mexico"],
        time_predictors_prior=range(cfg.pre_start, cfg.treatment_year),
        time_optimize_ssr=range(cfg.pre_start, cfg.treatment_year),
    )

    synth = Synth()
    synth.fit(dataprep=dataprep, optim_method="Nelder-Mead")
    return dataprep, synth


def _effects(synth: Synth, cfg: SCMConfig):
    """Devuelve (Z1, synthetic, gap) sobre todo el período observado."""
    end_year = int(synth.dataprep.foo["year"].max()) + 1
    Z0, Z1 = synth.dataprep.make_outcome_mats(time_period=range(cfg.pre_start, end_year))
    synthetic = synth._synthetic(Z0=Z0)
    gap = Z1 - synthetic
    return Z1, synthetic, gap


def _effects_table(gap: pd.Series) -> pd.DataFrame:
    """Tabla de efectos estimados vs McCloud en años clave."""
    rows = []
    for yr, mc in MCCLOUD_EFFECTS.items():
        if yr in gap.index:
            g = float(gap.loc[yr])
            rows.append({"Año": yr, "Estimado (pp)": round(g, 2),
                         "McCloud (pp)": mc, "Diferencia": round(g - mc, 2)})
    return pd.DataFrame(rows).set_index("Año")


def estimate(cfg: SCMConfig | None = None, df: pd.DataFrame | None = None,
             verbose: bool = False) -> SCMResult:
    """Pipeline completo de estimación: carga → muestra → ajuste → efectos.

    Es el punto de entrada recomendado para el documento Quarto.
    """
    cfg = cfg or SCMConfig()
    if df is None:
        df = load_panel()
    df_final, treated_pool, donor_pool = build_sample(df, cfg, verbose=verbose)
    dataprep, synth = fit_scm(df_final, donor_pool, cfg)
    weights = synth.weights(round=3, threshold=0.001)
    rmspe = float(np.sqrt(synth.mspe()))
    Z1, synthetic, gap = _effects(synth, cfg)
    return SCMResult(
        config=cfg, dataprep=dataprep, synth=synth,
        treated_pool=treated_pool, donor_pool=donor_pool,
        weights=weights, rmspe=rmspe,
        Z1=Z1, synthetic=synthetic, gap=gap,
        effects_table=_effects_table(gap),
    )


# ── Figuras ──────────────────────────────────────────────────────────────────

def fig_path(res: SCMResult):
    """Path plot: México real vs sintético. Devuelve la figura (no la cierra)."""
    cfg = res.config
    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.plot(res.Z1.index, res.Z1.values, color="black", lw=2, label="México (real)")
    ax.plot(res.synthetic.index, res.synthetic.values, color="black", lw=2, ls="--",
            label="México sintético")
    ax.axvline(x=cfg.treatment_year, color="red", ls="--", alpha=0.6,
               label=f"IT ({cfg.treatment_year})")
    ax.set_title("México vs México sintético: formación bruta de capital fijo")
    ax.set_xlabel("Año")
    ax.set_ylabel("Formación bruta de capital fijo (% del PIB)")
    ax.grid(alpha=0.3)
    ax.legend()
    fig.tight_layout()
    return fig


def fig_gap(res: SCMResult):
    """Treatment gap: efecto año a año (México real − sintético)."""
    cfg = res.config
    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.plot(res.gap.index, res.gap.values, color="black", lw=2)
    ax.axhline(y=0, color="gray", lw=0.8)
    ax.axvline(x=cfg.treatment_year, color="red", ls="--", alpha=0.6,
               label=f"IT ({cfg.treatment_year})")
    ax.set_title("Efecto del IT sobre la inversión en México (gap)")
    ax.set_xlabel("Año")
    ax.set_ylabel("México real − México sintético (pp del PIB)")
    ax.grid(alpha=0.3)
    ax.legend()
    fig.tight_layout()
    return fig


@dataclass
class PlaceboResult:
    p_value: float
    placebo: PlaceboTest
    fig: object = field(default=None)


def run_placebos(res: SCMResult, mspe_threshold: float = 5.0,
                 verbose: bool = False) -> PlaceboResult:
    """Placebos in-space + pseudo p-value de Fisher. Devuelve resultado y figura.

    Cálculo **en proceso** (serial), sin ProcessPoolExecutor. `PlaceboTest.fit`
    de pysyncon siempre lanza un pool de procesos; en Windows el multiprocessing
    *spawn* no puede re-importar el módulo llamante cuando se invoca desde
    `python -c` o desde el kernel de Jupyter de Quarto, lo que cuelga el cálculo.
    Aquí replicamos la lógica llamando directamente al staticmethod
    `PlaceboTest._single_placebo`, garantizando ejecución serial confiable en todo
    contexto (algo más lento: del orden de minutos para ~80 donantes).
    """
    import copy

    cfg = res.config
    controls = list(res.dataprep.controls_identifier)
    n = len(controls)

    placebo = PlaceboTest()
    paths, gaps_list = [], []
    for i, (treated, ctrls) in enumerate(PlaceboTest.placebo_iter(controls), 1):
        _dp = copy.copy(res.dataprep)
        _dp.treatment_identifier = treated
        _dp.controls_identifier = ctrls
        path, gap = PlaceboTest._single_placebo(dataprep=_dp, scm=Synth())
        paths.append(path)
        gaps_list.append(gap)
        if verbose:
            print(f"({i}/{n}) placebo: {treated}")

    placebo.paths = pd.concat(paths, axis=1)
    placebo.gaps = pd.concat(gaps_list, axis=1)
    placebo.time_optimize_ssr = res.dataprep.time_optimize_ssr
    placebo.treated_path, placebo.treated_gap = PlaceboTest._single_placebo(
        dataprep=res.dataprep, scm=Synth()
    )

    p_val = placebo.pvalue(treatment_time=cfg.treatment_year)

    gaps = placebo.gaps
    pre_mspe = gaps.loc[:cfg.treatment_year].pow(2).sum(axis=0)
    pre_mspe_treated = placebo.treated_gap.loc[:cfg.treatment_year].pow(2).sum()
    keep = pre_mspe[pre_mspe < mspe_threshold * pre_mspe_treated].index
    gaps_plot = gaps[keep]

    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.plot(gaps_plot.index, gaps_plot.values, color="gray", alpha=0.3, lw=0.8)
    ax.plot(placebo.treated_gap.index, placebo.treated_gap.values,
            color="red", lw=2.5, label="México")
    ax.axhline(y=0, color="black", lw=0.5)
    ax.axvline(x=cfg.treatment_year, color="red", ls="--", alpha=0.5,
               label=f"IT ({cfg.treatment_year})")
    ax.set_title("Placebos in-space: México vs donantes non-OECD")
    ax.set_xlabel("Año")
    ax.set_ylabel("Gap (real − sintético)")
    ax.grid(alpha=0.3)
    ax.legend()
    fig.tight_layout()
    return PlaceboResult(p_value=float(p_val), placebo=placebo, fig=fig)


# ── Helpers descriptivos (para la sección de análisis descriptivo) ───────────

def mexico_series(df: pd.DataFrame) -> pd.DataFrame:
    """Series de México (inversión, crecimiento, inflación) para gráficos descriptivos."""
    cols = ["year", OUTCOME, "gdp_growth", "gdp_deflator_inflation"]
    mx = df[df["country_name"] == "Mexico"][cols].set_index("year").sort_index()
    return mx


def fig_mexico_series(df: pd.DataFrame, treatment_year: int = 2001):
    """Serie histórica de inversión de México con marca del año de adopción del IT."""
    mx = mexico_series(df)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(mx.index, mx[OUTCOME], color="black", lw=2)
    ax.axvline(x=treatment_year, color="red", ls="--", alpha=0.6, label=f"IT ({treatment_year})")
    ax.set_title("Formación bruta de capital fijo en México, 1984–2023")
    ax.set_xlabel("Año")
    ax.set_ylabel("% del PIB")
    ax.grid(alpha=0.3)
    ax.legend()
    fig.tight_layout()
    return fig


def prepost_summary(df: pd.DataFrame, cfg: SCMConfig | None = None) -> pd.DataFrame:
    """Medias pre/post IT de la inversión mexicana."""
    cfg = cfg or SCMConfig()
    mx = df[df["country_name"] == "Mexico"]
    pre = mx[mx["year"] < cfg.treatment_year][cfg.outcome].mean()
    post = mx[mx["year"] >= cfg.treatment_year][cfg.outcome].mean()
    return pd.DataFrame(
        {"Periodo": [f"Pre-IT (<{cfg.treatment_year})", f"Post-IT (≥{cfg.treatment_year})", "Diferencia"],
         "Inversión media (% PIB)": [round(pre, 2), round(post, 2), round(post - pre, 2)]}
    ).set_index("Periodo")


# ── Interfaz de línea de comandos (compatibilidad con run_scm_from_csv.py) ────

def _save_and_close(fig, out_dir: Path, fname: str):
    out_dir.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_dir / fname, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Guardado: {fname}")


def main():
    parser = argparse.ArgumentParser(description="SCM México desde CSV (sin API).")
    parser.add_argument("--placebos", action="store_true", help="Correr placebo tests (~5-10 min)")
    parser.add_argument("--savings", action="store_true", help="Incluir gross_savings como predictor")
    parser.add_argument("--pre1984", action="store_true", help="Ventana pre 1984-2000 (default: 1990-2000)")
    args = parser.parse_args()

    cfg = SCMConfig(savings=args.savings, pre_start=1984 if args.pre1984 else 1990)

    print("=" * 60)
    print(f"SCM México — {cfg.label}")
    print("=" * 60)

    res = estimate(cfg, verbose=True)

    print("\n-- Pesos del control sintético de México --")
    print(res.weights.to_string())
    print(f"\nRMSPE pre-tratamiento: {res.rmspe:.4f}  (McCloud: {MCCLOUD_RMSPE})")
    print("\n-- Efectos estimados vs McCloud (años clave) --")
    print(res.effects_table.to_string())

    _save_and_close(fig_path(res), OUT_DIR, f"mexico_synthetic_control{cfg.suffix}.png")
    _save_and_close(fig_gap(res), OUT_DIR, f"mexico_treatment_gap{cfg.suffix}.png")

    if args.placebos:
        print(f"\nEjecutando placebos para {len(res.donor_pool) - 1} donantes non-OECD…")
        pb = run_placebos(res, verbose=True)
        print(f"\nPseudo p-value (Fisher exact): {pb.p_value:.4f}")
        print("(McCloud reporta p-values entre 0.080 y 0.093 para México)")
        _save_and_close(pb.fig, OUT_DIR, f"mexico_placebo_tests{cfg.suffix}.png")
    else:
        print("\nTip: usa --placebos para correr los placebo tests in-space.")

    print("\nListo.")


if __name__ == "__main__":
    main()
