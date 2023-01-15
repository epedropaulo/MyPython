day = int(input('Quantos dias foi alugado? '))
km = float(input('Quantos km foi rodado? '))
cost = (day * 60) + (km * 0.15)
print(f'Com {day} dias alugados e {km :.2f}km rodados. \n'
      f'O custo ficou R${cost :.2f}')
