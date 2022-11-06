def area(larg, comp):
    s = larg * comp
    print(f'O terreno com {larg}x{comp} tem {s}m².')


# Programa principal
print('Controle de Terrenos')
print('--' * 10)
l = float(input('Largura [M]: '))
c = float(input('Comprimento [M]: '))
area(l, c)
