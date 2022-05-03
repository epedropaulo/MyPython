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
