from random import randint
from time import sleep

print('--' * 20)
print(f'{"JOGA NA MEGA SENA" :^40}')
print('--' * 20)
megasena = []
vezes = int(input('Quantos jogos você quer que eu sorteie? '))
print('')
print(f'-=-=-= SORTEANDO {vezes} JOGOS -=-=-=')
for v in range(0, vezes):
    megasena.append([])
    while len(megasena[v]) != 6:
        num = randint(0, 60)
        if num not in megasena[v]:
            megasena[v].append(num)
    print(f'Jogo {v + 1}: {sorted(megasena[v])}')
    sleep(1)
print('-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=')
