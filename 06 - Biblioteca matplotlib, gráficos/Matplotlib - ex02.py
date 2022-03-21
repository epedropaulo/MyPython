import matplotlib.pyplot as plt


# Abrindo e lendo os dados do arquivo
arq = open('Matplotlib - ex02.txt')
x = eval(arq.readline())
y = eval(arq.readline())

# Criando as linhas do gráfico
plt.plot(x, y, linewidth='2', linestyle='-', color='blue', label='gráfico simples!')

# Adicionando legendas
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')

# Exibindo o gráfico
plt.show()
