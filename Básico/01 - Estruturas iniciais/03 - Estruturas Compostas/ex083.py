expressao = str(input('Digite a expressão: '))
p = expressao.count('(')
x = expressao.count(')')
if '()' in expressao:
    print('Sua expressão não está válida')
elif x == p:
    print('Sua expressão é válida!')
else:
    print('Sua expressão não está válida!')
