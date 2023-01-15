# Definindo as listas iniciais
num = [1, 2, 3, 5, 7, 8, 9, 10]

# Usando a função filter que tem como parametro ser ou não ser par.
pares = list(filter(lambda x: x % 2 == 0, num))
impares = list(filter(lambda x: x % 2 != 0, num))

print(len(pares))
print(len(impares))
