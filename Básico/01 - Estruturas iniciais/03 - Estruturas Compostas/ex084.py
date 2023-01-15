Lista = []
cadastro = []
nomeMaior = []
nomeMenor = []
maior = menor = 0
while True:
    cadastro.append(str(input('Nome: ')).capitalize())
    cadastro.append(float(input('Peso [KG]: ')))
    Lista.append(cadastro[:])
    cadastro.clear()

    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Tente novamente! Deseja continuar [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break

for p in range(0, len(Lista)):
    if Lista[p][1] == maior:
        nomeMaior.append(Lista[p][0])
    elif Lista[p][1] > maior or p == 0:
        maior = Lista[p][1]
        nomeMaior.clear()
        nomeMaior.append(Lista[p][0])

    if Lista[p][1] == menor:
        nomeMenor.append(Lista[p][0])
    elif Lista[p][1] < menor or p == 0:
        menor = Lista[p][1]
        nomeMenor.clear()
        nomeMenor.append(Lista[p][0])
print('-=' * 30)
print(f'Foram cadastradas {len(Lista)} pessoas!')
print(f'Os mais leves eram: {nomeMenor}, e pesavam {menor} kgs.')
print(f'Os mais pesados eram: {nomeMaior}, e pesavam {maior} kgs.')
