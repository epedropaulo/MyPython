import math

cateto1 = float(input('Digite o cateto: '))
cateto2 = float(input('Digite o outro cateto: '))
# hipotenusa = math.sqrt(cateto1**2+cateto2**2)
hipotenusa = math.hypot(cateto1, cateto2)
print(f'Com esses catetos, a hipotenusa é: {hipotenusa :.2f}  ')
