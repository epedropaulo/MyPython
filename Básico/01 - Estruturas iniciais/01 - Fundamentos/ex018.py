import math
rad = math.radians(float(input('Digite um ângulo em graus: ')))
sin = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print(f'Este é o seno: {sin :.3f}. \n'
      f'Este é o cosseno: {cos :.3f}. \n'
      f'Essa é a tangente: {tan :.3f}.')
