aluno = {'Nome': str(input('Nome: '))}
aluno['Media'] = float(input(f'Média de {aluno["Nome"]}: '))

if aluno['Media'] >= 7:
    aluno['Situação'] = 'aprovado'

elif aluno['Media'] >= 5:
    aluno['Situação'] = 'recuperação'

else:
    aluno['Situação'] = 'reprovado'
print('--' * 30)
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')
