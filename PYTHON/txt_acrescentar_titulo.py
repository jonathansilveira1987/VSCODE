# Criar arquivo TXT.
nome = input('\nNome do Arquivo: ')
arquivo = open(nome + '.txt', 'a')
print()
# Acrescentando título ao início do arquivo, usando o modo 'r+'
titulo = input('Digite um título para acrescentar ao arquivo: ')
arquivo = open(nome + '.txt', 'r+')
arquivo.seek(0)
arquivo.write(titulo + '\n' + '\n')
arquivo.close()
arquivo = open(nome + '.txt', 'a')
file = input('\nDigite algo: ')
arquivo.write(file + '\n')
print()