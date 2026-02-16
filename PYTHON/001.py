from time import sleep
i = 0
j = int(input('\nInforme um número inteiro: '))
print('\033[0;32m')
while i <= j:
    sleep(0.3)
    print(f'Número {i}')
    i = i + 1
print('\033[m')