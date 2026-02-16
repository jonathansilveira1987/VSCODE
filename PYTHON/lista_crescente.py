n = int(input('\nDigite a quantidade de valores: '))
valores = list()
print()
for c in range(1, n + 1):
    x = int(input(f'Digite o {c}º valor: '))
    while x in valores:
        print('\033[31mO valor já existe! Digite outro valor!\033[m')
        x = int(input(f'Digite o {c}º valor: '))
    valores.append(x)
print(f'\n\033[32mA lista gerada foi: {valores}\033[m')
valores.sort()
print(f'\033[33mLista do menor ao maior: {valores}\033[m\n')