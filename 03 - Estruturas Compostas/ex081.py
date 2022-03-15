valores = []
while True:
    valores.append(int(input('Digite um número: ')))
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Tente novamente! Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar in 'N':
        break
print('-=' * 30)
print(f'Foram digitados {len(valores)} números.')
print(f'De forma decrescente os valores ficam: {sorted(valores, reverse=True)}')
if 5 in valores:
    print('O número cinco foi digitado!')
else:
    print('O número cinco não foi digitado!')
