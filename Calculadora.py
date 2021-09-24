# Calculadora aprimorada usando while, continue, break e boolean
from tkinter import *
from functools import partial


# Funções da calculadora

def click_ponto():
    caixatexto.insert(END, ".")

def click_multi():
    primeiro_numero = caixatexto.get()
    global p_numero
    global matematica
    matematica = "multiplica"
    p_numero = float(primeiro_numero)
    caixatexto.delete(0, END)

def click_divi():
    primeiro_numero = caixatexto.get()
    global p_numero
    global matematica
    matematica = "divisao"
    p_numero = float(primeiro_numero)
    caixatexto.delete(0, END)

def click_sub():
    primeiro_numero = caixatexto.get()
    global p_numero
    global matematica
    matematica = "menos"
    p_numero = float(primeiro_numero)
    caixatexto.delete(0, END)

def click_igual():
    segundo_numero = caixatexto.get()
    caixatexto.delete(0, END)
    if matematica == "mais":
        caixatexto.insert(0, p_numero + float(segundo_numero))
    if matematica == "menos":
        caixatexto.insert(0, p_numero - float(segundo_numero))
    if matematica == "multiplica":
        caixatexto.insert(0, p_numero * float(segundo_numero))
    if matematica == "divisao":
        caixatexto.insert(0, p_numero / float(segundo_numero))


def click_soma():
    primeiro_numero = caixatexto.get()
    global p_numero
    global matematica
    matematica = "mais"
    p_numero = float(primeiro_numero)
    caixatexto.delete(0, END)

def deletar():
    caixatexto.delete(0, END)

def click_button(numero):
    atual = caixatexto.get()
    caixatexto.delete(0, END)
    caixatexto.insert(END, str(atual) + str(numero))


# Interface gráfica

janela = Tk()
janela.title("Calculadora")
janela.geometry("280x380")
janela.resizable(False, False)

# Caixa de texto
caixatexto = Entry(janela)
caixatexto.pack(padx=10, pady=50)

# Botões de números
sete = Button(janela, text="7", pady=14, padx=14, bd=4, command=lambda: click_button(7))
sete.place(x=10, y=100)
quatro = Button(janela, text="4", pady=14, padx=14, bd=4, command=lambda: click_button(4))
quatro.place(x=10, y=155)
um = Button(janela, text="1", pady=14, padx=14, bd=4, command=lambda: click_button(1))
um.place(x=10, y=210)

oito = Button(janela, text="8", pady=14, padx=14, bd=4, command=lambda: click_button(8))
oito.place(x=60, y=100)
cinco = Button(janela, text="5", pady=14, padx=14, bd=4, command=lambda: click_button(5))
cinco.place(x=60, y=155)
dois = Button(janela, text="2", pady=14, padx=14, bd=4, command=lambda: click_button(2))
dois.place(x=60, y=210)

nove = Button(janela, text="9", pady=14, padx=14, bd=4, command=lambda: click_button(9))
nove.place(x=110, y=100)
seis = Button(janela, text="6", pady=14, padx=14, bd=4, command=lambda: click_button(6))
seis.place(x=110, y=155)
tres = Button(janela, text="3", pady=14, padx=14, bd=4, command=lambda: click_button(3))
tres.place(x=110, y=210)
ponto = Button(janela, text=".", pady=14, padx=14, bd=4, command= click_ponto)
ponto.place(x=110, y=265)

divi = Button(janela, text="/", pady=14, padx=14, bd=4, command= click_divi)
divi.place(x=155, y=100)
multi = Button(janela, text="X", pady=14, padx=14, bd=4, command= click_multi)
multi.place(x=155, y=155)
menos = Button(janela, text="-", pady=14, padx=14, bd=4, command= click_sub)
menos.place(x=155, y=210)
mais = Button(janela, text="+", pady=14, padx=14, bd=4, command=  click_soma)
mais.place(x=155, y=265)

c = Button(janela, text="C", pady=100, padx=14, bd=4, command=  deletar)
c.place(x=205, y=100)
igual = Button(janela, text="=", pady=12, padx=40, bd=4, command = click_igual)
igual.place(x=10, y=265)

janela.mainloop()
