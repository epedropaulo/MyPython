import matplotlib.pyplot as plt

# Definindo as variáveis.
x = [0, 50, 100]
y = [0, 50, 100]

# Fazendo a linha do gráfico.
plt.plot(x, y, linewidth=1, linestyle='-', color='red', marker='*', label='f(x) = x')

# Dando título ao gráfico
plt.title('Representação f(x) = x')
plt.xlabel('X')
plt.ylabel('F(X)')

# Adicionando legendas
plt.legend()

# Exibindo o gráfico
plt.show()
