class livro:
    def __init__(self, titulo, autor, paginastotal, paginaslidas):
        self.titulo = titulo
        self.autor = autor
        self.paginastotal = paginastotal
        self.paginaslidas = paginaslidas

    def ler(self, paginashoje):
        jalido = (self.paginaslidas * 100) / self.paginastotal

        if self.paginaslidas + paginashoje < self.paginastotal:
            self.paginaslidas += paginashoje
        else:
            self.paginaslidas = self.paginastotal

        leu = (self.paginaslidas * 100) / self.paginastotal

        return f'Tinha lido {jalido:.2f}% e com as paginas de hoje foi para {leu :.2f}%.'

    def voltarPaginas(self, voltar):
        jalido = (self.paginaslidas * 100) / self.paginastotal

        if self.paginaslidas - voltar > 0:
            self.paginaslidas -= voltar
        else:
            self.paginaslidas = 0

        leu = (self.paginaslidas * 100) / self.paginastotal

        return f'Tinha lido {jalido:.2f}% e voltando foi para {leu :.2f}%.'


class sublivro(livro):
    def __init__(self, titulo=0, autor=0, paginastotal=0, paginaslidas=0):
        super().__init__(titulo, autor, paginastotal, paginaslidas)

        if self.titulo == 0:
            self.setTitulo()

        if self.autor == 0:
            self.setAutor()

        if self.paginastotal == 0:
            self.setNumPaginas()

    def posicionarInicio(self):
        self.paginaslidas = 0

    def posicionarFinal(self):
        self.paginaslidas = self.paginastotal

    def setTitulo(self):
        self.titulo = input('Digite o título do livro: ')

    def setAutor(self):
        self.autor = input('Digite o nome do autor: ')

    def setNumPaginas(self):
        self.paginastotal = input('Digite o número de páginais totais: ')

    def setPaginasLidas(self):
        self.paginaslidas = input('Digite o número de página lidas: ')
