import pandas as pd


texto = open('1_user.dat', 'rb').read() # Abre o arquivo em bytes
texto_hex = bytearray(texto).hex()  # Transforma o arquivo em bytes em hexadecimais

picotado = texto_hex.split('0000000000010000')  # Retira parte do padrão, descoberto pelo Paulo.

def little(string):
    """Função que transforma o byte de little endian to big endian
    Str -> Str"""
    t= bytearray.fromhex(string)
    t.reverse()
    return ''.join(format(x,'02x') for x in t).upper()

nomes = []  # Observando o 'picotado', percebe-se que os nomes possuem no máximo 8 letras. (O que da 16 bytes)
            # E da forma como criei o picotado, esses nomes estão todos no final de cada elemento do picotado.
for binario in picotado[:-1]:
    nome1 = binario[-16:]
    nome2 = bytes.fromhex(nome1).decode('ASCII')    # Pega os hexadecimais dos nomes, joga pra bytes e de bytes joga pra ASCII
    nome2 = nome2.replace('\x00', '')   # Retira os espaços de bytes vazios da string
    nomes.append(nome2)
nomes = nomes[2:] # Exclui o caso das pontas que são problemáticos

numeros = []
for binario in picotado:
    num = int(little(binario[:4]), 16)  # Pega os big endian e transforma para int64
    numeros.append(num)
numeros = numeros[3:] # Exclui o caso das pontas que são problemáticos

finalmente = {'nomes': nomes, 'número': numeros}
dataframe = pd.DataFrame(finalmente)
dataframe.to_excel('dataframe.xlsx')
