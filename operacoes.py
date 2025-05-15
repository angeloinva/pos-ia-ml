import pandas as pd
import numpy as np
from numpy.random import randn

np.random.seed(101)

df = pd.read_csv('data/sales_clear.csv')

print (df.head())

soma = df['2016'] + df['2017'] # soma as 2 colunas e joga pra variavel soma
print(soma) #exibe o valor da variavel soma

df['Total biênio'] = df['2016'] + df['2017'] # cria uma nova coluna com a soma da coluna 2016 com a de 2017

print('A dataframe com uma nova coluna')
print (df.head(5)) # Mostra o valor da dataframe com 5 linhas

print('iniciando o drop')
df.drop(['Total biênio'], axis=1, inplace=True)

print('mostrando depois do drop')
print (df.head(5)) # Mostra o valor da dataframe com 5 linhas