'''
nomes = [
    'Daniel',
    'Mike',
    'William'
]
'''

c = 0
for i in range(c + 1):
    elemento = int(input('\nInforme o número de nomes para a lista: '))
    print()
    nomes = [input(f'{i + 1}º nome: ') for i in range(elemento)]

# Compreensão de Lista
comprimento_lista = [len(nome) for nome in nomes]
print(f'\n\033[33mCompreensão de Lista = {comprimento_lista}\033[m\n')


# Compreensão de Dicionário
comprimento_dicionario = {nome:len(nome) for nome in nomes}
print(f'\033[34mCompreensão de Dicionário = {comprimento_dicionario}\033[m\n')