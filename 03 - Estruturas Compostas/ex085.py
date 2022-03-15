valores = [[], []]

for p in range(1, 8):
    valor = int(input(f'Digite o {p}° valor: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)
print('-=' * 30)
print(f'Os valores pares são: {sorted(valores[0])}')
print(f'Os valores impares são: {sorted(valores[1])}')
