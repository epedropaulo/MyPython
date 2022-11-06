"""Aqui se encontrará a relação entre todas as classes, métodos e atributos usados para fazer o
jogo rodar e funcionar perfeitamente.

O jogo será o 2048. seguindo o modelo: https://play2048.co"""
try:
    import numpy as np
    import pandas as pd

    from estatistica import *
    from mecanica import *
    from interface import *
    from arquivos import *
except ModuleNotFoundError or ImportError:
    print('MÓDULOS NÃO ENCONTRADOS')


menu = Menu()
while True:
    tecla = 0
    while True:
        print(menu)
        
        tecla = menu.entrada()

        if tecla == 'enter': break
        
        menu.selecao(tecla)

    opcao = menu.detecta()

    if opcao == 'Novo Jogo' or opcao == 'Carregar':
        
        matriz = MatrizTela()

        if opcao == 'Carregar':
            matriz.blocos, matriz.jogadas = Arquivos.leitura_carregar_save()

        while True:
            Arquivos.salvar(matriz.blocos, matriz.jogadas)

            print(matriz)
            lado = menu.entrada()   # Pede a jogada

            menu.tela_pause(lado)   # Verifica se foi feito o pause

            matriz.jogada(lado)     # Executa a jogada

            matriz.junta(lado)      # Junta os blocos
            
            if Mecanica.ganhou(matriz.blocos):  # Verifica se ganhou logo depois de juntar
                situacao = 'ganhou'
                break

            matriz.gera()            # Gera um novo bloco

            if Mecanica.perdeu(matriz.blocos):  # Verifica se é possível fazer alguma jogada, logo depois de gerar.
                situacao = 'perdeu'
                break

        menu.tela_pos_partida(situacao)

    if opcao == 'Estatística':
        matriz, jogadas = Arquivos.leitura_carregar_save()
        Estatistica.plotar(jogadas)

    if opcao == 'Sair':
        break
