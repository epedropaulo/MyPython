print('-=-' * 7)
print('  TERMOS DE UMA P.A.')
print('-=-' * 7)

primeiro = float(input('Digite o primeiro termo da pa: '))
razao = float(input('Digite a razão da pa: '))

termos = 0
quantidade = 10
mais = 1

while mais != 0:
    while termos != quantidade:
        termo = primeiro + razao * termos
        print(f'{termo} -> ', end='')
        termos += 1
    print('Pausa.')
    print('')
    print('Digite 0 termos para sair do programa!')
    mais = int(input('Quantos termos a mais você quer ver? '))
    quantidade = mais + termos
print(f'Finalizou a progressão aritmética com {quantidade} termos.')
