cor = ['\033[m', '\033[34m', '\033[31m']
salario = float(input(f'Qual é o {cor[1]}salário{cor[0]} do funcionário? R$'))
if salario > 1250:
    salario = (110/100) * salario
    print(f'Seu novo {cor[1]}salário{cor[0]} é de: {cor[2]}R${salario :.2f}{cor[0]} !')
else:
    salario = (115/100) * salario
    print(f'Seu novo {cor[1]}salário{cor[0]} é de: {cor[2]}R${salario :.2f}{cor[0]} !')
print('...')
