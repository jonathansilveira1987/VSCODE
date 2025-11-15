triangulo = int(input('\nDimensão do Triângulo Invertido: '))
def triangulo_invertido(linhas):
    for i in range(linhas, 0, -1):
        print(" *" * i)
print('\033[0;36m')
triangulo_invertido(triangulo)
print('\033[m')