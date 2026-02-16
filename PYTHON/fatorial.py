n = int(input('\nCalcular Fatorial de: '))
fatorial = 1
print('\033[34m')
while n > 1:
  fatorial *= n 
  n -= 1 
print(f'O Fatorial de {n} equivale a {fatorial}\033[m\n')