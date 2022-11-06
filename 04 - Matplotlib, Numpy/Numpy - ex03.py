# Faça uma função gera matriz que recebe como parâmetros de entrada (a, b, n, m) e que
# tem como retorno um array Numpy de formato m × m, onde os elementos são os n
# números igualmente espaçados obtidos ao se dividir o intervalo [a, b]. Caso não seja
# possível construir tal array, a função deve retornar a mensagem 'Nao é possível construir'.
import numpy as np


def geraMatriz(a, b, n, m):
    
    x = np.linspace(a, b, n)

    if n != m**2:
        return 'Não é possível construir.'
    
    x.shape = (m, m)

    return x


print(geraMatriz(0, 10, 16, 4)) # Caso sucesso.

print(geraMatriz(0, 10, 10, 4)) # Caso falho.