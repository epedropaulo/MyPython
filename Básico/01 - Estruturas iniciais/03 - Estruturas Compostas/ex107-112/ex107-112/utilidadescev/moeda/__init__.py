def moeda(preco):
    return f'R${preco :.2f}'.replace('.', ',')


def metade(preco):
    a = preco / 2
    return moeda(a)


def dobro(preco):
    a = 2 * preco
    return moeda(a)


def aumentar(preco, b):
    a = (100 + b) * preco / 100
    return moeda(a)


def diminuir(preco, b):
    a = (100 - b) * preco / 100
    return moeda(a)


def resumo(preco, a, b):
    print(f'-' * 30)
    print(f'RESUMO DO VALOR'.center(30))
    print(f'-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço:  \t{dobro(preco)}')
    print(f'Metade do preço: \t{metade(preco)}')
    print(f'{a}% de aumento:  \t{aumentar(preco, a)}')
    print(f'{b}% de redução:  \t{diminuir(preco, b)}')
