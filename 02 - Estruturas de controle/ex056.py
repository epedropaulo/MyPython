media = 0
maior = 0
count = 0
for p in range(1, 5):
    print('')
    print(f'----- {p}° PESSOA -----')
    nome = str(input('Nome: ')).strip()

    idade = int(input('Idade: '))
    media += idade/4

    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    if sexo == 'M':
        if idade > maior:
            maior = idade
            nome1 = nome
    elif sexo == 'F':
        if idade < 21:
            count += 1
    else:
        print('DIGITE UM SEXO VÁLIDO!!!')
print('')
print(f'A idade média deles é: {media :.1f}')
print(f'O nome do homem mais velho é: {nome1}')
print(f'A quantidade de mulheres com menos de 21 é: {count}')
