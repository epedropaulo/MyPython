def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos [aceita várias]
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a turma.
    """
    boletim = {'total': len(n), 'maior': max(n), 'menor': min(n)}
    media = sum(n) / len(n)
    boletim['média'] = media
    if sit:
        if media >= 7:
            boletim['situação'] = 'BOA'
        elif media >= 5:
            boletim['situação'] = 'RAZOÁVEL'
        else:
            boletim['situação'] = 'RUIM'
    return boletim


# Programa Principal
resp = notas(7.5, 8, 6.5, 2, 7, 4, sit=True)
print(resp)
