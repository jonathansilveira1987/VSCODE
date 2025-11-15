# Criar arquivo TXT.
nome = input('\nNome do Arquivo: ')
arquivo = open(nome + '.txt', 'a')
file = input('\nDigite algo: ')
arquivo.write(file + '\n')
# Acrescentando texto ao arquivo criado, usando o modo de acesso 'a'
texto = input('\nDigite algo para acrescentar ao arquivo: ')
arquivo = open(nome + '.txt', 'a')
arquivo.write(texto + "\n")
print('\nOperação concluída no arquivo ' + arquivo.name + ' usando o modo de acesso ' + arquivo.mode)
arquivo.close()
print(f'\nConteúdo atual do arquivo {nome}: ')
print('\033[0;32m')
arquivo = open(nome + '.txt', 'r')
for linha in arquivo:
    linha = linha.rstrip()
    print (linha)
arquivo.close()
print('\033[m')