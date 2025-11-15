from time import sleep

# Contador Infinito Automático Negativo.
n = int(input('\nInforme o valor para começar o contador infinito negativo: '))
print()
n = n + 1
while True:
    n = n -1
    sleep(0.2)
    print(f'\033[31m{n}\033[m')
    # break # Retirar para execução do loop.