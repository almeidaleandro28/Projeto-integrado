import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv('datatran2024.csv', encoding='latin-1')
df = pd.read_csv('datatran2024-2.csv', dtype='unicode')

causaAcidentes = df['causa_acidente']
causaAcidentesUnq = df['causa_acidente'].unique()
pcausasAcidentes = df['causa_acidente'].value_counts()

classificacaoAcidente = df['classificacao_acidente'].unique()
pclassificacaoAcidente = df['classificacao_acidente'].value_counts()

acidentesFatais = df[ df['feridos_graves'].isin( ['1'] ) ] 
principaisCausas = acidentesFatais['causa_acidente'].value_counts().head( 8 )


principaisCausas.plot( kind='barh', title='Principais causas de acidentes fatais')
plt.xlabel('Números de Ocorrências')
plt.show()

