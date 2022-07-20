# Colocar os blocos nas pilhas com o teclado e não com o mouse

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
        
        def gera_bloco():
            """Gera um novo bloco.
            none -> Bloco"""
            pass


    class Pilha:    
        """É a pilha onde será colocado os blocos. 
        Atributos: Um array de blocos.
        Métodos: Quando recebe um novo bloco verifica se é pra somar."""
        def __init__(self, blocos):
            self.blocos = blocos

        def soma(self, blocoNovo):
            """Recebe um bloco novo caso ele seja igual ao último bloco da Pilha, soma os 2 e forma um novo bloco,
            e muda o atributo blocos da própria pilha.
            Bloco -> Pilha"""
            pass

    def coloca(pilha, bloco):
        """Dado uma pilha e um bloco novo, adiciona esse bloco a essa pilhas. E retorna a nova pilha
        Pilha, Bloco -> Pilha"""
        pass
    
    def perdeu(pilhas):
        """Recebendo o conjunto de pilhas verifica se é possível colocar mais blocos, se não for possível 
        o jogador perdeu.
        se perdeu -> True
        se continua -> False
        pilhas -> bool"""