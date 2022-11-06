matriz = [[], [], []]
somapar = soma3 = 0

for L in range(0, 3):
    for C in range(0, 3):
        matriz[L].append(int(input(f'Digite o valor [{L}, {C}]: ')))

print('-=' * 30)
for L in range(0, 3):
    for C in range(0, 3):
        num = matriz[L][C]
        print(f'[{num :^5}]', end='')
        if num % 2 == 0:
            somapar += num
    print()
    soma3 += matriz[L][2]

print('-=' * 30)
print(f'A soma de todos os pares é {somapar}')
print(f'A soma dos valores da terceira coluna é {soma3}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
