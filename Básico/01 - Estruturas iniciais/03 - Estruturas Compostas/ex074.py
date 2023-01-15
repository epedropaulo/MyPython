from random import randint
num = (randint(0, 10), randint(0, 10), randint(0, 10),
       randint(0, 10), randint(0, 10))
print('A lista sortida foi: ', end='')
for c in num:
    print(f'{c} ', end='')
print(f'\nO maior é {max(num)}, o menor é {min(num)}.')
