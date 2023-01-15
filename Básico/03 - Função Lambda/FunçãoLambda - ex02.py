# Definindo a lista dada pelo exercício
subjects = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Usando a função lambda para organizar a lista pelo parâmetro de notas
subjects.sort(key=lambda x: x[1])
print(subjects)
