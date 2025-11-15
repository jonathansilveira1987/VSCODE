# Criar arquivo TXT.
nome = input('\nNome do Arquivo: ')
arquivo = open(nome + '.txt', 'a')
file = input('\nDigite algo: ')
arquivo.write(file + '\n')
print()
# Adicionar conteúdo.
print(f'Conteúdo adicionado: \033[0;35m{file}\033[m\n')
arquivo = open(nome + '.txt', 'r')
for linha in arquivo:
    linha = linha.rstrip()
    print(linha)
arquivo.close()
print()