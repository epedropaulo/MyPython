totgols = 0

jogadores = []
registro = {}
gols = []

while True:
    print('--' * 25)
    registro['nome'] = str(input('Nome do jogador: ')).capitalize()
    partidas = int(input(f'N° de partidas de {registro["nome"]}: '))

    for a in range(0, partidas):
        gol = int(input(f'  Quantos gols foram feitos na {a + 1}° partida: '))
        gols.append(gol)
        totgols += gol
    registro['gols'] = gols[:]
    gols.clear()
    registro['total'] = totgols
    totgols = 0

    jogadores.append(registro.copy())

    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while continuar not in 'SN':
        print('ERRO! Digite apenas S ou N.')
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print('-=' * 25)
print('cod nome         gols        total')
print('--' * 20)
for k, v in enumerate(jogadores):
    print(f'{k:>4} ', end='')
    for a in v.values():
        print(f'{str(a):<12}', end='')
    print()
while True:
    print('--' * 20)
    dados = int(input('Mostrar dados de qual jogador? [999 acaba] '))
    if dados == 999:
        break
    if dados <= len(jogadores) - 1:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[dados]["nome"]}')
        for i, g in enumerate(jogadores[dados]['gols']):
            print(f'   No jogo {i + 1} fez {g} gols.')
    else:
        print(f'ERRO! Não existe jogador com código {dados}! Tente novamente.')
print('<<< VOLTE SEMPRE >>>')
