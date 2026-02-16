print(not None != '')

# Linhas
linhas = int(input('\nLinhas: '))
for i in range(linhas + 1):
    # loop aninhado
    for j in range(i):
        # número de exibição
        print(i, end='')
    # nova linha após cada linha
    print('')
print()