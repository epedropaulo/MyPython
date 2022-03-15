def voto(ano):
    from datetime import datetime

    atual = datetime.today().year
    idade = atual - ano

    if idade >= 65:
        resp = 'VOTO OPCIONAL'
    elif idade >= 18:
        resp = 'VOTO OBRIGATÓRIO'
    elif idade >= 16:
        resp = 'VOTO OPCIONAL'
    else:
        resp = 'NÃO VOTA'
    return f'Com {idade} anos: {resp}'


# Programa Principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
