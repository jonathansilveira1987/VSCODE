# Caso já tenha uma lista com mesmo nome os dados anteriores são apagados do arquivo.
nome = input('\nNome do Arquivo: ')
elemento = int(input('\nInforme o número de elementos para a lista: '))
print()
c = 0
for i in range(c + 1):
    conteudo = [input(f'{i + 1}º dado: ') for i in range(elemento)]
    with open('lista.txt', 'w') as arquivo:
        arquivo.write("\n".join(conteudo))
        arquivo.write(f'\nTotal de dados salvos {len(conteudo)}') # Informa total de arquivos.
        arquivo.write('\n\n')
    print(f'\nArquivo salvo com o nome de {nome}\n')
    break

# Nesse caso se já tem uma lista com mesmo nome os dados são adicionados ao arquivo.
nome = input('\nNome do Arquivo: ')
elemento = int(input('\nInforme o número de elementos para a lista: '))
print()
c = 0
for i in range(c + 1):
    conteudo = [input(f'{i + 1}º dado: ') for i in range(elemento)]
    with open('lista.txt', 'a') as arquivo:
        arquivo.write("\n".join(conteudo))
        arquivo.write(f'\nTotal de dados salvos {len(conteudo)}') # Informa total de arquivos.
        arquivo.write('\n\n')
    print(f'\nArquivo salvo com o nome de {nome}\n')
    break

# ADICIONA MAIS DADOS EM UM MESMO ARQUIVO.
nome = input('\nNome do Arquivo: ')
elemento = int(input('\nInforme o número de elementos para a lista: '))
print()
c = 0
for i in range(c + 1):
    conteudo = [input(f'{i + 1}º dado: ') for i in range(elemento)]
    with open(nome + '.txt', 'a') as arquivo:
        arquivo.write('\n'.join(conteudo))
        arquivo.write(f'\nTotal de dados informados = {len(conteudo)}') # Informa total de arquivos.
        arquivo.write('\n\n')
    print(f'\nArquivo salvo com o nome de {nome}\n')
    break

# SUBSTITUI DADOS EXISTENTES EM UM MESMO ARQUIVO.
nome = input('\nNome do Arquivo: ')
elemento = int(input('\nInforme o número de elementos para a lista: '))
print()
conteudo = [input("Dado: ") for i in range(elemento)]
with open(nome + '.txt', 'w') as arquivo:
    arquivo.write("\n".join(conteudo))
    arquivo.write(f'\nTotal de dados informados = {len(conteudo)}') # Informa total de arquivos.
print(f'\nArquivo salvo com o nome de {nome}\n')

lista1 = int(input('\nQuantidade de valores na lista 1: '))
lista2 = int(input('\nQuantidade de valores na lista 2: '))

print('\033[32m')
for j in range (lista1 + 1):
    print(j)

print('\033[m \033[33m')
print(list(range(lista2 + 1)))
print('\033[m')








'''

with open('lista01.txt', 'w') as arquivo:
    arquivo.write(str(conteudo))




# conteudo = [1, 2, 3]
# Primeira solução.
elemento = int(input('\nInforme o número de elementos para a lista: '))
print()
conteudo = [input("Dado: ") for i in range(elemento)]
print(f'\n\033[0;32m{conteudo}\033[m')

'''