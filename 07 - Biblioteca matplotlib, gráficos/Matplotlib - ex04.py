import matplotlib.pyplot as plt

# Definindo as varáveis
arq = open('Matplotlib - ex04.txt')
dados = [[], [], [], [], []]

# Usando um loop para extrair os dados da coluna da matriz.
for i in arq.readlines():
    x = eval(i)
    for k in range(0, len(x)):
        dados[k].append(x[k])

x = dados[0]
y1 = dados[1]
y2 = dados[2]
y3 = dados[3]
y4 = dados[4]

# Desenhando o gráfico
plt.plot(x, y1, linewidth='1', color='blue', label='open')
plt.plot(x, y2, linewidth='1', color='orange', label='High')
plt.plot(x, y3, linewidth='1', color='green', label='Low')
plt.plot(x, y4, linewidth='1', color='red', label='Close')

# Aplicando legendas
plt.legend()
plt.xlabel('Oct-2016')

# Mostrando o gráfico feito
plt.show()
