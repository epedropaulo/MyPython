valores = []
impares = []
pares = []
while True:
    valor = int(input('Digite um número: '))
    valores.append(valor)
    continuar = str(input('Deseja continuar? [S/N] ')).upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Tente novamente! Deseja continuar? [S/N]')).upper()[0]
    if continuar in 'N':
        break
for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-=' * 30)
print(f'Todos os valores são: {valores}')
print(f'Os pares são: {pares}')
print(f'Os ímpares são: {impares}')
