import pandas as pd
import numpy as np

df = pd.read_csv('data/sales_raw.csv')

print (df.head())

print(df.dtypes) # Mostra os tipos de dados de cada coluna

print('Agora converterei o customer number para int')
df['Customer Number'] = df['Customer Number'].astype('int') #Converte a coluna customer number para int

print('exibe agora com o customer number convertido para int')
print (df.head())


print('agora vou tirar o cifrao e a vírgula da coluna 2016 e depois converter para ')
df['2016'] = df['2016'].str.replace(',','') #tirei a virgula
df['2016'] = df['2016'].str.replace('$','') #tirei o cifrao
df['2016'] = df['2016'].astype('float64') #converti para float64
print('Agora exibindo sem a virgula e sem o cifrao')
print (df.head())


print('converte a coluna Active para boolean')
df['Active'] = np.where(df['Active'] == 'Y', True, False) #aplica uma condição:sempre que tiver Y na coluna "Active" ele transforma para True e se não for Y ele transforma para false
print('Agora exibindo com a coluna active em boolean')
print (df.head())

