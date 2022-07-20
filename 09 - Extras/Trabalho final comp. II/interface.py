# https://pt.stackoverflow.com/questions/519070/como-transitar-entre-janelas múltiplas janelas tkinter
# Telas: Menu principal, jogo, pause, perdeu, estatística.

class Interface:
    """Classe que cuidará da interface e da interação com o usuário.
    Atributos:
    Métodos: """

    def __init__(self):
        pass

    class BotaoPadrao:
        """Essa será a classe principal para formar os botões: todos tem um texto, uma função, um tamanho, 
            uma certa cor, fonte, animação de passar o mouse por cima, etc... """
        def __init__(self, texto):
            self.texto = texto

        def funcao(self):
            """Será a função que esse certo botão fará"""
            pass
    
    class Telas:
        """Como haverá telas 'parecidas', um menu principal, um menu de pause e onde o jogo rodará.
            Acho interessante que essas telas compartilhem alguns atributos semelhantes.
            Atributos: nome das telas, o tamanho, se o tamanho é mutável
            Métodos: Gera uma nova tela"""
        def __init__(self, nome):
            pass

        def gerar_tela(self):
            
            pass

    def qual_tecla():
        """Percebe qual tecla, o usuário respondeu e retorna sua representação como um número inteiro.
        evento -> int"""
        pass
    
    def mostra_pilha(pilhas):
        """Recebe as pilhas e as plota para serem visualizadas visualmente pelo jogador(label com borda)*
        Pilha"""
        pass
