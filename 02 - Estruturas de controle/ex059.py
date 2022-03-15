from time import sleep

escolha = 0

print('-=-' * 5)
print('  CALCULADORA')
print('-=-' * 5)

while escolha != 6:
    if escolha == 0 or escolha == 5:
        num1 = float(input('Digite o 1° número: '))
        num2 = float(input('Digite o 2° número: '))
    sleep(2.3)
    print('-=-' * 7)
    print('[ 1 ] Somar.')
    print('[ 2 ] Subtrair.')
    print('[ 3 ] Multiplicar.')
    print('[ 4 ] Dividir.')
    print('[ 5 ] Novos números.')
    print('[ 6 ] Sair do programa.')
    print('')
    escolha = int(input('Digite a sua opção: '))

    if escolha == 1:
        operacao = 'soma'
        resultado = num1 + num2

    elif escolha == 2:
        operacao = 'subtração'
        resultado = num1 - num2

    elif escolha == 3:
        operacao = 'multiplição'
        resultado = num1 * num2

    elif escolha == 4:
        operacao = 'divisão'
        resultado = num1 / num2

    elif escolha == 5:
        print('Digite os novos números.')

    elif escolha == 6:
        print('Saindo do programa. Espero que tenha gostado...')

    else:
        print('DIGITE UMA OPÇÃO VÁLIDA!')
        print('')

    if 1 <= escolha <= 4:
        print(f'O resultado da sua {operacao} foi de {resultado}.')
    print('')
print('Fim.')
