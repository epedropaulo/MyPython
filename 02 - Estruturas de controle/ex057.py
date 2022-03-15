x = ''
while x != 'M' and x != 'F':
    x = str(input('Digite seu sexo [M/F]: ')).upper().strip()
    if x == 'M':
        print('Você foi registrado como MASCULINO!')
    elif x == 'F':
        print('Você foi registrado como FEMININO!')
    else:
        print('Digite um sexo VÁLIDO!!')
        print('')
