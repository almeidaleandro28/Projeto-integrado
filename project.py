import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv('datatran2024.csv', encoding='latin-1')
df = pd.read_csv('datatran2024-2.csv', dtype='unicode')

acidentesFatais = df[ df['feridos_graves'].isin( ['1'] ) ] 
principaisCausas = acidentesFatais['causa_acidente'].value_counts().head( 8 )


# principaisCausas.plot( kind='barh', title='Principais causas de acidentes fatais')
# plt.xlabel('Números de Ocorrências')
# plt.show()

# ---------------------------------------------------------------------------------------------------------------

condicaoMetereologica = df[ 'condicao_metereologica'].unique()
tipoAcidente = df[ 'tipo_acidente' ].unique()


lista = df.groupby( [ 'condicao_metereologica', 'tipo_acidente' ] ).size().unstack( fill_value=0)

lista.plot( kind='bar', stacked=True, figsize=(12,6))
plt.title('relacao c ondicao metereologica e tipo acidente')
plt.xlabel('condicao metereoloogica')
plt.ylabel('numero acidente')
plt.legend('tipo de acidente')
plt.tight_layout()
plt.show()