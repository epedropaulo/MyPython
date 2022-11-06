class Pilha:
    def __init__(self, elementos= []):

        if type(elementos) == list:
            self.elementos = elementos
            print('O valor foi armazenado com sucesso.')
        
        else:
            self.elementos = []
            print('O valor não foi armazenado! Ao invés disso, armazenamos uma lista vazia.')


    def empilhar(self, elemento):
        """Adiciona um elemento na pilha.
        * -> none"""

        self.elementos.append(elemento) 


    def desempilhar(self):
        """Retira um elemento da pilha
        none -> Objeto retirado"""

        if len(self.elementos) > 0:

            ultimo = self.elementos[-1]
            del self.elementos[-1]
            
            return ultimo

        else:
            print('Erro! A lista já está vazia.')


    def getPilha(self):
        """Retorna uma cópia dos elementos da pilha em formato de lista
        none -> list"""

        return self.elementos


    def lenPilha(self):
        """Retorna o tamanho da pilha
        none -> int"""

        return len(self.elementos)


    def  __add__(self, other):
        """Permite o uso de operadores soma para instâncias da classe Pilha."""

        if type(other) != Pilha or type(self) != Pilha:
            print('Operação feita apenas com elementos do tipo pilha.')
        
        else:

            pilha3 = list(self.getPilha() + other.getPilha())
            
            return Pilha(pilha3)


    def mostra(self):
        """Printa os elementos da Pilha"""

        print(self.elementos)

# 7.a)
p1 = Pilha([1, 7, 9])
p2 = Pilha()

# 7.c)
p2.empilhar(4)
p2.empilhar(10)

# 7.d)
p2.desempilhar()
p2.mostra()

ultimo = p2.desempilhar()
p2.mostra()

# 7.e)
p2.empilhar(5)
p2.mostra()

# 7.g)
p3 = p2 + p1
p2.mostra()
p3.mostra()

p4 = p1 + p2
p1.mostra()
p4.mostra()
