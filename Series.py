# Importa o panda como pd
import pandas as pd
# cria uma series "serie1" com os valores e labels, os labels são os indexadores
serie1 = pd.Series(['43', '26', '3'], index=['Angelo','Maiara','Aninha'])

# Executa a serie "serie1"
serie1

# Filtra o dado pelo index 1
serie1['Maiara']

# Escreve a frase utilizando o valor já filtrado
print('A maiara possui', serie1['Maiara'], 'anos')
print('O Angelo possui', serie1['Angelo'])

# Usa nome variavel
nomedapessoa = 'Maiara'
print('A pessoa possui', serie1[nomedapessoa], 'anos')