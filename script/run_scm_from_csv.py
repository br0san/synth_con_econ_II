"""
SCM para Mexico — carga desde CSV, sin API del Banco Mundial.

Ejecutar desde la carpeta script/:
    python run_scm_from_csv.py

O con placebos (~5-10 min):
    python run_scm_from_csv.py --placebos
"""
import sys
import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from pysyncon import Dataprep, Synth
from pysyncon.utils import PlaceboTest
import warnings
warnings.filterwarnings('ignore')

DATA_DIR = Path('../data')
OUT_DIR  = Path('../out')

# ── Constantes del modelo ────────────────────────────────────────────────────

IT_ADOPTERS = {
    'Australia': 1993, 'Canada': 1991, 'Finland': 1993, 'Iceland': 2001,
    'Israel': 1992, 'Japan': 2013, 'Korea, Rep.': 2001, 'New Zealand': 1990,
    'Norway': 2001, 'Spain': 1995, 'Sweden': 1995, 'United Kingdom': 1997,
    'Brazil': 1999, 'Chile': 1991, 'Colombia': 2000, 'Czechia': 1998,
    'Dominican Republic': 2012, 'Ghana': 2007, 'Guatemala': 2005,
    'Hungary': 2001, 'Indonesia': 2005, 'Mexico': 2001, 'Paraguay': 2013,
    'Peru': 2002, 'Philippines': 2002, 'Poland': 1999, 'Romania': 2005,
    'Thailand': 2000, 'Uruguay': 2007,
}

BASE_PREDICTORS = ['gdp_growth', 'log_population', 'gdp_deflator_inflation', 'oil_exporter']
OUTCOME         = 'gross_capital_formation'
TREATMENT_YEAR  = 2001
PRE_START       = 1990
PRE_END         = 2000

MCCLOUD_EFFECTS = {2004: -3.21, 2005: -3.54, 2007: -4.79, 2008: -7.48, 2011: -6.25}
MCCLOUD_RMSPE   = 0.12


def load_panel() -> pd.DataFrame:
    csv_path = DATA_DIR / 'panel_mccloud_mexico.csv'
    df = pd.read_csv(csv_path)
    df['year'] = df['year'].astype(int)
    print(f"Panel cargado: {df.shape[0]} filas, {df['country_name'].nunique()} paises")
    return df


def build_sample(df: pd.DataFrame):
    pre_mask = (df['year'] >= PRE_START) & (df['year'] <= PRE_END)
    df_pre = df[pre_mask]

    all_vars = BASE_PREDICTORS + [OUTCOME]
    missing = df_pre.groupby('country_name')[all_vars].apply(
        lambda x: x.isnull().sum().sum()
    )
    complete_countries = missing[missing == 0].index.tolist()
    print(f"Paises con datos completos en {PRE_START}-{PRE_END}: {len(complete_countries)}")

    if 'Mexico' not in complete_countries:
        raise RuntimeError("Mexico NO tiene datos completos en el periodo pre-tratamiento")

    treated_pool   = [c for c in complete_countries if c in IT_ADOPTERS]
    donor_pool_all = [c for c in complete_countries if c not in IT_ADOPTERS]

    oecd_countries = df[df['oecd_member'] == 1]['country_name'].unique()
    donor_pool     = [c for c in donor_pool_all if c not in oecd_countries]
    excluded_oecd  = [c for c in donor_pool_all if c in oecd_countries]

    print(f"Tratados (IT):            {len(treated_pool)}")
    print(f"Donantes (non-OECD):      {len(donor_pool)}")
    print(f"Donantes OECD excluidos:  {len(excluded_oecd)}: {sorted(excluded_oecd)}")
    print(f"Total muestra:            {len(treated_pool) + len(donor_pool)}")
    print(f"(McCloud: 29 IT + 75 control = 104)")

    sample = treated_pool + donor_pool
    df_final = df[df['country_name'].isin(sample)].copy()
    df_final = df_final.sort_values(['country_name', 'year']).reset_index(drop=True)
    return df_final, treated_pool, donor_pool


def fit_scm(df_final: pd.DataFrame, donor_pool: list):
    pre_years = list(range(PRE_START, TREATMENT_YEAR))
    special_predictors = [(OUTCOME, [yr], 'mean') for yr in pre_years]

    dataprep = Dataprep(
        foo=df_final,
        predictors=BASE_PREDICTORS,
        predictors_op='mean',
        special_predictors=special_predictors,
        dependent=OUTCOME,
        unit_variable='country_name',
        time_variable='year',
        treatment_identifier='Mexico',
        controls_identifier=[c for c in donor_pool if c != 'Mexico'],
        time_predictors_prior=range(PRE_START, TREATMENT_YEAR),
        time_optimize_ssr=range(PRE_START, TREATMENT_YEAR),
    )

    print("\nAjustando Synthetic Control (Nelder-Mead)…")
    synth = Synth()
    synth.fit(dataprep=dataprep, optim_method='Nelder-Mead')
    return dataprep, synth


def report_results(synth):
    weights = synth.weights(round=3, threshold=0.001)
    rmspe   = np.sqrt(synth.mspe())

    print(f"\n── Pesos del control sintetico de Mexico ──")
    print(weights.to_string())
    print(f"\nRMSPE pre-tratamiento: {rmspe:.4f}  (McCloud: {MCCLOUD_RMSPE})")

    end_year = int(synth.dataprep.foo['year'].max()) + 1
    Z0, Z1   = synth.dataprep.make_outcome_mats(time_period=range(PRE_START, end_year))
    synthetic = synth._synthetic(Z0=Z0)
    gap = Z1 - synthetic

    print(f"\n── Efectos estimados vs McCloud (anios clave) ──")
    print(f"{'Año':<6} {'Estimado (pp)':>15} {'McCloud (pp)':>15} {'Δ':>10}")
    for yr, mc in MCCLOUD_EFFECTS.items():
        if yr in gap.index:
            g = float(gap.loc[yr])
            print(f"{yr:<6} {g:>15.2f} {mc:>15.2f} {g - mc:>+10.2f}")

    return Z1, synthetic, gap


def plot_path(Z1, synthetic, out_dir: Path):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(Z1.index, Z1.values,         color='black', lw=2,       label='Mexico (real)')
    ax.plot(synthetic.index, synthetic.values, color='black', lw=2, ls='--', label='Mexico sintetico')
    ax.axvline(x=TREATMENT_YEAR, color='red', ls='--', alpha=0.6, label=f'IT ({TREATMENT_YEAR})')
    ax.set_title(f'Mexico vs Synthetic Mexico: {OUTCOME}')
    ax.set_xlabel('Year')
    ax.set_ylabel('Gross Capital Formation (% GDP)')
    ax.grid(alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(out_dir / 'mexico_synthetic_control.png', dpi=150, bbox_inches='tight')
    plt.close(fig)
    print("Guardado: mexico_synthetic_control.png")


def plot_gap(gap, out_dir: Path):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(gap.index, gap.values, color='black', lw=2)
    ax.axhline(y=0, color='gray', lw=0.8)
    ax.axvline(x=TREATMENT_YEAR, color='red', ls='--', alpha=0.6, label=f'IT ({TREATMENT_YEAR})')
    ax.set_title('Efecto del IT sobre la Inversion en Mexico (Gap)')
    ax.set_xlabel('Year')
    ax.set_ylabel('Mexico real − Mexico sintetico (pp del PIB)')
    ax.grid(alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(out_dir / 'mexico_treatment_gap.png', dpi=150, bbox_inches='tight')
    plt.close(fig)
    print("Guardado: mexico_treatment_gap.png")


def run_placebos(dataprep, synth, out_dir: Path):
    n_donors = len(dataprep.controls_identifier)
    print(f"\nEjecutando placebos para {n_donors} donantes non-OECD…")
    placebo = PlaceboTest()
    placebo.fit(dataprep=dataprep, scm=Synth(), max_workers=4, verbose=True)

    p_val = placebo.pvalue(treatment_time=TREATMENT_YEAR)
    print(f"\nPseudo p-value (Fisher exact): {p_val:.4f}")
    print("(McCloud reporta p-values entre 0.080 y 0.093 para Mexico)")

    mspe_threshold = 5.0
    gaps = placebo.gaps
    pre_mspe         = gaps.loc[:TREATMENT_YEAR].pow(2).sum(axis=0)
    pre_mspe_treated = placebo.treated_gap.loc[:TREATMENT_YEAR].pow(2).sum()
    keep = pre_mspe[pre_mspe < mspe_threshold * pre_mspe_treated].index
    gaps_plot = gaps[keep]

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(gaps_plot.index, gaps_plot.values, color='gray', alpha=0.3, lw=0.8)
    ax.plot(placebo.treated_gap.index, placebo.treated_gap.values,
            color='red', lw=2.5, label='Mexico')
    ax.axhline(y=0, color='black', lw=0.5)
    ax.axvline(x=TREATMENT_YEAR, color='red', ls='--', alpha=0.5, label=f'IT ({TREATMENT_YEAR})')
    ax.set_title(f'Placebo Tests: Mexico vs Donantes Non-OECD (mspe_threshold={mspe_threshold})')
    ax.set_xlabel('Year')
    ax.set_ylabel('Gap (real − sintetico)')
    ax.grid(alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(out_dir / 'mexico_placebo_tests.png', dpi=150, bbox_inches='tight')
    plt.close(fig)
    print("Guardado: mexico_placebo_tests.png")
    return p_val


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--placebos', action='store_true', help='Correr placebo tests (~5-10 min)')
    args = parser.parse_args()

    print("=" * 60)
    print("SCM Mexico — spec non-OECD")
    print("=" * 60)

    df = load_panel()
    df_final, treated_pool, donor_pool = build_sample(df)
    dataprep, synth = fit_scm(df_final, donor_pool)
    Z1, synthetic, gap = report_results(synth)
    plot_path(Z1, synthetic, OUT_DIR)
    plot_gap(gap, OUT_DIR)

    if args.placebos:
        run_placebos(dataprep, synth, OUT_DIR)
    else:
        print("\nTip: usa --placebos para correr los placebo tests in-space.")

    print("\n✓ Listo.")


if __name__ == '__main__':
    main()
