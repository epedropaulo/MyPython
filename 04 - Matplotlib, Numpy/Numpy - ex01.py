# Exercício: Crie um array de inteiros de 32 bits de formato (3,2,5), onde todos os elementos são iguais a 3.
import numpy as np

x = np.ones((3,2,5), dtype='int32')
x = x * 3

print(x)