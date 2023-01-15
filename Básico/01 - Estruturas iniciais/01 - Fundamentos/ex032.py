from datetime import date
from time import sleep
ano = int(input('Descubra se é ou não bissexto, se quiser analisar o ano atual digite 0: '))

if ano == 0:
    ano = date.today().year
print(f'\033[34mAnalisando\033[m o ano {ano} ...')
print(' ')
sleep(1.5)


if (ano % 4) == 0 and (ano % 100) != 0:
    print('O ano \033[4;31mé\033[m bissexto!!')
elif (ano % 400) == 0:
    print('O ano \033[4;31é\033[m bissexto!!')
else:
    print('O ano \033[4;31mnão é\033[m bissexto!!')
