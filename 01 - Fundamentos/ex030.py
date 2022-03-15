from time import sleep
num = int(input('Digite um número para descobrir se ele é par ou ímpar: '))
print(f'\033[4;34mAnalisando\033[m o número {num}...')
sleep(1.5)
print(' ')

if (num % 2) == 0:
    print('Se trata de um número \033[1;31mPAR!!')
else:
    print('Se trata de um número \033[1;31mÍMPAR!!')
