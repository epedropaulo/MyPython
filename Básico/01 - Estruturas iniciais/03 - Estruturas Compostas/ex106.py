from time import sleep

c = ['\033[m',         # 0 - sem cores
     '\033[0;30;41m',  # 1 - vermelho
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;43m',  # 3 - amarelo
     '\033[0;30;44m',  # 4 - azul
     '\033[0;30;45m'   # 5 - roxo
     ]


def mostrar(msg, cor=0):
    """
    -> Uma variação do print para que tenha uma estética melhor.
    :param msg: Parametro a ser exibido.
    :param cor: Cor a ser exibida.
    :return: no return
    """
    print(c[cor], end='')
    print('~' * (len(msg) + 4))
    print('  ' + msg)
    print('~' * (len(msg) + 4))
    print(c[0], end='')


def ajuda(com):
    """
    -> Mostra a ajuda interativa do python.
    :param com: O comando a ser usado no help
    :return: no return
    """
    mostrar(f"Acessando a manual do comando '{com}'", 4)
    sleep(1)
    print(c[5])
    help(com)
    print(c[0])
    sleep(1)


# Programa Principal
while True:
    print('')
    mostrar('SISTEMA DE AJUDA PyHelp', 1)
    sleep(1)
    comando = str(input('Função ou biblioteca -> ')).strip()
    if comando in 'Fimfim':
        break
    ajuda(comando)
mostrar('ATÉ LOGO', 2)
