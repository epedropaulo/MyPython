def musica(nota):
    """Recebe uma string com notas e retorna sua frequência.
    str -> list"""
    if len(nota) % 2 != 0:
        print("Só é aceito strings com uma quantidade pares de caracteres")
        return None

    base = {"C":262, "D":294, "E":330, "F":349, "G":392, "A":440, "B":494}  # Base de referência
    hz = [] # Lista onde ficará armazenado as frequências que serão retornadas.

    for i in range(0, len(nota), 2):
        frequencia = base[nota[i].upper()]
        parte = int(nota[i+1])
        pronta = frequencia * 2**(parte-3)
        hz.append(pronta)

    return hz


def semRepeticao(frase):
    """Usando Set, recebe uma string e retorna a quantidade de elementos distintos.
    str -> int"""
    unicos = set(frase)

    return len(unicos)


def conjuntos(f, i, w):
    """Recebendo 3 sets com o nome de usuários de redes sociais, retorna uma tupla com alguns dados.
    set, set, set -> tuple"""
    total = 30

    redes = set(f | i | w)  # Com a união haveria sobreposição de elementos, mas o set não admite elementos repetidos.

    porcentagem = f'{len(redes) / total :.2f}'

    diferencaSimetrica = f ^ i

    semW = diferencaSimetrica - w

    return (redes, porcentagem, semW)


def equivalencia(civil, eletronica):
    """Recebendo duas listas com os códigos das disciplinas do curso, retorna certa informações.
    lst, lst -> tuple"""
    
    civil = set(civil)
    eletronica = set(eletronica)
    juncao = civil | eletronica
    intersecao = civil & eletronica

    porcentagem = f'{ (len(intersecao) / len(eletronica)) * 100 :.2f}'

    return (porcentagem, len(juncao))


def resistencia(faixa1, faixa2, faixa3):
    """Recebendo 3 strings, válidas, retorno um certo valor correspondente de resistência associado a um conjunto de cores.
    str, str, str -> int"""
    padrao = {'preto': 0, 'marrom': 1, 'vermelho': 2, 'laranja': 3, 'amarelo': 4,}

    if faixa1 and faixa2 and faixa3 not in padrao:
        print('Código não encontrado')
        return 0
    
    valor = (padrao[faixa1]*10 + padrao[faixa2]) * 10 ** padrao[faixa3]
    
    return valor
