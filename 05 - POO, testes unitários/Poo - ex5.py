"""Neste exercício será um pouco mais complexo. Terá 3 classes que interagem entre si
A primeira classe será Aluno que possui como atributo nome e cpf.
A segunda classe será Equipe que possui como atributo uma lista de participantes do tipo Aluno e um atributo chamado
projeto.
A terceira classe será GerenciadorEquipes que possui como atributo uma lista de todas as equipes formadas,
com método criar equipe."""


class Aluno:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf


class Equipe:
    def __init__(self, alunos, projeto):
        self.alunos = alunos
        self.projeto = projeto


class GerenciadorEquipes:
    def __init__(self, equipes):
        self.equipes = equipes

    def criarEquipe(self, alunos2, projeto):
        """Cria a equipe recebendo como parametro uma lista de alunos e o seu projeto.
        list, str -> Equipe"""

        # Loop para impedir a criação de novas equipes com o mesmo projeto.
        for i in range(0, len(self)):
            if self[i].projeto == projeto:
                raise 'Não pode ser criado duas equipes com o mesmo projeto.'

        return Equipe(alunos2, projeto)


# Criando objetos do tipo Aluno
Joao = Aluno('Joao', 123)
Ethan = Aluno('Ethan', 123)
Allemand = Aluno('Allemand', 123)
Enzo = Aluno('Enzo', 123)
Paulo = Aluno('Paulo', 123)
DG = Aluno('DG', 123)
Pedro = Aluno('Pedro', 123)
Dudu = Aluno('Dudu', 123)

# Criando equipes
Equipe1 = Equipe([Joao, Ethan], 'Dev')
Equipe2 = Equipe([Allemand, Enzo], 'Arte')
Equipe3 = Equipe([Paulo, DG], 'PC')

# Lista de equipes já criadas
Equipes = [Equipe1, Equipe2, Equipe3]

# Criando equipe pelo método.
Equipe4 = GerenciadorEquipes.criarEquipe(Equipes, [Pedro, Dudu], 'Python')

