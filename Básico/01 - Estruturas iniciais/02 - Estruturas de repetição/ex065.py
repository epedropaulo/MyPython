from time import sleep
cont = ''
vezes = soma = 0

while cont != 'N':
    vezes += 1
    num = int(input(f'Digite o {vezes}° número: '))
    soma += num
    media = soma / vezes
    if vezes == 1:
        menor = num
        maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    cont = str(input('Quer digitar mais valores [S/N] ? ')).upper().strip()[0]
    if cont != 'N' and cont != 'S':
        while cont != 'N' and cont != 'S':
            print('')
            print('Digite algo válido.')
            cont = str(input('Quer digitar mais valores [S/N] ? ')).upper().strip()[0]
print('')
print('Finalizando o programa...')
print('')
sleep(2)
print(f'O menor número foi o {menor} e o maior foi o {maior}.')
print(f'Você digitou {vezes} números e a média foi de {media}.')
