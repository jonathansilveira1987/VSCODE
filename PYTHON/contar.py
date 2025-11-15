from time import sleep

titulo = str(input('\nDefina um título: '))
sleep(0.5)
print(f'\n\033[32m{titulo:•^50}\033[m') # Centralizado.
sleep(0.5)
print(f'\n\033[33m{titulo:.>50}\033[m') # Direita.
sleep(0.5)
print(f'\n\033[34m{titulo:_<50}\033[m') # Esquerda.

# Contador Manual.
n = int(input('\nAté quanto você deseja contar: '))
print('\033[32m')
for i in range(n + 1):
    sleep(0.3)
    print(i)
print('\033[m')

# Contador com Ponto Incial & Final.
a = int(input('Ponto Inicial: '))
b = int(input('Ponto Final: '))
print('\033[33m')
c = range(a, b + 1)
for d in c:
    sleep(0.3)
    print(d)
print('\033[m')

# Contador Infinito.
x = -1
while True:
    x > 0
    x = x + 1
    sleep(0.3)
    print(f'\033[31m{x}\033[m')