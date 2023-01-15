from datetime import date
registro = dict()

registro['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
registro['idade'] = date.today().year - ano
registro['ctps'] = int(input('Carteira de trabalho [0 não tem]: '))

if registro['ctps'] != 0:
    registro['contratação'] = int(input('Ano de contratação: '))
    registro['salário'] = float(input('Salário: '))
    registro['aposentadoria'] = (registro['contratação'] + 35) - ano

print('-=' * 30)
for k, v in registro.items():
    print(f'  - {k} tem o valor {v}')
