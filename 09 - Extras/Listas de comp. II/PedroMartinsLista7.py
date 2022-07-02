import numpy as np

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
