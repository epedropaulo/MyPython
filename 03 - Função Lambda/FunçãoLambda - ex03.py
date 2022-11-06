# Definindo a lista original
telefones = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
    ]
# Organizando a lista pelas cores em ordem alfabética usando a função lambda
telefones.sort(key=lambda x: x['color'])
print(telefones)
