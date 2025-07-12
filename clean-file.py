import pandas as pd

df = pd.read_csv( 'datatran2024-3.csv', dtype='unicode' )

# delect unesessary collumn 
df = df.drop( columns=['Unnamed: 30','Unnamed: 31',  'Unnamed: 32'  ])

# how much null values 
# print( df.isnull().sum() )

# delect null values
df = df.dropna()

df.to_csv('clean-archive.csv', index=False)