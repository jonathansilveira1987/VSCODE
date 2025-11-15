# Par & Ímpar com Lista.
num = [[], []]
valor = 0
quantidade = int(input('\nInforme a quantidade de números da lista: '))
print()
for c in range(1, quantidade + 1):
    valor = int(input(f"Digite o {c}º valor: "))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print()
print("-=" * 40)
num[0].sort()
num[1].sort()
print(f"\nOs valores PARES digitados foram...")
print(f"\033[0;32m{num[0]}\033[m")
print(f"\nOs valores ÍMPARES digitados foram...")
print(f"\033[0;31m{num[1]}\033[m\n")