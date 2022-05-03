# EXERCÍCIO 2
from random import randint, sample


def SemRepeticao(valores):
    """Sorteará uma quantidade dada de números, tendo inicio e fim. Que não possua repetições.
    input -> inicio (valor inicial do intervalo de sorteio)
             fim (valor final do intervalo de sorteio)
             quantidade (quantidade de números sorteados)
    output -> lista (uma lista com números não repetidos sorteados)"""

    while True:
        
        num = randint(1, 60)

        if num not in valores:
            valores.append(num)

            return valores


def FazCartela(nCartelas):
    """Definirá quais valores estão em cada cartela, e as armazenará em uma matriz.
    input-> nCartelas
    output -> matrizCartelas"""
    matrizCartelas = []
    
    for i in range(0, nCartelas):
        valoresCartela = sample(range(1, 61), 6)
        matrizCartelas.append(valoresCartela)
    
    return matrizCartelas


def EscolheCartela(nCartelas):
    conjuntoValores = []
    while True:
        conjuntoValores = SemRepeticao(conjuntoValores)

        for i in range(0, len(nCartelas)):
            if nCartelas[i] in conjuntoValores:
                return nCartelas[i]


def main():
    numCartelas = int(input('Digite o número de cartelas participantes: '))
    matrizCartelas = FazCartela(numCartelas)
    cartelaSorteada = EscolheCartela(matrizCartelas)
    print(cartelaSorteada)
    

main()
