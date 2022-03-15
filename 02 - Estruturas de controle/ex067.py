print('')
print('Digite um número negativo para sair do loop!')
while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    if n < 0:
        break
    print('---' * 5)
    for c in range(1, 11):
        print(f'  {n} x {c} = {n * c}')
    print('---' * 5)
print('PROGRAMA TABUADA ENCERRADO!!')
