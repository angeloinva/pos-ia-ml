import pandas as pd
import numpy as np

#criar uma lista
data = {'Nome':['Angelo','Maiara','Ana Cé', 'Paulo', 'Salete','Nenéns da Ana Maria','Ana Maria'],
        'Cidade':['Rio do Sul','Rio do Sul','Rio do Sul','Rio do Sul','Rio do Sul','Taió','Taió'],
        'Estado':['SC','SC','SC','SC','SC','SC','SC'],
        'Salario':['10000','5000','0','1800','1800','0','2000']}

df = pd.DataFrame(data) #cria um dataframe com essa lista acima

print(df) #exibe o conteudo da df

grupo = df.groupby('Cidade')



