cores = ['\033[m', '\033[31m', '\033[34m']
div = 0
print('Analisador de números primos!')
num = int(input('Digite um número: '))
for c in range(1, num+1):
    if num % c == 0:
        print(f'{cores[2]} {c} {cores[0]}', end='')
        div += 1
    else:
        print(f'{cores[1]} {c} {cores[0]}', end='')
print(f'\nO número {num} foi divisível {div} vezes.')
if div == 2:
    print('E por isso ele É PRIMO!')
elif div == 1:
    print('Putz... O 1 é um caso complicado...')
else:
    print('E por isso ele NÃO É PRIMO!')
