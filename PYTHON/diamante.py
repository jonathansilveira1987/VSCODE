diamante = int(input("\nDimensão do Diamante: "))
def print_diamante(linhas):
    for i in range(1, linhas + 1):
        print(" " * (linhas - i) + "*" * (2 * i - 1))
    for i in range(linhas - 1, 0, -1):
        print(" " * (linhas - i) + "*" * (2 * i -1))
print('\033[0;34m')
print_diamante(diamante)
print('\033[m')