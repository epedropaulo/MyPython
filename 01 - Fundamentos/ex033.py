from time import sleep

num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
num3 = float(input('Digite novamente: '))
print(f'Analisando os números: {num1 :.1f}, {num2 :.1f}, {num3 :.1f}.')
sleep(1.5)
if num1 >= num2 >= num3:
    menor = num3
    maior = num1
if num1 >= num3 >= num2:
    menor = num2
    maior = num1
if num2 >= num1 >= num3:
    menor = num3
    maior = num2
if num2 >= num3 >= num1:
    menor = num1
    maior = num2
if num3 >= num1 >= num2:
    menor = num2
    maior = num3
if num3 >= num2 >= num1:
    menor = num1
    maior = num3
print(f'O menor valor digitado foi: {menor}.\n'
      f'O maior valor digitado foi: {maior}.')
