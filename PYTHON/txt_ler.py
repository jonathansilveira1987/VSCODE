# Criar arquivo TXT.
nome = input('\nNome do Arquivo: ')
arquivo = open(nome + '.txt', 'a')
file = input('\nDigite algo: ')
arquivo.write(file + '\n')
print()
# Lendo o arquivo criado:
arquivo = open(nome + '.txt', 'r')
print(f'\nSegue conteúdo do arquivo {nome} criado...\n\033[0;33m')
for linha in arquivo:
    linha = linha.rstrip()
    print(linha)
arquivo.close()
print('\033[m')