km = float(input('Digite a velocidade (em km/h): '))
print('Analisando...')
x = (km - 80) * 7
if km > 80:
    print('Você ultrapassou o limite de velocidade!!!'
          f' Foi multado em R${x :.2f}')
else:
    print('Parabéns! Você está no limite de velocidade.')
