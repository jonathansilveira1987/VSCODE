# Nessa módulo os dados são adicionados caso seja salvo na mesma lista.
elemento = int(input('\nInforme o número de elementos para a lista: '))
print()
conteudo = [input("Dado: ") for i in range(elemento)]
nome = input('\nNome da Lista: ')
with open(nome + '.txt', 'a') as arquivo:
    arquivo.write(f'Total de dados na lista = {len(conteudo)}') # Informa total de arquivos.
    arquivo.write('\n' + str(conteudo) + '\n')
print(f'\nArquivo salvo com o nome de \033[0;31m{nome}\033[m')

# Nessa módulo os dados são sobrescitos caso seja salvo na mesma lista.
elemento = int(input('\nInforme o número de elementos para a lista: '))
print()
conteudo = [input("Dado: ") for i in range(elemento)]
nome = input('\nNome da Lista: ')
with open(nome + '.txt', 'w') as arquivo:
    arquivo.write(f'Total de dados na lista = {len(conteudo)}') # Informa total de arquivos.
    arquivo.write('\n' + str(conteudo) + '\n')
print(f'\nArquivo salvo com o nome de \033[0;31m{nome}\033[m\n')