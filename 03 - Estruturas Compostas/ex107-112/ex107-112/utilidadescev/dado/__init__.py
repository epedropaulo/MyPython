def leiaDinheiro(frase):
    x = input(frase).replace(',', '.').strip()
    while True:
        if x.isalpha() or x == '':
            print(f'ERROR! "{x}" não é um número!')
            print('Tente novamente!')
            print()
            x = input(frase)
        else:
            a = float(x)
            break
    return a
