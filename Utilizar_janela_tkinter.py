# Importa a biblioteca tkinter
from tkinter import *
import requests

#Pega as cotações de dólar, euro e BTC
def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    # Exibe o texto no console
    # print(texto)

    # pega o texto_cotacoes, na propriedade text e adiciona o valor da variavel texto
    texto_cotacoes["text"] = texto





# Cria a janela
janela = Tk()

# Muda o título
janela.title("Abrindo janelas com TKINTER")

# Adiciona um texto dentro da janela
texto_orientacao = Label(janela, text="Seja bem vindo, clique no botão abaixo para exibir as cotações")
# Coloca o texto na posição 0,0 no grid
texto_orientacao.grid(column=0, row=0)

# Adiciona um botão que aciona uma função quando acionado
botao = Button(janela, text="Ver cotações", command=pegar_cotacoes)
botao.grid(column=0, row=1)

# Cria um texto para ser exibido o resultado das cotações
texto_cotacoes = Label(janela, text="")
texto_cotacoes.grid(column=0, row=2)



# Esse comando deixa a janela aberta, se não colocar ela fecha sozinha
janela.mainloop()