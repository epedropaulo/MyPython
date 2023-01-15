frase = str(input('Digite uma frase: ')).upper().split()
string1 = ''.join(frase)
string2 = ''
for c in range(len(string1) - 1, -1, -1):
    string2 += string1[c]
print(f'O inverso de {string1} é {string2}')
if string1 == string2:
    print('E por isso ele é um palíndromo.')
else:
    print('E por isso ele não é um palíndromo.')
