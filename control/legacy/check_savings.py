import pandas as pd
from pathlib import Path

df = pd.read_csv(r'D:\2026\clases\final_econometria\data\panel_mccloud_mexico.csv')
df['year'] = df['year'].astype(int)

IT_ADOPTERS = {
    'Australia','Canada','Finland','Iceland','Israel','Japan','Korea, Rep.','New Zealand',
    'Norway','Spain','Sweden','United Kingdom','Brazil','Chile','Colombia','Czechia',
    'Dominican Republic','Ghana','Guatemala','Hungary','Indonesia','Mexico','Paraguay',
    'Peru','Philippines','Poland','Romania','Thailand','Uruguay'
}
OECD = set(df[df['oecd_member']==1]['country_name'].unique())

pre = df[(df['year'] >= 1990) & (df['year'] <= 2000)]

# Non-OECD donors
non_oecd_donors = [c for c in df['country_name'].unique() if c not in IT_ADOPTERS and c not in OECD]

pre_donors = pre[pre['country_name'].isin(non_oecd_donors)]
coverage = pre_donors.groupby('country_name')['gross_savings'].apply(lambda x: x.notna().all())

complete = coverage[coverage].index.tolist()
incomplete = coverage[~coverage].index.tolist()

print(f'Non-OECD donors con gross_savings completo (1990-2000): {len(complete)} / {len(non_oecd_donors)}')
print(f'Excluidos por falta de savings: {len(incomplete)}')
print(f'Excluidos: {sorted(incomplete)}')

# With savings: how many donors would survive?
all_vars = ['gdp_growth','log_population','gdp_deflator_inflation','oil_exporter','gross_savings']
outcome = 'gross_capital_formation'
completeness = pre_donors.groupby('country_name')[all_vars + [outcome]].apply(
    lambda x: x.isnull().sum().sum()
)
survivors = completeness[completeness==0].index.tolist()
print(f'\nPool con savings incluido: {len(survivors)} donantes')
print(f'Pool sin savings (actual): 83')
print(f'Perdemos: {len(non_oecd_donors) - len(survivors)} donantes adicionales')
