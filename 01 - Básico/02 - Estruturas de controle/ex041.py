from datetime import date

nascimento = int(input('Digite o ano de nascimento: '))
idade = date.today().year - nascimento
print(f'Ele tem {idade} anos.')
if idade <= 9:
    lugar = 'mirim'
elif idade <= 14:
    lugar = 'infantil'
elif idade <= 19:
    lugar = 'junior'
elif idade <= 25:
    lugar = 'sênior'
else:
    lugar = 'master'
print(f'Logo ele pertence a classe dos {lugar}.')
