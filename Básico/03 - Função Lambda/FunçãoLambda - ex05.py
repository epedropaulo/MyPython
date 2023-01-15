num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usando a função map para fazer com que a função lambda seja aplicada para cada item de num
quadrado = list(map(lambda x: x**2, num))
cubo = list(map(lambda x: x**3, num))

# Exibindo o resultado
print(quadrado)
print(cubo)
