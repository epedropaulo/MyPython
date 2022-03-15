cores = ['\033[m', '\033[31m', '\033[34m']
print(f'{cores[1]}-=-' * 7)
print(f'{cores[2]}FORMAS DE PAGAMENTO.')
print(f'{cores[1]}-=-{cores[0]}' * 7)
print('')
preco = float(input('Quanto é o produto? R$'))

print('')
print(f'Digite [{cores[2]} 1 {cores[0]}] para {cores[2]}sim{cores[0]}. \n'
      f'Digite [{cores[1]} 2 {cores[0]}] para {cores[1]}não{cores[0]}.')
parcela = int(input('Você vai parcelar? '))
print('')

if parcela == 2:
    print(f'Digite [{cores[2]} 1 {cores[0]}] para {cores[2]}DINHEIRO / CHEQUE{cores[0]}.\n'
          f'Digite [{cores[1]} 2 {cores[0]}] para {cores[1]}cartão{cores[0]}.')
    modo = int(input('Dinheiro/Cheque ou cartão: '))
    if modo == 1:
        preco1 = preco * 0.9
    else:
        preco1 = preco * 0.95
    print('')
    print(f'O preço em parcela única será de: R${preco1 :.2f}.')
elif parcela == 1:
    vezes = int(input('Quantas vezes vai parcelar? '))
    if vezes == 2:
        preco1 = preco / vezes
    else:
        preco1 = (preco * 1.2) / vezes
    print('')
    print(f'O preço em {vezes} parcelas, será de R${preco1 :.2f} por parcela, pagando R${preco * 1.2 :.2f}.')
else:
    print('OPÇÃO INVÁLIDA!')
