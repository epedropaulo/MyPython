cont = soma = 0
while True:
    cont += 1
    n = int(input(f'Digite o {cont}° número [999 para sair]: '))
    if n == 999:
        cont -= 1
        break
    soma += n
print(f'Você digitou {cont} números e a soma deles foi {soma}!')
