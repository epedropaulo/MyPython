# Faça duas funções, linha e coluna, cada uma recebendo como parâmetro de entrada um array M
# e um número inteiro i. O formato (n, m) do array M não é passado como parâmetro de
# entrada. As funções devem retornar, respectivamente, a linha e a coluna i de M. Se M não
# possui linha (coluna) i, a mensagem 'Nao existe esta linha (coluna)' deve ser retornada.
# Caso M não tenha o formato (n, m), a mensagem 'Isto nao é uma matriz.' deve ser retornada.
import numpy as np

def linha(M, i):
    if len(M.shape) > 2:
        return 'Isso não é uma matriz!'

    if M.shape[0] < i:
        return f'A matriz não possui a linha {i}'
    
    return M[i, :]


def coluna(M, i):
    if len(M.shape) > 2:
        return 'Isso não é uma matriz!'

    if M.shape[1] < i:
        return f'A matriz não possui a coluna {i}'
    
    return M[:, i]