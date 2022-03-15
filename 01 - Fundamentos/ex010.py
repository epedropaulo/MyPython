din = float(input('Quanto você tem na carteira? R$'))
dol = float(input('Quanto está o dólar agora? US$'))
x = din/dol
print(f'Com R${din :.2f}, e o dólar a US${dol :.2f}, pode ser comprado {x :.2f} dólares')
