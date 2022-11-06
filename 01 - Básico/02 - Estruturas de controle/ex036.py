cores = ['\033[m', '\033[31m', '\033[34m']

print('')
print(f'{cores[1]}-=-' * 9)
print(f'{cores[2]}AVALIADOR DE EMPRÉSTIMOS!!!')
print(f'{cores[1]}-=-{cores[0]}' * 9)

casa = float(input('Digite o valor da casa que deseja comprar: R$'))
salario = float(input('Digite quanto é o seu salário: R$'))
meses = int(input('Digite em quantos meses deseja pagar:'))
prestacao = casa / meses
print('')

print(f'Sua prestacão é de R${prestacao :.2f} por mês.')
if prestacao > 0.3 * salario:
    print(f'Seu empréstimo {cores[1]}NÃO FOI{cores[0]} aprovado!')
else:
    print(f'Seu empréstimo {cores[2]}FOI{cores[0]} aprovado!')
