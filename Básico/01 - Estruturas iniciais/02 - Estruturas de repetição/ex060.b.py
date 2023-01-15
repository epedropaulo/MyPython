# O fatorial de um número usando for.

print('-=-' * 8)
print('  FATORIAL DE UM NÚMERO')
print('-=-' * 8)

fatorial = 1
num = int(input('Digite o número: '))
parameter = num

if num > 0:
    for c in range(parameter, 0, -1):
        fatorial *= num
        num -= 1
    print(f'O fatorial de {parameter} é {fatorial}')
elif num == 0:
    print('O fatorial de 0 é 1.')
else:
    print('Digite um número positivo!!.')
