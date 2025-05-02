# Importa a biblioteca tkinter
from tkinter import *

# Cria a janela
janela = Tk()

# Muda o título
janela.title("Abrindo janelas com TKINTER")

# Adiciona um texto dentro da janela
texto_orientacao = Label(janela, text="Seja bem vindo, clique no botão abaixo para exibir as cotações")
# Coloca o texto na posição 0,0 no grid
texto_orientacao.grid(column=0, row=0)

# Esse comando deixa a janela aberta, se não colocar ela fecha sozinha
janela.mainloop()