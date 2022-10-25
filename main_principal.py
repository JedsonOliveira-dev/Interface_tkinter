from tkinter import *


def selecao():
    if var.get() == 1:
        selecionou = "Você selecionou: Opção 01"
        label.config(text=selecionou, font='arial 20')
    elif var.get() == 2:
        selecionou = "Você selecionou: Opção 02"
        label.config(text=selecionou, font='arial 20')
    elif var.get() == 3:
        selecionou = "Você selecionou: Opção 03"
        label.config(text=selecionou, font='arial 20')
    elif var.get() == 4:
        selecionou = "Você selecionou: Opção 04"
        label.config(text=selecionou, font='arial 20')
    else:
        label.config(text='Escolha uma das opções', font='arial 20')


window = Tk()
window.title('Interface com tkinter')
window.geometry('500x300+550+300')
var = IntVar()
radio01 = Radiobutton(window, text="Opção 01", font='arial 12 bold', bd=5, padx=15, pady=6, variable=var, value=1,
                      command=selecao)
radio01.pack(anchor=W)

radio02 = Radiobutton(window, text="Opção 02", font='arial 12 bold', bd=5, padx=15, pady=6, variable=var, value=2,
                      command=selecao)
radio02.pack(anchor=W)

radio03 = Radiobutton(window, text="Opção 03", font='arial 12 bold', bd=5, padx=15, pady=6, variable=var, value=3,
                      command=selecao)
radio03.pack(anchor=W)

radio04 = Radiobutton(window, text="Opção 04", font='arial 12 bold', bd=5, padx=15, pady=6, variable=var, value=4,
                      command=selecao)
radio04.pack(anchor=W)


label = Label(window)
label.pack()
window.mainloop()
