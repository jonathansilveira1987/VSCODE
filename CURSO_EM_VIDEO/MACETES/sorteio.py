import random

dados1 = random.sample(range(10, 50), k=10)
dados2 = random.sample(range(10, 50), k=5)
dados3 = random.sample(range(10, 50), k=10)
dados4 = random.sample(range(10, 50), k=5)

print('\nSorteio 1 ->', dados1)
print('Sorteio 2 ->', dados2)
print('Sorteio 3 ->', dados3)
print(f'Sorteio 4 -> {dados4}\n')