print('PA AUTÓMATICA!')
primeiro = int(input('O primeiro termo da PA: '))
razao = int(input('A razão da PA: '))
for c in range(0, 10):
    resto = primeiro + razao * c
    print(f'{resto}')
