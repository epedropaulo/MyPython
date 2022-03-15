print('==' * 14)
print('   REGISTRADOR DE PESSOAS!')
print('==' * 14)

idade18 = homens = mulher = 0

while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    print('')
    if sexo in 'MF':
        if idade > 18:
            idade18 += 1
        if sexo in 'M':
            homens += 1
        elif sexo in 'F' and idade < 20:
            mulher += 1
        resposta = str(input('Deseja cadastrar mais pessoas? [S/N] ')).upper().strip()
        if resposta in 'N':
            break
    else:
        print('DIGITE UM SEXO VÁLIDO!!!')
print('')
print(f'Houve um total de {idade18} pessoas que são maiores de 18.')
print(f'E foram registrados {homens} homens.')
print(f'E houve a ocorrência de {mulher} mulheres com menos de 20.')
print('Espero que tenha alcançado os objetivos!!')
