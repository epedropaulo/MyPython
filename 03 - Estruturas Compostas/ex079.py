valores = []

while True:
    valor = int(input('Digite um valor: '))
    if valor in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        valores.append(valor)
        print('Valor adicionado com sucesso!')
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Tente novamente! Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print('-=' * 25)
print(f'Você digitou os valores {sorted(valores)}')
