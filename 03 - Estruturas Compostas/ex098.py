from time import sleep


def contador(i, f, p):
    print('~' * 40)
    if p == 0:
        p = 1

    if i > f and p > 0:
        p = -p

    if p < 0:
        print(f'Contagem de {i} até {f + 1} de {-p} em {-p}')
    else:
        print(f'Contagem de {i} até {f - 1} de {p} em {p}')
    for c in range(i, f, p):
        print(c, end=' ')
        sleep(0.5)
    print('FIM!')


# Programa Principal
contador(1, 11, 1)
contador(10, -1, -2)

print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)
