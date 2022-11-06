"""Trabalho final de computação II, onde eu farei o jogo 2048 infinito."""


class Mecanica:
    """Classe que vai tratar da mecânica do jogo. 
    Métodos:  gerar o bloco, ter pilhas onde possam ser colocados, colocar os blocos, 
    somar os blocos. """

    def __init__(self):
        pass


    class Bloco:    #Perguntar se é bom!
        """São os blocos.
        Atributos: Número 'aleatório'.
        Método: Gera um novo bloco"""
        def __init__(self):
            pass
        
        def geraBloco():
            """Gera um novo bloco.
            none -> Bloco"""
            pass


    class Pilha:    
        """É a pilha onde será colocado os blocos. 
        Atributos: A lista de blocos.
        Métodos: Quando recebe um novo bloco verifica se é pra somar."""
        def __init__(self, blocos):
            self.blocos = blocos

        def soma(self, blocoNovo):
            """Recebe um bloco novo caso ele seja igual ao último bloco da lista, soma os 2 e forma um novo bloco,
            e muda o atributo blocos da própria pilha.
            Bloco -> Pilha"""
            pass

    def coloca(self, pilhas, bloco):
        """Dado um array de pilhas e um bloco novo, adiciona esse bloco a uma dessas pilhas, e retorna a nova pilha
        array, Bloco -> Pilha"""
        pass


class Interface:
    """Classe que cuidará da interface e da interação com o usuário.
    Atributos:
    Métodos: """

    def __init__(self):
        pass

    class BotaoPadrao:
        def __init__(self, texto):
            """Essa será a classe principal para formar os botões: todos tem um texto, uma função, um tamanho, 
            uma certa cor, fonte, animação de passar o mouse por cima, etc... """
            self.texto = texto

        def funcao(self):
            """Será a função que esse certo botão fará"""
            pass

