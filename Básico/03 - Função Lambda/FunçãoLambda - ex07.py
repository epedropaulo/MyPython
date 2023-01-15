# Definindo as listas iniciais
num1 = [1, 2, 3, 5, 7, 8, 9, 10]
num2 = [1, 2, 4, 8, 9, 11]

# Usando a função filter que tem como parametro estar no 1 e no 2,
num3 = list(filter(lambda x: x in num1, num2))
print(num3)
