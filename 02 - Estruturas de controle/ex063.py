print('-=-' * 9)
print('   SEQUÊNCIA DE FIBONACCI')
print('-=-' * 9)

vezes = int(input('Digite quantos termos da sequência tu quer ver: '))

t1 = 0
t2 = 1
cont = 3

if vezes >= 1:
    print(f'{t1} ', end='')
if vezes >= 2:
    print(f'-> {t2} ', end='')
if vezes >= 3:
    while cont <= vezes:
        t3 = t1 + t2
        print(f'-> {t3} ', end='')
        t1 = t2
        t2 = t3
        cont += 1
print('\nEspero que tenha gostado.')
