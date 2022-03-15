nome = str(input('Digite a frase: ')).lower().strip()
x = nome.rfind('a')
print(f'Existem {nome.count("a")} As na sua frase.\n'
      f'O primeiro A é a {1 + nome.find("a")}º letra.\n'
      f'Aparece a última vez na {(1 + x) - nome.count(" ", 0, x)}º.')
