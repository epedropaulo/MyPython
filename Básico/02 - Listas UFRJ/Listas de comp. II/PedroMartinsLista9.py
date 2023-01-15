from tkinter import *


def questao1():
    """Cria a janela como pedido no exercício. 
    none -> none"""

    inicio = Tk()

    inicio.geometry('175x140+350+350')

    lblNorth = Label(inicio, text='label 1', font='bold')
    lblNorth.grid(column=1, row=0, sticky=N)

    lblSouth = Label(inicio, text='label 2', font='bold')
    lblSouth.grid(column=1, row=2, sticky=S)

    lblWest = Label(inicio, text='label 3', font='bold')
    lblWest.grid(column=0, row=1, sticky=W)

    lblEast = Label(inicio, text='label 4', font='bold')
    lblEast.grid(column=2, row=1, sticky=E)

    vazio = Label(inicio)   # Criei esse label vazio para que ele fique no centro da nossa matriz, para que possa
    vazio.grid(column=1, row=1, padx=30, pady=30)   # Colocar o espaço entre as outras células.

    inicio.mainloop()


def questao2():
    """A def pede ao usuário que escreva uma palavra e escreve em um Label seu inverso.
    none -> none"""

    def comandbtn(entrada):
        tamanho = len(entrada)
        entradaReverse = entrada[tamanho::-1]   # Faz o recorte da string com o passo de -1

        resposta = Label(inicio, text=entradaReverse)
        resposta.grid(column=1, row=1, sticky=W, padx=5, pady=5)

    inicio = Tk()

    texto = Label(inicio, text='Enter a word:')
    caixa = Entry(inicio)
    reverseButton = Button(inicio, text='Validate', command = lambda: comandbtn(caixa.get()))

    texto.grid(column=0, row=0, sticky= W, padx=10, pady=10)
    caixa.grid(column=1, row=0, sticky= E, padx=5, pady=5)
    reverseButton.grid(column=1, row=2, sticky=EW, padx=5, pady=5)

    inicio.mainloop()


def questao3():
    """É feita uma interface com duas entrys, e um label. Clicando no label sera printado no console a soma das duas entradas
    none -> none"""

    def printar(e, valor1, valor2):
        v1 = int(valor1)
        v2 = int(valor2)

        print(v1 + v2)

    inicio = Tk()

    texto = Label(inicio, text='Clique aqui para printar a soma das entradas.')
    entrada1 = Entry(inicio)
    entrada2 = Entry(inicio)

    texto.bind('<ButtonRelease-1>', lambda e: printar(e, entrada1.get(), entrada2.get() ))

    texto.grid(column=0, row=0, rowspan=2, sticky=W, padx=10, pady=10)
    entrada1.grid(column=1, row=0, sticky=EW)
    entrada2.grid(column=1, row=1, sticky=EW)

    inicio.mainloop()


def questao4():
    """Sera feita uma interface com duas entradas, e clicando no botão aparecerá na interface a soma dos 2 valores.
    none -> none"""

    def comandbtn(valor1, valor2):

        resultado = int(valor1) + int(valor2)
        
        resposta = Label(inicio, text=f'The sum of {valor1} + {valor2} = {resultado}')
    
        resposta.grid(column=1, row=2, sticky=W, padx=2, pady=2)

    inicio = Tk()

    texto1 = Label(inicio, text='Enter the first value:')
    entrada1 = Entry(inicio)

    texto2 = Label(inicio, text='Enter the second value:')
    entrada2 = Entry(inicio)

    sumButton = Button(inicio, text='Validate', command = lambda: comandbtn(entrada1.get(), entrada2.get()))

    texto1.grid(column=0, row=0, sticky= W, padx=2, pady=2)
    entrada1.grid(column=1, row=0, sticky= E, padx=2, pady=2)

    texto2.grid(column=0, row=1, sticky= W, padx=2, pady=2)
    entrada2.grid(column=1, row=1, sticky= E, padx=2, pady=2)

    sumButton.grid(column=1, row=3, sticky=EW, padx=2, pady=2)

    inicio.mainloop()


def questao5():
    """Cria uma interface com duas entradas uma estática e outra para receber a entrada, depois de clicar no botão,
    Na entrada estática aparecerá o dobro da entrada.
    none -> none"""
    def comandbtn(valor, entrada):

            resultado = int(valor)*2
            
            entrada['state'] = 'normal'
            entrada.delete(0, END)
            entrada.insert(0, resultado)
            entrada['state'] = 'disabled'

            entrada.grid(column=1, row=1, sticky= E, padx=2, pady=2)

    inicio = Tk()

    texto1 = Label(inicio, text='Enter the value:')
    entrada1 = Entry(inicio)

    texto2 = Label(inicio, text='The double of the value is:')
    entrada2 = Entry(inicio)


    sumButton = Button(inicio, text='Validate', command = lambda: comandbtn(entrada1.get(), entrada2))

    texto1.grid(column=0, row=0, sticky= W, padx=2, pady=2)
    entrada1.grid(column=1, row=0, sticky= E, padx=2, pady=2)

    texto2.grid(column=0, row=1, sticky= W, padx=2, pady=2)

    sumButton.grid(column=1, row=2, sticky=EW, padx=2, pady=2)


    inicio.mainloop()

