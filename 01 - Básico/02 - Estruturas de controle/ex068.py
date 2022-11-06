from random import randint


cont = 0
while True:
    print('-=-' * 10)
    jogador = ' '
    while jogador not in 'PI':
        jogador = str(input('Você escolhe par ou ímpar? [P/I]')).upper().strip()[0]
    print('')
    njogador = int(input('Qual número você escolhe [0/10]? '))
    print('')
    npc = randint(0, 10)
    print(f'Eu escolhi {npc}...')
    resultado = npc + njogador

    if resultado % 2 == 0:
        print(f'E {resultado} é par!')
        if jogador == 'P':
            print('Parabéns!!!')
            cont += 1
        if jogador == 'I':
            print('Perdeu...')
            break
    else:
        print(f'E {resultado} é ímpar!')
        if jogador == 'P':
            print('Perdeu...')
            break
        if jogador == 'I':
            print('Parabéns!!!')
            cont += 1
    print('Vamos jogar novamente...')

print(f'Você conseguiu ganhar {cont} vez(es) seguida(s)!')
