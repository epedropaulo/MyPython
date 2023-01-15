registro = []
pessoa = []
notas = []
while True:
    nome = str(input('Nome: ')).capitalize().strip()
    pessoa.append(nome)

    n1 = float(input('Nota 1: '))
    notas.append(n1)

    n2 = float(input('Nota 2: '))
    notas.append(n2)

    pessoa.append(notas[:])
    notas.clear()

    media = (n1 + n2) / 2
    pessoa.append(media)

    registro.append(pessoa[:])
    pessoa.clear()

    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Tente novamente! Deseja continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print('-=' * 30)
print('No. NOME       MÉDIA')
print('--' * 15)
for c in range(0, len(registro)):
    print(f'{c}   {registro[c][0] :<12} {registro[c][2] :.1f}')
print('--' * 15)
while True:
    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if aluno == 999:
        break
    print(f'Notas de {registro[aluno][0]} são {registro[aluno][1]}')
    print('--' * 15)
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
