from tkinter import *
from banco import *

def raise_frame(frame):
    frame.tkraise()

janela = Tk()

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
bd = Banco("localhost", "root", "", "livro")

Entry

Buton(janela, bg="blue", text="Cadastrar")


#
# f1 = Frame(janela, bg="orange")
# f2 = Frame(janela, bg="orange")
#
# topo = janela.winfo_toplevel()
#
# menubar = Menu(topo)
#
# opt1 = Menu(menubar, tearoff = 0)
#
# opt1.add_command(label="Cadastro de usuários", command=lambda: raise_frame(f1))
# opt1.add_command(label="Cadastro de produtos", command=lambda: raise_frame(f2))

# menubar.add_cascade(label="Cadastros", menu=opt1)
#
# topo.config(menu=menubar)

janela.mainloop()
