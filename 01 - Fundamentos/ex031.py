km = float(input('Digite o km da sua viagem: '))
if km <= 200:
    x = km * 0.50
else:
    x = km * 0.45
print(f'O preço da sua viagem será de R${x :.2f}')
