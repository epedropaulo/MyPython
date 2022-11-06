gasto = menorp = caro = 0

print('--' * 20)
print('           LOJA SUPER BARATÃO')
print('--' * 20)

while True:
    produto = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$'))

    if menorp > preco or gasto == 0:
        menorp = preco
        menor = produto
    if preco > 1000:
        caro += 1
    gasto += preco

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'{"FIM DO PROGRAMA" :-^40}')
print(f'O gasto total é de R${gasto :.2f}')
print(f'{menor} é o item de menor valor, de R${menorp :.2f}')
print(f'Há {caro} itens que valem mais de R$1000.00')
