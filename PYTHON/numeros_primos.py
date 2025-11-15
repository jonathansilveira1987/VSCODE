inicio = int(input('\nInforme o valor inicial: '))
fim = int(input('Informe o valor final: '))
numeros = range(inicio, fim + 1)
# print(f'\n{list(numeros)}\n')

def numeros_primos(numeros):
    for x in range(2, numeros):
        if (numeros%x) == 0:
            return False
    return True

primos = list(filter(numeros_primos, numeros))

print(f'\nSegue lista de números primos...')
print(f'\n{list(primos)}\n')