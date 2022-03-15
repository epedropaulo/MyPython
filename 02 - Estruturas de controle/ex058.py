from random import randint
from time import sleep

x = randint(0, 10)
resposta = -1
tentativas = 0

print('-=-' * 10)
print('      JOGO DE ADIVINHAÇÃO')
print('-=-' * 10)
print('')
print('Vamos ver se consegue me vencer...')
print('Pensando em um número entre 0 e 10...')
print('')
sleep(2)

while resposta != x:
    resposta = int(input('Digite a sua escolha: '))
    tentativas += 1
    if resposta != x:
        print('Hmmm tenta outra vez...')
        print('')
if tentativas == 1:
    print('CARAMBOLAS! Você acertou de primeira... Parabêns!')
elif tentativas <= 4:
    print(f'Conseguiu acertar na {tentativas}° tentativa... boa!')
else:
    print(f'Com {tentativas} tentativas fica fácil né...')
if tentativas == 10:
    print('MEU DEUS KKKKKKKKKKKKKKKKK ÚLTIMA TENTATIVA É FOGO VIU!')
