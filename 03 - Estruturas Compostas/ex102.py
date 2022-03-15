def fatorial(fator, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param fator: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    print('-' * 40)
    f = 1
    for c in range(fator, 1, -1):
        f *= c
        if show:
            print(f'{c} x ', end='')
            if c == 2:
                print(f'1 = ', end='')
    return f


# Programa Principal
print(fatorial(7, True))
