from time import sleep


def maior(*num):
    print('=-=' * 15)
    print('Analisando os valores passados...')
    for a in num:
        print(a, end=' ')
        sleep(0.3)
    if len(num) != 0:
        print(f'Foram informados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi {max(num)}.')
    else:
        print('Não foi informado nenhum valor.')
        print(f'O maior valor informado foi 0.')


# Programa Principal
maior(9, 4, 5, 7, 1, 3)
maior(4, 7, 0)
maior(1, 2)
maior(5)
maior()
