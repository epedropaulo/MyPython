# Colocar os blocos nas pilhas com o teclado e não com o mouse

"""Arquivo contendo as classes que fazem a mecânica do jogo."""

import numpy as np


class MatrizTela:
    """Classe que representará a matriz que aparecerá na tela
    Atributos: A matriz que armazenará todos os blocos, A lista das jogadas.
    Métodos: jogada(faz a jogada), junta(junta os blocos), gera(gera um novo bloco)"""
    
    def __init__(self):
        """Recebe o array com os blocos já postos, por padrão cria com 2 blocos aleatórios."""
        self.blocos = []
        self.jogadas = []
        pass
    
    def __str__(self):
        """Muda como é mostrado quando da print nesse objeto"""
        pass

    def jogada(self, jogada):
        """Dado a jogada a faz. Mudando o atributo da matriz tela.
        str -> none"""
        pass

    def junta(self, jogada):
        """Dado a última jogada, verifica se possui blocos para se juntar. Muda o atributo da matriz_tela.
        str -> none"""
        pass
    
    def gera(self):
        """Gera um novo bloco, muda o atributo da matriz_tela."""
        pass

 
class Mecanica:
    """Classe que conterá os métodos para o funcionamento do jogo."""
    def __init__(self):
        pass
    
    def perdeu(matrizTela):
        """Dado a matriz Tela verifica se é possível fazer alguma jogada. Se não for o jogador
        Perdeu. Retorna True se Perdeu, e False se ganhou.
        MatrizTela -> bool"""
        pass

    def ganhou(matrizTela):
        """Dado a matriz Tela verifica se há um bloco com o valor de 2048 foi formado. Se sim o jogador
        ganhou. Retorna True caso ganhe, e False caso continue.
        MatrizTela -> bool"""
        pass
