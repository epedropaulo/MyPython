#Faça uma função que dado um intervalo fechado [a, b] e um número de pontos n, retorna o array
#X, formado pelos n pontos obtidos a partir do intervalo[a, b], e Y é o array onde Yi = Xi**2 - 9.
import numpy as np

def Conjuntos(intervalo, n):
    x = np.linspace(intervalo[0], intervalo[1], n)

    y = x**2 - 9

    return x, y
