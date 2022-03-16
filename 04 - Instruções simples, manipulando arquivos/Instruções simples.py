"""Esse arquivo consiste na demonstração do conhecimento sobre as expressões:
    assert, pass, del, raise, global, nonlocal."""


# Assert
def assert_teste():
    def limite_caracteres(cpf):
        assert (len(cpf) == 11), 'Número com a quantidade errada.'

        return 'aceito'

    print(limite_caracteres('12345678910'))
    print(limite_caracteres('123412'))


# Pass
def pass_teste():
    for letra in 'Github':
        if letra == 'u':
            pass
            print('bloco usando o Pass.')
        print(f'Letra atual: {letra}')


# Del
def del_teste():
    frutas = ['melao', 'banana', 'uva']
    del frutas[2]
    print(frutas)


# Raise
def raise_teste():
    def verificacao_tipo(entrada):
        if not type(entrada) is str:
            raise TypeError('Digite uma string.')

        return print(entrada)

    verificacao_tipo('Melancia')
    verificacao_tipo(10)


# Nonlocal
def nonlocal_teste():
    y = 'Batata'

    def mudar():
        nonlocal y
        y = 'potato'
    mudar()
    print(y)


# Global
x = 'Batata'


def global_teste():
    def mudar():
        global x
        x = 'Abacate'
    mudar()
    print(x)
