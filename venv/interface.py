from tkinter import *

janela = Tk()

janela = Tk();
L = "800"
A = "800"
E = "100"
T = "100"
tamanho = str(L + "x" + A + "+" + E + "+" + T)
janela.geometry(tamanho)
janela.title("Cadastro !")
janela["bg"] = "blue"
corJanela = janela["bg"]
corReversa = "orange"

menubar = Menu(janela)

opt1 = Menu(menubar, tearoff = 0)

janela.config(menu=menu)

opt1.add_command(label="Cadastro de usuários")