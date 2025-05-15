import pandas as pd
import numpy as np
import random
from numpy.random import randn

#importar o csv
df = pd.read_csv('data/leresalvar_csv.csv') #importa o arquivo csv na variavel df
print(df.head()) #exibe o df.head

#pegar dados de forma aleatoria
print(df.sample(2))

#selecionar somente uma coluna e imprimir na tela
print(df['X'])

#selecionar mais colunas e imprimir na tela
print(df[['X','Y']])

#Selecionar as colunas com base no index
print(df.loc[10:15]) #pega os registros com o index 10 ao 15
print(df.loc[10:15, ['W','X']]) # Pega os registros com o index 10 ao 15, somente as colunas W e X

#Selecionar as colunas com base na posição do cursor
print(df.iloc[10]) #pega os registros com a posição 10
print(df.iloc[10:15]) # Pega os registros com a posição 10 ao 15

#Filtrar resultados por uma condição
print('somente os resultados com a coluna W maiores que zero')
Registro_positivo = (df['X'] > 0) # filtra os resultados que a coluna X são maiores que 0 e coloca na variavel registro_positivo
print(df[Registro_positivo]) #printa o resultado

print('somente os resultados com a coluna W e X maiores que zero')
Registro_positivo = (df['X'] > 0) & (df['Y'] > 0) # filtra os resultados que a coluna X e Y são maiores que 0 e coloca na variavel registro_positivo
print(df[Registro_positivo]) #printa o resultado

print('Agora filtrar por string')
Registro_stringer = (df['W'].str.contains('A')) #filtra os resultados que contenham a letra A
print(df[Registro_stringer])

Registro_stringer = (df['W'].str.contains('^A')) #filtra os resultados que comecem com a letra A
print(df[Registro_stringer])

Registro_stringer = (df['W'].str.contains('^M')) #filtra os resultados que comecem com a letra M
print(df[Registro_stringer])