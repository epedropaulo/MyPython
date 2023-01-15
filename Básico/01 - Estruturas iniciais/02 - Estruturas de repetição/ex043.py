print('-=-' * 7)
print('ANALISADOR DE IMC')
print('-=-' * 7)
peso = float(input('Digite o seu peso (em kg): '))
altura = float(input('Digite a sua altura (em cm): '))
imc = peso / (altura / 100) ** 2
print(f'Seu imc é de {imc :.2f}.')
if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc < 25:
    print('Você está no peso ideal.')
elif imc < 30:
    print('Você está sobrepeso.')
elif imc < 40:
    print('Você está obeso.')
else:
    print('Você está em obesidade mórbida.')
