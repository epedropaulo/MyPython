"""Neste exercício vou criar uma classe funcionario que tem como atributos nome e salário,
e o método aumentar salário"""


class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

        if not type(salario) == int and not type(salario) == float:     # Verificação no tipo do salário.
            raise TypeError

    def aumentarSalario(self, porcentagem):
        """Método que aumenta o salário com base numa porcentagem dada.
        int -> mudança no atributo"""
        self.salario += (porcentagem/100) * self.salario


harry = Funcionario("Harry", 2500)
harry.aumentarSalario(10)
print(harry.salario)
