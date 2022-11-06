# Lista original
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usando a função filter para filtrar com base na preposição da função lambda
pares = list(filter(lambda x: x % 2 == 0, num))

impares = list(filter(lambda x: x % 2 != 0, num))

print(pares)
print(impares)
