totgols = 0

registro = dict()
gols = list()

registro['nome'] = str(input('Nome do jogador: ')).capitalize()
partidas = int(input(f'N° de partidas de {registro["nome"]}: '))

for a in range(0, partidas):
    gol = int(input(f'Quantos gols foram feitos na {a}° partida: '))
    gols.append(gol)
    totgols += gol
registro['gols'] = gols
registro['total'] = totgols

print('-=' * 30)
for k, v in registro.items():
    print(f'O campo {k} tem o valor {v}.')

print('-=' * 30)
print(f'O jogador {registro["nome"]} jogou {partidas} partidas')
for i, v in enumerate(gols):
    print(f'  => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {totgols} gols')
