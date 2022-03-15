valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um número para a posição {c}: ')))

menor = min(valores)
maior = max(valores)
primeiro = 0
print('=-' * 25)
print(f'Os valores foram: {valores}')
print(f'O menor valor é {menor}, e está nas posições: ', end='')
for c in range(0, valores.count(menor)):
    print(f'{valores.index(menor, primeiro)}... ', end='')
    primeiro = valores.index(menor) + 1

primeiro = 0

print(f'\nO maior valor é {maior}, e está nas posições: ', end='')
for c in range(0, valores.count(maior)):
    print(f'{valores.index(maior, primeiro)}... ', end='')
    primeiro = valores.index(maior) + 1
