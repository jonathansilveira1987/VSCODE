from time import sleep
padrao = int(input('\nPadrão: '))
def imprimir_padrao(linhas):
    for i in range(linhas):
        for colunas in range(linhas-i):
            print('\033[0;35m ● \033[m', end='')
        print()
print()
imprimir_padrao(padrao)
print()