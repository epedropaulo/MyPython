arquivo = open("texto.txt", "w")
arquivo.write('Meu python.\n')

frutas = ['banana\n', 'pera\n', 'uva\n', 'maça']
arquivo.writelines(frutas)
arquivo.close()
