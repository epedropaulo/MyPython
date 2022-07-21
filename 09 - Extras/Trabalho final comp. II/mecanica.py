# Colocar os blocos nas pilhas com o teclado e não com o mouse

"""Arquivo contendo as classes que fazem a mecânica do jogo."""


class Mecanica:
    """Classe que conterá os métodos para o funcionamento do jogo"""
    def __init__(self):
        pass
    
    def gera_bloco(matriz_tela):
        """Dado a matriz tela, gera um novo bloco, e muda o atributo da matriz_tela.
        matriz_tela -> matriz_tela"""
        pass
    
    def junta(matriz_tela):
        """Dado a matriz tela verifica se possui blocos para se juntar. E muda o atributo da matriz_tela.
        matriz_tela -> matriz_tela"""
        pass

    def jogada(matriz_tela, lado):
        """Dado a matriz tela e o lado para que se vira, faz a jogada e muda o atributo da matriz,
        com a jogada feita. (Chama a def junta?)
        matriz_tela, tecla -> matriz_tela"""
        pass

class MatrizTela:
    """Classe que representará a matriz que aparecerá na tela
    Atributos: A matriz que armazenará todos os blocos"""
    
    def __init__(self):
        """Recebe o array com os blocos já postos, por padrão cria vazio."""
        pass