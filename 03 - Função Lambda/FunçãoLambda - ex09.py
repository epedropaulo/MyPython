# Definindo as variaveis iniciais
lstnum = [2, 4, 6, 9, 11]
num = 2

# Usando map para fazer rodar a função lambda por toda lstnum
num2 = list(map(lambda x: x * num, lstnum))

print(num2)
