cores = ['\033[m', '\033[31m', '\033[34m']
print('\n'
      'Digite o comprimento de três retas para saber se é possível formar um triângulo com elas.')
r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo  segmento: '))
r3 = float(input('Digite o terceiro segmento: '))
if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print(f'Essas retas {cores[2]}PODEM FORMAR{cores[0]} um triângulo!!!')
    print('ShowShow...')
    if r1 == r2 == r3:
        print('É um triângulo EQUILÁTERO!!')
    elif r1 != r2 != r3 != r1:
        print('É um triângulo ESCALENO!!')
    else:
        print('É um triângulo ISÓSCELES!!')
else:
    print(f'Essas retas {cores[1]}NÃO PODEM FORMAR{cores[0]} um triângulo!!!')
    print('putz...')
