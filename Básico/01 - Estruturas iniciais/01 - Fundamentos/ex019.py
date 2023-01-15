import random
a = input('Digite a primeira pessoa: ')
b = input('Digite a segunda  pessoa: ')
c = input('Digite a terceira pessoa: ')
lista = [a, b, c]
print(f'O escolhido foi {random.choice(lista)}!')
