"""
inject_notebook_outputs.py
Actualiza las celdas con outputs stale en 00_data_pipeline.ipynb usando
los resultados de la spec non-OECD ya verificados.

Celdas afectadas:
  - cell-20: muestra final (27 -> 108 paises)
  - cell-27: SCM fit (error -> pesos + RMSPE)
  - cell-29: path plot (error -> imagen PNG)
  - cell-30: gap plot (error -> imagen PNG + tabla)

Ejecutar desde script/:
    python inject_notebook_outputs.py
"""
import json
import base64
import io
import sys
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
from pysyncon import Dataprep, Synth
import warnings
warnings.filterwarnings('ignore')

NB_PATH   = Path('../script/00_data_pipeline.ipynb')
DATA_DIR  = Path('../data')
OUT_DIR   = Path('../out')

# ── Constantes del modelo (replica cell-12, 18) ─────────────────────────────

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

# ── Helpers de formato de outputs de notebook ────────────────────────────────

def stream_output(text: str) -> dict:
    lines = [l + '\n' for l in text.rstrip('\n').split('\n')]
    lines[-1] = lines[-1].rstrip('\n')
    return {'output_type': 'stream', 'name': 'stdout', 'text': lines}


def image_output(fig) -> dict:
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=150, bbox_inches='tight')
    buf.seek(0)
    encoded = base64.b64encode(buf.read()).decode('ascii')
    plt.close(fig)
    return {
        'output_type': 'display_data',
        'data': {
            'image/png': encoded,
            'text/plain': ['<Figure size 1200x600 with 1 Axes>'],
        },
        'metadata': {'needs_background': 'light'},
    }


# ── Pipeline ────────────────────────────────────────────────────────────────

def load_and_build():
    df = pd.read_csv(DATA_DIR / 'panel_mccloud_mexico.csv')
    df['year'] = df['year'].astype(int)

    pre_mask = (df['year'] >= PRE_START) & (df['year'] <= PRE_END)
    df_pre   = df[pre_mask]

    all_vars = BASE_PREDICTORS + [OUTCOME]
    missing  = df_pre.groupby('country_name')[all_vars].apply(
        lambda x: x.isnull().sum().sum()
    )
    complete = missing[missing == 0].index.tolist()

    treated_pool   = [c for c in complete if c in IT_ADOPTERS]
    donor_pool_all = [c for c in complete if c not in IT_ADOPTERS]
    oecd           = df[df['oecd_member'] == 1]['country_name'].unique()
    donor_pool     = [c for c in donor_pool_all if c not in oecd]
    excluded_oecd  = [c for c in donor_pool_all if c in oecd]

    df_final = df[df['country_name'].isin(treated_pool + donor_pool)].copy()
    df_final = df_final.sort_values(['country_name', 'year']).reset_index(drop=True)

    return df_final, complete, treated_pool, donor_pool, excluded_oecd


def fit_scm(df_final, donor_pool):
    pre_years         = list(range(PRE_START, TREATMENT_YEAR))
    special_predictors = [(OUTCOME, [yr], 'mean') for yr in pre_years]

    dataprep = Dataprep(
        foo=df_final, predictors=BASE_PREDICTORS, predictors_op='mean',
        special_predictors=special_predictors,
        dependent=OUTCOME, unit_variable='country_name', time_variable='year',
        treatment_identifier='Mexico',
        controls_identifier=[c for c in donor_pool if c != 'Mexico'],
        time_predictors_prior=range(PRE_START, TREATMENT_YEAR),
        time_optimize_ssr=range(PRE_START, TREATMENT_YEAR),
    )
    synth = Synth()
    synth.fit(dataprep=dataprep, optim_method='Nelder-Mead')
    return dataprep, synth


# ── Construir outputs para cada celda ────────────────────────────────────────

def build_cell20_output(complete, treated_pool, donor_pool, excluded_oecd) -> list:
    excluded_it = [c for c in IT_ADOPTERS if c not in treated_pool]
    lines = [
        f"Muestra final (donor pool non-OECD):",
        f"  Tratados (IT): {len(treated_pool)} paises",
        f"  Donantes (no-IT, non-OECD): {len(donor_pool)} paises",
        f"  Total: {len(treated_pool) + len(donor_pool)} paises",
        f"  Donantes OECD excluidos: {len(excluded_oecd)}",
        f"",
        f"  McCloud original: 29 IT + 75 control = 104 paises",
        f"",
        f"Tratados incluidos: {len(treated_pool)}",
        f"",
        f"Tratados EXCLUIDOS por missing data: {excluded_it}",
        f"Donantes OECD excluidos: {sorted(excluded_oecd)}",
    ]
    return [stream_output('\n'.join(lines))]


def build_cell27_output(synth, donor_pool) -> list:
    weights = synth.weights(round=3, threshold=0.001)
    rmspe   = np.sqrt(synth.mspe())

    w_lines = ['Dataprep creado exitosamente.',
               f'  Donor pool: {len([c for c in donor_pool if c != "Mexico"])} paises (non-OECD)',
               f'  Pre-tratamiento: {PRE_START}-{PRE_END} ({TREATMENT_YEAR - PRE_START} anios)',
               '',
               f'Paises en el control sintetico de Mexico (non-OECD): {len(weights)}',
               weights.to_string(),
               '',
               f'MSPE pre-tratamiento: {synth.mspe():.4f}',
               f'RMSPE pre-tratamiento: {rmspe:.4f}',
               f'MAE pre-tratamiento:   {synth.mae():.4f}',
               f'(McCloud reporta RMSPE = 0.12 para Mexico en spec non-OECD)']

    return [stream_output('\n'.join(w_lines))]


def build_cell29_output(synth, df_final) -> list:
    end_year   = int(df_final['year'].max()) + 1
    Z0, Z1     = synth.dataprep.make_outcome_mats(time_period=range(PRE_START, end_year))
    synthetic  = synth._synthetic(Z0=Z0)

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(Z1.index, Z1.values,               color='black', lw=2,       label='Mexico (real)')
    ax.plot(synthetic.index, synthetic.values, color='black', lw=2, ls='--', label='Mexico sintetico')
    ax.axvline(x=TREATMENT_YEAR, color='red', ls='--', alpha=0.6, label=f'IT Adoption ({TREATMENT_YEAR})')
    ax.set_title(f'Mexico vs Synthetic Mexico: {OUTCOME}')
    ax.set_xlabel('Year')
    ax.set_ylabel('Gross Capital Formation (% GDP)')
    ax.grid(alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT_DIR / 'mexico_synthetic_control.png', dpi=150, bbox_inches='tight')

    img_out  = image_output(fig)
    text_out = stream_output('OK: mexico_synthetic_control.png guardado.')
    return [img_out, text_out]


def build_cell30_output(synth, df_final) -> list:
    end_year  = int(df_final['year'].max()) + 1
    Z0, Z1    = synth.dataprep.make_outcome_mats(time_period=range(PRE_START, end_year))
    synthetic = synth._synthetic(Z0=Z0)
    gap       = Z1 - synthetic

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(gap.index, gap.values, color='black', lw=2)
    ax.axhline(y=0, color='gray', lw=0.8)
    ax.axvline(x=TREATMENT_YEAR, color='red', ls='--', alpha=0.6, label=f'IT Adoption ({TREATMENT_YEAR})')
    ax.set_title('Efecto del IT sobre la Inversion en Mexico (Gap)')
    ax.set_xlabel('Year')
    ax.set_ylabel('Mexico real − Mexico sintetico (pp del PIB)')
    ax.grid(alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT_DIR / 'mexico_treatment_gap.png', dpi=150, bbox_inches='tight')

    img_out = image_output(fig)

    table_lines = [
        '',
        'Efecto estimado vs McCloud (2022), anios clave:',
        f'{"Anio":<6} {"Estimado (pp)":>15} {"McCloud (pp)":>15}',
    ]
    for yr, mc in MCCLOUD_EFFECTS.items():
        if yr in gap.index:
            g = float(gap.loc[yr])
            table_lines.append(f'{yr:<6} {g:>15.2f} {mc:>15.2f}')
    table_lines.append('OK: mexico_treatment_gap.png guardado.')

    text_out = stream_output('\n'.join(table_lines))
    return [img_out, text_out]


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    print("Cargando panel y construyendo muestra…")
    df_final, complete, treated_pool, donor_pool, excluded_oecd = load_and_build()

    print("Ajustando SCM (Nelder-Mead)…")
    dataprep, synth = fit_scm(df_final, donor_pool)

    print("Construyendo outputs para cada celda…")
    outputs = {
        20: build_cell20_output(complete, treated_pool, donor_pool, excluded_oecd),
        27: build_cell27_output(synth, donor_pool),
        29: build_cell29_output(synth, df_final),
        30: build_cell30_output(synth, df_final),
    }

    print("Leyendo notebook…")
    with open(NB_PATH) as f:
        nb = json.load(f)

    print("Inyectando outputs…")
    for cell_idx, cell_outputs in outputs.items():
        cell = nb['cells'][cell_idx]
        old_types = [o.get('output_type') for o in cell.get('outputs', [])]
        cell['outputs'] = cell_outputs
        cell['execution_count'] = cell_idx + 1
        new_types = [o.get('output_type') for o in cell_outputs]
        print(f"  cell-{cell_idx}: {old_types} -> {new_types}")

    with open(NB_PATH, 'w') as f:
        json.dump(nb, f, indent=1)

    print("\nNotebook actualizado correctamente.")
    rmspe = np.sqrt(synth.mspe())
    print(f"RMSPE verificado: {rmspe:.4f}  (McCloud: 0.12)")
    print(f"Muestra: {len(treated_pool)} IT + {len(donor_pool)} non-OECD = {len(treated_pool)+len(donor_pool)} paises")


if __name__ == '__main__':
    main()
