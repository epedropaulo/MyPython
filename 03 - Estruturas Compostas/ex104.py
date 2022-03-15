def leiaint(frase):
    """
    -> Pede um número e só viabiliza quando o mesmo for numerico.
    :param frase: A pergunta a ser feita na hora de pedir o num
    :return: O valor numerico num
    """
    num = input(frase)
    while not num.isnumeric():
        print('\033[1;31m ERRO! digite um número inteiro válido.\033[m')
        num = input(frase)
    return num


# Programa principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
