print('Somador de números pares.')
s = 0
for c in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
print(f'A soma dos pares é {s}')
