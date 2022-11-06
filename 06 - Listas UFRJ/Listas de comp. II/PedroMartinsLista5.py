class minhaCalculadora:
    def soma(x, y):
        try:    # Essa foi a maneira que eu vi para evitar problemas como, por exemplo se fosse duas strings e colocasse no try x + y poderia haver
                # A concatenação de strings, e assim apenas aqueles números que podem virar float serão somados. Como faz sem a repetição de código ?
            x = float(x)
            y = float(y)

            return x + y
        
        except TypeError and ValueError:
            print('Digite valores válidos.')
            
            return None


    def subtracao(x, y):
        try:
            x = float(x)
            y = float(y)

            return x - y

        except TypeError and ValueError:
            print('Digite valores válidos.')
            
            return None


    def multiplicacao(x, y):
        try:
            x = float(x)
            y = float(y)

            return x * y

        except TypeError and ValueError:
            print('Digite valores válidos.')
            
            return None
        

    def divisao(x, y):
        try:
            x = float(x)
            y = float(y)

            return x / y

        except TypeError and ValueError:
            print('Digite valores válidos.')
            
            return None

        except ZeroDivisionError:
            print('Ocorre a divisão por zero!')
            
            return None


def main():

    print('SOMA')
    print(minhaCalculadora.soma(1.3, 2))
    print(minhaCalculadora.soma(1, '1'))
    print(minhaCalculadora.soma(1, 'e'))
    print(minhaCalculadora.soma('d', 'b'))
    print('')

    print('SUBTRAÇÃO')
    print(minhaCalculadora.subtracao(1.3, 2))
    print(minhaCalculadora.subtracao(1, '1'))
    print(minhaCalculadora.subtracao('a', 'b'))
    print('')

    print('MULTIPLICAÇÃO')
    print(minhaCalculadora.multiplicacao(1.3, 2))
    print(minhaCalculadora.multiplicacao(1, '1'))
    print(minhaCalculadora.multiplicacao(1, 'e'))
    print(minhaCalculadora.multiplicacao('d', 'b'))
    print('')

    print('DIVISÃO')
    print(minhaCalculadora.divisao(1.3, 2))
    print(minhaCalculadora.divisao(1, '1'))
    print(minhaCalculadora.divisao(1, '0'))
    print(minhaCalculadora.divisao('d', 'b'))
    print('')


main()
