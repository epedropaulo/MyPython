for p in range(1, 6):
    peso = float(input(f'Peso da {p}° pessoa (kg): '))
    if p == 1:
        menor = peso
        maior = peso
    elif peso < menor:
        menor = peso
    if peso > maior:
        maior = peso
print(f'O menor valor foi de {menor} kgs.')
print(f'O maior valor foi de {maior} kgs.')
