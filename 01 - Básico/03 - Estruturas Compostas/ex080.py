valores = []
for c in range(0, 5):
    valor = int(input('Digite um valor: '))
    if c == 0 or valor > max(valores):
        valores.append(valor)
        print('Adicionado ao final da lista!')
    else:
        for d in range(0, len(valores)):
            if valor < valores[d]:
                pos = valores.index(valores[d])
                valores.insert(pos, valor)
                print(f'Foi adicionado à posição {pos}...')
                break
print(f'Os valores ordenados são: {valores}')
