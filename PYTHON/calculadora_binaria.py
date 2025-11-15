binario = int(input('\nDigite o número (binário) para ser convertido para base decimal: '))
n = len(str(binario))
valor_digitado = binario
decimal = 0
i = 0

while n >= 0:
    resto = binario % 10
    decimal = decimal + (resto * (2**i))
    n = n - 1
    i = i + 1
    binario = binario // 10

print(f'\nO número (binário) digitado {valor_digitado} na base decimal vale: {decimal}\n')