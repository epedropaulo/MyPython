from random import randint
from time import sleep
jogador = randint(0, 5)
print(' ')
print('-=-' * 26)
print('O computador vai pensar em um número de 0 a 5. Você cosegue acertar qual é ??')
print('-=-' * 26)
computador = int(input('Adivinhe o número de 0 a 5: '))
print('Pensando...')
sleep(2)
print(' ')
if jogador == computador:
    print('Parabéns! Você acertou!!!')
else:
    print('O computador te venceu...\n'
          f'O número que ele pensou foi: {jogador} e não {computador}.')
