lista = []
registro = {}
soma = 0

while True:
    registro['nome'] = str(input('Nome: ')).strip().capitalize()

    registro['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
    while registro['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        registro['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]

    registro['idade'] = int(input('Idade: '))
    soma += registro['idade']

    lista.append(registro.copy())

    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while continuar not in 'SN':
        print('ERRO! Por favor, digite apenas S ou N')
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    print('--' * 30)
    if continuar == 'N':
        break
media = soma / len(lista)

print(f'- O grupo tem {len(lista)} pessoas.')
print(f'- A média de idade é de {media :.2f} anos')
print(f'- As mulheres cadastradas foram: ', end='')
for a in lista:
    if a['sexo'] == 'F':
        print(a['nome'], end='  ')
print()
print('- Lista das pessoas que estão acima da média:')
for a in lista:
    if a['idade'] >= media:
        print('     ', end='')
        for k, v in a.items():
            print(f'{k} = {v}; ', end='')
        print('')
print('<< ENCERRADO >>')
