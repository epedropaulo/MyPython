import numpy as np
from random import uniform

# Exercício 1
def geraMatriz(a, b, n, m):
    """A função gera uma matriz que recebe como parâmetros de entrada (a, b, n, m) e que tem como retorno
    um array Numpy de formato MxM, onde os elementos são os n números igualmente espaçados obtidos ao
    se dividir o intervalo [a, b]."""
    x = np.linspace(a, b, n)

    if n != m**2:
        return 'Não é possível construir.'
    
    x.shape = (m, m)

    return x


# Exercício 2
def linha(M, i):
    """A função recebe como parâmetro de entrada um array M e um número inteiro i. O formato (n, m) do array M não é passado 
    como parâmetro de entrada. Retorna a linha i de M. Se M não possui linha i, a mensagem 
    'Nao existe esta linha' deve ser retornada.
    array, inteiro -> array"""
    if len(M.shape) > 2:
        return 'Isso não é uma matriz!'

    if M.shape[0] < i:
        return f'A matriz não possui a linha {i}'
    
    return M[i, :]


def coluna(M, i):
    """A função recebe como parâmetro de entrada um array M e um número inteiro i. O formato (n, m) do array M não é passado 
    como parâmetro de entrada. Retorna a coluna i de M. Se M não possui coluna i, a mensagem 
    'Nao existe esta coluna' deve ser retornada.
    array, inteiro -> array"""
    if len(M.shape) > 2:
        return 'Isso não é uma matriz!'

    if M.shape[1] < i:
        return f'A matriz não possui a coluna {i}'
    
    return M[:, i]


# Exercício 3
def f(intervalo, n):
    """Faça uma função que dado um intervalo fechado [a, b] e um número de pontos n, retorna o array
    X, formado pelos n pontos obtidos a partir do intervalo[a, b], e Y é o array onde Yi = Xi**2 - 9.
    array, inteiro-> array, array, array"""

    x = np.linspace(intervalo[0], intervalo[1], n)

    y = x**2 - 9

    condicao = y >= 0
    
    return x, y, condicao

    """A = f([-10,10],10)
        
    yPositivo = A[1][ A[2]] #   Array com os valores positivos, usando o array booleano como índice.
        
    yNegativo = A[1][ A[2] == False] #   Array com os valores negativos, usando o array booleano como índice."""


# Exercício 4
def polinomio(coeficientes, x):
    """A função retornará um valor de X dado os coeficientes do polinômio de grau (len(coeficientes))
    array, float -> float"""
    if x == 0:
        return coeficientes[0]

    grau = len(coeficientes)    # O grau do nosso polinômio

    arrayComX = np.ones(grau) * x

    xElevado = np.cumprod(arrayComX) / x    # Arruma o fato de na var ArrayComX não aparece o X**0 depois de cumprod ele divide todos por x.

    poli = coeficientes * xElevado

    valor = np.sum(poli)

    return valor
    
# Exercício 5
def sample(n):
    """A função divide o intervalo [0, 1] em n intervalos de mesmo comprimento. Depois sortea um valor e verifica em qual intervalo
    está esse valor sorteado.
    int -> int"""
    q = np.linspace(0, 1, n)

    qcumsoma = np.cumsum(q) # O cumsum é necessário para facilitar a comparação do número sorteado com o intervalo.
    
    valor = uniform(0, 1)   # Sorteando

    intervalo = qcumsoma[qcumsoma >= valor][0]  # Ele verifica em quais intervalos o valor está contido, e seleciona o primeiro intervalo.

    x = np.searchsorted(q, intervalo)   # Descobrimos o índice desse intervalo e o retornamos.

    return x