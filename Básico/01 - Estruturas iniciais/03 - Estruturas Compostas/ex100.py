from random import randint
from time import sleep
numeros = []


def sortear(lst):
    print('Sorteando 5 valores da lista temos: ', end='')
    for c in range(0, 5):
        num = randint(0, 10)
        print(num, end=' ')
        lst.append(num)
        sleep(0.3)
    print('PRONTO!')


def somar(num):
    somapar = 0
    for c in num:
        if c % 2 == 0:
            somapar += c
    print(f'Somando os valores pares de {num}, temos {somapar}')


# Programa principal
sortear(numeros)
somar(numeros)
