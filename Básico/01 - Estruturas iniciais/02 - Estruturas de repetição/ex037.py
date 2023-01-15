print('')
print('-=-' * 10)
print('TRANSFORMADOR DE BASES!')
print('-=-' * 10)
num = int(input('Digite o número inteiro: '))
print('Digite [ 1 ] para binário.\n'
      'Digite [ 2 ] para octal.\n'
      'Digite [ 3 ] para hexadecimal.')
base = int(input('Qual base você deseja? '))
if base == 1:
    print(f'O {num} convertido para binário é {bin(num)[2:]}')
elif base == 2:
    print(f'O {num} convertido em octal é {oct(num)[2:]}')
elif base == 3:
    print(f'O {num} convertido em hexadecimal é {hex(num)[2:]}')
else:
    print('Digite uma base válida!')
