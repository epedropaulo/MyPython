Listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.9,
            'Estojo', 25,
            'Transferidor', 4.2,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.3,
            'Livro', 34.9)
print('-' * 30)
print(f'{"LISTAGEM DE PREÇOS" :^30}')
print('-' * 30)
for c in range(0, len(Listagem), 2):
    print(f'{Listagem[c] :.<20}R${Listagem[c + 1] :>7.2f}')
print('-' * 30)
