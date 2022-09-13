"""Arquivo que conterá as classes que cuidarão da interface mostrada para o usuário, e também
da interação com o mesmo.

Será feito para o cmd do windows."""

import os

from msvcrt import getch

class Menu:
    """Classe que representará os botões.
    Atributos: botões(um array de strings). #Quando estiver no primeiro loop a primeira opção estará selecionada
    Método: função(a função do botão.)"""

    def __init__(self):
        """"""
        pass

    def __str__(self):
        """Muda como é mostrado quando da print nessa classe"""
        pass

    def entrada(self):
        """Chama o getch e o transforma em algo mais 'palpável'.
        none -> str"""
        pass

    def detecta(self):
        """Detecta em qual opção está selecionada. #Vendo em qual atributo-texto está a 'seta'.
        Retorna a opção selecionada, que depende em qual está selecionado."""
        pass

    def selecao(self, tecla):
        """Recebe uma str, e modifica a seleção da opção no momento."""
        pass
    
    def tela_pause(self, jogada):
        """Recebe a tecla apertada e caso seja a tecla que provoca o pause. Mostra a tela de pause
        str -> none"""
        pass

    def tela_pos_partida(self, situacao):
        """Recebe a situacao do jogo e mostra a tela ou de vitória ou de derrota.
        str -> none"""
        pass
    
    def comeca(self):
        """É a função do botão começa, começa um novo jogo"""
        pass
