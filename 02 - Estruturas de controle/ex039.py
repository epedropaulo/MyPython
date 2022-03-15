from datetime import date
nascimento = int(input('Digite o ano em que você nasceu: '))
idade = date.today().year - nascimento

if idade == 18:
    print('Esse é o seu ano de se alistar em meu rapaz!')
elif idade > 18:
    print('Já passou da hora de você se alistar em!!!')
    x = idade - 18
    print(f'Já passou de {x} ano(s) do alistamento.')
else:
    x = 18 - idade
    print(f'Ainda falta {x} ano(s) para você se alistar!')
