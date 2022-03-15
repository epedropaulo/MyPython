num = vezes = soma = 0

print('Para sair do loop digite 999 !')
while num != 999:
    vezes += 1
    num = int(input(f'Digite o {vezes}° número: '))
    if num != 999:
        soma += num
print(f'A soma dos seus {vezes - 1} números foi de {soma}.')
