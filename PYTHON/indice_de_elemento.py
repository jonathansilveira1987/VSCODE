# Índice de elemento.
a = int(input('\nVetor A: '))
b = int(input('Vetor B: '))
print('\033[34m')
for indice, elemento in enumerate(range(a, b + 1)):
    print(indice, elemento)
print('\033[m')