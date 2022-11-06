from time import ctime

class Caderno:
    """A classe caderno é uma lista de listas, onde cada sub-lista representa uma folha,
    e um elemento da sub-lista representa a respectiva linha."""

    def __init__(self, folhas=[], totalPaginas=0):
        self.folhas = folhas
        self.totalPaginas = totalPaginas

    def novaFolha(self):
        """Adiciona uma lista (folha) a nossa lista de listas."""
        self.folhas.append([])
        print('Uma nova página foi adicionada com sucesso!')

    def rasgarFolha(self, folha=0):
        """Retira uma certa folha do caderno(valor padrão a última folha).
        None, int -> List"""
        if self.folhas == []:
            print('A lista já estava vazia.')
            return None
        rasgado = self.folhas[folha - 1]
        del self.folhas[folha - 1]

        return rasgado

    def escrever(self, linha, folha):
        """Adiciona um elemento na última sub-lista, ou seja, escreve uma linha no caderno.
        str, int -> None"""
        self.folhas[folha - 1].append(linha)
        print('Linha adicionada com sucesso!')

    def imprimir(self):
        """Printa a classe de uma maneira organizada e de melhor entendimento."""
        for i in range(len(self.folhas)):
            print(f'Folha {i + 1}')
            for j in self.folhas[i]:
                print(f'{j}')
            print('')


"""a = Caderno([    # Testes sobre a classe caderno.
    ['L1F1', 'L2F1', 'L3F1'],
    ['L1F2', 'L2F2', 'L3F2'],
    ['L1F3', 'L2F3', 'L3F3'],
])
a.imprimir()
a.rasgarFolha()
"""


class Diario(Caderno):
    """Classe filha da classe caderno, que em toda primeira linha de folhas é escrita a data."""

    def __init__(self, folhas=[], totalPaginas=0):
        super().__init__( folhas, totalPaginas)

    def novaFolha(self):
        self.folhas.append([ctime()])
        print('Uma nova página foi adicionada com sucesso!')
