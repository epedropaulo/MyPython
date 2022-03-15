# O fatorial de um número usando while.

print('-=-' * 8)
print('  FATORIAL DE UM NÚMERO')
print('-=-' * 8)

fatorial = 1
num = int(input('Digite o número: '))
antecessor = num
vezes = ''

if num > 0:
    while antecessor != 1:
        fatorial *= antecessor
        vezes += str(antecessor) + ' x '
        antecessor -= 1
    print(f'O fatorial de {num} é igual a {fatorial}.')
    print(vezes + f'1 = {fatorial}')
    print(f'')
elif num == 0:
    print('O fatorial de 0 é 1.')
else:
    print('Digite um número positivo!!')
