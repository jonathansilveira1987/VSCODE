a = float(input('\nValor do plano: '))
b = 12
c = a / 30 # Valor diário
d = a * b # Total anual
print(f'\nO valor pago por dia será de R$ {c:.2f}')
print(f'\nO valor pago pelo plano em 1 ano será de R$ {d:.2f}.')
print(f'\nO valor pago pelo plano em 1 ano será de R$ {d:.2f}.')

('\033[0;31m')
contador = int(input('\nContar até? '))
for i in range(0, contador + 1):
    for j in range(i):
        if i ^ j == 0:
        # if i % j == 0:
            break
    else:
        print(i, end=" ")