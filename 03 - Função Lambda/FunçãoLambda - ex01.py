# def que multiplica um certo número por outro número desconhecido
def mult(a):
    return lambda x: a * x


# Definindo o primeiro número da multiplicação
double = mult(2)
triple = mult(3)
quadruple = mult(4)

# Definindo o segundo número da multiplicação e exibindo o resultado
print(double(15))
print(triple(15))
print(quadruple(15))
