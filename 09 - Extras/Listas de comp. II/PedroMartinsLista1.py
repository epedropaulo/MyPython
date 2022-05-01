def artilheiros():
    """Lê e armazena em uma matriz diversas informações nesta ordem:
    NomeDoJogador, Rodada, NGols
    parâmetro -> none
    output-> list"""
    
    jogadores = []  # Declaração da matriz onde os dados serão armazenados

    ValoresRodada = ["classificatoria", "oitavas", "quartas", "semi", "final"]
    # Possíveis valores para a rodada
    
    while True:
        NomeDoJogador = input('Digite o nome do jogador (Fim para sair): ').capitalize()
        if NomeDoJogador == 'Fim':
            return jogadores
        
        while True: # Loop para verificar se o input rodada está dentro das respostas aceitas
            print("Digite em qual rodada ele parou")
            rodada = input('(Valores aceitos: classificatoria, oitavas, quartas, semi e final): ').lower()
            if rodada in ValoresRodada:
                break
        
        NGols = int(input('Digite o número de gols: '))

        jogadores.append([NomeDoJogador, rodada, NGols])
