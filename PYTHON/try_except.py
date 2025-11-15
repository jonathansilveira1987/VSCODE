indice = int(input('\nInsira o índice: '))
try:
    lista = [1, 2, 3, 4]
    print(lista)
except:
    print('Insira um índice válido!')

a = int(input('\nInsira A: '))
b = int(input('Insira B: '))
try:
    divisao = a / b
    print(f'\n{divisao}')
except ZeroDivisionError as err:
    print('\nInsira valores válidos.')
else:
    print('\nOs dois valores eram válidos.')
finally:
    print('\nO programa terminou.\n')