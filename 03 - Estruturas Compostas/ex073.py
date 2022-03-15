time = ('flamengo', 'santos', 'palmeiras', 'grêmio', 'atlético paranaense', 'são paulo', 'corinthians', 'internacional',
        'fortaleza', 'goiás', 'bahia', 'atlético mineiro', 'vasco da gama', 'fluminense', 'botafogo', 'ceará',
        'cruzeiro', 'csa', 'chapecoense', 'avaí')
print('')
print(f'Lista do brasileirão: {time}')
print('=-=' * 15)
print(f'Os 5 primeiros são {time[:5]}')
print('=-=' * 15)
print(f'Os 4 últimos são {time [-4:]}')
print('=-=' * 15)
print(f'A lista em ordem alfabética é: {sorted(time)}')
print('=-=' * 15)
print(f'A chapecoense está na posição: {time.index("chapecoense") + 1}°')
