"""Consiste em testar a biblioteca pytest. que quando colocamos o nome da função de teste, ele permite execução de
apenas a função em si, ótimo para depuração de código."""

import pytest


def soma(a, b):
    """Soma dois números dados
    int, int -> int"""
    return a + b


def test1():
    """Com a biblioteca ativa, e colocando o nome da função """
    assert 5 == soma(3, 2)


def test2():
    assert 6 == soma(3, 2)


class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def soma(self):
        return self.a + self.b

    def subtracao(self):
        return self.a - self.b

    def multiplicacao(self):
        return self.a * self.b

    def divisao(self):
        return self.a / self.b


num = Calculadora(10, 2)


def test3():
    assert 12 == num.soma()

    assert 8 == num.subtracao()

    assert 20 == num.multiplicacao()

    assert 5 == num.divisao()
