# input("Escreva seu nome: ")

# print('Olá Mundo')

# nome = input("Escreva seu nome: ")
# print('Seu nome é:', nome)

# print('Dia', 'Mês', 'Ano', sep='/')
# print('ontem', 'Hoje', 'Amanhã', sep='-')
# print("B", "n", "n", ".", sep='a')

# Exemplo com fim de linha sem nenhum caracter
# print('Vamos estudar Na ', end='')
# print('Python Academy')
# Exemplo com fim de linha igual à ->
# print('As rosas são', end=' -> ')
# print('Vermelhas')
# Exemplo com fim de linha igual à :
# print("Quantidade", end=': ')
# print(40)

with open('arquivo.txt', 'w') as arquivo:
    print("Meu nome e Argermiro Variante,", file=arquivo)
    print("Sou estudante de engenharia.", file=arquivo)