import matplotlib.pyplot as plt

# Definindo variáveis
x = [1, 3, 5]
y = [2, 6, 10]

# Criando um gráfico e atribuindo etiquetas
plt.plot(x, y, linewidth=2, linestyle='--', marker='o', label='f(x) = 2x', color='black')
plt.plot(y, x, linewidth=2, linestyle=':', marker='D', label='f(x) = x/2', color='red')

# Atribuindo um título ao gráfico
plt.title('Primeiro exemplo utilizando Plot')
plt.xlabel('Função 2')
plt.ylabel('Função 1')

# Aplicando legenda
plt.legend()

# Exibindo o gráfico gerado
plt.show()
