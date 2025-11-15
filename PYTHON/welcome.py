from datetime import datetime

data_atual = datetime.now()
print(data_atual.date())


elemento = int(input('\nInforme o número de elementos para a lista: '))
print()
conteudo = [input("Dado: ") for i in range(elemento)]
# numeros = [21, 5, 34, 8, 16, 7, 3]
soma_pares = sum(map(lambda n: n if n % 2 == 0 else 0, conteudo))
soma_impares = sum(map(lambda n: n if n % 2 != 0 else 0, conteudo))
print(f'A soma dos valores pares é {soma_pares} e dos ímpares é {soma_impares}')