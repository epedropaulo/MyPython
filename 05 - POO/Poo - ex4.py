"""Neste exercício terei uma classe Aluno que tem como atributos nome, curso e tempo sem dormir.
e métodos estudar e dormir."""


class Aluno:
    def __init__(self, nome, curso, tempoSemDormir):
        self.nome = nome
        self.curso = curso
        self.tempoSemDormir = tempoSemDormir

    def estudar(self, estudo):
        """Aumenta a quantidade de tempo sem dormir com base num número dado.
        int -> muda atributo"""
        self.tempoSemDormir += estudo

    def dormir(self, dormi):
        """Diminui a quantidade de tempo sem dormir com base num número dado.
        int -> muda atributo"""
        self.tempoSemDormir -= dormi

        if self.tempoSemDormir < 0:
            self.tempoSemDormir = 0


enzo = Aluno('Enzo', 'Engenharia', 16)
print(enzo.tempoSemDormir)
enzo.dormir(8)
print(enzo.tempoSemDormir)
enzo.estudar(16)
print(enzo.tempoSemDormir)
