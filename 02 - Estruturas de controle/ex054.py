from datetime import date

maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input(f'Digite o {c}° ano: '))
    idade = date.today().year - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'Existem {maior} maiores, e existem {menor} menores.')
