import numpy as np
import matplotlib.pyplot as plt


def sample():
    """Criará o gráfico exemplo da questão 1.
    none -> none"""
    fig, ax = plt.subplots()

    x = np.array((1, 2, 3))
    y = np.array((2, 4, 1))

    ax.plot(x, y, 'b-', linewidth=1)

    plt.xlabel('X - axis')
    plt.ylabel('Y - axis')

    ax.set_title('Sample graph!')
    ax.set_yticks(np.arange(1, 4.1, 0.5))
    ax.set_xticks(np.arange(1, 3.1, 0.5))

    ax.margins(0)   # Procurar esse comando para deixar sem margens foi interessante.

    ax.legend()
    plt.show()


def dates():
    """Pegará os dados do exemplo e criará um gráfico assim como o pedido.
    none -> none"""

    matriz = np.array(( # Cada coluna representa uma informação, na coluna 0 há o eixo X e nas outras colunas estão os Y. [date, open, high, low, close]
    [3, 774.25,     776.065002, 769.5,      772.559998],
    [4, 776.030029, 778.710022, 772.890015, 776.429993],
    [5, 779.309998, 782.070007, 775.650024, 776.469971],
    [6, 779,        780.47998,  775.539978, 776.859985],
    [7, 779.659973, 779.659973, 770.75,     775.080017]
    ))

    fig, ax = plt.subplots()

    x = matriz[:, 0]

    y1 = matriz[:, 1]
    y2 = matriz[:, 2]
    y3 = matriz[:, 3]
    y4 = matriz[:, 4]

    ax.plot(x, y1,           label ='Open')
    ax.plot(x, y2, 'orange', label = 'High')
    ax.plot(x, y3, 'g',      label = 'Low')
    ax.plot(x, y4, 'r',      label = 'Close')

    plt.xlabel('Oct 2016', loc='left')
    plt.xticks((3, 4, 5, 6, 7), ('03', '04', '05', '06', '07')) # Comando para colocar o label no formato desejado

    ax.legend()
    plt.show()


def line():
    """Fará uma linha do ponto (0,0) até o ponto (50, 150)
    none -> none"""
    fig, ax = plt.subplots()

    x = (0, 50)
    y = (0, 150)

    ax.plot(x, y)
    ax.set_title('Draw a line')

    plt.xlabel('x - axis')
    plt.ylabel('y - axis')

    ax.set_xticks(range(0, 101, 20))
    ax.set_yticks(range(0, 201, 50))
    
    plt.legend()
    plt.show()


def last():
    """Desenha o gráfico representado no último exercício.
    none -> none"""

    fig, ax = plt.subplots()
    
    x = np.array([1, 4, 5, 6, 7])
    y = np.array([2, 6, 3, 6, 3])

    ax.plot(x, y, '-.r')
    ax.plot(x, y, 'bo')

    ax.set_xticks(range(1, 9, 1))
    ax.set_yticks(range(1, 9, 1))

    ax.set_title('Display Marker')
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')

    plt.legend()
    plt.show()
