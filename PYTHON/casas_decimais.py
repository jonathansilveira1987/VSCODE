a = float(input('\nNúmero/Base: '))
b = float(input('Potência/Expoente: '))

resultado1 = a ** b

print(f'\n{int(resultado1)}')
print(f'\n\033[32m{resultado1:.2f}\033[m')
print(f'\033[33m{resultado1:.4f}\033[m')
print(f'\033[34m{resultado1:.6f}\033[m')
print(f'\033[35m{resultado1:.8f}\033[m\n')