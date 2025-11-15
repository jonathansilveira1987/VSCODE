oco = int(input('\nDimensão do Quadrado Oco: '))
def quadrado_oco(linhas):
    for i in range(linhas):
        if i == 0 or i == linhas - 1:
            print(" *" * linhas)
        else:
            print(" *" + " " * (linhas + (oco - 4)) + " *")
print('\033[0;32m')
quadrado_oco(oco)
print('\033[m')