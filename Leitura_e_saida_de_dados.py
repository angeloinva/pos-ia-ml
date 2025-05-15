import pandas as pd
import numpy as np
from numpy.random import randn

np.random.seed(101)

# Método split() converte em lista
'w x y z'.split()

# Cria um dataframe randomizado com 20 linhas e 4 colunas, nomeando as 4 colunas como WXYZ, depois usa o método split pra converter em lista
df = pd.DataFrame(randn(20,4), columns='W X Y Z'.split())

# Imprime na tela o resultado da DataFrame, passando como parâmetro o head, para listar por default os primeiros registros da dataframe, o n=10 é para limitar a 10 registros
print(df.head(n=10))

# Imprime na tela o resultado da DataFrame, passando como parâmetro o tail, para listar por default os últimos registros da dataframe, o n=10 é para limitar a 10 registros
print(df.tail(n=10))

#Salva em CSV
df.head() #para pegar os 10 primeiros registros
df.to_csv('data/leresalvar_csv.csv', index=False) #para salvar o df.head no disco

#Ler em CSV
print('Agora a leitura do CSV') #aqui é só
df_csv = pd.read_csv('data/leresalvar_csv.csv') #lê o arquivo csv
print(df_csv.head()) #exibe na tela o resultado da leitura

