import math
num = int(input('Digite um número: '))
print(f'Analisando o número {num}...')
print(f'Unidade: {num // 1    % 10}\n'
      f'Dezena:  {num // 10   % 10} \n'
      f'Centena: {num // 100  % 10} \n'
      f'Milhar:  {num // 1000 % 10}')
