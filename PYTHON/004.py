import random

a = int(input('\nValor 1: '))
b = int(input('Valor 2: '))
c = int(input('Valor 3: '))

a = random.random()
print(f'\n{a}')

b = random.randint(1, 10)
print(f'\n{b}')

c = random.choice([a, b, c])
print(f'\n{c}\n')