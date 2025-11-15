linhas = int(input('\nLinhas: '))
caractere = str(input('Caractere: '))
def imprimrir_padrao(linhas, caractere):
    for i in range(linhas):
        for colunas in range(linhas-i):
            print(caractere, end='')
        print()
print('\033[0;34m')
imprimrir_padrao(linhas, caractere)
print('\033[m')