def ficha(nome='<desconhecido>', ngols=0):
    print(f'O jogador {nome} fez {ngols} gol(s) no campeonato.')


# Programa Principal
jogador = str(input('Nome do jogador: ')).strip().capitalize()
gols = str(input('Número de gols: ')).strip()
if jogador == '':
    jogador = '<desconhecido>'
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
ficha(jogador, gols)
