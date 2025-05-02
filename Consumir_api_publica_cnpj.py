import requests
from pprint import pprint

#define o cnpj
cnpj = "24227436000186"

#cria a url e adiciona o cnpj junto
url = f"https://publica.cnpj.ws/cnpj/{cnpj}"

#Faz a requisição usando a biblioteca requests, método get e passa a url como parametro
requisicao = requests.get(url)

# Printa o codigo (200 sucesso, 400 erro.. etc..)
print (requisicao)

# Printa em json identado usando o pprint
pprint(requisicao.json())

# Printa na tela somente o campo escolhido, nesse caso são campos dentro de listas, dentro de listas
atividade_principal = requisicao.json()["estabelecimento"]["atividade_principal"]["descricao"]
print("A atividade é:", atividade_principal)

#Fim do arquivo