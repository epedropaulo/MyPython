"""Neste exercicio tenho a classe Triangulo que tem os lados e o perimetro como atributos
e os métodos calcularPerimetro e getMaiorLado."""


class Triangulo:
    def __init__(self):
        self.LadoA = int(input('Digite o primeiro lado: '))
        self.LadoB = int(input('Digite o segundo lado: '))
        self.LadoC = int(input('Digite o terceiro lado: '))

        global lados    # Declaração global para a lista lados, para facilitar o método getMaiorLado.
        lados = [self.LadoA, self.LadoB, self.LadoC]

        for i in range(0, 3):    # For para comprovação que o triângulo pode ser formado com os valores dados.
            if lados[i] > lados[i - 2] + lados[i - 1]:
                raise 'Soma dos valores incompatível com um triângulo.'

        self.perimetro = self.LadoA + self.LadoB + self.LadoC   # Adiciona o atributo perimetro.

        semiperimetro = self.perimetro/2

        # Utiliza a fórmula matemática de heron para calcular a área do triângulo, apenas com os lados.
        self.area = (semiperimetro * (semiperimetro - lados[0]) * (semiperimetro - lados[1]) * (semiperimetro - lados[2])) ** (1/2)

    def getMaiorLado(self):
        """Compara os lados e retorna o maior.
        none -> int"""

        maior = 0
        for i in range(0, 3):
            if maior < lados[i]:
                maior = lados[i]

        return maior


triangulo1 = Triangulo()
print(triangulo1.getMaiorLado())
print(f"{triangulo1.area:.2f}")
