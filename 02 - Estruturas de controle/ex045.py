from random import randint
print('-=-' * 6)
print('     JOKENPÔ')
print('-=-' * 6)
print('')
print('Vamos ver se você consegue me vencer...')
print('')
itens = ['PEDRA', 'PAPEL', 'TESOURA']
cpu = randint(0, 2)
j1 = int(input('[ 0 ] para pedra.\n'
               '[ 1 ] para papel.\n'
               '[ 2 ] para tesoura.\n'
               'Qual você escolhe? '))
print('')
if j1 == 0 or j1 == 1 or j1 == 2:
    print('==' * 12)
    print(f'Eu escolhi {itens[cpu]}.')
    print(f'Você escolheu {itens[j1]}.')
    print('==' * 12)
    if cpu == j1:
        print('Parece que houve um EMPATE!!')
    elif j1 == 1 and cpu == 2 or j1 == 2 and cpu == 3 or j1 == 3 and cpu == 1:
        print('Parece que você PERDEU!!')
    else:
        print('Parece que você GANHOU!!')
else:
    print('OPÇÃO INVÁLIDA!!! TENTE NOVAMENTE!!!')
