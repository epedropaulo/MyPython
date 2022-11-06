from random import randint


class Criptografia:
    """Classe que possui como único atributo o conjunto dos caracteres que podem ser criptografados.
    A função da classe é exatamente a de criptografar e descriptografar certos arquivos usando a cifra de César."""
    def __init__(self):
        self.caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ#$&*@().:,!?[]=+-%abcdefghijklmnopqrstuvwxyz'
        
    def criptografar(self, letra, chave):
        """Recebe uma Letra qualquer, e uma chave. Com base nessa chave, retorna o valor criptografado da letra dada.
        str, int -> str"""

        if letra not in self.caracteres:
            return letra
            
        indiceLetra = self.caracteres.index(letra)  # Indice da letra dada na tabela.

        indiceCriptografado = (indiceLetra + chave) % len(self.caracteres)  # O resultado é o índice da letra criptografada.
        
        return self.caracteres[indiceCriptografado]
    
    def descriptografar(self, letra, chave):
        """Recebe uma letra criptografada, e uma chave. Com base nessa chave, retorna o valor descriptografado da letra.
        str, int -> str"""
        if letra not in self.caracteres:
            return letra
            
        indiceLetra = self.caracteres.index(letra)  # Indice da letra dada na tabela.

        indiceDescriptografado = (indiceLetra - chave) % len(self.caracteres)   # O resultado é o índice da letra descriptografada.
        
        return self.caracteres[indiceDescriptografado]
    
    def arqCriptografar(self, nomeArquivo='', chave=0):
        """Recebe o nome de um arquivo (por padrão é vazio), e recebe uma chave(por padrão é 0).
        O método verificará se é possível abrir o arquivo e se ele existe. Caso não haja problema. Um outro arquivo
        será criado com o mesmo conteúdo, mas agora criptografado."""
        while True:
            if -69 < chave < 69 and chave != 0:
                break
            
            chave = randint(-69, 69)
        
        if nomeArquivo == '':
            nomeArquivo = input('Digite o nome do arquivo: ')

        try:
            arq = open(nomeArquivo)
            
            nomeArqCripto = nomeArquivo[0:-4] + 'Cripto.txt'
            arqCripto = open(nomeArqCripto, mode='w')

            for i in arq.read():
                letra = self.criptografar(i, chave)
                arqCripto.write(letra)

            arq.close()
            arqCripto.close()
            
            return chave

        except FileNotFoundError:
            print('Arquivo não encontrado!')

        except PermissionError:
            print('Não tem permissão para modificar o arquivo!')

    def arqDescriptografar(self, nomeArquivo, chave):
        """Recebe o nome de um arquivo criptografado, e recebe uma chave.
        O método verificará se é possível abrir o arquivo e se ele existe. Caso não haja problema. Um outro arquivo
        será criado com o mesmo conteúdo, mas agora descriptografado."""
        try:
            arq = open(nomeArquivo)
            
            nomeArqDescripto = nomeArquivo[0:-4] + 'Descripto.txt'
            arqDescripto = open(nomeArqDescripto, mode='w')

            for i in arq.read():
                letra = self.descriptografar(i, chave)
                arqDescripto.write(letra)

            arq.close()
            arqDescripto.close()

        except FileNotFoundError:
            print('Arquivo não encontrado!')
        
        except PermissionError:
            print('Não tem permissão para modificar o arquivo!')