cont50 = cont20 = cont10 = cont1 = 0
print('===' * 10)
print(f'{"BANCO CEV" :^30}')
print('===' * 10)
num = int(input('Qual o valor a ser sacado: R$'))
while True:
    if num >= 50:
        num -= 50
        cont50 += 1
    elif num >= 20:
        num -= 20
        cont20 += 1
    elif num >= 10:
        num -= 10
        cont10 += 1
    elif num >= 1:
        num -= 1
        cont1 += 1
    elif num == 0:
        break
print('Serão impressas: ')
if cont50 > 0:
    print(f'    {cont50} notas de R$50. ')
if cont20 > 0:
    print(f'    {cont20} notas de R$20. ')
if cont10 > 0:
    print(f'    {cont10} notas de R$10. ')
if cont1 > 0:
    print(f'    {cont1} notas de R$1.')
print('')
