extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
cont = 'S'
while cont in 'S':
    num = int(input('Digite um número entre 0 e 20: '))
    while not 0 <= num <= 20:
        num = int(input('Tente novamente! Digite um número entre 0 e 20: '))
    print(f'O número escolhido é o {num} e o seu extenso é {extenso[num]}')
    cont = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while cont not in 'SN':
        cont = str(input('Tente novamente. Deseja continuar? [S/N] ')).upper().strip()[0]
