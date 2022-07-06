"""Neste exercício fiz o meu primeiro programa utilizando programação orientada a objetos, com uma classe pricinpal e
uma subclasse."""


class livro:
    """Classe pricinpal do nosso programa, com atributos de titulo, autor, páginastotal e páginas lidas
    métodos ler e voltar Paginas."""

    def __init__(self, titulo, autor, paginastotal, paginaslidas):
        self.titulo = titulo
        self.autor = autor
        self.paginastotal = paginastotal
        self.paginaslidas = paginaslidas

    def ler(self, paginashoje):
        """Pede que o usuário introduza o número de páginas lidas no dia, e retorna uma str com certos dados.
        int -> str"""

        jalido = (self.paginaslidas * 100) / self.paginastotal

        if self.paginaslidas + paginashoje < self.paginastotal:
            self.paginaslidas += paginashoje
        else:
            self.paginaslidas = self.paginastotal

        leu = (self.paginaslidas * 100) / self.paginastotal

        return f'Tinha lido {jalido:.2f}% e com as paginas de hoje foi para {leu :.2f}%.'

    def voltarPaginas(self, voltar):
        """Pede pro usuário por um int, para voltar essa quantidade de páginas, e retorna uma string.
        int -> str"""

        jalido = (self.paginaslidas * 100) / self.paginastotal

        if self.paginaslidas - voltar > 0:
            self.paginaslidas -= voltar
        else:
            self.paginaslidas = 0

        leu = (self.paginaslidas * 100) / self.paginastotal

        return f'Tinha lido {jalido:.2f}% e voltando foi para {leu :.2f}%.'


class sublivro(livro):
    """Subclasse que adiciona interação com o usuário e métodos para posicionar o inicio e o final."""
    def __init__(self, titulo=0, autor=0, paginastotal=0, paginaslidas=0):
        super().__init__(titulo, autor, paginastotal, paginaslidas)

        if self.titulo == 0:
            self.setTitulo()

        if self.autor == 0:
            self.setAutor()

        if self.paginastotal == 0:
            self.setNumPaginas()

    def posicionarInicio(self):
        """Coloca a posição de paginas lidas para o começo."""
        self.paginaslidas = 0

    def posicionarFinal(self):
        """Coloca a posição de paginas lidas para o final."""
        self.paginaslidas = self.paginastotal

    def setTitulo(self):
        """Pede ao usuário o nome do título
        recebe str."""
        self.titulo = input('Digite o título do livro: ')

    def setAutor(self):
        """Pede ao usuário o nome do autor
        recebe str."""
        self.autor = input('Digite o nome do autor: ')

    def setNumPaginas(self):
        """Pede ao usuário o total de páginas
        recebe int."""
        self.paginastotal = int(input('Digite o número de páginais totais: '))

    def setPaginasLidas(self):
        """Pede ao usuário o total de páginas lidas
        recebe int."""
        self.paginaslidas = int(input('Digite o número de página lidas: '))
