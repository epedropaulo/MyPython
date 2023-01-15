while True:
    escolha = int(input('Digite qual exercício é pra ser testado (0 pra sair): '))
    if escolha in [0, 1, 2, 3]:
        break
    else:
        print('Digite uma opção válida.')

if escolha == 1:

    # EXERCÍCIO 1
    from time import sleep


    def mediaGOLS(jogador):
        """Dada uma matriz de jogadores adiciona a média de gols deles na lista dada.
        parâmetro -> jogador
        output -> jogador(agora com mais um elemento, sendo esse a média.)"""
        for i in range(len(jogador)):

            NumRodada = 3 + ValoresRodada.index(jogador[i][1])    # Descobrimos o índice da rodada, ainda em modo string, e somamos 3 ao índice.
            mGols = jogador[i][2] / NumRodada
            jogador[i].append(mGols)
        
        return jogador


    def artilheiros():
        """Lê e armazena em uma matriz diversas informações nesta ordem:
        NomeDoJogador, Rodada, NGols
        parâmetro -> none
        output-> list"""
        
        jogadores = []  # Declaração da matriz onde os dados serão armazenados

        # Possíveis valores para a rodada.
        global ValoresRodada    # Vendo que mais pra frente vou comparar esses valores pra poder dizer os números de jogos em cada rodada
        ValoresRodada = ["classificatoria", "oitavas", "quartas", "semi", "final"]  # Pensei em deixá-la global, ou declara-la na main. Porém ai a função artilheiros iria recebê-la.
        
        
        while True:
            NomeDoJogador = input('Digite o nome do jogador (Fim para sair): ').capitalize()
            if NomeDoJogador == 'Fim':
                return mediaGOLS(jogadores) # Aplicando aqui a função acima chamando a artilheiros ele automáticamente, fará a média.

            while True: # Loop para verificar se o input rodada está dentro das respostas aceitas
                print("Digite em qual rodada ele parou")
                rodada = input('(Valores aceitos: classificatoria, oitavas, quartas, semi e final): ').lower()
                if rodada in ValoresRodada:
                    break
            
            NGols = int(input('Digite o número de gols: '))
            print(f'Jogador computado.')
            jogadores.append([NomeDoJogador, rodada, NGols])

            sleep(2)


    def main():
        melhores = artilheiros()
        MediaOuro = 0

        for i in range(len(melhores)):
            if not melhores[i][1] == 'classificatoria': # IF para verificar se o jogador atuou apenas nas classificatórias.
                
                if melhores[i][3] > MediaOuro:
                    NomeOuro = melhores[i][0]
                    MediaOuro = melhores[i][3]
        print(f'O melhor jogador foi o {NomeOuro}, com uma média de gols de {MediaOuro :.2f}')

    main()

if escolha == 2:
    # EXERCÍCIO 2
    from random import randint, sample


    def SemRepeticao(valores):
        """Sorteará uma quantidade dada de números, tendo inicio e fim. Que não possua repetições.
        input -> inicio (valor inicial do intervalo de sorteio)
                fim (valor final do intervalo de sorteio)
                quantidade (quantidade de números sorteados)
        output -> lista (uma lista com números não repetidos sorteados)"""

        while True:
            
            num = randint(1, 60)

            if num not in valores:
                valores.append(num)

                return valores


    def FazCartela(nCartelas):
        """Definirá quais valores estão em cada cartela, e as armazenará em uma matriz.
        input-> nCartelas (Quantidade de cartelas)
        output -> matrizCartelas (Retorna a matriz com todos os valores de cada cartela)"""
        matrizCartelas = []
        
        for i in range(0, nCartelas):
            valoresCartela = sample(range(1, 61), 6)    # Usa a função sample para não repetir os números do valor da cartela
            matrizCartelas.append(sorted(valoresCartela))
        
        return matrizCartelas


    def EscolheCartela(nCartelas):
        """Faz o sorteio dos números e os compara. Se a interseção dos valores da cartela com o conjunto dos valores sorteados
        for igual aos próprios valores da cartela. Logo a cartela será premiada.
        input -> nCartelas (matriz com as cartelas)
        output -> A cartela sorteada"""
        conjuntoValores = []
        
        while True:
            conjuntoValores = SemRepeticao(conjuntoValores)
            
            for i in nCartelas:
                
                if set(i) == set(i).intersection(conjuntoValores):
                    print(f'Os números sorteados, na ordem, foram: {conjuntoValores}')
                    return i


    def main():
        numCartelas = int(input('Digite o número de cartelas participantes: '))
        
        matrizCartelas = FazCartela(numCartelas)    # Declara a matriz contendo todas as cartelas
        
        cartelaSorteada = EscolheCartela(matrizCartelas)    # Faz a seleção da cartela sorteada.

        linhaSorteada = matrizCartelas.index(cartelaSorteada) + 1   # Ve qual a linha da cartela sorteada

        print(f"E a cartela vencedora foi a com valores: {cartelaSorteada}\n"
            f"Sendo a cartela de número: {linhaSorteada}")


    main()

if escolha == 3:
    print('Fui fazer em cima da hora e não deu tempo.\U0001F622')

if escolha == 0:
    print('Finalizando o programa.')
