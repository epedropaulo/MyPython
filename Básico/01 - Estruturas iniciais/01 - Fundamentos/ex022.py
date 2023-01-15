nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...\n'
      f'Seu nome em maiúsculo é {nome.upper()}.\n'
      f'Seu nome em minúsculo é {nome.lower()}.\n'
      f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras.\n'
      f'Seu primeiro nome é {nome.split()[0].capitalize()} e ele tem {len(nome.split()[0])} letras.')
