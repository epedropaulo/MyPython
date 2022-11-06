from random import randint
from time import sleep
from operator import itemgetter

jogos = dict()
ranking = dict

for c in range(1, 5):
    jogos[f'jogador{c}'] = randint(1, 6)

print('Valores sorteados:')
for k, v in jogos.items():
    print(f'    O {k} tirou {v} no dado')
    sleep(1)

ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)

print('-=' * 20)
print('  == Ranking dos jogadores ==')
for i, v in enumerate(ranking):
    print(f'    {i + 1}° lugar: {v[0]} com {v[1]}')
    sleep(1)
