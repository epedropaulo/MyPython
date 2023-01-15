"""Está faltando a parte da rodada final, mas por descuido meu acabei não conseguindo realiza-la a tempo,
e peço que o senhor avalie de forma justa e que achar melhor, me empenhei ao máximo e me exigiu algumas pesquisas,
mas acho que a parte mais complexa foi feita. A parte da rodada final seria só mais um detalhe dentro do que já foi
apresentado, mas estou exausto para continuar e sem tempo.
Atenciosamente: Pedro Paulo Dantas Silva Martins
"""

from random import *
from base_de_dados import *


def TemaEscolhido():
    """Escolhe um tema.
    none-> str"""
    temas = list(base_de_dados)  # Transforma apenas as keys da base de dados em uma lista.

    temaescolhido = temas[randint(0, len(temas) - 1)]  # Pega a quantidade de keys e sorteia uma.

    return temaescolhido


def SorteiaPalavra(tema):
    """Faz o sorteio de quais palavras deve ser adivinhadas;
    none -> list"""

    palavras = sample(base_de_dados[tema], 3)  # Sorteia 3 palavras dentro do tema, e retorna uma lista.

    return palavras


def Roleta():
    """Faz a parte da roleta. possibilidades: 100 a 950, de 50 em 50. dois 1000; duas 'passa a vez';
    duas 'perdeu tudo', os resultados são equiprováveis;
    perdeu tudo == 0
    passa a vez == 1
    none -> int"""

    possibilidades = [0, 0, 1, 1, 1000, 1000]

    for i in range(100, 951, 50):  # Adiciona os 100 a 950 na lista de possibilidade.
        possibilidades.append(i)

    numero = choice(possibilidades)  # Sorteia uma possibilidade.
    return numero


def Divisoria():
    """Faz a divisóra do display.
    none -> display"""

    print('+' + '=' * 50 + '+')


def Centralizar(frase):
    """Centraliza uma certa string em 50 espaços.
    string -> string"""

    print(f'|{frase:^50}|')


def Ativo(turno):
    """Decide de quem é o turno.
    int -> string"""

    if turno == 1:
        return 'Ana'

    if turno == 2:
        return 'Barbara'

    if turno == 3:
        return 'Carlos'


def Display(rodada, turno, roleta, tema, a=0, b=0, c=0):
    """Função que faz o trabalho do display.
    Recebe a rodada, o turno, o valor da roleta
    e a quantidade de pontos de Ana, Barbara e Carlos.
    int, int,int, int, int, int -> display"""

    Divisoria()
    rodaroda = 'RODA-RODA'
    Centralizar(rodaroda)

    Divisoria()
    partedasrodadas = f' RODADA {rodada} --- TURNO {turno}'
    Centralizar(partedasrodadas)

    Divisoria()
    partedosnomes = f'ANA - {a}  | BARBARA - {b} |  CARLOS - {c}'
    Centralizar(partedosnomes)

    Divisoria()
    partedojogadorativo = f'JOGADOR ATIVO: {Ativo(turno)}  |  VALOR DA ROLETA: {roleta}'
    Centralizar(partedojogadorativo)

    Divisoria()
    partedotema = f'Tema: {tema}'
    Centralizar(partedotema)

    Divisoria()


def Resposta(tentativas, frase):
    """Def que cuida de substituir o input para a resposta, e analisa a entrada dala pelo user.
    list, str -> str"""

    resposta = input(frase)

    while True:
        x = 0   # Variável é zero. quando passa por uma barreira de verificação, o valor.

        while not resposta.isalpha():  # Verifica se o input faz parte do alfabeto.
            print('\nDIGITE UMA LETRA VÁLIDA!')
            resposta = input('Digite a letra desejada: ')
            x += 1

        while len(resposta) != 1:  # Verifica se foi digitado duas letras ao mesmo tempo.
            print('\nDIGITE APENAS UMA LETRA!')
            resposta = input('Digite a letra desejada: ')
            x += 1

        while resposta in tentativas:
            print('\nDIGITE UMA LETRA QUE NÃO FOI AINDA.')
            resposta = input('Digite a letra desejada: ')
            x += 1

        if x == 0:
            break

    return resposta.lower().strip()


def SimNao(frase):
    """Def que cuida do input se deseja acertar as 3 palavras, analisando-o.
    str -> str"""
    continua = input(frase).lower()
    while not 's' and 'n' in continua:
        continua = input('Digite uma opção válida: ')
    return continua.lower()


def AcertaPalavra(palavras, frase):
    """Def que verifica se acertou as 3 tentativas de palavras.
    list -> bool"""

    tent = [input('DIGITE A PRIMEIRA PALAVRA CORRETAMENTE: ').lower(),
            input('DIGITE A SEGUNDA PALAVRA CORRETAMENTE: ').lower(),
            input('DIGITE A TERCEIRA PALAVRA CORRETAMENTE: ').lower()]
    if tent == palavras:
        return True
    else:
        return False


tentativas = []  # Registra todas as respostas obtidas.

lcertos = []  # Registra letras certas, com repetição, com o intuito de ver quantas faltam.

tema = TemaEscolhido()  # Escolhe o tema em um escopo global e que não varia.

palavras = SorteiaPalavra(tema)  # Escolhe as palavras em um escopo global e que não varia.

pontos = {'Ana': 0, 'Barbara': 0, 'Carlos': 0}  # Variaveis iniciais aos pontos.

rodada = turno = 1  # Variaveis iniciais das rodadas e turnos.

nletras = nacertos = len(palavras[0]) + len(palavras[1]) + len(palavras[2])  # Quantidade de letras certas, com repetição.

while rodada != 4 and nacertos != 0:  # Looping principal que cuida do jogo.

    valordaroleta = Roleta()  # Define o valor da roleta neste turno.

    Display(rodada, turno, valordaroleta, tema, pontos['Ana'], pontos['Barbara'], pontos['Carlos'])
    # Faz o display do cabeçalho

    for i in range(0, len(palavras)):  # Faz uma comparação uma a uma das letras numa forma de matriz.

        for j in palavras[i]:

            if j in tentativas:
                print(f'{j}', end='')
            else:
                print(f'_', end='')

        print('\n')

    print('Letras que já foram:', end=' ')  # Faz a parte de mostrar as letras que já foram.
    for i in tentativas:
        print(i, end=' ')

    if valordaroleta == 0:
        print('\nVOCÊ PERDEU TUDO E A SUA VEZ!!.')  # Analisa se a roleta o fez perder todos os pontos
        pontos[Ativo(turno)] = 0
        turno += 1

    elif valordaroleta == 1:
        print('\nVOCÊ PERDEU A SUA VEZ.')  # Analisa se a roleta o fez perder só a vez.
        turno += 1

    else:

        acertopalavra = 0  # Variavel que controla o acerto de palavras

        if nacertos <= 3:  # Verifica a quantidade de letras sobrando e se for menor ou igual a 3 oferece a opção de
            # acertar as palavras

            tentar = SimNao('\nDeseja tentar acertar as palavras?(sim/nao) ')

            if 's' in tentar:
                tentarpalavras = AcertaPalavra(palavras, 'Digite as palavras que você acha que é: ')
                if tentarpalavras:
                    print('\nVocê Acertou as palavras e ganhou 2000 pontos bônus!')
                    pontos[Ativo(turno)] += 2000

                    break
                else:
                    print('\nVocê errou as palavras e perdeu sua vez.')
                    turno += 1
                    acertopalavra += 1

        if acertopalavra == 0:
            resposta = Resposta(tentativas, '\nLetra Desejada: ')

            testeseacertou = 0  # Variável que analisa se acertou ou não e quantas vezes acertou de uma vez.

            for i in range(0, len(palavras)):  # Faz uma comparação uma a uma das letras numa forma de matriz.

                for j in palavras[i]:

                    if j == resposta:  # Caso a resposta esteja certa não passa o turno.
                        testeseacertou += 1
                        lcertos.append(j)

            if testeseacertou == 0:
                turno += 1  # Calibra o turno, caso a resposta esteja errada
                print('\nVocê não acertou nenhuma letra.')
            else:
                pontos[Ativo(turno)] += valordaroleta
                nacertos = nletras - len(lcertos)  # Número de acertos, restantes. se for igual a zero não continuara o loop
                print('\nVocê acertou a letra.')

            tentativas.append(resposta)  # Adiciona a resposta a lista de letras que já tentaram.

    if turno == 4:
        turno = 1
        rodada += 1

    continuar = input('press enter to continue.')

    print('\n' * 30)

listaponto = [pontos['Ana'], pontos['Barbara'], pontos['Carlos']]

ganhador = Ativo(listaponto.index(max(listaponto)) + 1)

for i in range(1, 4):
    print(f'A {i} palavra era {palavras[i - 1]}')

print(f'Parabéns o/a {ganhador} ganhou a competição!')
